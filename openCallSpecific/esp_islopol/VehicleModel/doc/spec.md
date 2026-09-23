<!-- 10-Header -->  
Entity: VehicleModel  
====================<!-- /10-Header -->  
<!-- 15-License -->  
[Open License](https://raw.githubusercontent.com/european-dynamics-rnd/CIRCULOOS_Data_model/refs/heads/main/LICENSE)  
<!-- /15-License -->  
<!-- 20-Description -->  
Global description: **CIRCULOOS data model for a vehicle model in the ISLOPOL value chain, grouping the technical characteristics shared by vehicles of that model, including brand, fuel type, cargo volume and weight.**  
version: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## List of properties  

<sup><sub>[*] If there is not a type in an attribute is because it could have several types or different formats/patterns</sub></sup>  
- `brandName[*]`: Brand or marque of the vehicle model.  - `cargoVolume[*]`: Expected unitCode: LTR. Cargo volume specified for the vehicle model.  - `fuelType[*]`: Fuel or energy type used by vehicles of this model. Given in the source as https://schema.org/fuelType.  - `id[string]`:   . Model: [Unique entity identifier, with the format urn:ngsi-ld:Vehicle<brand>_<model>.](Unique entity identifier, with the format urn:ngsi-ld:Vehicle<brand>_<model>.)- `modelName[*]`: Manufacturer's model designation.  - `name[*]`: Human-readable name of the vehicle model, typically combining the brand and model designation. Given in the source as https://schema.org/name.  - `type[string]`: NGSI Entity type. It has to be VehicleModel  - `weight[*]`: Expected unitCode: KGM. Vehicle weight recorded for the model. Given in the source as https://schema.org/weight.  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Required properties  
- `id`  - `name`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Data Model description of properties  
Sorted alphabetically (click for details)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
VehicleModel:    
  description: CIRCULOOS data model for a vehicle model in the ISLOPOL value chain, grouping the technical characteristics shared by vehicles of that model, including brand, fuel type, cargo volume and weight.    
  properties:    
    brandName:    
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
      description: Brand or marque of the vehicle model.    
      x-ngsi:    
        type: Property    
    cargoVolume:    
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
      description: 'Expected unitCode: LTR. Cargo volume specified for the vehicle model.'    
      x-ngsi:    
        type: Property    
    fuelType:    
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
      description: Fuel or energy type used by vehicles of this model. Given in the source as https://schema.org/fuelType.    
      x-ngsi:    
        type: Property    
    id:    
      description: ''    
      type: string    
      x-ngsi:    
        model: Unique entity identifier, with the format urn:ngsi-ld:Vehicle<brand>_<model>.    
        type: Property    
    modelName:    
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
      description: Manufacturer's model designation.    
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
      description: Human-readable name of the vehicle model, typically combining the brand and model designation. Given in the source as https://schema.org/name.    
      x-ngsi:    
        type: Property    
    type:    
      description: NGSI Entity type. It has to be VehicleModel    
      enum:    
        - VehicleModel    
      type: string    
      x-ngsi:    
        type: Property    
    weight:    
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
      description: 'Expected unitCode: KGM. Vehicle weight recorded for the model. Given in the source as https://schema.org/weight.'    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - name    
  type: object    
  x-derived-from: https://context.dataspace-arditi.com/islopol/entities/VehicleModel/v2/schema.json    
  x-disclaimer: Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program    
  x-license-url: https://github.com/smart-data-models/circuloos_data_model/blob/master/VehicleModel/LICENSE.md    
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
Not available the example of a VehicleModel in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
#### VehicleModel NGSI-LD normalized Example    
Here is an example of a VehicleModel in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "@context": [  
    "http://circuloos-ld-context/circuloos-context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context-v1.8.jsonld"  
  ],  
  "id": "urn:ngsi-ld:VehicleModel:daf_85-cf-380",  
  "type": "VehicleModel",  
  "name": {  
    "type": "Property",  
    "value": "DAF 85 CF 380"  
  },  
  "brandName": {  
    "type": "Property",  
    "value": "DAF"  
  },  
  "modelName": {  
    "type": "Property",  
    "value": "85 CF 380"  
  },  
  "fuelType": {  
    "type": "Property",  
    "value": "diesel"  
  },  
  "cargoVolume": {  
    "type": "Property",  
    "value": 12000,  
    "unitCode": "LTR"  
  },  
  "weight": {  
    "type": "Property",  
    "value": 26000,  
    "unitCode": "KGM"  
  }  
}  
```  
</details><!-- /80-Examples -->  
