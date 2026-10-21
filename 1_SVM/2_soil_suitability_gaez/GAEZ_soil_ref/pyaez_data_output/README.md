# PyAEZ — sorties de reference (Laos, culture maïs)

Source : https://github.com/gicait/PyAEZ (branche `master`, commit `792e1d4231f6fa75beb98bbeed162a4fa9efbb56`,
2026-02-10), dossier `data_output/`. Sorties attendues en executant les tutoriels
`NB1_ClimateRegime.ipynb` a `NB6_EconomicSuitability.ipynb` (voir `../pyaez_tutorials/`) sur
les donnees d'entree Laos (`../pyaez_data_input/`).

**Pourquoi ces fichiers sont ici** : references numeriques concretes pour une validation
croisee future -- ce ne sont pas nos propres resultats, mais les sorties que PyAEZ produit
reellement pour un jeu de donnees connu, utile pour comparer l'ordre de grandeur/la structure
de nos propres sorties (ex. `fournier_index.tif` de NB5 directement comparable au Fournier
calcule dans notre `4.d)_Build_TerrainSlopeSuitability.ipynb`, ou `LAO_LGP.tif`/`LAO_LGPt5.tif`
de NB1 comparables a notre `1.b)_Build_WaterBalance_LGP.ipynb`).

## Contenu par sous-dossier (correspond aux notebooks `../pyaez_tutorials/`)

- **NB1/** (48 fichiers) -- Module I complet : LGP (`LAO_LGP.tif`), LGP equivalent, LGPt0/5/10,
  profils de temperature (9 classes montantes A1-A9 + 9 descendantes B1-B9), climats/zones
  thermiques, sommes de temperature (TSUM0/5/10), indice de gel/permafrost, zones de culture
  multiple (irrigue/pluvial), AEZ, jachere -- + versions `.png` pour visualisation rapide.
- **NB2/** (6 fichiers) -- Module II : dates de semis, rendement maïs (irrigue/pluvial),
  facteurs de correction fc1/fc2.
- **NB3/** (4 fichiers) -- Module III : rendement climatique ajuste, facteur fc3.
- **NB4/** (4 fichiers) -- Module IV sol : rendement ajuste sol+climat (+ versions classees).
- **NB5/** (5 fichiers) -- Module IV terrain : **`fournier_index.tif`** (comparable
  directement a notre module terrain), rendement ajuste terrain+sol+climat.
- **NB6/** (6 fichiers) -- evaluation economique : revenu net (irrigue/pluvial, normalise,
  classe).
