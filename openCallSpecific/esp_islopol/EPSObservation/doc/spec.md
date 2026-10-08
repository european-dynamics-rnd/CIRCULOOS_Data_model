<!-- 10-Header -->  
Entity: EPSObservation  
======================<!-- /10-Header -->  
<!-- 15-License -->  
[Open License](https://raw.githubusercontent.com/european-dynamics-rnd/CIRCULOOS_Data_model/refs/heads/main/LICENSE)  
<!-- /15-License -->  
<!-- 20-Description -->  
Global description: **CIRCULOOS data model for an automated observation of EPS material and its contamination in the ISLOPOL value chain, covering the contamination score and category, the confidence and model used to produce them, and the device, process event and batch the assessment relates to.**  
version: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## List of properties  

<sup><sub>[*] If there is not a type in an attribute is because it could have several types or different formats/patterns</sub></sup>  
- `confidence[*]`: Confidence score reported by the model for the observation, expressed from 0 to 1. It describes confidence in the prediction, not the amount of contamination. (Multiply by 100 to obtain the Confidence percentage.)  - `contaminationLevel[*]`: Contamination category assigned from the score using the thresholds recorded for the observation. The schema supports none, low, medium and high.  - `contaminationScore[*]`: Estimated contamination expressed as a fraction from 0 to 1, with higher values indicating more contamination. (Multiply by 100 to obtain the Contamination Score percentage.)  - `eventTime[*]`: Date and time when the EPS observation took place, expressed as an ISO 8601 timestamp.  - `id[string]`: Unique entity identifier, with the format urn:ngsi-ld:EPSObservation:<facility>:<stream>:<date>.  - `modelUsed[*]`: Name or identifier of the machine-learning model or inference method used to analyse the EPS observation.  - `modelVersion[*]`: Version or deployed model artefact used to produce the observation, allowing predictions to be traced to a specific model release.  - `refDevice[*]`: Identifier of the Device entity representing the equipment that generated the observation, such as the camera and inference device installed at ARM.  - `refEPSBatch[*]`: Identifier of the EPSBatch assessed by this observation, linking the model result to the tracked batch of material.  - `refProcessEvent[*]`: Identifier of the ProcessEvent during which the observation was generated, linking the assessment to the corresponding sorting operation.  - `thresholds[*]`: Configuration used to convert contamination scores into categories, including the lowMax, medMax and highMax upper limits. The object may also record the formula used to calculate the score.  - `type[string]`: NGSI Entity type. It has to be EPSObservation  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Required properties  
- `confidence`  - `contaminationScore`  - `eventTime`  - `id`  - `modelUsed`  - `modelVersion`  - `refDevice`  - `refProcessEvent`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Data Model description of properties  
Sorted alphabetically (click for details)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
EPSObservation:    
  description: CIRCULOOS data model for an automated observation of EPS material and its contamination in the ISLOPOL value chain, covering the contamination score and category, the confidence and model used to produce them, and the device, process event and batch the assessment relates to.    
  properties:    
    confidence:    
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
              maximum: 1    
              minimum: 0    
              type: number    
          required:    
            - type    
            - value    
          type: object    
      description: Confidence score reported by the model for the observation, expressed from 0 to 1. It describes confidence in the prediction, not the amount of contamination. (Multiply by 100 to obtain the Confidence percentage.)    
      x-ngsi:    
        type: Property    
    contaminationLevel:    
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
                - none    
                - low    
                - medium    
                - high    
              type: string    
          required:    
            - type    
            - value    
          type: object    
      description: Contamination category assigned from the score using the thresholds recorded for the observation. The schema supports none, low, medium and high.    
      x-ngsi:    
        type: Property    
    contaminationScore:    
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
              maximum: 1    
              minimum: 0    
              type: number    
          required:    
            - type    
            - value    
          type: object    
      description: Estimated contamination expressed as a fraction from 0 to 1, with higher values indicating more contamination. (Multiply by 100 to obtain the Contamination Score percentage.)    
      x-ngsi:    
        type: Property    
    eventTime:    
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
      description: Date and time when the EPS observation took place, expressed as an ISO 8601 timestamp.    
      x-ngsi:    
        type: Property    
    id:    
      description: Unique entity identifier, with the format urn:ngsi-ld:EPSObservation:<facility>:<stream>:<date>.    
      type: string    
      x-ngsi:    
        type: Property    
    modelUsed:    
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
      description: Name or identifier of the machine-learning model or inference method used to analyse the EPS observation.    
      x-ngsi:    
        type: Property    
    modelVersion:    
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
      description: Version or deployed model artefact used to produce the observation, allowing predictions to be traced to a specific model release.    
      x-ngsi:    
        type: Property    
    refDevice:    
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
      description: Identifier of the Device entity representing the equipment that generated the observation, such as the camera and inference device installed at ARM.    
      x-ngsi:    
        type: Relationship    
    refEPSBatch:    
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
      description: Identifier of the EPSBatch assessed by this observation, linking the model result to the tracked batch of material.    
      x-ngsi:    
        type: Relationship    
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
      description: Identifier of the ProcessEvent during which the observation was generated, linking the assessment to the corresponding sorting operation.    
      x-ngsi:    
        type: Relationship    
    thresholds:    
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
              additionalProperties: no    
              properties:    
                contaminationScoreFormula:    
                  description: Formula used to calculate the contamination score.    
                  type: string    
                highMax:    
                  description: Upper limit of the high contamination category.    
                  maximum: 1    
                  minimum: 0    
                  type: number    
                lowMax:    
                  description: Upper limit of the low contamination category.    
                  maximum: 1    
                  minimum: 0    
                  type: number    
                medMax:    
                  description: Upper limit of the medium contamination category.    
                  maximum: 1    
                  minimum: 0    
                  type: number    
              required:    
                - lowMax    
                - medMax    
                - highMax    
              type: object    
          required:    
            - type    
            - value    
          type: object    
      description: Configuration used to convert contamination scores into categories, including the lowMax, medMax and highMax upper limits. The object may also record the formula used to calculate the score.    
      x-ngsi:    
        type: Property    
    type:    
      description: NGSI Entity type. It has to be EPSObservation    
      enum:    
        - EPSObservation    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - eventTime    
    - contaminationScore    
    - confidence    
    - modelUsed    
    - modelVersion    
    - refDevice    
    - refProcessEvent    
  type: object    
  x-derived-from: https://context.dataspace-arditi.com/islopol/entities/EPSObservation/v2/schema.json    
  x-disclaimer: Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program    
  x-license-url: https://github.com/smart-data-models/circuloos_data_model/blob/master/EPSObservation/LICENSE.md    
  x-model-schema: https://raw.githubusercontent.com/european-dynamics-rnd/CIRCULOOS_Data_model/main/openCallSpecific/esp_islopol/EPSObservation/schema.json    
  x-model-tags: esp_islopol    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Example payloads    
Not available the example of a EPSObservation in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
#### EPSObservation NGSI-LD normalized Example    
Here is an example of a EPSObservation in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "@context": [  
    "http://circuloos-ld-context/circuloos-context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context-v1.8.jsonld"  
  ],  
  "id": "urn:ngsi-ld:EPSObservation:ARM:reciclable-eps:20260903",  
  "type": "EPSObservation",  
  "eventTime": {  
    "type": "Property",  
    "value": "2026-09-03T20:44:12.000Z"  
  },  
  "contaminationScore": {  
    "type": "Property",  
    "value": 0.107308  
  },  
  "contaminationLevel": {  
    "type": "Property",  
    "value": "high"  
  },  
  "confidence": {  
    "type": "Property",  
    "value": 0.397136  
  },  
  "modelUsed": {  
    "type": "Property",  
    "value": "YOLO segmentation NCNN"  
  },  
  "modelVersion": {  
    "type": "Property",  
    "value": "best_ncnn_model"  
  },  
  "thresholds": {  
    "type": "Property",  
    "value": {  
      "lowMax": 0.03,  
      "medMax": 0.1,  
      "highMax": 1,  
      "contaminationScoreFormula": "contamination_pct / 100"  
    }  
  },  
  "refDevice": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Device:ARM:Mounted01"  
  },  
  "refProcessEvent": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:ProcessEvent:ARM:blue-waste-stream-processing:20260903"  
  },  
  "refEPSBatch": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:EPSBatch:ARM:20260903"  
  }  
}  
```  
</details><!-- /80-Examples -->  
