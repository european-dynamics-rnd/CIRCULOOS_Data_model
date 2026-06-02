<!-- 10-Header -->  
Entity: leather  
===============<!-- /10-Header -->  
<!-- 15-License -->  
[Open License](https://github.com/smart-data-models//circuloos_data_model/blob/master/leather/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Global description: **CIRCULOOS data model for 3D printed concrete parts.**  
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
- `alternateName[string]`: An alternative name for this item  - `areaServed[string]`: The geographic area where a service or offered item is provided  . Model: [https://schema.org/Text](https://schema.org/Text)- `cementContent`:   	- `observedAt`:     
	- `type`:     
	- `unitCode`:     
	- `value`:     
- `color`:   	- `observedAt`:     
	- `type`:     
	- `value`:     
- `compressiveStrength`:   	- `observedAt`:     
	- `type`:     
	- `unitCode`:     
	- `value`:     
- `dataProvider[string]`: A sequence of characters identifying the provider of the harmonised data entity  - `dateCreated[date-time]`: Entity creation timestamp. This will usually be allocated by the storage platform  - `dateModified[date-time]`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform  - `density`:   	- `observedAt`:     
	- `type`:     
	- `unitCode`:     
	- `value`:     
- `description[string]`: A description of this item  - `energyUsage`:   	- `observedAt`:     
	- `type`:     
	- `unitCode`:     
	- `value`:     
- `fabricationTimestamp`:   	- `observedAt`:     
	- `type`:     
	- `value`:     
- `id[*]`: Unique identifier of the entity  - `location[*]`: GeoProperty. Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon  - `name[string]`: The name of this item  - `overallDimensions`:   	- `observedAt`:     
	- `type`:     
	- `unitCode`:     
	- `value`:     
- `owner[array]`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  - `partId`:   	- `observedAt`:     
	- `type`:     
	- `value`:     
- `printSpeed`:   	- `observedAt`:     
	- `type`:     
	- `unitCode`:     
	- `value`:     
- `realTimeCoordinates`:   	- `observedAt`:     
	- `type`:     
	- `unitCode`:     
	- `value`:     
- `realTimePressureSensorData`:   	- `observedAt`:     
	- `type`:     
	- `unitCode`:     
	- `value`:     
- `realTimeTemperatureSensorData`:   	- `observedAt`:     
	- `type`:     
	- `unitCode`:     
	- `value`:     
- `recycledContent`:   	- `observedAt`:     
	- `type`:     
	- `unitCode`:     
	- `value`:     
- `seeAlso[*]`: list of uri pointing to additional resources about the item  - `source[string]`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object  - `torqueData`:   	- `observedAt`:     
	- `type`:     
	- `unitCode`:     
	- `value`:     
- `type[string]`: NGSI Entity type. It has to be reConcretePart  - `waterUsage`:   	- `observedAt`:     
	- `type`:     
	- `unitCode`:     
	- `value`:     
- `weight`:   	- `observedAt`:     
	- `type`:     
	- `unitCode`:     
	- `value`:     
<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Required properties  
- `fabricationTimestamp`  - `id`  - `overallDimensions`  - `partId`  - `type`  - `weight`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Data Model description of properties  
Sorted alphabetically (click for details)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
leather:    
  description: CIRCULOOS data model for 3D printed concrete parts.    
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
    cementContent:    
      additionalProperties: no    
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
          minimum: 0    
          type: number    
      required:    
        - type    
        - value    
      type: object    
    color:    
      additionalProperties: no    
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
    compressiveStrength:    
      additionalProperties: no    
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
          minimum: 0    
          type: number    
      required:    
        - type    
        - value    
      type: object    
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
    density:    
      additionalProperties: no    
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
          minimum: 0    
          type: number    
      required:    
        - type    
        - value    
      type: object    
    description:    
      description: A description of this item    
      type: string    
      x-ngsi:    
        type: Property    
    energyUsage:    
      additionalProperties: no    
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
          minimum: 0    
          type: number    
      required:    
        - type    
        - value    
      type: object    
    fabricationTimestamp:    
      additionalProperties: no    
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
          type: string    
      required:    
        - type    
        - value    
      type: object    
    id:    
      anyOf:    
        - description: Property. Identifier format of any NGSI entity    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: Property. Identifier format of any NGSI entity    
          format: uri    
          type: string    
      description: Unique identifier of the entity    
      x-ngsi:    
        type: Relationship    
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
    overallDimensions:    
      additionalProperties: no    
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
          additionalProperties: no    
          properties:    
            height:    
              description: Property. Overall height of the part.    
              minimum: 0    
              type: number    
            length:    
              description: Property. Overall length of the part.    
              minimum: 0    
              type: number    
            width:    
              description: Property. Overall width of the part.    
              minimum: 0    
              type: number    
          required:    
            - length    
            - width    
            - height    
          type: object    
      required:    
        - type    
        - value    
      type: object    
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
    partId:    
      additionalProperties: no    
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
    printSpeed:    
      additionalProperties: no    
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
          minimum: 0    
          type: number    
      required:    
        - type    
        - value    
      type: object    
    realTimeCoordinates:    
      additionalProperties: no    
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
          additionalProperties: no    
          properties:    
            x:    
              description: Property. X-axis coordinates captured during manufacturing.    
              items:    
                type: number    
              minItems: 1    
              type: array    
            y:    
              description: Property. Y-axis coordinates captured during manufacturing.    
              items:    
                type: number    
              minItems: 1    
              type: array    
            z:    
              description: Property. Z-axis coordinates captured during manufacturing.    
              items:    
                type: number    
              minItems: 1    
              type: array    
          required:    
            - x    
            - y    
            - z    
          type: object    
      required:    
        - type    
        - value    
      type: object    
    realTimePressureSensorData:    
      additionalProperties: no    
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
          additionalProperties: no    
          properties:    
            values:    
              description: Property. Sensor values captured during manufacturing.    
              items:    
                type: number    
              minItems: 1    
              type: array    
          required:    
            - values    
          type: object    
      required:    
        - type    
        - value    
      type: object    
    realTimeTemperatureSensorData:    
      additionalProperties: no    
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
          additionalProperties: no    
          properties:    
            values:    
              description: Property. Sensor values captured during manufacturing.    
              items:    
                type: number    
              minItems: 1    
              type: array    
          required:    
            - values    
          type: object    
      required:    
        - type    
        - value    
      type: object    
    recycledContent:    
      additionalProperties: no    
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
          minimum: 0    
          type: number    
      required:    
        - type    
        - value    
      type: object    
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
    torqueData:    
      additionalProperties: no    
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
          additionalProperties: no    
          properties:    
            values:    
              description: Property. Sensor values captured during manufacturing.    
              items:    
                type: number    
              minItems: 1    
              type: array    
          required:    
            - values    
          type: object    
      required:    
        - type    
        - value    
      type: object    
    type:    
      description: NGSI Entity type. It has to be reConcretePart    
      enum:    
        - reConcretePart    
      type: string    
      x-ngsi:    
        type: Property    
    waterUsage:    
      additionalProperties: no    
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
          minimum: 0    
          type: number    
      required:    
        - type    
        - value    
      type: object    
    weight:    
      additionalProperties: no    
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
          minimum: 0    
          type: number    
      required:    
        - type    
        - value    
      type: object    
  required:    
    - id    
    - type    
    - partId    
    - fabricationTimestamp    
    - overallDimensions    
    - weight    
  type: object    
  x-derived-from: ''    
  x-disclaimer: Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program    
  x-license-url: https://github.com/smart-data-models/circuloos_data_model/blob/master/leather/LICENSE.md    
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
Not available the example of a leather in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
#### leather NGSI-LD normalized Example    
Here is an example of a leather in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:reConcretePart:sicurta-001",  
  "type": "reConcretePart",  
  "partId": {  
    "type": "Property",  
    "value": "sicurta-001"  
  },  
  "fabricationTimestamp": {  
    "type": "Property",  
    "value": "2026-05-20T10:30:00Z"  
  },  
  "density": {  
    "type": "Property",  
    "value": 2150,  
    "unitCode": "KMQ"  
  },  
  "weight": {  
    "type": "Property",  
    "value": 135.0,  
    "unitCode": "KGM"  
  },  
  "overallDimensions": {  
    "type": "Property",  
    "value": {  
      "length": 0.8,  
      "width": 1.2,  
      "height": 0.6  
    },  
    "unitCode": "MTR"  
  },  
  "realTimeCoordinates": {  
    "type": "Property",  
    "value": {  
      "x": [0.0, 0.2, 0.4, 0.6],  
      "y": [0.0, 0.1, 0.1, 0.2],  
      "z": [0.0, 0.05, 0.1, 0.15]  
    },  
    "unitCode": "MTR"  
  },  
  "realTimePressureSensorData": {  
    "type": "Property",  
    "value": {  
      "values": [2.1, 2.2, 2.0, 2.3]  
    },  
    "unitCode": "BAR"  
  },  
  "realTimeTemperatureSensorData": {  
    "type": "Property",  
    "value": {  
      "values": [23.5, 23.8, 24.0, 24.1]  
    },  
    "unitCode": "CEL"  
  },  
  "torqueData": {  
    "type": "Property",  
    "value": {  
      "values": [14.1, 14.3, 14.0, 14.2]  
    },  
    "unitCode": "NU"  
  },  
  "printSpeed": {  
    "type": "Property",  
    "value": 100,  
    "unitCode": "C16"  
  },  
  "energyUsage": {  
    "type": "Property",  
    "value": 4.0,  
    "unitCode": "KWH"  
  },  
  "waterUsage": {  
    "type": "Property",  
    "value": 9.4,  
    "unitCode": "LTR"  
  },  
  "compressiveStrength": {  
    "type": "Property",  
    "value": 38.2,  
    "unitCode": "MPA"  
  },  
  "cementContent": {  
    "type": "Property",  
    "value": 20.0,  
    "unitCode": "P1"  
  },  
  "recycledContent": {  
    "type": "Property",  
    "value": 46.5,  
    "unitCode": "P1"  
  },  
  "color": {  
    "type": "Property",  
    "value": "light grey"  
  },  
  "@context": [  
    "https://TOBELater/context.jsonld"  
  ]  
}  
```  
</details><!-- /80-Examples -->  
