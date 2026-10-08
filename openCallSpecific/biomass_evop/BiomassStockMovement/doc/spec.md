<!-- 10-Header -->  
Entity: BiomassStockMovement  
============================<!-- /10-Header -->  
<!-- 15-License -->  
[Open License](https://raw.githubusercontent.com/european-dynamics-rnd/CIRCULOOS_Data_model/refs/heads/main/LICENSE)  
<!-- /15-License -->  
<!-- 20-Description -->  
Global description: **CIRCULOOS data model for a single stock movement of biomass in the EVOP value chain, recording the material, the kind of movement, the quantity moved and the batch or source record it relates to.**  
version: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## List of properties  

<sup><sub>[*] If there is not a type in an attribute is because it could have several types or different formats/patterns</sub></sup>  
- `description[*]`: Free-text description providing additional information about the stock movement, including the biomass type or test context.  - `id[string]`: Unique entity identifier, with the format urn:ngsi-ld:evop:biomass-stock-movement:<movementId>.  - `material[*]`: Identifies the biomass material involved in the stock movement, such as olive pits.  - `movementType[*]`: Indicates the type of stock movement recorded, such as receipt, consumption or transfer.  - `occurredAt[*]`: Date and time when the biomass stock movement occurred, recorded as a timestamp.  - `quantityKg[*]`: Expected unitCode: KGM. Quantity of biomass involved in the stock movement.  - `relatedEntityId[*]`: Identifier of the biomass batch or other EVOP entity associated with the stock movement.  - `sourceRef[*]`: Reference identifying the source or origin of the stock movement, such as an initial stock record or measurement source.  - `type[string]`: NGSI Entity type. It has to be BiomassStockMovement  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Required properties  
- `id`  - `material`  - `movementType`  - `occurredAt`  - `quantityKg`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Data Model description of properties  
Sorted alphabetically (click for details)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
BiomassStockMovement:    
  description: CIRCULOOS data model for a single stock movement of biomass in the EVOP value chain, recording the material, the kind of movement, the quantity moved and the batch or source record it relates to.    
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
      description: Free-text description providing additional information about the stock movement, including the biomass type or test context.    
      x-ngsi:    
        type: Property    
    id:    
      description: Unique entity identifier, with the format urn:ngsi-ld:evop:biomass-stock-movement:<movementId>.    
      type: string    
      x-ngsi:    
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
      description: Identifies the biomass material involved in the stock movement, such as olive pits.    
      x-ngsi:    
        type: Property    
    movementType:    
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
      description: Indicates the type of stock movement recorded, such as receipt, consumption or transfer.    
      x-ngsi:    
        type: Property    
    occurredAt:    
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
      description: Date and time when the biomass stock movement occurred, recorded as a timestamp.    
      x-ngsi:    
        type: Property    
    quantityKg:    
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
      description: 'Expected unitCode: KGM. Quantity of biomass involved in the stock movement.'    
      x-ngsi:    
        type: Property    
    relatedEntityId:    
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
      description: Identifier of the biomass batch or other EVOP entity associated with the stock movement.    
      x-ngsi:    
        type: Relationship    
    sourceRef:    
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
      description: Reference identifying the source or origin of the stock movement, such as an initial stock record or measurement source.    
      x-ngsi:    
        type: Property    
    type:    
      description: NGSI Entity type. It has to be BiomassStockMovement    
      enum:    
        - BiomassStockMovement    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - material    
    - movementType    
    - quantityKg    
    - occurredAt    
  type: object    
  x-derived-from: ''    
  x-disclaimer: Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program    
  x-license-url: https://github.com/smart-data-models/circuloos_data_model/blob/master/BiomassStockMovement/LICENSE.md    
  x-model-schema: https://raw.githubusercontent.com/european-dynamics-rnd/CIRCULOOS_Data_model/main/openCallSpecific/biomass_evop/BiomassStockMovement/schema.json    
  x-model-tags: biomass_evop    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Example payloads    
Not available the example of a BiomassStockMovement in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
#### BiomassStockMovement NGSI-LD normalized Example    
Here is an example of a BiomassStockMovement in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "@context": [  
    "http://circuloos-ld-context/circuloos-context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context-v1.8.jsonld"  
  ],  
  "id": "urn:ngsi-ld:evop:biomass-stock-movement:receipt-olive-pits-v6-hueso-certificado-10-humedad",  
  "type": "BiomassStockMovement",  
  "material": {  
    "type": "Property",  
    "value": "olive-pits"  
  },  
  "movementType": {  
    "type": "Property",  
    "value": "receipt"  
  },  
  "quantityKg": {  
    "type": "Property",  
    "value": 10,  
    "unitCode": "KGM"  
  },  
  "occurredAt": {  
    "type": "Property",  
    "value": "2026-05-03T22:00:00.000Z"  
  },  
  "sourceRef": {  
    "type": "Property",  
    "value": "initial-stock:olive-pits:V6-HUESO-CERTIFICADO-10-HUMEDAD"  
  },  
  "relatedEntityId": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:evop:biomass-batch:olive-pits-receipt:v6-hueso-certificado-10-humedad"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Entrada directa de hueso para prueba original v6: HUESO CERTIFICADO (10% HUMEDAD)"  
  }  
}  
```  
</details><!-- /80-Examples -->  
