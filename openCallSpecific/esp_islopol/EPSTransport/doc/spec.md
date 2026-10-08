<!-- 10-Header -->  
Entity: EPSTransport  
====================<!-- /10-Header -->  
<!-- 15-License -->  
[Open License](https://raw.githubusercontent.com/european-dynamics-rnd/CIRCULOOS_Data_model/refs/heads/main/LICENSE)  
<!-- /15-License -->  
<!-- 20-Description -->  
Global description: **CIRCULOOS data model for a transport operation carrying one or more EPS batches between facilities in the ISLOPOL value chain, covering departure and arrival times, the origin and destination facilities, the vehicle used and the batches shipped.**  
version: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## List of properties  

<sup><sub>[*] If there is not a type in an attribute is because it could have several types or different formats/patterns</sub></sup>  
- `arrivalTime[*]`: Date and time when the EPS shipment arrived at the destination facility, expressed as an ISO 8601 timestamp.  - `departureTime[*]`: Date and time when the EPS shipment departed from the origin facility, expressed as an ISO 8601 timestamp.  - `destination[*]`: Identifier of the Factory entity representing the facility receiving the EPS shipment, such as Esferolight.  - `id[string]`: Unique entity identifier, with the format urn:ngsi-ld:EPSTransport:<transportId>.  - `origin[*]`: Identifier of the Factory entity representing the facility from which the EPS shipment departs.  - `refEPSBatch[*]`: Identifiers of the EPSBatch entities included in the shipment. A single transport operation can therefore carry material from several batches.  - `refVehicle[*]`: Identifier of the Vehicle entity used to carry the EPS shipment.  - `type[string]`: NGSI Entity type. It has to be EPSTransport  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Required properties  
- `departureTime`  - `id`  - `refEPSBatch`  - `refVehicle`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Data Model description of properties  
Sorted alphabetically (click for details)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
EPSTransport:    
  description: CIRCULOOS data model for a transport operation carrying one or more EPS batches between facilities in the ISLOPOL value chain, covering departure and arrival times, the origin and destination facilities, the vehicle used and the batches shipped.    
  properties:    
    arrivalTime:    
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
      description: Date and time when the EPS shipment arrived at the destination facility, expressed as an ISO 8601 timestamp.    
      x-ngsi:    
        type: Property    
    departureTime:    
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
      description: Date and time when the EPS shipment departed from the origin facility, expressed as an ISO 8601 timestamp.    
      x-ngsi:    
        type: Property    
    destination:    
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
      description: Identifier of the Factory entity representing the facility receiving the EPS shipment, such as Esferolight.    
      x-ngsi:    
        type: Relationship    
    id:    
      description: Unique entity identifier, with the format urn:ngsi-ld:EPSTransport:<transportId>.    
      type: string    
      x-ngsi:    
        type: Property    
    origin:    
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
      description: Identifier of the Factory entity representing the facility from which the EPS shipment departs.    
      x-ngsi:    
        type: Relationship    
    refEPSBatch:    
      allOf:    
        - additionalProperties: no    
          properties:    
            object:    
              description: URN of the referenced entity, or a list of URNs.    
              oneOf:    
                - pattern: ^urn:ngsi-ld:.+$    
                  type: string    
                - items:    
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
      description: Identifiers of the EPSBatch entities included in the shipment. A single transport operation can therefore carry material from several batches.    
      x-ngsi:    
        type: Relationship    
    refVehicle:    
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
      description: Identifier of the Vehicle entity used to carry the EPS shipment.    
      x-ngsi:    
        type: Relationship    
    type:    
      description: NGSI Entity type. It has to be EPSTransport    
      enum:    
        - EPSTransport    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - refEPSBatch    
    - departureTime    
    - refVehicle    
  type: object    
  x-derived-from: https://context.dataspace-arditi.com/islopol/entities/EPSTransport/v2/schema.json    
  x-disclaimer: Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program    
  x-license-url: https://github.com/smart-data-models/circuloos_data_model/blob/master/EPSTransport/LICENSE.md    
  x-model-schema: https://raw.githubusercontent.com/european-dynamics-rnd/CIRCULOOS_Data_model/main/openCallSpecific/esp_islopol/EPSTransport/schema.json    
  x-model-tags: esp_islopol    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Example payloads    
Not available the example of a EPSTransport in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
#### EPSTransport NGSI-LD normalized Example    
Here is an example of a EPSTransport in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "@context": [  
    "http://circuloos-ld-context/circuloos-context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context-v1.8.jsonld"  
  ],  
  "id": "urn:ngsi-ld:EPSTransport:1789374097444",  
  "type": "EPSTransport",  
  "departureTime": {  
    "type": "Property",  
    "value": "2026-08-18T09:50:00.000Z"  
  },  
  "arrivalTime": {  
    "type": "Property",  
    "value": "2026-08-18T10:15:00.000Z"  
  },  
  "origin": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Factory:ARM:TrasferStation"  
  },  
  "destination": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Factory:Esferolight:Canical"  
  },  
  "refVehicle": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Vehicle:ARM:86-NI-59"  
  },  
  "refEPSBatch": {  
    "type": "Relationship",  
    "object": [  
      "urn:ngsi-ld:EPSBatch:ARM:20260810",  
      "urn:ngsi-ld:EPSBatch:ARM:20260808",  
      "urn:ngsi-ld:EPSBatch:ARM:20260807",  
      "urn:ngsi-ld:EPSBatch:ARM:20260806",  
      "urn:ngsi-ld:EPSBatch:ARM:20260805",  
      "urn:ngsi-ld:EPSBatch:ARM:20260804",  
      "urn:ngsi-ld:EPSBatch:ARM:20260731",  
      "urn:ngsi-ld:EPSBatch:ARM:20260730",  
      "urn:ngsi-ld:EPSBatch:ARM:20260729",  
      "urn:ngsi-ld:EPSBatch:ARM:20260728",  
      "urn:ngsi-ld:EPSBatch:ARM:20260727",  
      "urn:ngsi-ld:EPSBatch:ARM:20260725",  
      "urn:ngsi-ld:EPSBatch:ARM:20260724",  
      "urn:ngsi-ld:EPSBatch:ARM:20260723",  
      "urn:ngsi-ld:EPSBatch:ARM:20260722"  
    ]  
  }  
}  
```  
</details><!-- /80-Examples -->  
