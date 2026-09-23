<!-- 10-Header -->  
Entity: Process  
===============<!-- /10-Header -->  
<!-- 15-License -->  
[Open License](https://raw.githubusercontent.com/european-dynamics-rnd/CIRCULOOS_Data_model/refs/heads/main/LICENSE)  
<!-- /15-License -->  
<!-- 20-Description -->  
Global description: **CIRCULOOS data model for a reusable process definition in the ISLOPOL value chain, which can be referenced by multiple ProcessEvent or ProductionRun records, covering its name, purpose and triggering condition.**  
version: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## List of properties  

<sup><sub>[*] If there is not a type in an attribute is because it could have several types or different formats/patterns</sub></sup>  
- `description[*]`: Human-readable explanation of the process, including its purpose and the main input materials, resources and outputs.  - `id[string]`: Unique entity identifier, with the format urn:ngsi-ld:Process:<facility>:<processId>.  - `name[*]`: Human-readable name of the process. Given in the source as https://schema.org/name.  - `triggeringCondition[*]`: Condition or operational requirement that causes the process to be started, such as the need to process accumulated waste. Given in the source as https://context.dataspace-arditi.com/islopol/terms/v2/triggeringCondition.  - `type[string]`: NGSI Entity type. It has to be Process  <!-- /30-PropertiesList -->  
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
Process:    
  description: CIRCULOOS data model for a reusable process definition in the ISLOPOL value chain, which can be referenced by multiple ProcessEvent or ProductionRun records, covering its name, purpose and triggering condition.    
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
      description: Human-readable explanation of the process, including its purpose and the main input materials, resources and outputs.    
      x-ngsi:    
        type: Property    
    id:    
      description: Unique entity identifier, with the format urn:ngsi-ld:Process:<facility>:<processId>.    
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
      description: Human-readable name of the process. Given in the source as https://schema.org/name.    
      x-ngsi:    
        type: Property    
    triggeringCondition:    
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
      description: Condition or operational requirement that causes the process to be started, such as the need to process accumulated waste. Given in the source as https://context.dataspace-arditi.com/islopol/terms/v2/triggeringCondition.    
      x-ngsi:    
        type: Property    
    type:    
      description: NGSI Entity type. It has to be Process    
      enum:    
        - Process    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - name    
  type: object    
  x-derived-from: https://context.dataspace-arditi.com/islopol/entities/Process/v2/schema.json    
  x-disclaimer: Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program    
  x-license-url: https://github.com/smart-data-models/circuloos_data_model/blob/master/Process/LICENSE.md    
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
Not available the example of a Process in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
#### Process NGSI-LD normalized Example    
Here is an example of a Process in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "@context": [  
    "http://circuloos-ld-context/circuloos-context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context-v1.8.jsonld"  
  ],  
  "id": "urn:ngsi-ld:Process:ARM:blue-waste-stream-processing",  
  "type": "Process",  
  "name": {  
    "type": "Property",  
    "value": "Processamento da reciclagem da linha azul"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Processamento da reciclagem proveniente da linha azul da ARM. Inputs: Energia, Arame para enfardamento, Residuos da linha azul. Outputs: fardos de papel e cartao, residuos rejeitados, EPS reciclavel e EPS rejeitado."  
  },  
  "triggeringCondition": {  
    "type": "Property",  
    "value": "Quando necessario processar os residuos provenientes da linha azul da ARM."  
  }  
}  
```  
</details><!-- /80-Examples -->  
