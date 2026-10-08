<!-- 10-Header -->  
Entity: ElectrospindleObservation  
=================================<!-- /10-Header -->  
<!-- 15-License -->  
[Open License](https://raw.githubusercontent.com/european-dynamics-rnd/CIRCULOOS_Data_model/refs/heads/main/LICENSE)  
<!-- /15-License -->  
<!-- 20-Description -->  
Global description: **CIRCULOOS data model for the IoT data acquired from a electrospindle machine tool. The monitored temperatures, motor currents and rotational speeds define the duty cycle of the electrospindle, the spindle bearings and the X, Y and Z axis ballscrew/nut assemblies, and support the estimation of their residual lifetime and the prediction of suitable end-of-life R-strategies.**  
version: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## List of properties  

<sup><sub>[*] If there is not a type in an attribute is because it could have several types or different formats/patterns</sub></sup>  
- `address[object]`: The mailing address  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: Property. The country. For example, Spain. Model:'https://schema.org/addressCountry'    
	- `addressLocality[string]`: Property. The locality in which the street address is, and which is in the region. Model:'https://schema.org/addressLocality'    
	- `addressRegion[string]`: Property. The region in which the locality is, and which is in the country. Model:'https://schema.org/addressRegion'    
	- `district[string]`: Property. A district is a type of administrative division that, in some countries, is managed by the local government    
	- `postOfficeBoxNumber[string]`: Property. The post office box number for PO box addresses. For example, 03578. Model:'https://schema.org/postOfficeBoxNumber'    
	- `postalCode[string]`: Property. The postal code. For example, 24004. Model:'https://schema.org/https://schema.org/postalCode'    
	- `streetAddress[string]`: Property. The street address. Model:'https://schema.org/streetAddress'    
	- `streetNr[string]`: Property. Number identifying a specific property on a public street    
- `alternateName[string]`: An alternative name for this item  - `areaServed[string]`: The geographic area where a service or offered item is provided  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: A sequence of characters identifying the provider of the harmonised data entity  - `dateCreated[date-time]`: Entity creation timestamp. This will usually be allocated by the storage platform  - `dateModified[date-time]`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform  - `description[string]`: A description of this item  - `id[string]`: Unique entity identifier of the monitored machine tool, with the format urn:ngsi-ld:ElectrospindleObservation:<machineId>.  - `location[*]`: GeoProperty. Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon  - `name[string]`: The name of this item  - `owner[array]`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  - `seeAlso[*]`: list of uri pointing to additional resources about the item  - `source[string]`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object  - `spindleBearingTemperature[*]`: Expected unitCode: CEL. Temperature of the spindle bearings. This parameter is used to monitor the thermal load affecting the spindle bearing system and contributes to the definition of the bearing duty cycle. It supports the calculation of the residual lifetime of the spindle bearings and the prediction of suitable end-of-life R-strategies. Source field: T1.  - `spindleMotorCurrent[*]`: Expected unitCode: AMP. Motor current of the spindle drive. This attribute is used to estimate the spindle motor torque and, consequently, the mechanical loads acting on the spindle bearings. These data contribute to the duty-cycle calculation of the spindle bearing system, supporting residual lifetime estimation and the prediction of suitable end-of-life R-strategies. Source field: IS.  - `spindleMotorTemperature[*]`: Expected unitCode: CEL. Temperature of the electrospindle motor. This parameter is used to characterise the thermal operating conditions of the electrospindle and contributes to the definition of the component duty cycle. It supports the estimation of the residual lifetime of the electrospindle motor and the prediction of suitable end-of-life R-strategies. Source field: Te.  - `spindleSpeed[*]`: Expected unitCode: RPM. Electrospindle rotational speed. This attribute is used to characterise the operating profile of the spindle and to determine the duty cycle of the spindle bearing system. Together with load-related and thermal information, it supports residual lifetime calculation and the prediction of suitable end-of-life R-strategies. Source field: VS.  - `type[string]`: NGSI Entity type. It has to be ElectrospindleObservation  - `xAxisMotorCurrent[*]`: Expected unitCode: AMP. Motor current of the X-axis drive. This attribute is used to estimate the motor torque of the X-axis and, consequently, the mechanical forces transmitted to the X-axis ballscrew/nut system. These data contribute to the duty-cycle calculation of the X-axis ballscrew/nut assembly, supporting residual lifetime estimation and the prediction of suitable end-of-life R-strategies. Source field: IX.  - `xAxisMotorSpeed[*]`: Expected unitCode: RPM. Motor rotational speed of the X-axis drive. This attribute is used to characterise the operating profile of the X-axis and to determine the duty cycle of the X-axis ballscrew/nut system. Together with load-related information, it supports residual lifetime calculation and the prediction of suitable end-of-life R-strategies. Source field: VX.  - `yAxisMotorCurrent[*]`: Expected unitCode: AMP. Motor current of the Y-axis drive. This attribute is used to estimate the motor torque of the Y-axis and, consequently, the mechanical forces transmitted to the Y-axis ballscrew/nut system. These data contribute to the duty-cycle calculation of the Y-axis ballscrew/nut assembly, supporting residual lifetime estimation and the prediction of suitable end-of-life R-strategies. Source field: IY.  - `yAxisMotorSpeed[*]`: Expected unitCode: RPM. Motor rotational speed of the Y-axis drive. This attribute is used to characterise the operating profile of the Y-axis and to determine the duty cycle of the Y-axis ballscrew/nut system. Together with load-related information, it supports residual lifetime calculation and the prediction of suitable end-of-life R-strategies. Source field: VY.  - `zAxisMotorCurrent[*]`: Expected unitCode: AMP. Motor current of the Z-axis drive. This attribute is used to estimate the motor torque of the Z-axis and, consequently, the mechanical forces transmitted to the Z-axis ballscrew/nut system. These data contribute to the duty-cycle calculation of the Z-axis ballscrew/nut assembly, supporting residual lifetime estimation and the prediction of suitable end-of-life R-strategies. Source field: IZ.  - `zAxisMotorSpeed[*]`: Expected unitCode: RPM. Motor rotational speed of the Z-axis drive. This attribute is used to characterise the operating profile of the Z-axis and to determine the duty cycle of the Z-axis ballscrew/nut system. Together with load-related information, it supports residual lifetime calculation and the prediction of suitable end-of-life R-strategies. Source field: VZ.  <!-- /30-PropertiesList -->  
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
ElectrospindleObservation:    
  description: CIRCULOOS data model for the IoT data acquired from a electrospindle machine tool. The monitored temperatures, motor currents and rotational speeds define the duty cycle of the electrospindle, the spindle bearings and the X, Y and Z axis ballscrew/nut assemblies, and support the estimation of their residual lifetime and the prediction of suitable end-of-life R-strategies.    
  properties:    
    address:    
      description: The mailing address    
      properties:    
        addressCountry:    
          description: Property. The country. For example, Spain. Model:'https://schema.org/addressCountry'    
          type: string    
        addressLocality:    
          description: Property. The locality in which the street address is, and which is in the region. Model:'https://schema.org/addressLocality'    
          type: string    
        addressRegion:    
          description: Property. The region in which the locality is, and which is in the country. Model:'https://schema.org/addressRegion'    
          type: string    
        district:    
          description: Property. A district is a type of administrative division that, in some countries, is managed by the local government    
          type: string    
        postOfficeBoxNumber:    
          description: Property. The post office box number for PO box addresses. For example, 03578. Model:'https://schema.org/postOfficeBoxNumber'    
          type: string    
        postalCode:    
          description: Property. The postal code. For example, 24004. Model:'https://schema.org/https://schema.org/postalCode'    
          type: string    
        streetAddress:    
          description: Property. The street address. Model:'https://schema.org/streetAddress'    
          type: string    
        streetNr:    
          description: Property. Number identifying a specific property on a public street    
          type: string    
      type: object    
      x-ngsi:    
        model: https://schema.org/address    
        type: Property    
    alternateName:    
      description: An alternative name for this item    
      type: string    
      x-ngsi:    
        type: Property    
    areaServed:    
      description: The geographic area where a service or offered item is provided    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    dataProvider:    
      description: A sequence of characters identifying the provider of the harmonised data entity    
      type: string    
      x-ngsi:    
        type: Property    
    dateCreated:    
      description: Entity creation timestamp. This will usually be allocated by the storage platform    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateModified:    
      description: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    description:    
      description: A description of this item    
      type: string    
      x-ngsi:    
        type: Property    
    id:    
      description: Unique entity identifier of the monitored machine tool, with the format urn:ngsi-ld:ElectrospindleObservation:<machineId>.    
      type: string    
      x-ngsi:    
        type: Property    
    location:    
      description: GeoProperty. Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon    
      oneOf:    
        - description: GeoProperty. Geojson reference to the item. Point    
          properties:    
            bbox:    
              description: Property. BBox of the  Point    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              description: Property. Coordinates of the Point    
              items:    
                type: number    
              minItems: 2    
              type: array    
            type:    
              enum:    
                - Point    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON Point    
          type: object    
        - description: GeoProperty. Geojson reference to the item. LineString    
          properties:    
            bbox:    
              description: Property. BBox coordinates of the LineString    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              description: Property. Coordinates of the LineString    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              minItems: 2    
              type: array    
            type:    
              enum:    
                - LineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON LineString    
          type: object    
        - description: GeoProperty. Geojson reference to the item. Polygon    
          properties:    
            bbox:    
              description: Property. BBox coordinates of the Polygon    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              description: Property. Coordinates of the Polygon    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 4    
                type: array    
              type: array    
            type:    
              enum:    
                - Polygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON Polygon    
          type: object    
        - description: GeoProperty. Geojson reference to the item. MultiPoint    
          properties:    
            bbox:    
              description: Property. BBox coordinates of the LineString    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              description: Property. Coordinates of the MulitPoint    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiPoint    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON MultiPoint    
          type: object    
        - description: GeoProperty. Geojson reference to the item. MultiLineString    
          properties:    
            bbox:    
              description: Property. BBox coordinates of the LineString    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              description: Property. Coordinates of the MultiLineString    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 2    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiLineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON MultiLineString    
          type: object    
        - description: GeoProperty. Geojson reference to the item. MultiLineString    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              description: Property. Coordinates of the MultiPolygon    
              items:    
                items:    
                  items:    
                    items:    
                      type: number    
                    minItems: 2    
                    type: array    
                  minItems: 4    
                  type: array    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiPolygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON MultiPolygon    
          type: object    
    name:    
      description: The name of this item    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)    
      items:    
        anyOf:    
          - description: Property. Identifier format of any NGSI entity    
            maxLength: 256    
            minLength: 1    
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
            type: string    
          - description: Property. Identifier format of any NGSI entity    
            format: uri    
            type: string    
        description: Relationship. Unique identifier of the entity    
      type: array    
      x-ngsi:    
        type: Property    
    seeAlso:    
      description: list of uri pointing to additional resources about the item    
      oneOf:    
        - items:    
            format: uri    
            type: string    
          minItems: 1    
          type: array    
        - format: uri    
          type: string    
      x-ngsi:    
        type: Property    
    source:    
      description: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object    
      type: string    
      x-ngsi:    
        type: Property    
    spindleBearingTemperature:    
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
      description: 'Expected unitCode: CEL. Temperature of the spindle bearings. This parameter is used to monitor the thermal load affecting the spindle bearing system and contributes to the definition of the bearing duty cycle. It supports the calculation of the residual lifetime of the spindle bearings and the prediction of suitable end-of-life R-strategies. Source field: T1.'    
      x-ngsi:    
        type: Property    
    spindleMotorCurrent:    
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
      description: 'Expected unitCode: AMP. Motor current of the spindle drive. This attribute is used to estimate the spindle motor torque and, consequently, the mechanical loads acting on the spindle bearings. These data contribute to the duty-cycle calculation of the spindle bearing system, supporting residual lifetime estimation and the prediction of suitable end-of-life R-strategies. Source field: IS.'    
      x-ngsi:    
        type: Property    
    spindleMotorTemperature:    
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
      description: 'Expected unitCode: CEL. Temperature of the electrospindle motor. This parameter is used to characterise the thermal operating conditions of the electrospindle and contributes to the definition of the component duty cycle. It supports the estimation of the residual lifetime of the electrospindle motor and the prediction of suitable end-of-life R-strategies. Source field: Te.'    
      x-ngsi:    
        type: Property    
    spindleSpeed:    
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
      description: 'Expected unitCode: RPM. Electrospindle rotational speed. This attribute is used to characterise the operating profile of the spindle and to determine the duty cycle of the spindle bearing system. Together with load-related and thermal information, it supports residual lifetime calculation and the prediction of suitable end-of-life R-strategies. Source field: VS.'    
      x-ngsi:    
        type: Property    
    type:    
      description: NGSI Entity type. It has to be ElectrospindleObservation    
      enum:    
        - ElectrospindleObservation    
      type: string    
      x-ngsi:    
        type: Property    
    xAxisMotorCurrent:    
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
      description: 'Expected unitCode: AMP. Motor current of the X-axis drive. This attribute is used to estimate the motor torque of the X-axis and, consequently, the mechanical forces transmitted to the X-axis ballscrew/nut system. These data contribute to the duty-cycle calculation of the X-axis ballscrew/nut assembly, supporting residual lifetime estimation and the prediction of suitable end-of-life R-strategies. Source field: IX.'    
      x-ngsi:    
        type: Property    
    xAxisMotorSpeed:    
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
      description: 'Expected unitCode: RPM. Motor rotational speed of the X-axis drive. This attribute is used to characterise the operating profile of the X-axis and to determine the duty cycle of the X-axis ballscrew/nut system. Together with load-related information, it supports residual lifetime calculation and the prediction of suitable end-of-life R-strategies. Source field: VX.'    
      x-ngsi:    
        type: Property    
    yAxisMotorCurrent:    
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
      description: 'Expected unitCode: AMP. Motor current of the Y-axis drive. This attribute is used to estimate the motor torque of the Y-axis and, consequently, the mechanical forces transmitted to the Y-axis ballscrew/nut system. These data contribute to the duty-cycle calculation of the Y-axis ballscrew/nut assembly, supporting residual lifetime estimation and the prediction of suitable end-of-life R-strategies. Source field: IY.'    
      x-ngsi:    
        type: Property    
    yAxisMotorSpeed:    
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
      description: 'Expected unitCode: RPM. Motor rotational speed of the Y-axis drive. This attribute is used to characterise the operating profile of the Y-axis and to determine the duty cycle of the Y-axis ballscrew/nut system. Together with load-related information, it supports residual lifetime calculation and the prediction of suitable end-of-life R-strategies. Source field: VY.'    
      x-ngsi:    
        type: Property    
    zAxisMotorCurrent:    
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
      description: 'Expected unitCode: AMP. Motor current of the Z-axis drive. This attribute is used to estimate the motor torque of the Z-axis and, consequently, the mechanical forces transmitted to the Z-axis ballscrew/nut system. These data contribute to the duty-cycle calculation of the Z-axis ballscrew/nut assembly, supporting residual lifetime estimation and the prediction of suitable end-of-life R-strategies. Source field: IZ.'    
      x-ngsi:    
        type: Property    
    zAxisMotorSpeed:    
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
      description: 'Expected unitCode: RPM. Motor rotational speed of the Z-axis drive. This attribute is used to characterise the operating profile of the Z-axis and to determine the duty cycle of the Z-axis ballscrew/nut system. Together with load-related information, it supports residual lifetime calculation and the prediction of suitable end-of-life R-strategies. Source field: VZ.'    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: ''    
  x-disclaimer: Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program    
  x-license-url: https://github.com/smart-data-models/circuloos_data_model/blob/master/ElectrospindleObservation/LICENSE.md    
  x-model-schema: https://raw.githubusercontent.com/european-dynamics-rnd/CIRCULOOS_Data_model/main/openCallSpecific/electrospindle_machine_iot/ElectrospindleObservation/schema.json    
  x-model-tags: electrospindle_machine_iot    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Example payloads    
Not available the example of a ElectrospindleObservation in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
#### ElectrospindleObservation NGSI-LD normalized Example    
Here is an example of a ElectrospindleObservation in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "@context": [  
    "http://circuloos-ld-context/circuloos-context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context-v1.8.jsonld"  
  ],  
  "id": "urn:ngsi-ld:ElectrospindleObservation:Reclaim:iot-001",  
  "type": "ElectrospindleObservation",  
  "spindleMotorTemperature": {  
    "type": "Property",  
    "value": 46.172063,  
    "unitCode": "CEL",  
    "observedAt": "2026-06-30T17:50:00.000Z"  
  },  
  "spindleBearingTemperature": {  
    "type": "Property",  
    "value": 43.234649,  
    "unitCode": "CEL",  
    "observedAt": "2026-06-30T17:50:00.000Z"  
  },  
  "xAxisMotorCurrent": {  
    "type": "Property",  
    "value": 1.435287,  
    "unitCode": "AMP",  
    "observedAt": "2026-06-30T17:50:00.000Z"  
  },  
  "yAxisMotorCurrent": {  
    "type": "Property",  
    "value": 1.706294,  
    "unitCode": "AMP",  
    "observedAt": "2026-06-30T17:50:00.000Z"  
  },  
  "zAxisMotorCurrent": {  
    "type": "Property",  
    "value": 2.208068,  
    "unitCode": "AMP",  
    "observedAt": "2026-06-30T17:50:00.000Z"  
  },  
  "spindleMotorCurrent": {  
    "type": "Property",  
    "value": 3.677316,  
    "unitCode": "AMP",  
    "observedAt": "2026-06-30T17:50:00.000Z"  
  },  
  "xAxisMotorSpeed": {  
    "type": "Property",  
    "value": 10.542505,  
    "unitCode": "RPM",  
    "observedAt": "2026-06-30T17:50:00.000Z"  
  },  
  "yAxisMotorSpeed": {  
    "type": "Property",  
    "value": 1.117344,  
    "unitCode": "RPM",  
    "observedAt": "2026-06-30T17:50:00.000Z"  
  },  
  "zAxisMotorSpeed": {  
    "type": "Property",  
    "value": 40.608215,  
    "unitCode": "RPM",  
    "observedAt": "2026-06-30T17:50:00.000Z"  
  },  
  "spindleSpeed": {  
    "type": "Property",  
    "value": 10254,  
    "unitCode": "RPM",  
    "observedAt": "2026-06-30T17:50:00.000Z"  
  }  
}  
```  
</details><!-- /80-Examples -->  
