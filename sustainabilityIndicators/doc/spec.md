<!-- 10-Header -->  
Entity: leather  
===============<!-- /10-Header -->  
<!-- 15-License -->  
[Open License](https://github.com/smart-data-models//circuloos_data_model/blob/master/leather/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Global description: **Represents the environmental indicators calculated by GRETA using EF 3.1 methodology**  
version: 0.1.0  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## List of properties  

<sup><sub>[*] If there is not a type in an attribute is because it could have several types or different formats/patterns</sub></sup>  
- `acidificationAccumulatedExceedanceAE[object]`: Acidification refers to the process where emissions of sulfur dioxide (SO₂), nitrogen oxides (NOₓ), and ammonia (NH₃) lead to the formation of acidic compounds in the atmosphere, which then deposit in soils and water bodies, reducing pH levels. This indicator measures the potential impact of these emissions on ecosystems, using an accumulated exceedance approach to assess how much ecosystems can tolerate before damage occurs.  	- `observedAt[date-time]`: Timestamp when the value was observed    
	- `unitCode[string]`: Unit of measurement for acidificationAccumulatedExceedanceAE    
	- `value[number]`: acidificationAccumulatedExceedanceAE value    
- `climateChangeBiogenicGWP100[object]`: This measures the global warming potential of biogenic (plant-derived) carbon emissions over a 100-year period, which includes CO₂ released from the combustion or decomposition of biomass. Biogenic emissions are distinguished from fossil emissions, with a focus on the carbon cycle of living organisms.  	- `observedAt[date-time]`: Timestamp when the value was observed    
	- `unitCode[string]`: Unit of measurement for climateChangeBiogenicGWP100    
	- `value[number]`: climateChangeBiogenicGWP100 value    
- `climateChangeFossilGWP100[object]`: This indicator measures the global warming potential from fossil fuel-derived emissions, such as CO₂ from coal, oil, and natural gas combustion. It captures the long-term impact of these emissions on climate change, expressed in kilograms of CO₂-equivalents over a 100-year period.  	- `observedAt[date-time]`: Timestamp when the value was observed    
	- `unitCode[string]`: Unit of measurement for climateChangeFossilGWP100    
	- `value[number]`: climateChangeFossilGWP100 value    
- `climateChangeGlobalWarmingPotentialGWP[object]`: This indicator measures the contribution of greenhouse gas emissions to global warming over a 100-year timeframe, expressed in kilograms of CO₂-equivalent. It accounts for all major greenhouse gases such as carbon dioxide (CO₂), methane (CH₄), and nitrous oxide (N₂O), each normalized to its global warming potential.  	- `observedAt[date-time]`: Timestamp when the value was observed    
	- `unitCode[string]`: Unit of measurement for climateChangeGlobalWarmingPotentialGWP    
	- `value[number]`: climateChangeGlobalWarmingPotentialGWP value    
- `climateChangeLandUseAndLULUCGWP[object]`: Land use and land use change (LULUC) impacts on climate change refer to greenhouse gas emissions caused by deforestation, land conversion for agriculture, and other changes in land use. This indicator measures the potential warming effect of land use-related CO₂ emissions over 100 years.  	- `observedAt[date-time]`: Timestamp when the value was observed    
	- `unitCode[string]`: Unit of measurement for climateChangeLandUseAndLULUCGWP    
	- `value[number]`: climateChangeLandUseAndLULUCGWP value    
- `ecotoxicityFreshwaterComparativeToxicCTU[object]`: This indicator measures the potential harm of chemical substances released into freshwater ecosystems. It quantifies the toxicity of substances (e.g., heavy metals, pesticides) to aquatic organisms, expressed in Comparative Toxic Units for ecosystems (CTUe). It evaluates the impact on biodiversity and ecosystem health.  	- `observedAt[date-time]`: Timestamp when the value was observed    
	- `unitCode[string]`: Unit of measurement for ecotoxicityFreshwaterComparativeToxicCTU    
	- `value[number]`: ecotoxicityFreshwaterComparativeToxicCTU value    
- `ecotoxicityFreshwaterInorganicsCTUe[object]`: This indicator focuses on the toxicity of inorganic chemical pollutants, such as heavy metals and minerals, in freshwater ecosystems. It assesses the potential for harm to aquatic life due to exposure to these inorganic substances, expressed in CTUe.  	- `observedAt[date-time]`: Timestamp when the value was observed    
	- `unitCode[string]`: Unit of measurement for ecotoxicityFreshwaterInorganicsCTUe    
	- `value[number]`: ecotoxicityFreshwaterInorganicsCTUe value    
- `ecotoxicityFreshwaterOrganicsCTUe[object]`: This measures the toxicity of organic pollutants, including pesticides, herbicides, and other organic chemicals, in freshwater environments. These pollutants may disrupt aquatic ecosystems and harm species, with impacts measured in Comparative Toxic Units for ecosystems (CTUe).  	- `observedAt[date-time]`: Timestamp when the value was observed    
	- `unitCode[string]`: Unit of measurement for ecotoxicityFreshwaterOrganicsCTUe    
	- `value[number]`: ecotoxicityFreshwaterOrganicsCTUe value    
- `energyResourcesAbioticDepletionFossils[object]`: This indicator measures the depletion of non-renewable energy resources, primarily fossil fuels (oil, coal, natural gas). It reflects the consumption of these resources and the impact on their long-term availability, expressed in megajoules (MJ), focusing on energy content and environmental sustainability.  	- `observedAt[date-time]`: Timestamp when the value was observed    
	- `unitCode[string]`: Unit of measurement for energyResourcesAbioticDepletionFossils    
	- `value[number]`: energyResourcesAbioticDepletionFossils value    
- `eutrophicationFreshwaterNutrientsP[object]`: Freshwater eutrophication occurs when excessive nutrients, especially phosphorus (P), enter water bodies, leading to algal blooms and oxygen depletion. This indicator measures the potential for nutrient pollution to cause eutrophication, expressed in kilograms of phosphorus equivalents (kg P-Eq).  	- `observedAt[date-time]`: Timestamp when the value was observed    
	- `unitCode[string]`: Unit of measurement for eutrophicationFreshwaterNutrientsP    
	- `value[number]`: eutrophicationFreshwaterNutrientsP value    
- `eutrophicationMarineNutrientsN[object]`: Marine eutrophication is caused by nitrogen (N) pollution, which can lead to harmful algal blooms in oceans and coastal waters. This indicator measures the impact of nitrogen runoff on marine ecosystems, expressed in kilograms of nitrogen equivalents (kg N-Eq).  	- `observedAt[date-time]`: Timestamp when the value was observed    
	- `unitCode[string]`: Unit of measurement for eutrophicationMarineNutrientsN    
	- `value[number]`: eutrophicationMarineNutrientsN value    
- `eutrophicationTerrestrialAccumExceedance[object]`: This measures the impact of nutrient pollution, particularly nitrogen, on terrestrial ecosystems. It assesses the potential for nutrient accumulation to exceed the natural capacity of the land, leading to changes in vegetation and soil degradation, expressed in mol N-Eq.  	- `observedAt[date-time]`: Timestamp when the value was observed    
	- `unitCode[string]`: Unit of measurement for eutrophicationTerrestrialAccumExceedance    
	- `value[number]`: eutrophicationTerrestrialAccumExceedance value    
- `humanToxicityCarcinogenicCTUh[object]`: This indicator assesses the potential impact of exposure to carcinogenic substances on human health. It is expressed in Comparative Toxic Units for humans (CTUh) and measures the risk of developing cancer from exposure to various chemicals, such as heavy metals, industrial solvents, and certain organic compounds.  	- `observedAt[date-time]`: Timestamp when the value was observed    
	- `unitCode[string]`: Unit of measurement for humanToxicityCarcinogenicCTUh    
	- `value[number]`: humanToxicityCarcinogenicCTUh value    
- `humanToxicityCarcinogenicInorganicsCTU[object]`: This focuses on the carcinogenic risks to humans from exposure to inorganic substances, such as arsenic, lead, and other heavy metals. It evaluates the potential harm in terms of cancer development, expressed in CTUh.  	- `observedAt[date-time]`: Timestamp when the value was observed    
	- `unitCode[string]`: Unit of measurement for humanToxicityCarcinogenicInorganicsCTU    
	- `value[number]`: humanToxicityCarcinogenicInorganicsCTU value    
- `humanToxicityCarcinogenicOrganicsCTU[object]`: This indicator assesses the carcinogenic potential of organic chemical substances, such as formaldehyde, benzene, and pesticides, on human health. It evaluates the risk of cancer associated with exposure to these compounds, expressed in CTUh.  	- `observedAt[date-time]`: Timestamp when the value was observed    
	- `unitCode[string]`: Unit of measurement for humanToxicityCarcinogenicOrganicsCTU    
	- `value[number]`: humanToxicityCarcinogenicOrganicsCTU value    
- `humanToxicityNonCarcinogenicCTUh[object]`: This indicator measures the potential risk to human health from non-carcinogenic substances. It assesses the likelihood of harm such as organ damage or neurological effects from exposure to chemicals, expressed in CTUh.  	- `observedAt[date-time]`: Timestamp when the value was observed    
	- `unitCode[string]`: Unit of measurement for humanToxicityNonCarcinogenicCTUh    
	- `value[number]`: humanToxicityNonCarcinogenicCTUh value    
- `humanToxicityNonCarcinogenicInorganicsCTU[object]`: This focuses on non-carcinogenic health risks from inorganic substances, including heavy metals like cadmium and lead. It evaluates the impact of these chemicals on human health, expressed in CTUh.  	- `observedAt[date-time]`: Timestamp when the value was observed    
	- `unitCode[string]`: Unit of measurement for humanToxicityNonCarcinogenicInorganicsCTU    
	- `value[number]`: humanToxicityNonCarcinogenicInorganicsCTU value    
- `humanToxicityNonCarcinogenicOrganicsCTU[object]`: This indicator assesses the non-carcinogenic health risks posed by organic substances, including solvents, pesticides, and other chemicals. It measures the potential for organ damage or other chronic effects, expressed in CTUh.  	- `observedAt[date-time]`: Timestamp when the value was observed    
	- `unitCode[string]`: Unit of measurement for humanToxicityNonCarcinogenicOrganicsCTU    
	- `value[number]`: humanToxicityNonCarcinogenicOrganicsCTU value    
- `id[string]`: Unique identifier for the entity  - `ionisingRadiationHumanHealthU235[object]`: This measures the potential health impact of ionizing radiation exposure on humans. It is based on the efficiency of radiation exposure relative to uranium-235 (U235), expressed in kilobecquerels (kBq). This indicator focuses on risks such as radiation sickness or long-term health effects like cancer.  	- `observedAt[date-time]`: Timestamp when the value was observed    
	- `unitCode[string]`: Unit of measurement for ionisingRadiationHumanHealthU235    
	- `value[number]`: ionisingRadiationHumanHealthU235 value    
- `landUseSoilQualityIndex[object]`: This indicator evaluates the impact of land use on soil quality, taking into account factors such as organic carbon content, nutrient availability, and erosion potential. It provides a measure of how land use practices affect soil health and sustainability.  	- `observedAt[date-time]`: Timestamp when the value was observed    
	- `unitCode[string]`: Unit of measurement for landUseSoilQualityIndex    
	- `value[number]`: landUseSoilQualityIndex value    
- `materialResourcesAbioticDepletionElements[object]`: This indicator measures the depletion of non-renewable material resources, particularly metals and minerals (e.g., copper, zinc, antimony). It reflects the long-term availability of these elements and the environmental impact of their extraction, expressed in kilograms of antimony equivalents (kg Sb-Eq).  	- `observedAt[date-time]`: Timestamp when the value was observed    
	- `unitCode[string]`: Unit of measurement for materialResourcesAbioticDepletionElements    
	- `value[number]`: materialResourcesAbioticDepletionElements value    
- `ozoneDepletionPotentialODP[object]`: This indicator measures the potential for chemical substances to deplete the stratospheric ozone layer. It is expressed in kilograms of CFC-11 equivalents (kg CFC-11-Eq), focusing on substances like chlorofluorocarbons (CFCs) that contribute to ozone layer depletion.  	- `observedAt[date-time]`: Timestamp when the value was observed    
	- `unitCode[string]`: Unit of measurement for ozoneDepletionPotentialODP    
	- `value[number]`: ozoneDepletionPotentialODP value    
- `particulateMatterFormationHealth[object]`: This indicator assesses the impact of particulate matter (PM) emissions on human health. Particulates such as PM10 and PM2.5 can penetrate the respiratory system, causing conditions like asthma, bronchitis, and cardiovascular diseases. This is expressed in disease incidence cases.  	- `observedAt[date-time]`: Timestamp when the value was observed    
	- `unitCode[string]`: Unit of measurement for particulateMatterFormationHealth    
	- `value[number]`: particulateMatterFormationHealth value    
- `photochemicalOxidantFormationHealth[object]`: This measures the impact of emissions of volatile organic compounds (VOCs) and nitrogen oxides (NOx) that lead to the formation of ground-level ozone (smog), which affects human respiratory health. It is expressed in kilograms of NMVOC equivalents (kg NMVOC-Eq).  	- `observedAt[date-time]`: Timestamp when the value was observed    
	- `unitCode[string]`: Unit of measurement for photochemicalOxidantFormationHealth    
	- `value[number]`: photochemicalOxidantFormationHealth value    
- `waterUseUserDeprivationPotential[object]`: This indicator evaluates the potential for water consumption to lead to human water deprivation, considering local water scarcity and water use efficiency. It is expressed in cubic meters of world equivalents deprived (m³ world Eq. deprived).  	- `observedAt[date-time]`: Timestamp when the value was observed    
	- `unitCode[string]`: Unit of measurement for waterUseUserDeprivationPotential    
	- `value[number]`: waterUseUserDeprivationPotential value    
<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Required properties  
- `acidificationAccumulatedExceedanceAE`  - `climateChangeBiogenicGWP100`  - `climateChangeFossilGWP100`  - `climateChangeGlobalWarmingPotentialGWP`  - `climateChangeLandUseAndLULUCGWP`  - `ecotoxicityFreshwaterComparativeToxicCTU`  - `ecotoxicityFreshwaterInorganicsCTUe`  - `ecotoxicityFreshwaterOrganicsCTUe`  - `energyResourcesAbioticDepletionFossils`  - `eutrophicationFreshwaterNutrientsP`  - `eutrophicationMarineNutrientsN`  - `eutrophicationTerrestrialAccumExceedance`  - `humanToxicityCarcinogenicCTUh`  - `humanToxicityCarcinogenicInorganicsCTU`  - `humanToxicityCarcinogenicOrganicsCTU`  - `humanToxicityNonCarcinogenicCTUh`  - `humanToxicityNonCarcinogenicInorganicsCTU`  - `humanToxicityNonCarcinogenicOrganicsCTU`  - `id`  - `ionisingRadiationHumanHealthU235`  - `landUseSoilQualityIndex`  - `materialResourcesAbioticDepletionElements`  - `ozoneDepletionPotentialODP`  - `particulateMatterFormationHealth`  - `photochemicalOxidantFormationHealth`  - `waterUseUserDeprivationPotential`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Data Model description of properties  
Sorted alphabetically (click for details)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
leather:    
  description: Represents the environmental indicators calculated by GRETA using EF 3.1 methodology    
  properties:    
    acidificationAccumulatedExceedanceAE:    
      description: Acidification refers to the process where emissions of sulfur dioxide (SO₂), nitrogen oxides (NOₓ), and ammonia (NH₃) lead to the formation of acidic compounds in the atmosphere, which then deposit in soils and water bodies, reducing pH levels. This indicator measures the potential impact of these emissions on ecosystems, using an accumulated exceedance approach to assess how much ecosystems can tolerate before damage occurs.    
      properties:    
        observedAt:    
          description: Timestamp when the value was observed    
          format: date-time    
          type: string    
        unitCode:    
          description: Unit of measurement for acidificationAccumulatedExceedanceAE    
          type: string    
        value:    
          description: acidificationAccumulatedExceedanceAE value    
          type: number    
      required:    
        - value    
        - unitCode    
      type: object    
    climateChangeBiogenicGWP100:    
      description: This measures the global warming potential of biogenic (plant-derived) carbon emissions over a 100-year period, which includes CO₂ released from the combustion or decomposition of biomass. Biogenic emissions are distinguished from fossil emissions, with a focus on the carbon cycle of living organisms.    
      properties:    
        observedAt:    
          description: Timestamp when the value was observed    
          format: date-time    
          type: string    
        unitCode:    
          description: Unit of measurement for climateChangeBiogenicGWP100    
          type: string    
        value:    
          description: climateChangeBiogenicGWP100 value    
          type: number    
      required:    
        - value    
        - unitCode    
      type: object    
    climateChangeFossilGWP100:    
      description: This indicator measures the global warming potential from fossil fuel-derived emissions, such as CO₂ from coal, oil, and natural gas combustion. It captures the long-term impact of these emissions on climate change, expressed in kilograms of CO₂-equivalents over a 100-year period.    
      properties:    
        observedAt:    
          description: Timestamp when the value was observed    
          format: date-time    
          type: string    
        unitCode:    
          description: Unit of measurement for climateChangeFossilGWP100    
          type: string    
        value:    
          description: climateChangeFossilGWP100 value    
          type: number    
      required:    
        - value    
        - unitCode    
      type: object    
    climateChangeGlobalWarmingPotentialGWP:    
      description: This indicator measures the contribution of greenhouse gas emissions to global warming over a 100-year timeframe, expressed in kilograms of CO₂-equivalent. It accounts for all major greenhouse gases such as carbon dioxide (CO₂), methane (CH₄), and nitrous oxide (N₂O), each normalized to its global warming potential.    
      properties:    
        observedAt:    
          description: Timestamp when the value was observed    
          format: date-time    
          type: string    
        unitCode:    
          description: Unit of measurement for climateChangeGlobalWarmingPotentialGWP    
          type: string    
        value:    
          description: climateChangeGlobalWarmingPotentialGWP value    
          type: number    
      required:    
        - value    
        - unitCode    
      type: object    
    climateChangeLandUseAndLULUCGWP:    
      description: Land use and land use change (LULUC) impacts on climate change refer to greenhouse gas emissions caused by deforestation, land conversion for agriculture, and other changes in land use. This indicator measures the potential warming effect of land use-related CO₂ emissions over 100 years.    
      properties:    
        observedAt:    
          description: Timestamp when the value was observed    
          format: date-time    
          type: string    
        unitCode:    
          description: Unit of measurement for climateChangeLandUseAndLULUCGWP    
          type: string    
        value:    
          description: climateChangeLandUseAndLULUCGWP value    
          type: number    
      required:    
        - value    
        - unitCode    
      type: object    
    ecotoxicityFreshwaterComparativeToxicCTU:    
      description: This indicator measures the potential harm of chemical substances released into freshwater ecosystems. It quantifies the toxicity of substances (e.g., heavy metals, pesticides) to aquatic organisms, expressed in Comparative Toxic Units for ecosystems (CTUe). It evaluates the impact on biodiversity and ecosystem health.    
      properties:    
        observedAt:    
          description: Timestamp when the value was observed    
          format: date-time    
          type: string    
        unitCode:    
          description: Unit of measurement for ecotoxicityFreshwaterComparativeToxicCTU    
          type: string    
        value:    
          description: ecotoxicityFreshwaterComparativeToxicCTU value    
          type: number    
      required:    
        - value    
        - unitCode    
      type: object    
    ecotoxicityFreshwaterInorganicsCTUe:    
      description: This indicator focuses on the toxicity of inorganic chemical pollutants, such as heavy metals and minerals, in freshwater ecosystems. It assesses the potential for harm to aquatic life due to exposure to these inorganic substances, expressed in CTUe.    
      properties:    
        observedAt:    
          description: Timestamp when the value was observed    
          format: date-time    
          type: string    
        unitCode:    
          description: Unit of measurement for ecotoxicityFreshwaterInorganicsCTUe    
          type: string    
        value:    
          description: ecotoxicityFreshwaterInorganicsCTUe value    
          type: number    
      required:    
        - value    
        - unitCode    
      type: object    
    ecotoxicityFreshwaterOrganicsCTUe:    
      description: This measures the toxicity of organic pollutants, including pesticides, herbicides, and other organic chemicals, in freshwater environments. These pollutants may disrupt aquatic ecosystems and harm species, with impacts measured in Comparative Toxic Units for ecosystems (CTUe).    
      properties:    
        observedAt:    
          description: Timestamp when the value was observed    
          format: date-time    
          type: string    
        unitCode:    
          description: Unit of measurement for ecotoxicityFreshwaterOrganicsCTUe    
          type: string    
        value:    
          description: ecotoxicityFreshwaterOrganicsCTUe value    
          type: number    
      required:    
        - value    
        - unitCode    
      type: object    
    energyResourcesAbioticDepletionFossils:    
      description: This indicator measures the depletion of non-renewable energy resources, primarily fossil fuels (oil, coal, natural gas). It reflects the consumption of these resources and the impact on their long-term availability, expressed in megajoules (MJ), focusing on energy content and environmental sustainability.    
      properties:    
        observedAt:    
          description: Timestamp when the value was observed    
          format: date-time    
          type: string    
        unitCode:    
          description: Unit of measurement for energyResourcesAbioticDepletionFossils    
          type: string    
        value:    
          description: energyResourcesAbioticDepletionFossils value    
          type: number    
      required:    
        - value    
        - unitCode    
      type: object    
    eutrophicationFreshwaterNutrientsP:    
      description: Freshwater eutrophication occurs when excessive nutrients, especially phosphorus (P), enter water bodies, leading to algal blooms and oxygen depletion. This indicator measures the potential for nutrient pollution to cause eutrophication, expressed in kilograms of phosphorus equivalents (kg P-Eq).    
      properties:    
        observedAt:    
          description: Timestamp when the value was observed    
          format: date-time    
          type: string    
        unitCode:    
          description: Unit of measurement for eutrophicationFreshwaterNutrientsP    
          type: string    
        value:    
          description: eutrophicationFreshwaterNutrientsP value    
          type: number    
      required:    
        - value    
        - unitCode    
      type: object    
    eutrophicationMarineNutrientsN:    
      description: Marine eutrophication is caused by nitrogen (N) pollution, which can lead to harmful algal blooms in oceans and coastal waters. This indicator measures the impact of nitrogen runoff on marine ecosystems, expressed in kilograms of nitrogen equivalents (kg N-Eq).    
      properties:    
        observedAt:    
          description: Timestamp when the value was observed    
          format: date-time    
          type: string    
        unitCode:    
          description: Unit of measurement for eutrophicationMarineNutrientsN    
          type: string    
        value:    
          description: eutrophicationMarineNutrientsN value    
          type: number    
      required:    
        - value    
        - unitCode    
      type: object    
    eutrophicationTerrestrialAccumExceedance:    
      description: This measures the impact of nutrient pollution, particularly nitrogen, on terrestrial ecosystems. It assesses the potential for nutrient accumulation to exceed the natural capacity of the land, leading to changes in vegetation and soil degradation, expressed in mol N-Eq.    
      properties:    
        observedAt:    
          description: Timestamp when the value was observed    
          format: date-time    
          type: string    
        unitCode:    
          description: Unit of measurement for eutrophicationTerrestrialAccumExceedance    
          type: string    
        value:    
          description: eutrophicationTerrestrialAccumExceedance value    
          type: number    
      required:    
        - value    
        - unitCode    
      type: object    
    humanToxicityCarcinogenicCTUh:    
      description: This indicator assesses the potential impact of exposure to carcinogenic substances on human health. It is expressed in Comparative Toxic Units for humans (CTUh) and measures the risk of developing cancer from exposure to various chemicals, such as heavy metals, industrial solvents, and certain organic compounds.    
      properties:    
        observedAt:    
          description: Timestamp when the value was observed    
          format: date-time    
          type: string    
        unitCode:    
          description: Unit of measurement for humanToxicityCarcinogenicCTUh    
          type: string    
        value:    
          description: humanToxicityCarcinogenicCTUh value    
          type: number    
      required:    
        - value    
        - unitCode    
      type: object    
    humanToxicityCarcinogenicInorganicsCTU:    
      description: This focuses on the carcinogenic risks to humans from exposure to inorganic substances, such as arsenic, lead, and other heavy metals. It evaluates the potential harm in terms of cancer development, expressed in CTUh.    
      properties:    
        observedAt:    
          description: Timestamp when the value was observed    
          format: date-time    
          type: string    
        unitCode:    
          description: Unit of measurement for humanToxicityCarcinogenicInorganicsCTU    
          type: string    
        value:    
          description: humanToxicityCarcinogenicInorganicsCTU value    
          type: number    
      required:    
        - value    
        - unitCode    
      type: object    
    humanToxicityCarcinogenicOrganicsCTU:    
      description: This indicator assesses the carcinogenic potential of organic chemical substances, such as formaldehyde, benzene, and pesticides, on human health. It evaluates the risk of cancer associated with exposure to these compounds, expressed in CTUh.    
      properties:    
        observedAt:    
          description: Timestamp when the value was observed    
          format: date-time    
          type: string    
        unitCode:    
          description: Unit of measurement for humanToxicityCarcinogenicOrganicsCTU    
          type: string    
        value:    
          description: humanToxicityCarcinogenicOrganicsCTU value    
          type: number    
      required:    
        - value    
        - unitCode    
      type: object    
    humanToxicityNonCarcinogenicCTUh:    
      description: This indicator measures the potential risk to human health from non-carcinogenic substances. It assesses the likelihood of harm such as organ damage or neurological effects from exposure to chemicals, expressed in CTUh.    
      properties:    
        observedAt:    
          description: Timestamp when the value was observed    
          format: date-time    
          type: string    
        unitCode:    
          description: Unit of measurement for humanToxicityNonCarcinogenicCTUh    
          type: string    
        value:    
          description: humanToxicityNonCarcinogenicCTUh value    
          type: number    
      required:    
        - value    
        - unitCode    
      type: object    
    humanToxicityNonCarcinogenicInorganicsCTU:    
      description: This focuses on non-carcinogenic health risks from inorganic substances, including heavy metals like cadmium and lead. It evaluates the impact of these chemicals on human health, expressed in CTUh.    
      properties:    
        observedAt:    
          description: Timestamp when the value was observed    
          format: date-time    
          type: string    
        unitCode:    
          description: Unit of measurement for humanToxicityNonCarcinogenicInorganicsCTU    
          type: string    
        value:    
          description: humanToxicityNonCarcinogenicInorganicsCTU value    
          type: number    
      required:    
        - value    
        - unitCode    
      type: object    
    humanToxicityNonCarcinogenicOrganicsCTU:    
      description: This indicator assesses the non-carcinogenic health risks posed by organic substances, including solvents, pesticides, and other chemicals. It measures the potential for organ damage or other chronic effects, expressed in CTUh.    
      properties:    
        observedAt:    
          description: Timestamp when the value was observed    
          format: date-time    
          type: string    
        unitCode:    
          description: Unit of measurement for humanToxicityNonCarcinogenicOrganicsCTU    
          type: string    
        value:    
          description: humanToxicityNonCarcinogenicOrganicsCTU value    
          type: number    
      required:    
        - value    
        - unitCode    
      type: object    
    id:    
      description: Unique identifier for the entity    
      type: string    
    ionisingRadiationHumanHealthU235:    
      description: This measures the potential health impact of ionizing radiation exposure on humans. It is based on the efficiency of radiation exposure relative to uranium-235 (U235), expressed in kilobecquerels (kBq). This indicator focuses on risks such as radiation sickness or long-term health effects like cancer.    
      properties:    
        observedAt:    
          description: Timestamp when the value was observed    
          format: date-time    
          type: string    
        unitCode:    
          description: Unit of measurement for ionisingRadiationHumanHealthU235    
          type: string    
        value:    
          description: ionisingRadiationHumanHealthU235 value    
          type: number    
      required:    
        - value    
        - unitCode    
      type: object    
    landUseSoilQualityIndex:    
      description: This indicator evaluates the impact of land use on soil quality, taking into account factors such as organic carbon content, nutrient availability, and erosion potential. It provides a measure of how land use practices affect soil health and sustainability.    
      properties:    
        observedAt:    
          description: Timestamp when the value was observed    
          format: date-time    
          type: string    
        unitCode:    
          description: Unit of measurement for landUseSoilQualityIndex    
          type: string    
        value:    
          description: landUseSoilQualityIndex value    
          type: number    
      required:    
        - value    
        - unitCode    
      type: object    
    materialResourcesAbioticDepletionElements:    
      description: This indicator measures the depletion of non-renewable material resources, particularly metals and minerals (e.g., copper, zinc, antimony). It reflects the long-term availability of these elements and the environmental impact of their extraction, expressed in kilograms of antimony equivalents (kg Sb-Eq).    
      properties:    
        observedAt:    
          description: Timestamp when the value was observed    
          format: date-time    
          type: string    
        unitCode:    
          description: Unit of measurement for materialResourcesAbioticDepletionElements    
          type: string    
        value:    
          description: materialResourcesAbioticDepletionElements value    
          type: number    
      required:    
        - value    
        - unitCode    
      type: object    
    ozoneDepletionPotentialODP:    
      description: This indicator measures the potential for chemical substances to deplete the stratospheric ozone layer. It is expressed in kilograms of CFC-11 equivalents (kg CFC-11-Eq), focusing on substances like chlorofluorocarbons (CFCs) that contribute to ozone layer depletion.    
      properties:    
        observedAt:    
          description: Timestamp when the value was observed    
          format: date-time    
          type: string    
        unitCode:    
          description: Unit of measurement for ozoneDepletionPotentialODP    
          type: string    
        value:    
          description: ozoneDepletionPotentialODP value    
          type: number    
      required:    
        - value    
        - unitCode    
      type: object    
    particulateMatterFormationHealth:    
      description: This indicator assesses the impact of particulate matter (PM) emissions on human health. Particulates such as PM10 and PM2.5 can penetrate the respiratory system, causing conditions like asthma, bronchitis, and cardiovascular diseases. This is expressed in disease incidence cases.    
      properties:    
        observedAt:    
          description: Timestamp when the value was observed    
          format: date-time    
          type: string    
        unitCode:    
          description: Unit of measurement for particulateMatterFormationHealth    
          type: string    
        value:    
          description: particulateMatterFormationHealth value    
          type: number    
      required:    
        - value    
        - unitCode    
      type: object    
    photochemicalOxidantFormationHealth:    
      description: This measures the impact of emissions of volatile organic compounds (VOCs) and nitrogen oxides (NOx) that lead to the formation of ground-level ozone (smog), which affects human respiratory health. It is expressed in kilograms of NMVOC equivalents (kg NMVOC-Eq).    
      properties:    
        observedAt:    
          description: Timestamp when the value was observed    
          format: date-time    
          type: string    
        unitCode:    
          description: Unit of measurement for photochemicalOxidantFormationHealth    
          type: string    
        value:    
          description: photochemicalOxidantFormationHealth value    
          type: number    
      required:    
        - value    
        - unitCode    
      type: object    
    waterUseUserDeprivationPotential:    
      description: This indicator evaluates the potential for water consumption to lead to human water deprivation, considering local water scarcity and water use efficiency. It is expressed in cubic meters of world equivalents deprived (m³ world Eq. deprived).    
      properties:    
        observedAt:    
          description: Timestamp when the value was observed    
          format: date-time    
          type: string    
        unitCode:    
          description: Unit of measurement for waterUseUserDeprivationPotential    
          type: string    
        value:    
          description: waterUseUserDeprivationPotential value    
          type: number    
      required:    
        - value    
        - unitCode    
      type: object    
  required:    
    - id    
    - acidificationAccumulatedExceedanceAE    
    - climateChangeGlobalWarmingPotentialGWP    
    - climateChangeBiogenicGWP100    
    - climateChangeFossilGWP100    
    - climateChangeLandUseAndLULUCGWP    
    - ecotoxicityFreshwaterComparativeToxicCTU    
    - ecotoxicityFreshwaterInorganicsCTUe    
    - ecotoxicityFreshwaterOrganicsCTUe    
    - energyResourcesAbioticDepletionFossils    
    - eutrophicationFreshwaterNutrientsP    
    - eutrophicationMarineNutrientsN    
    - eutrophicationTerrestrialAccumExceedance    
    - humanToxicityCarcinogenicCTUh    
    - humanToxicityCarcinogenicInorganicsCTU    
    - humanToxicityCarcinogenicOrganicsCTU    
    - humanToxicityNonCarcinogenicCTUh    
    - humanToxicityNonCarcinogenicInorganicsCTU    
    - humanToxicityNonCarcinogenicOrganicsCTU    
    - ionisingRadiationHumanHealthU235    
    - landUseSoilQualityIndex    
    - materialResourcesAbioticDepletionElements    
    - ozoneDepletionPotentialODP    
    - particulateMatterFormationHealth    
    - photochemicalOxidantFormationHealth    
    - waterUseUserDeprivationPotential    
  type: object    
  x-derived-from: ''    
  x-disclaimer: Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program    
  x-license-url: https://github.com/smart-data-models/circuloos_data_model/blob/master/leather/LICENSE.md    
  x-model-schema: https://raw.githubusercontent.com/TO_ADD_LATER/schema.json    
  x-model-tags: Environmental indicators    
  x-version: 0.1.0    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Example payloads    
Not available the example of a leather in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
#### leather NGSI-LD normalized Example    
Here is an example of a leather in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "entity-001",  
  "acidificationAccumulatedExceedanceAE": {  
    "value": 345.67,  
    "unitCode": "XMHQ",  // UNECE unit for mol H+-Eq  
    "observedAt": "2024-09-25T10:20:30Z"  
  },  
  "climateChangeGlobalWarmingPotentialGWP": {  
    "value": 1234.56,  
    "unitCode": "XCO2",  // UNECE unit for kg CO2 equivalent  
    "observedAt": "2024-09-25T12:34:56Z"  
  },  
  "climateChangeBiogenicGWP100": {  
    "value": 98.76,  
    "unitCode": "XCO2",  // UNECE unit for kg CO2 equivalent  
    "observedAt": "2024-09-24T15:45:00Z"  
  },  
  "climateChangeFossilGWP100": {  
    "value": 567.89,  
    "unitCode": "XCO2",  // UNECE unit for kg CO2 equivalent  
    "observedAt": "2024-09-23T10:45:00Z"  
  },  
  "climateChangeLandUseAndLULUCGWP": {  
    "value": 432.1,  
    "unitCode": "XCO2",  // UNECE unit for kg CO2 equivalent  
    "observedAt": "2024-09-22T11:30:00Z"  
  },  
  "ecotoxicityFreshwaterComparativeToxicCTU": {  
    "value": 876.54,  
    "unitCode": "CTUe",  // UNECE unit for comparative toxic unit  
    "observedAt": "2024-09-22T08:15:00Z"  
  },  
  "ecotoxicityFreshwaterInorganicsCTUe": {  
    "value": 543.21,  
    "unitCode": "CTUe",  // UNECE unit for comparative toxic unit  
    "observedAt": "2024-09-21T09:30:00Z"  
  },  
  "ecotoxicityFreshwaterOrganicsCTUe": {  
    "value": 321.09,  
    "unitCode": "CTUe",  // UNECE unit for comparative toxic unit  
    "observedAt": "2024-09-20T12:00:00Z"  
  },  
  "energyResourcesAbioticDepletionFossils": {  
    "value": 987.65,  
    "unitCode": "MJ",  // UNECE unit for megajoule (energy)  
    "observedAt": "2024-09-19T14:30:00Z"  
  },  
  "eutrophicationFreshwaterNutrientsP": {  
    "value": 0.987,  
    "unitCode": "kg P-Eq",  // UNECE unit for kg phosphorus equivalent  
    "observedAt": "2024-09-18T16:30:00Z"  
  },  
  "eutrophicationMarineNutrientsN": {  
    "value": 0.123,  
    "unitCode": "kg N-Eq",  // UNECE unit for kg nitrogen equivalent  
    "observedAt": "2024-09-17T08:30:00Z"  
  },  
  "eutrophicationTerrestrialAccumExceedance": {  
    "value": 765.43,  
    "unitCode": "mol N-Eq",  // UNECE unit for mol nitrogen equivalent  
    "observedAt": "2024-09-16T10:30:00Z"  
  },  
  "humanToxicityCarcinogenicCTUh": {  
    "value": 56.78,  
    "unitCode": "CTUh",  // UNECE unit for comparative toxic unit  
    "observedAt": "2024-09-15T14:45:00Z"  
  },  
  "humanToxicityCarcinogenicInorganicsCTU": {  
    "value": 12.34,  
    "unitCode": "CTUh",  // UNECE unit for comparative toxic unit  
    "observedAt": "2024-09-14T16:15:00Z"  
  },  
  "humanToxicityCarcinogenicOrganicsCTU": {  
    "value": 34.56,  
    "unitCode": "CTUh",  // UNECE unit for comparative toxic unit  
    "observedAt": "2024-09-13T18:30:00Z"  
  },  
  "humanToxicityNonCarcinogenicCTUh": {  
    "value": 78.90,  
    "unitCode": "CTUh",  // UNECE unit for comparative toxic unit  
    "observedAt": "2024-09-12T08:15:00Z"  
  },  
  "humanToxicityNonCarcinogenicInorganicsCTU": {  
    "value": 65.43,  
    "unitCode": "CTUh",  // UNECE unit for comparative toxic unit  
    "observedAt": "2024-09-11T12:45:00Z"  
  },  
  "humanToxicityNonCarcinogenicOrganicsCTU": {  
    "value": 90.12,  
    "unitCode": "CTUh",  // UNECE unit for comparative toxic unit  
    "observedAt": "2024-09-10T10:45:00Z"  
  },  
  "ionisingRadiationHumanHealthU235": {  
    "value": 76.54,  
    "unitCode": "BQU",  // UNECE unit for becquerel (Bq) U235 equivalent  
    "observedAt": "2024-09-09T09:15:00Z"  
  },  
  "landUseSoilQualityIndex": {  
    "value": 5.43,  
    "unitCode": "M2AQ",  // UNECE unit for m²a crop-equivalent  
    "observedAt": "2024-09-08T07:45:00Z"  
  },  
  "materialResourcesAbioticDepletionElements": {  
    "value": 543.21,  
    "unitCode": "kg Sb-Eq",  // UNECE unit for kg antimony equivalent  
    "observedAt": "2024-09-07T16:00:00Z"  
  },  
  "ozoneDepletionPotentialODP": {  
    "value": 0.0123,  
    "unitCode": "kg CFC-11-Eq",  // UNECE unit for kg CFC-11 equivalent  
    "observedAt": "2024-09-06T14:30:00Z"  
  },  
  "particulateMatterFormationHealth": {  
    "value": 432.10,  
    "unitCode": "kg PM10-Eq",  // UNECE unit for kg particulate matter (PM10)  
    "observedAt": "2024-09-05T13:30:00Z"  
  },  
  "photochemicalOxidantFormationHealth": {  
    "value": 321.98,  
    "unitCode": "kg NMVOC-Eq",  // UNECE unit for kg non-methane VOC  
    "observedAt": "2024-09-04T15:15:00Z"  
  },  
  "waterUseUserDeprivationPotential": {  
    "value": 543.12,  
    "unitCode": "m3 H2O-Eq",  // UNECE unit for cubic meters of water  
    "observedAt": "2024-09-03T18:00:00Z"  
  },  
     "@context": [  
        "https://TOBELater/context.jsonld"  
    ]  
}  
```  
</details><!-- /80-Examples -->  
