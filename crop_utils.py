"""
crop_utils.py - helpers shared by all notebooks of the crop-suitability pipeline (1_SVM/...).

Lives at the project root, next to 00_config_and_inventory.ipynb (locally and on BDAP).
No data path is defined here: everything comes from config/config_<profile>.json, written by notebook 00.
Only pathlib / forward-slash paths are used, so the code runs unchanged on Linux (BDAP JupyterLab) and Windows.

Typical use at the top of a notebook (after BASE is found):
    sys.path.insert(0, str(BASE)); import crop_utils as cu
    CFG = cu.load_config()
    ERA5_DIR = cu.data_dir(CFG, "era5")              # folder of a dataset
    HWSD_TIF = cu.data_file(CFG, "hwsd_raster")      # one file
    files    = cu.data_files(CFG, "isimip_mri_ssp585", "pr")   # all files of one variable
"""
import glob
import json
import os
os.environ.setdefault("HDF5_USE_FILE_LOCKING", "FALSE")   # BDAP/EOS refuses HDF5 file locks ("NetCDF: HDF error")
import re
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent
CONFIG_DIR = PROJECT_ROOT / "config"

REQUIRED_PACKAGES = ["numpy", "pandas", "xarray", "netCDF4", "cftime", "scipy", "sklearn", "joblib",
                     "matplotlib", "rasterio", "regionmask", "geopandas", "shapely", "openpyxl"]


# --------------------------------------------------------------------------
# 1. Configuration
# --------------------------------------------------------------------------
def on_bdap():
    return Path("/eos/jeodpp").exists()


def profile():
    return "bdap" if on_bdap() else "local"


def find_config(path=None):
    """Locate config_<profile>.json written by notebook 00 (or the CROP_CONFIG environment variable)."""
    if path:
        return Path(path)
    if os.environ.get("CROP_CONFIG"):
        return Path(os.environ["CROP_CONFIG"])
    p = CONFIG_DIR / f"config_{profile()}.json"
    if p.exists():
        return p
    raise FileNotFoundError(f"{p} not found. Run 00_config_and_inventory.ipynb first (or set CROP_CONFIG).")


def load_config(path=None, verbose=True):
    p = find_config(path)
    cfg = json.loads(p.read_text(encoding="utf-8"))
    cfg["_config_file"] = str(p)
    if verbose:
        print(f"Config: {p}  (profile = {cfg['profile']})")
    return cfg


# --------------------------------------------------------------------------
# 2. Dataset paths
# --------------------------------------------------------------------------
def _patterns(cfg, name, var=None):
    """Pattern(s) of one dataset; `var` = one of its variables (None = first one / no variable)."""
    pats = cfg["datasets"][name]["patterns"]
    key = var if var is not None else next(iter(pats))
    p = pats[key]
    return p if isinstance(p, list) else [p]


def is_filled(pattern):
    return bool(pattern) and "TO_FILL" not in pattern


def data_files(cfg, name, var=None):
    """All files of a dataset (and variable), sorted; [] while the pattern is still TO_FILL."""
    pats = _patterns(cfg, name, var)
    if not all(is_filled(p) for p in pats):
        return []
    return sorted(f for p in pats for f in glob.glob(p))


def data_file(cfg, name, var=None):
    """The single file of a dataset. While not found, returns the (non-existing) pattern itself, so that
    `.exists()` is False and any read fails with a message that shows the path to fill in."""
    files = data_files(cfg, name, var)
    if len(files) > 1:
        raise ValueError(f"{name}: {len(files)} files match {_patterns(cfg, name, var)} but one is expected:\n  "
                         + "\n  ".join(files[:10]))
    return Path(files[0]) if files else Path(_patterns(cfg, name, var)[0])


def data_dir(cfg, name):
    """Folder of a dataset = the part of its pattern (with {var} still in it) before the first wildcard.
    While the pattern is still TO_FILL, returns it as is, so that any read fails showing what to fill in."""
    p = cfg["datasets"][name]["template"]
    p = p[0] if isinstance(p, list) else p
    if not is_filled(p):
        return Path(p)
    m = re.search(r"[*?\[{]", p)
    if not m:
        return Path(p).parent
    head = p[:m.start()]
    return Path(head) if head.endswith("/") else Path(head).parent


def hwsd_connect(path):
    """Connection to the HWSD v2 attribute database, for pandas.read_sql: HWSD2.sqlite (any platform, written from the
    .mdb by hwsd2_mdb_to_sqlite.py) or HWSD2.mdb (Windows only: pyodbc + Microsoft Access driver)."""
    path = Path(path)
    if path.suffix.lower() in (".sqlite", ".db"):
        import sqlite3
        return sqlite3.connect(f"file:{path.as_posix()}?mode=ro", uri=True)
    import pyodbc
    return pyodbc.connect(r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=" + str(path) + ";")


def out_dir(cfg, *parts):
    """Output folder <out_root>/<parts> (created if needed). out_root comes from the config (BDAP:
    .../elisa/Crop_suitability/outputs), one sub-folder per step: 0_masks_ecearth3, 1_biovariables/<variant>, ..."""
    d = Path(cfg.get("out_root") or PROJECT_ROOT / "outputs").joinpath(*parts)
    d.mkdir(parents=True, exist_ok=True)
    return d


# --------------------------------------------------------------------------
# 3. SVM grid = EC-Earth3 grid (0.7 deg, global)
# --------------------------------------------------------------------------
MASKS = "0_masks_ecearth3"   # out_dir(cfg, MASKS): land mask and MIRCA2000 masks of notebook 0.1


def lon180(lon):
    """Longitudes in [-180, 180)."""
    import numpy as np
    return ((np.asarray(lon, float) + 180.0) % 360.0) - 180.0


def _edges(c, lo=None, hi=None):
    import numpy as np
    c = np.asarray(c, float)
    e = np.concatenate([[c[0] - (c[1] - c[0]) / 2], (c[1:] + c[:-1]) / 2, [c[-1] + (c[-1] - c[-2]) / 2]])
    return e if lo is None else np.clip(e, lo, hi)


def svm_grid(cfg):
    """
    Grid of the SVM: the EC-Earth3 grid (0.7 deg, global), the grid of the ERA5 file regridded with CDO, of EC-Earth3
    historical and of the four runs. Read from an EC-Earth3 historical file: cell centres (lat ascending, lon in
    [-180, 180) ascending) and cell edges (lat from lat_bnds, lon halfway between centres).
    """
    import numpy as np
    import xarray as xr
    with xr.open_dataset(data_files(cfg, "gcm_historical", "tasmax")[0]) as ds:
        lat, lon = ds["lat"].values, ds["lon"].values
        lat_b = ds["lat_bnds"].values if "lat_bnds" in ds else None
    ol, lat = np.argsort(lat), np.sort(lat)
    if lat_b is not None:
        b = np.sort(lat_b[ol], axis=1)
        lat_e = np.concatenate([b[:, 0], b[-1:, 1]])
    else:
        lat_e = _edges(lat, -90.0, 90.0)
    lon = np.sort(lon180(lon))
    return {"lat": lat, "lon": lon, "lat_edges": lat_e, "lon_edges": _edges(lon)}


def cell_of(lat, lon, grid):
    """(i, j) of the SVM cell containing the points (lat, lon) (arrays of the same shape); longitude periodic."""
    import numpy as np
    lat = np.asarray(lat, float)
    lon = lon180(lon)
    lon = np.where(lon >= grid["lon_edges"][-1], lon - 360.0, lon)
    i = np.clip(np.searchsorted(grid["lat_edges"], lat, side="right") - 1, 0, grid["lat"].size - 1)
    j = np.clip(np.searchsorted(grid["lon_edges"], lon, side="right") - 1, 0, grid["lon"].size - 1)
    return i, j


def to_svm_grid(da, grid):
    """A climate field (ERA5 regridded, EC-Earth3 historical or a run) with lat ascending and lon in [-180, 180),
    checked to be on the SVM grid."""
    import numpy as np
    ren = {k: v for k, v in (("latitude", "lat"), ("longitude", "lon")) if k in da.dims}
    da = da.rename(ren) if ren else da
    da = da.assign_coords(lon=lon180(da["lon"].values)).sortby("lon").sortby("lat")
    if not (np.allclose(da["lat"].values, grid["lat"], atol=1e-3) and np.allclose(da["lon"].values, grid["lon"], atol=1e-3)):
        raise ValueError("not on the SVM (EC-Earth3) grid")
    return da.assign_coords(lat=grid["lat"], lon=grid["lon"])


def land_mask(cfg):
    """Land mask of the SVM grid (True = land), written by notebook 0.1."""
    import xarray as xr
    with xr.open_dataset(out_dir(cfg, MASKS) / "land_mask_ecearth3.nc") as ds:
        return ds["land_mask"].load() == 1


def crop_mask(cfg, crop):
    """MIRCA2000 no-threshold presence, harvested area and calendar of `crop` (e.g. 'Maize_rf'), notebook 0.1."""
    import xarray as xr
    with xr.open_dataset(out_dir(cfg, MASKS) / f"mirca2000_no_threshold_ecearth3_{crop}.nc") as ds:
        return ds.load()


def mirca_cropland(cfg):
    """MIRCA2000 cropland of the SVM grid (True = harvested area > 0 of any of the 26 classes), notebook 0.1: the
    background of the SVM training (absences only where other crops are grown)."""
    import xarray as xr
    with xr.open_dataset(out_dir(cfg, MASKS) / "mirca2000_any_crop_ecearth3.nc") as ds:
        return ds["cropland"].load() == 1


def _to_std_units(da, var):
    """degC for tasmax / tasmin, mm/day for pr, W m-2 for the radiation; error on unknown units."""
    u = str(da.attrs.get("units", "")).strip().lower().replace(" ", "").replace("**", "").replace("^", "")
    if var in ("tasmax", "tasmin"):
        if u in ("k", "kelvin"):
            return da - 273.15
        if u in ("degc", "c", "celsius", "degreec", "degrees_c", "°c"):
            return da
    elif var == "pr":
        if u in ("kgm-2s-1", "kg/m2/s", "mm/s"):
            return da * 86400.0
        if u in ("mm/day", "mm/d", "mmday-1", "mmd-1", "mm"):
            return da
        if u in ("m", "m/day"):
            return da * 1000.0
    else:   # radiation
        if u in ("wm-2", "w/m2"):
            return da
        if u in ("jm-2", "j/m2"):
            return da / 86400.0
    raise ValueError(f"{var}: unknown units '{da.attrs.get('units')}'")


def read_climate(cfg, name, var, grid, period=None):
    """
    Daily climate field of a dataset of the configuration (era5, gcm_historical, gcm_<period>_<run>) on the SVM grid:
    variable found through the aliases, units converted (degC, mm/day, W m-2), lat ascending, lon in [-180, 180),
    grid checked; files combined by coordinates (yearly files, and the northern / southern hemisphere files of the
    runs' pr). var = 'tasmax', 'tasmin', 'pr' or 'rad' (the dataset's radiation key, dswrf or ssrd). Lazy (dask).
    """
    import xarray as xr
    if var == "rad":
        var_key = next(v for v in cfg["datasets"][name]["vars"] if v in ("dswrf", "ssrd"))
    else:
        var_key = var
    files = data_files(cfg, name, var_key)
    if not files:
        raise FileNotFoundError(f"{name} / {var_key}: no file ({_patterns(cfg, name, var_key)})")
    ds = xr.open_mfdataset(files, combine="by_coords", chunks={"time": 366}, data_vars="minimal", coords="minimal",
                           compat="override")
    vname = next((a for a in cfg["aliases"].get(var_key, [var_key]) if a in ds.data_vars), None)
    if vname is None:
        raise KeyError(f"{name} / {var_key}: none of {cfg['aliases'].get(var_key)} in {list(ds.data_vars)}")
    std = {"tasmax": "degC", "tasmin": "degC", "pr": "mm/day", "rad": "W m-2"}[var]
    da = to_svm_grid(_to_std_units(ds[vname], var).rename(var).assign_attrs(units=std, source=name), grid)
    if period is not None:
        da = da.sel(time=slice(str(period[0]), str(period[1])))
    return da


def land_series(da, cells, years_per_block=1):
    """Values of a daily (time, lat, lon) field at the land cells (i, j) = cells, as a numpy array (time, n_cells),
    float32, read block of years by block of years (bounded memory)."""
    import numpy as np
    i, j = cells
    years = np.unique(da["time"].dt.year.values)
    out = []
    for k in range(0, years.size, years_per_block):
        sub = da.sel(time=slice(str(years[k]), str(years[min(k + years_per_block, years.size) - 1])))
        out.append(np.asarray(sub.values, dtype=np.float32)[:, i, j])
    return np.concatenate(out, axis=0)


# --------------------------------------------------------------------------
# 4. Environment
# --------------------------------------------------------------------------
def check_environment():
    """Print which required Python packages are available (call at the top of a notebook)."""
    import importlib
    missing = []
    for mod in REQUIRED_PACKAGES:
        try:
            m = importlib.import_module(mod)
            print(f"  ok       {mod:11s} {getattr(m, '__version__', '')}")
        except Exception:
            print(f"  MISSING  {mod}")
            missing.append(mod)
    if missing:
        names = {"sklearn": "scikit-learn"}
        print("\nInstall in your conda environment (or create it from environment.yml), e.g.:")
        print("  conda install -c conda-forge " + " ".join(names.get(m, m) for m in missing))
    return missing
