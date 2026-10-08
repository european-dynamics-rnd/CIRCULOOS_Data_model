<!-- 10-Header -->  
Entity: MortarProcess  
=====================<!-- /10-Header -->  
<!-- 15-License -->  
[Open License](https://raw.githubusercontent.com/european-dynamics-rnd/CIRCULOOS_Data_model/refs/heads/main/LICENSE)  
<!-- /15-License -->  
<!-- 20-Description -->  
Global description: **CIRCULOOS data model for a Biocorner mortar manufacturing process, covering the energy, water, waste and carbon dioxide figures recorded per functional unit of production at the manufacturing facility boundary.**  
version: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## List of properties  

<sup><sub>[*] If there is not a type in an attribute is because it could have several types or different formats/patterns</sub></sup>  
- `CO2emission[*]`: Expected unitCode: KGM/TNE. Carbon dioxide equivalent emissions per functional unit of production. Covers direct process emissions at the manufacturing facility boundary.  - `dateCreated[*]`: Date at which the entity was created.  - `description[*]`: Technical description of the manufacturing process including equipment type, automation level, and key control parameters.  - `energyConsumption[*]`: Expected unitCode: KWH/TNE. Electrical and thermal energy consumed per functional unit of production. Measured at the manufacturing facility boundary.  - `id[string]`: Unique entity identifier, with the format urn:ngsi-ld:MortarProcess:<id>.  - `name[*]`: Descriptive name identifying the process variant, including the product type and version number for traceability across process iterations.  - `recyclingProcess[*]`: Description of how production waste and off-spec material can be recirculated or recovered within the manufacturing process or downstream.  - `type[string]`: NGSI Entity type. It has to be MortarProcess  - `wasteGeneration[*]`: Expected unitCode: KGM/TNE. Total solid waste generated per functional unit of production. Includes off-spec material, cleaning residues, and packaging waste.  - `waterConsumption[*]`: Expected unitCode: LTR/TNE. Total water consumed per functional unit of production. Includes process water and cleaning water at the manufacturing facility.  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Required properties  
- `id`  - `name`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Data Model description of properties  
Sorted alphabetically (click for details)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
MortarProcess:    
  description: CIRCULOOS data model for a Biocorner mortar manufacturing process, covering the energy, water, waste and carbon dioxide figures recorded per functional unit of production at the manufacturing facility boundary.    
  properties:    
    CO2emission:    
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
      description: 'Expected unitCode: KGM/TNE. Carbon dioxide equivalent emissions per functional unit of production. Covers direct process emissions at the manufacturing facility boundary.'    
      x-ngsi:    
        type: Property    
    dateCreated:    
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
      description: Date at which the entity was created.    
      x-ngsi:    
        type: Property    
    description:    
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
      description: Technical description of the manufacturing process including equipment type, automation level, and key control parameters.    
      x-ngsi:    
        type: Property    
    energyConsumption:    
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
      description: 'Expected unitCode: KWH/TNE. Electrical and thermal energy consumed per functional unit of production. Measured at the manufacturing facility boundary.'    
      x-ngsi:    
        type: Property    
    id:    
      description: Unique entity identifier, with the format urn:ngsi-ld:MortarProcess:<id>.    
      type: string    
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
      description: Descriptive name identifying the process variant, including the product type and version number for traceability across process iterations.    
      x-ngsi:    
        type: Property    
    recyclingProcess:    
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
      description: Description of how production waste and off-spec material can be recirculated or recovered within the manufacturing process or downstream.    
      x-ngsi:    
        type: Property    
    type:    
      description: NGSI Entity type. It has to be MortarProcess    
      enum:    
        - MortarProcess    
      type: string    
      x-ngsi:    
        type: Property    
    wasteGeneration:    
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
      description: 'Expected unitCode: KGM/TNE. Total solid waste generated per functional unit of production. Includes off-spec material, cleaning residues, and packaging waste.'    
      x-ngsi:    
        type: Property    
    waterConsumption:    
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
      description: 'Expected unitCode: LTR/TNE. Total water consumed per functional unit of production. Includes process water and cleaning water at the manufacturing facility.'    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - name    
  type: object    
  x-derived-from: ''    
  x-disclaimer: Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program    
  x-license-url: https://github.com/smart-data-models/circuloos_data_model/blob/master/MortarProcess/LICENSE.md    
  x-model-schema: https://raw.githubusercontent.com/european-dynamics-rnd/CIRCULOOS_Data_model/main/openCallSpecific/biocorner/MortarProcess/schema.json    
  x-model-tags: biocorner    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Example payloads    
Not available the example of a MortarProcess in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
#### MortarProcess NGSI-LD normalized Example    
Here is an example of a MortarProcess in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "@context": [  
    "http://circuloos-ld-context/circuloos-context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context-v1.8.jsonld"  
  ],  
  "id": "urn:ngsi-ld:MortarProcess:DryMixing-Mortar1",  
  "type": "MortarProcess",  
  "name": {  
    "type": "Property",  
    "value": "Industrial Dry Mixing Process - MORTAR 1 Posidonia",  
    "observedAt": "2026-06-15T15:16:02.000Z"  
  },  
  "energyConsumption": {  
    "type": "Property",  
    "value": 60,  
    "unitCode": "KWH/TNE",  
    "observedAt": "2026-06-15T15:16:02.000Z"  
  },  
  "CO2emission": {  
    "type": "Property",  
    "value": 70,  
    "unitCode": "KGM/TNE",  
    "observedAt": "2026-06-15T15:16:02.000Z"  
  },  
  "dateCreated": {  
    "type": "Property",  
    "value": "2018-01-06T00:00:00Z",  
    "observedAt": "2026-06-15T15:16:02.000Z"  
  },  
  "waterConsumption": {  
    "type": "Property",  
    "maxValue": 100,  
    "unitCode": "LTR/TNE",  
    "observedAt": "2026-06-15T15:16:02.000Z"  
  },  
  "wasteGeneration": {  
    "type": "Property",  
    "maxValue": 10,  
    "unitCode": "KGM/TNE",  
    "observedAt": "2026-06-15T15:16:02.000Z"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Automated powder mixing system with controlled temperature and humidity",  
    "observedAt": "2026-06-15T15:16:02.000Z"  
  },  
  "recyclingProcess": {  
    "type": "Property",  
    "value": "100% powders produced recyclable",  
    "observedAt": "2026-06-15T15:16:02.000Z"  
  }  
}  
```  
</details><!-- /80-Examples -->  
