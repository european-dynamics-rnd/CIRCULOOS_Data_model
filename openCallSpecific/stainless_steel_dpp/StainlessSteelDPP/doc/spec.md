<!-- 10-Header -->  
Entity: StainlessSteelDPP  
=========================<!-- /10-Header -->  
<!-- 15-License -->  
[Open License](https://raw.githubusercontent.com/european-dynamics-rnd/CIRCULOOS_Data_model/refs/heads/main/LICENSE)  
<!-- /15-License -->  
<!-- 20-Description -->  
Global description: **CIRCULOOS data model for the Digital Product Passport of a stainless steel product, covering product identification, production time window and the manufacturing route the product goes through.**  
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
- `alternateName[string]`: An alternative name for this item  - `areaServed[string]`: The geographic area where a service or offered item is provided  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: A sequence of characters identifying the provider of the harmonised data entity  - `dateCreated[date-time]`: Entity creation timestamp. This will usually be allocated by the storage platform  - `dateModified[date-time]`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform  - `description[string]`: A description of this item  - `dppId[*]`: Unique UUID of the Digital Product Passport of this product.  - `endTime[*]`: End time of the Digital Product Passport (ISO 8601 date-time, UTC).  - `factoryInternalBarcode[*]`: Product unique identifier (barcode) assigned at the factory.  - `id[string]`: Unique entity identifier, with the format urn:ngsi-ld:StainlessSteelDPP:<dppId>.  - `location[*]`: GeoProperty. Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon  - `name[string]`: The name of this item  - `owner[array]`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  - `productName[*]`: Commercial product name.  - `route[*]`: The processes the product goes through, each with its operation name, date, production status and energy consumption.  - `seeAlso[*]`: list of uri pointing to additional resources about the item  - `source[string]`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object  - `startTime[*]`: Start time of the Digital Product Passport (ISO 8601 date-time, UTC).  - `type[string]`: NGSI Entity type. It has to be StainlessSteelDPP  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Required properties  
- `dppId`  - `factoryInternalBarcode`  - `id`  - `productName`  - `route`  - `startTime`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Data Model description of properties  
Sorted alphabetically (click for details)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
StainlessSteelDPP:    
  description: CIRCULOOS data model for the Digital Product Passport of a stainless steel product, covering product identification, production time window and the manufacturing route the product goes through.    
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
    dppId:    
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
      description: Unique UUID of the Digital Product Passport of this product.    
      x-ngsi:    
        type: Property    
    endTime:    
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
      description: End time of the Digital Product Passport (ISO 8601 date-time, UTC).    
      x-ngsi:    
        type: Property    
    factoryInternalBarcode:    
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
      description: Product unique identifier (barcode) assigned at the factory.    
      x-ngsi:    
        type: Property    
    id:    
      description: Unique entity identifier, with the format urn:ngsi-ld:StainlessSteelDPP:<dppId>.    
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
    productName:    
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
      description: Commercial product name.    
      x-ngsi:    
        type: Property    
    route:    
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
              description: Property. Ordered list of the manufacturing operations the product goes through.    
              items:    
                additionalProperties: no    
                properties:    
                  date:    
                    description: Property. Date and time (ISO 8601, UTC) at which the operation was performed.    
                    format: date-time    
                    type: string    
                  energyConsumption:    
                    additionalProperties: no    
                    description: Property. Energy consumed for this route step.    
                    properties:    
                      unitCode:    
                        description: Property. UN/CEFACT code of the unit of the consumed energy, for example WHR (watt hour).    
                        type: string    
                      value:    
                        description: Property. Energy consumed by this route step.    
                        minimum: 0    
                        type: number    
                    required:    
                      - value    
                      - unitCode    
                    type: object    
                  operation:    
                    description: Property. Name of the manufacturing operation performed in this route step, for example Plastic Injection Molding, Metal Cutting or Assembly.    
                    type: string    
                  productionStatus:    
                    description: Property. Outcome of the operation as reported by the production line, for example OK.    
                    type: string    
                required:    
                  - operation    
                  - date    
                  - productionStatus    
                type: object    
              minItems: 1    
              type: array    
          required:    
            - type    
            - value    
          type: object    
      description: The processes the product goes through, each with its operation name, date, production status and energy consumption.    
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
    startTime:    
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
      description: Start time of the Digital Product Passport (ISO 8601 date-time, UTC).    
      x-ngsi:    
        type: Property    
    type:    
      description: NGSI Entity type. It has to be StainlessSteelDPP    
      enum:    
        - StainlessSteelDPP    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - dppId    
    - factoryInternalBarcode    
    - productName    
    - startTime    
    - route    
  type: object    
  x-derived-from: ''    
  x-disclaimer: Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program    
  x-license-url: https://github.com/smart-data-models/circuloos_data_model/blob/master/StainlessSteelDPP/LICENSE.md    
  x-model-schema: https://raw.githubusercontent.com/european-dynamics-rnd/CIRCULOOS_Data_model/main/openCallSpecific/stainless_steel_dpp/StainlessSteelDPP/schema.json    
  x-model-tags: stainless_steel_dpp    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Example payloads    
Not available the example of a StainlessSteelDPP in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
#### StainlessSteelDPP NGSI-LD normalized Example    
Here is an example of a StainlessSteelDPP in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "@context": [  
    "http://circuloos-ld-context/circuloos-context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context-v1.8.jsonld"  
  ],  
  "id": "urn:ngsi-ld:StainlessSteelDPP:6705c58b-dd1d-4087-b520-4ee3c3f71dc7",  
  "type": "StainlessSteelDPP",  
  "dppId": {  
    "type": "Property",  
    "value": "6705c58b-dd1d-4087-b520-4ee3c3f71dc7",  
    "observedAt": "2026-03-25T10:04:03.000Z"  
  },  
  "factoryInternalBarcode": {  
    "type": "Property",  
    "value": "100023659",  
    "observedAt": "2026-03-25T10:04:03.000Z"  
  },  
  "productName": {  
    "type": "Property",  
    "value": "MICRO VR N/A - 12(4) (90 CN) T150",  
    "observedAt": "2026-03-25T10:04:03.000Z"  
  },  
  "startTime": {  
    "type": "Property",  
    "value": "2025-03-13T14:50:00Z",  
    "observedAt": "2026-03-25T10:04:04.000Z"  
  },  
  "endTime": {  
    "type": "Property",  
    "value": "2025-03-13T14:55:00Z",  
    "observedAt": "2026-03-25T12:04:04.000Z"  
  },  
  "route": {  
    "type": "Property",  
    "value": [  
      {  
        "operation": "Plastic Injection Molding",  
        "date": "2025-03-13T14:50:00Z",  
        "productionStatus": "OK",  
        "energyConsumption": {  
          "value": 18.76,  
          "unitCode": "WHR"  
        }  
      },  
      {  
        "operation": "Metal Cutting",  
        "date": "2025-03-13T14:55:00Z",  
        "productionStatus": "OK",  
        "energyConsumption": {  
          "value": 1.87,  
          "unitCode": "WHR"  
        }  
      },  
      {  
        "operation": "Assembly",  
        "date": "2025-03-13T15:00:00Z",  
        "productionStatus": "OK",  
        "energyConsumption": {  
          "value": 0.93,  
          "unitCode": "WHR"  
        }  
      }  
    ],  
    "observedAt": "2026-03-25T12:04:04.000Z"  
  }  
}  
```  
</details><!-- /80-Examples -->  
