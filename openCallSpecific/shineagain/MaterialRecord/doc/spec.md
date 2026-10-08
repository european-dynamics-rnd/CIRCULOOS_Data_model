<!-- 10-Header -->  
Entity: MaterialRecord  
======================<!-- /10-Header -->  
<!-- 15-License -->  
[Open License](https://raw.githubusercontent.com/european-dynamics-rnd/CIRCULOOS_Data_model/refs/heads/main/LICENSE)  
<!-- /15-License -->  
<!-- 20-Description -->  
Global description: **CIRCULOOS data model for a single record in the ShineAgain data log, describing either a processing step (e.g. Shredding, Sorting, Pressing, CNC milling) or a transport operation performed on a material in a recycling loop, including mass in/out, energy use, locations and the partner that performed the step.**  
version: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## List of properties  

<sup><sub>[*] If there is not a type in an attribute is because it could have several types or different formats/patterns</sub></sup>  
- `date[*]`: Date on which the process step or transport took place. Source field: Date.  - `dateCreated[*]`: Date at which the entity was created.  - `destination[*]`: Location where the material ends up after the step. Mainly used for transport records; usually empty for on-site processing steps. Source field: End_location.  - `distance[*]`: Expected unitCode: KMT. Distance travelled in kilometres. Only used for transport records; empty for processing steps. Source field: KM.  - `energyConsumption[*]`: Expected unitCode: KWH. Electricity used by the machine(s) during this process step, as measured with an energy meter. If multiple machines are used the value is the calculated total of the measured values. Empty if not measured. Source field: Energy_use_kWh.  - `id[string]`: Unique entity identifier, with the format urn:ngsi-ld:MaterialRecord:ShineAgain:<id>. The number follows the record numbering in the ShineAgain data log, so each process step or transport can be traced.  - `materialIn[*]`: Expected unitCode: KGM. Mass of material going into this step, in kilograms, as weighed before the step. Source field: Material_in_kg.  - `materialLoop[*]`: Expected unitCode: C62 (unit). Number of the material loop (recycling cycle) the record belongs to, so the same material can be followed through successive reuse cycles; 1 is the first loop. Source field: Material_Loop.  - `materialOut[*]`: Expected unitCode: KGM. Mass of material coming out of this step, in kilograms, as weighed afterwards. The difference with materialIn is the loss or waste of this step. Source field: Material_out_kg.  - `notes[*]`: Free-text remarks on the record, e.g. settings used, issues encountered etc. Source field: Notes.  - `origin[*]`: For transport records, location where the transport starts. Source field: Start_location.  - `partner[*]`: ShineAgain partner (or external supplier) that performed this step, e.g. Better_Future_Factory, The_New_Raw or Vacumetal. Source field: Partner.  - `processStep[*]`: Processing step this record describes, e.g. Shredding, Sorting, Pressing or CNC milling. Empty for transport records. Source field: Proces_step.  - `transportationMode[*]`: Vehicle used to move the material. Only used for transport records; empty for processing steps. Source field: Type_of_transport.  - `type[string]`: NGSI Entity type. It has to be MaterialRecord  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Required properties  
- `date`  - `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Data Model description of properties  
Sorted alphabetically (click for details)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
MaterialRecord:    
  description: CIRCULOOS data model for a single record in the ShineAgain data log, describing either a processing step (e.g. Shredding, Sorting, Pressing, CNC milling) or a transport operation performed on a material in a recycling loop, including mass in/out, energy use, locations and the partner that performed the step.    
  properties:    
    date:    
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
      description: 'Date on which the process step or transport took place. Source field: Date.'    
      x-ngsi:    
        type: Property    
    dateCreated:    
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
      description: Date at which the entity was created.    
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
      description: 'Location where the material ends up after the step. Mainly used for transport records; usually empty for on-site processing steps. Source field: End_location.'    
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
              description: UN/CEFACT code of the unit of measurement of the value.    
              type: string    
            value:    
              description: Exact measured value, when a single figure is known.    
              type: number    
          required:    
            - type    
            - unitCode    
          type: object    
      description: 'Expected unitCode: KMT. Distance travelled in kilometres. Only used for transport records; empty for processing steps. Source field: KM.'    
      x-ngsi:    
        type: Property    
    energyConsumption:    
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
      description: 'Expected unitCode: KWH. Electricity used by the machine(s) during this process step, as measured with an energy meter. If multiple machines are used the value is the calculated total of the measured values. Empty if not measured. Source field: Energy_use_kWh.'    
      x-ngsi:    
        type: Property    
    id:    
      description: Unique entity identifier, with the format urn:ngsi-ld:MaterialRecord:ShineAgain:<id>. The number follows the record numbering in the ShineAgain data log, so each process step or transport can be traced.    
      type: string    
      x-ngsi:    
        type: Property    
    materialIn:    
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
      description: 'Expected unitCode: KGM. Mass of material going into this step, in kilograms, as weighed before the step. Source field: Material_in_kg.'    
      x-ngsi:    
        type: Property    
    materialLoop:    
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
      description: 'Expected unitCode: C62 (unit). Number of the material loop (recycling cycle) the record belongs to, so the same material can be followed through successive reuse cycles; 1 is the first loop. Source field: Material_Loop.'    
      x-ngsi:    
        type: Property    
    materialOut:    
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
      description: 'Expected unitCode: KGM. Mass of material coming out of this step, in kilograms, as weighed afterwards. The difference with materialIn is the loss or waste of this step. Source field: Material_out_kg.'    
      x-ngsi:    
        type: Property    
    notes:    
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
      description: 'Free-text remarks on the record, e.g. settings used, issues encountered etc. Source field: Notes.'    
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
      description: 'For transport records, location where the transport starts. Source field: Start_location.'    
      x-ngsi:    
        type: Property    
    partner:    
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
      description: 'ShineAgain partner (or external supplier) that performed this step, e.g. Better_Future_Factory, The_New_Raw or Vacumetal. Source field: Partner.'    
      x-ngsi:    
        type: Property    
    processStep:    
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
      description: 'Processing step this record describes, e.g. Shredding, Sorting, Pressing or CNC milling. Empty for transport records. Source field: Proces_step.'    
      x-ngsi:    
        type: Property    
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
      description: 'Vehicle used to move the material. Only used for transport records; empty for processing steps. Source field: Type_of_transport.'    
      x-ngsi:    
        type: Property    
    type:    
      description: NGSI Entity type. It has to be MaterialRecord    
      enum:    
        - MaterialRecord    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - date    
  type: object    
  x-derived-from: ''    
  x-disclaimer: Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program    
  x-license-url: https://github.com/smart-data-models/circuloos_data_model/blob/master/MaterialRecord/LICENSE.md    
  x-model-schema: https://raw.githubusercontent.com/european-dynamics-rnd/CIRCULOOS_Data_model/main/openCallSpecific/shineagain/MaterialRecord/schema.json    
  x-model-tags: shineagain    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Example payloads    
Not available the example of a MaterialRecord in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
#### MaterialRecord NGSI-LD normalized Example    
Here is an example of a MaterialRecord in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "@context": [  
    "http://circuloos-ld-context/circuloos-context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context-v1.8.jsonld"  
  ],  
  "id": "urn:ngsi-ld:MaterialRecord:ShineAgain:029",  
  "type": "MaterialRecord",  
  "processStep": {  
    "type": "Property",  
    "value": "Shredding"  
  },  
  "date": {  
    "type": "Property",  
    "value": "2026-03-11"  
  },  
  "materialLoop": {  
    "type": "Property",  
    "value": 1,  
    "unitCode": "C62"  
  },  
  "materialIn": {  
    "type": "Property",  
    "value": 7.25,  
    "unitCode": "KGM"  
  },  
  "materialOut": {  
    "type": "Property",  
    "value": 7.1,  
    "unitCode": "KGM"  
  },  
  "energyConsumption": {  
    "type": "Property",  
    "value": 0.33,  
    "unitCode": "KWH"  
  },  
  "partner": {  
    "type": "Property",  
    "value": "Better_Future_Factory"  
  }  
}  
```  
</details><!-- /80-Examples -->  
