<!-- 10-Header -->  
Entity: YeastProduct  
====================<!-- /10-Header -->  
<!-- 15-License -->  
[Open License](https://raw.githubusercontent.com/european-dynamics-rnd/CIRCULOOS_Data_model/refs/heads/main/LICENSE)  
<!-- /15-License -->  
<!-- 20-Description -->  
Global description: **CIRCULOOS data model for a product derived from brewer's spent yeast in the Yeast2Value value chain, covering the process stream it comes from, its commercial maturity and price range, and the customers, collaborations and market opportunities attached to it.**  
version: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## List of properties  

<sup><sub>[*] If there is not a type in an attribute is because it could have several types or different formats/patterns</sub></sup>  
- `description[*]`: Short description of the product, its composition and functional properties, and its target applications.  - `goToMarketStage[*]`: Current commercial maturity of the product, from development through validation to an MVP ready for commercialisation.  - `id[string]`: Unique entity identifier, with the format urn:ngsi-ld:circuloos-yeast2value:product:<productId>.  - `keyCollaborations[*]`: Research or industry partners involved in developing, testing or validating the product.  - `mainMarketOpportunities[*]`: Main market needs the product addresses, i.e. its value proposition for customers.  - `potentialCustomers[*]`: Companies identified as potential buyers or application partners for the product, with the intended application.  - `priceRange[*]`: Expected unitCode: EUR/KGM. Indicative selling price range of the product. Use minValue and maxValue for a range, or value for a single price.  - `processStream[*]`: Yeast fraction or process stream the product comes from (e.g. yeast protein, cell walls, low-molecular fractions, or blends).  - `productName[*]`: Commercial name of the product derived from brewer's spent yeast.  - `specifications[*]`: Technical specifications or datasheet information for the product (e.g. composition).  - `type[string]`: NGSI Entity type. It has to be YeastProduct  - `valueChain[*]`: Identifier of the CIRCULOOS value chain the record belongs to (here "yeast2value").  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Required properties  
- `id`  - `processStream`  - `productName`  - `type`  - `valueChain`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Data Model description of properties  
Sorted alphabetically (click for details)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
YeastProduct:    
  description: CIRCULOOS data model for a product derived from brewer's spent yeast in the Yeast2Value value chain, covering the process stream it comes from, its commercial maturity and price range, and the customers, collaborations and market opportunities attached to it.    
  properties:    
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
      description: Short description of the product, its composition and functional properties, and its target applications.    
      x-ngsi:    
        type: Property    
    goToMarketStage:    
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
      description: Current commercial maturity of the product, from development through validation to an MVP ready for commercialisation.    
      x-ngsi:    
        type: Property    
    id:    
      description: Unique entity identifier, with the format urn:ngsi-ld:circuloos-yeast2value:product:<productId>.    
      type: string    
      x-ngsi:    
        type: Property    
    keyCollaborations:    
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
      description: Research or industry partners involved in developing, testing or validating the product.    
      x-ngsi:    
        type: Property    
    mainMarketOpportunities:    
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
      description: Main market needs the product addresses, i.e. its value proposition for customers.    
      x-ngsi:    
        type: Property    
    potentialCustomers:    
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
      description: Companies identified as potential buyers or application partners for the product, with the intended application.    
      x-ngsi:    
        type: Property    
    priceRange:    
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
      description: 'Expected unitCode: EUR/KGM. Indicative selling price range of the product. Use minValue and maxValue for a range, or value for a single price.'    
      x-ngsi:    
        type: Property    
    processStream:    
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
      description: Yeast fraction or process stream the product comes from (e.g. yeast protein, cell walls, low-molecular fractions, or blends).    
      x-ngsi:    
        type: Property    
    productName:    
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
      description: Commercial name of the product derived from brewer's spent yeast.    
      x-ngsi:    
        type: Property    
    specifications:    
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
      description: Technical specifications or datasheet information for the product (e.g. composition).    
      x-ngsi:    
        type: Property    
    type:    
      description: NGSI Entity type. It has to be YeastProduct    
      enum:    
        - YeastProduct    
      type: string    
      x-ngsi:    
        type: Property    
    valueChain:    
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
      description: Identifier of the CIRCULOOS value chain the record belongs to (here "yeast2value").    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - productName    
    - processStream    
    - valueChain    
  type: object    
  x-derived-from: ''    
  x-disclaimer: Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program    
  x-license-url: https://github.com/smart-data-models/circuloos_data_model/blob/master/YeastProduct/LICENSE.md    
  x-model-schema: https://raw.githubusercontent.com/european-dynamics-rnd/CIRCULOOS_Data_model/main/openCallSpecific/yeast/YeastProduct/schema.json    
  x-model-tags: yeast    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Example payloads    
Not available the example of a YeastProduct in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
#### YeastProduct NGSI-LD normalized Example    
Here is an example of a YeastProduct in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "@context": [  
    "http://circuloos-ld-context/circuloos-context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context-v1.8.jsonld"  
  ],  
  "id": "urn:ngsi-ld:circuloos-yeast2value:product:prewmix",  
  "type": "YeastProduct",  
  "productName": {  
    "type": "Property",  
    "value": "PrewÂ®mix"  
  },  
  "processStream": {  
    "type": "Property",  
    "value": "Blends"  
  },  
  "goToMarketStage": {  
    "type": "Property",  
    "value": "MVPs in validation stage"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Whole solutions bringing texturizing systems and versatile handling for different applications such as vegan scarmbled eggs or cheese blends."  
  },  
  "priceRange": {  
    "type": "Property",  
    "minValue": 13.0,  
    "maxValue": 15.0,  
    "unitCode": "EUR/KGM"  
  },  
  "potentialCustomers": {  
    "type": "Property",  
    "value": [  
      "Pacifico Biolabs (meatballs using mycoprotein)",  
      "M Food Group (nuggets using mycoprotein)"  
    ]  
  },  
  "keyCollaborations": {  
    "type": "Property",  
    "value": [  
      "Naplasol (applications using mycoprotein"  
    ]  
  },  
  "mainMarketOpportunities": {  
    "type": "Property",  
    "value": "Provides a clean-label option for texturizing systems that is versatile in terms of applications, and flavour profiles."  
  },  
  "valueChain": {  
    "type": "Property",  
    "value": "yeast2value"  
  }  
}  
```  
</details><!-- /80-Examples -->  
