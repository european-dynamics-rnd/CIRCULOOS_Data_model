<!-- 10-Header -->  
Entity: Recipe  
==============<!-- /10-Header -->  
<!-- 15-License -->  
[Open License](https://raw.githubusercontent.com/european-dynamics-rnd/CIRCULOOS_Data_model/refs/heads/main/LICENSE)  
<!-- /15-License -->  
<!-- 20-Description -->  
Global description: **CIRCULOOS data model for a Biocorner bio-based mortar formulation, covering the secondary raw materials it combines, its mixing and curing parameters and the organization that developed it.**  
version: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## List of properties  

<sup><sub>[*] If there is not a type in an attribute is because it could have several types or different formats/patterns</sub></sup>  
- `containsSRM[*]`: SRM entities combined in this formulation, listed with the primary (main bio-based) secondary raw material first.  - `curingDuration[*]`: Expected unitCode: DAY. Required curing period before the product reaches its declared performance characteristics under standard reference conditions.  - `developedBy[*]`: Relationship to the Organization entity that developed and validated this formulation through laboratory testing and characterisation.  - `formulation[*]`: Quantitative composition summary listing each component with its percentage by weight, including both SRM components and conventional binders or additives.  - `id[string]`: Unique entity identifier, with the format urn:ngsi-ld:Recipe:<id>.  - `mixingTime[*]`: Expected unitCode: MIN. Total duration of the mixing process, from initial component blending to final homogeneous mixture ready for application or casting.  - `name[*]`: Descriptive name of the recipe identifying the primary SRM and formulation variant for internal reference and traceability.  - `processingInstructions[*]`: Step-by-step manufacturing procedure including mixing parameters, component addition sequence, timing, and environmental conditions for production.  - `type[string]`: NGSI Entity type. It has to be Recipe  - `waterBinderRatio[*]`: Dimensionless. Mass ratio of water to binder content in the formulation. Critical parameter controlling workability, strength development, and porosity of the final product.  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Required properties  
- `containsSRM`  - `developedBy`  - `formulation`  - `id`  - `name`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Data Model description of properties  
Sorted alphabetically (click for details)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
Recipe:    
  description: CIRCULOOS data model for a Biocorner bio-based mortar formulation, covering the secondary raw materials it combines, its mixing and curing parameters and the organization that developed it.    
  properties:    
    containsSRM:    
      allOf:    
        - additionalProperties: no    
          properties:    
            object:    
              description: URNs of the referenced entities, each with the format urn:ngsi-ld:<type>:<id>.    
              items:    
                pattern: ^urn:ngsi-ld:[A-Za-z0-9_]+:.+$    
                type: string    
              minItems: 1    
              type: array    
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
      description: SRM entities combined in this formulation, listed with the primary (main bio-based) secondary raw material first.    
      x-ngsi:    
        type: Relationship    
    curingDuration:    
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
              description: UN/CEFACT code of the unit of measurement of the value.    
              type: string    
            value:    
              description: Exact measured value, when a single figure is known.    
              type: number    
          required:    
            - type    
            - unitCode    
          type: object    
      description: 'Expected unitCode: DAY. Required curing period before the product reaches its declared performance characteristics under standard reference conditions.'    
      x-ngsi:    
        type: Property    
    developedBy:    
      allOf:    
        - additionalProperties: no    
          properties:    
            object:    
              description: URN of the referenced entity, with the format urn:ngsi-ld:<type>:<id>.    
              pattern: ^urn:ngsi-ld:[A-Za-z0-9_]+:.+$    
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
      description: Relationship to the Organization entity that developed and validated this formulation through laboratory testing and characterisation.    
      x-ngsi:    
        type: Relationship    
    formulation:    
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
      description: Quantitative composition summary listing each component with its percentage by weight, including both SRM components and conventional binders or additives.    
      x-ngsi:    
        type: Property    
    id:    
      description: Unique entity identifier, with the format urn:ngsi-ld:Recipe:<id>.    
      type: string    
      x-ngsi:    
        type: Property    
    mixingTime:    
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
              description: UN/CEFACT code of the unit of measurement of the value.    
              type: string    
            value:    
              description: Exact measured value, when a single figure is known.    
              type: number    
          required:    
            - type    
            - unitCode    
          type: object    
      description: 'Expected unitCode: MIN. Total duration of the mixing process, from initial component blending to final homogeneous mixture ready for application or casting.'    
      x-ngsi:    
        type: Property    
    name:    
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
      description: Descriptive name of the recipe identifying the primary SRM and formulation variant for internal reference and traceability.    
      x-ngsi:    
        type: Property    
    processingInstructions:    
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
      description: Step-by-step manufacturing procedure including mixing parameters, component addition sequence, timing, and environmental conditions for production.    
      x-ngsi:    
        type: Property    
    type:    
      description: NGSI Entity type. It has to be Recipe    
      enum:    
        - Recipe    
      type: string    
      x-ngsi:    
        type: Property    
    waterBinderRatio:    
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
      description: Dimensionless. Mass ratio of water to binder content in the formulation. Critical parameter controlling workability, strength development, and porosity of the final product.    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - name    
    - formulation    
    - developedBy    
    - containsSRM    
  type: object    
  x-derived-from: ''    
  x-disclaimer: Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program    
  x-license-url: https://github.com/smart-data-models/circuloos_data_model/blob/master/Recipe/LICENSE.md    
  x-model-schema: https://raw.githubusercontent.com/european-dynamics-rnd/CIRCULOOS_Data_model/main/openCallSpecific/biocorner/Recipe/schema.json    
  x-model-tags: biocorner    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Example payloads    
Not available the example of a Recipe in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
#### Recipe NGSI-LD normalized Example    
Here is an example of a Recipe in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "@context": [  
    "http://circuloos-ld-context/circuloos-context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context-v1.8.jsonld"  
  ],  
  "id": "urn:ngsi-ld:Recipe:CementFreeMortar",  
  "type": "Recipe",  
  "containsSRM": {  
    "type": "Relationship",  
    "object": [  
      "urn:ngsi-ld:SRM:RiceHusk",  
      "urn:ngsi-ld:SRM:RiceStraw",  
      "urn:ngsi-ld:SRM:RiceHuskAsh",  
      "urn:ngsi-ld:SRM:GGBS"  
    ],  
    "observedAt": "2026-06-16T08:05:08.000Z"  
  },  
  "name": {  
    "type": "Property",  
    "value": "Cement free-Mortar",  
    "observedAt": "2026-06-16T08:05:08.000Z"  
  },  
  "mixingTime": {  
    "type": "Property",  
    "value": 20,  
    "unitCode": "MIN",  
    "observedAt": "2026-06-16T08:05:08.000Z"  
  },  
  "curingDuration": {  
    "type": "Property",  
    "value": 28,  
    "unitCode": "DAY",  
    "observedAt": "2026-06-16T08:05:08.000Z"  
  },  
  "developedBy": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Organization:CETMA",  
    "observedAt": "2026-06-16T08:05:08.000Z"  
  },  
  "processingInstructions": {  
    "type": "Property",  
    "value": "Binder preparation in concrete mixer until homogeneous consistency reached",  
    "observedAt": "2026-06-16T08:05:08.000Z"  
  },  
  "formulation": {  
    "type": "Property",  
    "value": "80% GGBS, 20% Rice Husk, alkaline activators, natural additives",  
    "observedAt": "2026-06-16T08:05:08.000Z"  
  },  
  "waterBinderRatio": {  
    "type": "Property",  
    "value": 0.32,  
    "observedAt": "2026-06-16T08:05:08.000Z"  
  }  
}  
```  
</details><!-- /80-Examples -->  
