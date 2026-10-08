<!-- 10-Header -->  
Entity: Factory  
===============<!-- /10-Header -->  
<!-- 15-License -->  
[Open License](https://raw.githubusercontent.com/european-dynamics-rnd/CIRCULOOS_Data_model/refs/heads/main/LICENSE)  
<!-- /15-License -->  
<!-- 20-Description -->  
Global description: **CIRCULOOS data model for a physical facility involved in the ISLOPOL value chain, covering its name, principal activities, operating organisation, postal address and geographical position.**  
version: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## List of properties  

<sup><sub>[*] If there is not a type in an attribute is because it could have several types or different formats/patterns</sub></sup>  
- `address[*]`: Postal address of the facility, as a structured object containing fields such as street, postal code, locality, region and country.  - `factoryType[*]`: Type or category of the facility, or a description of its principal activities (e.g. sorting, recycling, production).  - `id[string]`: Unique entity identifier, with the format urn:ngsi-ld:Factory:<operator>:<facility>.  - `location[*]`: GeoProperty. Geographical position of the facility, represented as a GeoJSON Point. Coordinates are ordered as longitude followed by latitude.  - `name[*]`: Human-readable name of the facility, used to identify it in maps, forms and reports. Given in the source as https://schema.org/name.  - `operatedBy[*]`: Name of the organisation that operates the facility.  - `type[string]`: NGSI Entity type. It has to be Factory  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Required properties  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Data Model description of properties  
Sorted alphabetically (click for details)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
Factory:    
  description: CIRCULOOS data model for a physical facility involved in the ISLOPOL value chain, covering its name, principal activities, operating organisation, postal address and geographical position.    
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
      description: Postal address of the facility, as a structured object containing fields such as street, postal code, locality, region and country.    
      x-ngsi:    
        type: Property    
    factoryType:    
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
      description: Type or category of the facility, or a description of its principal activities (e.g. sorting, recycling, production).    
      x-ngsi:    
        type: Property    
    id:    
      description: Unique entity identifier, with the format urn:ngsi-ld:Factory:<operator>:<facility>.    
      type: string    
      x-ngsi:    
        type: Property    
    location:    
      allOf:    
        - additionalProperties: no    
          properties:    
            observedAt:    
              format: date-time    
              type: string    
            type:    
              enum:    
                - GeoProperty    
              type: string    
            value:    
              additionalProperties: no    
              properties:    
                coordinates:    
                  description: GeoJSON coordinates ordered as longitude followed by latitude.    
                  items:    
                    type: number    
                  maxItems: 2    
                  minItems: 2    
                  type: array    
                type:    
                  enum:    
                    - Point    
                  type: string    
              required:    
                - type    
                - coordinates    
              type: object    
          required:    
            - type    
            - value    
          type: object    
      description: GeoProperty. Geographical position of the facility, represented as a GeoJSON Point. Coordinates are ordered as longitude followed by latitude.    
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
      description: Human-readable name of the facility, used to identify it in maps, forms and reports. Given in the source as https://schema.org/name.    
      x-ngsi:    
        type: Property    
    operatedBy:    
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
      description: Name of the organisation that operates the facility.    
      x-ngsi:    
        type: Property    
    type:    
      description: NGSI Entity type. It has to be Factory    
      enum:    
        - Factory    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: https://context.dataspace-arditi.com/islopol/entities/Factory/v2/schema.json    
  x-disclaimer: Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program    
  x-license-url: https://github.com/smart-data-models/circuloos_data_model/blob/master/Factory/LICENSE.md    
  x-model-schema: https://raw.githubusercontent.com/european-dynamics-rnd/CIRCULOOS_Data_model/main/openCallSpecific/esp_islopol/Factory/schema.json    
  x-model-tags: esp_islopol    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Example payloads    
Not available the example of a Factory in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
#### Factory NGSI-LD normalized Example    
Here is an example of a Factory in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "@context": [  
    "http://circuloos-ld-context/circuloos-context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context-v1.8.jsonld"  
  ],  
  "id": "urn:ngsi-ld:Factory:ARM:ETRS",  
  "type": "Factory",  
  "name": {  
    "type": "Property",  
    "value": "ETRS - Estacao de Tratamento de Residuos Solidos da Meia Serra"  
  },  
  "factoryType": {  
    "type": "Property",  
    "value": "Tratamento, valorizacao e eliminacao de residuos solidos urbanos."  
  },  
  "operatedBy": {  
    "type": "Property",  
    "value": "ARM - Aguas e Residuos da Madeira S.A."  
  },  
  "address": {  
    "type": "Property",  
    "value": {  
      "streetAddress": "Meia Serra",  
      "postalCode": "9135-080",  
      "addressLocality": "Camacha",  
      "addressRegion": "Madeira",  
      "addressCountry": "Portugal"  
    }  
  },  
  "location": {  
    "type": "GeoProperty",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -16.869608,  
        32.703529  
      ]  
    }  
  }  
}  
```  
</details><!-- /80-Examples -->  
