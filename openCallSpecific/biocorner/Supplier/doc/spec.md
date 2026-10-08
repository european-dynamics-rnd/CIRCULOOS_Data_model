<!-- 10-Header -->  
Entity: Supplier  
================<!-- /10-Header -->  
<!-- 15-License -->  
[Open License](https://raw.githubusercontent.com/european-dynamics-rnd/CIRCULOOS_Data_model/refs/heads/main/LICENSE)  
<!-- /15-License -->  
<!-- 20-Description -->  
Global description: **CIRCULOOS data model for a supplier facility or collection point delivering secondary raw materials to Biocorner mortar production, covering its location, contact details, transport mode and distance to the manufacturer.**  
version: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## List of properties  

<sup><sub>[*] If there is not a type in an attribute is because it could have several types or different formats/patterns</sub></sup>  
- `address[*]`: Postal address of the supplier facility as a structured object (street, locality, region, country, postal code), following the schema.org PostalAddress format. addressRegion holds the administrative region where the facility is located, a key parameter for regional circular economy indicators.  - `contactEmail[*]`: Email address of the primary contact person at the supplier facility. Used for supply chain communication and batch tracing inquiries.  - `contactPerson[*]`: Name of the designated contact person responsible for material supply coordination at this facility.  - `distanceToManufacturer[*]`: Expected unitCode: KMT. Road distance from the supplier facility to the manufacturer. Used for transport emission estimation and regional sourcing analysis.  - `id[string]`: Unique entity identifier, with the format urn:ngsi-ld:Supplier:<id>.  - `name[*]`: Name of the supplier facility or collection point. May differ from the parent organization name when multiple supply facilities exist.  - `operatedBy[*]`: Relationship to the Organization entity that operates this supplier facility.  - `suppliesSRM[*]`: SRM entity types supplied by this facility. Establishes which secondary raw materials originate from this point in the supply chain.  - `transportationMode[*]`: Primary transport method and vehicle type used for material delivery, including emission standard classification where applicable.  - `type[string]`: NGSI Entity type. It has to be Supplier  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Required properties  
- `id`  - `name`  - `operatedBy`  - `suppliesSRM`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Data Model description of properties  
Sorted alphabetically (click for details)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
Supplier:    
  description: CIRCULOOS data model for a supplier facility or collection point delivering secondary raw materials to Biocorner mortar production, covering its location, contact details, transport mode and distance to the manufacturer.    
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
      description: Postal address of the supplier facility as a structured object (street, locality, region, country, postal code), following the schema.org PostalAddress format. addressRegion holds the administrative region where the facility is located, a key parameter for regional circular economy indicators.    
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
      description: Email address of the primary contact person at the supplier facility. Used for supply chain communication and batch tracing inquiries.    
      x-ngsi:    
        type: Property    
    contactPerson:    
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
      description: Name of the designated contact person responsible for material supply coordination at this facility.    
      x-ngsi:    
        type: Property    
    distanceToManufacturer:    
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
      description: 'Expected unitCode: KMT. Road distance from the supplier facility to the manufacturer. Used for transport emission estimation and regional sourcing analysis.'    
      x-ngsi:    
        type: Property    
    id:    
      description: Unique entity identifier, with the format urn:ngsi-ld:Supplier:<id>.    
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
      description: Name of the supplier facility or collection point. May differ from the parent organization name when multiple supply facilities exist.    
      x-ngsi:    
        type: Property    
    operatedBy:    
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
      description: Relationship to the Organization entity that operates this supplier facility.    
      x-ngsi:    
        type: Relationship    
    suppliesSRM:    
      allOf:    
        - additionalProperties: no    
          properties:    
            object:    
              description: URNs of the referenced entities, each with the format urn:ngsi-ld:<type>:<id>.    
              items:    
                pattern: ^urn:ngsi-ld:[A-Za-z0-9_]+:.+$    
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
      description: SRM entity types supplied by this facility. Establishes which secondary raw materials originate from this point in the supply chain.    
      x-ngsi:    
        type: Relationship    
    transportationMode:    
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
      description: Primary transport method and vehicle type used for material delivery, including emission standard classification where applicable.    
      x-ngsi:    
        type: Property    
    type:    
      description: NGSI Entity type. It has to be Supplier    
      enum:    
        - Supplier    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - name    
    - operatedBy    
    - suppliesSRM    
  type: object    
  x-derived-from: ''    
  x-disclaimer: Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program    
  x-license-url: https://github.com/smart-data-models/circuloos_data_model/blob/master/Supplier/LICENSE.md    
  x-model-schema: https://raw.githubusercontent.com/european-dynamics-rnd/CIRCULOOS_Data_model/main/openCallSpecific/biocorner/Supplier/schema.json    
  x-model-tags: biocorner    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Example payloads    
Not available the example of a Supplier in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
#### Supplier NGSI-LD normalized Example    
Here is an example of a Supplier in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "@context": [  
    "http://circuloos-ld-context/circuloos-context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context-v1.8.jsonld"  
  ],  
  "id": "urn:ngsi-ld:Supplier:Confidential01-Rice",  
  "type": "Supplier",  
  "operatedBy": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Organization:LITOKOL",  
    "observedAt": "2026-06-16T08:04:49.000Z"  
  },  
  "address": {  
    "type": "Property",  
    "value": {  
      "addressRegion": "Emilia-Romagna",  
      "addressCountry": "Italy"  
    },  
    "observedAt": "2026-06-16T08:04:49.000Z"  
  },  
  "suppliesSRM": {  
    "type": "Relationship",  
    "object": [  
      "urn:ngsi-ld:SRM:RiceHusk",  
      "urn:ngsi-ld:SRM:RiceStraw"  
    ],  
    "observedAt": "2026-06-16T08:04:49.000Z"  
  },  
  "name": {  
    "type": "Property",  
    "value": "Confidential Supplier 01",  
    "observedAt": "2026-06-16T08:04:49.000Z"  
  },  
  "transportationMode": {  
    "type": "Property",  
    "value": "Road transport - Truck Euro 6",  
    "observedAt": "2026-06-16T08:04:49.000Z"  
  },  
  "distanceToManufacturer": {  
    "type": "Property",  
    "value": 50,  
    "unitCode": "KMT",  
    "observedAt": "2026-06-16T08:04:49.000Z"  
  }  
}  
```  
</details><!-- /80-Examples -->  
