## Introduction 

Module V executes the final step in the GAEZ crop suitability and land productivity assessment. It reads the LUT specific results of the agro-climatic evaluation for biomass and yield calculated in Module II/III for different soil classes and it uses the edaphic rating produced for each soil/slope combination in Module IV to estimate agro-ecological attainable yields and related variables. The inventories of soil resources and terrain-slope conditions are integrated by ranking all soil types in each soil map unit with regard to occurrence in different slope classes. Considering simultaneously the slope class distribution of all grid cells belonging to a particular soil map unit results in an overall consistent distribution of soil-terrain slope combinations by individual soil association map units and 30 arc-sec grid cells. Soil unit ratings and terrain slope ratings are applied separately for each water supply system. The information flow in Module V is summarized in the figure below.

*Figure 7-1 Information flow in Module V*

![fig7_1](https://github.com/user-attachments/assets/e07eea7d-c865-49e2-bd12-7170207879cd)

## Description of Module V operation 

### Main processing steps in Module V

The algorithm in Module V steps through the 30 arc-seconds grid cells of the spatial soil association layer of the Harmonized World Soil Database (Nachtergaele et al., 2012) and determines for each grid cell the respective make-up of land units in terms of soil types and slope classes. Each of these component land units is separately assessed and assigned a suitability rating and simulated attainable yield. The grid cell results are accumulated over all component land units in a grid cell.
Processing of soil and slope distribution information takes place for 30 arc-second grid cells. One hundred of these produce the edaphic characterization at 5 arc-minutes, which is the resolution used for providing GAEZ v5 results. Information stored for 5 arc-minute grid cells contains distributions resulting from the individual 30 arc-second sub-grid evaluations.
The main purpose of Module V is to compile a grid-cell database for each crop, which stores evaluation results and summarizes the processed sub-grid information. Computations include the following steps:

* Assign applicable agro-climatic yields calculated in separate crop water balances for eight broad soil AWC classes (simulated in Module II/III);
* Under low input conditions, apply AEZ rules for water-collecting sites (defined as Fluvisols and Gleysols on flat terrain);
* Apply yield reduction factors according to results of edaphic and terrain slope evaluation for the specific combinations of soil types/slope classes making up a grid cell (evaluated in Module IV);
* Apply yield adjustment factors to account for CO₂ fertilization effect according to crop, atmospheric CO₂ concentration and land suitability rating;
* Determine an applicable fallow requirement factor depending on climate characteristics, soil type, crop group and input level;
* Aggregate results of attainable yields, actual crop evapotranspiration and crop water deficits/net irrigation requirements over the component land units that make up a grid cell (soil type/slope combinations), and
* Map and tabulate results for each past and future 40-year period by crop, input level and water source.

The make-up of different land units (soil type/slope class combinations) within a 5 arc-minute grid cell usually involves multiple combinations of soil types and texture classes, each of which is assigned to the closest matching of the eight soil AWC classes used for simulation in Module II/III. The respective class results are then retrieved to represent for each component soil the agro-climatic potential yield and associated crop calendar and crop water balance indicators. Results of the individual soil component evaluations are aggregated up to the 5 arc-minute grid cell level and stored as distributions of suitable areas and corresponding attainable yields.

Cropping activities are among the most critical in causing topsoil erosion, because of their management and the cover dynamics of annual crops. For this reason, GAEZ applies in Module V a terrain-slope suitability rating procedure to account for important factors that influence production sustainability (for details see Chapter 6, section 6.6). Terrain suitability is estimated according to grid-cell specific terrain-slope classes and location specific rainfall amounts and concentration characteristics. Soil and terrain characteristics are read by 30 arc-second grid-cells for which sub-grid soil and terrain combinations have been quantified in the database. These calculations are crop/LUT specific and are separately performed for three basic input levels for rain-fed and irrigated water supply systems.

The processing in Module V also accounts for fallow period requirements, which have been established for main crop groups, by level of inputs, and for different climatic conditions. The fallow factors included in GAEZ are expressed as percentage of time during the fallow-cropping cycle the land must be under fallow, foremost to maintain its soil fertility status. In crop summary tabulations produced in Module V, the fallow requirement factors are applied for the estimation of attainable average annual production that can be achieved on a sustainable basis under the assumed level of inputs and management.


### Module V mapping and tabulation 

The results of crop evaluation in Module V are stored as separate databases, each organized in terms of 5 arc-minutes grid cells. Separate files are generated holding results by crop, input level, type of water supply and climate scenario/time period. Each of these crop databases contains sub-grid distribution information with regard to suitable extents, potential production, water deficit and fallow factors, with all information kept by suitability classes.

Various utility programs have been developed to aggregate and tabulate results by administrative or hydro-region units, or to map the contents of Module V crop databases in terms of a suitability index, suitable area shares, potential grid-cell production and related water balance variables.

Crop summary tables provide standardized information for each crop by administrative units (country or country/province for a few major countries) and by broad hydro-regions. The comprehensive tables summarize by suitability class the suitable extents and attainable yields, various constraint factors (due to thermal regime, moisture deficits, agro-climatic constraints due to pest, disease and workability limitations and due to soil/terrain limitations) and aggregate simulated water deficits. 

Following below, three examples of mapped outputs from Module V analysis are presented. The mapped classes are based on the normalized suitability index SI:

SI = (90 x VS + 70 x S + 50 x MS + 30 x mS + 15 x vmS + 0 x NS)/0.9

where VS, S, …, NS are the area extents in a grid cell assessed as respectively very suitable (VS), suitable (S), moderately suitable (MS), marginally suitable (mS), very marginally suitable (vmS) and not suitable (NS).

See GAEZ v5 dataset on crop suitability, class index on the FAO Agro-Informatic Data Catalog ([link](https://data.apps.fao.org/catalog/iso/00cffd62-2ebf-47ab-9777-332cd1071aa0)).

See GAEZ v5 dataset on water deficit/net irrigation requirement during crop cycle on the FAO Agro-Informatic Data Catalog ([link](https://data.apps.fao.org/catalog/iso/85264f81-9796-49ab-91ae-bc8c24ac4a1a)).

## Impact of atmospheric CO₂ concentrations on crop yields 

The “fertilization” effect of increasing atmospheric CO₂ on crop yields is accounted in GAEZ by the CO₂ yield-adjustment factor (fCO₂). Crop species respond differently to CO₂ depending on physiological characteristics such as photosynthetic pathway (e.g., C3 or C4 plants). These crop-specific responses are accounted in the parameterization of fCO₂:

$$
f_{\mathrm{sui}\_\mathrm{CO_{2}}} = \left(1 + \left(a \cdot [\mathrm{CO_{2}}]^2 + b \cdot [\mathrm{CO_{2}}] + c\right)\right)
$$


Where a, b and c are parameters (by broad crop groups) used to capture the different CO₂ responses of five broad crop groups (see table below). 

*Table: Crop-specific coefficients for the calculation of CO₂ fertilization effect*
| Coefficient | Crop Group 1 | Crop Group 2 | Crop Group 3 | Crop Group 4 | Crop Group 5 |
|-------------|---------------|---------------|---------------|---------------|---------------|
| **a**        | -0.0003500    | -0.0003325    | -0.0002800    | -0.0003850    | -0.0004025    |
| **b**        | 0.10636       | 0.10104       | 0.057888      | 0.11700       | 0.12231       |
| **c**        | -31.2870      | -29.7227      | -16.0540      | -34.4157      | -35.9801      |


_**1**: wheat, barley, rye, oat, buckwheat, temperate beans, chickpea, dry pea, rapeseed, flax, cabbage, carrot, onion, tomato, alfalfa._
_**2**: rice, cassava, sweet potato, yam, lowland beans, cowpea, gram, pigeon pea, groundnut, sunflower, tobacco, banana, oil palm, olive, citrus, cocoa, coffee, coconut, red canary grass, jatropha, rubber, grass legumes._
_**3**: maize, sorghum, millet, sugar cane, napier grass, miscanthus, switchgrass._
_**4**: soybean._
_**5**: white potato, sugar beet, cotton._

The factor fsui_CO₂ is an empirical correction factor accounting for land suitability as explained below. The maximum yield increment due to CO₂ enrichment (i.e., without considering land suitability constraints) is shown in the figure below.

*Figure: Yield response to elevated ambient CO₂ concentrations*
![image](https://github.com/user-attachments/assets/032d0574-76f2-4b67-9c4d-a9fe144ca1a0)

The local environment also influences the impact that CO₂ has on crop growth. Realization of the fertilization effect of CO₂ is adjusted when sub-optimum growth conditions are indicated by the suitability classification for a LUT in each grid-cell. Under very suitable conditions it is assumed that a fertilization effect equal to 85% of that derived from laboratory experiments could be realized in farmers’ fields. For marginally suitable conditions this share is set to one-third (see table below). This mechanism and the functions used are broadly consistent with results reported in free-air CO₂ enrichment (FACE) experiments.

*Table: Adjustment factors for CO₂ fertilization effect according to land suitability class*
|  | Very Suitable (VS) | Suitable (S) | Moderately Suitable (MS) | Marginally Suitable (mS) |
| --- | --- | --- | --- | --- |
| fsui_CO₂ | 0.850 | 0.667 | 0.500 | 0.333 |

In GAEZ various atmospheric CO₂ concentration pathways were simulated, as used for the IPCC AR6 and quantified by different climate modeling groups. GAEZ runs were performed with different CO₂ concentrations for each scenario for three future time periods (2030s, 2050s, 2070s and 2090s).

## Description of Module V outputs
Module V records for each grid-cell and crop the relevant results of the assessment, including by suitability class the suitable extents, attainable yields, yield-reducing factors, accumulated temperatures, and water balance information.
Operation of Module V generates many maps which are named using a 3-character map type acronym and a 3-character crop acronym. Maps are by crop, map type, input level, water source, climate, concentration pathway, and time period. Since 5 arc-minute grid cells can be made up of multiple soil types and terrain slope classes, the assessment assigns an estimate to each of these components, to capture the heterogeneity of each grid cell, which produces a distribution of results falling into different suitability classes, as follows:

| Acronym | suitability description | Farm economics |
| --- | --- | --- |
| VS | Very suitable land (80–100 % of maximum attainable yield) | Prime land offering best conditions for economic crop production |
| S | Suitable land (60–80%) | Good land for economic crop production |
| MS | Moderately suitable land (40–60%) | Moderate land with substantial climate and/or soil/terrain constraints requiring high product prices for profitability |
| mS | Marginally suitable land (20–40%) | Commercial production not viable. Land could be used for subsistence production when no other land is available |
| vmS | Very marginally suitable (< 20%) | Economic production not feasible |
| NS | Not suitable | Production not possible |

The mapping therefore generates different products that either average the results for an entire grid cell (see map types etl, si, sx, wdl and yl in the table below) or relate to a fraction of the grid cell indicated by the land cover data as cropland (see map types etc, sc, su, wdc and yc). For these maps it is assumed that farmers will have used the better part of the suitability distribution in a grid cell, e.g. when the cropland share is 20% of a grid cell then the top 20% of the suitability and yield distribution are used to define the map contents. In addition, the average yield of the highest occurring suitability class in a grid cell is mapped as well (map type yx). Also, the maps of type sx1 to sx3 help to understand the make-up of a grid cell by summarizing components of the suitability distribution of each pixel. The different themes of mapped information provided by Module V are listed in the table below.

*Table: Mapped output produced by Module V analysis*
| Type | Crop indicator | Unit |
| --- | --- | --- |
| etc | Actual crop evapotranspiration (excluding irrigation), average for current cropland | mm |
| etl | Actual crop evapotranspiration (excluding irrigation), average for grid cell | mm |
| sc | Suitability index class, current cropland | Class |
| si | Suitability index class, total grid cell | Class |
| su | Average suitability index of current cropland | Scalar |
| sx1 | Share of grid cell assessed as VS or S | Scalar |
| sx2 | Share of grid cell assessed as VS, S or MS | Scalar |
| sx3 | Share of grid cell assessed as VS, S, MS or mS | Scalar |
| sx | Average suitability index of total grid cell | Scalar |
| wdc | LUT water deficit/net irrigation requirement during crop cycle, current cropland | mm |
| wdl | LUT water deficit/net irrigation requirement during crop cycle, total grid cell | mm |
| yc | Average attainable yield, current cropland | Kg/ha* |
| yl | Output density (= potential grid cell production/grid cell area), total grid cell | Kg/ha* |
| yx | Maximum attainable class yield in grid cell | Kg/ha* |

The 3-character crop name acronyms, which are used to generate file names in Module V, are listed in the table below.

*Table: Crop name acronyms used in GAEZ v5*
Acronym | Crop name | Acronym | Crop name
-- | -- | -- | --
alf | Alfalfa | ban | Banana
bck | Buckwheat | brl | Barley
bsg | Biomass sorghum | cab | Cabbage
car | Carrot | chk | Chickpea
cit | Citrus | coc | Cacao
cof | Coffee (best type) | con | Coconut
cot | Cotton | cow | Cowpea
csv | Cassava | flx | Flax fibre
fml | Foxtail millet | grd | Groundnut
grm | Gram | jtr | Jatropha
mis | Miscanthus | mlt | Millet (best type)
mze | Maize, grain | mzs | Silage maize
nap | Napier grass | oat | Oat
olp | Oil palm | olv | Olive
oni | Onion | pea | Dry pea
phb | Phaseolous bean | pig | Pigeonpea
pml | Pearl millet | pst | Pasture
rcd | Dryland rice | rcg | Reed canary grass
rcw | Wetland rice | rsd | Rapeseed
rub | Rubber | rye | Rye
sfl | Sunflower | soy | Soybean
spo | Sweet potato | srg | Sorghum, grain
sub | Sugar beet | suc | Sugar cane
swg | Switchgrass | tea | Tea (best type)
tob | Tobacco | tom | Tomato
whe | Wheat | wpo | White potato
yam | Yam (best type) |   |  



