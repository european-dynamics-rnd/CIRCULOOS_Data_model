<!-- 10-Header -->  
Entity: MortarBatch  
===================<!-- /10-Header -->  
<!-- 15-License -->  
[Open License](https://raw.githubusercontent.com/european-dynamics-rnd/CIRCULOOS_Data_model/refs/heads/main/LICENSE)  
<!-- /15-License -->  
<!-- 20-Description -->  
Global description: **CIRCULOOS data model for a single production batch of a Biocorner bio-based mortar, providing full traceability from the finished batch back to its product, recipe, manufacturing process, producer and secondary raw material batches.**  
version: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## List of properties  

<sup><sub>[*] If there is not a type in an attribute is because it could have several types or different formats/patterns</sub></sup>  
- `batchCode[*]`: Internal production batch identifier assigned by the manufacturer for traceability. Follows a structured naming convention including product code, year, and sequence number.  - `dateCreated[*]`: Date at which the entity was created.  - `description[*]`: Free-text description of the production batch including production scale, total quantity produced, and any notable quality observations.  - `id[string]`: Unique entity identifier, with the format urn:ngsi-ld:MortarBatch:<id>.  - `instanceOf[*]`: Relationship linking this production batch to its parent MortarProduct entity. Establishes which product line this specific batch belongs to.  - `producedBy[*]`: Relationship to the Organization entity responsible for manufacturing this batch. Identifies the production facility and legal entity.  - `producedFromRecipe[*]`: Relationship to the Recipe entity whose formulation was followed during production. Enables traceability from final product back to formulation specifications.  - `type[string]`: NGSI Entity type. It has to be MortarBatch  - `usedProcess[*]`: Relationship to the MortarProcess entity describing the manufacturing procedure applied. Links the batch to specific energy, water, and waste generation data.  - `usedSRMBatches[*]`: SRMBatch entities used as input material, listed with the batch of the primary SRM first. Enables full upstream traceability to raw material origin and supplier.  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Required properties  
- `batchCode`  - `id`  - `instanceOf`  - `producedBy`  - `producedFromRecipe`  - `type`  - `usedProcess`  - `usedSRMBatches`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Data Model description of properties  
Sorted alphabetically (click for details)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
MortarBatch:    
  description: CIRCULOOS data model for a single production batch of a Biocorner bio-based mortar, providing full traceability from the finished batch back to its product, recipe, manufacturing process, producer and secondary raw material batches.    
  properties:    
    batchCode:    
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
      description: Internal production batch identifier assigned by the manufacturer for traceability. Follows a structured naming convention including product code, year, and sequence number.    
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
      description: Free-text description of the production batch including production scale, total quantity produced, and any notable quality observations.    
      x-ngsi:    
        type: Property    
    id:    
      description: Unique entity identifier, with the format urn:ngsi-ld:MortarBatch:<id>.    
      type: string    
      x-ngsi:    
        type: Property    
    instanceOf:    
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
      description: Relationship linking this production batch to its parent MortarProduct entity. Establishes which product line this specific batch belongs to.    
      x-ngsi:    
        type: Relationship    
    producedBy:    
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
      description: Relationship to the Organization entity responsible for manufacturing this batch. Identifies the production facility and legal entity.    
      x-ngsi:    
        type: Relationship    
    producedFromRecipe:    
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
      description: Relationship to the Recipe entity whose formulation was followed during production. Enables traceability from final product back to formulation specifications.    
      x-ngsi:    
        type: Relationship    
    type:    
      description: NGSI Entity type. It has to be MortarBatch    
      enum:    
        - MortarBatch    
      type: string    
      x-ngsi:    
        type: Property    
    usedProcess:    
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
      description: Relationship to the MortarProcess entity describing the manufacturing procedure applied. Links the batch to specific energy, water, and waste generation data.    
      x-ngsi:    
        type: Relationship    
    usedSRMBatches:    
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
      description: SRMBatch entities used as input material, listed with the batch of the primary SRM first. Enables full upstream traceability to raw material origin and supplier.    
      x-ngsi:    
        type: Relationship    
  required:    
    - id    
    - type    
    - batchCode    
    - instanceOf    
    - producedFromRecipe    
    - producedBy    
    - usedProcess    
    - usedSRMBatches    
  type: object    
  x-derived-from: ''    
  x-disclaimer: Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program    
  x-license-url: https://github.com/smart-data-models/circuloos_data_model/blob/master/MortarBatch/LICENSE.md    
  x-model-schema: https://raw.githubusercontent.com/european-dynamics-rnd/CIRCULOOS_Data_model/main/openCallSpecific/biocorner/MortarBatch/schema.json    
  x-model-tags: biocorner    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Example payloads    
Not available the example of a MortarBatch in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
#### MortarBatch NGSI-LD normalized Example    
Here is an example of a MortarBatch in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "@context": [  
    "http://circuloos-ld-context/circuloos-context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context-v1.8.jsonld"  
  ],  
  "id": "urn:ngsi-ld:MortarBatch:MB-M1-2026-001",  
  "type": "MortarBatch",  
  "instanceOf": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:MortarProduct:SuperThermoblock",  
    "observedAt": "2026-06-16T08:06:08.000Z"  
  },  
  "batchCode": {  
    "type": "Property",  
    "value": "MB-M1-2026-001",  
    "observedAt": "2026-06-16T08:06:08.000Z"  
  },  
  "usedProcess": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:MortarProcess:DryMixing-Mortar1",  
    "observedAt": "2026-06-16T08:06:08.000Z"  
  },  
  "producedFromRecipe": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Recipe:MortarSuperThermoblock",  
    "observedAt": "2026-06-16T08:06:08.000Z"  
  },  
  "producedBy": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Organization:LITOKOL",  
    "observedAt": "2026-06-16T08:06:08.000Z"  
  },  
  "usedSRMBatches": {  
    "type": "Relationship",  
    "object": [  
      "urn:ngsi-ld:SRMBatch:POS-2025-DEC"  
    ],  
    "observedAt": "2026-06-16T08:06:08.000Z"  
  },  
  "dateCreated": {  
    "type": "Property",  
    "value": "2026-04-15T00:00:00Z",  
    "observedAt": "2026-06-16T08:06:08.000Z"  
  },  
  "description": {  
    "type": "Property",  
    "value": "First production batch MORTAR 1, pilot scale 25 litres",  
    "observedAt": "2026-06-16T08:06:08.000Z"  
  }  
}  
```  
</details><!-- /80-Examples -->  
