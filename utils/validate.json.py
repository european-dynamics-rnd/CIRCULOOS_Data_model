from jsonschema import validate

validate(instance={
  "id": "urn:ngsi-ld:efi:entity-001",
  "type": "environmental_footprint_indicator",
  "acidificationAccumulatedExceedanceAE": {
    "value": "345.67",
    "unitCode": "XMHQ",
    "observedAt": "2024-09-25T10:20:30Z"
  },
  "climateChangeGlobalWarmingPotentialGWP": {
    "value": "1234.56",
    "unitCode": "XCO2",
    "observedAt": "2024-09-25T12:34:56Z"
  },
  "climateChangeBiogenicGWP100": {
    "value": "98.76",
    "unitCode": "XCO2",
    "observedAt": "2024-09-24T15:45:00Z"
  },
  "climateChangeFossilGWP100": {
    "value": "567.89",
    "unitCode": "XCO2",
    "observedAt": "2024-09-23T10:45:00Z"
  },
  "climateChangeLandUseAndLULUCGWP": {
    "value": "432.1",
    "unitCode": "XCO2",
    "observedAt": "2024-09-22T11:30:00Z"
  },
  "ecotoxicityFreshwaterComparativeToxicCTU": {
    "value": "876.54",
    "unitCode": "CTUe",
    "observedAt": "2024-09-22T08:15:00Z"
  },
  "ecotoxicityFreshwaterInorganicsCTUe": {
    "value": "543.21",
    "unitCode": "CTUe",
    "observedAt": "2024-09-21T09:30:00Z"
  },
  "ecotoxicityFreshwaterOrganicsCTUe": {
    "value": "321.09",
    "unitCode": "CTUe",
    "observedAt": "2024-09-20T12:00:00Z"
  },
  "energyResourcesAbioticDepletionFossils": {
    "value": "987.65",
    "unitCode": "MJ",
    "observedAt": "2024-09-19T14:30:00Z"
  },
  "eutrophicationFreshwaterNutrientsP": {
    "value": "0.987",
    "unitCode": "kg P-Eq",
    "observedAt": "2024-09-18T16:30:00Z"
  },
  "eutrophicationMarineNutrientsN": {
    "value": "0.123",
    "unitCode": "kg N-Eq",
    "observedAt": "2024-09-17T08:30:00Z"
  },
  "eutrophicationTerrestrialAccumExceedance": {
    "value": "765.43",
    "unitCode": "mol N-Eq",
    "observedAt": "2024-09-16T10:30:00Z"
  },
  "humanToxicityCarcinogenicCTUh": {
    "value": "56.78",
    "unitCode": "CTUh",
    "observedAt": "2024-09-15T14:45:00Z"
  },
  "humanToxicityCarcinogenicInorganicsCTU": {
    "value": "12.34",
    "unitCode": "CTUh",
    "observedAt": "2024-09-14T16:15:00Z"
  },
  "humanToxicityCarcinogenicOrganicsCTU": {
    "value": "34.56",
    "unitCode": "CTUh",
    "observedAt": "2024-09-13T18:30:00Z"
  },
  "humanToxicityNonCarcinogenicCTUh": {
    "value": "78.90",
    "unitCode": "CTUh",
    "observedAt": "2024-09-12T08:15:00Z"
  },
  "humanToxicityNonCarcinogenicInorganicsCTU": {
    "value": "65.43",
    "unitCode": "CTUh",
    "observedAt": "2024-09-11T12:45:00Z"
  },
  "humanToxicityNonCarcinogenicOrganicsCTU": {
    "value": "90.12",
    "unitCode": "CTUh",
    "observedAt": "2024-09-10T10:45:00Z"
  },
  "ionisingRadiationHumanHealthU235": {
    "value": "76.54",
    "unitCode": "BQU",
    "observedAt": "2024-09-09T09:15:00Z"
  },
  "landUseSoilQualityIndex": {
    "value": "5.43",
    "unitCode": "M2AQ",
    "observedAt": "2024-09-08T07:45:00Z"
  },
  "materialResourcesAbioticDepletionElements": {
    "value": "543.21",
    "unitCode": "kg Sb-Eq",
    "observedAt": "2024-09-07T16:00:00Z"
  },
  "ozoneDepletionPotentialODP": {
    "value": "0.0123",
    "unitCode": "kg CFC-11-Eq",
    "observedAt": "2024-09-06T14:30:00Z"
  },
  "particulateMatterFormationHealth": {
    "value": "432.10",
    "unitCode": "kg PM10-Eq",
    "observedAt": "2024-09-05T13:30:00Z"
  },
  "photochemicalOxidantFormationHealth": {
    "value": "321.98",
    "unitCode": "kg NMVOC-Eq",
    "observedAt": "2024-09-04T15:15:00Z"
  },
  "waterUseUserDeprivationPotential": {
    "value": "543.12",
    "unitCode": "m3 H2O-Eq",
    "observedAt": "2024-09-03T18:00:00Z"
  },
     "@context": [
        "https://TOBELater/context.jsonld"
    ]
}
, schema={
  "$schema": "http://json-schema.org/schema#",
  "modelTags": "Environmental indicators",
  "$id": "https://raw.githubusercontent.com/TO_ADD_LATER/schema.json",
  "$schemaVersion": "0.1.0",
  "title": "Data model for environmental indicators produced by GRETA",
  "description": "Represents the environmental indicators calculated by GRETA using Environmental Footprint 3.1 methodology",
  "type": "object",
  "properties": {
    "id": {
      "type": "string",
      "description": "Unique identifier for the entity"
    },
    "type": {
      "type": "string",
      "enum": [
        "environmental_footprint_indicator"
      ],
      "description": "Type of message published"
    },
    "acidificationAccumulatedExceedanceAE": {
      "type": "object",
      "properties": {
        "value": {
          "type": "string",
          "description": "acidificationAccumulatedExceedanceAE value"
        },
        "unitCode": {
          "type": "string",
          "description": "Unit of measurement for acidificationAccumulatedExceedanceAE"
        },
        "observedAt": {
          "type": "string",
          "format": "date-time",
          "description": "Timestamp when the value was observed"
        }
      },
      "description": "Acidification refers to the process where emissions of sulfur dioxide (SO\u2082), nitrogen oxides (NO\u2093), and ammonia (NH\u2083) lead to the formation of acidic compounds in the atmosphere, which then deposit in soils and water bodies, reducing pH levels. This indicator measures the potential impact of these emissions on ecosystems, using an accumulated exceedance approach to assess how much ecosystems can tolerate before damage occurs.",
      "required": [
        "value",
        "unitCode"
      ]
    },
    "climateChangeGlobalWarmingPotentialGWP": {
      "type": "object",
      "properties": {
        "value": {
          "type": "string",
          "description": "climateChangeGlobalWarmingPotentialGWP value"
        },
        "unitCode": {
          "type": "string",
          "description": "Unit of measurement for climateChangeGlobalWarmingPotentialGWP"
        },
        "observedAt": {
          "type": "string",
          "format": "date-time",
          "description": "Timestamp when the value was observed"
        }
      },
      "description": "This indicator measures the contribution of greenhouse gas emissions to global warming over a 100-year timeframe, expressed in kilograms of CO\u2082-equivalent. It accounts for all major greenhouse gases such as carbon dioxide (CO\u2082), methane (CH\u2084), and nitrous oxide (N\u2082O), each normalized to its global warming potential.",
      "required": [
        "value",
        "unitCode"
      ]
    },
    "climateChangeBiogenicGWP100": {
      "type": "object",
      "properties": {
        "value": {
          "type": "string",
          "description": "climateChangeBiogenicGWP100 value"
        },
        "unitCode": {
          "type": "string",
          "description": "Unit of measurement for climateChangeBiogenicGWP100"
        },
        "observedAt": {
          "type": "string",
          "format": "date-time",
          "description": "Timestamp when the value was observed"
        }
      },
      "description": "This measures the global warming potential of biogenic (plant-derived) carbon emissions over a 100-year period, which includes CO\u2082 released from the combustion or decomposition of biomass. Biogenic emissions are distinguished from fossil emissions, with a focus on the carbon cycle of living organisms.",
      "required": [
        "value",
        "unitCode"
      ]
    },
    "climateChangeFossilGWP100": {
      "type": "object",
      "properties": {
        "value": {
          "type": "string",
          "description": "climateChangeFossilGWP100 value"
        },
        "unitCode": {
          "type": "string",
          "description": "Unit of measurement for climateChangeFossilGWP100"
        },
        "observedAt": {
          "type": "string",
          "format": "date-time",
          "description": "Timestamp when the value was observed"
        }
      },
      "description": "This indicator measures the global warming potential from fossil fuel-derived emissions, such as CO\u2082 from coal, oil, and natural gas combustion. It captures the long-term impact of these emissions on climate change, expressed in kilograms of CO\u2082-equivalents over a 100-year period.",
      "required": [
        "value",
        "unitCode"
      ]
    },
    "climateChangeLandUseAndLULUCGWP": {
      "type": "object",
      "properties": {
        "value": {
          "type": "string",
          "description": "climateChangeLandUseAndLULUCGWP value"
        },
        "unitCode": {
          "type": "string",
          "description": "Unit of measurement for climateChangeLandUseAndLULUCGWP"
        },
        "observedAt": {
          "type": "string",
          "format": "date-time",
          "description": "Timestamp when the value was observed"
        }
      },
      "description": "Land use and land use change (LULUC) impacts on climate change refer to greenhouse gas emissions caused by deforestation, land conversion for agriculture, and other changes in land use. This indicator measures the potential warming effect of land use-related CO\u2082 emissions over 100 years.",
      "required": [
        "value",
        "unitCode"
      ]
    },
    "ecotoxicityFreshwaterComparativeToxicCTU": {
      "type": "object",
      "properties": {
        "value": {
          "type": "string",
          "description": "ecotoxicityFreshwaterComparativeToxicCTU value"
        },
        "unitCode": {
          "type": "string",
          "description": "Unit of measurement for ecotoxicityFreshwaterComparativeToxicCTU"
        },
        "observedAt": {
          "type": "string",
          "format": "date-time",
          "description": "Timestamp when the value was observed"
        }
      },
      "description": "This indicator measures the potential harm of chemical substances released into freshwater ecosystems. It quantifies the toxicity of substances (e.g., heavy metals, pesticides) to aquatic organisms, expressed in Comparative Toxic Units for ecosystems (CTUe). It evaluates the impact on biodiversity and ecosystem health.",
      "required": [
        "value",
        "unitCode"
      ]
    },
    "ecotoxicityFreshwaterInorganicsCTUe": {
      "type": "object",
      "properties": {
        "value": {
          "type": "string",
          "description": "ecotoxicityFreshwaterInorganicsCTUe value"
        },
        "unitCode": {
          "type": "string",
          "description": "Unit of measurement for ecotoxicityFreshwaterInorganicsCTUe"
        },
        "observedAt": {
          "type": "string",
          "format": "date-time",
          "description": "Timestamp when the value was observed"
        }
      },
      "description": "This indicator focuses on the toxicity of inorganic chemical pollutants, such as heavy metals and minerals, in freshwater ecosystems. It assesses the potential for harm to aquatic life due to exposure to these inorganic substances, expressed in CTUe.",
      "required": [
        "value",
        "unitCode"
      ]
    },
    "ecotoxicityFreshwaterOrganicsCTUe": {
      "type": "object",
      "properties": {
        "value": {
          "type": "string",
          "description": "ecotoxicityFreshwaterOrganicsCTUe value"
        },
        "unitCode": {
          "type": "string",
          "description": "Unit of measurement for ecotoxicityFreshwaterOrganicsCTUe"
        },
        "observedAt": {
          "type": "string",
          "format": "date-time",
          "description": "Timestamp when the value was observed"
        }
      },
      "description": "This measures the toxicity of organic pollutants, including pesticides, herbicides, and other organic chemicals, in freshwater environments. These pollutants may disrupt aquatic ecosystems and harm species, with impacts measured in Comparative Toxic Units for ecosystems (CTUe).",
      "required": [
        "value",
        "unitCode"
      ]
    },
    "energyResourcesAbioticDepletionFossils": {
      "type": "object",
      "properties": {
        "value": {
          "type": "string",
          "description": "energyResourcesAbioticDepletionFossils value"
        },
        "unitCode": {
          "type": "string",
          "description": "Unit of measurement for energyResourcesAbioticDepletionFossils"
        },
        "observedAt": {
          "type": "string",
          "format": "date-time",
          "description": "Timestamp when the value was observed"
        }
      },
      "description": "This indicator measures the depletion of non-renewable energy resources, primarily fossil fuels (oil, coal, natural gas). It reflects the consumption of these resources and the impact on their long-term availability, expressed in megajoules (MJ), focusing on energy content and environmental sustainability.",
      "required": [
        "value",
        "unitCode"
      ]
    },
    "eutrophicationFreshwaterNutrientsP": {
      "type": "object",
      "properties": {
        "value": {
          "type": "string",
          "description": "eutrophicationFreshwaterNutrientsP value"
        },
        "unitCode": {
          "type": "string",
          "description": "Unit of measurement for eutrophicationFreshwaterNutrientsP"
        },
        "observedAt": {
          "type": "string",
          "format": "date-time",
          "description": "Timestamp when the value was observed"
        }
      },
      "description": "Freshwater eutrophication occurs when excessive nutrients, especially phosphorus (P), enter water bodies, leading to algal blooms and oxygen depletion. This indicator measures the potential for nutrient pollution to cause eutrophication, expressed in kilograms of phosphorus equivalents (kg P-Eq).",
      "required": [
        "value",
        "unitCode"
      ]
    },
    "eutrophicationMarineNutrientsN": {
      "type": "object",
      "properties": {
        "value": {
          "type": "string",
          "description": "eutrophicationMarineNutrientsN value"
        },
        "unitCode": {
          "type": "string",
          "description": "Unit of measurement for eutrophicationMarineNutrientsN"
        },
        "observedAt": {
          "type": "string",
          "format": "date-time",
          "description": "Timestamp when the value was observed"
        }
      },
      "description": "Marine eutrophication is caused by nitrogen (N) pollution, which can lead to harmful algal blooms in oceans and coastal waters. This indicator measures the impact of nitrogen runoff on marine ecosystems, expressed in kilograms of nitrogen equivalents (kg N-Eq).",
      "required": [
        "value",
        "unitCode"
      ]
    },
    "eutrophicationTerrestrialAccumExceedance": {
      "type": "object",
      "properties": {
        "value": {
          "type": "string",
          "description": "eutrophicationTerrestrialAccumExceedance value"
        },
        "unitCode": {
          "type": "string",
          "description": "Unit of measurement for eutrophicationTerrestrialAccumExceedance"
        },
        "observedAt": {
          "type": "string",
          "format": "date-time",
          "description": "Timestamp when the value was observed"
        }
      },
      "description": "This measures the impact of nutrient pollution, particularly nitrogen, on terrestrial ecosystems. It assesses the potential for nutrient accumulation to exceed the natural capacity of the land, leading to changes in vegetation and soil degradation, expressed in mol N-Eq.",
      "required": [
        "value",
        "unitCode"
      ]
    },
    "humanToxicityCarcinogenicCTUh": {
      "type": "object",
      "properties": {
        "value": {
          "type": "string",
          "description": "humanToxicityCarcinogenicCTUh value"
        },
        "unitCode": {
          "type": "string",
          "description": "Unit of measurement for humanToxicityCarcinogenicCTUh"
        },
        "observedAt": {
          "type": "string",
          "format": "date-time",
          "description": "Timestamp when the value was observed"
        }
      },
      "description": "This indicator assesses the potential impact of exposure to carcinogenic substances on human health. It is expressed in Comparative Toxic Units for humans (CTUh) and measures the risk of developing cancer from exposure to various chemicals, such as heavy metals, industrial solvents, and certain organic compounds.",
      "required": [
        "value",
        "unitCode"
      ]
    },
    "humanToxicityCarcinogenicInorganicsCTU": {
      "type": "object",
      "properties": {
        "value": {
          "type": "string",
          "description": "humanToxicityCarcinogenicInorganicsCTU value"
        },
        "unitCode": {
          "type": "string",
          "description": "Unit of measurement for humanToxicityCarcinogenicInorganicsCTU"
        },
        "observedAt": {
          "type": "string",
          "format": "date-time",
          "description": "Timestamp when the value was observed"
        }
      },
      "description": "This focuses on the carcinogenic risks to humans from exposure to inorganic substances, such as arsenic, lead, and other heavy metals. It evaluates the potential harm in terms of cancer development, expressed in CTUh.",
      "required": [
        "value",
        "unitCode"
      ]
    },
    "humanToxicityCarcinogenicOrganicsCTU": {
      "type": "object",
      "properties": {
        "value": {
          "type": "string",
          "description": "humanToxicityCarcinogenicOrganicsCTU value"
        },
        "unitCode": {
          "type": "string",
          "description": "Unit of measurement for humanToxicityCarcinogenicOrganicsCTU"
        },
        "observedAt": {
          "type": "string",
          "format": "date-time",
          "description": "Timestamp when the value was observed"
        }
      },
      "description": "This indicator assesses the carcinogenic potential of organic chemical substances, such as formaldehyde, benzene, and pesticides, on human health. It evaluates the risk of cancer associated with exposure to these compounds, expressed in CTUh.",
      "required": [
        "value",
        "unitCode"
      ]
    },
    "humanToxicityNonCarcinogenicCTUh": {
      "type": "object",
      "properties": {
        "value": {
          "type": "string",
          "description": "humanToxicityNonCarcinogenicCTUh value"
        },
        "unitCode": {
          "type": "string",
          "description": "Unit of measurement for humanToxicityNonCarcinogenicCTUh"
        },
        "observedAt": {
          "type": "string",
          "format": "date-time",
          "description": "Timestamp when the value was observed"
        }
      },
      "description": "This indicator measures the potential risk to human health from non-carcinogenic substances. It assesses the likelihood of harm such as organ damage or neurological effects from exposure to chemicals, expressed in CTUh.",
      "required": [
        "value",
        "unitCode"
      ]
    },
    "humanToxicityNonCarcinogenicInorganicsCTU": {
      "type": "object",
      "properties": {
        "value": {
          "type": "string",
          "description": "humanToxicityNonCarcinogenicInorganicsCTU value"
        },
        "unitCode": {
          "type": "string",
          "description": "Unit of measurement for humanToxicityNonCarcinogenicInorganicsCTU"
        },
        "observedAt": {
          "type": "string",
          "format": "date-time",
          "description": "Timestamp when the value was observed"
        }
      },
      "description": "This focuses on non-carcinogenic health risks from inorganic substances, including heavy metals like cadmium and lead. It evaluates the impact of these chemicals on human health, expressed in CTUh.",
      "required": [
        "value",
        "unitCode"
      ]
    },
    "humanToxicityNonCarcinogenicOrganicsCTU": {
      "type": "object",
      "properties": {
        "value": {
          "type": "string",
          "description": "humanToxicityNonCarcinogenicOrganicsCTU value"
        },
        "unitCode": {
          "type": "string",
          "description": "Unit of measurement for humanToxicityNonCarcinogenicOrganicsCTU"
        },
        "observedAt": {
          "type": "string",
          "format": "date-time",
          "description": "Timestamp when the value was observed"
        }
      },
      "description": "This indicator assesses the non-carcinogenic health risks posed by organic substances, including solvents, pesticides, and other chemicals. It measures the potential for organ damage or other chronic effects, expressed in CTUh.",
      "required": [
        "value",
        "unitCode"
      ]
    },
    "ionisingRadiationHumanHealthU235": {
      "type": "object",
      "properties": {
        "value": {
          "type": "string",
          "description": "ionisingRadiationHumanHealthU235 value"
        },
        "unitCode": {
          "type": "string",
          "description": "Unit of measurement for ionisingRadiationHumanHealthU235"
        },
        "observedAt": {
          "type": "string",
          "format": "date-time",
          "description": "Timestamp when the value was observed"
        }
      },
      "description": "This measures the potential health impact of ionizing radiation exposure on humans. It is based on the efficiency of radiation exposure relative to uranium-235 (U235), expressed in kilobecquerels (kBq). This indicator focuses on risks such as radiation sickness or long-term health effects like cancer.",
      "required": [
        "value",
        "unitCode"
      ]
    },
    "landUseSoilQualityIndex": {
      "type": "object",
      "properties": {
        "value": {
          "type": "string",
          "description": "landUseSoilQualityIndex value"
        },
        "unitCode": {
          "type": "string",
          "description": "Unit of measurement for landUseSoilQualityIndex"
        },
        "observedAt": {
          "type": "string",
          "format": "date-time",
          "description": "Timestamp when the value was observed"
        }
      },
      "description": "This indicator evaluates the impact of land use on soil quality, taking into account factors such as organic carbon content, nutrient availability, and erosion potential. It provides a measure of how land use practices affect soil health and sustainability.",
      "required": [
        "value",
        "unitCode"
      ]
    },
    "materialResourcesAbioticDepletionElements": {
      "type": "object",
      "properties": {
        "value": {
          "type": "string",
          "description": "materialResourcesAbioticDepletionElements value"
        },
        "unitCode": {
          "type": "string",
          "description": "Unit of measurement for materialResourcesAbioticDepletionElements"
        },
        "observedAt": {
          "type": "string",
          "format": "date-time",
          "description": "Timestamp when the value was observed"
        }
      },
      "description": "This indicator measures the depletion of non-renewable material resources, particularly metals and minerals (e.g., copper, zinc, antimony). It reflects the long-term availability of these elements and the environmental impact of their extraction, expressed in kilograms of antimony equivalents (kg Sb-Eq).",
      "required": [
        "value",
        "unitCode"
      ]
    },
    "ozoneDepletionPotentialODP": {
      "type": "object",
      "properties": {
        "value": {
          "type": "string",
          "description": "ozoneDepletionPotentialODP value"
        },
        "unitCode": {
          "type": "string",
          "description": "Unit of measurement for ozoneDepletionPotentialODP"
        },
        "observedAt": {
          "type": "string",
          "format": "date-time",
          "description": "Timestamp when the value was observed"
        }
      },
      "description": "This indicator measures the potential for chemical substances to deplete the stratospheric ozone layer. It is expressed in kilograms of CFC-11 equivalents (kg CFC-11-Eq), focusing on substances like chlorofluorocarbons (CFCs) that contribute to ozone layer depletion.",
      "required": [
        "value",
        "unitCode"
      ]
    },
    "particulateMatterFormationHealth": {
      "type": "object",
      "properties": {
        "value": {
          "type": "string",
          "description": "particulateMatterFormationHealth value"
        },
        "unitCode": {
          "type": "string",
          "description": "Unit of measurement for particulateMatterFormationHealth"
        },
        "observedAt": {
          "type": "string",
          "format": "date-time",
          "description": "Timestamp when the value was observed"
        }
      },
      "description": "This indicator assesses the impact of particulate matter (PM) emissions on human health. Particulates such as PM10 and PM2.5 can penetrate the respiratory system, causing conditions like asthma, bronchitis, and cardiovascular diseases. This is expressed in disease incidence cases.",
      "required": [
        "value",
        "unitCode"
      ]
    },
    "photochemicalOxidantFormationHealth": {
      "type": "object",
      "properties": {
        "value": {
          "type": "string",
          "description": "photochemicalOxidantFormationHealth value"
        },
        "unitCode": {
          "type": "string",
          "description": "Unit of measurement for photochemicalOxidantFormationHealth"
        },
        "observedAt": {
          "type": "string",
          "format": "date-time",
          "description": "Timestamp when the value was observed"
        }
      },
      "description": "This measures the impact of emissions of volatile organic compounds (VOCs) and nitrogen oxides (NOx) that lead to the formation of ground-level ozone (smog), which affects human respiratory health. It is expressed in kilograms of NMVOC equivalents (kg NMVOC-Eq).",
      "required": [
        "value",
        "unitCode"
      ]
    },
    "waterUseUserDeprivationPotential": {
      "type": "object",
      "properties": {
        "value": {
          "type": "string",
          "description": "waterUseUserDeprivationPotential value"
        },
        "unitCode": {
          "type": "string",
          "description": "Unit of measurement for waterUseUserDeprivationPotential"
        },
        "observedAt": {
          "type": "string",
          "format": "date-time",
          "description": "Timestamp when the value was observed"
        }
      },
      "description": "This indicator evaluates the potential for water consumption to lead to human water deprivation, considering local water scarcity and water use efficiency. It is expressed in cubic meters of world equivalents deprived (m\u00b3 world Eq. deprived).",
      "required": [
        "value",
        "unitCode"
      ]
    }
  },
  "required": [
    "id",
    "type",
    "acidificationAccumulatedExceedanceAE",
    "climateChangeGlobalWarmingPotentialGWP",
    "climateChangeBiogenicGWP100",
    "climateChangeFossilGWP100",
    "climateChangeLandUseAndLULUCGWP",
    "ecotoxicityFreshwaterComparativeToxicCTU",
    "ecotoxicityFreshwaterInorganicsCTUe",
    "ecotoxicityFreshwaterOrganicsCTUe",
    "energyResourcesAbioticDepletionFossils",
    "eutrophicationFreshwaterNutrientsP",
    "eutrophicationMarineNutrientsN",
    "eutrophicationTerrestrialAccumExceedance",
    "humanToxicityCarcinogenicCTUh",
    "humanToxicityCarcinogenicInorganicsCTU",
    "humanToxicityCarcinogenicOrganicsCTU",
    "humanToxicityNonCarcinogenicCTUh",
    "humanToxicityNonCarcinogenicInorganicsCTU",
    "humanToxicityNonCarcinogenicOrganicsCTU",
    "ionisingRadiationHumanHealthU235",
    "landUseSoilQualityIndex",
    "materialResourcesAbioticDepletionElements",
    "ozoneDepletionPotentialODP",
    "particulateMatterFormationHealth",
    "photochemicalOxidantFormationHealth",
    "waterUseUserDeprivationPotential"
  ]
})
