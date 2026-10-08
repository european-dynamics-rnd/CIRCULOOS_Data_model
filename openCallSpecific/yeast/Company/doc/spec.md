<!-- 10-Header -->  
Entity: Company  
===============<!-- /10-Header -->  
<!-- 15-License -->  
[Open License](https://raw.githubusercontent.com/european-dynamics-rnd/CIRCULOOS_Data_model/refs/heads/main/LICENSE)  
<!-- /15-License -->  
<!-- 20-Description -->  
Global description: **CIRCULOOS data model for a company taking part in the Yeast2Value value chain, covering its identity, postal address, industry sectors and the role it plays in valorising brewer's spent yeast.**  
version: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## List of properties  

<sup><sub>[*] If there is not a type in an attribute is because it could have several types or different formats/patterns</sub></sup>  
- `address[*]`: Postal address of the company as a structured object (street, locality, region, country, postal code), following the schema.org PostalAddress format.  - `category[*]`: List of sectors or industry categories the company operates in.  - `description[*]`: Short description of the company's activities and its role in valorising brewer's spent yeast.  - `id[string]`: Unique entity identifier, with the format urn:ngsi-ld:circuloos-yeast2value:Company:<companyId>.  - `name[*]`: Legal or trading name of the company.  - `type[string]`: NGSI Entity type. It has to be Company  - `valueChainRole[*]`: Role of the company in the Yeast2Value value chain (e.g. feedstock supplier, processor, customer/off-taker).  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Required properties  
- `id`  - `name`  - `type`  - `valueChainRole`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Data Model description of properties  
Sorted alphabetically (click for details)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
Company:    
  description: CIRCULOOS data model for a company taking part in the Yeast2Value value chain, covering its identity, postal address, industry sectors and the role it plays in valorising brewer's spent yeast.    
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
              additionalProperties: no    
              properties:    
                addressCountry:    
                  description: The country. Model:'https://schema.org/addressCountry'    
                  type: string    
                addressLocality:    
                  description: The locality in which the street address is. Model:'https://schema.org/addressLocality'    
                  type: string    
                addressRegion:    
                  description: The region in which the locality is. Model:'https://schema.org/addressRegion'    
                  type: string    
                postalCode:    
                  description: The postal code. Model:'https://schema.org/postalCode'    
                  type: string    
                streetAddress:    
                  description: The street address. Model:'https://schema.org/streetAddress'    
                  type: string    
              type: object    
          required:    
            - type    
            - value    
          type: object    
      description: Postal address of the company as a structured object (street, locality, region, country, postal code), following the schema.org PostalAddress format.    
      x-ngsi:    
        type: Property    
    category:    
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
              items:    
                type: string    
              minItems: 1    
              type: array    
          required:    
            - type    
            - value    
          type: object    
      description: List of sectors or industry categories the company operates in.    
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
      description: Short description of the company's activities and its role in valorising brewer's spent yeast.    
      x-ngsi:    
        type: Property    
    id:    
      description: Unique entity identifier, with the format urn:ngsi-ld:circuloos-yeast2value:Company:<companyId>.    
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
      description: Legal or trading name of the company.    
      x-ngsi:    
        type: Property    
    type:    
      description: NGSI Entity type. It has to be Company    
      enum:    
        - Company    
      type: string    
      x-ngsi:    
        type: Property    
    valueChainRole:    
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
      description: Role of the company in the Yeast2Value value chain (e.g. feedstock supplier, processor, customer/off-taker).    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - name    
    - valueChainRole    
  type: object    
  x-derived-from: ''    
  x-disclaimer: Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program    
  x-license-url: https://github.com/smart-data-models/circuloos_data_model/blob/master/Company/LICENSE.md    
  x-model-schema: https://raw.githubusercontent.com/european-dynamics-rnd/CIRCULOOS_Data_model/main/openCallSpecific/yeast/Company/schema.json    
  x-model-tags: yeast    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Example payloads    
Not available the example of a Company in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
#### Company NGSI-LD normalized Example    
Here is an example of a Company in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "@context": [  
    "http://circuloos-ld-context/circuloos-context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context-v1.8.jsonld"  
  ],  
  "id": "urn:ngsi-ld:circuloos-yeast2value:Company:proteindistillery",  
  "type": "Company",  
  "name": {  
    "type": "Property",  
    "value": "ProteinDistillery"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Converts brewer's spent yeast into food-grade protein, cell-wall fractions and low-molecular fractions."  
  },  
  "address": {  
    "type": "Property",  
    "value": {  
      "streetAddress": "Ostpreussenstrasse 2/2",  
      "addressLocality": "Ostfildern",  
      "addressRegion": "Baden-Wuerttemberg",  
      "addressCountry": "Germany",  
      "postalCode": "73760"  
    }  
  },  
  "category": {  
    "type": "Property",  
    "value": [  
      "Food ingredients",  
      "Biotechnology"  
    ]  
  },  
  "valueChainRole": {  
    "type": "Property",  
    "value": "Processor"  
  }  
}  
```  
</details><!-- /80-Examples -->  
