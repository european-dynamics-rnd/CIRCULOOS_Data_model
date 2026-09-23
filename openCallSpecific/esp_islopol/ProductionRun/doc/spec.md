<!-- 10-Header -->  
Entity: ProductionRun  
=====================<!-- /10-Header -->  
<!-- 15-License -->  
[Open License](https://raw.githubusercontent.com/european-dynamics-rnd/CIRCULOOS_Data_model/refs/heads/main/LICENSE)  
<!-- /15-License -->  
<!-- 20-Description -->  
Global description: **CIRCULOOS data model for a specific production or transformation run in the ISLOPOL value chain, covering the period over which it ran, the process performed and the input and output products involved.**  
version: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## List of properties  

<sup><sub>[*] If there is not a type in an attribute is because it could have several types or different formats/patterns</sub></sup>  
- `endDate[*]`: Date and time when the production run actually ended, expressed as an ISO 8601 timestamp. Together with startDate, it defines the recorded duration of the run.  - `id[string]`: Unique entity identifier, with the format urn:ngsi-ld:ProductionRun:<facility>:<process>:<timestamp>.  - `refInputProducts[*]`: Identifiers of the Product entities used during the production run. The referenced Product records specify input quantities and units.  - `refOutputProducts[*]`: Identifiers of the Product entities produced by the run. The referenced Product records specify output quantities and units.  - `refProcess[*]`: Identifier of the Process entity defining the production or transformation operation performed during the run.  - `startDate[*]`: Date and time when the production run actually started, expressed as an ISO 8601 timestamp. This can differ from the date embedded in the record identifier.  - `type[string]`: NGSI Entity type. It has to be ProductionRun  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Required properties  
- `id`  - `refProcess`  - `startDate`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Data Model description of properties  
Sorted alphabetically (click for details)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
ProductionRun:    
  description: CIRCULOOS data model for a specific production or transformation run in the ISLOPOL value chain, covering the period over which it ran, the process performed and the input and output products involved.    
  properties:    
    endDate:    
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
      description: Date and time when the production run actually ended, expressed as an ISO 8601 timestamp. Together with startDate, it defines the recorded duration of the run.    
      x-ngsi:    
        type: Property    
    id:    
      description: Unique entity identifier, with the format urn:ngsi-ld:ProductionRun:<facility>:<process>:<timestamp>.    
      type: string    
      x-ngsi:    
        type: Property    
    refInputProducts:    
      allOf:    
        - additionalProperties: no    
          properties:    
            object:    
              description: URNs of the referenced entities.    
              items:    
                pattern: ^urn:ngsi-ld:.+$    
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
      description: Identifiers of the Product entities used during the production run. The referenced Product records specify input quantities and units.    
      x-ngsi:    
        type: Relationship    
    refOutputProducts:    
      allOf:    
        - additionalProperties: no    
          properties:    
            object:    
              description: URNs of the referenced entities.    
              items:    
                pattern: ^urn:ngsi-ld:.+$    
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
      description: Identifiers of the Product entities produced by the run. The referenced Product records specify output quantities and units.    
      x-ngsi:    
        type: Relationship    
    refProcess:    
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
      description: Identifier of the Process entity defining the production or transformation operation performed during the run.    
      x-ngsi:    
        type: Relationship    
    startDate:    
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
      description: Date and time when the production run actually started, expressed as an ISO 8601 timestamp. This can differ from the date embedded in the record identifier.    
      x-ngsi:    
        type: Property    
    type:    
      description: NGSI Entity type. It has to be ProductionRun    
      enum:    
        - ProductionRun    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - refProcess    
    - startDate    
  type: object    
  x-derived-from: https://context.dataspace-arditi.com/islopol/entities/ProductionRun/v2/schema.json    
  x-disclaimer: Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program    
  x-license-url: https://github.com/smart-data-models/circuloos_data_model/blob/master/ProductionRun/LICENSE.md    
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
Not available the example of a ProductionRun in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
#### ProductionRun NGSI-LD normalized Example    
Here is an example of a ProductionRun in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "@context": [  
    "http://circuloos-ld-context/circuloos-context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context-v1.8.jsonld"  
  ],  
  "id": "urn:ngsi-ld:ProductionRun:Esferolight:EPSShredding:20260916T095306Z",  
  "type": "ProductionRun",  
  "startDate": {  
    "type": "Property",  
    "value": "2026-08-19T10:00:00.000Z"  
  },  
  "endDate": {  
    "type": "Property",  
    "value": "2026-08-19T10:35:00.000Z"  
  },  
  "refProcess": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Process:Esferolight:EPSShredding"  
  },  
  "refInputProducts": {  
    "type": "Relationship",  
    "object": [  
      "urn:ngsi-ld:Product:Esferolight:electricity:20260916T095306Z",  
      "urn:ngsi-ld:Product:Esferolight:PlasticBag:20260916T095306Z",  
      "urn:ngsi-ld:Product:Esferolight:UnprocessedRecycledEPS:20260916T083416Z"  
    ]  
  },  
  "refOutputProducts": {  
    "type": "Relationship",  
    "object": [  
      "urn:ngsi-ld:Product:Esferolight:ShreddedEPS:20260916T095306Z"  
    ]  
  }  
}  
```  
</details><!-- /80-Examples -->  
