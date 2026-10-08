<!-- 10-Header -->  
Entity: RecyclingMaterialCollection  
===================================<!-- /10-Header -->  
<!-- 15-License -->  
[Open License](https://raw.githubusercontent.com/european-dynamics-rnd/CIRCULOOS_Data_model/refs/heads/main/LICENSE)  
<!-- /15-License -->  
<!-- 20-Description -->  
Global description: **CIRCULOOS data model for a material collection or reception movement in the ISLOPOL value chain, covering the client and transporter involved, the vehicle used, the waste code and stream, the origin and destination, and the mass received.**  
version: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## List of properties  

<sup><sub>[*] If there is not a type in an attribute is because it could have several types or different formats/patterns</sub></sup>  
- `client[*]`: Name of the client associated with the material movement.  - `clientType[*]`: Client classification code.  - `destination[*]`: Receiving site, treatment route or sorting destination recorded for the material movement.  - `distance[*]`: Expected unitCode: KMT. Distance travelled by the collection movement.  - `id[string]`: Unique entity identifier, with the format urn:ngsi-ld:RecyclingMaterialCollection:<facility>:<kind>:<timestamp>.  - `lerCode[*]`: European List of Waste code.  - `movementKind[*]`: Type of material movement or operation.  - `origin[*]`: Place, municipality or source site from which the collected material originated.  - `product[*]`: Material or waste description.  - `refFactoryDestination[*]`: ARM Factory the collection movement arrives at, when it arrives at an ARM facility.  - `refFactoryOrigin[*]`: ARM Factory the collection movement departs from, when it departs from an ARM facility.  - `refVehicle[*]`: Identifier of the Vehicle entity associated with the material movement.  - `timestampArrival[*]`: Date and time of the recorded arrival or reception of the material, expressed as an ISO 8601 timestamp.  - `timestampDeparture[*]`: Date and time when the material movement departed, expressed as an ISO 8601 timestamp.  - `transporter[*]`: Name of the organisation responsible for transporting the material in the recorded movement.  - `type[string]`: NGSI Entity type. It has to be RecyclingMaterialCollection  - `vehiclePlateIdentifier[*]`: Vehicle registration plate or other vehicle identifier recorded in the source document.  - `wasteStream[*]`: Classification of the collected material stream: Blue Stream, Yellow Stream, EPS Stream, Rejected EPS Stream, Paper/Cardboard Stream, Other.  - `weight[*]`: Expected unitCode: KGM. Mass of material recorded for the movement.  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Required properties  
- `id`  - `type`  - `weight`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Data Model description of properties  
Sorted alphabetically (click for details)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
RecyclingMaterialCollection:    
  description: CIRCULOOS data model for a material collection or reception movement in the ISLOPOL value chain, covering the client and transporter involved, the vehicle used, the waste code and stream, the origin and destination, and the mass received.    
  properties:    
    client:    
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
      description: Name of the client associated with the material movement.    
      x-ngsi:    
        type: Property    
    clientType:    
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
      description: Client classification code.    
      x-ngsi:    
        type: Property    
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
      description: Receiving site, treatment route or sorting destination recorded for the material movement.    
      x-ngsi:    
        type: Property    
    distance:    
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
      description: 'Expected unitCode: KMT. Distance travelled by the collection movement.'    
      x-ngsi:    
        type: Property    
    id:    
      description: Unique entity identifier, with the format urn:ngsi-ld:RecyclingMaterialCollection:<facility>:<kind>:<timestamp>.    
      type: string    
      x-ngsi:    
        type: Property    
    lerCode:    
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
      description: European List of Waste code.    
      x-ngsi:    
        type: Property    
    movementKind:    
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
      description: Type of material movement or operation.    
      x-ngsi:    
        type: Property    
    origin:    
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
      description: Place, municipality or source site from which the collected material originated.    
      x-ngsi:    
        type: Property    
    product:    
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
      description: Material or waste description.    
      x-ngsi:    
        type: Property    
    refFactoryDestination:    
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
      description: ARM Factory the collection movement arrives at, when it arrives at an ARM facility.    
      x-ngsi:    
        type: Relationship    
    refFactoryOrigin:    
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
      description: ARM Factory the collection movement departs from, when it departs from an ARM facility.    
      x-ngsi:    
        type: Relationship    
    refVehicle:    
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
      description: Identifier of the Vehicle entity associated with the material movement.    
      x-ngsi:    
        type: Relationship    
    timestampArrival:    
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
      description: Date and time of the recorded arrival or reception of the material, expressed as an ISO 8601 timestamp.    
      x-ngsi:    
        type: Property    
    timestampDeparture:    
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
      description: Date and time when the material movement departed, expressed as an ISO 8601 timestamp.    
      x-ngsi:    
        type: Property    
    transporter:    
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
      description: Name of the organisation responsible for transporting the material in the recorded movement.    
      x-ngsi:    
        type: Property    
    type:    
      description: NGSI Entity type. It has to be RecyclingMaterialCollection    
      enum:    
        - RecyclingMaterialCollection    
      type: string    
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
      description: Vehicle registration plate or other vehicle identifier recorded in the source document.    
      x-ngsi:    
        type: Property    
    wasteStream:    
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
              enum:    
                - Blue Stream    
                - Yellow Stream    
                - EPS Stream    
                - Rejected EPS Stream    
                - Paper/Cardboard Stream    
                - Other    
              type: string    
          required:    
            - type    
            - value    
          type: object    
      description: 'Classification of the collected material stream: Blue Stream, Yellow Stream, EPS Stream, Rejected EPS Stream, Paper/Cardboard Stream, Other.'    
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
      description: 'Expected unitCode: KGM. Mass of material recorded for the movement.'    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - weight    
  type: object    
  x-derived-from: https://context.dataspace-arditi.com/islopol/entities/RecyclingMaterialCollection/v2/schema.json    
  x-disclaimer: Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program    
  x-license-url: https://github.com/smart-data-models/circuloos_data_model/blob/master/RecyclingMaterialCollection/LICENSE.md    
  x-model-schema: https://raw.githubusercontent.com/european-dynamics-rnd/CIRCULOOS_Data_model/main/openCallSpecific/esp_islopol/RecyclingMaterialCollection/schema.json    
  x-model-tags: esp_islopol    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Example payloads    
Not available the example of a RecyclingMaterialCollection in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
#### RecyclingMaterialCollection NGSI-LD normalized Example    
Here is an example of a RecyclingMaterialCollection in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "@context": [  
    "http://circuloos-ld-context/circuloos-context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context-v1.8.jsonld"  
  ],  
  "id": "urn:ngsi-ld:RecyclingMaterialCollection:ARM:Import:20260827T102839Z",  
  "type": "RecyclingMaterialCollection",  
  "movementKind": {  
    "type": "Property",  
    "value": "D - Entrada"  
  },  
  "client": {  
    "type": "Property",  
    "value": "C.M. de Santa Cruz"  
  },  
  "clientType": {  
    "type": "Property",  
    "value": "AUT"  
  },  
  "transporter": {  
    "type": "Property",  
    "value": "C.M. de Santa Cruz"  
  },  
  "vehiclePlateIdentifier": {  
    "type": "Property",  
    "value": "BZ-21-JT"  
  },  
  "refVehicle": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Vehicle:external:BZ-21-JT"  
  },  
  "lerCode": {  
    "type": "Property",  
    "value": "LER150101"  
  },  
  "product": {  
    "type": "Property",  
    "value": "EMBALAGENS PAPEL/CARTAO"  
  },  
  "origin": {  
    "type": "Property",  
    "value": "Santa Cruz"  
  },  
  "destination": {  
    "type": "Property",  
    "value": "TPC - TRIAGEM PAPEL/CARTAO"  
  },  
  "timestampArrival": {  
    "type": "Property",  
    "value": "2026-08-27T10:28:39.000Z"  
  },  
  "weight": {  
    "type": "Property",  
    "value": 740,  
    "unitCode": "KGM"  
  },  
  "wasteStream": {  
    "type": "Property",  
    "value": "Paper/Cardboard Stream"  
  }  
}  
```  
</details><!-- /80-Examples -->  
