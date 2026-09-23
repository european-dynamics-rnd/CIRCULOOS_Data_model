<!-- 10-Header -->  
Entity: BoilerTestSession  
=========================<!-- /10-Header -->  
<!-- 15-License -->  
[Open License](https://raw.githubusercontent.com/european-dynamics-rnd/CIRCULOOS_Data_model/refs/heads/main/LICENSE)  
<!-- /15-License -->  
<!-- 20-Description -->  
Global description: **CIRCULOOS data model for a biomass combustion test session on the EVOP boiler, covering the scenario and biomass batch tested, the fuel and energy figures recorded, the efficiency parameters reported by the measurement system, and the flue gas emission measurements.**  
version: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## List of properties  

<sup><sub>[*] If there is not a type in an attribute is because it could have several types or different formats/patterns</sub></sup>  
- `actualConsumptionKg[*]`: Expected unitCode: KGM. Actual quantity of biomass consumed during the specific test measurement.  - `airTemperature[*]`: Expected unitCode: CEL. Temperature of the surrounding air measured during the boiler test.  - `ashPercent[*]`: Expected unitCode: P1. Percentage of ash remaining after biomass combustion.  - `biomassBatch[*]`: Identifier of the biomass batch used during the boiler test session.  - `biomassConsumption[*]`: Expected unitCode: KGM. Quantity of biomass consumed during the boiler test.  - `boilerType[*]`: Identifies the boiler or heating system used during the test session.  - `co[*]`: Expected unitCode: 59 (ppm). Measured concentration of carbon monoxide (CO) in the flue gas.  - `co2[*]`: Expected unitCode: P1. Measured concentration of carbon dioxide (CO2) in the flue gas.  - `coCorrected[*]`: Expected unitCode: 59 (ppm). Corrected carbon monoxide (CO) concentration in the flue gas, according to the measurement conditions.  - `consumption7days[*]`: Expected unitCode: KGM. Biomass consumption recorded over a seven-day period during the test.  - `deltaT[*]`: Expected unitCode: KEL. Temperature difference measured during the boiler test.  - `density[*]`: Expected unitCode: KMQ. Density of the biomass used in the test, expressed as mass per unit of volume.  - `efficiency[*]`: Expected unitCode: P1. Overall efficiency recorded for the boiler test, expressed as a percentage.  - `electricConsumption[*]`: Expected unitCode: KWH. Electricity consumed by the boiler or associated equipment during the test.  - `etaC[*]`: Expected unitCode: P1. Combustion efficiency parameter recorded by the measurement system.  - `etaS[*]`: Expected unitCode: P1. Efficiency parameter recorded by the measurement system for the test session.  - `etaT[*]`: Expected unitCode: P1. Overall thermal efficiency parameter recorded by the measurement system.  - `flueGasDepression[*]`: Expected unitCode: PAL. Depression or negative pressure measured in the flue gas system during the boiler test.  - `flueGasTempAnalyzer[*]`: Expected unitCode: CEL. Flue gas temperature measured by the gas analyser.  - `flueGasTemperature[*]`: Expected unitCode: CEL. Flue gas temperature measured during the boiler test.  - `gasPressure[*]`: Expected unitCode: MBR. Gas pressure measured during the boiler test.  - `humidity[*]`: Expected unitCode: P1. Moisture content of the biomass used in the boiler test, expressed as a percentage.  - `id[string]`: Unique entity identifier, with the format urn:ngsi-ld:evop:boiler-session:<scenarioId>.  - `lambda[*]`: Dimensionless. Air-to-fuel ratio parameter (lambda) measured during biomass combustion.  - `no[*]`: Expected unitCode: 59 (ppm). Measured concentration of nitrogen monoxide (NO) in the flue gas.  - `noCorrected[*]`: Expected unitCode: 59 (ppm). Corrected nitrogen monoxide (NO) concentration according to the measurement conditions.  - `nox[*]`: Expected unitCode: 59 (ppm). Measured concentration of nitrogen oxides (NOx) in the flue gas.  - `noxCorrected[*]`: Expected unitCode: 59 (ppm). Corrected nitrogen oxides (NOx) concentration according to the measurement conditions.  - `o2[*]`: Expected unitCode: P1. Measured oxygen (O2) concentration in the flue gas.  - `o2Reference[*]`: Expected unitCode: P1. Reference oxygen concentration used for correcting flue gas emission measurements.  - `pci[*]`: Expected unitCode: KWH/KGM. Lower heating value (LHV) of the biomass, representing the energy released per unit of biomass during combustion.  - `pressure[*]`: Expected unitCode: PAL. Pressure measured during the boiler test by the monitoring equipment.  - `pufferTemperature[*]`: Expected unitCode: CEL. Temperature measured in the buffer or puffer tank during the boiler test.  - `qs[*]`: Expected unitCode: P1. Heat-loss or combustion-related parameter recorded by the measurement system during the test.  - `readingIndex[*]`: Dimensionless. Index identifying the specific measurement or reading within the test dataset.  - `scenarioName[*]`: Name of the biomass combustion scenario tested in the boiler, including the biomass type and relevant characteristics such as moisture content.  - `sourceWorkbookFileName[*]`: Name of the source spreadsheet from which the boiler test measurement data were obtained.  - `startDate[*]`: Date on which the boiler test session started.  - `targetTemperature[*]`: Expected unitCode: CEL. Target temperature set for the boiler or heated system during the test.  - `thermalEnergy[*]`: Expected unitCode: KWH. Thermal energy generated by the biomass combustion process during the test.  - `tiro[*]`: Expected unitCode: MBR. Draught parameter of the boiler or flue gas system measured during the test.  - `type[string]`: NGSI Entity type. It has to be BoilerTestSession  - `waterTemperature[*]`: Expected unitCode: CEL. Water temperature measured in the boiler or heating system during the test.  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Required properties  
- `boilerType`  - `id`  - `scenarioName`  - `startDate`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Data Model description of properties  
Sorted alphabetically (click for details)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
BoilerTestSession:    
  description: CIRCULOOS data model for a biomass combustion test session on the EVOP boiler, covering the scenario and biomass batch tested, the fuel and energy figures recorded, the efficiency parameters reported by the measurement system, and the flue gas emission measurements.    
  properties:    
    actualConsumptionKg:    
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
      description: 'Expected unitCode: KGM. Actual quantity of biomass consumed during the specific test measurement.'    
      x-ngsi:    
        type: Property    
    airTemperature:    
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
      description: 'Expected unitCode: CEL. Temperature of the surrounding air measured during the boiler test.'    
      x-ngsi:    
        type: Property    
    ashPercent:    
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
      description: 'Expected unitCode: P1. Percentage of ash remaining after biomass combustion.'    
      x-ngsi:    
        type: Property    
    biomassBatch:    
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
      description: Identifier of the biomass batch used during the boiler test session.    
      x-ngsi:    
        type: Relationship    
    biomassConsumption:    
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
      description: 'Expected unitCode: KGM. Quantity of biomass consumed during the boiler test.'    
      x-ngsi:    
        type: Property    
    boilerType:    
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
      description: Identifies the boiler or heating system used during the test session.    
      x-ngsi:    
        type: Property    
    co:    
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
      description: 'Expected unitCode: 59 (ppm). Measured concentration of carbon monoxide (CO) in the flue gas.'    
      x-ngsi:    
        type: Property    
    co2:    
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
      description: 'Expected unitCode: P1. Measured concentration of carbon dioxide (CO2) in the flue gas.'    
      x-ngsi:    
        type: Property    
    coCorrected:    
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
      description: 'Expected unitCode: 59 (ppm). Corrected carbon monoxide (CO) concentration in the flue gas, according to the measurement conditions.'    
      x-ngsi:    
        type: Property    
    consumption7days:    
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
      description: 'Expected unitCode: KGM. Biomass consumption recorded over a seven-day period during the test.'    
      x-ngsi:    
        type: Property    
    deltaT:    
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
      description: 'Expected unitCode: KEL. Temperature difference measured during the boiler test.'    
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
              description: Unit of measurement of the value, given as a UN/CEFACT code where one exists.    
              type: string    
            value:    
              description: Exact measured value, when a single figure is known.    
              type: number    
          required:    
            - type    
            - unitCode    
          type: object    
      description: 'Expected unitCode: KMQ. Density of the biomass used in the test, expressed as mass per unit of volume.'    
      x-ngsi:    
        type: Property    
    efficiency:    
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
      description: 'Expected unitCode: P1. Overall efficiency recorded for the boiler test, expressed as a percentage.'    
      x-ngsi:    
        type: Property    
    electricConsumption:    
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
      description: 'Expected unitCode: KWH. Electricity consumed by the boiler or associated equipment during the test.'    
      x-ngsi:    
        type: Property    
    etaC:    
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
      description: 'Expected unitCode: P1. Combustion efficiency parameter recorded by the measurement system.'    
      x-ngsi:    
        type: Property    
    etaS:    
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
      description: 'Expected unitCode: P1. Efficiency parameter recorded by the measurement system for the test session.'    
      x-ngsi:    
        type: Property    
    etaT:    
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
      description: 'Expected unitCode: P1. Overall thermal efficiency parameter recorded by the measurement system.'    
      x-ngsi:    
        type: Property    
    flueGasDepression:    
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
      description: 'Expected unitCode: PAL. Depression or negative pressure measured in the flue gas system during the boiler test.'    
      x-ngsi:    
        type: Property    
    flueGasTempAnalyzer:    
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
      description: 'Expected unitCode: CEL. Flue gas temperature measured by the gas analyser.'    
      x-ngsi:    
        type: Property    
    flueGasTemperature:    
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
      description: 'Expected unitCode: CEL. Flue gas temperature measured during the boiler test.'    
      x-ngsi:    
        type: Property    
    gasPressure:    
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
      description: 'Expected unitCode: MBR. Gas pressure measured during the boiler test.'    
      x-ngsi:    
        type: Property    
    humidity:    
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
      description: 'Expected unitCode: P1. Moisture content of the biomass used in the boiler test, expressed as a percentage.'    
      x-ngsi:    
        type: Property    
    id:    
      description: Unique entity identifier, with the format urn:ngsi-ld:evop:boiler-session:<scenarioId>.    
      type: string    
      x-ngsi:    
        type: Property    
    lambda:    
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
      description: Dimensionless. Air-to-fuel ratio parameter (lambda) measured during biomass combustion.    
      x-ngsi:    
        type: Property    
    'no':    
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
      description: 'Expected unitCode: 59 (ppm). Measured concentration of nitrogen monoxide (NO) in the flue gas.'    
      x-ngsi:    
        type: Property    
    noCorrected:    
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
      description: 'Expected unitCode: 59 (ppm). Corrected nitrogen monoxide (NO) concentration according to the measurement conditions.'    
      x-ngsi:    
        type: Property    
    nox:    
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
      description: 'Expected unitCode: 59 (ppm). Measured concentration of nitrogen oxides (NOx) in the flue gas.'    
      x-ngsi:    
        type: Property    
    noxCorrected:    
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
      description: 'Expected unitCode: 59 (ppm). Corrected nitrogen oxides (NOx) concentration according to the measurement conditions.'    
      x-ngsi:    
        type: Property    
    o2:    
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
      description: 'Expected unitCode: P1. Measured oxygen (O2) concentration in the flue gas.'    
      x-ngsi:    
        type: Property    
    o2Reference:    
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
      description: 'Expected unitCode: P1. Reference oxygen concentration used for correcting flue gas emission measurements.'    
      x-ngsi:    
        type: Property    
    pci:    
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
      description: 'Expected unitCode: KWH/KGM. Lower heating value (LHV) of the biomass, representing the energy released per unit of biomass during combustion.'    
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
      description: 'Expected unitCode: PAL. Pressure measured during the boiler test by the monitoring equipment.'    
      x-ngsi:    
        type: Property    
    pufferTemperature:    
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
      description: 'Expected unitCode: CEL. Temperature measured in the buffer or puffer tank during the boiler test.'    
      x-ngsi:    
        type: Property    
    qs:    
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
      description: 'Expected unitCode: P1. Heat-loss or combustion-related parameter recorded by the measurement system during the test.'    
      x-ngsi:    
        type: Property    
    readingIndex:    
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
      description: Dimensionless. Index identifying the specific measurement or reading within the test dataset.    
      x-ngsi:    
        type: Property    
    scenarioName:    
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
      description: Name of the biomass combustion scenario tested in the boiler, including the biomass type and relevant characteristics such as moisture content.    
      x-ngsi:    
        type: Property    
    sourceWorkbookFileName:    
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
      description: Name of the source spreadsheet from which the boiler test measurement data were obtained.    
      x-ngsi:    
        type: Property    
    startDate:    
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
      description: Date on which the boiler test session started.    
      x-ngsi:    
        type: Property    
    targetTemperature:    
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
      description: 'Expected unitCode: CEL. Target temperature set for the boiler or heated system during the test.'    
      x-ngsi:    
        type: Property    
    thermalEnergy:    
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
      description: 'Expected unitCode: KWH. Thermal energy generated by the biomass combustion process during the test.'    
      x-ngsi:    
        type: Property    
    tiro:    
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
      description: 'Expected unitCode: MBR. Draught parameter of the boiler or flue gas system measured during the test.'    
      x-ngsi:    
        type: Property    
    type:    
      description: NGSI Entity type. It has to be BoilerTestSession    
      enum:    
        - BoilerTestSession    
      type: string    
      x-ngsi:    
        type: Property    
    waterTemperature:    
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
      description: 'Expected unitCode: CEL. Water temperature measured in the boiler or heating system during the test.'    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - scenarioName    
    - boilerType    
    - startDate    
  type: object    
  x-derived-from: ''    
  x-disclaimer: Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program    
  x-license-url: https://github.com/smart-data-models/circuloos_data_model/blob/master/BoilerTestSession/LICENSE.md    
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
Not available the example of a BoilerTestSession in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
#### BoilerTestSession NGSI-LD normalized Example    
Here is an example of a BoilerTestSession in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "@context": [  
    "http://circuloos-ld-context/circuloos-context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context-v1.8.jsonld"  
  ],  
  "id": "urn:ngsi-ld:evop:boiler-session:hueso-certificado-10-humedad",  
  "type": "BoilerTestSession",  
  "scenarioName": {  
    "type": "Property",  
    "value": "HUESO CERTIFICADO (10% HUMEDAD)"  
  },  
  "boilerType": {  
    "type": "Property",  
    "value": "EVOP Biomasa"  
  },  
  "biomassBatch": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:evop:biomass-batch:olive-pits-receipt:v6-hueso-certificado-10-humedad"  
  },  
  "startDate": {  
    "type": "Property",  
    "value": "2026-06-18"  
  },  
  "readingIndex": {  
    "type": "Property",  
    "value": 4  
  },  
  "sourceWorkbookFileName": {  
    "type": "Property",  
    "value": "Datos de medicion hueso certificado TOMA 1_v6.xlsx"  
  },  
  "targetTemperature": {  
    "type": "Property",  
    "value": 80,  
    "unitCode": "CEL"  
  },  
  "humidity": {  
    "type": "Property",  
    "value": 10,  
    "unitCode": "P1"  
  },  
  "consumption7days": {  
    "type": "Property",  
    "value": 469,  
    "unitCode": "KGM"  
  },  
  "pci": {  
    "type": "Property",  
    "value": 4.41,  
    "unitCode": "KWH/KGM"  
  },  
  "thermalEnergy": {  
    "type": "Property",  
    "value": 2068,  
    "unitCode": "KWH"  
  },  
  "electricConsumption": {  
    "type": "Property",  
    "value": 14,  
    "unitCode": "KWH"  
  },  
  "biomassConsumption": {  
    "type": "Property",  
    "value": 10,  
    "unitCode": "KGM"  
  },  
  "actualConsumptionKg": {  
    "type": "Property",  
    "value": 10,  
    "unitCode": "KGM"  
  },  
  "ashPercent": {  
    "type": "Property",  
    "value": 0.9,  
    "unitCode": "P1"  
  },  
  "efficiency": {  
    "type": "Property",  
    "value": 84.9,  
    "unitCode": "P1"  
  },  
  "density": {  
    "type": "Property",  
    "value": 650,  
    "unitCode": "KMQ"  
  },  
  "airTemperature": {  
    "type": "Property",  
    "value": 28.1,  
    "unitCode": "CEL"  
  },  
  "waterTemperature": {  
    "type": "Property",  
    "value": 80,  
    "unitCode": "CEL"  
  },  
  "pufferTemperature": {  
    "type": "Property",  
    "value": 29,  
    "unitCode": "CEL"  
  },  
  "deltaT": {  
    "type": "Property",  
    "value": 125.2,  
    "unitCode": "KEL"  
  },  
  "flueGasTemperature": {  
    "type": "Property",  
    "value": 164,  
    "unitCode": "CEL"  
  },  
  "flueGasTempAnalyzer": {  
    "type": "Property",  
    "value": 153.3,  
    "unitCode": "CEL"  
  },  
  "flueGasDepression": {  
    "type": "Property",  
    "value": 27,  
    "unitCode": "PAL"  
  },  
  "gasPressure": {  
    "type": "Property",  
    "value": -0.04,  
    "unitCode": "MBR"  
  },  
  "pressure": {  
    "type": "Property",  
    "value": 2099,  
    "unitCode": "PAL"  
  },  
  "tiro": {  
    "type": "Property",  
    "value": 0.122,  
    "unitCode": "MBR"  
  },  
  "lambda": {  
    "type": "Property",  
    "value": 3.31  
  },  
  "co": {  
    "type": "Property",  
    "value": 541,  
    "unitCode": "59"  
  },  
  "coCorrected": {  
    "type": "Property",  
    "value": 678,  
    "unitCode": "59"  
  },  
  "co2": {  
    "type": "Property",  
    "value": 5.8,  
    "unitCode": "P1"  
  },  
  "no": {  
    "type": "Property",  
    "value": 58,  
    "unitCode": "59"  
  },  
  "noCorrected": {  
    "type": "Property",  
    "value": 73,  
    "unitCode": "59"  
  },  
  "nox": {  
    "type": "Property",  
    "value": 61,  
    "unitCode": "59"  
  },  
  "noxCorrected": {  
    "type": "Property",  
    "value": 76,  
    "unitCode": "59"  
  },  
  "o2": {  
    "type": "Property",  
    "value": 14.6,  
    "unitCode": "P1"  
  },  
  "o2Reference": {  
    "type": "Property",  
    "value": 13,  
    "unitCode": "P1"  
  },  
  "etaC": {  
    "type": "Property",  
    "value": 0,  
    "unitCode": "P1"  
  },  
  "etaS": {  
    "type": "Property",  
    "value": 84.4,  
    "unitCode": "P1"  
  },  
  "etaT": {  
    "type": "Property",  
    "value": 84.4,  
    "unitCode": "P1"  
  },  
  "qs": {  
    "type": "Property",  
    "value": 15.6,  
    "unitCode": "P1"  
  }  
}  
```  
</details><!-- /80-Examples -->  
