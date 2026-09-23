<!-- 10-Header -->  
Entity: ExtruderObservation  
===========================<!-- /10-Header -->  
<!-- 15-License -->  
[Open License](https://raw.githubusercontent.com/european-dynamics-rnd/CIRCULOOS_Data_model/refs/heads/main/LICENSE)  
<!-- /15-License -->  
<!-- 20-Description -->  
Global description: **CIRCULOOS data model for a monitoring observation of the Plasmix Road recycled-plastic extrusion line, covering the actual and set temperatures of the ten extruder zones and the cutting zone, together with the speeds and currents of the extruder, cutter, feeder and shredder.**  
version: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## List of properties  

<sup><sub>[*] If there is not a type in an attribute is because it could have several types or different formats/patterns</sub></sup>  
- `crusherCurrent[*]`: Expected unitCode: AMP. Shredder current.  - `crusherRotationSpeed[*]`: Expected unitCode: RPM. Speed of the shredder motor.  - `crusherTemperature[*]`: Expected unitCode: CEL. Shredder temperature.  - `cuttingSpeed[*]`: Expected unitCode: RPM. Cutting motor speed. Source tag: cut_speed_rpm.  - `cuttingSpeedCurrent[*]`: Expected unitCode: AMP. Cutting motor amperage. Source tag: cutting_speed_amp.  - `cuttingZoneActualTemperature[*]`: Expected unitCode: CEL. Cutting zone temperature (current value). Source tag: t_cutting_zone_act_c.  - `cuttingZoneSetTemperature[*]`: Expected unitCode: CEL. Cutting zone temperature (target value). Source tag: t_cutting_zone_sp_c.  - `extruderCurrent[*]`: Expected unitCode: AMP. Extruder motor current. Source tag: extr_corr_amp.  - `extruderId[*]`: Identifier of the extruder the observation belongs to (recorded in the source as the user session).  - `extruderWorkingSpeed[*]`: Expected unitCode: P1. Extruder speed, as a percentage of its maximum.  - `feedSpeedWorking[*]`: Expected unitCode: P1. Feeder auger speed, as a percentage of its maximum.  - `id[string]`: Unique entity identifier, with the format urn:ngsi-ld:extruder:observation:<timestamp>.  - `screwFeedCurrent[*]`: Expected unitCode: AMP. Feeder screw amperage.  - `type[string]`: NGSI Entity type. It has to be ExtruderObservation  - `zone10ActualTemperature[*]`: Expected unitCode: CEL. Extruder Zone 10 temperature (current value). Source tag: t_zone10_extr_act_c.  - `zone10SetTemperature[*]`: Expected unitCode: CEL. Extruder Zone 10 set temperature (target value). Source tag: t_zone10_extr_sp_c.  - `zone1ActualTemperature[*]`: Expected unitCode: CEL. Extruder Zone 1 temperature (current value). Source tag: t_zone1_extr_act_c.  - `zone1SetTemperature[*]`: Expected unitCode: CEL. Extruder Zone 1 set temperature (target value). Source tag: t_zone1_extr_sp_c.  - `zone2ActualTemperature[*]`: Expected unitCode: CEL. Extruder Zone 2 temperature (current value). Source tag: t_zone2_extr_act_c.  - `zone2SetTemperature[*]`: Expected unitCode: CEL. Extruder Zone 2 set temperature (target value). Source tag: t_zone2_extr_sp_c.  - `zone3ActualTemperature[*]`: Expected unitCode: CEL. Extruder Zone 3 temperature (current value). Source tag: t_zone3_extr_act_c.  - `zone3SetTemperature[*]`: Expected unitCode: CEL. Extruder Zone 3 set temperature (target value). Source tag: t_zone3_extr_sp_c.  - `zone4ActualTemperature[*]`: Expected unitCode: CEL. Extruder Zone 4 temperature (current value). Source tag: t_zone4_extr_act_c.  - `zone4SetTemperature[*]`: Expected unitCode: CEL. Extruder Zone 4 set temperature (target value). Source tag: t_zone4_extr_sp_c.  - `zone5ActualTemperature[*]`: Expected unitCode: CEL. Extruder Zone 5 temperature (current value). Source tag: t_zone5_extr_act_c.  - `zone5SetTemperature[*]`: Expected unitCode: CEL. Extruder Zone 5 set temperature (target value). Source tag: t_zone5_extr_sp_c.  - `zone6ActualTemperature[*]`: Expected unitCode: CEL. Extruder Zone 6 temperature (current value). Source tag: t_zone6_extr_act_c.  - `zone6SetTemperature[*]`: Expected unitCode: CEL. Extruder Zone 6 set temperature (target value). Source tag: t_zone6_extr_sp_c.  - `zone7ActualTemperature[*]`: Expected unitCode: CEL. Extruder Zone 7 temperature (current value). Source tag: t_zone7_extr_act_c.  - `zone7SetTemperature[*]`: Expected unitCode: CEL. Extruder Zone 7 set temperature (target value). Source tag: t_zone7_extr_sp_c.  - `zone8ActualTemperature[*]`: Expected unitCode: CEL. Extruder Zone 8 temperature (current value). Source tag: t_zone8_extr_act_c.  - `zone8SetTemperature[*]`: Expected unitCode: CEL. Extruder Zone 8 set temperature (target value). Source tag: t_zone8_extr_sp_c.  - `zone9ActualTemperature[*]`: Expected unitCode: CEL. Extruder Zone 9 temperature (current value). Source tag: t_zone9_extr_act_c.  - `zone9SetTemperature[*]`: Expected unitCode: CEL. Extruder Zone 9 set temperature (target value). Source tag: t_zone9_extr_sp_c.  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Required properties  
- `extruderId`  - `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Data Model description of properties  
Sorted alphabetically (click for details)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
ExtruderObservation:    
  description: CIRCULOOS data model for a monitoring observation of the Plasmix Road recycled-plastic extrusion line, covering the actual and set temperatures of the ten extruder zones and the cutting zone, together with the speeds and currents of the extruder, cutter, feeder and shredder.    
  properties:    
    crusherCurrent:    
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
      description: 'Expected unitCode: AMP. Shredder current.'    
      x-ngsi:    
        type: Property    
    crusherRotationSpeed:    
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
      description: 'Expected unitCode: RPM. Speed of the shredder motor.'    
      x-ngsi:    
        type: Property    
    crusherTemperature:    
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
      description: 'Expected unitCode: CEL. Shredder temperature.'    
      x-ngsi:    
        type: Property    
    cuttingSpeed:    
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
      description: 'Expected unitCode: RPM. Cutting motor speed. Source tag: cut_speed_rpm.'    
      x-ngsi:    
        type: Property    
    cuttingSpeedCurrent:    
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
      description: 'Expected unitCode: AMP. Cutting motor amperage. Source tag: cutting_speed_amp.'    
      x-ngsi:    
        type: Property    
    cuttingZoneActualTemperature:    
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
      description: 'Expected unitCode: CEL. Cutting zone temperature (current value). Source tag: t_cutting_zone_act_c.'    
      x-ngsi:    
        type: Property    
    cuttingZoneSetTemperature:    
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
      description: 'Expected unitCode: CEL. Cutting zone temperature (target value). Source tag: t_cutting_zone_sp_c.'    
      x-ngsi:    
        type: Property    
    extruderCurrent:    
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
      description: 'Expected unitCode: AMP. Extruder motor current. Source tag: extr_corr_amp.'    
      x-ngsi:    
        type: Property    
    extruderId:    
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
      description: Identifier of the extruder the observation belongs to (recorded in the source as the user session).    
      x-ngsi:    
        type: Property    
    extruderWorkingSpeed:    
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
      description: 'Expected unitCode: P1. Extruder speed, as a percentage of its maximum.'    
      x-ngsi:    
        type: Property    
    feedSpeedWorking:    
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
      description: 'Expected unitCode: P1. Feeder auger speed, as a percentage of its maximum.'    
      x-ngsi:    
        type: Property    
    id:    
      description: Unique entity identifier, with the format urn:ngsi-ld:extruder:observation:<timestamp>.    
      type: string    
      x-ngsi:    
        type: Property    
    screwFeedCurrent:    
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
      description: 'Expected unitCode: AMP. Feeder screw amperage.'    
      x-ngsi:    
        type: Property    
    type:    
      description: NGSI Entity type. It has to be ExtruderObservation    
      enum:    
        - ExtruderObservation    
      type: string    
      x-ngsi:    
        type: Property    
    zone10ActualTemperature:    
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
      description: 'Expected unitCode: CEL. Extruder Zone 10 temperature (current value). Source tag: t_zone10_extr_act_c.'    
      x-ngsi:    
        type: Property    
    zone10SetTemperature:    
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
      description: 'Expected unitCode: CEL. Extruder Zone 10 set temperature (target value). Source tag: t_zone10_extr_sp_c.'    
      x-ngsi:    
        type: Property    
    zone1ActualTemperature:    
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
      description: 'Expected unitCode: CEL. Extruder Zone 1 temperature (current value). Source tag: t_zone1_extr_act_c.'    
      x-ngsi:    
        type: Property    
    zone1SetTemperature:    
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
      description: 'Expected unitCode: CEL. Extruder Zone 1 set temperature (target value). Source tag: t_zone1_extr_sp_c.'    
      x-ngsi:    
        type: Property    
    zone2ActualTemperature:    
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
      description: 'Expected unitCode: CEL. Extruder Zone 2 temperature (current value). Source tag: t_zone2_extr_act_c.'    
      x-ngsi:    
        type: Property    
    zone2SetTemperature:    
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
      description: 'Expected unitCode: CEL. Extruder Zone 2 set temperature (target value). Source tag: t_zone2_extr_sp_c.'    
      x-ngsi:    
        type: Property    
    zone3ActualTemperature:    
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
      description: 'Expected unitCode: CEL. Extruder Zone 3 temperature (current value). Source tag: t_zone3_extr_act_c.'    
      x-ngsi:    
        type: Property    
    zone3SetTemperature:    
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
      description: 'Expected unitCode: CEL. Extruder Zone 3 set temperature (target value). Source tag: t_zone3_extr_sp_c.'    
      x-ngsi:    
        type: Property    
    zone4ActualTemperature:    
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
      description: 'Expected unitCode: CEL. Extruder Zone 4 temperature (current value). Source tag: t_zone4_extr_act_c.'    
      x-ngsi:    
        type: Property    
    zone4SetTemperature:    
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
      description: 'Expected unitCode: CEL. Extruder Zone 4 set temperature (target value). Source tag: t_zone4_extr_sp_c.'    
      x-ngsi:    
        type: Property    
    zone5ActualTemperature:    
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
      description: 'Expected unitCode: CEL. Extruder Zone 5 temperature (current value). Source tag: t_zone5_extr_act_c.'    
      x-ngsi:    
        type: Property    
    zone5SetTemperature:    
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
      description: 'Expected unitCode: CEL. Extruder Zone 5 set temperature (target value). Source tag: t_zone5_extr_sp_c.'    
      x-ngsi:    
        type: Property    
    zone6ActualTemperature:    
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
      description: 'Expected unitCode: CEL. Extruder Zone 6 temperature (current value). Source tag: t_zone6_extr_act_c.'    
      x-ngsi:    
        type: Property    
    zone6SetTemperature:    
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
      description: 'Expected unitCode: CEL. Extruder Zone 6 set temperature (target value). Source tag: t_zone6_extr_sp_c.'    
      x-ngsi:    
        type: Property    
    zone7ActualTemperature:    
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
      description: 'Expected unitCode: CEL. Extruder Zone 7 temperature (current value). Source tag: t_zone7_extr_act_c.'    
      x-ngsi:    
        type: Property    
    zone7SetTemperature:    
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
      description: 'Expected unitCode: CEL. Extruder Zone 7 set temperature (target value). Source tag: t_zone7_extr_sp_c.'    
      x-ngsi:    
        type: Property    
    zone8ActualTemperature:    
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
      description: 'Expected unitCode: CEL. Extruder Zone 8 temperature (current value). Source tag: t_zone8_extr_act_c.'    
      x-ngsi:    
        type: Property    
    zone8SetTemperature:    
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
      description: 'Expected unitCode: CEL. Extruder Zone 8 set temperature (target value). Source tag: t_zone8_extr_sp_c.'    
      x-ngsi:    
        type: Property    
    zone9ActualTemperature:    
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
      description: 'Expected unitCode: CEL. Extruder Zone 9 temperature (current value). Source tag: t_zone9_extr_act_c.'    
      x-ngsi:    
        type: Property    
    zone9SetTemperature:    
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
      description: 'Expected unitCode: CEL. Extruder Zone 9 set temperature (target value). Source tag: t_zone9_extr_sp_c.'    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - extruderId    
  type: object    
  x-derived-from: ''    
  x-disclaimer: Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program    
  x-license-url: https://github.com/smart-data-models/circuloos_data_model/blob/master/ExtruderObservation/LICENSE.md    
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
Not available the example of a ExtruderObservation in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
#### ExtruderObservation NGSI-LD normalized Example    
Here is an example of a ExtruderObservation in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "@context": [  
    "http://circuloos-ld-context/circuloos-context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context-v1.8.jsonld"  
  ],  
  "id": "urn:ngsi-ld:extruder:observation:20260131T234401",  
  "type": "ExtruderObservation",  
  "zone1ActualTemperature": {  
    "type": "Property",  
    "value": 189.609,  
    "unitCode": "CEL"  
  },  
  "zone1SetTemperature": {  
    "type": "Property",  
    "value": 0.0019,  
    "unitCode": "CEL"  
  },  
  "zone2ActualTemperature": {  
    "type": "Property",  
    "value": 220.1775,  
    "unitCode": "CEL"  
  },  
  "zone2SetTemperature": {  
    "type": "Property",  
    "value": 0.0022,  
    "unitCode": "CEL"  
  },  
  "zone3ActualTemperature": {  
    "type": "Property",  
    "value": 219.7894,  
    "unitCode": "CEL"  
  },  
  "zone3SetTemperature": {  
    "type": "Property",  
    "value": 0.0022,  
    "unitCode": "CEL"  
  },  
  "zone4ActualTemperature": {  
    "type": "Property",  
    "value": 22.00941,  
    "unitCode": "CEL"  
  },  
  "zone4SetTemperature": {  
    "type": "Property",  
    "value": 220,  
    "unitCode": "CEL"  
  },  
  "zone5ActualTemperature": {  
    "type": "Property",  
    "value": 22.93826,  
    "unitCode": "CEL"  
  },  
  "zone5SetTemperature": {  
    "type": "Property",  
    "value": 0.0023,  
    "unitCode": "CEL"  
  },  
  "zone6ActualTemperature": {  
    "type": "Property",  
    "value": 24.51125,  
    "unitCode": "CEL"  
  },  
  "zone6SetTemperature": {  
    "type": "Property",  
    "value": 245,  
    "unitCode": "CEL"  
  },  
  "zone7ActualTemperature": {  
    "type": "Property",  
    "value": 22.50941,  
    "unitCode": "CEL"  
  },  
  "zone7SetTemperature": {  
    "type": "Property",  
    "value": 0.00225,  
    "unitCode": "CEL"  
  },  
  "zone8ActualTemperature": {  
    "type": "Property",  
    "value": 22.49059,  
    "unitCode": "CEL"  
  },  
  "zone8SetTemperature": {  
    "type": "Property",  
    "value": 0.00225,  
    "unitCode": "CEL"  
  },  
  "zone9ActualTemperature": {  
    "type": "Property",  
    "value": 22.99925,  
    "unitCode": "CEL"  
  },  
  "zone9SetTemperature": {  
    "type": "Property",  
    "value": 230,  
    "unitCode": "CEL"  
  },  
  "zone10ActualTemperature": {  
    "type": "Property",  
    "value": 24.00941,  
    "unitCode": "CEL"  
  },  
  "zone10SetTemperature": {  
    "type": "Property",  
    "value": 0.0024,  
    "unitCode": "CEL"  
  },  
  "extruderId": {  
    "type": "Property",  
    "value": "extruder_1"  
  },  
  "cuttingZoneActualTemperature": {  
    "type": "Property",  
    "value": 24.08102,  
    "unitCode": "CEL"  
  },  
  "cuttingZoneSetTemperature": {  
    "type": "Property",  
    "value": 0.0024,  
    "unitCode": "CEL"  
  },  
  "extruderWorkingSpeed": {  
    "type": "Property",  
    "value": 0,  
    "unitCode": "P1"  
  },  
  "extruderCurrent": {  
    "type": "Property",  
    "value": 0,  
    "unitCode": "AMP"  
  },  
  "cuttingSpeedCurrent": {  
    "type": "Property",  
    "value": 0,  
    "unitCode": "AMP"  
  },  
  "cuttingSpeed": {  
    "type": "Property",  
    "value": 0,  
    "unitCode": "RPM"  
  },  
  "feedSpeedWorking": {  
    "type": "Property",  
    "value": 0,  
    "unitCode": "P1"  
  },  
  "screwFeedCurrent": {  
    "type": "Property",  
    "value": 0,  
    "unitCode": "AMP"  
  },  
  "crusherTemperature": {  
    "type": "Property",  
    "value": 14.90131,  
    "unitCode": "CEL"  
  },  
  "crusherCurrent": {  
    "type": "Property",  
    "value": 0,  
    "unitCode": "AMP"  
  },  
  "crusherRotationSpeed": {  
    "type": "Property",  
    "value": 0,  
    "unitCode": "RPM"  
  }  
}  
```  
</details><!-- /80-Examples -->  
