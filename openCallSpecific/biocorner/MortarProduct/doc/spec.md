<!-- 10-Header -->  
Entity: MortarProduct  
=====================<!-- /10-Header -->  
<!-- 15-License -->  
[Open License](https://raw.githubusercontent.com/european-dynamics-rnd/CIRCULOOS_Data_model/refs/heads/main/LICENSE)  
<!-- /15-License -->  
<!-- 20-Description -->  
Global description: **CIRCULOOS data model for a Biocorner bio-based mortar product formulation, covering its classification by secondary raw material source, its application guidelines and the Declaration of Performance that certifies it.**  
version: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## List of properties  

<sup><sub>[*] If there is not a type in an attribute is because it could have several types or different formats/patterns</sub></sup>  
- `applicationGuidelines[*]`: Technical guidance for product application including suitable substrates, recommended application parameters, ambient conditions, and curing requirements.  - `certifiedBy[*]`: Relationship to the DoP entity containing the performance declaration for this product. Links the product to its regulatory compliance documentation.  - `classification[*]`: Product classification based on the primary secondary raw material used in the formulation. Enables grouping and comparison by SRM source type.  - `country[*]`: The country where the product is manufactured.  - `dateCreated[*]`: Date at which the entity was created.  - `description[*]`: Technical description of the product including primary bio-based components, key performance characteristics, and intended application domain.  - `id[string]`: Unique entity identifier, with the format urn:ngsi-ld:MortarProduct:<id>.  - `name[*]`: Commercial or project-internal product name used to identify this formulation within the product portfolio.  - `productionRegion[*]`: Geographic region where the product is manufactured. Used for regional supply chain analysis and local economic impact assessment.  - `type[string]`: NGSI Entity type. It has to be MortarProduct  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Required properties  
- `certifiedBy`  - `classification`  - `id`  - `name`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Data Model description of properties  
Sorted alphabetically (click for details)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
MortarProduct:    
  description: CIRCULOOS data model for a Biocorner bio-based mortar product formulation, covering its classification by secondary raw material source, its application guidelines and the Declaration of Performance that certifies it.    
  properties:    
    applicationGuidelines:    
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
      description: Technical guidance for product application including suitable substrates, recommended application parameters, ambient conditions, and curing requirements.    
      x-ngsi:    
        type: Property    
    certifiedBy:    
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
      description: Relationship to the DoP entity containing the performance declaration for this product. Links the product to its regulatory compliance documentation.    
      x-ngsi:    
        type: Relationship    
    classification:    
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
      description: Product classification based on the primary secondary raw material used in the formulation. Enables grouping and comparison by SRM source type.    
      x-ngsi:    
        type: Property    
    country:    
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
      description: The country where the product is manufactured.    
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
      description: Technical description of the product including primary bio-based components, key performance characteristics, and intended application domain.    
      x-ngsi:    
        type: Property    
    id:    
      description: Unique entity identifier, with the format urn:ngsi-ld:MortarProduct:<id>.    
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
      description: Commercial or project-internal product name used to identify this formulation within the product portfolio.    
      x-ngsi:    
        type: Property    
    productionRegion:    
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
      description: Geographic region where the product is manufactured. Used for regional supply chain analysis and local economic impact assessment.    
      x-ngsi:    
        type: Property    
    type:    
      description: NGSI Entity type. It has to be MortarProduct    
      enum:    
        - MortarProduct    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - name    
    - classification    
    - certifiedBy    
  type: object    
  x-derived-from: ''    
  x-disclaimer: Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program    
  x-license-url: https://github.com/smart-data-models/circuloos_data_model/blob/master/MortarProduct/LICENSE.md    
  x-model-schema: https://raw.githubusercontent.com/european-dynamics-rnd/CIRCULOOS_Data_model/main/openCallSpecific/biocorner/MortarProduct/schema.json    
  x-model-tags: biocorner    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Example payloads    
Not available the example of a MortarProduct in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
#### MortarProduct NGSI-LD normalized Example    
Here is an example of a MortarProduct in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "@context": [  
    "http://circuloos-ld-context/circuloos-context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context-v1.8.jsonld"  
  ],  
  "id": "urn:ngsi-ld:MortarProduct:M16BioThermalMortar",  
  "type": "MortarProduct",  
  "productionRegion": {  
    "type": "Property",  
    "value": "Puglia",  
    "observedAt": "2026-06-16T08:05:47.000Z"  
  },  
  "name": {  
    "type": "Property",  
    "value": "M16 Bio-Thermal Mortar",  
    "observedAt": "2026-06-16T08:05:47.000Z"  
  },  
  "classification": {  
    "type": "Property",  
    "value": "Rice-based",  
    "observedAt": "2026-06-16T08:05:47.000Z"  
  },  
  "applicationGuidelines": {  
    "type": "Property",  
    "value": "Suitable for interior/exterior insulation, thickness 15-40mm, apply at 10-30C ambient temperature",  
    "observedAt": "2026-06-16T08:05:47.000Z"  
  },  
  "dateCreated": {  
    "type": "Property",  
    "value": "2026-04-13T00:00:00Z",  
    "observedAt": "2026-06-16T08:05:47.000Z"  
  },  
  "certifiedBy": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:DoP:DoP-CementFreeMortar",  
    "observedAt": "2026-06-16T08:05:47.000Z"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Lightweight thermal bio-mortar based on rice husk and straw with GGBS binder",  
    "observedAt": "2026-06-16T08:05:47.000Z"  
  },  
  "country": {  
    "type": "Property",  
    "value": "Italy",  
    "observedAt": "2026-06-16T08:05:47.000Z"  
  }  
}  
```  
</details><!-- /80-Examples -->  
