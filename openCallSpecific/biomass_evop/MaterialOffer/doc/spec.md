<!-- 10-Header -->  
Entity: MaterialOffer  
=====================<!-- /10-Header -->  
<!-- 15-License -->  
[Open License](https://raw.githubusercontent.com/european-dynamics-rnd/CIRCULOOS_Data_model/refs/heads/main/LICENSE)  
<!-- /15-License -->  
<!-- 20-Description -->  
Global description: **CIRCULOOS data model for an offer of surplus biomass made available to other organisations in the EVOP circular supply chain, covering the quantity offered, the safety margin retained and the inventory the offer derives from.**  
version: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## List of properties  

<sup><sub>[*] If there is not a type in an attribute is because it could have several types or different formats/patterns</sub></sup>  
- `availableForOthers[*]`: Indicates whether the material is available for use or purchase by other organisations through the circular supply chain.  - `availableQuantityKg[*]`: Expected unitCode: KGM. Quantity of the material currently available for other users.  - `id[string]`: Unique entity identifier, with the format urn:ngsi-ld:evop:material-offer:<material>.  - `material[*]`: Identifies the biomass material being offered, such as olive pits.  - `offerPercentage[*]`: Expected unitCode: P1. Percentage of the available inventory quantity that is intended to be offered to other users.  - `quantityUnit[*]`: Unit used to express the available material quantity, e.g. kg.  - `safetyMarginPercent[*]`: Expected unitCode: P1. Percentage of stock reserved as a safety margin and therefore not intended to be offered.  - `sourceInventory[*]`: Identifier of the inventory record from which the material offer quantity is derived.  - `status[*]`: Current status of the material offer, indicating whether it is available or otherwise unavailable.  - `type[string]`: NGSI Entity type. It has to be MaterialOffer  - `updatedAt[*]`: Date and time when the material offer information was last updated.  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Required properties  
- `availableForOthers`  - `id`  - `material`  - `status`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Data Model description of properties  
Sorted alphabetically (click for details)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
MaterialOffer:    
  description: CIRCULOOS data model for an offer of surplus biomass made available to other organisations in the EVOP circular supply chain, covering the quantity offered, the safety margin retained and the inventory the offer derives from.    
  properties:    
    availableForOthers:    
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
              type: boolean    
          required:    
            - type    
            - value    
          type: object    
      description: Indicates whether the material is available for use or purchase by other organisations through the circular supply chain.    
      x-ngsi:    
        type: Property    
    availableQuantityKg:    
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
      description: 'Expected unitCode: KGM. Quantity of the material currently available for other users.'    
      x-ngsi:    
        type: Property    
    id:    
      description: Unique entity identifier, with the format urn:ngsi-ld:evop:material-offer:<material>.    
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
      description: Identifies the biomass material being offered, such as olive pits.    
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
      description: 'Expected unitCode: P1. Percentage of the available inventory quantity that is intended to be offered to other users.'    
      x-ngsi:    
        type: Property    
    quantityUnit:    
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
      description: Unit used to express the available material quantity, e.g. kg.    
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
      description: 'Expected unitCode: P1. Percentage of stock reserved as a safety margin and therefore not intended to be offered.'    
      x-ngsi:    
        type: Property    
    sourceInventory:    
      allOf:    
        - additionalProperties: no    
          properties:    
            object:    
              description: URN of the referenced entity.    
              pattern: ^urn:ngsi-ld:.+$    
              type: string    
            observedAt:    
              format: date-time    
              type: string    
            type:    
              enum:    
                - Relationship    
              type: string    
          required:    
            - type    
            - object    
          type: object    
      description: Identifier of the inventory record from which the material offer quantity is derived.    
      x-ngsi:    
        type: Relationship    
    status:    
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
      description: Current status of the material offer, indicating whether it is available or otherwise unavailable.    
      x-ngsi:    
        type: Property    
    type:    
      description: NGSI Entity type. It has to be MaterialOffer    
      enum:    
        - MaterialOffer    
      type: string    
      x-ngsi:    
        type: Property    
    updatedAt:    
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
      description: Date and time when the material offer information was last updated.    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - material    
    - availableForOthers    
    - status    
  type: object    
  x-derived-from: ''    
  x-disclaimer: Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program    
  x-license-url: https://github.com/smart-data-models/circuloos_data_model/blob/master/MaterialOffer/LICENSE.md    
  x-model-schema: https://raw.githubusercontent.com/european-dynamics-rnd/CIRCULOOS_Data_model/main/openCallSpecific/biomass_evop/MaterialOffer/schema.json    
  x-model-tags: biomass_evop    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Example payloads    
Not available the example of a MaterialOffer in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
#### MaterialOffer NGSI-LD normalized Example    
Here is an example of a MaterialOffer in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "@context": [  
    "http://circuloos-ld-context/circuloos-context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context-v1.8.jsonld"  
  ],  
  "id": "urn:ngsi-ld:evop:material-offer:olive-pits",  
  "type": "MaterialOffer",  
  "material": {  
    "type": "Property",  
    "value": "olive-pits"  
  },  
  "availableForOthers": {  
    "type": "Property",  
    "value": true  
  },  
  "availableQuantityKg": {  
    "type": "Property",  
    "value": 4500,  
    "unitCode": "KGM"  
  },  
  "quantityUnit": {  
    "type": "Property",  
    "value": "kg"  
  },  
  "offerPercentage": {  
    "type": "Property",  
    "value": 100,  
    "unitCode": "P1"  
  },  
  "safetyMarginPercent": {  
    "type": "Property",  
    "value": 10,  
    "unitCode": "P1"  
  },  
  "status": {  
    "type": "Property",  
    "value": "available"  
  },  
  "sourceInventory": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:evop:biomass-inventory:olive-pits"  
  },  
  "updatedAt": {  
    "type": "Property",  
    "value": "2026-09-17T06:57:32.026Z"  
  }  
}  
```  
</details><!-- /80-Examples -->  
