"""
Helpers to run the FAO AquaCrop 7.3 stand-alone programme (KU Leuven build, github.com/KUL-RSDA/AquaCrop, release
v7.3_typofix) on grid cells: input files written from daily series, one project (PRM) per cell with one run per season,
execution in a work folder, seasonal results read back.

Layout of a work folder (the programme reads LIST/ListProjects.txt in its working directory):
    aquacrop(.exe)  LIST/  PARAM/  SIMUL/  OUTP/  DATA/
Paths written in the project files are relative ('./DATA/') because the programme splits the lines on blanks: the
work folder itself may contain blanks, the paths in the files may not.
"""
import os
import re
import shutil
import subprocess
from datetime import date, timedelta
from pathlib import Path

import numpy as np
import pandas as pd

AQ_VERSION = "7.3"
EPOCH = date(1901, 1, 1)                       # AquaCrop day number 1
SEP = "\\" if os.name == "nt" else "/"           # path separator inside the project files
EOL = "\r\n" if os.name == "nt" else "\n"        # end of line of the input files (README of the test case)
HERE = Path(__file__).resolve().parent
EXE = {"nt": HERE / "aquacrop-7.3-x86_64-windows" / "aquacrop-7.3-x86_64-windows" / "aquacrop.exe",
       "posix": HERE / "aquacrop-7.3-x86_64-linux" / "aquacrop-7.3-x86_64-linux" / "aquacrop"}[os.name]
# FAO crop (.CRO) and soil (.SOL) files of the standard programme: GUI_AC7.3/GUI_AC7.3/DATA when unpacked by
# ensure_installed (the archive has a top folder), GUI_AC7.3/DATA when unpacked by hand
DATABASE_CANDIDATES = (HERE / "GUI_AC7.3" / "GUI_AC7.3" / "DATA", HERE / "GUI_AC7.3" / "DATA")


def database():
    return next((p for p in DATABASE_CANDIDATES if p.exists()), DATABASE_CANDIDATES[0])

# HWSD v2 USDA texture class (D_TEXTURE_USDA) -> soil file of the AquaCrop database
HWSD_TEXTURE_TO_SOL = {1: "Clay.SOL", 2: "SiltyClay.SOL", 3: "Clay.SOL", 4: "SiltClayLoam.SOL", 5: "ClayLoam.SOL",
                       6: "Silt.SOL", 7: "SiltLoam.SOL", 8: "SandyClay.SOL", 9: "Loam.SOL", 10: "SandyClayLoam.SOL",
                       11: "SandyLoam.SOL", 12: "LoamySand.SOL", 13: "Sand.SOL"}

# programme parameters (PARAM/<project>.PPn): the defaults of the programme, as in the test case of the release
PROGRAM_PARAMETERS = """      4         : Evaporation decline factor for stage II
      1.10      : Ke(x) Soil evaporation coefficient for fully wet and non-shaded soil surface
      5         : Threshold for green CC below which HI can no longer increase (% cover)
     70         : Starting depth of root zone expansion curve (% of Zmin)
      5.00      : Maximum allowable root zone expansion (fixed at 5 cm/day)
     -6         : Shape factor for effect water stress on root zone expansion
     20         : Required soil water content in top soil for germination (% TAW)
      1.0       : Adjustment factor for FAO-adjustment soil water depletion (p) by ETo
      3         : Number of days after which deficient aeration is fully effective
      1.00      : Exponent of senescence factor adjusting drop in photosynthetic activity of dying crop
     12         : Decrease of p(sen) once early canopy senescence is triggered (% of p(sen))
     10         : Thickness top soil (cm) in which soil water depletion has to be determined
     30         : Depth [cm] of soil profile affected by water extraction by soil evaporation
      0.30      : Considered depth (m) of soil profile for calculation of mean soil water content for CN adjustment
      1         : CN is adjusted to Antecedent Moisture Class
     20         : Salt diffusion factor (capacity for salt diffusion in micro pores) [%]
    100         : Salt solubility [g/liter]
     16         : Shape factor for effect of soil water content gradient on capillary rise
     12.0       : Default minimum temperature (degC) if no temperature file is specified
     28.0       : Default maximum temperature (degC) if no temperature file is specified
      3         : Default method for the calculation of growing degree days
      1         : Daily rainfall is estimated by USDA-SCS procedure (when input is 10-day/monthly rainfall)
     70         : Percentage of effective rainfall (when input is 10-day/monthly rainfall)
      2         : Number of showers in a decade for run-off estimate (when input is 10-day/monthly rainfall)
      5         : Parameter for reduction of soil evaporation (when input is 10-day/monthly rainfall)"""


def daynr(d):
    """AquaCrop day number of a date (1 January 1901 = 1)."""
    return (d - EPOCH).days + 1


def date_of(n):
    return EPOCH + timedelta(days=int(n) - 1)


def _write(path, lines):
    Path(path).write_text(EOL.join(lines) + EOL, encoding="latin-1", newline="")


def _record_header(title, first):
    return [title,
            "     1  : Daily records (1=daily, 2=10-daily and 3=monthly data)",
            f"     {first.day}  : First day of record (1, 11 or 21 for 10-day or 1 for months)",
            f"     {first.month}  : First month of record",
            f"  {first.year}  : First year of record (1901 if not linked to a specific year)",
            ""]


def write_climate(folder, name, first, tmin, tmax, eto, rain, co2_file="MaunaLoa.CO2", title=None):
    """Daily Tnx, ETo and PLU files and the CLI file <name>.* in folder (series start on the date `first`, every
    calendar day, 29 February included). Returns the file names."""
    folder = Path(folder)
    title = title or name
    tmin, tmax, eto, rain = (np.asarray(x, float) for x in (tmin, tmax, eto, rain))
    assert tmin.size == tmax.size == eto.size == rain.size
    assert np.isfinite(tmin).all() and np.isfinite(tmax).all() and np.isfinite(eto).all() and np.isfinite(rain).all()
    _write(folder / f"{name}.Tnx", _record_header(title, first) + ["  Tmin (C)   TMax (C)", "========================"]
           + [f"{a:.1f}\t{b:.1f}" for a, b in zip(tmin, np.maximum(tmax, tmin))])
    _write(folder / f"{name}.ETo", _record_header(title, first) + ["  Average ETo (mm/day)", "======================="]
           + [f"{max(x, 0.0):.1f}" for x in eto])
    _write(folder / f"{name}.PLU", _record_header(title, first) + ["  Total Rain (mm)", "======================="]
           + [f"{max(x, 0.0):.1f}" for x in rain])
    _write(folder / f"{name}.CLI", [title, f" {AQ_VERSION}  : AquaCrop Version (January 2026)",
                                    f"{name}.Tnx", f"{name}.ETo", f"{name}.PLU", co2_file])
    return {"cli": f"{name}.CLI", "tnx": f"{name}.Tnx", "eto": f"{name}.ETo", "plu": f"{name}.PLU", "co2": co2_file}


def _ref(fname, folder):
    if fname is None:
        return ["   (None)", "   (None)"]
    return [f"   {fname}", f"   '.{SEP}{folder}{SEP}'"]


def write_project(path, title, runs, files, crop_file, soil_file):
    """Project file (PRM) with one run per season. runs: list of dicts with sim1, simN, crop1, cropN (day numbers)
    and keep (True: soil water carried over from the end of the previous run, 'KeepSWC'; False: field capacity at the
    start of the run). files: the climate file names of write_climate (in DATA/; the CO2 file in SIMUL/)."""
    lines = [title, f"      {AQ_VERSION}  : AquaCrop Version (January 2026)"]
    for k, r in enumerate(runs):
        lines += [f"      {1}         : Year number of cultivation (Seeding/planting year)",
                  f"  {r['sim1']}         : First day of simulation period - {date_of(r['sim1']):%d %B %Y}",
                  f"  {r['simN']}         : Last day of simulation period - {date_of(r['simN']):%d %B %Y}",
                  f"  {r['crop1']}         : First day of cropping period - {date_of(r['crop1']):%d %B %Y}",
                  f"  {r['cropN']}         : Last day of cropping period - {date_of(r['cropN']):%d %B %Y}",
                  "-- 1. Climate (CLI) file", *_ref(files["cli"], "DATA"),
                  "   1.1 Temperature (Tnx or TMP) file", *_ref(files["tnx"], "DATA"),
                  "   1.2 Reference ET (ETo) file", *_ref(files["eto"], "DATA"),
                  "   1.3 Rain (PLU) file", *_ref(files["plu"], "DATA"),
                  "   1.4 Atmospheric CO2 concentration (CO2) file", *_ref(files["co2"], "SIMUL"),
                  "-- 2. Calendar (CAL) file", *_ref(None, None),
                  "-- 3. Crop (CRO) file", *_ref(crop_file, "DATA"),
                  "-- 4. Irrigation management (IRR) file", *_ref(None, None),
                  "-- 5. Field management (MAN) file", *_ref(None, None),
                  "-- 6. Soil profile (SOL) file", *_ref(soil_file, "DATA"),
                  "-- 7. Groundwater table (GWT) file", *_ref(None, None),
                  "-- 8. Initial conditions (SW0) file",
                  *(["   KeepSWC", "   (None)"] if (r.get("keep") and k > 0) else _ref(None, None)),
                  "-- 9. Off-season conditions (OFF) file", *_ref(None, None),
                  "-- 10. Field data (OBS) file", *_ref(None, None)]
    _write(path, lines)


RELEASE = "https://github.com/KUL-RSDA/AquaCrop/releases/download/v7.3_typofix"


def ensure_installed():
    """Downloads and unpacks the AquaCrop 7.3 release of KU Leuven (stand-alone of this system, standard programme with
    the FAO database) next to this module when they are missing (they are not in git)."""
    import urllib.request
    import zipfile
    need = {"aquacrop-7.3-x86_64-windows" if os.name == "nt" else "aquacrop-7.3-x86_64-linux": lambda: EXE, "GUI_AC7.3": database}
    for name, target in need.items():
        if target().exists():
            continue
        z = HERE / "downloads_v7.3" / f"{name}.zip"
        z.parent.mkdir(exist_ok=True)
        if not z.exists():
            print(f"downloading {RELEASE}/{name}.zip")
            urllib.request.urlretrieve(f"{RELEASE}/{name}.zip", z)
        with zipfile.ZipFile(z) as zf:
            assert not [n for n in zf.namelist() if n.startswith("/") or ".." in n], f"unsafe paths in {z}"
            zf.extractall(HERE / name)
        assert target().exists(), f"{target()} not found after unpacking {z}"


def make_workdir(work, database_files=()):
    """Work folder for the programme: executable, LIST, PARAM, SIMUL (CO2 file and output settings of the release),
    OUTP, DATA with the crop and soil files of the FAO database listed. Existing results are removed."""
    ensure_installed()
    work = Path(work)
    for d in ("LIST", "PARAM", "SIMUL", "OUTP", "DATA"):
        (work / d).mkdir(parents=True, exist_ok=True)
    shutil.copy2(EXE, work / EXE.name)
    if os.name == "posix":
        (work / EXE.name).chmod(0o755)
    for f in (EXE.parent / "SIMUL").iterdir():
        shutil.copy2(f, work / "SIMUL" / f.name)
    for f in list((work / "OUTP").iterdir()) + list((work / "LIST").iterdir()) + list((work / "DATA").iterdir()):
        f.unlink()                                       # results and inputs of a previous use of the folder
    for f in database_files:
        shutil.copy2(database() / f, work / "DATA" / f)
    return work


def run_projects(work, projects, timeout=3600):
    """Writes LIST/ListProjects.txt and the program parameters of each project, runs the programme in `work`, returns
    the lines of OUTP/ListProjectsLoaded.OUT (one per project) and raises if a project was not loaded."""
    work = Path(work)
    _write(work / "LIST" / "ListProjects.txt", list(projects))
    for p in projects:
        _write(work / "PARAM" / (p[:-3] + "PPn"), PROGRAM_PARAMETERS.splitlines())
    for f in (work / "OUTP").iterdir():
        f.unlink()
    res = subprocess.run([str(work / EXE.name)], cwd=work, capture_output=True, text=True, timeout=timeout)
    log = (work / "OUTP" / "ListProjectsLoaded.OUT").read_text(encoding="latin-1", errors="replace")
    bad = [l.strip() for l in log.splitlines() if "NOT loaded" in l]
    if bad or res.returncode != 0:
        raise RuntimeError(f"AquaCrop: return code {res.returncode}; {bad[:5]}; stdout: {res.stdout[-500:]}")
    return log


def run_cells(work_root, cells, write_inputs, database_files, n_workers=4, timeout=120):
    """Runs one project per cell in parallel, each worker in its own work folder <work_root>/w<k> (inputs written there
    by write_inputs(work, cell) -> project file name), one programme call per cell with a timeout (a cell that does not
    finish is reported, the others go on). Returns {cell: seasonal DataFrame or None} and the list of the cells that
    timed out."""
    import concurrent.futures as cf
    import queue
    works = queue.Queue()
    for k in range(n_workers):
        works.put(make_workdir(Path(work_root) / f"w{k}", database_files))
    out, timed_out = {}, []

    def one(cell):
        work = works.get()
        try:
            prm = write_inputs(work, cell)
            try:
                run_projects(work, [prm], timeout=timeout)
            except subprocess.TimeoutExpired:
                timed_out.append(cell)
                return cell, None
            return cell, read_season(work / "OUTP" / f"{prm[:-4]}PRMseason.OUT")
        finally:
            for f in list((work / "DATA").glob(f"{prm[:-4]}.*")) + [work / "LIST" / prm, work / "PARAM" / (prm[:-3] + "PPn")]:
                f.unlink(missing_ok=True)                   # inputs of the cell (the results are read above)
            works.put(work)

    with cf.ThreadPoolExecutor(max_workers=n_workers) as ex:
        for cell, df in ex.map(one, list(cells)):
            out[cell] = df
    return out, timed_out


def crop_gdd_parameters(crop_file):
    """Base and upper temperature and growing degree-days from sowing to maturity of a crop file (GDD mode)."""
    ensure_installed()
    lines = (database() / crop_file).read_text(encoding="latin-1").replace(chr(13), "").splitlines()
    val = lambda key: float(next(l for l in lines if key in l).split(":")[0].split()[0])
    return {"tbase": val("Base temperature"), "tupper": val("Upper temperature"),
            "gdd_maturity": val("GDDays: from sowing to maturity")}


# growing degree-day durations of a crop file (GDD mode) scaled together for a cultivar of another cycle length;
# emergence is kept (seed physiology), the canopy coefficients per degree-day are scaled inversely
GDD_DURATIONS = ("Total length of crop cycle in growing degree-days", "GDDays: from sowing to maximum rooting depth",
                 "GDDays: from sowing to start senescence", "GDDays: from sowing to maturity",
                 "GDDays: from sowing to flowering", "Length of the flowering stage (growing degree days)",
                 "GDDays: building-up of Harvest Index")
GDD_RATES = ("CGC for GGDays", "CDC for GGDays")


def write_crop_variant(crop_file, path, gdd_maturity, title=None):
    """Copy of a crop file of the FAO database with the cycle length set to gdd_maturity growing degree-days: every
    degree-day duration but emergence scaled by f = gdd_maturity / original maturity, the canopy growth and decline
    coefficients per degree-day divided by f (same canopy course in relative time). Returns f."""
    ensure_installed()
    lines = (database() / crop_file).read_text(encoding="latin-1").replace(chr(13), "").splitlines()
    f = gdd_maturity / crop_gdd_parameters(crop_file)["gdd_maturity"]
    out = []
    for k, l in enumerate(lines):
        if k == 0 and title:
            l = title
        elif any(key in l for key in GDD_DURATIONS):
            v, rest = l.split(":", 1)
            l = f"  {int(round(float(v) * f)):4d}         :{rest}"
        elif any(key in l for key in GDD_RATES):
            v, rest = l.split(":", 1)
            l = f"     {float(v) / f:.6f}  :{rest}"
        out.append(l)
    _write(path, out)
    return f


def daily_gdd(tmin, tmax, tbase, tupper):
    """Growing degree-days of each day, AquaCrop method 3 (default of the programme parameters): Tmax and Tmin bounded
    by Tupper, Tmax by Tbase from below, mean bounded by Tbase."""
    tx = np.maximum(np.minimum(tmax, tupper), tbase)
    tn = np.minimum(tmin, tupper)
    return np.maximum((tx + tn) / 2 - tbase, 0.0)


def read_season(path):
    """Seasonal results (<project>PRMseason.OUT) as a DataFrame, one row per run (columns as in the file header,
    plus sowing / end dates)."""
    text = Path(path).read_text(encoding="latin-1", errors="replace").replace("\r", "").splitlines()
    head = next(l for l in text if l.strip().startswith("RunNr")).split()
    rows = []
    for l in text:
        if l.strip().startswith("Tot("):
            run = int(re.search(r"Tot\((\d+)\)", l).group(1))
            vals = l.split(")", 1)[1].split()
            rows.append([run] + [float(x) for x in vals[:len(head) - 1]] + [" ".join(vals[len(head) - 1:])])
    df = pd.DataFrame(rows, columns=head + ["project"])
    if len(df):
        df["start"] = [date(int(y), int(m), int(d)) for d, m, y in zip(df["Day1"], df["Month1"], df["Year1"])]
        if {"DayN", "MonthN", "YearN"} <= set(df.columns):
            df["end"] = [date(int(y), int(m), int(d)) for d, m, y in zip(df["DayN"], df["MonthN"], df["YearN"])]
    return df


# ---------------------------------------------------------------------------------------------------------------------
# Soil profiles from HWSD v2 layers: Saxton & Rawls (2006) pedotransfer functions, AquaCrop rules for the other fields
# ---------------------------------------------------------------------------------------------------------------------
# HWSD v2 layers D1..D7 (cm) grouped into the (at most 5) horizons of an AquaCrop soil file
HWSD_HORIZONS = [("D1",), ("D2",), ("D3", "D4"), ("D5", "D6"), ("D7",)]


def saxton_rawls(sand, clay, om, bd=None):
    """Saxton & Rawls (2006, Soil Sci. Soc. Am. J. 70, 1569) for the fine earth: sand, clay (weight fractions), organic
    matter (weight %), optional bulk density (g cm-3, density adjustment with DF = bd / normal density, clipped to
    0.9-1.3 as in the paper). Returns saturation, field capacity (33 kPa), wilting point (1500 kPa) (volume fractions)
    and the saturated conductivity (mm/day)."""
    S, C, OM = float(sand), float(clay), float(min(max(om, 0.0), 8.0))     # equations fitted for OM <= 8 %
    t1500t = -0.024 * S + 0.487 * C + 0.006 * OM + 0.005 * S * OM - 0.013 * C * OM + 0.068 * S * C + 0.031
    t1500 = t1500t + (0.14 * t1500t - 0.02)
    t33t = -0.251 * S + 0.195 * C + 0.011 * OM + 0.006 * S * OM - 0.027 * C * OM + 0.452 * S * C + 0.299
    t33 = t33t + (1.283 * t33t ** 2 - 0.374 * t33t - 0.015)
    ts33t = 0.278 * S + 0.034 * C + 0.022 * OM - 0.018 * S * OM - 0.027 * C * OM - 0.584 * S * C + 0.078
    ts33 = ts33t + (0.636 * ts33t - 0.107)
    tS = t33 + ts33 - 0.097 * S + 0.043
    if bd is not None and np.isfinite(bd) and bd > 0:
        rhoN = (1 - tS) * 2.65
        DF = min(max(bd / rhoN, 0.9), 1.3)
        tS_df = 1 - rhoN * DF / 2.65
        t33 = t33 - 0.2 * (tS - tS_df)
        tS = tS_df
    t1500 = min(t1500, t33 - 0.01)
    B = (np.log(1500) - np.log(33)) / (np.log(t33) - np.log(t1500))
    ks = 1930 * max(tS - t33, 1e-4) ** (3 - 1 / B)                       # mm/h
    return tS, t33, t1500, 24 * ks


def usda_class(sand, silt, clay):
    """USDA texture class of the fine earth (percentages), as the soil textural triangle."""
    s, si, c = sand, silt, clay
    if si + 1.5 * c < 15:
        return "Sand"
    if si + 2 * c < 30:
        return "LoamySand"
    if (7 <= c < 20 and s > 52 and si + 2 * c >= 30) or (c < 7 and si < 50 and si + 2 * c >= 30):
        return "SandyLoam"
    if 7 <= c < 27 and 28 <= si < 50 and s <= 52:
        return "Loam"
    if (si >= 50 and 12 <= c < 27) or (50 <= si < 80 and c < 12):
        return "SiltLoam"
    if si >= 80 and c < 12:
        return "Silt"
    if 20 <= c < 35 and si < 28 and s > 45:
        return "SandyClayLoam"
    if 27 <= c < 40 and 20 < s <= 45:
        return "ClayLoam"
    if 27 <= c < 40 and s <= 20:
        return "SiltClayLoam"
    if c >= 35 and s > 45:
        return "SandyClay"
    if c >= 40 and si >= 40:
        return "SiltyClay"
    return "Clay"


# AquaCrop capillary-rise parameters per group of textures (checked on the 12 soils of the FAO database)
CR_GROUP = {"Sand": "sandy", "LoamySand": "sandy", "SandyLoam": "sandy", "Loam": "loamy", "SiltLoam": "loamy",
            "Silt": "loamy", "SandyClayLoam": "sandyclay", "SandyClay": "sandyclay", "ClayLoam": "sandyclay",
            "SiltClayLoam": "siltyclay", "SiltyClay": "siltyclay", "Clay": "siltyclay"}
CR_PARAMS = {"sandy": (-0.3112, -1e-5, -1.4936, 0.2416), "loamy": (-0.4986, 9e-5, -2.132, 0.4778),
             "sandyclay": (-0.5677, -4e-5, -3.7189, 0.5922), "siltyclay": (-0.6366, 8e-4, -1.9165, 0.7063)}


def aquacrop_cn(ksat_top):
    """Curve number from the saturated conductivity of the top horizon (mm/day), as the AquaCrop database."""
    return 46 if ksat_top > 864 else 61 if ksat_top > 347 else 72 if ksat_top > 36 else 77


def aquacrop_rew(fc_pct, wp_pct):
    """Readily evaporable water (mm) of the top layer, as the AquaCrop database: 10 (FC - WP/2) 0.04."""
    return int(round(10 * (fc_pct - wp_pct / 2) * 0.04))


def gravel_mass_pct(coarse_vol_pct, bd_fine):
    """HWSD coarse fragments (% of the volume) -> AquaCrop gravel (% of the mass), mineral density 2.65."""
    v = min(max(coarse_vol_pct, 0.0), 90.0) / 100
    if v <= 0 or not np.isfinite(bd_fine) or bd_fine <= 0:
        return 0
    return int(round(100 * v * 2.65 / (v * 2.65 + (1 - v) * bd_fine)))


def hwsd_profile(layers):
    """AquaCrop horizons from the HWSD v2 layers of one soil component (DataFrame with LAYER, TOPDEP, BOTDEP, SAND,
    SILT, CLAY, ORG_CARBON, BULK, COARSE). Layers are used down to the first one without texture (shallow soils end
    there); the layers of a horizon are averaged by thickness. Returns a list of dicts (thickness m, sat, fc, wp in
    vol %, ksat mm/day, gravel mass %, texture class)."""
    L = layers.set_index("LAYER")
    below_rock = lambda r: float(r["SAND"]) == -7                  # HWSD v2: -7 = not applicable (below the bedrock)
    ok = lambda r: all(np.isfinite(float(r[k])) and float(r[k]) >= 0 for k in ("SAND", "SILT", "CLAY")) and float(r["SAND"]) + float(r["CLAY"]) > 0
    out = []
    for group in HWSD_HORIZONS:
        rows = [L.loc[g] for g in group if g in L.index and ok(L.loc[g])]
        if len(rows) < len(group) and not rows:
            if any(g in L.index and below_rock(L.loc[g]) for g in group) and out:
                out[-1]["rock_below"] = True
            break
        th = np.array([float(r["BOTDEP"]) - float(r["TOPDEP"]) for r in rows]) / 100.0
        w = th / th.sum()
        avg = lambda k, default=np.nan: float(np.nansum([w[i] * (float(r[k]) if r[k] is not None and float(r[k]) >= 0 else default)
                                                          for i, r in enumerate(rows)]))
        sand, silt, clay = avg("SAND"), avg("SILT"), avg("CLAY")
        tot = sand + silt + clay
        sand, silt, clay = 100 * sand / tot, 100 * silt / tot, 100 * clay / tot
        om = 1.724 * avg("ORG_CARBON", 0.0)
        bd = avg("BULK") if all(r["BULK"] is not None and float(r["BULK"]) > 0 for r in rows) else None
        sat, fc, wp, ks = saxton_rawls(sand / 100, clay / 100, om, bd)
        out.append({"thickness": float(th.sum()), "sat": 100 * sat, "fc": 100 * fc, "wp": 100 * wp, "ksat": ks,
                    "gravel": gravel_mass_pct(avg("COARSE", 0.0), bd if bd else 1.4), "texture": usda_class(sand, silt, clay),
                    "sand": sand, "clay": clay, "om": om})
        if len(rows) < len(group):
            out[-1]["rock_below"] = any(g in L.index and below_rock(L.loc[g]) for g in group)
            break
    return out


def write_soil(path, title, horizons, depth=2.0):
    """AquaCrop soil file (.SOL) of the horizons of hwsd_profile: CN and readily evaporable water from the top
    horizon, capillary-rise parameters per texture group, penetrability 100 %. Where HWSD has the bedrock below the
    last horizon (rock_below), a horizon down to `depth` m with penetrability 0 % is added: the restrictive layer of
    AquaCrop, which stops the roots (the thickness of the horizons alone does not limit them)."""
    top = horizons[0]
    horizons = [dict(h, pen=100) for h in horizons]
    z = sum(h["thickness"] for h in horizons)
    if horizons[-1].get("rock_below") and z < depth - 1e-6:
        horizons.append(dict(horizons[-1], thickness=depth - z, pen=0, rock_below=False))
    lines = [title, f"        {AQ_VERSION}  : AquaCrop Version (January 2026)",
             f"       {aquacrop_cn(top['ksat'])}                   : CN (Curve Number)",
             f"        {aquacrop_rew(top['fc'], top['wp'])}                   : Readily evaporable water from top layer (mm)",
             f"        {len(horizons)}                   : number of soil horizons",
             "       -9                   : variable no longer applicable",
             "  Thickness  Sat   FC    WP     Ksat   Penetrability  Gravel  CRa       CRb           description",
             "  ---(m)-   ----(vol %)-----  (mm/day)      (%)        (%)    -----------------------------------------"]
    for h in horizons:
        a0, a1, b0, b1 = CR_PARAMS[CR_GROUP[h["texture"]]]
        cra, crb = a0 + a1 * h["ksat"], b0 + b1 * np.log(h["ksat"])
        lines.append(f"    {h['thickness']:.2f}    {h['sat']:.1f}  {h['fc']:.1f}  {h['wp']:.1f}  {h['ksat']:.1f}        {h['pen']:d}"
                     f"        {h['gravel']:d}     {cra:.6f}  {crb:.6f}   {h['texture']}")
    _write(path, lines)


def compute_Ra(lat_rad, doy):
    # extraterrestrial radiation (MJ m-2 day-1), FAO-56 eq. 21 (as 11.a)
    Gsc = 0.0820
    dr = 1 + 0.033 * np.cos(2 * np.pi / 365 * doy)
    delta = 0.409 * np.sin(2 * np.pi / 365 * doy - 1.39)
    ws = np.arccos(np.clip(-np.tan(lat_rad) * np.tan(delta), -1, 1))
    return (24 * 60 / np.pi) * Gsc * dr * (ws * np.sin(lat_rad) * np.sin(delta) + np.cos(lat_rad) * np.cos(delta) * np.sin(ws))


def eto_hargreaves(tx, tn, lat_deg, doy):
    """Hargreaves reference evapotranspiration (mm/day), as compute_ETo_day of 1.1.d and 11.a."""
    tm = (tx + tn) / 2.0
    return 0.0023 * compute_Ra(np.radians(lat_deg), doy) / (2.501 - 0.002361 * tm) * (tm + 17.8) * np.sqrt(np.maximum(tx - tn, 0.0))
