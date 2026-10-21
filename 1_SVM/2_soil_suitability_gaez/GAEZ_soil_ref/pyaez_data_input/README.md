# PyAEZ — donnees d'exemple (Laos, culture maïs)

Source : https://github.com/gicait/PyAEZ (branche `master`, commit `792e1d4231f6fa75beb98bbeed162a4fa9efbb56`,
2026-02-10), dossier `data_input/` — **sans** le sous-dossier `climate/` (donnees climatiques
brutes .npy, non recuperees, pas necessaires pour notre usage).

**Pourquoi ces fichiers sont ici** : jeu de donnees d'exemple complet (Laos, culture maïs)
utilise par les tutoriels PyAEZ (`NB1_ClimateRegime.ipynb`, `NB2_CropSimulation.ipynb`) —
utile comme reference concrete de parametres reels (terrain, sol, TSUM, regles specifiques
culture) en complement du code source dans `../pyaez_source/`. Pas utilise directement par
notre pipeline (nos propres donnees ERA5/HWSD2/SLOPE-MED restent la source), juste consultable
pour comparaison/verification si besoin.

## Fichiers

- `LAO_Admin.tif`, `LAO_Elevation.tif`, `LAO_Slope.tif`, `LAO_Soil.tif`,
  `LAO_soil_terrain_lulc.tif` : rasters d'entree (administration, elevation, pente, sol,
  occupation du sol) pour le Laos.
- `LAO_Maize_CropSuitability_rain.tiff` : sortie d'exemple (suitability maïs pluvial calculee
  par PyAEZ) — utile comme reference de sortie attendue.
- `crop-specific_rule_maiz_sugar.xlsx`, `input_crop_TSUM_parameters_maiz_sugar.xlsx` : regles
  et sommes de temperature specifiques maïs/canne a sucre.
- `maiz_fc3_irr_lst.xlsx`, `maiz_fc3_rain_lst.xlsx` : listes de parametres maïs (irrigue/pluvial).
- `maiz_soil_characteristics_topsoil.xlsx`, `maiz_soil_characteristics_subsoil.xlsx` :
  caracteristiques de sol (surface/sous-sol) pour maïs.
- `maiz_soil_params_irr.xlsx`, `maiz_soil_params_rain.xlsx` : parametres sol par regime
  d'irrigation.
- `maiz_terrain_constraints_irr.xlsx`, `maiz_terrain_constraints_rain.xlsx` : contraintes de
  terrain/pente par regime d'irrigation — a comparer avec notre propre table
  `../appendix_tables/terrain_slope_ratings_A6-8_parsed.csv` (meme concept, source GAEZ v4
  differente) si utile pour validation croisee du module terrain (4.d).
