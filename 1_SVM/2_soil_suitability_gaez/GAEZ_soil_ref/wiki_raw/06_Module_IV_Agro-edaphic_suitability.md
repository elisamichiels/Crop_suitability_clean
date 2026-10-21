# 06. Module IV (Agro-edaphic suitability) — copie brute du wiki GAEZ v5

_Source : https://github.com/un-fao/gaezv5/wiki/06.-Module-IV-(Agro-edaphic-suitability)_
_Markdown brut recupere directement depuis : https://raw.githubusercontent.com/wiki/un-fao/gaezv5/06.-Module-IV-(Agro-edaphic-suitability).md_
_Date de recuperation : 2026-10-01_

_Copie brute, non modifiee, de la page wiki GAEZ v5 utilisee comme source primaire pour toutes les formules SQ1-SQ7/SSR du Module IV (2_GAEZ/4_Module_IV_SoilSuitability/). Voir aussi GAEZ_v5_Pipeline_Documentation.docx pour la synthese des citations utilisees et leur traduction en code._

---


## Introduction

Module IV estimates yield reductions due to the constraints induced by prevailing soil and terrain-slope conditions. Crop yield impacts resulting from sub-optimum conditions for soils and for terrain-slopes are assessed separately.

The Harmonized World Soil Database HWSD v2.01 (FAO/IIASA, 2023) served as source for soil resources data that was used for spatially detailed evaluation of soil qualities for edaphic crop suitability assessments. The agro-edaphic suitability estimations are crop/LUT-specific and are implemented for three basic levels of inputs and management and rain-fed and irrigated water supply systems. HWSD v2.01 was built on the previous version HWSD v1.2, but with several improvements. To name a few:

- The replacement of soil data derived from the ISRIC-WISE database with soil data of the WISE30sec database more than doubled the number of soil profiles used from 10,250 to 21,000.
- In the previous version of HWSD soil attribute data were limited to two layers, topsoil (0–30 cm) and subsoil (30–100 cm). HWSD v2.01 uses seven depth layers as available from WISE30sec, namely 0–20 cm, 20–40 cm, 40–60 cm, 60–80 cm, 80–100 cm, 100–150 cm and 150–200 cm.
- Soil attribute information is expanded with additional attribute data available from WISE30sec, namely: effective CEC, total nitrogen, carbon over nitrogen ratio, and aluminum saturation.
- HWSD v2.01 uses the FAO 1990 Revised Legend, and in addition correlations with the 2022 version of the World Reference Base for Soil Resources.
- Error estimates and statistics of individual soil parameters have become accessible through linkage with the WISE30sec database.
- Full use has been made of soil phase information globally available in the Digital Soil Map of the World and was accounted for when defining WRB Soil Reference Groups and WRB Soil Units.

A list of attributes contained in HWSD v2.01 is given in the table below.

_Table: Attributes in HWSD v2.01._
| HWSD Soil Mapping Unit Details | Soil attributes by depth layer D1-D7 |
| --- | --- |
| Coverage | Depth of top layer (cm) |
| Soil Mapping Unit code (SMU) | Depth of bottom layer (cm) |
| Dominant Soil Unit (WRB 2022) | Coarse fragments (% volume) |
| Dominant Soil Unit (FAO90) | Sand (% weight) |
| **General soil unit information** | Silt (% weight) |
| Sequence in Soil mapping Unit (i) | Clay (% weight) |
| Share in Soil Mapping Unit (%) | Texture class (USDA conventions) |
| Database ID | Bulk Density (g cm–3) |
| National Soil Classification | Reference Bulk Density (g cm–3) |
| Soil Unit Symbol (WRB 2022) | Organic Carbon content (% weight) |
| Soil Unit Name (WRB correlation FAO90) | pH in water (–log(H+) |
| Soil Unit Symbol (FAO90) | Total nitrogen content (g kg–1) |
| Soil Unit Name (FAO90) | Carbon nitrogen ratio (C/N) |
| Rootable Soil Depth (Class) | CECsoil (cmolckg–1) |
| Soil Phase 1 | CECclay, (cmolckg–1) |
| Soil Phase 2 | ECEC (cmolckg–1) |
| Obstacle to Roots (ESDB) | TEB (cmolckg–1) |
| Impermeable layer (ESDB) | BS (% of  CECsoil) |
| Soil Water Regime (ESDB) | Aluminum saturation (% of ECEC) |
| Drainage class (class) | ESP (%) |
| AWC for Rootable Soil Depth (mm) | Calcium carbonate  (% weight) |
| Gelic properties | Gypsum content  (% weight ) |
| Vertic properties | Electric Conductivity (dS m–1) |

In the global agro-ecological modeling framework, soil suitability procedures estimate yield reductions due to the constraints induced by soil limitations. Soil suitability is assessed through crop/LUT specific evaluations of soil qualities characteristics relevant for agriculture. Soil quality (Soil health) is defined as the continued capacity of soil to function as a vital living ecosystem that sustains plants, animals, and humans. 
In this module the concept of soil quality is restricted to soil properties relevant for agricultural production.Crop yield impacts resulting from sub-optimum soil conditions are assessed through crop specific evaluations of seven major agronomic soil qualities estimated from soil attributes available in HWSD. Soil qualities include nutrient availability (SQ1), nutrient retention (SQ2), rooting conditions (SQ3), oxygen availability (SQ4), calcium carbonate and gypsum conditions (SQ5), salinity and sodicity (sodium) conditions (SQ6), and management/workability conditions (SQ7). Limitations depend on the level of inputs and management and are estimated on a crop-by-crop basis and combined into crop and input specific soil suitability ratings for rain-fed cultivation and irrigated water supply systems. These are estimated from soil characteristics available in HWSD v1.2.

These qualities are assessed for each crop and input/management level and for four water supply systems (rain-fed, gravity irrigated, sprinkler irrigation and drip irrigation) and result in a crop and input specific suitability rating. Available soil water is assessed considering soil depth, soil volume and salinity.

Terrain suitability is estimated according to terrain-slope classes and location-specific rainfall amounts and rainfall-concentration characteristics. The latter allow to better assess soil erosion risks and to refine the terrain suitability rating scheme. Module IV evaluates soil units and terrain-slopes separately. Soil resources and terrain-slope conditions are aligned and integrated at 30 arc-second grid cell level (AEZ soil and terrain-slope databases) by ranking soil types regarding occurrence in different slope classes (see Module V).

In this chapter, the framework used to assess the soil and terrain suitability for irrigated agriculture and for defining water collecting sites, areas which are prone to seasonal waterlogging and flood risks, is described. These sites with very specific soil water regimes are set aside for separate assessment. The need for fallow periods is soil and climate related. Soil suitability assessments procedures as part of agro-edaphic assessments are schematically presented in the schema below.


_Figure: Information flow in Module IV_

![fig6_1](https://github.com/user-attachments/assets/36ac8c84-3986-4c5c-a9f7-e7a60ac56938)


**Level of inputs and management**

Individual soil and terrain characteristics have been related to requirements and tolerances of crops at three basic levels of inputs and management circumstances, namely: high, intermediate and low.

_Low-level inputs/traditional management:_ Under the low input, traditional management assumption, the farming system is largely subsistence based and not necessarily market oriented. Production is based on the use of traditional cultivars (if improved cultivars are used, they are treated in the same way as local cultivars), labor intensive techniques, and no application of nutrients, no use of chemicals for pest and disease control and minimum conservation measures.

_Intermediate-level inputs/improved management:_ Under the intermediate input, improved management assumption, the farming system is partly market oriented. Production for subsistence plus commercial sale is a management objective. Production is based on improved varieties, on manual labor with hand tools and/or animal traction and some mechanization. It is medium labor intensive, uses some fertilizer application and chemical pest, disease and weed control, adequate fallow and some conservation measures.

_High-level inputs/advanced management:_ Under the high input, advanced management assumption, the farming system is mainly market oriented. Commercial production is a management objective. Production is based on improved high yielding varieties, is fully mechanized with low labor intensity and uses optimum applications of nutrients and chemical pest, disease and weed control.

**Water supply systems**

Four water supply systems have been separately evaluated. Apart from evaluating crop production systems based on rain-fed cultivation, specific soil requirements for three major irrigation systems have been established namely for gravity, sprinkler and drip irrigation. The table below presents an example of the water supply system/crop associations that are considered in the assessment.

_Table: Examples of combining crops, input levels and water supply systems in GAEZ v5_

![image](https://github.com/user-attachments/assets/26216546-2894-4219-9f36-8c903df3ddce)


**Soil and terrain suitability assessment procedures**

In the GAEZ approach, land qualities are assessed in several steps involving specific procedures. The land qualities related to climate and climate-soil/terrain interactions (flooding regimes, soil erosion and soil nutrient maintenance) are treated separately from those land qualities specifically related to soil chemical properties and conditions that directly affect crop growth and production (see table below).

_Table: Land qualities and corresponding AEZ assessment procedures._
| Land quality                                | AEZ procedure                                    |
|---------------------------------------------|----------------------------------------------------------------------|
| Climate regime (temperature, moisture, radiation) | Climatic suitability assessment                    |
| Soil physical and chemical properties       | Soil suitability assessment                                          |
| Terrain slope                               | Assessment of sustainable use of sloping terrain                     |
| Soil nutrient maintenance                   | Fallow period requirement assessments                                |
| Flooding regime                             | Moisture regime analysis of water collecting sites                   |


## Soil suitability assessment procedure

Procedures and activities employed in the soil suitability assessment are schematically represented below.

_Figure: Soil suitability rating procedures._

![image](https://github.com/user-attachments/assets/0a553ce9-deb8-4fb0-afb0-1bf90f5eb6c6)


In the GAEZ approach, first individual soil qualities are defined and quantified. The table below provides an overview of the seven soil qualities in relation to relevant soil characteristics, including soil drainage characteristics and soil phase occurrences. The seven soil qualities (SQ1–7) are estimated from specific soil characteristics, the prevalence of soil phases, soil drainage characteristics, vertic and petric soil units, and gelic soil conditions.

_Table: Soil qualities and soil characteristics_
| Soil qualities | Soil quality related soil profile characteristics, soil drainage conditions and soil phase characteristics |
|----------------|------------------------------------------------------------------------------------------------------------|
| SQ1 Nutrient availability | Soil texture, soil organic carbon, soil pH, total exchangeable bases. |
| SQ2 Nutrient retention capacity | Soil texture, base saturation, cation exchange capacity of soil and of clay fraction. |
| SQ3 Rooting conditions | Soil texture, coarse fragments, vertic soil properties and soil phases affecting root penetration and rootable soil depth and effective soil volume. |
| SQ4 Oxygen availability to roots | Soil drainage and soil phases affecting soil drainage. |
| SQ5 Salinity and sodicity conditions | Soil salinity, soil sodicity and soil phases influencing soil salinity and sodicity conditions. |
| SQ6 Calcium carbonate and gypsum conditions | Calcium carbonate and gypsum content, and soil phases influencing calcium carbonate and gypsum conditions. |
| SQ7 Workability (constraining field management) | Soil texture, effective soil depth/volume, and soil phases constraining soil management (soil depth, rock outcrops, stoniness, gravel/concretions and hardpans). |


### Soil characteristics

Chemical and physical soil profile characteristics considered for different soil depth layers and include: the soil textural class; organic carbon content; pH, cation exchange capacity of soil and clay fraction; base saturation; total exchangeable bases; calcium carbonate contents; gypsum content; sodicity and salinity. For each soil unit these values are available from HWSD.

**Soil texture classes (TXT) and soil textural groupings (1 - 3)**

Soil texture indicates the relative content of particles of various sizes, such as sand, silt and clay in the soil. Texture influences the ease with which soil can be worked, the amount of water and air it holds, and the rate at which water can enter and move through soil and as such it influences the following soil qualities: nutrient availability (SQ1), nutrient retention (SQ2), rooting conditions (SQ3) and soil workability (SQ7). Soil texture is also an important factor for determining soil drainage.

There are 13 soil textural classes defined on the basis of their sand, silt and clay percentages: sand (S); loamy sand (LS); sandy loam (SL); loam (L); silt loam (SiL); silt (Si); sandy clay loam (SCL); clay loam (CL); silty clay loam (SiCL); sandy clay (SC); silty clay (SiC); clay (C), and heavy clay (Ch). These classes can be grouped into 3 main soil textural groupings corresponding approximately with soil texture classes: coarse (S, LS) with symbol 1, fine (C, Ch, SiC, SC) with symbol 3 and medium (all other textures) with symbol 2. Soil textural classes and Soil textural groupings are illustrated in the figure below.

_Figure: Soil texture classes (a) and Soil textural groupings (b)_

![image](https://github.com/user-attachments/assets/ff897c01-dc13-4c83-bff6-35f2abc2336f)


**Gravel content (GRC)**

While texture refers to the granulometry of particles less than 2mm in diameter, gravel concerns the soil fraction that has particles larger than 2mm. HWSD contains an estimate of the gravel content of each soil unit.

**Soil Organic carbon content (SOC)**

Soil organic carbon (SOC) is the main component of soil organic matter (SOM) that consists of plant and animal detritus at various stages of decomposition, cells and tissues of soil organisms, and substances that soil organisms synthesize. SOM provides numerous benefits to the physical and chemical properties of soil and its capacity to provide regulatory ecosystem services. SOM is especially critical for soil functions and soil health. Organic carbon is, the best simple indicator of SOM and moderate to high amounts of organic carbon are associated with fertile soils with a good structure and a good nutrient availability (SQ1).

**Soil acidity and alkalinity (pH value)**

The pH, measured in a soil-water solution, is a measure for the acidity and alkalinity of the soil. The pH has a strong effect on the availability of nutrients to the plant (SQ1). Optimum pH values range between 5.5 and 7.0. Very low pH values are associated with Aluminum toxicity.

**Cation exchange capacity of clay (apparent CEC)**

The apparent CEC gives an indication of the weathering stage of soils and is associated with the absence or presence of mineral reserves that influences the retention of nutrients and water. Weathering stages are also associated with clay minerals that have typical cation exchange capacities, with kaolinites generally having the lowest at less than 16 cmol/kg, while smectites have one of the highest with 80 cmol/kg or more. This is a good indicator for nutrient retention (SQ2).

**Cation exchange capacity of soil (CEC)**

The total nutrient fixing capacity of a soil is well expressed by its Cation Exchange Capacity (CEC). Soils with low CEC have little resilience and cannot build up stores of nutrients. Many sandy soils have CEC less than 4 cmol/kg. The clay content, the clay type and the organic matter content all determine the total nutrient storage capacity. Values in excess of 10 cmol/kg are considered satisfactory for most crops. The CEC is an excellent indicator for soil nutrient availability (SQ1).

**Base saturation (BS)**

The base saturation measures the sum of exchangeable cations (nutrients) Na, Ca, Mg and K as a percentage of the overall exchange capacity of the soil (including the same cations plus H and Al). High base saturation is associated with higher pH and high availability of nutrients.

**Total exchangeable bases (TEB)**

Total exchangeable bases represent for the sum of exchangeable cations in a soil: Sodium (Na), Calcium (Ca), Magnesium (Mg) and Potassium (K). TEB, as the CEC of the soil, is a good indication of nutrient availability (SQ1)

**Calcium carbonate (CCB)**

Calcium carbonate is a chemical compound (a salt), with the chemical formula CaCO<sub>3</sub>. It is a common substance found as rock in all parts of the world and is the main component of shells of marine organisms, snails, and eggshells. Calcium carbonate is the active ingredient in agricultural lime and is usually the principal cause of hard water. It is quite common in soils particularly in drier areas and it may occur in different forms as mycelium-like threads, as soft powdery lime, as harder concretions or cemented in petrocalcic horizons. Low levels of calcium carbonate enhance soil structure and are generally beneficial for crop production. At higher concentrations they may induce iron deficiency and when cemented limit the water storage capacity of soils. It is of direct relevance to match CCB with the tolerance of crops for lime and gypsum (SQ6).

**Calcium sulphate (GYP)**

Gypsum is a chemical compound (a salt) which occurs occasionally in soils particularly in dryer areas. Research indicates that up to 2% gypsum in the soil favors plant growth, between 2 and 25% has little or no adverse effect if in powdery form, but more than 25% can cause substantial reduction in yields. It is of direct relevance to match GYP with the tolerance of crops for lime and gypsum (SQ6).

**Exchangeable sodium percentage (ESP)**

The exchangeable sodium percentage (ESP) has been used to indicate levels of sodium in soils. Sodium influences negatively soil structure and soil permeability. The tolerance of crops for sodium is variable avocado and nuts are extremely sensitive and show toxicity symptoms with ESP as low as 10%, while wheat, cotton and date palm for instance can stand ESP up till 40%. It is of direct relevance to match ESP with the tolerance of crops for sodicity (SQ5).

**Electrical conductivity (EC)**

Coastal and desert soils in particular can be enriched with water-soluble salts or salts more soluble than gypsum. Crops vary considerably in their resistance and response to salt in soils. Some crops will suffer at values as little as 2 dS.m<sup>\-1</sup> (beans, radish, pear, apples) others can stand up to 16 dS.m<sup>\-1</sup> (sugar beet, spinach, date palm). It is of direct relevance to match EC with the tolerance of crops for salinity (SQ5).

In addition to these soil characteristics three other soil characteristics are considered that are contained in the soil unit name. These are:

**Vertic soil units and properties**

Vertic soil units are those that have clayey textures which at some time in most years show one or more of the following: cracks, slickensides, wedge-shaped or parallel-piped structural aggregates that are not sufficiently expressed to qualify as Vertisols. Like Vertisols these characteristics unfavourably affect the workability of soils (SQ7) (FAO, Unesco and ISRIC, 1990).

**Petric soil units**

Petric Calcisols and Petric Gypsisols have respectively petrocalcic and petrogypsic horizons within 100cm of the surface, affecting SQ3 (rooting conditions), SQ6 (presence of lime and gypsum) SQ7 (workability) and available soil water.

**Gelic soil units**

Gelic soil units are those that have permafrost within 200 cm of the surface (FAO, Unesco and ISRIC, 1990). Permafrost areas are unsuitable for crop growing and excluded from evaluation.

**Reference Soil Depth (RSD)**

The reference soil depth is set at 100 cm for all soil units except for Lithosols (10cm), Rankers (30cm), Rendzinas (30cm) and Leptosols (30cm). The reference soil depth is consequently adjusted as a function of impermeable layers or hardened layers and pans that occur within 100 cm of the surface.

### Soil drainage

Soil drainage refers to the natural capability of a soil to remove excess water. The drainage capacity of a soil depends on the soil type, its texture, the presence or absence of impermeable layers and the slope on which the soil occurs.

The rate at which water drains into the soil has a direct effect on the amount and timing of runoff, what crops can be grown, and where wetlands form. In soils with low drainage rates, water will pond on the soil's surface. Poorly drained soils are desirable when growing crops like rice where the fields are flooded during cultivation, but other crops need better drained soils. Seven classes are recognized (FAO, 1995):

- **Excessively drained (E):** water is removed from the soil very rapidly Soils are commonly very coarse textured or rocky, shallow or on steep slopes;
- **Somewhat excessively drained (SE):** water is removed from the soil rapidly. Soils are commonly sandy and very pervious;
- **Well drained (W):** water is removed from the soil readily but not rapidly. Soils commonly retain optimum amounts of moisture, but wetness does not inhibit root growth for significant periods;
- **Moderately well drained (MW):** Water is removed from the soil somewhat slowly during some periods of the year. For a short period, soils are wet within the rooting depth, they commonly have an almost impervious layer;
- **Imperfectly drained (I):** Water is removed slowly so that soil is wet at a shallow depth for significant periods. Soils commonly have an impervious layer, a high-water table, or additions of water by seepage;
- **Poorly drained (P):** Water is removed so slowly that soils are commonly wet at a shallow depth for considerable periods. Soils commonly have a shallow water table which is usually the result of an almost impervious layer, or seepage, and
- **Very poorly drained (VP):** Water is removed so slowly that the soils are wet at shallow depths for long periods. Soils have a very shallow water table and are commonly in level or depressed sites.

Drainage characteristics for each soil are generally included in national soil surveys. In HWSD a reference drainage class is given based on soil textural class; no soil phase and flat terrain is assumed. For the suitability assessment local occurrences of soil phases and terrain slope conditions are accounted for.

Soils characterized by permanent or frequent high-water tables (such as most Histosols, Gleysols, and gleyic units of other soils) that generally occur on flat to gently sloping terrain had the poorest drainage (ranging between very poor to imperfectly drained). Soils with a high clay content (Vertisols) or soils characterized by an abrupt textural change (Planosols) or an anthraquic phase have similar poor drainage classes.

Soils characterized by coarse textures that occur on gentle slopes such as most Arenosols, Regosols and (non-gleyic) Podzols are partly excessively and partly somewhat excessively drained.

Shallow soils such as Leptosols and soils with plinthite or with a petrocalcic, petrogypsic, petroferric or duripan phase are imperfectly drained when having medium or fine textures and moderately well drained when having a coarse topsoil texture. In general, steep slopes and coarse topsoil texture, improve drainage conditions.

### Soil phases

Phases are subdivisions of soil units based on characteristics that are significant for the use or management of the land, but were not diagnostic for the separation of the soil units themselves at the time they were mapped (Since then soil classification changes have incorporated several of these phases in the soil unit name). In HWSD 33 different soil phases are recognized but only a smaller number of them have sufficient extent and have a direct link with the soil suitability to be discussed here. Some of the phases, mapped by different agencies (CEC, 1985; FAO and Unesco, undated; ISRIC and FAO, 2006; Shi et al., 2004) can be grouped as they stand for very similar characteristics. In addition to the definition of the phases the link with the soil quality impact is given.

The soil phases (except Anthraquic) are also used for adjustments of the available water storage capacity of the soils in which they occur.

**Stony/rudic/concretionary phases**

These phases mark areas where the presence (> 35%) of gravel, stones, boulders or rock outcrops in the surface layers or at the surface makes the use of mechanized agricultural equipment impracticable. Hand tools or simple mechanical equipment may to some extent be used provided other conditions are favorable. Fragments up to 7.5 cm are considered as gravel; larger fragments are stones and boulders. These soil phases affect in the first place the workability of the soil (SQ7) but also the soil volume and rooting conditions (SQ3).

**Lithic phase**

This phase is used when continuous coherent and hard rock occurs within 50 cm of the soil surface. For Leptosols the lithic phase is not shown as it is implied in the soil unit name. This characteristic clearly affects the soil depth and consequently the rooting conditions (SQ3) and the workability (SQ7).

**Petric and gravelly phases**

The gravelly and petric phases refers to soil material which contains more than 40% coarse fragments or oxidic concretions within 100 cm of the soil surface. The coarse material is embedded at less shallow depth compared to the stony phase but also affect the workability of the soil (SQ7) and the soil volume and rooting conditions (SQ3).

**Skeletic phase**

The skeletic phases refers to soil material which contains more than 40% coarse fragments or oxidic concretions within 50 cm of the soil surface. Coarse material affects workability of soils (SQ7), and soil volume and rooting conditions (SQ3).

**Petrocalcic phase**

Marks soils in which the upper part of a petrocalcic horizon (> 40% lime, cemented, usually thicker than 10 cm) occurs within 100 cm of the surface. The limitation in soil depth and the high concentration of lime implies constraints related to lime and gypsum (SQ6), but also the soils depth (SQ3) and the workability (SQ7) are affected.

**Petrogypsic phase**

Used for soils in which the upper part of a petrogypsic horizon (> 60% gypsum, cemented, usually thicker than 10 cm) occurs within 100 cm of the surface. This high concentration of gypsum in an indurated layer implies constraints related to lime and gypsum (SQ6), but also the soils depth (SQ3) and the workability (SQ7) are affected.

**Petroferric phase**

The petroferric phase marks soils with a continuous layer of indurated material in which iron is important cement and organic matter is absent within 100 cm of the soil surface. These characteristics affect the workability of the soil (SQ7) and the soil volume and rooting conditions (SQ3).

**Fragipan phase**

The fragipan phase marks soils which have the upper level of the fragipan occurring within 100 cm of the surface. The fragipan is a loamy subsurface horizon with a high bulk density relatively to the horizon above it. It is hard or very hard and seemingly cemented when dry. Dry fragments slake or fracture in water. A fragipan is low in organic matter and is only slowly permeable. These characteristics limit the soil depth and the soil volume and affect the rooting conditions (SQ3).

**Duripan phase**

The duripan phase marks soils in which the upper level of a duripan occurs within 100 cm of the soil surface. A duripan is a subsurface horizon that is cemented by silica and contains often accessory cements mainly iron oxides or calcium carbonate. These characteristics limit the soil depth and the soil volume and affect the rooting conditions (SQ3).

**Saline/salic phases**

The saline and salic phase marks soils in which in some horizons within 100 cm of the soil surface show electric conductivity values higher than 4 dS m<sup>\-1</sup>. The saline phase is not shown for Solonchaks because their definition implies a high salt content. These concentrations of soluble salts are harmful for salt -sensitive crops and affects SQ5.

**Sodic phase**

The sodic phase marks soils which have more than 6 % saturation with exchangeable sodium in some horizons within 100 cm of the soil surface. The sodic phase is not shown for Solonetz because their definition implies a high ESP. These concentrations of sodium are harmful for Na -sensitive crops and affects SQ5.

**Anthraquic phase**

The anthraquic phase marks soils showing stagnic properties within 50 cm of the surface due to surface water logging associated with long continued irrigation, particularly of rice. This affects the rooting conditions of crops (SQ3).

## Rating of soil characteristics

The soil suitability assessment considers soil profile attributes, soil texture, soil drainage and soil phases.

Soil characteristics suitability ratings are empirical coefficients that reflect the effect the value of the soil characteristic has on the yield potential of a specific crop. The rating system is adapted from Sys et al. (1991). The individual ratings themselves draw on extensive compilation of results of research farm experiments and empirical knowledge among others summarized by Sys et al. (1993), Nachtergaele (1988) and Nachtergaele and Bruggeman (1986). The ’Sys’ system uses six constraint classes namely:

- S0 - No constraint (100)
- S1 - Slight constraint (90)
- S2 - Moderate (70)
- S3 - Severe constraint (50)
- S4 - Very severe constraint (30)
- N - Not suitable (10)

The effect of soil characteristics often goes in a single direction: the lower the value the higher the constraint level (organic carbon is an example), or the higher the value the higher the constraint level (salinity and sodicity are examples). There are also characteristics that have an optimum value below and above which the constraints level increases (pH is an example). Note that for some characteristics, thresholds are built in that limit the constraint levels to be used. For instance, even at zero organic carbon content the maximum constraint is set at 70. For intermediate values of soil characteristics, the lower rating is selected. For instance, a pH value of 8.4 in rain-fed maize high input gets a rating of 50. A coarse fragments content of 60% for workability (SQ7) is rated 10.

The ratings have been compiled by input level (high, intermediate and low) and by the four water supply systems (rain-fed, gravity irrigation, sprinkler irrigation and drip irrigation systems). The soil profile characteristics ratings account for soil characteristics, _gelic_ soil conditions and _vertic_ soil properties.

**Soil texture ratings**

Soil texture conditions are influencing the various soil qualities (SQ1, SQ2, SQ3 and SQ7). In addition, texture is used in the determination of soil drainage conditions and therefore indirectly used for SQ4 as well. The table below provides example soil texture ratings for rain-fed production of wheat for individual soil qualities. Soil workability ratings differ for high (H) and intermediate and low inputs (L+I) and are provided separately. Soil texture ratings are compiled for individual water supply systems.

**Soil drainage ratings**

Reference soil drainage (on flat land) is characterized in the Harmonized World Soil Database in 7 classes and corrected for slope conditions. These classes are in a next step corrected as a function of the slope on which they occur.

Soil drainage ratings are varying by crop and may vary by prevalent soil texture conditions.. Assumptions for artificial soil drainage differ by input levels. High level inputs assume full and adequate artificial drainage systems are installed while low and intermediate inputs assume no artificial drainage.

**Soil phases ratings**

The soil phase ratings available from published and unpublished data sets have been compiled by input level (high, intermediate and low) and by the four water supply systems (rain-fed, gravity irrigation, sprinkler irrigation and drip irrigation systems). The ratings represent constraints implied by the occurrence of soil phases in percentage (100% rating no constraint to 0% rendering a soil totally unsuitable).

The soil phases are organized by soil quality to which they apply and by level of input and management and water supply system. Two rating types have been used: “_full_” indicating that the soil phase rating would apply to 100% of the extent of the soil unit to which the soil phase is attributed and _“split”,_ where the soil phase rating is assumed to affect 50% of the soil to which it is attributed while the other 50% is assumed not to be affected.

## Soil quality and soil suitability

This section deals with soil suitability classification procedures, following a two-step approach:

1. Crop responses to individual soil attribute conditions and relevant soil drainage and phase conditions are combined into soil quality (SQ) ratings, and
1. Soil qualities are combined into crop specific soil suitability ratings, by input and management level and by water supply system.

The soil suitability assessment considers soil profile attributes, soil texture, soil drainage and soil phases. To cover the range of conventional farming options, three levels of farming are assumed in AEZ , i.e., (i) low level inputs, high labor intensity and traditional management using local cultivars, (ii) intermediate level inputs, medium labor intensity and management using local and improved cultivars, and (iii) high level inputs, low labor intensity, mechanization and advanced management, using high yielding cultivars. In all three levels of inputs appropriate monocropping rotation requirements and fallow requirements as appropriate for input levels are assumed implemented.

### Soil qualities

Procedures to derive soil qualities (SQ1-7) and soil unit suitability from various combinations of soil attributes are based on Liebig’s law of the minimum with specified adjustments to account for other constraints than the most limiting.

To determine SQ3 (Rooting conditions) the rootable soil depth is adjusted with the minimum rating of (i) soil depth/volume limited soil properties (ii) occurrence of soil depth/soil volume limiting soil phases, and (iii) obstacles to roots or impermeable layers.

To determine SQ4 (Oxygen availability) the minimum of soil drainage conditions and specific soil phases impeding soil drainage conditions are used.

To determine SQ5 (Soil salinity and sodicity) the minimum of the soil salinity and soil sodicity conditions, and occurrence of saline (salic) and or sodic or saline/sodic soil phases are used.

To determine SQ6 (Calcium carbonate and gypsum), the most limiting of calcium carbonate content and gypsum content and occurrence of petrocalcic and petrogypsic soil phases are considered. Calcium carbonate content may affect physiological (growth) aspects, while high gypsum content may cause nutrient imbalances. Gypsum prevalence may also hinder field and water supply management which is considered in SQ7 (soil workability).

When more complex relationships and multiple factors make up a soil quality, as is the case for SQ1 (nutrient availability), SQ2 (nutrient retention), and SQ7 (soil workability), the lowest rated attribute is adjusted with the average rating of the remaining attributes, as illustrated by the rating function _f<sub>SQ</sub>_ below:

Let (x<sub>1</sub>,….,x<sub>m</sub>) be a vector of soil attributes relevant for a particular soil quality SQ and (τ(x<sub>1</sub>),…, τ(x<sub>m</sub>)) the vector of respective soil attribute ratings, 0 ≤ τ(x<sub>j</sub>) ≤ 100.

Further, let j<sub>o</sub> denote the soil attribute with the lowest rating such that:

$$
\tau(x_{j0}) \leq \tau(x_j), \quad j = 1, \dots, m
$$

Then we define soil quality SQ by multiplying the lowest soil attribute rating with the average of the remaining soil attributes ratings, as follows:

$$
SQ = f_{SQ}(x_1, \dots, x_m) = \tau(x_{j_0}) \cdot \frac{1}{m - 1} \sum_{j \ne j_0} \tau(x_j)
$$

Note that the soil attribute ratings are obtained by linear interpolation.

Soil qualities are separately estimated by soil layer. Individual soil layer qualities are combined using specific weighting factors derived from crop/LUT specific root distribution occurring within a crop’s maximum rooting depth and rootable soil depth. Soil qualities are separately estimated for individual soil layers: D1 (0-20 cm), D2 (20-40 cm), D3 (40-60 cm), D4 (60-80 cm), D5 (80-100 cm), D6 (100-150 cm), and D7 (150-200 cm) and combined by crop specific weighing factors according to crop-soil specific rooting patterns and crop specific tillage practices (Annex 2). The use of soil attributes of seven soil layers versus the two layers (0-30 and 30 -100cm) of the previous version of HWSD markedly improves suitability estimations for crop/LUTs with varying rooting depths.

**Nutrient availability (SQ1)**

Natural availability of nutrients is decisive for successful farming for (i) low inputs and traditional soil and plant/crop management, and (ii) assuming intermediate inputs and improved soil and plant/crop management.

Diagnostics related to nutrient availability are manifold. Important soil characteristics of the upper layer are soil texture/mineralogy/structure (attribute TXT), soil organic carbon (OC), soil pH (pH<sub>Wat</sub>) and total exchangeable bases (TEB). For the deeper layers these are: texture/mineralogy/structure (TXT), soil pH, and total exchangeable bases (TEB). Evaluations of upper and deeper layers are plant/crop specific depending on rooting pattern and rooting depth.

The soil profile attributes relevant to soil nutrient availability are related. For SQ1 the attribute with the lowest suitability rating is multiplied with the average of the remaining ones. The relationships shown below represent upper soil layer (0-20 cm) and deeper layers (> 20 cm) separately by using weighted values of soil attributes and ratings of the respective soil layers and crop/LUTs.


$$
\mathrm{SQ1_{upper\ soil\ layer}} = f_{SQ}(\mathrm{TXT},\ \mathrm{OC},\ \mathrm{pH},\ \mathrm{TEB})
$$


$$
\mathrm{SQ1_{deeper\ soil\ layers}} = f_{SQ}(\mathrm{TXT},\ \mathrm{pH},\ \mathrm{TEB})
$$

SQ1 is evaluated separately for upper soil layer and the deeper soil layers. Soil attributes in deeper layers are weighted according to root mass distribution of specific plants/crops within rootable soil depth.

**Nutrient retention(SQ2)**

Nutrient retention is of particular importance for the effectiveness of fertilizer applications and is foremost relevant for intermediate and high input farming.

Nutrient retention refers to the capacity of the soil to retain added nutrients against losses caused by leaching. Plant nutrients are held in the soil on the exchange sites provided by the clay fraction, soil organic carbon and the clay-humus complex. Losses vary with the intensity of leaching which is determined by the rate of drainage of soil moisture through the soil profile. Soil texture affects nutrient retention in two ways, through its effects on available exchange capacity of the clay minerals and by soil permeability.

The soil characteristics used for the assessment of the upper soil layer are respectively soil texture/mineralogy/structure (TXT), base saturation (BS), cation exchange capacity of soil (CEC<sub>soil</sub>), and for the deeper layers soil TXT, pH BS, and cation exchange capacity of the clay fraction (CEC<sub>clay</sub>). Soil pH serves as proxy measure of micro-nutrient deficiencies.

For SQ2 the attribute with the lowest suitability rating is multiplied with the average of the remaining ones. The relationships shown below represent upper soil layer D1 (0-20 cm) and deeper layers D2-D7 (> 20 cm) separately by using weighted values of soil attributes and ratings of the respective soil layers and crop/LUTs.

$$
\mathrm{SQ2_{upper\ soil\ layer}} = f_{SQ}(\mathrm{TXT},\ \mathrm{BS},\ \mathrm{CEC_{soil}})
$$

$$
\mathrm{SQ2_{deeper\ soil\ layers}} = f_{SQ}(\mathrm{TXT},\ \mathrm{pH},\ \mathrm{BS},\ \mathrm{CEC_{clay}})
$$

SQ2 is evaluated separately for upper soil layer and the deeper soil layers. Soil attributes in deeper layers are weighted according to root mass distribution of specific plants/crops within rootable soil depth.

**Rooting conditions (SQ3)**

Rooting conditions include rootable soil depth (cm) accounting for impermeable layers, pans or indurated horizons in the soil, and effective soil volume (vol. %) accounting for the presence of gravel and stones. Rooting conditions may be affected by the presence of a soil phase, either limiting the rootable soil depth or decreasing the effective volume accessible for root penetration. Rooting conditions influence crop growth in several ways:

* Adequacy of foothold, i.e., sufficient soil depth for the crop for anchoring.
* Available soil volume and penetrability of the soil for roots to extract nutrients.
* Space for root and tuber crops for expansion where the economic yield is produced in the soil.
* Absence of shrinking and swelling properties (vertic), mainly affecting root and tuber crops.

Rootable soil depth and soil volume limitations affect root penetration and constrain yield formation, for roots and tubers. Rooting conditions (SQ3) are estimated by combining the rootable soil depth rating _τ(RSD)_ \[14\], \[15\] with additional soil ratings for conditions affecting root development and root and tuber yield.

Rooting condition (SQ3) is derived from rootable soil depth rating τ(RSD) adjusted by the minimum rating of the additional limitation factors, as follows:

$$
\mathrm{SQ3} = \tau(\mathrm{RSD}) \times \min \left[ \tau(\mathrm{TXT}),\ \tau(\mathrm{GRC}),\ \tau(\mathrm{VSP}),\ \tau(\mathrm{GSP}) \right]
$$

where, τ( ) is the respective input level specific and crop specific attribute rating for soil texture (TXT), gravel content (GRC), vertic or gelic soil properties (VSP, GSP).

**Oxygen availability (SQ4)**

Oxygen availability in soils is largely defined by drainage characteristics of soils. The determination of soil drainage classes is based on procedures developed at FAO. These procedures account for soil type, soil texture, soil phases and terrain slope.

Assumptions regarding artificial drainage vary with input level. For low and intermediate input farming, drainage ratings assume no artificial drainage. For high input, drainage ratings assume that adequate artificial drainage systems are installed.

Apart from drainage characteristics, oxygen availability may be influenced by soil and terrain characteristics that are defined through the occurrence of specific soil phases and presence of impermeable layers and/or prevailing temporal soil wetness conditions

SQ4 for a specific plant/crop has been defined as the most limiting attribute rating of either soil drainage or soil phase. The SQ4 soil quality differs between input levels due to different assumptions regarding artificial drainage.

$$
\mathrm{SQ4} = \min \left[ \tau(\mathrm{DRG}),\ \tau(\mathrm{SPH}) \right]
$$

where, τ(…) is the respective input level specific attribute rating for drainage and soil phases.

As DRG and SPH relate to a soil unit rather than individual soil layers, SQ4 is evaluated for the entire soil profile.

**Salinity and sodicity (SQ5)**

Accumulation of salts may cause soil salinity. Excess of free salts, referred to as soil salinity, are measured as electric conductivity (EC) or as saturation of the exchange complex with sodium ions. The latter is referred to as sodicity or sodium alkalinity (it often occurs with high pH values) and is measured as exchangeable sodium percentage (ESP).

Soil salinity affects crops through inhibiting the uptake of water. Moderate salinity affects growth and reduces yields; high salinity levels might prevent growth of plants/crops. Sodicity causes sodium toxicity and affects soil structure leading to massive or coarse columnar structure with low permeability. Apart from soil salinity and soil sodicity, saline (salic) and sodic soil phases affect crop growth and yields.

In the case of simultaneous occurrence of saline (salic) and sodic soils the limitations are combined. Subsequently the most limiting of the combined soil salinity and/or sodicity conditions and occurrence of saline (salic) and/or sodic soil phase is selected. Soil salinity and sodicity are assumed independent of farming input and management.

The most limiting rating of the soil salinity and sodicity conditions and occurrence of saline (salic) and/or sodic soil phases determines SQ5.

$$
\mathrm{SQ5} = \min \left[ \tau(\mathrm{ESP}),\ \tau(\mathrm{EC}),\ \tau(\mathrm{SPH}) \right]
$$

where, τ( ) is the respective attribute rating function evaluated separately for upper and deeper soil layers attributes.

SQ5 is evaluated for upper and deeper soil layers within rooting zone of specific plants/crops, limited to rootable soil depth.

**Calcium carbonate and Gypsum (SQ6)**

Calcisols and calcareous soils with high calcium carbonate content, as well as soils with petrocalcic soil phases, may exhibit micronutrient deficiencies of, e.g., iron, manganese, and zinc and in some cases toxicity of molybdenum, all of which may affect growth and yield performance of specific crops.

Gypsisols and gypsiferous soils with high gypsum content, as well as soils with a petrogypsic soil phase may depress yield performance through nutrient imbalances. High gypsum prevalence may affect field operations and interfere with irrigation water supply and soil drainage. The latter constraints are rated under workability (SQ7). Tolerance of crops to calcium carbonate (CCB) and gypsum (GYP) varies widely.

In SQ6, the most limiting of the combination of excess calcium carbonate and gypsum in the soil and occurrence of petrocalcic and petrogypsic soil phases. This soil quality is assumed independent of the level of input and management.

$$
\mathrm{SQ6} = \min \left[ \tau(\mathrm{CCB}),\ \tau(\mathrm{GYP}),\ \tau(\mathrm{SPH}) \right]
$$

where, τ( ) is the respective attribute rating function.

SQ6 is evaluated for upper and deeper soil layers within rooting zone of specific plants/crops, limited to rootable soil depth.

**Workability (SQ7)**

Diagnostic characteristics that can be related to soil workability vary by type of management applied. Workability or ease of tillage depends on interrelated soil characteristics such as texture, soil structure, organic matter content, soil consistence/bulk density, the occurrence of gravel or stones in the profile or at the soil surface, and the presence of continuous hard rock at shallow depth as well as rock outcrops. Some soils are easy to work independent of moisture content, other soils are only manageable at a specific moisture status for hand cultivation or light machinery.

Irregular soil depth, gravel and stones in the profile and rock outcrops, might prevent the use of farm machinery. Soil constraints related to soil texture and soil structure are particularly affecting low and intermediate input LUTs, while the constraints related to irregular soil depth and stony and rocky soil conditions are foremost affecting mechanized land preparation and harvesting operations of high-level input farming LUTs. Workability constraints are therefore handled separately for low, intermediate, and high input farming.

Physical hindrance depends on crop and specific field management. AEZ procedures are crop and management specific and consider hindrance by limited rootable soil depth, soil phases (stony, rudic, lithic, petric, skeletic, petrocalcic, petroferric, fragipan, duripan), prevalence of coarse fragments, soil texture and vertic soil properties. Soil texture ratings and presence of coarse fragments ratings (gravel content) are determined for each of the seven soil depth layers (D1-D7). Rootable soil depth, soil drainage, soil phases and vertic soil properties apply to entire soil units. Soil workability is evaluated for upper and deeper soil layers within rooting and tillage zones of specific plant/crop LUTs, limited to rootable soil depth.

SQ7 is derived by multiplying the most limiting soil/soil phase attribute rating with the average of the remaining attribute ratings as follows:

$$
\mathrm{SQ7} = fSQ (\mathrm{RSD}, \mathrm{GRC}, \mathrm{TXT}, \mathrm{VSP}, \mathrm{DRN}, \mathrm{SPH}, \mathrm{OTR}, \mathrm{ISL})
$$

where, τ( ) is the respective input level specific attribute rating, RSD is rootable soil depth, GRC is soil gravel content, TXT is soil texture, VSP represents vertic soil properties, DRN represents soil drainage and related and soil percolation conditions, SPH indicates occurrence of soil phases, OTR occurrence of obstacles to roots and ISL indicates prevalence of impermeable soil layers.

Miscellaneous units in HWSD v2.01 are considered to render land unsuitable for plant/crop production. These include shifting sand, rock debris, rock outcrops, dunes, salt flats, inland water, ice caps, as well as gelundic, takyric, yermic, desert and gobi units.

### Soil unit suitability rating

Functional relationships of soil qualities have been formulated to quantify crop/LUT suitability of soil units. The following guiding principles formed the basis for the way soil qualities by crop/LUT were combined for different levels of inputs and management:

* Nutrient availability and nutrient retention are key soil qualities, interacting with other limitation factors.
* Nutrient availability is of utmost importance for low level input farming; nutrient retention is most important for high level inputs.
* Nutrient availability and nutrient retention are considered of equal importance for intermediate level inputs farming.
* Nutrient availability is strongly related to rooting depth and soil volume available, and
* Rooting conditions, oxygen available to roots, excess salts, tolerance to calcium carbonate and gypsum, and workability are regarded as equally important soil qualities. The combination of these five soil qualities is best achieved by multiplication of the most limiting rating with the average of the ratings of the remaining four soil qualities.

Following the above principles, by three levels of inputs and four different water supply systems, each soil unit suitability rating (SSR<sub>low</sub>, SSR<sub>int</sub> and SSR<sub>high</sub>) has been estimated for individual crops. The functional relationships for respectively low, intermediate, and high input farming vary in their use of SQ1 and SQ2, as presented below.

Let (SQ<sub>1</sub>,….,SQ<sub>m</sub>) be a vector of soil qualities relevant for a particular soil rating SSR and SQ<sub>1</sub>…, SQ<sub>m</sub> the vector of respective soil quality values, 0 ≤ SQ<sub>j</sub> ≤ 1 or 100%. Further, let j<sub>o</sub> denote the soil quality with the lowest value such that: SQ<sub>jo</sub> ≤ SQ<sub>j</sub>, j = 1,…,m.

Then we define soil unit suitability function f<sub>SSR</sub>, as:

![image](https://github.com/user-attachments/assets/7fb50664-615d-4227-9006-73537706daff) 

Low input farming:

_S_SR<sub>low</sub> = SQ1 × f<sub>SSR</sub>(SQ3, SQ4, SQ5, SQ6, SQ7)_

Intermediate input farming:

_S_SR<sub>int</sub> = 0.5 × (SQ1+SQ2) × f<sub>SSR</sub>(SQ3, SQ4, SQ5, SQ6, SQ7)_

High input farming:

_S_SR<sub>high</sub> = SQ2 × f<sub>SSR</sub>(SQ3, SQ4, SQ5, SQ6, SQ7)_


The results of soil unit suitability assessment have been tabulated by the combination of each crop/soil unit/slope class/input level/water supply system, for integration with the results of the agro-climatic suitability assessment to estimate agro-ecological attainable crop yields.

## Available soil water

The growing period for most crops continues beyond the rainy season and, to a greater or lesser extent, crops mature on moisture stored in the soil profile. However, the amount of soil moisture stored and available to a crop, varies, e.g., with depth of the soil, physical characteristics, and the rooting pattern of the crop. Depletion of soil moisture reserves causes the actual evapotranspiration to fall short of the potential rate. Available soil water capacity depends on physical and chemical characteristics, but above all on effective depth or volume (FAO, 1995).

**Estimation of Available Soil Water Capacity (AWC)**

The 21,000 soil profiles used for WISE 30 and subsequent in HWSD v2.01 and classified according to FAO’90 classification are representing typical soil characteristics by soil unit, within defined climatic zones (Koeppen Geiger 1st level classification, Peel et al. 2007). It is assumed that the soil profiles are representing locally typical profiles by soil unit without considering soil phases.

Therefore, in soil suitability classifications, for the determination of available water holding capacity and soil drainage, relevant soil phases must be considered in addition and taken into account in the GAEZ procedures for estimating AWC for rootable soil depth.

**AWC for rootable soil depth** is the amount of water that the soil can hold and that is available for plant growth. It is the difference between the amount of water in the soil at field capacity and the amount of water in the soil at wilting point. It is also referred to as Available Water Capacity (AWC). AWC depends on physical and chemical characteristics, but above all on effective depth and volume of the soil (FAO, 1995).

The presence of a root-restricting layer reduces the rootable depth and therefore the available water capacity. The AWC calculation in GAEZ uses soil phase information to determine rootable depth and computes AWC values by layer. The procedure consists of 6 steps.

**Step 1: Determine reference AWC from USDA textures per Layer (D1-D7).**

Reviewing various texture-based estimates of AWC in the literature reference AWC values per textural class were set in Step 1.

_Table: Texture based AWC used in GAEZ v5_
| Nr. | USDA Texture Classes  | AWC (mm m⁻¹) |
|-----|-----------------------|--------------|
| 1   | Heavy clay            | 160          |
| 2   | Silty clay            | 175          |
| 3   | Clay                  | 175          |
| 4   | Silty clay loam       | 190          |
| 5   | Clay loam             | 190          |
| 6   | Silt                  | 175          |
| 7   | Silt loam             | 175          |
| 8   | Sandy clay            | 160          |
| 9   | Loam                  | 160          |
| 10  | Sandy clay loam       | 160          |
| 11  | Sandy loam            | 125          |
| 12  | Loamy sand            | 85           |
| 13  | Sand                  | 65           |
|     | Histosols             | 250          |



**Step 2: Adjust AWC for soil parent material. AWC + Soil parent material adjustments => AWC**

Soil parent material influences soil classification and affects available water capacity. Adjustments of AWC for soil parent material are adapted from FAO (1995) (Digital Soil Map of the World and derived soil properties version 3.5) as follows:

* **Andosols:** Due to specific parent material Andosols have higher AWC (except Vitric Andosols).
* **Vertisols:** specific clay mineralogy (montmorrilonite) reduces AWC from reference AWC.
* **Tropical soils:** Tropical soils may have specific mineralogy and AWC. Prevalence of kaolinitic clay minerals cause low or very low cation exchange capacity (CEC<sub>clay</sub> < 24 cmol<sub>c</sub>/kg), resulting in substantial lower AWC than reference. Suspect soils are Ferralsols, Acrisols, Nitisols, Plinthosols, and Lixisols.

For Andosols reference AWC is increased by 10%, for Vertisols AWC is reduced by 20%, and for tropical soils with low CEC<sub>clay</sub>, reference AWC values are reduced by 10%. In the latter case the reduction is only applied when values of CEC<sub>clay</sub> < 24 cmol<sub>c</sub>/kg occur in the D3 layer (40-60 cm depth).

**Step 3: Reduce AWC for coarse material fraction (i.e., gravel, concretions, stones) and/ or volume reducing soil phases. AWC + Coarse fragment reduction => AWC**

Presence of coarse fragments in the soil profile (gravel, concretions, stones and boulders, larger than 2 mm)) reduces AWC. The reduction is estimated from coarse materials attribute information available for individual soil layers (D1-D7) in HWSD v2.01. Reduction is estimated at about 1% for each volume percent of coarse fragments.

_Table: AWC adjustment for coarse fragments_


![Picture1](https://github.com/user-attachments/assets/964b4eb5-7ec0-4364-b3cb-47b1844db3ee)


Soil volume reducing soil phases (petric gravelly, skeletic, stony, rudi and concretionary) decrease AWC. These soil phases occur within 50 cm or within 100 cm of the soil surface and restrict AWC. It is assumed that effective soil volume and therefore AWC within the rootable soil depth are reduced by  and by 25% for petric,  gravelly, and skeletic soil phases and by 35% for stony, rudic and concretionary soil phases.

_Figure: AWC constraints of soil phases occurring within 100cm of soil surface (*: soil phases reducing rootable soil volume and AWC: i.e., petric, skeletic and gravelly soil phases, reduction of AWC available to crops in the order of 25%)._

![image](https://github.com/user-attachments/assets/d838ebab-b1bd-415c-a0ef-4b06089eab80)


_Figure: AWC constraints of soil phases occurring within 100cm of soil surface (*: soil phases reducing rootable soil volume and AWC: i.e., stony, rudic and concretionary, reduction of AWC available to crops in the order of 35%)._

![image](https://github.com/user-attachments/assets/d952bd7f-c2ad-4fbe-98f4-ef10b6e7a88e)


**Step 4: Reduce AWC for soil salinity – AWC + Soil salinity reduction => AWC**

Salinity reduces soil water holding capacity as a function of soil electric conductivity. The reduction is estimated from the soil salinity attribute information separately available for individual soil layers (D1-D7) in HWSD v2.01. AWC adjustments are also made for soil units where a saline or salic phase is indicated. According to soil phase definition, we consider EC ≥ 4 dS/m for soil layers to 100 cm.

_Table: AWC adjustments for soil salinity_

![Picture2](https://github.com/user-attachments/assets/8d92111c-899a-4c4a-8dd8-29150ae0ee0c)


**Step 5: Reduction of rootable soil depth due to depth reducing soil phases**

Decreased rootable soil depth limits available water capacity, Rootable soil depth is defined as the depth to which plants can exploit the soil for nutrients and moisture. When processing a soil unit record, a rootable soil depth class is derived from the respective soil unit and soil phase information, as follows:

* **Deep > 100 cm:** all soils, excluding Leptosols, soils with depth limiting soil phases, soils with obstacles to roots (soil attribute ROO, Classes 2–6) and soils with an impermeable layer (soil attribute IL, Class 1).
* **Moderately deep 50–100 cm:** 50% of soils with _petroferric_, _petrocalcic_, _petrogypsic_, _placic_ or _duripan_ soil phases, soils with other obstacles to roots (soil attribute ROO, Class 2) and soils with an impermeable layer (soil attribute IL, Class 3).
* **Shallow 10–50 cm:** 50% of soils with _petroferric, petrocalcic, petrogypsic, placic, duripan_ and 100% of soils with _lithic_ soil phases and Leptosols (LPe, LPd, LPk, LPm, LPu, LPi), and soils with other obstacles to roots (soil attribute ROO, Classes 3–5), and soils with an impermeable layer (soil attribute IL, Class 4).
* **Very shallow < 10 cm:** Lithic Leptosols (LPq), soils with obstacle to roots (soil attribute ROO, Class 6), and Bare Rock.

_Figure: AWC and rootable soil depth constraints of soil phases occurring within 100cm of soil surface (*: soil phases reducing rootable soil depth and AWC: i.e., petrocalcic, petrogypsic, petroferric, fragipan, duripan and placic soil phases, obstacles to roots (ROO - classes 3-5) and impermeable layers (IL - class 4))._

![image](https://github.com/user-attachments/assets/33bd2093-e837-440c-8a68-5c8cafbb9f8a)

_Figure: AWC constraints due to coherent hard rock occurring within 50cm of soil surface (*: lithic soil phases reducing rootable soil depth and AWC)._

![image](https://github.com/user-attachments/assets/d22dc51d-c050-499b-b372-9f064e701f68)


**Step 6: Estimation of AWC to rootable soil depth**

This step in the calculation of AWC to rootable depth pertains to adding up layer specific AWC values for all layers within the effective rootable depth.

_Table: Estimation of AWC to rootable soil depth_
| Rootable depth range (cm) | Representative value (cm) | Rootable depth specific AWC       |
|---------------------------|---------------------------|----------------------------------|
| <10                       | 10                        | 0.5×AWC4 (D1)                    |
| 10-50                      | 40                        | AWC4 (D1+D2)                     |
| 50-100                     | 80                        | AWC4 (D1+D2+D3+D4)               |
| 100-200                    | 150                       | AWC4 (D1+D2+D3+D4+D5+D6)         |


## Terrain suitability assessment procedures

The influence of topography on agricultural land use is manifold. Farming practices are by necessity adapted to terrain slope, slope aspect, slope configuration and micro-relief. For instance, steep irregular slopes are not practical for mechanized cultivation, while these slopes might very well be cultivated with adapted machinery and hand tools.

Sustainable agricultural production on sloping land is foremost concerned with the prevention of erosion of topsoil and decline of fertility. Usually this is achieved by combining special crop management and soil conservation measures. Cultivated sloping land may provide inadequate soil protection and without sufficient soil conservation measures, cause a considerable risk of accelerated soil erosion. In the short term, cultivation of slopes might lead to yield reductions due to loss of applied fertilizer and fertile topsoil. In the long term, this will result in losses of land productivity due to truncation of the soil profile and consequently reduction of natural soil fertility and of available soil moisture.

Rain-fed annual crops are the most critical to cause topsoil erosion, because of their particular cover dynamics and management. The terrain-slope suitability rating used in the Global AEZ study captures the factors described above which influence production and sustainability. This is achieved through: (i) defining for the various crops permissible slope ranges for cultivation, by setting maximum slope limits; (ii) for slopes within the permissible limits, accounting for likely yield reduction due to loss of fertilizer and topsoil, and (iii) distinguishing among farming practices ranging from manual cultivation to fully mechanized cultivation.

Ceteris paribus, i.e., under similar crop cover, soil erodibility and crop and soil management conditions, soil erosion hazards largely depend on amount and intensity of rainfall. Data on rainfall amount is available on a monthly basis for all grid cells in the climate inventory. Rainfall intensity or energy, as is relevant for soil erosion, is not estimated in these data sets.

To account for clearly existing differences in both amount and within-year distribution of rainfall, use has been made of the modified Fournier index (Fm), which reflects the combined effect of rainfall amount and distribution (FAO/UNEP, 1977), as follows:

$$
F_m = \frac{12 \sum_{i=1}^{12} P_i^2}{\sum_{i=1}^{12} P_i}
$$

where _P<sub>i</sub>_ is the precipitation of month i

When precipitation is equally distributed during the year, i.e., in each month one-twelfth of the annual amount is received, then the value of Fm is equal to the annual precipitation. On the other extreme, when all precipitation is received within one month, the value of Fm amounts to twelve times the annual precipitation. Hence, Fm is sensitive to both total amount and distribution of rainfall and is limited to the range 1 to 12 times the annual precipitation.

The Fm index has been calculated for all grid cells of the 5 arc-minute climatic inventory in Module I. The results have been grouped in six classes, namely: Fm &lt; 1300, 1300–1800, 1800–2200, 2200–2500, 2500–2700, and Fm &gt; 2700. These classes were determined on basis of regression analysis, correlating different ranges of length of growing period zones with levels of the Fournier index Fm. This was done to incorporate the improved climatic information on within year rainfall distribution into GAEZ while keeping consistency with earlier procedures of the methodology, which were originally defined by LGP classes.

Slope ratings are defined for the ten slope range classes used in the land resources database, namely: 0–0.5%, 0.5–2%, 2–5%, 5–8%, 8–12%, 12–16%, 16–24%, 24–30%, 30–45%, and >45%. 

## Soil and terrain suitability assessment for irrigated conditions

Apart from evaluating rain-fed crop production systems, specific soil requirements for three major irrigation systems have been established namely for gravity, sprinkler and drip irrigation.

**Soil suitability for irrigated conditions**

The suitability evaluation procedures for irrigated crop production cover dry-land crops and wetland rice, at intermediate and high levels of inputs. Crop-specific soil limitations for rain-fed production, such as limitations imposed by soil rooting conditions, soil nutrient availability, soil nutrient retention capacity, soil toxicity is similar to those for rain-fed suitability. Examples of water supply system specific soil evaluation criteria are soil salinity and soil alkalinity that are separately evaluated for drip irrigation systems and gypsum content, which is separately evaluated for gravity irrigation (Fischer and van Velthuizen, 2002).

The following land and soil characteristics have been interpreted specifically for the irrigation suitability classification: topography; soil drainage; soil texture; surface and sub-surface stoniness; calcium carbonate levels; gypsum status; and salinity and alkalinity conditions. The main literature sources used in the interpretation include Sys et al. ( 1993), Sys and Riquier (1980), FAO (1985), FAO (1996), FAO (FAO, 1976), FAO and Unesco ( 1974), and FAO et al. (1990).

**Terrain suitability for irrigated conditions**

The dominant terrain factor governing the suitability of an area for any water supply system is terrain slope. Other topographic factors, such as micro-relief, have partly been accounted for in the soil unit and soil phase suitability classifications.

Permissible slopes depend on type of water supply system and assumed level of inputs and management. Terrain suitability ratings for individual water supply systems and input levels, for eight slope classes and eight crop groups, are presented by the six Fournier index classes varying from Fm &lt; 1300 to Fm &gt; 2700.

## Suitability of water-collecting sites

In water-collecting sites substantially more water can be available to plants as compared to upland situations. Water-collecting sites are difficult to locate in a global study but can be approximately determined on basis of prevalence of specific soil types. Fluvisols and to a lesser extent Gleysols are typically representing the flat terrain of alluvial valleys and water-collecting sites.

The cultivation of Fluvisols (under unprotected natural conditions) is determined by frequency, duration and depth of flooding. The flooding attributes are generally controlled by external factors such as a river’s flood regime which in turn is influenced by hydrological features of the catchment area and catchment/site relations, rather than by the amount of ‘on site’ precipitation.

Therefore, with exception of wetland crops, the cultivation of these soils is mainly confined to post-flood periods, with crops growing on residual soil moisture. The flooding regime in arid and semi-arid zones is erratic. Some years, severe flash floods may occur, in other years no floods occur at all. In sub-humid and humid zones flooding is more regular but duration and depth of flooding may vary widely from year to year. Gleysols are not directly affected by river flooding. These soils are however frequently situated in low-lying water-collecting sites and when not artificially drained, the Gleysols may be subject to waterlogging or even inundation as result from combinations of high groundwater tables and ponding rainwater. In arid and semi-arid areas these soils are cultivated in the later part and after rainy seasons; the crops grow and mature on residual soil moisture. In sub-humid and humid areas Gleysols without artificial drainage often remain waterlogged for extensive periods, rendering them unsuitable for cultivation of dryland crops.

On both, Fluvisols and Gleysols, crops of short duration that are adapted to growing and producing yields on residual soil moisture and which are tolerant to flooding, water-logging and high groundwater tables, can be found producing satisfactorily outside the growing period defined by the local rainfall regime. Therefore, a separate crop suitability classification for water-collecting sites is required. In compiling this classification, the logic of the original AEZ study (FAO, 1981) has been followed. This includes accounting for crop-specific tolerances to excess moisture (high groundwater, waterlogging and flooding/inundation) and the use of available estimates of flooding regimes of the Fluvisols. Since Gleysols are mostly, but not necessarily, subjected to waterlogging and inundation just like the ‘natural Fluvisols’, it was decided to treat Gleysols with terrain-slopes of less than 2% the same as Fluvisols.

In many parts of the world the flooding of Fluvisols is increasingly being controlled with dikes and other protection means. Fluvisols, in protected conditions, do not benefit additional water supply and regular fresh sediment deposits, nor do they suffer from flooding. The moisture regime of Fluvisols under these protected conditions are similar to other soils and therefore protected Fluvisols are treated according to the procedures used for crops in upland conditions.

In a similar way, Gleysols may be artificially drained, thereby diminishing a major limitation for the cultivation of these soils. For areas where the Gleysols have been drained, a revised (i.e., less severe) set of soil ratings is used and the rules for natural Fluvisols are not applied. Since spatial details of the occurrence of protected Fluvisols and artificial drainage of Gleysols are not available at the global scale these factors are assumed to be linked to the level of inputs/management. The application of Fluvisol suitability ratings and soil unit suitability ratings of artificially drained Gleysols are presented in the table below

_Table: Application of fluvisol and gleysol suitability ratings by input level_

| Water Source       | Fluvisols (Natural) | Fluvisols (Protected) | Gleysols (Natural) | Gleysols (Artificially Drained) |
|--------------------|---------------------|-----------------------|--------------------|---------------------------------|
| **RAIN-FED**       |                     |                       |                    |                                 |
| High level inputs  | no                  | yes                   | no                 | yes                             |
| Intermediate level inputs | 50%             | 50%                   | 50%                | 50%                             |
| Low level inputs   | yes                 | no                    | yes                | no                              |
| **IRRIGATION**     |                     |                       |                    |                                 |
| High level inputs  | no                  | yes                   | no                 | yes                             |
| Intermediate level inputs | 50%             | 50%                   | 50%                | 50%                             |


Moisture suitability ratings devised for unprotected Fluvisols and Gleysols without artificial drainage are organized in ten groups of crops with comparable growth cycle lengths and similar tolerances to high groundwater levels, waterlogging and flooding . An example is given in the table below.

_Table: Suitability make up for short-term dryland crops in ‘natural’ (unprotected) water collecting sites without artificial drainage by LGP class_

![image](https://github.com/user-attachments/assets/0883ed22-db69-40ca-946e-a0d5dd428452)


**Short-term dry-land crops (I)**

This group includes some short duration crops (wheat, barley, rye, oat, dryland rice, foxtail millet, chickpea, rape, and alfalfa) which are somewhat tolerant to excess moisture. For LGPs less than 30 days it is assumed there is on the average insufficient water to bring these crops to maturation and yield, especially since the contribution from rainfall is also almost non-existent. At LGPs longer than 120 days these crops will grow irrespective additional water. It has been assumed that the Fluvisols are too wet in LGPs over 300 days. Most of these crops are marginal to not suitable in humid areas. Agro-climatic constraints alone will render these long LGPs already marginal to not suitable.

## Fallow period requirements

In their natural state many tropical soils cannot be continuously cultivated without undergoing degradation. Such degradation is marked by a decrease in crop yields and a deterioration of soil structure, nutrient status and other physical, chemical and biological attributes. Under traditional low input farming systems, this deterioration is kept in check by alternating some years of cultivation with periods of fallow. The length of the necessary rest period is dependent on inputs applied, soil and climate conditions, and crops. Hence, the main reason for incorporating fallow into crop rotations is to enhance sustainability of production through maintenance of soil fertility.

Regeneration of nutrients and maintenance of soil fertility under low input cultivation is achieved through natural bush or grass fallow. At somewhat higher inputs to soils, the soil fertility is maintained through fallow, which may include for a portion of time a grass, grass-legume ley or a green-manure crop. Factors affecting changes in soil organic matter are reviewed in Nye and Greenland (1960) and Kowal (1978). They include temperature, rainfall, soil moisture and drainage, soil parent material, and cultivation practices. The fallow factors used in the present GAEZ land potentials assessments are based on earlier work done in the context of FAO’s regional assessments (Young and Wright, 1980) and the Kenya AEZ study (Kassam et al., 1991b).

The fallow factors have been established by main crop groups and environmental conditions. The crop groups include cereals, legumes, roots and tubers, and a miscellaneous group consisting of long-term annuals/perennials. The environmental frame consists of individual soil units, thermal regimes and moisture regimes. The thermal regimes are expressed in terms of annual mean temperatures of > 25°C, 20–25°C, 15–20°C and &lt;15°C. The moisture regimes are expressed in terms of five broad LGP ranges: <60 days, 60–120 days, 120–180 days, 180–270 days, and &gt; 270 days.

The fallow factors included in GAEZ are expressed as percentage of time during the fallow-cropping cycle the land must be under fallow, foremost to maintain its soil fertility status. For the four crop groups: cereals, legumes, roots and tubers, and a miscellaneous group consisting of long-term annuals/perennials, at intermediate level of inputs, the fallow requirements are set at one third of the levels required under low level of inputs, and at high levels of inputs and management fallow requirements are uniformly set at 10%.

Exceptions to the above are:
* For Fluvisols and Gleysols fallow factors are set lower because of their special moisture and fertility conditions;
* For wetland rice on Fluvisols, fallow requirements for all three input levels are set to 10%;
* For wetland rice on Gleysols, at high and intermediate inputs the fallow requirements are set to 10% and at low inputs to 20%;
* For wetland rice on soils other than Fluvisols and Gleysols, fallow requirements are set as for crop group 1 (cereals), and
* Fallow requirements have been assumed to be negligible for the perennial crops oilpalm, olive, citrus, cocoa, tea, coffee, jatropha, coconut, miscanthus, switchgrass, reed canary grass and alfalfa. For these perennials, no fallow requirements have been set.

In GAEZ the fallow requirement factors are applied for the estimation of potential average annual production which can be achieved on a sustainable basis under the assumed level of inputs and management.

1. Soil quality (Soil health) is defined as the continued capacity of soil to function as a vital living ecosystem that sustains plants, animals, and humans. In this module the concept of soil quality is restricted to soil properties relevant for agricultural production.
1. Soil textures generally are associated with specific soil structures and mineralogy.
1. Constraint ratings for stony, petric, petroferric, fragipan, duripan, rudic, skeletic, gravelly and concretionary soil phases have not been applied for cropland.
1. Soil profile attribute constraints ratings are obtained from rating classes (100%, 90%, 70%, 50%, 30% and <10%) by interpolation between class limits. Soil unit characteristics constraints are obtained from soil characteristic rating table for entire spatial extent of soil units or as split rating, whereby only 50% of the spatial extent of soil units are affected.
1. To deal with rootable depth reducing soil phases occurring within 100 cm from the soil surface, it is assumed that these soil phases for 50% occur between 50 and 100 cm and for 50% in the class less than 50 cm. This applies for instance for soils with petroferric, petrocalcic, petrogypsic, placic and/or duripan soil phases. Soils with such soil phases are therefore split (in statistical sense) and have been assigned for 50% to occur in the rootable soil depth class 50-100 cm and for 50% in the < 50 cm class.
1. Fluvisols are, by definition, flooded by rivers. Fluvisols are young soils where sedimentary structures are clearly recognizable in the soil profile.
1. Gleysols are generally not flooded by rivers. However, the soil profiles indicate regular occurrence of high groundwater tables through reduction (gley) features. Low-lying Gleysols may be ponded/water-logged by high groundwater and rainfall during the rainy season.
1. Histosols are partly occurring in water collecting sites as well. When reclaimed, including artificial drainage and after mixing the histic topsoil with underlying mineral materials, Histosols may be turned in very productive soils for intensive forms of arable cropping/horticulture (Driessen and Dudal, 1991). Draining and reclaiming poorly drained Histosols is not recommended because they serve as important habitat for wetland ecosystems and are significant carbon reservoirs. Unreclaimed natural Histosols, due to low bearing capacities of upper histic horizon (bulk density < 0.1 Mg/m<sup>3</sup>), generally poor drainage conditions and other unfavorable chemical and physical characteristics, are considered unfit to permit its use for arable purposes and therefore rendering possibilities of benefitting from additional water resources in water collecting sites irrelevant.