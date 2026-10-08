<!-- 10-Header -->  
Entity: SEMImage  
================<!-- /10-Header -->  
<!-- 15-License -->  
[Open License](https://raw.githubusercontent.com/european-dynamics-rnd/CIRCULOOS_Data_model/refs/heads/main/LICENSE)  
<!-- /15-License -->  
<!-- 20-Description -->  
Global description: **CIRCULOOS data model for a scanning electron microscope (SEM) image of a material sample in the SEARCLE value chain, covering the instrument that produced it, the machine settings used, and the link to the stored image file.**  
version: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## List of properties  

<sup><sub>[*] If there is not a type in an attribute is because it could have several types or different formats/patterns</sub></sup>  
- `acceleratingVoltage[*]`: Expected unitCode: KVT. Accelerating voltage of the electron beam, another machine setting of the acquisition.  - `equipment[*]`: Equipment that generated the data.  - `id[string]`: Unique entity identifier, with the format urn:ngsi-ld:circuloos_searcle:sem:<imageId>.  - `imageUrl[*]`: Internal link to the data if too big (requires authentication).  - `magnification[*]`: Machine settings (e.g. microscope magnification), recorded as reported by the instrument (e.g. "x250").  - `type[string]`: NGSI Entity type. It has to be SEMImage  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Required properties  
- `equipment`  - `id`  - `imageUrl`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Data Model description of properties  
Sorted alphabetically (click for details)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
SEMImage:    
  description: CIRCULOOS data model for a scanning electron microscope (SEM) image of a material sample in the SEARCLE value chain, covering the instrument that produced it, the machine settings used, and the link to the stored image file.    
  properties:    
    acceleratingVoltage:    
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
      description: 'Expected unitCode: KVT. Accelerating voltage of the electron beam, another machine setting of the acquisition.'    
      x-ngsi:    
        type: Property    
    equipment:    
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
      description: Equipment that generated the data.    
      x-ngsi:    
        type: Property    
    id:    
      description: Unique entity identifier, with the format urn:ngsi-ld:circuloos_searcle:sem:<imageId>.    
      type: string    
      x-ngsi:    
        type: Property    
    imageUrl:    
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
      description: Internal link to the data if too big (requires authentication).    
      x-ngsi:    
        type: Property    
    magnification:    
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
      description: Machine settings (e.g. microscope magnification), recorded as reported by the instrument (e.g. "x250").    
      x-ngsi:    
        type: Property    
    type:    
      description: NGSI Entity type. It has to be SEMImage    
      enum:    
        - SEMImage    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - equipment    
    - imageUrl    
  type: object    
  x-derived-from: ''    
  x-disclaimer: Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program    
  x-license-url: https://github.com/smart-data-models/circuloos_data_model/blob/master/SEMImage/LICENSE.md    
  x-model-schema: https://raw.githubusercontent.com/european-dynamics-rnd/CIRCULOOS_Data_model/main/openCallSpecific/searcle/SEMImage/schema.json    
  x-model-tags: searcle    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Example payloads    
Not available the example of a SEMImage in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
#### SEMImage NGSI-LD normalized Example    
Here is an example of a SEMImage in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "@context": [  
    "http://circuloos-ld-context/circuloos-context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context-v1.8.jsonld"  
  ],  
  "id": "urn:ngsi-ld:circuloos_searcle:sem:20260717-KTRL65",  
  "type": "SEMImage",  
  "equipment": {  
    "type": "Property",  
    "value": "FEG Quanta450"  
  },  
  "magnification": {  
    "type": "Property",  
    "value": "x250"  
  },  
  "imageUrl": {  
    "type": "Property",  
    "value": "https://api.searcle.cloud/files/urn%3Angsi-ld%3Acirculoos_searcle%3Asample%3A20260717-6U2HBA/20260717-KTRL65__008.tif"  
  },  
  "acceleratingVoltage": {  
    "type": "Property",  
    "value": 15,  
    "unitCode": "KVT"  
  }  
}  
```  
</details><!-- /80-Examples -->  
