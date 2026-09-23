<!-- 10-Header -->  
Entity: ProcessEvent  
====================<!-- /10-Header -->  
<!-- 15-License -->  
[Open License](https://raw.githubusercontent.com/european-dynamics-rnd/CIRCULOOS_Data_model/refs/heads/main/LICENSE)  
<!-- /15-License -->  
<!-- 20-Description -->  
Global description: **CIRCULOOS data model for a specific execution of a process in the ISLOPOL value chain, covering the input and output products, the sorting line and waste stream handled, the throughput achieved and the period over which it ran.**  
version: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## List of properties  

<sup><sub>[*] If there is not a type in an attribute is because it could have several types or different formats/patterns</sub></sup>  
- `endDate[*]`: Date and time when the process execution ended, expressed as an ISO 8601 timestamp.  - `id[string]`: Unique entity identifier, with the format urn:ngsi-ld:ProcessEvent:<facility>:<process>:<date>.  - `refInputProducts[*]`: Identifiers of the Product entities consumed or processed during the event.  - `refLcaId[*]`: Reference identifier linking the process event to a life-cycle assessment (LCA) record or dataset.  - `refOutputProducts[*]`: Identifiers of the Product entities produced by the event. Their quantities and units are stored in the referenced Product records.  - `refProcess[*]`: Identifier of the Process entity that defines the operation executed by this event, linking the recorded execution to its process description.  - `sortingLine[*]`: Name or identifier of the physical sorting line used for the event, such as ARM's paper and cardboard sorting line.  - `sortingStream[*]`: Name or classification of the waste stream being processed, such as the blue-bin paper and cardboard stream. It describes the overall input stream, which may also contain recoverable EPS.  - `startDate[*]`: Date and time when the process execution started, expressed as an ISO 8601 timestamp. Together with endDate, it defines the recorded execution period.  - `throughput[*]`: Expected unitCode: KGM. Processing throughput for the event.  - `type[string]`: NGSI Entity type. It has to be ProcessEvent  <!-- /30-PropertiesList -->  
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
ProcessEvent:    
  description: CIRCULOOS data model for a specific execution of a process in the ISLOPOL value chain, covering the input and output products, the sorting line and waste stream handled, the throughput achieved and the period over which it ran.    
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
      description: Date and time when the process execution ended, expressed as an ISO 8601 timestamp.    
      x-ngsi:    
        type: Property    
    id:    
      description: Unique entity identifier, with the format urn:ngsi-ld:ProcessEvent:<facility>:<process>:<date>.    
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
      description: Identifiers of the Product entities consumed or processed during the event.    
      x-ngsi:    
        type: Relationship    
    refLcaId:    
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
      description: Reference identifier linking the process event to a life-cycle assessment (LCA) record or dataset.    
      x-ngsi:    
        type: Property    
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
      description: Identifiers of the Product entities produced by the event. Their quantities and units are stored in the referenced Product records.    
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
      description: Identifier of the Process entity that defines the operation executed by this event, linking the recorded execution to its process description.    
      x-ngsi:    
        type: Relationship    
    sortingLine:    
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
      description: Name or identifier of the physical sorting line used for the event, such as ARM's paper and cardboard sorting line.    
      x-ngsi:    
        type: Property    
    sortingStream:    
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
      description: Name or classification of the waste stream being processed, such as the blue-bin paper and cardboard stream. It describes the overall input stream, which may also contain recoverable EPS.    
      x-ngsi:    
        type: Property    
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
      description: Date and time when the process execution started, expressed as an ISO 8601 timestamp. Together with endDate, it defines the recorded execution period.    
      x-ngsi:    
        type: Property    
    throughput:    
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
      description: 'Expected unitCode: KGM. Processing throughput for the event.'    
      x-ngsi:    
        type: Property    
    type:    
      description: NGSI Entity type. It has to be ProcessEvent    
      enum:    
        - ProcessEvent    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - refProcess    
    - startDate    
  type: object    
  x-derived-from: https://context.dataspace-arditi.com/islopol/entities/ProcessEvent/v2/schema.json    
  x-disclaimer: Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program    
  x-license-url: https://github.com/smart-data-models/circuloos_data_model/blob/master/ProcessEvent/LICENSE.md    
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
Not available the example of a ProcessEvent in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
#### ProcessEvent NGSI-LD normalized Example    
Here is an example of a ProcessEvent in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "@context": [  
    "http://circuloos-ld-context/circuloos-context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context-v1.8.jsonld"  
  ],  
  "id": "urn:ngsi-ld:ProcessEvent:ARM:blue-waste-stream-processing:20260903",  
  "type": "ProcessEvent",  
  "refProcess": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Process:ARM:blue-waste-stream-processing"  
  },  
  "refInputProducts": {  
    "type": "Relationship",  
    "object": [  
      "urn:ngsi-ld:Product:ARM:paper-cardboard-stream-waste:20260903",  
      "urn:ngsi-ld:Product:ARM:electricity:20260903",  
      "urn:ngsi-ld:Product:ARM:baling-wire:20260903"  
    ]  
  },  
  "refOutputProducts": {  
    "type": "Relationship",  
    "object": [  
      "urn:ngsi-ld:Product:ARM:paper-cardboard-bales:20260903",  
      "urn:ngsi-ld:Product:ARM:rejected-waste:20260903",  
      "urn:ngsi-ld:Product:ARM:reciclable-eps:20260903",  
      "urn:ngsi-ld:Product:ARM:rejected-eps:20260903"  
    ]  
  },  
  "sortingLine": {  
    "type": "Property",  
    "value": "Linha de triagem de Papel e Cartao da ARM"  
  },  
  "sortingStream": {  
    "type": "Property",  
    "value": "Ecoponto Azul"  
  },  
  "throughput": {  
    "type": "Property",  
    "value": 6396.748215,  
    "unitCode": "KGM"  
  },  
  "startDate": {  
    "type": "Property",  
    "value": "2026-09-02T07:05:17.000Z"  
  },  
  "endDate": {  
    "type": "Property",  
    "value": "2026-09-03T20:44:12.000Z"  
  }  
}  
```  
</details><!-- /80-Examples -->  
