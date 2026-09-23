<!-- 10-Header -->  
Entity: Product  
===============<!-- /10-Header -->  
<!-- 15-License -->  
[Open License](https://raw.githubusercontent.com/european-dynamics-rnd/CIRCULOOS_Data_model/refs/heads/main/LICENSE)  
<!-- /15-License -->  
<!-- 20-Description -->  
Global description: **CIRCULOOS data model for a recorded quantity of material, energy, a consumable or a finished product used or produced in the ISLOPOL value chain, covering its quantity and unit, its supplier and destination, its physical dimensions and the process event it belongs to.**  
version: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## List of properties  

<sup><sub>[*] If there is not a type in an attribute is because it could have several types or different formats/patterns</sub></sup>  
- `destination[*]`: Name or identifier of the intended recipient, facility or destination for the product or material. The schema allows a list of destinations.  - `id[string]`: Unique entity identifier, with the format urn:ngsi-ld:Product:<facility>:<material>:<date>.  - `length[*]`: Expected unitCode: CMT. Physical length of the product.  - `quantity[*]`: Amount of the product, material or resource represented by the record, expressed in the accompanying unitCode.  - `refProcessEvent[*]`: Identifier of the ProcessEvent associated with this Product record, linking its material or resource to the corresponding operation.  - `refProductModel[*]`: Identifier of the ProductModel defining the product's shared characteristics, such as its material, category and default unit of measurement.  - `supplier[*]`: Name or identifier of the organisation or source supplying the product or material. The schema allows a list of suppliers.  - `thickness[*]`: Expected unitCode: CMT. Physical thickness of the product.  - `type[string]`: NGSI Entity type. It has to be Product  - `unitCode[*]`: Unit of measurement for quantity.  - `width[*]`: Expected unitCode: CMT. Physical width of the product.  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Required properties  
- `id`  - `quantity`  - `type`  - `unitCode`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Data Model description of properties  
Sorted alphabetically (click for details)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
Product:    
  description: CIRCULOOS data model for a recorded quantity of material, energy, a consumable or a finished product used or produced in the ISLOPOL value chain, covering its quantity and unit, its supplier and destination, its physical dimensions and the process event it belongs to.    
  properties:    
    destination:    
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
      description: Name or identifier of the intended recipient, facility or destination for the product or material. The schema allows a list of destinations.    
      x-ngsi:    
        type: Property    
    id:    
      description: Unique entity identifier, with the format urn:ngsi-ld:Product:<facility>:<material>:<date>.    
      type: string    
      x-ngsi:    
        type: Property    
    length:    
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
      description: 'Expected unitCode: CMT. Physical length of the product.'    
      x-ngsi:    
        type: Property    
    quantity:    
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
            unitCode:    
              type: string    
            value:    
              type: number    
          required:    
            - type    
            - value    
          type: object    
      description: Amount of the product, material or resource represented by the record, expressed in the accompanying unitCode.    
      x-ngsi:    
        type: Property    
    refProcessEvent:    
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
      description: Identifier of the ProcessEvent associated with this Product record, linking its material or resource to the corresponding operation.    
      x-ngsi:    
        type: Relationship    
    refProductModel:    
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
      description: Identifier of the ProductModel defining the product's shared characteristics, such as its material, category and default unit of measurement.    
      x-ngsi:    
        type: Relationship    
    supplier:    
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
      description: Name or identifier of the organisation or source supplying the product or material. The schema allows a list of suppliers.    
      x-ngsi:    
        type: Property    
    thickness:    
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
      description: 'Expected unitCode: CMT. Physical thickness of the product.'    
      x-ngsi:    
        type: Property    
    type:    
      description: NGSI Entity type. It has to be Product    
      enum:    
        - Product    
      type: string    
      x-ngsi:    
        type: Property    
    unitCode:    
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
      description: Unit of measurement for quantity.    
      x-ngsi:    
        type: Property    
    width:    
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
      description: 'Expected unitCode: CMT. Physical width of the product.'    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - quantity    
    - unitCode    
  type: object    
  x-derived-from: https://context.dataspace-arditi.com/islopol/entities/Product/v2/schema.json    
  x-disclaimer: Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program    
  x-license-url: https://github.com/smart-data-models/circuloos_data_model/blob/master/Product/LICENSE.md    
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
Not available the example of a Product in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
#### Product NGSI-LD normalized Example    
Here is an example of a Product in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "@context": [  
    "http://circuloos-ld-context/circuloos-context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context-v1.8.jsonld"  
  ],  
  "id": "urn:ngsi-ld:Product:ARM:paper-cardboard-stream-waste:20260903",  
  "type": "Product",  
  "refProcessEvent": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:ProcessEvent:ARM:blue-waste-stream-processing:20260903"  
  },  
  "refProductModel": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:ProductModel:paper-cardboard-stream-waste"  
  },  
  "supplier": {  
    "type": "Property",  
    "value": "ARM Collection"  
  },  
  "destination": {  
    "type": "Property",  
    "value": "ARM ETZL/ET"  
  },  
  "quantity": {  
    "type": "Property",  
    "value": 6396.748215  
  },  
  "unitCode": {  
    "type": "Property",  
    "value": "kg"  
  },  
  "length": {  
    "type": "Property",  
    "value": 0,  
    "unitCode": "CMT"  
  },  
  "width": {  
    "type": "Property",  
    "value": 0,  
    "unitCode": "CMT"  
  },  
  "thickness": {  
    "type": "Property",  
    "value": 0,  
    "unitCode": "CMT"  
  }  
}  
```  
</details><!-- /80-Examples -->  
