<!-- 10-Header -->  
Entity: YeastBatch  
==================<!-- /10-Header -->  
<!-- 15-License -->  
[Open License](https://raw.githubusercontent.com/european-dynamics-rnd/CIRCULOOS_Data_model/refs/heads/main/LICENSE)  
<!-- /15-License -->  
<!-- 20-Description -->  
Global description: **CIRCULOOS data model for a batch of brewer's spent yeast (BSY) collected from a brewery in the Yeast2Value value chain, covering its origin and collection, its storage conditions before pick-up, and the cell count and dry matter measurements taken on receipt.**  
version: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## List of properties  

<sup><sub>[*] If there is not a type in an attribute is because it could have several types or different formats/patterns</sub></sup>  
- `batchId[*]`: Laboratory code assigned to the yeast sample on receipt (e.g. PT_0149), used to trace the batch through analysis and processing.  - `brewery[*]`: Name of the brewery (or source label) that supplied the brewer's spent yeast batch.  - `dataSource[*]`: Name of the source file or dataset the record was taken from, for traceability.  - `dryMassUnfiltered[*]`: Expected unitCode: P1. Dry matter content of the unfiltered raw yeast slurry, in % (w/w). A key parameter for processing yield and transport efficiency.  - `feedstockSource[*]`: Type of feedstock the batch represents; in Yeast2Value this is brewer's spent yeast (BSY), a by-product of beer fermentation.  - `id[string]`: Unique entity identifier, with the format urn:ngsi-ld:circuloos-yeast2value:batch:<batchId>.  - `livingCellsCount[*]`: Expected unitCode: cells/mL. Number of viable (living) yeast cells per millilitre of sample.  - `livingCellsPercent[*]`: Expected unitCode: P1. Viability of the batch: living cells as a percentage of the total cell count (livingCellsCount / totalCellCount x 100).  - `phValueRawYeast[*]`: Dimensionless. pH of the raw (untreated) spent yeast slurry, measured on receipt.  - `pickUpDate[*]`: Date on which the spent yeast was collected from the brewery (ISO 8601, YYYY-MM-DD).  - `runId[*]`: Dimensionless. Sequential run number of the sampling/analysis entry in the Yeast2Value yeast log.  - `storageDateBeforePickUp[*]`: Date from which the yeast was stored at the brewery after harvesting, before collection (ISO 8601). Together with pickUpDate it gives the storage time before pick-up.  - `storageTemperatureBeforePickUp[*]`: Expected unitCode: CEL. Temperature at which the yeast was kept at the brewery before collection. Breweries report either a single value or a bound or range, so use value for an exact figure and minValue/maxValue for a bound (e.g. "<4") or a range (e.g. "10 to 20").  - `totalCellCount[*]`: Expected unitCode: cells/mL. Total number of yeast cells (living and dead) per millilitre of sample, determined by counting-chamber microscopy.  - `type[string]`: NGSI Entity type. It has to be YeastBatch  - `valueChain[*]`: Identifier of the CIRCULOOS value chain the record belongs to (here "yeast2value").  - `volumetricFraction[*]`: Expected unitCode: P1. Mass of the yeast pellet after centrifugation relative to the total sample mass, in %. Indicates how much solid yeast biomass the slurry contains.  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Required properties  
- `batchId`  - `brewery`  - `feedstockSource`  - `id`  - `pickUpDate`  - `type`  - `valueChain`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Data Model description of properties  
Sorted alphabetically (click for details)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
YeastBatch:    
  description: CIRCULOOS data model for a batch of brewer's spent yeast (BSY) collected from a brewery in the Yeast2Value value chain, covering its origin and collection, its storage conditions before pick-up, and the cell count and dry matter measurements taken on receipt.    
  properties:    
    batchId:    
      allOf:    
        - additionalProperties: no    
          properties:    
            observedAt:    
              format: date-time    
              type: string    
            type:    
              enum:    
                - Property    
              type: string    
            value:    
              type: string    
          required:    
            - type    
            - value    
          type: object    
      description: Laboratory code assigned to the yeast sample on receipt (e.g. PT_0149), used to trace the batch through analysis and processing.    
      x-ngsi:    
        type: Property    
    brewery:    
      allOf:    
        - additionalProperties: no    
          properties:    
            observedAt:    
              format: date-time    
              type: string    
            type:    
              enum:    
                - Property    
              type: string    
            value:    
              type: string    
          required:    
            - type    
            - value    
          type: object    
      description: Name of the brewery (or source label) that supplied the brewer's spent yeast batch.    
      x-ngsi:    
        type: Property    
    dataSource:    
      allOf:    
        - additionalProperties: no    
          properties:    
            observedAt:    
              format: date-time    
              type: string    
            type:    
              enum:    
                - Property    
              type: string    
            value:    
              type: string    
          required:    
            - type    
            - value    
          type: object    
      description: Name of the source file or dataset the record was taken from, for traceability.    
      x-ngsi:    
        type: Property    
    dryMassUnfiltered:    
      allOf:    
        - additionalProperties: no    
          anyOf:    
            - required:    
                - value    
            - required:    
                - minValue    
            - required:    
                - maxValue    
          properties:    
            maxValue:    
              description: Upper bound of the value, when the source declares a range or a maximum.    
              type: number    
            minValue:    
              description: Lower bound of the value, when the source declares a range or a minimum.    
              type: number    
            observedAt:    
              format: date-time    
              type: string    
            type:    
              enum:    
                - Property    
              type: string    
            unitCode:    
              description: Unit of measurement of the value, given as a UN/CEFACT code where one exists.    
              type: string    
            value:    
              description: Exact measured value, when a single figure is known.    
              type: number    
          required:    
            - type    
            - unitCode    
          type: object    
      description: 'Expected unitCode: P1. Dry matter content of the unfiltered raw yeast slurry, in % (w/w). A key parameter for processing yield and transport efficiency.'    
      x-ngsi:    
        type: Property    
    feedstockSource:    
      allOf:    
        - additionalProperties: no    
          properties:    
            observedAt:    
              format: date-time    
              type: string    
            type:    
              enum:    
                - Property    
              type: string    
            value:    
              type: string    
          required:    
            - type    
            - value    
          type: object    
      description: Type of feedstock the batch represents; in Yeast2Value this is brewer's spent yeast (BSY), a by-product of beer fermentation.    
      x-ngsi:    
        type: Property    
    id:    
      description: Unique entity identifier, with the format urn:ngsi-ld:circuloos-yeast2value:batch:<batchId>.    
      type: string    
      x-ngsi:    
        type: Property    
    livingCellsCount:    
      allOf:    
        - additionalProperties: no    
          anyOf:    
            - required:    
                - value    
            - required:    
                - minValue    
            - required:    
                - maxValue    
          properties:    
            maxValue:    
              description: Upper bound of the value, when the source declares a range or a maximum.    
              type: number    
            minValue:    
              description: Lower bound of the value, when the source declares a range or a minimum.    
              type: number    
            observedAt:    
              format: date-time    
              type: string    
            type:    
              enum:    
                - Property    
              type: string    
            unitCode:    
              description: Unit of measurement of the value, given as a UN/CEFACT code where one exists.    
              type: string    
            value:    
              description: Exact measured value, when a single figure is known.    
              type: number    
          required:    
            - type    
            - unitCode    
          type: object    
      description: 'Expected unitCode: cells/mL. Number of viable (living) yeast cells per millilitre of sample.'    
      x-ngsi:    
        type: Property    
    livingCellsPercent:    
      allOf:    
        - additionalProperties: no    
          anyOf:    
            - required:    
                - value    
            - required:    
                - minValue    
            - required:    
                - maxValue    
          properties:    
            maxValue:    
              description: Upper bound of the value, when the source declares a range or a maximum.    
              type: number    
            minValue:    
              description: Lower bound of the value, when the source declares a range or a minimum.    
              type: number    
            observedAt:    
              format: date-time    
              type: string    
            type:    
              enum:    
                - Property    
              type: string    
            unitCode:    
              description: Unit of measurement of the value, given as a UN/CEFACT code where one exists.    
              type: string    
            value:    
              description: Exact measured value, when a single figure is known.    
              type: number    
          required:    
            - type    
            - unitCode    
          type: object    
      description: 'Expected unitCode: P1. Viability of the batch: living cells as a percentage of the total cell count (livingCellsCount / totalCellCount x 100).'    
      x-ngsi:    
        type: Property    
    phValueRawYeast:    
      allOf:    
        - additionalProperties: no    
          properties:    
            observedAt:    
              format: date-time    
              type: string    
            type:    
              enum:    
                - Property    
              type: string    
            unitCode:    
              type: string    
            value:    
              type: number    
          required:    
            - type    
            - value    
          type: object    
      description: Dimensionless. pH of the raw (untreated) spent yeast slurry, measured on receipt.    
      x-ngsi:    
        type: Property    
    pickUpDate:    
      allOf:    
        - additionalProperties: no    
          properties:    
            observedAt:    
              format: date-time    
              type: string    
            type:    
              enum:    
                - Property    
              type: string    
            value:    
              format: date    
              pattern: ^[0-9]{4}-[0-9]{2}-[0-9]{2}$    
              type: string    
          required:    
            - type    
            - value    
          type: object    
      description: Date on which the spent yeast was collected from the brewery (ISO 8601, YYYY-MM-DD).    
      x-ngsi:    
        type: Property    
    runId:    
      allOf:    
        - additionalProperties: no    
          properties:    
            observedAt:    
              format: date-time    
              type: string    
            type:    
              enum:    
                - Property    
              type: string    
            unitCode:    
              type: string    
            value:    
              type: number    
          required:    
            - type    
            - value    
          type: object    
      description: Dimensionless. Sequential run number of the sampling/analysis entry in the Yeast2Value yeast log.    
      x-ngsi:    
        type: Property    
    storageDateBeforePickUp:    
      allOf:    
        - additionalProperties: no    
          properties:    
            observedAt:    
              format: date-time    
              type: string    
            type:    
              enum:    
                - Property    
              type: string    
            value:    
              format: date    
              pattern: ^[0-9]{4}-[0-9]{2}-[0-9]{2}$    
              type: string    
          required:    
            - type    
            - value    
          type: object    
      description: Date from which the yeast was stored at the brewery after harvesting, before collection (ISO 8601). Together with pickUpDate it gives the storage time before pick-up.    
      x-ngsi:    
        type: Property    
    storageTemperatureBeforePickUp:    
      allOf:    
        - additionalProperties: no    
          anyOf:    
            - required:    
                - value    
            - required:    
                - minValue    
            - required:    
                - maxValue    
          properties:    
            maxValue:    
              description: Upper bound of the value, when the source declares a range or a maximum.    
              type: number    
            minValue:    
              description: Lower bound of the value, when the source declares a range or a minimum.    
              type: number    
            observedAt:    
              format: date-time    
              type: string    
            type:    
              enum:    
                - Property    
              type: string    
            unitCode:    
              description: Unit of measurement of the value, given as a UN/CEFACT code where one exists.    
              type: string    
            value:    
              description: Exact measured value, when a single figure is known.    
              type: number    
          required:    
            - type    
            - unitCode    
          type: object    
      description: 'Expected unitCode: CEL. Temperature at which the yeast was kept at the brewery before collection. Breweries report either a single value or a bound or range, so use value for an exact figure and minValue/maxValue for a bound (e.g. "<4") or a range (e.g. "10 to 20").'    
      x-ngsi:    
        type: Property    
    totalCellCount:    
      allOf:    
        - additionalProperties: no    
          anyOf:    
            - required:    
                - value    
            - required:    
                - minValue    
            - required:    
                - maxValue    
          properties:    
            maxValue:    
              description: Upper bound of the value, when the source declares a range or a maximum.    
              type: number    
            minValue:    
              description: Lower bound of the value, when the source declares a range or a minimum.    
              type: number    
            observedAt:    
              format: date-time    
              type: string    
            type:    
              enum:    
                - Property    
              type: string    
            unitCode:    
              description: Unit of measurement of the value, given as a UN/CEFACT code where one exists.    
              type: string    
            value:    
              description: Exact measured value, when a single figure is known.    
              type: number    
          required:    
            - type    
            - unitCode    
          type: object    
      description: 'Expected unitCode: cells/mL. Total number of yeast cells (living and dead) per millilitre of sample, determined by counting-chamber microscopy.'    
      x-ngsi:    
        type: Property    
    type:    
      description: NGSI Entity type. It has to be YeastBatch    
      enum:    
        - YeastBatch    
      type: string    
      x-ngsi:    
        type: Property    
    valueChain:    
      allOf:    
        - additionalProperties: no    
          properties:    
            observedAt:    
              format: date-time    
              type: string    
            type:    
              enum:    
                - Property    
              type: string    
            value:    
              type: string    
          required:    
            - type    
            - value    
          type: object    
      description: Identifier of the CIRCULOOS value chain the record belongs to (here "yeast2value").    
      x-ngsi:    
        type: Property    
    volumetricFraction:    
      allOf:    
        - additionalProperties: no    
          anyOf:    
            - required:    
                - value    
            - required:    
                - minValue    
            - required:    
                - maxValue    
          properties:    
            maxValue:    
              description: Upper bound of the value, when the source declares a range or a maximum.    
              type: number    
            minValue:    
              description: Lower bound of the value, when the source declares a range or a minimum.    
              type: number    
            observedAt:    
              format: date-time    
              type: string    
            type:    
              enum:    
                - Property    
              type: string    
            unitCode:    
              description: Unit of measurement of the value, given as a UN/CEFACT code where one exists.    
              type: string    
            value:    
              description: Exact measured value, when a single figure is known.    
              type: number    
          required:    
            - type    
            - unitCode    
          type: object    
      description: 'Expected unitCode: P1. Mass of the yeast pellet after centrifugation relative to the total sample mass, in %. Indicates how much solid yeast biomass the slurry contains.'    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - batchId    
    - brewery    
    - pickUpDate    
    - feedstockSource    
    - valueChain    
  type: object    
  x-derived-from: ''    
  x-disclaimer: Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program    
  x-license-url: https://github.com/smart-data-models/circuloos_data_model/blob/master/YeastBatch/LICENSE.md    
  x-model-schema: https://raw.githubusercontent.com/TO_ADD_LATER/schema.json    
  x-model-tags: ''    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Example payloads    
Not available the example of a YeastBatch in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
#### YeastBatch NGSI-LD normalized Example    
Here is an example of a YeastBatch in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "@context": [  
    "http://circuloos-ld-context/circuloos-context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context-v1.8.jsonld"  
  ],  
  "id": "urn:ngsi-ld:circuloos-yeast2value:batch:PT_0149",  
  "type": "YeastBatch",  
  "runId": {  
    "type": "Property",  
    "value": 5  
  },  
  "batchId": {  
    "type": "Property",  
    "value": "PT_0149"  
  },  
  "brewery": {  
    "type": "Property",  
    "value": "Heineken Yeast 2"  
  },  
  "pickUpDate": {  
    "type": "Property",  
    "value": "2026-01-30"  
  },  
  "storageDateBeforePickUp": {  
    "type": "Property",  
    "value": "2026-01-30"  
  },  
  "storageTemperatureBeforePickUp": {  
    "type": "Property",  
    "maxValue": 4,  
    "unitCode": "CEL"  
  },  
  "phValueRawYeast": {  
    "type": "Property",  
    "value": 5.8  
  },  
  "dryMassUnfiltered": {  
    "type": "Property",  
    "value": 18.3,  
    "unitCode": "P1"  
  },  
  "volumetricFraction": {  
    "type": "Property",  
    "value": 58.72,  
    "unitCode": "P1"  
  },  
  "totalCellCount": {  
    "type": "Property",  
    "value": 933000000,  
    "unitCode": "cells/mL"  
  },  
  "livingCellsCount": {  
    "type": "Property",  
    "value": 830000000,  
    "unitCode": "cells/mL"  
  },  
  "livingCellsPercent": {  
    "type": "Property",  
    "value": 88.96,  
    "unitCode": "P1"  
  },  
  "feedstockSource": {  
    "type": "Property",  
    "value": "Brewer's spent yeast"  
  },  
  "valueChain": {  
    "type": "Property",  
    "value": "yeast2value"  
  },  
  "dataSource": {  
    "type": "Property",  
    "value": "Yeast_Log (1).xlsx"  
  }  
}  
```  
</details><!-- /80-Examples -->  
