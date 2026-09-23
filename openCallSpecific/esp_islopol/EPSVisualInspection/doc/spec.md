<!-- 10-Header -->  
Entity: EPSVisualInspection  
===========================<!-- /10-Header -->  
<!-- 15-License -->  
[Open License](https://raw.githubusercontent.com/european-dynamics-rnd/CIRCULOOS_Data_model/refs/heads/main/LICENSE)  
<!-- /15-License -->  
<!-- 20-Description -->  
Global description: **CIRCULOOS data model for a visual inspection of EPS material received at a recycling facility in the ISLOPOL value chain, covering the inspection period, the mass rejected and the transport and output products it links to.**  
version: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## List of properties  

<sup><sub>[*] If there is not a type in an attribute is because it could have several types or different formats/patterns</sub></sup>  
- `endDate[*]`: Date and time when the visual inspection ended, expressed as an ISO 8601 timestamp.  - `id[string]`: Unique entity identifier, with the format urn:ngsi-ld:EPSVisualInspection:<facility>:<timestamp>.  - `refEPSTransport[*]`: Identifier of the EPSTransport operation that delivered the EPS being inspected, linking the inspection to the shipment and its batches.  - `refOutputProducts[*]`: Identifiers of Product entities linked as outputs of the inspection, providing traceability to the material that proceeds through the recycling workflow.  - `rejections[*]`: Expected unitCode: KGM. Mass of material rejected during the visual inspection. This is an absolute mass, not a rejection percentage.  - `startDate[*]`: Date and time when the visual inspection started, expressed as an ISO 8601 timestamp.  - `type[string]`: NGSI Entity type. It has to be EPSVisualInspection  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Required properties  
- `id`  - `startDate`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Data Model description of properties  
Sorted alphabetically (click for details)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
EPSVisualInspection:    
  description: CIRCULOOS data model for a visual inspection of EPS material received at a recycling facility in the ISLOPOL value chain, covering the inspection period, the mass rejected and the transport and output products it links to.    
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
      description: Date and time when the visual inspection ended, expressed as an ISO 8601 timestamp.    
      x-ngsi:    
        type: Property    
    id:    
      description: Unique entity identifier, with the format urn:ngsi-ld:EPSVisualInspection:<facility>:<timestamp>.    
      type: string    
      x-ngsi:    
        type: Property    
    refEPSTransport:    
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
      description: Identifier of the EPSTransport operation that delivered the EPS being inspected, linking the inspection to the shipment and its batches.    
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
      description: Identifiers of Product entities linked as outputs of the inspection, providing traceability to the material that proceeds through the recycling workflow.    
      x-ngsi:    
        type: Relationship    
    rejections:    
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
      description: 'Expected unitCode: KGM. Mass of material rejected during the visual inspection. This is an absolute mass, not a rejection percentage.'    
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
      description: Date and time when the visual inspection started, expressed as an ISO 8601 timestamp.    
      x-ngsi:    
        type: Property    
    type:    
      description: NGSI Entity type. It has to be EPSVisualInspection    
      enum:    
        - EPSVisualInspection    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - startDate    
  type: object    
  x-derived-from: https://context.dataspace-arditi.com/islopol/entities/EPSVisualInspection/v2/schema.json    
  x-disclaimer: Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program    
  x-license-url: https://github.com/smart-data-models/circuloos_data_model/blob/master/EPSVisualInspection/LICENSE.md    
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
Not available the example of a EPSVisualInspection in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
#### EPSVisualInspection NGSI-LD normalized Example    
Here is an example of a EPSVisualInspection in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "@context": [  
    "http://circuloos-ld-context/circuloos-context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context-v1.8.jsonld"  
  ],  
  "id": "urn:ngsi-ld:EPSVisualInspection:Esferolight:20260702T145010Z",  
  "type": "EPSVisualInspection",  
  "startDate": {  
    "type": "Property",  
    "value": "2026-06-02T13:00:00.000Z"  
  },  
  "endDate": {  
    "type": "Property",  
    "value": "2026-06-02T16:00:00.000Z"  
  },  
  "rejections": {  
    "type": "Property",  
    "value": 10,  
    "unitCode": "KGM"  
  },  
  "refOutputProducts": {  
    "type": "Relationship",  
    "object": [  
      "urn:ngsi-ld:Product:Esferolight:ShreddedEPS:20260702T153321Z"  
    ]  
  },  
  "refEPSTransport": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:EPSTransport:13082026"  
  }  
}  
```  
</details><!-- /80-Examples -->  
