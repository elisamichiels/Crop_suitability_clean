"""Real GAEZ v4 Appendix 6-3 (rainfed) / 6-4 (irrigated, gravity) SQ1-SQ7 + Soil Rating (L/I/H)
engine. Column offsets verified against the appendix workbook's own header rows and cross-checked
against PyAEZ's reference code (pyaez/SoilConstraints.py) and its bundled maize parameter tables,
which match the appendix's rainfed maize row exactly (see design notes in 2.a).

Simplifications, documented: soil-phase (SPH) sub-factors reuse this pipeline's existing
Sys-1993-derived severe-phase exclusion set (SEVERE_PHASE_SQ) rather than the appendix's own
939-row phase tables (A6-3.4/5/6); Vertic (VSP) uses a simple present/absent rule; SQ2's
sub-factors always use the appendix's 'High'-input column (matches PyAEZ's reference code, which
computes SQ2 once and reuses it for both the Intermediate and High Soil-Rating formulas); SQ3's
root-depth curve likewise always uses the 'High' column, also matching PyAEZ.
"""
from pathlib import Path

import numpy as np
import openpyxl

# project root = two levels above this file (1_SVM/2_soil_suitability/)
APP = Path(__file__).resolve().parents[2] / "0_Input_data" / "gaez" / "docs" / "GAEZv4_Appendices.xlsx"

COLS = dict(SOC=range(3, 9), pH_IL=range(9, 15), pH_H=range(15, 21), TEB=range(33, 39),
            CECa_H=range(45, 51), BS_H=range(57, 63), RC=range(63, 69), CF=range(75, 81),
            EC=range(81, 87), ESP=range(87, 93), CCB=range(93, 99), GYP=range(99, 105),
            CECs_H=range(117, 123))
FCT6 = [100, 90, 70, 50, 30, 10]

_TEX_CLASSES = ['Clay (heavy)', 'Silty clay', 'Clay (light)', 'Silty clay loam', 'Clay loam', 'Silt',
                'Silt loam', 'Sandy clay', 'Loam', 'Sandy clay loam', 'Sandy loam', 'Loamy sand', 'Sand']
_DRG_MAP = {'VP': 'Very Poor', 'P': 'Poor', 'I': 'Imperfectly', 'MW': 'Moderately well',
            'W': 'Well', 'SE': 'Somewhat excessive', 'E': 'Excessive'}

SEVERE_PHASE_SQ = {'Saline', 'Sodic', 'Lithic', 'Petric', 'Petrocalcic', 'Petrogypsic',
                    'Petroferric', 'Fragipan', 'Duripan', 'Glaciers', 'Flooded'}


def load_crop_params(chem_sheet, texture_sheet, drainage_sheet, crop_name, drg_level='High',
                      drg_texgroup='Medium textures'):
    """One crop's full parameter set, straight from the official GAEZ v4 appendix workbook."""
    wb = openpyxl.load_workbook(APP, data_only=True)
    rows = {s: list(wb[s].iter_rows(values_only=True)) for s in {chem_sheet, texture_sheet, drainage_sheet}}

    chem_row = next(r for r in rows[chem_sheet] if r[2] == crop_name)
    curves = {k: ([chem_row[c] for c in rng], FCT6[:len(rng)]) for k, rng in COLS.items()}

    tex_row = next(r for r in rows[texture_sheet] if r[2] == crop_name)
    texture = dict(zip(_TEX_CLASSES, tex_row[3:16]))

    hdr_lvl = list(rows[drainage_sheet][3]); hdr_tex = list(rows[drainage_sheet][4])
    hdr_cls = rows[drainage_sheet][5]
    for j in range(3, len(hdr_lvl)):
        if hdr_lvl[j] is None: hdr_lvl[j] = hdr_lvl[j - 1]
        if hdr_tex[j] is None: hdr_tex[j] = hdr_tex[j - 1]
    drg_row = next(r for r in rows[drainage_sheet] if r[2] == crop_name)
    drg_raw = {}
    for j in range(3, len(hdr_lvl)):
        if hdr_lvl[j] == drg_level and hdr_tex[j] and hdr_tex[j].strip() == drg_texgroup and hdr_cls[j]:
            drg_raw[hdr_cls[j].strip()] = drg_row[j]
    drainage = {code: drg_raw.get(label) for code, label in _DRG_MAP.items()}

    return {'curves': curves, 'texture': texture, 'drainage': drainage}


def interp_num(val, val_fct):
    val_list, fct_list = val_fct
    xp = np.asarray(val_list, float); fp = np.asarray(fct_list, float)
    ok = np.isfinite(xp) & (xp < 900) & np.isfinite(fp)
    xp, fp = xp[ok], fp[ok]
    order = np.argsort(xp)
    return np.interp(val, xp[order], fp[order]) / 100.0


def lookup_cat(series, mapping, default=1.0):
    m = {k: (v / 100.0 if v is not None else default) for k, v in mapping.items()}
    return series.map(m).fillna(default)


def rate_gaez(comp, params):
    """comp: the 2.a) component-level dataframe (HWSD2 attributes). Returns a dict of numpy arrays
    (SQ1..SQ7, SR_low, SR_int, SR_high), aligned with comp.index."""
    c = params['curves']
    txt = lookup_cat(comp['texture'], params['texture'])
    sph_ls = comp['phase1'].where(comp['phase1'].isin(['Lithic', 'Skeletic']), comp['phase2'])
    sph3 = lookup_cat(sph_ls, {'Lithic': 50, 'Skeletic': 75})
    sph_other = lookup_cat(sph_ls, {'Lithic': 50, 'Skeletic': 60})
    hard = (comp['phase1'].isin(SEVERE_PHASE_SQ) | comp['phase2'].isin(SEVERE_PHASE_SQ)
            | (comp['add_prop'] == 'Gelic'))

    oc = interp_num(comp['ORG_CARBON'].fillna(0).values, c['SOC'])
    ph1 = interp_num(comp['PH_WATER'].values, c['pH_IL'])
    ph2 = interp_num(comp['PH_WATER'].values, c['pH_H'])
    teb = interp_num(comp['TEB'].values, c['TEB'])
    ceca = interp_num(comp['CEC_CLAY'].values, c['CECa_H'])
    cecs = interp_num(comp['CEC_SOIL'].values, c['CECs_H'])
    bs = interp_num(comp['BSAT'].values, c['BS_H'])
    rc = interp_num(comp['rsd_cm'].values, c['RC'])
    cf = interp_num(comp['COARSE'].values, c['CF'])
    ec = interp_num(comp['ELEC_COND'].values, c['EC'])
    esp = interp_num(comp['ESP'].values, c['ESP'])
    ccb = interp_num(comp['TCARBON_EQ'].values, c['CCB'])
    gyp = interp_num(comp['GYPSUM'].values, c['GYP'])
    vsp = lookup_cat(comp['add_prop'], {'Vertic': 90}, default=100 / 100.0)
    drg = lookup_cat(comp['DRAINAGE'], params['drainage'])

    def blend(stack):
        m = stack.min(axis=0)
        return (m + (stack.sum(axis=0) - m) / (stack.shape[0] - 1)) / 2.0

    SQ1 = np.where(hard, 0.0, blend(np.stack([txt.values, oc, ph1, teb])))
    SQ2 = np.where(hard, 0.0, blend(np.stack([txt.values, bs, ceca, cecs, ph2])))
    SQ3 = np.where(hard, 0.0, rc * np.minimum(sph3.values, 1.0))
    SQ4 = np.where(hard, 0.0, np.minimum(drg.values, sph_other.values))
    SQ5 = np.where(hard, 0.0, np.minimum(esp * ec, sph_other.values))
    SQ6 = np.where(hard, 0.0, np.minimum(ccb * gyp, sph_other.values))
    SQ7 = np.where(hard, 0.0, blend(np.stack([rc, cf, sph3.values, txt.values, vsp.values])))

    fsq_stack = np.stack([SQ4, SQ5, SQ6, SQ7])
    fsq = (fsq_stack.min(axis=0) + fsq_stack.sum(axis=0) / 3) / 2
    SR_low = SQ1 * SQ3 * fsq
    SR_high = SQ2 * SQ3 * fsq
    SR_int = 0.5 * (SQ1 + SQ2) * SQ3 * fsq

    out = dict(SQ1=SQ1, SQ2=SQ2, SQ3=SQ3, SQ4=SQ4, SQ5=SQ5, SQ6=SQ6, SQ7=SQ7,
               SR_low=SR_low, SR_int=SR_int, SR_high=SR_high)
    for k in out:
        out[k] = np.where(comp['texture'].isna().values, np.nan, out[k])
    return out
