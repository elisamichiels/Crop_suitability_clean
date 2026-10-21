# PyAEZ — tutoriels (notebooks + archives d'exercices)

Source : https://github.com/gicait/PyAEZ (branche `master`, commit `792e1d4231f6fa75beb98bbeed162a4fa9efbb56`,
2026-02-10), dossier `tutorials/`.

**Pourquoi ces fichiers sont ici** : complement a `../pyaez_source/` (le code) et
`../pyaez_data_input/` (les donnees d'exemple) — montrent comment les fonctions de
`pyaez/LGPCalc.py`, `ClimateRegime.py` etc. sont reellement appelees bout-en-bout, utile pour
verifier qu'on utilise bien les memes parametres/ordre d'appel que l'implementation de
reference. Pas executes dans notre pipeline, consultables uniquement.

## Fichiers

- `NB1_ClimateRegime.ipynb` : **Module I** (climat) — le plus pertinent pour notre
  `1_Module_I_ClimaticRegime/`, demontre l'appel reel de `getLGP()` et des autres methodes de
  `ClimateRegime`.
- `NB2_CropSimulation.ipynb` : Module II (simulation culture, rendement limite par l'eau).
- `NB3_ClimaticConstraints.ipynb` : Module III (contraintes agro-climatiques).
- `NB4_SoilConstraints.ipynb` : Module IV (sol) — comparable a notre `4.a)-4.c)`.
- `NB5_TerrainConstraints.ipynb` : Module IV (terrain/pente) — comparable a notre `4.d)`.
- `NB6_EconomicSuitability.ipynb` : evaluation economique (hors perimetre thesis actuel).
- `Day1_Python_Training_and.ipynb`, `Day2_Module_I_and_II_Demonstration.ipynb` : supports de
  formation generaux.
- `A_Data_Preparation.zip`, `B_AgroClimatic_Analysis.zip`, `C_Crop_Simulation.zip`,
  `D_Applying_Yield_Reduction_Factors.zip` : archives d'exercices associees (donnees +
  notebooks complementaires), non decompressees.
