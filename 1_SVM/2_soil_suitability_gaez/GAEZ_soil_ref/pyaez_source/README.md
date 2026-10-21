# PyAEZ — code source de reference (telecharge, non installe comme package)

Source : https://github.com/gicait/PyAEZ (branche `master`, commit `792e1d4231f6fa75beb98bbeed162a4fa9efbb56`,
2026-02-10), dossier `pyaez/`. Auteurs : Geoinformatics Center, Asian Institute of Technology,
Thailand (geoinfo@ait.asia). Version `2.2` (Dec 2023, cf. `__version__.py` et en-tete de
`LGPCalc.py`).

**Pourquoi ces fichiers sont ici** : implementation Python publique et independante de la
methodologie GAEZ, consultee pour verifier des details non precises numeriquement dans le
wiki GAEZ v5 ni dans `GAEZ V4.pdf` (notamment le facteur de depletion `p`, voir
`LGPCalc.py::psh()`, et la logique exacte de `Kc`/bilan hydrique/LGP, voir
`LGPCalc.py::EtaCalc()` et `ClimateRegime.py::getLGP()`). Utilise comme reference de lecture
pour construire `2_GAEZ/1_Module_I_ClimaticRegime/1.b)_Build_WaterBalance_LGP.ipynb` (logique
traduite a la main en numpy vectorise, pas une dependance au package PyAEZ lui-meme — voir
ce notebook pour le detail de ce qui a ete repris et les ecarts assumes, ex. notre ETo
Hargreaves-Samona a la place de leur Penman-Monteith complet, faute de RH/vent dans nos
donnees ERA5).

**Pas installe comme dependance Python** (`pip show pyaez` -> absent) — ces fichiers sont ici
uniquement comme reference/archive consultable, pas importes par le code du pipeline.

## Fichiers

| Fichier | Role (Module GAEZ correspondant) |
|---|---|
| `ClimateRegime.py` | Module I — indicateurs agro-climatiques, LGP, regimes thermiques |
| `LGPCalc.py` | Module I — bilan hydrique journalier, Kc, LGP (le plus consulte ici) |
| `ETOCalc.py` | Module I — ETo (Penman-Monteith complet, RH+vent requis) |
| `ClimaticConstraints.py` | Module III — contraintes agro-climatiques |
| `CropSimulation.py`, `CropWatCalc.py` | Module II — simulation culture, bilan hydrique specifique |
| `BioMassCalc.py` | Module II — calcul de biomasse/rendement |
| `SoilConstraints.py` | Module IV — contraintes edaphiques |
| `TerrainConstraints.py` | Module IV — contraintes de pente/terrain |
| `ThermalScreening.py` | filtrage thermique des cultures |
| `EconomicSuitability.py` | evaluation economique |
| `UtilitiesCalc.py` | fonctions utilitaires partagees |
