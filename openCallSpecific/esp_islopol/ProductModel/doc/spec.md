<!-- 10-Header -->  
Entity: ProductModel  
====================<!-- /10-Header -->  
<!-- 15-License -->  
[Open License](https://raw.githubusercontent.com/european-dynamics-rnd/CIRCULOOS_Data_model/refs/heads/main/LICENSE)  
<!-- /15-License -->  
<!-- 20-Description -->  
Global description: **CIRCULOOS data model for a product or material model that defines shared characteristics for individual Product records in the ISLOPOL value chain, covering its name, constituents, material, available categories and default unit of measurement.**  
version: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## List of properties  

<sup><sub>[*] If there is not a type in an attribute is because it could have several types or different formats/patterns</sub></sup>  
- `availableCategories[*]`: List of product categories or grades available for the model. Simple hierarchies are allowed, e.g. 'Waste > EPS'.  - `constituents[*]`: Materials or components making up the product model.  - `description[*]`: Human-readable description of the product or material represented by the model.  - `id[string]`:   . Model: [Unique entity identifier, with the format urn:ngsi-ld:Product<modelId>.](Unique entity identifier, with the format urn:ngsi-ld:Product<modelId>.)- `material[*]`: Main material or composition associated with the product model. Given in the source as https://schema.org/material.  - `name[*]`: Human-readable name of the product model, used to label products. Given in the source as https://schema.org/name.  - `quantityUnit[*]`: UN/CEFACT code of the default unit of measurement for products of this model, e.g. KGM (kilogram), KWH (kilowatt hour) or EA (each).  - `refLcaId[*]`: Reference identifier used for LCA traceability.  - `type[string]`: NGSI Entity type. It has to be ProductModel  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Required properties  
- `id`  - `material`  - `name`  - `quantityUnit`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Data Model description of properties  
Sorted alphabetically (click for details)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
ProductModel:    
  description: CIRCULOOS data model for a product or material model that defines shared characteristics for individual Product records in the ISLOPOL value chain, covering its name, constituents, material, available categories and default unit of measurement.    
  properties:    
    availableCategories:    
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
      description: List of product categories or grades available for the model. Simple hierarchies are allowed, e.g. 'Waste > EPS'.    
      x-ngsi:    
        type: Property    
    constituents:    
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
      description: Materials or components making up the product model.    
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
      description: Human-readable description of the product or material represented by the model.    
      x-ngsi:    
        type: Property    
    id:    
      description: ''    
      type: string    
      x-ngsi:    
        model: Unique entity identifier, with the format urn:ngsi-ld:Product<modelId>.    
        type: Property    
    material:    
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
      description: Main material or composition associated with the product model. Given in the source as https://schema.org/material.    
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
      description: Human-readable name of the product model, used to label products. Given in the source as https://schema.org/name.    
      x-ngsi:    
        type: Property    
    quantityUnit:    
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
      description: UN/CEFACT code of the default unit of measurement for products of this model, e.g. KGM (kilogram), KWH (kilowatt hour) or EA (each).    
      x-ngsi:    
        type: Property    
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
      description: Reference identifier used for LCA traceability.    
      x-ngsi:    
        type: Property    
    type:    
      description: NGSI Entity type. It has to be ProductModel    
      enum:    
        - ProductModel    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - name    
    - quantityUnit    
    - material    
  type: object    
  x-derived-from: https://context.dataspace-arditi.com/islopol/entities/ProductModel/v2/schema.json    
  x-disclaimer: Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program    
  x-license-url: https://github.com/smart-data-models/circuloos_data_model/blob/master/ProductModel/LICENSE.md    
  x-model-schema: https://raw.githubusercontent.com/european-dynamics-rnd/CIRCULOOS_Data_model/main/openCallSpecific/esp_islopol/ProductModel/schema.json    
  x-model-tags: esp_islopol    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Example payloads    
Not available the example of a ProductModel in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
#### ProductModel NGSI-LD normalized Example    
Here is an example of a ProductModel in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "@context": [  
    "http://circuloos-ld-context/circuloos-context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context-v1.8.jsonld"  
  ],  
  "id": "urn:ngsi-ld:ProductModel:EPSThermalBoards",  
  "type": "ProductModel",  
  "name": {  
    "type": "Property",  
    "value": "Placas termicas de EPS"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Placas termicas de EPS"  
  },  
  "constituents": {  
    "type": "Property",  
    "value": [  
      "EPS"  
    ]  
  },  
  "availableCategories": {  
    "type": "Property",  
    "value": [  
      "EPS150",  
      "EPS100",  
      "NEO80",  
      "EPS60"  
    ]  
  },  
  "material": {  
    "type": "Property",  
    "value": "EPS"  
  },  
  "quantityUnit": {  
    "type": "Property",  
    "value": "EA"  
  }  
}  
```  
</details><!-- /80-Examples -->  
