<!-- 10-Header -->  
Entity: Organization  
====================<!-- /10-Header -->  
<!-- 15-License -->  
[Open License](https://raw.githubusercontent.com/european-dynamics-rnd/CIRCULOOS_Data_model/refs/heads/main/LICENSE)  
<!-- /15-License -->  
<!-- 20-Description -->  
Global description: **CIRCULOOS data model for an organization participating in the Biocorner supply chain, covering its legal identity, contact details and its functional role and tier within the supply chain.**  
version: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## List of properties  

<sup><sub>[*] If there is not a type in an attribute is because it could have several types or different formats/patterns</sub></sup>  
- `address[*]`: The mailing address of the organization.  - `city[*]`: The city in which the organization is located.  - `contactEmail[*]`: Email address of the organization.  - `contactPhone[*]`: Telephone number of the organization.  - `country[*]`: The country in which the organization is located.  - `id[string]`: Unique entity identifier, with the format urn:ngsi-ld:Organization:<id>.  - `legalForm[*]`: Legal entity classification (e.g. Limited Liability Company, Research Center, Public University). Relevant for consortium agreements and contractual arrangements.  - `name[*]`: Full official name of the organization as registered in public records, including legal suffix where applicable.  - `postalCode[*]`: The postal code of the organization address.  - `region[*]`: Administrative region where the organization is headquartered. Used for regional supply chain mapping and geographic analysis.  - `role[*]`: Functional role of the organization within the project supply chain (e.g. RTO, Manufacturer, Contract Manufacturer, SRM Supplier).  - `supplyChainRole[*]`: High-level classification of the organization function: RTO for research and development, Manufacturer for production, or SRM Supplier for material sourcing.  - `tier[*]`: Supply chain tier relative to final product: Tier 0 for entities directly involved in product development or manufacturing, Tier 1 for raw material suppliers.  - `type[string]`: NGSI Entity type. It has to be Organization  - `website[*]`: Website of the organization.  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Required properties  
- `id`  - `name`  - `supplyChainRole`  - `tier`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Data Model description of properties  
Sorted alphabetically (click for details)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
Organization:    
  description: CIRCULOOS data model for an organization participating in the Biocorner supply chain, covering its legal identity, contact details and its functional role and tier within the supply chain.    
  properties:    
    address:    
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
      description: The mailing address of the organization.    
      x-ngsi:    
        type: Property    
    city:    
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
      description: The city in which the organization is located.    
      x-ngsi:    
        type: Property    
    contactEmail:    
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
      description: Email address of the organization.    
      x-ngsi:    
        type: Property    
    contactPhone:    
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
      description: Telephone number of the organization.    
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
      description: The country in which the organization is located.    
      x-ngsi:    
        type: Property    
    id:    
      description: Unique entity identifier, with the format urn:ngsi-ld:Organization:<id>.    
      type: string    
      x-ngsi:    
        type: Property    
    legalForm:    
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
      description: Legal entity classification (e.g. Limited Liability Company, Research Center, Public University). Relevant for consortium agreements and contractual arrangements.    
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
      description: Full official name of the organization as registered in public records, including legal suffix where applicable.    
      x-ngsi:    
        type: Property    
    postalCode:    
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
      description: The postal code of the organization address.    
      x-ngsi:    
        type: Property    
    region:    
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
      description: Administrative region where the organization is headquartered. Used for regional supply chain mapping and geographic analysis.    
      x-ngsi:    
        type: Property    
    role:    
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
      description: Functional role of the organization within the project supply chain (e.g. RTO, Manufacturer, Contract Manufacturer, SRM Supplier).    
      x-ngsi:    
        type: Property    
    supplyChainRole:    
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
      description: 'High-level classification of the organization function: RTO for research and development, Manufacturer for production, or SRM Supplier for material sourcing.'    
      x-ngsi:    
        type: Property    
    tier:    
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
      description: 'Supply chain tier relative to final product: Tier 0 for entities directly involved in product development or manufacturing, Tier 1 for raw material suppliers.'    
      x-ngsi:    
        type: Property    
    type:    
      description: NGSI Entity type. It has to be Organization    
      enum:    
        - Organization    
      type: string    
      x-ngsi:    
        type: Property    
    website:    
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
      description: Website of the organization.    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - name    
    - supplyChainRole    
    - tier    
  type: object    
  x-derived-from: ''    
  x-disclaimer: Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program    
  x-license-url: https://github.com/smart-data-models/circuloos_data_model/blob/master/Organization/LICENSE.md    
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
Not available the example of a Organization in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
#### Organization NGSI-LD normalized Example    
Here is an example of a Organization in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "@context": [  
    "http://circuloos-ld-context/circuloos-context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context-v1.8.jsonld"  
  ],  
  "id": "urn:ngsi-ld:Organization:CESTHA",  
  "type": "Organization",  
  "name": {  
    "type": "Property",  
    "value": "CESTHA - Centro Sperimentale per la Tutela degli Habitat",  
    "observedAt": "2026-06-16T08:04:28.000Z"  
  },  
  "region": {  
    "type": "Property",  
    "value": "Emilia-Romagna",  
    "observedAt": "2026-06-16T08:04:28.000Z"  
  },  
  "supplyChainRole": {  
    "type": "Property",  
    "value": "SRM Supplier",  
    "observedAt": "2026-06-16T08:04:28.000Z"  
  },  
  "postalCode": {  
    "type": "Property",  
    "value": "47042",  
    "observedAt": "2026-06-16T08:04:28.000Z"  
  },  
  "legalForm": {  
    "type": "Property",  
    "value": "Research Center",  
    "observedAt": "2026-06-16T08:04:28.000Z"  
  },  
  "role": {  
    "type": "Property",  
    "value": "SRM Supplier - Marine Biomass",  
    "observedAt": "2026-06-16T08:04:28.000Z"  
  },  
  "city": {  
    "type": "Property",  
    "value": "Cesenatico",  
    "observedAt": "2026-06-16T08:04:28.000Z"  
  },  
  "tier": {  
    "type": "Property",  
    "value": "Tier 1",  
    "observedAt": "2026-06-16T08:04:28.000Z"  
  },  
  "country": {  
    "type": "Property",  
    "value": "Italy",  
    "observedAt": "2026-06-16T08:04:28.000Z"  
  }  
}  
```  
</details><!-- /80-Examples -->  
