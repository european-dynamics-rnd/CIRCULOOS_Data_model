<!-- 10-Header -->  
Entity: BiomassInventory  
========================<!-- /10-Header -->  
<!-- 15-License -->  
[Open License](https://raw.githubusercontent.com/european-dynamics-rnd/CIRCULOOS_Data_model/refs/heads/main/LICENSE)  
<!-- /15-License -->  
<!-- 20-Description -->  
Global description: **CIRCULOOS data model for the calculated stock position of a biomass material in the EVOP value chain, covering physical, free, reserved and safely available quantities together with the safety margin and offer percentages applied.**  
version: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## List of properties  

<sup><sub>[*] If there is not a type in an attribute is because it could have several types or different formats/patterns</sub></sup>  
- `advertisedQuantityKg[*]`: Expected unitCode: KGM. Quantity of biomass from the inventory currently advertised or made available to other users.  - `calculatedAt[*]`: Date and time when the inventory values were last calculated or updated.  - `freeStockKg[*]`: Expected unitCode: KGM. Quantity of biomass available after accounting for quantities already committed or reserved.  - `id[string]`: Unique entity identifier, with the format urn:ngsi-ld:evop:biomass-inventory:<material>.  - `material[*]`: Identifies the biomass material represented in the inventory, such as olive pits.  - `movementCount[*]`: Dimensionless. Number of stock movements recorded for the corresponding biomass inventory.  - `offerPercentage[*]`: Expected unitCode: P1. Percentage of the available inventory intended to be offered to other users.  - `physicalStockKg[*]`: Expected unitCode: KGM. Total physical quantity of the biomass currently recorded in stock.  - `reserveKg[*]`: Expected unitCode: KGM. Quantity of biomass reserved and therefore excluded from the freely available stock.  - `safeAvailableKg[*]`: Expected unitCode: KGM. Quantity of biomass considered safely available for offering or use after applying the defined safety margin.  - `safetyMarginPercent[*]`: Expected unitCode: P1. Percentage of inventory retained as a safety margin to avoid committing the full physical stock.  - `type[string]`: NGSI Entity type. It has to be BiomassInventory  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Required properties  
- `calculatedAt`  - `id`  - `material`  - `physicalStockKg`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Data Model description of properties  
Sorted alphabetically (click for details)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
BiomassInventory:    
  description: CIRCULOOS data model for the calculated stock position of a biomass material in the EVOP value chain, covering physical, free, reserved and safely available quantities together with the safety margin and offer percentages applied.    
  properties:    
    advertisedQuantityKg:    
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
      description: 'Expected unitCode: KGM. Quantity of biomass from the inventory currently advertised or made available to other users.'    
      x-ngsi:    
        type: Property    
    calculatedAt:    
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
              format: date-time    
              pattern: ^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}(\.[0-9]+)?(Z|[+-][0-9]{2}:[0-9]{2})$    
              type: string    
          required:    
            - type    
            - value    
          type: object    
      description: Date and time when the inventory values were last calculated or updated.    
      x-ngsi:    
        type: Property    
    freeStockKg:    
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
      description: 'Expected unitCode: KGM. Quantity of biomass available after accounting for quantities already committed or reserved.'    
      x-ngsi:    
        type: Property    
    id:    
      description: Unique entity identifier, with the format urn:ngsi-ld:evop:biomass-inventory:<material>.    
      type: string    
      x-ngsi:    
        type: Property    
    material:    
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
      description: Identifies the biomass material represented in the inventory, such as olive pits.    
      x-ngsi:    
        type: Property    
    movementCount:    
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
      description: Dimensionless. Number of stock movements recorded for the corresponding biomass inventory.    
      x-ngsi:    
        type: Property    
    offerPercentage:    
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
      description: 'Expected unitCode: P1. Percentage of the available inventory intended to be offered to other users.'    
      x-ngsi:    
        type: Property    
    physicalStockKg:    
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
      description: 'Expected unitCode: KGM. Total physical quantity of the biomass currently recorded in stock.'    
      x-ngsi:    
        type: Property    
    reserveKg:    
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
      description: 'Expected unitCode: KGM. Quantity of biomass reserved and therefore excluded from the freely available stock.'    
      x-ngsi:    
        type: Property    
    safeAvailableKg:    
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
      description: 'Expected unitCode: KGM. Quantity of biomass considered safely available for offering or use after applying the defined safety margin.'    
      x-ngsi:    
        type: Property    
    safetyMarginPercent:    
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
      description: 'Expected unitCode: P1. Percentage of inventory retained as a safety margin to avoid committing the full physical stock.'    
      x-ngsi:    
        type: Property    
    type:    
      description: NGSI Entity type. It has to be BiomassInventory    
      enum:    
        - BiomassInventory    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - material    
    - physicalStockKg    
    - calculatedAt    
  type: object    
  x-derived-from: ''    
  x-disclaimer: Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program    
  x-license-url: https://github.com/smart-data-models/circuloos_data_model/blob/master/BiomassInventory/LICENSE.md    
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
Not available the example of a BiomassInventory in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
#### BiomassInventory NGSI-LD normalized Example    
Here is an example of a BiomassInventory in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "@context": [  
    "http://circuloos-ld-context/circuloos-context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context-v1.8.jsonld"  
  ],  
  "id": "urn:ngsi-ld:evop:biomass-inventory:olives",  
  "type": "BiomassInventory",  
  "material": {  
    "type": "Property",  
    "value": "olives"  
  },  
  "physicalStockKg": {  
    "type": "Property",  
    "value": 0,  
    "unitCode": "KGM"  
  },  
  "freeStockKg": {  
    "type": "Property",  
    "value": 0,  
    "unitCode": "KGM"  
  },  
  "safeAvailableKg": {  
    "type": "Property",  
    "value": 0,  
    "unitCode": "KGM"  
  },  
  "advertisedQuantityKg": {  
    "type": "Property",  
    "value": 0,  
    "unitCode": "KGM"  
  },  
  "reserveKg": {  
    "type": "Property",  
    "value": 0,  
    "unitCode": "KGM"  
  },  
  "safetyMarginPercent": {  
    "type": "Property",  
    "value": 10,  
    "unitCode": "P1"  
  },  
  "offerPercentage": {  
    "type": "Property",  
    "value": 100,  
    "unitCode": "P1"  
  },  
  "movementCount": {  
    "type": "Property",  
    "value": 0  
  },  
  "calculatedAt": {  
    "type": "Property",  
    "value": "2026-09-17T06:57:32.026Z"  
  }  
}  
```  
</details><!-- /80-Examples -->  
