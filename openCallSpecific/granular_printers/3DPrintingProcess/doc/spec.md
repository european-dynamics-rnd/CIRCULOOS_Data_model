<!-- 10-Header -->  
Entity: 3DPrintingProcess  
=========================<!-- /10-Header -->  
<!-- 15-License -->  
[Open License](https://raw.githubusercontent.com/european-dynamics-rnd/CIRCULOOS_Data_model/refs/heads/main/LICENSE)  
<!-- /15-License -->  
<!-- 20-Description -->  
Global description: **CIRCULOOS data model for a sensor reading taken on the cartesian granular 3D printer, covering slurry and adjuvant flow, extrusion head temperatures, motor intensity and speed, and circuit pressure during a print run.**  
version: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## List of properties  

<sup><sub>[*] If there is not a type in an attribute is because it could have several types or different formats/patterns</sub></sup>  
- `additiveFlowRate[*]`: Expected unitCode: LTR/HUR. Flow of adjuvant in the circuit.  - `additiveFlowRateSetPoint[*]`: Expected unitCode: P1. Theoretical percentage of adjuvant injected in the extrusion head.  - `id[string]`: Unique entity identifier, with the format urn:ngsi-ld:3DPrintingProcess:cartesian-printer:<printRun>:<readingId>.  - `motorIntensity[*]`: Expected unitCode: AMP. Electrical intensity of the motor of the extrusion head.  - `pressure[*]`: Expected unitCode: BAR. Pressure of the slurry in the circuit.  - `printingTime[*]`: Expected unitCode: MIN. Time to print a defined part.  - `rotationSpeed[*]`: Expected unitCode: RPM. Speed of the motor of the extrusion head.  - `slurryFlowRate[*]`: Expected unitCode: LTR/HUR. Flow of slurry in the circuit.  - `temperatureInput[*]`: Expected unitCode: CEL. Temperature of the slurry in the injection.  - `temperatureOutput[*]`: Expected unitCode: CEL. Temperature of the slurry in the output of the extrusion head.  - `type[string]`: NGSI Entity type. It has to be 3DPrintingProcess  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Required properties  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Data Model description of properties  
Sorted alphabetically (click for details)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
3DPrintingProcess:    
  description: CIRCULOOS data model for a sensor reading taken on the cartesian granular 3D printer, covering slurry and adjuvant flow, extrusion head temperatures, motor intensity and speed, and circuit pressure during a print run.    
  properties:    
    additiveFlowRate:    
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
      description: 'Expected unitCode: LTR/HUR. Flow of adjuvant in the circuit.'    
      x-ngsi:    
        type: Property    
    additiveFlowRateSetPoint:    
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
      description: 'Expected unitCode: P1. Theoretical percentage of adjuvant injected in the extrusion head.'    
      x-ngsi:    
        type: Property    
    id:    
      description: Unique entity identifier, with the format urn:ngsi-ld:3DPrintingProcess:cartesian-printer:<printRun>:<readingId>.    
      type: string    
      x-ngsi:    
        type: Property    
    motorIntensity:    
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
      description: 'Expected unitCode: AMP. Electrical intensity of the motor of the extrusion head.'    
      x-ngsi:    
        type: Property    
    pressure:    
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
      description: 'Expected unitCode: BAR. Pressure of the slurry in the circuit.'    
      x-ngsi:    
        type: Property    
    printingTime:    
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
      description: 'Expected unitCode: MIN. Time to print a defined part.'    
      x-ngsi:    
        type: Property    
    rotationSpeed:    
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
      description: 'Expected unitCode: RPM. Speed of the motor of the extrusion head.'    
      x-ngsi:    
        type: Property    
    slurryFlowRate:    
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
      description: 'Expected unitCode: LTR/HUR. Flow of slurry in the circuit.'    
      x-ngsi:    
        type: Property    
    temperatureInput:    
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
      description: 'Expected unitCode: CEL. Temperature of the slurry in the injection.'    
      x-ngsi:    
        type: Property    
    temperatureOutput:    
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
      description: 'Expected unitCode: CEL. Temperature of the slurry in the output of the extrusion head.'    
      x-ngsi:    
        type: Property    
    type:    
      description: NGSI Entity type. It has to be 3DPrintingProcess    
      enum:    
        - 3DPrintingProcess    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: ''    
  x-disclaimer: Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program    
  x-license-url: https://github.com/smart-data-models/circuloos_data_model/blob/master/3DPrintingProcess/LICENSE.md    
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
Not available the example of a 3DPrintingProcess in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
#### 3DPrintingProcess NGSI-LD normalized Example    
Here is an example of a 3DPrintingProcess in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "@context": [  
    "http://circuloos-ld-context/circuloos-context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context-v1.8.jsonld"  
  ],  
  "id": "urn:ngsi-ld:3DPrintingProcess:cartesian-printer:print-2026-02-18-001:data-1",  
  "type": "3DPrintingProcess",  
  "temperatureInput": {  
    "type": "Property",  
    "value": 17.556424,  
    "unitCode": "CEL"  
  },  
  "temperatureOutput": {  
    "type": "Property",  
    "value": 17.158565,  
    "unitCode": "CEL"  
  },  
  "additiveFlowRateSetPoint": {  
    "type": "Property",  
    "value": 0.075,  
    "unitCode": "P1"  
  },  
  "additiveFlowRate": {  
    "type": "Property",  
    "value": 0.006944,  
    "unitCode": "LTR/HUR"  
  },  
  "slurryFlowRate": {  
    "type": "Property",  
    "value": 3.0,  
    "unitCode": "LTR/HUR"  
  },  
  "motorIntensity": {  
    "type": "Property",  
    "value": 0.011574,  
    "unitCode": "AMP"  
  },  
  "rotationSpeed": {  
    "type": "Property",  
    "value": 100.0,  
    "unitCode": "RPM"  
  },  
  "pressure": {  
    "type": "Property",  
    "value": 5.753038,  
    "unitCode": "BAR"  
  },  
  "printingTime": {  
    "type": "Property",  
    "value": 0.016667,  
    "unitCode": "MIN"  
  }  
}  
```  
</details><!-- /80-Examples -->  
