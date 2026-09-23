<!-- 10-Header -->  
Entity: DoP  
===========<!-- /10-Header -->  
<!-- 15-License -->  
[Open License](https://raw.githubusercontent.com/european-dynamics-rnd/CIRCULOOS_Data_model/refs/heads/main/LICENSE)  
<!-- /15-License -->  
<!-- 20-Description -->  
Global description: **CIRCULOOS data model for the Declaration of Performance (DoP) issued for a Biocorner bio-based mortar product, covering the certification body, the functional unit used for the declaration and the declared performance characteristics.**  
version: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## List of properties  

<sup><sub>[*] If there is not a type in an attribute is because it could have several types or different formats/patterns</sub></sup>  
- `certificationBody[*]`: Notified body or laboratory responsible for product performance assessment under the relevant regulatory framework. Includes certification system reference.  - `dateCreated[*]`: Date at which the entity was created.  - `functionalUnit[*]`: Expected unitCode: KGM or MTQ. Reference unit for performance declaration, typically expressed as mass or volume. Used as the basis for comparing performance across different product formulations.  - `id[string]`: Unique entity identifier, with the format urn:ngsi-ld:DoP:<id>.  - `name[*]`: Unique identifier name of the Declaration of Performance document, following an internal naming convention including product reference, year, and version.  - `performanceSummary[*]`: Aggregated summary of essential performance characteristics declared for the product, including relevant mechanical, thermal, and physical properties with their units.  - `type[string]`: NGSI Entity type. It has to be DoP  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Required properties  
- `certificationBody`  - `id`  - `name`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Data Model description of properties  
Sorted alphabetically (click for details)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
DoP:    
  description: CIRCULOOS data model for the Declaration of Performance (DoP) issued for a Biocorner bio-based mortar product, covering the certification body, the functional unit used for the declaration and the declared performance characteristics.    
  properties:    
    certificationBody:    
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
      description: Notified body or laboratory responsible for product performance assessment under the relevant regulatory framework. Includes certification system reference.    
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
              format: date    
              pattern: ^[0-9]{4}-[0-9]{2}-[0-9]{2}$    
              type: string    
          required:    
            - type    
            - value    
          type: object    
      description: Date at which the entity was created.    
      x-ngsi:    
        type: Property    
    functionalUnit:    
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
      description: 'Expected unitCode: KGM or MTQ. Reference unit for performance declaration, typically expressed as mass or volume. Used as the basis for comparing performance across different product formulations.'    
      x-ngsi:    
        type: Property    
    id:    
      description: Unique entity identifier, with the format urn:ngsi-ld:DoP:<id>.    
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
      description: Unique identifier name of the Declaration of Performance document, following an internal naming convention including product reference, year, and version.    
      x-ngsi:    
        type: Property    
    performanceSummary:    
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
      description: Aggregated summary of essential performance characteristics declared for the product, including relevant mechanical, thermal, and physical properties with their units.    
      x-ngsi:    
        type: Property    
    type:    
      description: NGSI Entity type. It has to be DoP    
      enum:    
        - DoP    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - name    
    - certificationBody    
  type: object    
  x-derived-from: ''    
  x-disclaimer: Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program    
  x-license-url: https://github.com/smart-data-models/circuloos_data_model/blob/master/DoP/LICENSE.md    
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
Not available the example of a DoP in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
#### DoP NGSI-LD normalized Example    
Here is an example of a DoP in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "@context": [  
    "http://circuloos-ld-context/circuloos-context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context-v1.8.jsonld"  
  ],  
  "id": "urn:ngsi-ld:DoP:DoP-CementFreeMortar",  
  "type": "DoP",  
  "certificationBody": {  
    "type": "Property",  
    "value": "CETMA",  
    "observedAt": "2026-06-15T15:17:44.000Z"  
  },  
  "name": {  
    "type": "Property",  
    "value": "DoP Cement free-Mortar",  
    "observedAt": "2026-06-15T15:17:44.000Z"  
  },  
  "dateCreated": {  
    "type": "Property",  
    "value": "2026-04-12",  
    "observedAt": "2026-06-15T15:17:44.000Z"  
  },  
  "performanceSummary": {  
    "type": "Property",  
    "value": "Compressive strength: 27 MPa",  
    "observedAt": "2026-06-15T15:17:44.000Z"  
  },  
  "functionalUnit": {  
    "type": "Property",  
    "value": 1,  
    "unitCode": "KGM",  
    "observedAt": "2026-06-15T15:17:44.000Z"  
  }  
}  
```  
</details><!-- /80-Examples -->  
