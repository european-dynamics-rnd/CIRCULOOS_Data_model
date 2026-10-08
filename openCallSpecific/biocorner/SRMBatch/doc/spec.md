<!-- 10-Header -->  
Entity: SRMBatch  
================<!-- /10-Header -->  
<!-- 15-License -->  
[Open License](https://raw.githubusercontent.com/european-dynamics-rnd/CIRCULOOS_Data_model/refs/heads/main/LICENSE)  
<!-- /15-License -->  
<!-- 20-Description -->  
Global description: **CIRCULOOS data model for a delivered batch of a secondary raw material used in Biocorner bio-based mortar production, covering its origin, supplier, reception date and the measured quantity and quality parameters of the delivery.**  
version: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## List of properties  

<sup><sub>[*] If there is not a type in an attribute is because it could have several types or different formats/patterns</sub></sup>  
- `arrivalDate[*]`: Date when the material batch was received at the manufacturing or research facility. Recorded in ISO 8601 format (YYYY-MM-DD).  - `batchCode[*]`: Internal batch tracking code assigned upon material reception. Follows a structured convention for unique identification across the supply chain.  - `country[*]`: The country where the material was sourced.  - `density[*]`: Expected unitCode: KMQ. Measured bulk density of this specific batch. May differ from the reference SRM density due to natural variability in biological materials.  - `derivedFromSRM[*]`: Relationship to the parent SRM entity, identifying which type of secondary raw material this batch contains.  - `description[*]`: Free-text description including collection or harvest details, quality observations, and any deviations from expected material characteristics.  - `harvestSeason[*]`: Season and year when the raw material was harvested or collected. Relevant for bio-based materials where properties vary with seasonal conditions.  - `id[string]`: Unique entity identifier, with the format urn:ngsi-ld:SRMBatch:<id>.  - `moistureContent[*]`: Expected unitCode: P1. Measured moisture content of the batch at reception, as percentage by weight. Critical quality parameter for bio-based materials.  - `region[*]`: Geographic region where the material was sourced. Used for regional supply chain analysis and transport distance calculation.  - `suppliedBy[*]`: Relationship to the Supplier entity that delivered this batch.  - `type[string]`: NGSI Entity type. It has to be SRMBatch  - `volume[*]`: Expected unitCode: MTQ. Total volume of the batch as delivered. Complementary to weight for density verification.  - `weight[*]`: Expected unitCode: KGM. Total weight of the batch as delivered. Primary quantity measure for material accounting.  - `weightKg[*]`: Unit: kilogram. Numeric weight value in kilograms without unit string. Used for automated aggregation and statistical calculations in the platform dashboard.  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Required properties  
- `arrivalDate`  - `batchCode`  - `derivedFromSRM`  - `id`  - `suppliedBy`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Data Model description of properties  
Sorted alphabetically (click for details)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
SRMBatch:    
  description: CIRCULOOS data model for a delivered batch of a secondary raw material used in Biocorner bio-based mortar production, covering its origin, supplier, reception date and the measured quantity and quality parameters of the delivery.    
  properties:    
    arrivalDate:    
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
      description: Date when the material batch was received at the manufacturing or research facility. Recorded in ISO 8601 format (YYYY-MM-DD).    
      x-ngsi:    
        type: Property    
    batchCode:    
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
      description: Internal batch tracking code assigned upon material reception. Follows a structured convention for unique identification across the supply chain.    
      x-ngsi:    
        type: Property    
    country:    
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
      description: The country where the material was sourced.    
      x-ngsi:    
        type: Property    
    density:    
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
      description: 'Expected unitCode: KMQ. Measured bulk density of this specific batch. May differ from the reference SRM density due to natural variability in biological materials.'    
      x-ngsi:    
        type: Property    
    derivedFromSRM:    
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
      description: Relationship to the parent SRM entity, identifying which type of secondary raw material this batch contains.    
      x-ngsi:    
        type: Relationship    
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
      description: Free-text description including collection or harvest details, quality observations, and any deviations from expected material characteristics.    
      x-ngsi:    
        type: Property    
    harvestSeason:    
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
      description: Season and year when the raw material was harvested or collected. Relevant for bio-based materials where properties vary with seasonal conditions.    
      x-ngsi:    
        type: Property    
    id:    
      description: Unique entity identifier, with the format urn:ngsi-ld:SRMBatch:<id>.    
      type: string    
      x-ngsi:    
        type: Property    
    moistureContent:    
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
      description: 'Expected unitCode: P1. Measured moisture content of the batch at reception, as percentage by weight. Critical quality parameter for bio-based materials.'    
      x-ngsi:    
        type: Property    
    region:    
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
      description: Geographic region where the material was sourced. Used for regional supply chain analysis and transport distance calculation.    
      x-ngsi:    
        type: Property    
    suppliedBy:    
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
      description: Relationship to the Supplier entity that delivered this batch.    
      x-ngsi:    
        type: Relationship    
    type:    
      description: NGSI Entity type. It has to be SRMBatch    
      enum:    
        - SRMBatch    
      type: string    
      x-ngsi:    
        type: Property    
    volume:    
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
      description: 'Expected unitCode: MTQ. Total volume of the batch as delivered. Complementary to weight for density verification.'    
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
              description: UN/CEFACT code of the unit of measurement of the value.    
              type: string    
            value:    
              description: Exact measured value, when a single figure is known.    
              type: number    
          required:    
            - type    
            - unitCode    
          type: object    
      description: 'Expected unitCode: KGM. Total weight of the batch as delivered. Primary quantity measure for material accounting.'    
      x-ngsi:    
        type: Property    
    weightKg:    
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
      description: 'Unit: kilogram. Numeric weight value in kilograms without unit string. Used for automated aggregation and statistical calculations in the platform dashboard.'    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - batchCode    
    - derivedFromSRM    
    - suppliedBy    
    - arrivalDate    
  type: object    
  x-derived-from: ''    
  x-disclaimer: Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program    
  x-license-url: https://github.com/smart-data-models/circuloos_data_model/blob/master/SRMBatch/LICENSE.md    
  x-model-schema: https://raw.githubusercontent.com/european-dynamics-rnd/CIRCULOOS_Data_model/main/openCallSpecific/biocorner/SRMBatch/schema.json    
  x-model-tags: biocorner    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Example payloads    
Not available the example of a SRMBatch in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
#### SRMBatch NGSI-LD normalized Example    
Here is an example of a SRMBatch in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "@context": [  
    "http://circuloos-ld-context/circuloos-context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context-v1.8.jsonld"  
  ],  
  "id": "urn:ngsi-ld:SRMBatch:RH-CONF01-2025",  
  "type": "SRMBatch",  
  "batchCode": {  
    "type": "Property",  
    "value": "RH-CONF01-2025",  
    "observedAt": "2026-06-16T08:05:27.000Z"  
  },  
  "derivedFromSRM": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:SRM:RiceHusk",  
    "observedAt": "2026-06-16T08:05:27.000Z"  
  },  
  "density": {  
    "type": "Property",  
    "value": 115,  
    "unitCode": "KMQ",  
    "observedAt": "2026-06-16T08:05:27.000Z"  
  },  
  "region": {  
    "type": "Property",  
    "value": "Emilia-Romagna",  
    "observedAt": "2026-06-16T08:05:27.000Z"  
  },  
  "harvestSeason": {  
    "type": "Property",  
    "value": "Autumn 2025",  
    "observedAt": "2026-06-16T08:05:27.000Z"  
  },  
  "suppliedBy": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Supplier:Confidential01-Rice",  
    "observedAt": "2026-06-16T08:05:27.000Z"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Autumn 2025 harvest, rice husk",  
    "observedAt": "2026-06-16T08:05:27.000Z"  
  },  
  "arrivalDate": {  
    "type": "Property",  
    "value": "2024-11-01",  
    "observedAt": "2026-06-16T08:05:27.000Z"  
  },  
  "country": {  
    "type": "Property",  
    "value": "Italy",  
    "observedAt": "2026-06-16T08:05:27.000Z"  
  }  
}  
```  
</details><!-- /80-Examples -->  
