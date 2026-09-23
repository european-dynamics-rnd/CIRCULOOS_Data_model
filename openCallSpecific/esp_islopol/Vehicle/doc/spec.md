<!-- 10-Header -->  
Entity: Vehicle  
===============<!-- /10-Header -->  
<!-- 15-License -->  
[Open License](https://raw.githubusercontent.com/european-dynamics-rnd/CIRCULOOS_Data_model/refs/heads/main/LICENSE)  
<!-- /15-License -->  
<!-- 20-Description -->  
Global description: **CIRCULOOS data model for an individual vehicle used in material collection or EPS transport in the ISLOPOL value chain, covering its registration plate, first registration date, configuration, fuel type and the vehicle model it belongs to.**  
version: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## List of properties  

<sup><sub>[*] If there is not a type in an attribute is because it could have several types or different formats/patterns</sub></sup>  
- `dateVehicleFirstRegistered[*]`: Date when the vehicle was first registered, normally expressed in ISO 8601 date format (YYYY-MM-DD). Given in the source as https://schema.org/dateVehicleFirstRegistered.  - `description[*]`: Free-text description of the vehicle.  - `fuelType[*]`: Fuel or energy type used by the individual vehicle. Given in the source as https://schema.org/fuelType.  - `id[string]`: Unique entity identifier, with the format urn:ngsi-ld:Vehicle:<operator>:<plate>.  - `name[*]`: Human-readable label for the individual vehicle. Given in the source as https://schema.org/name.  - `refVehicleModel[*]`: Identifier of the VehicleModel entity describing the shared technical characteristics of this vehicle's make and model. Given in the source as https://smartdatamodels.org/refVehicleModel.  - `type[string]`: NGSI Entity type. It has to be Vehicle  - `vehicleConfiguration[*]`: Text describing the vehicle's configuration or carrying arrangement. Given in the source as https://schema.org/vehicleConfiguration.  - `vehiclePlateIdentifier[*]`: Official registration plate identifying the individual vehicle. Given in the source as https://smartdatamodels.org/vehiclePlateIdentifier.  <!-- /30-PropertiesList -->  
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
Vehicle:    
  description: CIRCULOOS data model for an individual vehicle used in material collection or EPS transport in the ISLOPOL value chain, covering its registration plate, first registration date, configuration, fuel type and the vehicle model it belongs to.    
  properties:    
    dateVehicleFirstRegistered:    
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
      description: Date when the vehicle was first registered, normally expressed in ISO 8601 date format (YYYY-MM-DD). Given in the source as https://schema.org/dateVehicleFirstRegistered.    
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
      description: Free-text description of the vehicle.    
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
      description: Fuel or energy type used by the individual vehicle. Given in the source as https://schema.org/fuelType.    
      x-ngsi:    
        type: Property    
    id:    
      description: Unique entity identifier, with the format urn:ngsi-ld:Vehicle:<operator>:<plate>.    
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
      description: Human-readable label for the individual vehicle. Given in the source as https://schema.org/name.    
      x-ngsi:    
        type: Property    
    refVehicleModel:    
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
      description: Identifier of the VehicleModel entity describing the shared technical characteristics of this vehicle's make and model. Given in the source as https://smartdatamodels.org/refVehicleModel.    
      x-ngsi:    
        type: Relationship    
    type:    
      description: NGSI Entity type. It has to be Vehicle    
      enum:    
        - Vehicle    
      type: string    
      x-ngsi:    
        type: Property    
    vehicleConfiguration:    
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
      description: Text describing the vehicle's configuration or carrying arrangement. Given in the source as https://schema.org/vehicleConfiguration.    
      x-ngsi:    
        type: Property    
    vehiclePlateIdentifier:    
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
      description: Official registration plate identifying the individual vehicle. Given in the source as https://smartdatamodels.org/vehiclePlateIdentifier.    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - name    
  type: object    
  x-derived-from: https://context.dataspace-arditi.com/islopol/entities/Vehicle/v2/schema.json    
  x-disclaimer: Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program    
  x-license-url: https://github.com/smart-data-models/circuloos_data_model/blob/master/Vehicle/LICENSE.md    
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
Not available the example of a Vehicle in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
#### Vehicle NGSI-LD normalized Example    
Here is an example of a Vehicle in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "@context": [  
    "http://circuloos-ld-context/circuloos-context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context-v1.8.jsonld"  
  ],  
  "id": "urn:ngsi-ld:Vehicle:ARM:13-57-OR",  
  "type": "Vehicle",  
  "name": {  
    "type": "Property",  
    "value": "13-57-OR"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Mitsubishi Fuso Canter FE649C6SL-R; gross weight 6300 kg."  
  },  
  "vehiclePlateIdentifier": {  
    "type": "Property",  
    "value": "13-57-OR"  
  },  
  "dateVehicleFirstRegistered": {  
    "type": "Property",  
    "value": "1999-12-01"  
  },  
  "vehicleConfiguration": {  
    "type": "Property",  
    "value": "5 m3"  
  },  
  "refVehicleModel": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:VehicleModel:mitsubishi_fuso-canter-fe649c6sl-r"  
  },  
  "fuelType": {  
    "type": "Property",  
    "value": "diesel"  
  }  
}  
```  
</details><!-- /80-Examples -->  
