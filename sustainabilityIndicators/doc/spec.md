<!-- 10-Header -->  
Entity: environmental_footprint_indicator  
=========================================<!-- /10-Header -->  
<!-- 15-License -->  
[Open License](https://raw.githubusercontent.com/european-dynamics-rnd/CIRCULOOS_Data_model/refs/heads/main/LICENSE)  
<!-- /15-License -->  
<!-- 20-Description -->  
Global description: **Represents the environmental indicators calculated by GRETA using Environmental Footprint 3.1 methodology**  
version: 0.1.0  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## List of properties  

<sup><sub>[*] If there is not a type in an attribute is because it could have several types or different formats/patterns</sub></sup>  
- `acidificationAccumulatedExceedanceAE[*]`: Acidification refers to the process where emissions of sulfur dioxide (SO₂), nitrogen oxides (NOₓ), and ammonia (NH₃) lead to the formation of acidic compounds in the atmosphere, which then deposit in soils and water bodies, reducing pH levels. This indicator measures the potential impact of these emissions on ecosystems, using an accumulated exceedance approach to assess how much ecosystems can tolerate before damage occurs.  - `climateChangeBiogenicGWP100[*]`: This measures the global warming potential of biogenic (plant-derived) carbon emissions over a 100-year period, which includes CO₂ released from the combustion or decomposition of biomass. Biogenic emissions are distinguished from fossil emissions, with a focus on the carbon cycle of living organisms.  - `climateChangeFossilGWP100[*]`: This indicator measures the global warming potential from fossil fuel-derived emissions, such as CO₂ from coal, oil, and natural gas combustion. It captures the long-term impact of these emissions on climate change, expressed in kilograms of CO₂-equivalents over a 100-year period.  - `climateChangeGlobalWarmingPotentialGWP[*]`: This indicator measures the contribution of greenhouse gas emissions to global warming over a 100-year timeframe, expressed in kilograms of CO₂-equivalent. It accounts for all major greenhouse gases such as carbon dioxide (CO₂), methane (CH₄), and nitrous oxide (N₂O), each normalized to its global warming potential.  - `climateChangeLandUseAndLULUCGWP[*]`: Land use and land use change (LULUC) impacts on climate change refer to greenhouse gas emissions caused by deforestation, land conversion for agriculture, and other changes in land use. This indicator measures the potential warming effect of land use-related CO₂ emissions over 100 years.  - `ecotoxicityFreshwaterComparativeToxicCTU[*]`: This indicator measures the potential harm of chemical substances released into freshwater ecosystems. It quantifies the toxicity of substances (e.g., heavy metals, pesticides) to aquatic organisms, expressed in Comparative Toxic Units for ecosystems (CTUe). It evaluates the impact on biodiversity and ecosystem health.  - `ecotoxicityFreshwaterInorganicsCTUe[*]`: This indicator focuses on the toxicity of inorganic chemical pollutants, such as heavy metals and minerals, in freshwater ecosystems. It assesses the potential for harm to aquatic life due to exposure to these inorganic substances, expressed in CTUe.  - `ecotoxicityFreshwaterOrganicsCTUe[*]`: This measures the toxicity of organic pollutants, including pesticides, herbicides, and other organic chemicals, in freshwater environments. These pollutants may disrupt aquatic ecosystems and harm species, with impacts measured in Comparative Toxic Units for ecosystems (CTUe).  - `energyResourcesAbioticDepletionFossils[*]`: This indicator measures the depletion of non-renewable energy resources, primarily fossil fuels (oil, coal, natural gas). It reflects the consumption of these resources and the impact on their long-term availability, expressed in megajoules (MJ), focusing on energy content and environmental sustainability.  - `eutrophicationFreshwaterNutrientsP[*]`: Freshwater eutrophication occurs when excessive nutrients, especially phosphorus (P), enter water bodies, leading to algal blooms and oxygen depletion. This indicator measures the potential for nutrient pollution to cause eutrophication, expressed in kilograms of phosphorus equivalents (kg P-Eq).  - `eutrophicationMarineNutrientsN[*]`: Marine eutrophication is caused by nitrogen (N) pollution, which can lead to harmful algal blooms in oceans and coastal waters. This indicator measures the impact of nitrogen runoff on marine ecosystems, expressed in kilograms of nitrogen equivalents (kg N-Eq).  - `eutrophicationTerrestrialAccumExceedance[*]`: This measures the impact of nutrient pollution, particularly nitrogen, on terrestrial ecosystems. It assesses the potential for nutrient accumulation to exceed the natural capacity of the land, leading to changes in vegetation and soil degradation, expressed in mol N-Eq.  - `humanToxicityCarcinogenicCTUh[*]`: This indicator assesses the potential impact of exposure to carcinogenic substances on human health. It is expressed in Comparative Toxic Units for humans (CTUh) and measures the risk of developing cancer from exposure to various chemicals, such as heavy metals, industrial solvents, and certain organic compounds.  - `humanToxicityCarcinogenicInorganicsCTU[*]`: This focuses on the carcinogenic risks to humans from exposure to inorganic substances, such as arsenic, lead, and other heavy metals. It evaluates the potential harm in terms of cancer development, expressed in CTUh.  - `humanToxicityCarcinogenicOrganicsCTU[*]`: This indicator assesses the carcinogenic potential of organic chemical substances, such as formaldehyde, benzene, and pesticides, on human health. It evaluates the risk of cancer associated with exposure to these compounds, expressed in CTUh.  - `humanToxicityNonCarcinogenicCTUh[*]`: This indicator measures the potential risk to human health from non-carcinogenic substances. It assesses the likelihood of harm such as organ damage or neurological effects from exposure to chemicals, expressed in CTUh.  - `humanToxicityNonCarcinogenicInorganicsCTU[*]`: This focuses on non-carcinogenic health risks from inorganic substances, including heavy metals like cadmium and lead. It evaluates the impact of these chemicals on human health, expressed in CTUh.  - `humanToxicityNonCarcinogenicOrganicsCTU[*]`: This indicator assesses the non-carcinogenic health risks posed by organic substances, including solvents, pesticides, and other chemicals. It measures the potential for organ damage or other chronic effects, expressed in CTUh.  - `id[string]`: Unique identifier for the entity  - `ionisingRadiationHumanHealthU235[*]`: This measures the potential health impact of ionizing radiation exposure on humans. It is based on the efficiency of radiation exposure relative to uranium-235 (U235), expressed in kilobecquerels (kBq). This indicator focuses on risks such as radiation sickness or long-term health effects like cancer.  - `landUseSoilQualityIndex[*]`: This indicator evaluates the impact of land use on soil quality, taking into account factors such as organic carbon content, nutrient availability, and erosion potential. It provides a measure of how land use practices affect soil health and sustainability.  - `materialResourcesAbioticDepletionElements[*]`: This indicator measures the depletion of non-renewable material resources, particularly metals and minerals (e.g., copper, zinc, antimony). It reflects the long-term availability of these elements and the environmental impact of their extraction, expressed in kilograms of antimony equivalents (kg Sb-Eq).  - `ozoneDepletionPotentialODP[*]`: This indicator measures the potential for chemical substances to deplete the stratospheric ozone layer. It is expressed in kilograms of CFC-11 equivalents (kg CFC-11-Eq), focusing on substances like chlorofluorocarbons (CFCs) that contribute to ozone layer depletion.  - `particulateMatterFormationHealth[*]`: This indicator assesses the impact of particulate matter (PM) emissions on human health. Particulates such as PM10 and PM2.5 can penetrate the respiratory system, causing conditions like asthma, bronchitis, and cardiovascular diseases. This is expressed in disease incidence cases.  - `photochemicalOxidantFormationHealth[*]`: This measures the impact of emissions of volatile organic compounds (VOCs) and nitrogen oxides (NOx) that lead to the formation of ground-level ozone (smog), which affects human respiratory health. It is expressed in kilograms of NMVOC equivalents (kg NMVOC-Eq).  - `type[string]`: NGSI Entity type. Type of message published  - `waterUseUserDeprivationPotential[*]`: This indicator evaluates the potential for water consumption to lead to human water deprivation, considering local water scarcity and water use efficiency. It is expressed in cubic meters of world equivalents deprived (m³ world Eq. deprived).  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Required properties  
- `acidificationAccumulatedExceedanceAE`  - `climateChangeBiogenicGWP100`  - `climateChangeFossilGWP100`  - `climateChangeGlobalWarmingPotentialGWP`  - `climateChangeLandUseAndLULUCGWP`  - `ecotoxicityFreshwaterComparativeToxicCTU`  - `ecotoxicityFreshwaterInorganicsCTUe`  - `ecotoxicityFreshwaterOrganicsCTUe`  - `energyResourcesAbioticDepletionFossils`  - `eutrophicationFreshwaterNutrientsP`  - `eutrophicationMarineNutrientsN`  - `eutrophicationTerrestrialAccumExceedance`  - `humanToxicityCarcinogenicCTUh`  - `humanToxicityCarcinogenicInorganicsCTU`  - `humanToxicityCarcinogenicOrganicsCTU`  - `humanToxicityNonCarcinogenicCTUh`  - `humanToxicityNonCarcinogenicInorganicsCTU`  - `humanToxicityNonCarcinogenicOrganicsCTU`  - `id`  - `ionisingRadiationHumanHealthU235`  - `landUseSoilQualityIndex`  - `materialResourcesAbioticDepletionElements`  - `ozoneDepletionPotentialODP`  - `particulateMatterFormationHealth`  - `photochemicalOxidantFormationHealth`  - `type`  - `waterUseUserDeprivationPotential`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Data Model description of properties  
Sorted alphabetically (click for details)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
environmental_footprint_indicator:    
  description: Represents the environmental indicators calculated by GRETA using Environmental Footprint 3.1 methodology    
  properties:    
    acidificationAccumulatedExceedanceAE:    
      anyOf:    
        - description: Property. acidificationAccumulatedExceedanceAE value    
          type: string    
        - properties:    
            observedAt:    
              description: Property. Timestamp when the value was observed    
              format: date-time    
              type: string    
            type:    
              description: Property. NGSI-LD attribute type.    
              enum:    
                - Property    
              type: string    
            unitCode:    
              description: Property. Unit of measurement for acidificationAccumulatedExceedanceAE    
              type: string    
            value:    
              description: Property. acidificationAccumulatedExceedanceAE value    
              type: string    
          required:    
            - type    
            - value    
            - unitCode    
          type: object    
      description: Acidification refers to the process where emissions of sulfur dioxide (SO₂), nitrogen oxides (NOₓ), and ammonia (NH₃) lead to the formation of acidic compounds in the atmosphere, which then deposit in soils and water bodies, reducing pH levels. This indicator measures the potential impact of these emissions on ecosystems, using an accumulated exceedance approach to assess how much ecosystems can tolerate before damage occurs.    
      x-ngsi:    
        type: Property    
    climateChangeBiogenicGWP100:    
      anyOf:    
        - description: Property. climateChangeBiogenicGWP100 value    
          type: string    
        - properties:    
            observedAt:    
              description: Property. Timestamp when the value was observed    
              format: date-time    
              type: string    
            type:    
              description: Property. NGSI-LD attribute type.    
              enum:    
                - Property    
              type: string    
            unitCode:    
              description: Property. Unit of measurement for climateChangeBiogenicGWP100    
              type: string    
            value:    
              description: Property. climateChangeBiogenicGWP100 value    
              type: string    
          required:    
            - type    
            - value    
            - unitCode    
          type: object    
      description: This measures the global warming potential of biogenic (plant-derived) carbon emissions over a 100-year period, which includes CO₂ released from the combustion or decomposition of biomass. Biogenic emissions are distinguished from fossil emissions, with a focus on the carbon cycle of living organisms.    
      x-ngsi:    
        type: Property    
    climateChangeFossilGWP100:    
      anyOf:    
        - description: Property. climateChangeFossilGWP100 value    
          type: string    
        - properties:    
            observedAt:    
              description: Property. Timestamp when the value was observed    
              format: date-time    
              type: string    
            type:    
              description: Property. NGSI-LD attribute type.    
              enum:    
                - Property    
              type: string    
            unitCode:    
              description: Property. Unit of measurement for climateChangeFossilGWP100    
              type: string    
            value:    
              description: Property. climateChangeFossilGWP100 value    
              type: string    
          required:    
            - type    
            - value    
            - unitCode    
          type: object    
      description: This indicator measures the global warming potential from fossil fuel-derived emissions, such as CO₂ from coal, oil, and natural gas combustion. It captures the long-term impact of these emissions on climate change, expressed in kilograms of CO₂-equivalents over a 100-year period.    
      x-ngsi:    
        type: Property    
    climateChangeGlobalWarmingPotentialGWP:    
      anyOf:    
        - description: Property. climateChangeGlobalWarmingPotentialGWP value    
          type: string    
        - properties:    
            observedAt:    
              description: Property. Timestamp when the value was observed    
              format: date-time    
              type: string    
            type:    
              description: Property. NGSI-LD attribute type.    
              enum:    
                - Property    
              type: string    
            unitCode:    
              description: Property. Unit of measurement for climateChangeGlobalWarmingPotentialGWP    
              type: string    
            value:    
              description: Property. climateChangeGlobalWarmingPotentialGWP value    
              type: string    
          required:    
            - type    
            - value    
            - unitCode    
          type: object    
      description: This indicator measures the contribution of greenhouse gas emissions to global warming over a 100-year timeframe, expressed in kilograms of CO₂-equivalent. It accounts for all major greenhouse gases such as carbon dioxide (CO₂), methane (CH₄), and nitrous oxide (N₂O), each normalized to its global warming potential.    
      x-ngsi:    
        type: Property    
    climateChangeLandUseAndLULUCGWP:    
      anyOf:    
        - description: Property. climateChangeLandUseAndLULUCGWP value    
          type: string    
        - properties:    
            observedAt:    
              description: Property. Timestamp when the value was observed    
              format: date-time    
              type: string    
            type:    
              description: Property. NGSI-LD attribute type.    
              enum:    
                - Property    
              type: string    
            unitCode:    
              description: Property. Unit of measurement for climateChangeLandUseAndLULUCGWP    
              type: string    
            value:    
              description: Property. climateChangeLandUseAndLULUCGWP value    
              type: string    
          required:    
            - type    
            - value    
            - unitCode    
          type: object    
      description: Land use and land use change (LULUC) impacts on climate change refer to greenhouse gas emissions caused by deforestation, land conversion for agriculture, and other changes in land use. This indicator measures the potential warming effect of land use-related CO₂ emissions over 100 years.    
      x-ngsi:    
        type: Property    
    ecotoxicityFreshwaterComparativeToxicCTU:    
      anyOf:    
        - description: Property. ecotoxicityFreshwaterComparativeToxicCTU value    
          type: string    
        - properties:    
            observedAt:    
              description: Property. Timestamp when the value was observed    
              format: date-time    
              type: string    
            type:    
              description: Property. NGSI-LD attribute type.    
              enum:    
                - Property    
              type: string    
            unitCode:    
              description: Property. Unit of measurement for ecotoxicityFreshwaterComparativeToxicCTU    
              type: string    
            value:    
              description: Property. ecotoxicityFreshwaterComparativeToxicCTU value    
              type: string    
          required:    
            - type    
            - value    
            - unitCode    
          type: object    
      description: This indicator measures the potential harm of chemical substances released into freshwater ecosystems. It quantifies the toxicity of substances (e.g., heavy metals, pesticides) to aquatic organisms, expressed in Comparative Toxic Units for ecosystems (CTUe). It evaluates the impact on biodiversity and ecosystem health.    
      x-ngsi:    
        type: Property    
    ecotoxicityFreshwaterInorganicsCTUe:    
      anyOf:    
        - description: Property. ecotoxicityFreshwaterInorganicsCTUe value    
          type: string    
        - properties:    
            observedAt:    
              description: Property. Timestamp when the value was observed    
              format: date-time    
              type: string    
            type:    
              description: Property. NGSI-LD attribute type.    
              enum:    
                - Property    
              type: string    
            unitCode:    
              description: Property. Unit of measurement for ecotoxicityFreshwaterInorganicsCTUe    
              type: string    
            value:    
              description: Property. ecotoxicityFreshwaterInorganicsCTUe value    
              type: string    
          required:    
            - type    
            - value    
            - unitCode    
          type: object    
      description: This indicator focuses on the toxicity of inorganic chemical pollutants, such as heavy metals and minerals, in freshwater ecosystems. It assesses the potential for harm to aquatic life due to exposure to these inorganic substances, expressed in CTUe.    
      x-ngsi:    
        type: Property    
    ecotoxicityFreshwaterOrganicsCTUe:    
      anyOf:    
        - description: Property. ecotoxicityFreshwaterOrganicsCTUe value    
          type: string    
        - properties:    
            observedAt:    
              description: Property. Timestamp when the value was observed    
              format: date-time    
              type: string    
            type:    
              description: Property. NGSI-LD attribute type.    
              enum:    
                - Property    
              type: string    
            unitCode:    
              description: Property. Unit of measurement for ecotoxicityFreshwaterOrganicsCTUe    
              type: string    
            value:    
              description: Property. ecotoxicityFreshwaterOrganicsCTUe value    
              type: string    
          required:    
            - type    
            - value    
            - unitCode    
          type: object    
      description: This measures the toxicity of organic pollutants, including pesticides, herbicides, and other organic chemicals, in freshwater environments. These pollutants may disrupt aquatic ecosystems and harm species, with impacts measured in Comparative Toxic Units for ecosystems (CTUe).    
      x-ngsi:    
        type: Property    
    energyResourcesAbioticDepletionFossils:    
      anyOf:    
        - description: Property. energyResourcesAbioticDepletionFossils value    
          type: string    
        - properties:    
            observedAt:    
              description: Property. Timestamp when the value was observed    
              format: date-time    
              type: string    
            type:    
              description: Property. NGSI-LD attribute type.    
              enum:    
                - Property    
              type: string    
            unitCode:    
              description: Property. Unit of measurement for energyResourcesAbioticDepletionFossils    
              type: string    
            value:    
              description: Property. energyResourcesAbioticDepletionFossils value    
              type: string    
          required:    
            - type    
            - value    
            - unitCode    
          type: object    
      description: This indicator measures the depletion of non-renewable energy resources, primarily fossil fuels (oil, coal, natural gas). It reflects the consumption of these resources and the impact on their long-term availability, expressed in megajoules (MJ), focusing on energy content and environmental sustainability.    
      x-ngsi:    
        type: Property    
    eutrophicationFreshwaterNutrientsP:    
      anyOf:    
        - description: Property. eutrophicationFreshwaterNutrientsP value    
          type: string    
        - properties:    
            observedAt:    
              description: Property. Timestamp when the value was observed    
              format: date-time    
              type: string    
            type:    
              description: Property. NGSI-LD attribute type.    
              enum:    
                - Property    
              type: string    
            unitCode:    
              description: Property. Unit of measurement for eutrophicationFreshwaterNutrientsP    
              type: string    
            value:    
              description: Property. eutrophicationFreshwaterNutrientsP value    
              type: string    
          required:    
            - type    
            - value    
            - unitCode    
          type: object    
      description: Freshwater eutrophication occurs when excessive nutrients, especially phosphorus (P), enter water bodies, leading to algal blooms and oxygen depletion. This indicator measures the potential for nutrient pollution to cause eutrophication, expressed in kilograms of phosphorus equivalents (kg P-Eq).    
      x-ngsi:    
        type: Property    
    eutrophicationMarineNutrientsN:    
      anyOf:    
        - description: Property. eutrophicationMarineNutrientsN value    
          type: string    
        - properties:    
            observedAt:    
              description: Property. Timestamp when the value was observed    
              format: date-time    
              type: string    
            type:    
              description: Property. NGSI-LD attribute type.    
              enum:    
                - Property    
              type: string    
            unitCode:    
              description: Property. Unit of measurement for eutrophicationMarineNutrientsN    
              type: string    
            value:    
              description: Property. eutrophicationMarineNutrientsN value    
              type: string    
          required:    
            - type    
            - value    
            - unitCode    
          type: object    
      description: Marine eutrophication is caused by nitrogen (N) pollution, which can lead to harmful algal blooms in oceans and coastal waters. This indicator measures the impact of nitrogen runoff on marine ecosystems, expressed in kilograms of nitrogen equivalents (kg N-Eq).    
      x-ngsi:    
        type: Property    
    eutrophicationTerrestrialAccumExceedance:    
      anyOf:    
        - description: Property. eutrophicationTerrestrialAccumExceedance value    
          type: string    
        - properties:    
            observedAt:    
              description: Property. Timestamp when the value was observed    
              format: date-time    
              type: string    
            type:    
              description: Property. NGSI-LD attribute type.    
              enum:    
                - Property    
              type: string    
            unitCode:    
              description: Property. Unit of measurement for eutrophicationTerrestrialAccumExceedance    
              type: string    
            value:    
              description: Property. eutrophicationTerrestrialAccumExceedance value    
              type: string    
          required:    
            - type    
            - value    
            - unitCode    
          type: object    
      description: This measures the impact of nutrient pollution, particularly nitrogen, on terrestrial ecosystems. It assesses the potential for nutrient accumulation to exceed the natural capacity of the land, leading to changes in vegetation and soil degradation, expressed in mol N-Eq.    
      x-ngsi:    
        type: Property    
    humanToxicityCarcinogenicCTUh:    
      anyOf:    
        - description: Property. humanToxicityCarcinogenicCTUh value    
          type: string    
        - properties:    
            observedAt:    
              description: Property. Timestamp when the value was observed    
              format: date-time    
              type: string    
            type:    
              description: Property. NGSI-LD attribute type.    
              enum:    
                - Property    
              type: string    
            unitCode:    
              description: Property. Unit of measurement for humanToxicityCarcinogenicCTUh    
              type: string    
            value:    
              description: Property. humanToxicityCarcinogenicCTUh value    
              type: string    
          required:    
            - type    
            - value    
            - unitCode    
          type: object    
      description: This indicator assesses the potential impact of exposure to carcinogenic substances on human health. It is expressed in Comparative Toxic Units for humans (CTUh) and measures the risk of developing cancer from exposure to various chemicals, such as heavy metals, industrial solvents, and certain organic compounds.    
      x-ngsi:    
        type: Property    
    humanToxicityCarcinogenicInorganicsCTU:    
      anyOf:    
        - description: Property. humanToxicityCarcinogenicInorganicsCTU value    
          type: string    
        - properties:    
            observedAt:    
              description: Property. Timestamp when the value was observed    
              format: date-time    
              type: string    
            type:    
              description: Property. NGSI-LD attribute type.    
              enum:    
                - Property    
              type: string    
            unitCode:    
              description: Property. Unit of measurement for humanToxicityCarcinogenicInorganicsCTU    
              type: string    
            value:    
              description: Property. humanToxicityCarcinogenicInorganicsCTU value    
              type: string    
          required:    
            - type    
            - value    
            - unitCode    
          type: object    
      description: This focuses on the carcinogenic risks to humans from exposure to inorganic substances, such as arsenic, lead, and other heavy metals. It evaluates the potential harm in terms of cancer development, expressed in CTUh.    
      x-ngsi:    
        type: Property    
    humanToxicityCarcinogenicOrganicsCTU:    
      anyOf:    
        - description: Property. humanToxicityCarcinogenicOrganicsCTU value    
          type: string    
        - properties:    
            observedAt:    
              description: Property. Timestamp when the value was observed    
              format: date-time    
              type: string    
            type:    
              description: Property. NGSI-LD attribute type.    
              enum:    
                - Property    
              type: string    
            unitCode:    
              description: Property. Unit of measurement for humanToxicityCarcinogenicOrganicsCTU    
              type: string    
            value:    
              description: Property. humanToxicityCarcinogenicOrganicsCTU value    
              type: string    
          required:    
            - type    
            - value    
            - unitCode    
          type: object    
      description: This indicator assesses the carcinogenic potential of organic chemical substances, such as formaldehyde, benzene, and pesticides, on human health. It evaluates the risk of cancer associated with exposure to these compounds, expressed in CTUh.    
      x-ngsi:    
        type: Property    
    humanToxicityNonCarcinogenicCTUh:    
      anyOf:    
        - description: Property. humanToxicityNonCarcinogenicCTUh value    
          type: string    
        - properties:    
            observedAt:    
              description: Property. Timestamp when the value was observed    
              format: date-time    
              type: string    
            type:    
              description: Property. NGSI-LD attribute type.    
              enum:    
                - Property    
              type: string    
            unitCode:    
              description: Property. Unit of measurement for humanToxicityNonCarcinogenicCTUh    
              type: string    
            value:    
              description: Property. humanToxicityNonCarcinogenicCTUh value    
              type: string    
          required:    
            - type    
            - value    
            - unitCode    
          type: object    
      description: This indicator measures the potential risk to human health from non-carcinogenic substances. It assesses the likelihood of harm such as organ damage or neurological effects from exposure to chemicals, expressed in CTUh.    
      x-ngsi:    
        type: Property    
    humanToxicityNonCarcinogenicInorganicsCTU:    
      anyOf:    
        - description: Property. humanToxicityNonCarcinogenicInorganicsCTU value    
          type: string    
        - properties:    
            observedAt:    
              description: Property. Timestamp when the value was observed    
              format: date-time    
              type: string    
            type:    
              description: Property. NGSI-LD attribute type.    
              enum:    
                - Property    
              type: string    
            unitCode:    
              description: Property. Unit of measurement for humanToxicityNonCarcinogenicInorganicsCTU    
              type: string    
            value:    
              description: Property. humanToxicityNonCarcinogenicInorganicsCTU value    
              type: string    
          required:    
            - type    
            - value    
            - unitCode    
          type: object    
      description: This focuses on non-carcinogenic health risks from inorganic substances, including heavy metals like cadmium and lead. It evaluates the impact of these chemicals on human health, expressed in CTUh.    
      x-ngsi:    
        type: Property    
    humanToxicityNonCarcinogenicOrganicsCTU:    
      anyOf:    
        - description: Property. humanToxicityNonCarcinogenicOrganicsCTU value    
          type: string    
        - properties:    
            observedAt:    
              description: Property. Timestamp when the value was observed    
              format: date-time    
              type: string    
            type:    
              description: Property. NGSI-LD attribute type.    
              enum:    
                - Property    
              type: string    
            unitCode:    
              description: Property. Unit of measurement for humanToxicityNonCarcinogenicOrganicsCTU    
              type: string    
            value:    
              description: Property. humanToxicityNonCarcinogenicOrganicsCTU value    
              type: string    
          required:    
            - type    
            - value    
            - unitCode    
          type: object    
      description: This indicator assesses the non-carcinogenic health risks posed by organic substances, including solvents, pesticides, and other chemicals. It measures the potential for organ damage or other chronic effects, expressed in CTUh.    
      x-ngsi:    
        type: Property    
    id:    
      description: Unique identifier for the entity    
      type: string    
      x-ngsi:    
        type: Property    
    ionisingRadiationHumanHealthU235:    
      anyOf:    
        - description: Property. ionisingRadiationHumanHealthU235 value    
          type: string    
        - properties:    
            observedAt:    
              description: Property. Timestamp when the value was observed    
              format: date-time    
              type: string    
            type:    
              description: Property. NGSI-LD attribute type.    
              enum:    
                - Property    
              type: string    
            unitCode:    
              description: Property. Unit of measurement for ionisingRadiationHumanHealthU235    
              type: string    
            value:    
              description: Property. ionisingRadiationHumanHealthU235 value    
              type: string    
          required:    
            - type    
            - value    
            - unitCode    
          type: object    
      description: This measures the potential health impact of ionizing radiation exposure on humans. It is based on the efficiency of radiation exposure relative to uranium-235 (U235), expressed in kilobecquerels (kBq). This indicator focuses on risks such as radiation sickness or long-term health effects like cancer.    
      x-ngsi:    
        type: Property    
    landUseSoilQualityIndex:    
      anyOf:    
        - description: Property. landUseSoilQualityIndex value    
          type: string    
        - properties:    
            observedAt:    
              description: Property. Timestamp when the value was observed    
              format: date-time    
              type: string    
            type:    
              description: Property. NGSI-LD attribute type.    
              enum:    
                - Property    
              type: string    
            unitCode:    
              description: Property. Unit of measurement for landUseSoilQualityIndex    
              type: string    
            value:    
              description: Property. landUseSoilQualityIndex value    
              type: string    
          required:    
            - type    
            - value    
            - unitCode    
          type: object    
      description: This indicator evaluates the impact of land use on soil quality, taking into account factors such as organic carbon content, nutrient availability, and erosion potential. It provides a measure of how land use practices affect soil health and sustainability.    
      x-ngsi:    
        type: Property    
    materialResourcesAbioticDepletionElements:    
      anyOf:    
        - description: Property. materialResourcesAbioticDepletionElements value    
          type: string    
        - properties:    
            observedAt:    
              description: Property. Timestamp when the value was observed    
              format: date-time    
              type: string    
            type:    
              description: Property. NGSI-LD attribute type.    
              enum:    
                - Property    
              type: string    
            unitCode:    
              description: Property. Unit of measurement for materialResourcesAbioticDepletionElements    
              type: string    
            value:    
              description: Property. materialResourcesAbioticDepletionElements value    
              type: string    
          required:    
            - type    
            - value    
            - unitCode    
          type: object    
      description: This indicator measures the depletion of non-renewable material resources, particularly metals and minerals (e.g., copper, zinc, antimony). It reflects the long-term availability of these elements and the environmental impact of their extraction, expressed in kilograms of antimony equivalents (kg Sb-Eq).    
      x-ngsi:    
        type: Property    
    ozoneDepletionPotentialODP:    
      anyOf:    
        - description: Property. ozoneDepletionPotentialODP value    
          type: string    
        - properties:    
            observedAt:    
              description: Property. Timestamp when the value was observed    
              format: date-time    
              type: string    
            type:    
              description: Property. NGSI-LD attribute type.    
              enum:    
                - Property    
              type: string    
            unitCode:    
              description: Property. Unit of measurement for ozoneDepletionPotentialODP    
              type: string    
            value:    
              description: Property. ozoneDepletionPotentialODP value    
              type: string    
          required:    
            - type    
            - value    
            - unitCode    
          type: object    
      description: This indicator measures the potential for chemical substances to deplete the stratospheric ozone layer. It is expressed in kilograms of CFC-11 equivalents (kg CFC-11-Eq), focusing on substances like chlorofluorocarbons (CFCs) that contribute to ozone layer depletion.    
      x-ngsi:    
        type: Property    
    particulateMatterFormationHealth:    
      anyOf:    
        - description: Property. particulateMatterFormationHealth value    
          type: string    
        - properties:    
            observedAt:    
              description: Property. Timestamp when the value was observed    
              format: date-time    
              type: string    
            type:    
              description: Property. NGSI-LD attribute type.    
              enum:    
                - Property    
              type: string    
            unitCode:    
              description: Property. Unit of measurement for particulateMatterFormationHealth    
              type: string    
            value:    
              description: Property. particulateMatterFormationHealth value    
              type: string    
          required:    
            - type    
            - value    
            - unitCode    
          type: object    
      description: This indicator assesses the impact of particulate matter (PM) emissions on human health. Particulates such as PM10 and PM2.5 can penetrate the respiratory system, causing conditions like asthma, bronchitis, and cardiovascular diseases. This is expressed in disease incidence cases.    
      x-ngsi:    
        type: Property    
    photochemicalOxidantFormationHealth:    
      anyOf:    
        - description: Property. photochemicalOxidantFormationHealth value    
          type: string    
        - properties:    
            observedAt:    
              description: Property. Timestamp when the value was observed    
              format: date-time    
              type: string    
            type:    
              description: Property. NGSI-LD attribute type.    
              enum:    
                - Property    
              type: string    
            unitCode:    
              description: Property. Unit of measurement for photochemicalOxidantFormationHealth    
              type: string    
            value:    
              description: Property. photochemicalOxidantFormationHealth value    
              type: string    
          required:    
            - type    
            - value    
            - unitCode    
          type: object    
      description: This measures the impact of emissions of volatile organic compounds (VOCs) and nitrogen oxides (NOx) that lead to the formation of ground-level ozone (smog), which affects human respiratory health. It is expressed in kilograms of NMVOC equivalents (kg NMVOC-Eq).    
      x-ngsi:    
        type: Property    
    type:    
      description: NGSI Entity type. Type of message published    
      enum:    
        - environmental_footprint_indicator    
      type: string    
      x-ngsi:    
        type: Property    
    waterUseUserDeprivationPotential:    
      anyOf:    
        - description: Property. waterUseUserDeprivationPotential value    
          type: string    
        - properties:    
            observedAt:    
              description: Property. Timestamp when the value was observed    
              format: date-time    
              type: string    
            type:    
              description: Property. NGSI-LD attribute type.    
              enum:    
                - Property    
              type: string    
            unitCode:    
              description: Property. Unit of measurement for waterUseUserDeprivationPotential    
              type: string    
            value:    
              description: Property. waterUseUserDeprivationPotential value    
              type: string    
          required:    
            - type    
            - value    
            - unitCode    
          type: object    
      description: This indicator evaluates the potential for water consumption to lead to human water deprivation, considering local water scarcity and water use efficiency. It is expressed in cubic meters of world equivalents deprived (m³ world Eq. deprived).    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
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
  x-license-url: https://github.com/smart-data-models/circuloos_data_model/blob/master/environmental_footprint_indicator/LICENSE.md    
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
#### environmental_footprint_indicator NGSI-LD key-values Example    
Here is an example of a environmental_footprint_indicator in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:efi:entity-001",  
  "type": "environmental_footprint_indicator",  
  "acidificationAccumulatedExceedanceAE": "345.67",  
  "climateChangeGlobalWarmingPotentialGWP": "1234.56",  
  "climateChangeBiogenicGWP100": "98.76",  
  "climateChangeFossilGWP100": "567.89",  
  "climateChangeLandUseAndLULUCGWP": "432.1",  
  "ecotoxicityFreshwaterComparativeToxicCTU": "876.54",  
  "ecotoxicityFreshwaterInorganicsCTUe": "543.21",  
  "ecotoxicityFreshwaterOrganicsCTUe": "321.09",  
  "energyResourcesAbioticDepletionFossils": "987.65",  
  "eutrophicationFreshwaterNutrientsP": "0.987",  
  "eutrophicationMarineNutrientsN": "0.123",  
  "eutrophicationTerrestrialAccumExceedance": "765.43",  
  "humanToxicityCarcinogenicCTUh": "56.78",  
  "humanToxicityCarcinogenicInorganicsCTU": "12.34",  
  "humanToxicityCarcinogenicOrganicsCTU": "34.56",  
  "humanToxicityNonCarcinogenicCTUh": "78.90",  
  "humanToxicityNonCarcinogenicInorganicsCTU": "65.43",  
  "humanToxicityNonCarcinogenicOrganicsCTU": "90.12",  
  "ionisingRadiationHumanHealthU235": "76.54",  
  "landUseSoilQualityIndex": "5.43",  
  "materialResourcesAbioticDepletionElements": "543.21",  
  "ozoneDepletionPotentialODP": "0.0123",  
  "particulateMatterFormationHealth": "432.10",  
  "photochemicalOxidantFormationHealth": "321.98",  
  "waterUseUserDeprivationPotential": "543.12",  
  "@context": [  
    "https://raw.githubusercontent.com/european-dynamics-rnd/CIRCULOOS_Data_model/main/utils/circuloos_data_platform.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context-v1.8.jsonld"  
  ]  
}  
```  
</details>  
#### environmental_footprint_indicator NGSI-LD normalized Example    
Here is an example of a environmental_footprint_indicator in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:efi:entity-001",  
  "type": "environmental_footprint_indicator",  
  "acidificationAccumulatedExceedanceAE": {  
    "type": "Property",  
    "value": "345.67",  
    "unitCode": "XMHQ",  
    "observedAt": "2024-09-25T10:20:30Z"  
  },  
  "climateChangeGlobalWarmingPotentialGWP": {  
    "type": "Property",  
    "value": "1234.56",  
    "unitCode": "XCO2",  
    "observedAt": "2024-09-25T12:34:56Z"  
  },  
  "climateChangeBiogenicGWP100": {  
    "type": "Property",  
    "value": "98.76",  
    "unitCode": "XCO2",  
    "observedAt": "2024-09-24T15:45:00Z"  
  },  
  "climateChangeFossilGWP100": {  
    "type": "Property",  
    "value": "567.89",  
    "unitCode": "XCO2",  
    "observedAt": "2024-09-23T10:45:00Z"  
  },  
  "climateChangeLandUseAndLULUCGWP": {  
    "type": "Property",  
    "value": "432.1",  
    "unitCode": "XCO2",  
    "observedAt": "2024-09-22T11:30:00Z"  
  },  
  "ecotoxicityFreshwaterComparativeToxicCTU": {  
    "type": "Property",  
    "value": "876.54",  
    "unitCode": "CTUe",  
    "observedAt": "2024-09-22T08:15:00Z"  
  },  
  "ecotoxicityFreshwaterInorganicsCTUe": {  
    "type": "Property",  
    "value": "543.21",  
    "unitCode": "CTUe",  
    "observedAt": "2024-09-21T09:30:00Z"  
  },  
  "ecotoxicityFreshwaterOrganicsCTUe": {  
    "type": "Property",  
    "value": "321.09",  
    "unitCode": "CTUe",  
    "observedAt": "2024-09-20T12:00:00Z"  
  },  
  "energyResourcesAbioticDepletionFossils": {  
    "type": "Property",  
    "value": "987.65",  
    "unitCode": "MJ",  
    "observedAt": "2024-09-19T14:30:00Z"  
  },  
  "eutrophicationFreshwaterNutrientsP": {  
    "type": "Property",  
    "value": "0.987",  
    "unitCode": "kg P-Eq",  
    "observedAt": "2024-09-18T16:30:00Z"  
  },  
  "eutrophicationMarineNutrientsN": {  
    "type": "Property",  
    "value": "0.123",  
    "unitCode": "kg N-Eq",  
    "observedAt": "2024-09-17T08:30:00Z"  
  },  
  "eutrophicationTerrestrialAccumExceedance": {  
    "type": "Property",  
    "value": "765.43",  
    "unitCode": "mol N-Eq",  
    "observedAt": "2024-09-16T10:30:00Z"  
  },  
  "humanToxicityCarcinogenicCTUh": {  
    "type": "Property",  
    "value": "56.78",  
    "unitCode": "CTUh",  
    "observedAt": "2024-09-15T14:45:00Z"  
  },  
  "humanToxicityCarcinogenicInorganicsCTU": {  
    "type": "Property",  
    "value": "12.34",  
    "unitCode": "CTUh",  
    "observedAt": "2024-09-14T16:15:00Z"  
  },  
  "humanToxicityCarcinogenicOrganicsCTU": {  
    "type": "Property",  
    "value": "34.56",  
    "unitCode": "CTUh",  
    "observedAt": "2024-09-13T18:30:00Z"  
  },  
  "humanToxicityNonCarcinogenicCTUh": {  
    "type": "Property",  
    "value": "78.90",  
    "unitCode": "CTUh",  
    "observedAt": "2024-09-12T08:15:00Z"  
  },  
  "humanToxicityNonCarcinogenicInorganicsCTU": {  
    "type": "Property",  
    "value": "65.43",  
    "unitCode": "CTUh",  
    "observedAt": "2024-09-11T12:45:00Z"  
  },  
  "humanToxicityNonCarcinogenicOrganicsCTU": {  
    "type": "Property",  
    "value": "90.12",  
    "unitCode": "CTUh",  
    "observedAt": "2024-09-10T10:45:00Z"  
  },  
  "ionisingRadiationHumanHealthU235": {  
    "type": "Property",  
    "value": "76.54",  
    "unitCode": "BQU",  
    "observedAt": "2024-09-09T09:15:00Z"  
  },  
  "landUseSoilQualityIndex": {  
    "type": "Property",  
    "value": "5.43",  
    "unitCode": "M2AQ",  
    "observedAt": "2024-09-08T07:45:00Z"  
  },  
  "materialResourcesAbioticDepletionElements": {  
    "type": "Property",  
    "value": "543.21",  
    "unitCode": "kg Sb-Eq",  
    "observedAt": "2024-09-07T16:00:00Z"  
  },  
  "ozoneDepletionPotentialODP": {  
    "type": "Property",  
    "value": "0.0123",  
    "unitCode": "kg CFC-11-Eq",  
    "observedAt": "2024-09-06T14:30:00Z"  
  },  
  "particulateMatterFormationHealth": {  
    "type": "Property",  
    "value": "432.10",  
    "unitCode": "kg PM10-Eq",  
    "observedAt": "2024-09-05T13:30:00Z"  
  },  
  "photochemicalOxidantFormationHealth": {  
    "type": "Property",  
    "value": "321.98",  
    "unitCode": "kg NMVOC-Eq",  
    "observedAt": "2024-09-04T15:15:00Z"  
  },  
  "waterUseUserDeprivationPotential": {  
    "type": "Property",  
    "value": "543.12",  
    "unitCode": "m3 H2O-Eq",  
    "observedAt": "2024-09-03T18:00:00Z"  
  },  
  "@context": [  
    "https://raw.githubusercontent.com/european-dynamics-rnd/CIRCULOOS_Data_model/main/utils/circuloos_data_platform.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context-v1.8.jsonld"  
  ]  
}  
```  
</details><!-- /80-Examples -->  
