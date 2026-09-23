<!-- 10-Header -->  
Entity: EPSBatch  
================<!-- /10-Header -->  
<!-- 15-License -->  
[Open License](https://raw.githubusercontent.com/european-dynamics-rnd/CIRCULOOS_Data_model/refs/heads/main/LICENSE)  
<!-- /15-License -->  
<!-- 20-Description -->  
Global description: **CIRCULOOS data model for a batch of expanded polystyrene (EPS) tracked through collection, transport and recycling in the ISLOPOL value chain, covering its handling status, its rejection and contamination figures, and the observations that characterise it.**  
version: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## List of properties  

<sup><sub>[*] If there is not a type in an attribute is because it could have several types or different formats/patterns</sub></sup>  
- `avgContaminationScore[*]`: Average contamination score associated with the batch, expressed from 0 to 1, where higher values indicate greater contamination. (Multiply by 100 to obtain the Contamination Score percentage.)  - `dateCreated[*]`: Date and time when the EPSBatch record was created, expressed as an ISO 8601 timestamp. This is the record creation time, which can differ from the time of the physical operation.  - `id[string]`: Unique entity identifier, with the format urn:ngsi-ld:EPSBatch:<facility>:<date>.  - `refEPSObservations[*]`: Identifiers of the EPSObservation entities associated with this batch. These records provide the automated contamination assessments used to characterise it.  - `refProduct[*]`: Identifier of the Product entity representing the EPS material in this batch, including its recorded quantity and unit of measurement.  - `rejectionRate[*]`: Fraction of material in the batch that was rejected, expressed on a scale from 0 to 1. (Multiply by 100 to obtain the rejection percentage.)  - `status[*]`: Current stage of the batch in the operational workflow, such as awaiting transport. It describes the batch's handling status rather than its contamination level.  - `type[string]`: NGSI Entity type. It has to be EPSBatch  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Required properties  
- `id`  - `refProduct`  - `status`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Data Model description of properties  
Sorted alphabetically (click for details)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
EPSBatch:    
  description: CIRCULOOS data model for a batch of expanded polystyrene (EPS) tracked through collection, transport and recycling in the ISLOPOL value chain, covering its handling status, its rejection and contamination figures, and the observations that characterise it.    
  properties:    
    avgContaminationScore:    
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
              maximum: 1    
              minimum: 0    
              type: number    
          required:    
            - type    
            - value    
          type: object    
      description: Average contamination score associated with the batch, expressed from 0 to 1, where higher values indicate greater contamination. (Multiply by 100 to obtain the Contamination Score percentage.)    
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
      description: Date and time when the EPSBatch record was created, expressed as an ISO 8601 timestamp. This is the record creation time, which can differ from the time of the physical operation.    
      x-ngsi:    
        type: Property    
    id:    
      description: Unique entity identifier, with the format urn:ngsi-ld:EPSBatch:<facility>:<date>.    
      type: string    
      x-ngsi:    
        type: Property    
    refEPSObservations:    
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
      description: Identifiers of the EPSObservation entities associated with this batch. These records provide the automated contamination assessments used to characterise it.    
      x-ngsi:    
        type: Relationship    
    refProduct:    
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
      description: Identifier of the Product entity representing the EPS material in this batch, including its recorded quantity and unit of measurement.    
      x-ngsi:    
        type: Relationship    
    rejectionRate:    
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
              maximum: 1    
              minimum: 0    
              type: number    
          required:    
            - type    
            - value    
          type: object    
      description: Fraction of material in the batch that was rejected, expressed on a scale from 0 to 1. (Multiply by 100 to obtain the rejection percentage.)    
      x-ngsi:    
        type: Property    
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
      description: Current stage of the batch in the operational workflow, such as awaiting transport. It describes the batch's handling status rather than its contamination level.    
      x-ngsi:    
        type: Property    
    type:    
      description: NGSI Entity type. It has to be EPSBatch    
      enum:    
        - EPSBatch    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - refProduct    
    - status    
  type: object    
  x-derived-from: https://context.dataspace-arditi.com/islopol/entities/EPSBatch/v2/schema.json    
  x-disclaimer: Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program    
  x-license-url: https://github.com/smart-data-models/circuloos_data_model/blob/master/EPSBatch/LICENSE.md    
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
Not available the example of a EPSBatch in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
#### EPSBatch NGSI-LD normalized Example    
Here is an example of a EPSBatch in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "@context": [  
    "http://circuloos-ld-context/circuloos-context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context-v1.8.jsonld"  
  ],  
  "id": "urn:ngsi-ld:EPSBatch:ARM:20260903",  
  "type": "EPSBatch",  
  "refProduct": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Product:ARM:reciclable-eps:20260903"  
  },  
  "rejectionRate": {  
    "type": "Property",  
    "value": 0.369382  
  },  
  "status": {  
    "type": "Property",  
    "value": "Aguarda transporte"  
  },  
  "avgContaminationScore": {  
    "type": "Property",  
    "value": 0.107308  
  },  
  "refEPSObservations": {  
    "type": "Relationship",  
    "object": [  
      "urn:ngsi-ld:EPSObservation:ARM:reciclable-eps:20260903"  
    ]  
  },  
  "dateCreated": {  
    "type": "Property",  
    "value": "2026-09-03T22:00:21.000Z"  
  }  
}  
```  
</details><!-- /80-Examples -->  
