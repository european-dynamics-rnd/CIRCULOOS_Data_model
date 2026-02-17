<!-- 10-Header -->  
Entity: leather  
===============<!-- /10-Header -->  
<!-- 15-License -->  
[Open License](https://github.com/smart-data-models//circuloos_data_model/blob/master/leather/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Global description: **CIRCULOOS data model for intra-communication example-normalized.json**  
version: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## List of properties  

<sup><sub>[*] If there is not a type in an attribute is because it could have several types or different formats/patterns</sub></sup>  
- `CountryCode[object]`: Country code.  	- `observedAt`:     
	- `type`:     
	- `value`:     
- `address[object]`: The mailing address  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: Property. The country. For example, Spain. Model:'https://schema.org/addressCountry'    
	- `addressLocality[string]`: Property. The locality in which the street address is, and which is in the region. Model:'https://schema.org/addressLocality'    
	- `addressRegion[string]`: Property. The region in which the locality is, and which is in the country. Model:'https://schema.org/addressRegion'    
	- `district[string]`: Property. A district is a type of administrative division that, in some countries, is managed by the local government    
	- `postOfficeBoxNumber[string]`: Property. The post office box number for PO box addresses. For example, 03578. Model:'https://schema.org/postOfficeBoxNumber'    
	- `postalCode[string]`: Property. The postal code. For example, 24004. Model:'https://schema.org/https://schema.org/postalCode'    
	- `streetAddress[string]`: Property. The street address. Model:'https://schema.org/streetAddress'    
	- `streetNr[string]`: Property. Number identifying a specific property on a public street    
- `alternateName[string]`: An alternative name for this item  - `areaServed[string]`: The geographic area where a service or offered item is provided  . Model: [https://schema.org/Text](https://schema.org/Text)- `availableFrom[object]`: Date from which the material is available.  	- `observedAt`:     
	- `type`:     
	- `value`:     
- `dataProvider[string]`: A sequence of characters identifying the provider of the harmonised data entity  - `dateCreated[date-time]`: Entity creation timestamp. This will usually be allocated by the storage platform  - `dateModified[date-time]`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform  - `description[string]`: A description of this item  - `id[string]`: Unique identifier for the entity.  - `imageURL[object]`: URL of the material image.  	- `observedAt`:     
	- `type`:     
	- `value`:     
- `location[*]`: GeoProperty. Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon  - `materialAdStatus[object]`: Status of the advertisement.  	- `observedAt`:     
	- `type`:     
	- `value`:     
- `materialAdTitle[object]`: Title of the material advertisement.  	- `observedAt`:     
	- `type`:     
	- `value`:     
- `materialAdType[object]`: Type of advertisement: Sell or Buy.  	- `observedAt`:     
	- `type`:     
	- `value[string]`: Type of advertisement: Sell or Buy.    
- `materialDescription[object]`: Description of the material.  	- `observedAt`:     
	- `type`:     
	- `value`:     
- `materialPrice[object]`: Price of the material.  	- `observedAt`:     
	- `type`:     
	- `value`:     
- `materialQuantity[object]`: Quantity of the material.  	- `observedAt`:     
	- `type`:     
	- `unitCode`:     
	- `value`:     
- `materialToSellOrBuy[object]`: Material to sell or buy.  	- `observedAt`:     
	- `type`:     
	- `value`:     
- `materialTypeL0[object]`: Facility Input Categories, Level 0 material type.  	- `observedAt`:     
	- `type`:     
	- `value`:     
- `materialTypeL1[object]`: Facility Output Categories, Level 1 material type.  	- `observedAt`:     
	- `type`:     
	- `value`:     
- `name[string]`: The name of this item  - `ownedBy[object]`: Reference relationship: owner of the material.  	- `object`:     
	- `observedAt`:     
	- `type`:     
- `owner[array]`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  - `physicalFormCategory[object]`: To categorize materials based on their physical form: byWeight, byDimensions, bySurface.  	- `observedAt`:     
	- `type`:     
	- `value[string]`: Categorizes materials based on their physical form: byWeight, byDimensions, or bySurface.    
- `productionFacility[object]`: Reference relationship: production facility related to the material.  	- `object`:     
	- `observedAt`:     
	- `type`:     
- `seeAlso[*]`: list of uri pointing to additional resources about the item  - `source[string]`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object  - `type[string]`: NGSI Entity type.  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Required properties  
- `CountryCode`  - `availableFrom`  - `id`  - `imageURL`  - `materialAdStatus`  - `materialAdTitle`  - `materialAdType`  - `materialDescription`  - `materialPrice`  - `materialQuantity`  - `materialToSellOrBuy`  - `materialTypeL0`  - `materialTypeL1`  - `ownedBy`  - `physicalFormCategory`  - `productionFacility`  - `type`  <!-- /35-RequiredProperties -->  
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
  description: CIRCULOOS data model for intra-communication example-normalized.json    
  properties:    
    CountryCode:    
      description: Country code.    
      properties:    
        observedAt:    
          format: date-time    
          type: string    
        type:    
          type: string    
        value:    
          type: string    
      type: object    
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
    availableFrom:    
      description: Date from which the material is available.    
      properties:    
        observedAt:    
          format: date-time    
          type: string    
        type:    
          type: string    
        value:    
          format: date    
          type: string    
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
    description:    
      description: A description of this item    
      type: string    
      x-ngsi:    
        type: Property    
    id:    
      description: Unique identifier for the entity.    
      type: string    
    imageURL:    
      description: URL of the material image.    
      properties:    
        observedAt:    
          format: date-time    
          type: string    
        type:    
          type: string    
        value:    
          type: string    
      type: object    
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
    materialAdStatus:    
      description: Status of the advertisement.    
      properties:    
        observedAt:    
          format: date-time    
          type: string    
        type:    
          type: string    
        value:    
          type: string    
      type: object    
    materialAdTitle:    
      description: Title of the material advertisement.    
      properties:    
        observedAt:    
          format: date-time    
          type: string    
        type:    
          type: string    
        value:    
          type: string    
      type: object    
    materialAdType:    
      description: 'Type of advertisement: Sell or Buy.'    
      properties:    
        observedAt:    
          format: date-time    
          type: string    
        type:    
          type: string    
        value:    
          description: 'Type of advertisement: Sell or Buy.'    
          enum:    
            - Sell    
            - Buy    
          type: string    
      type: object    
    materialDescription:    
      description: Description of the material.    
      properties:    
        observedAt:    
          format: date-time    
          type: string    
        type:    
          type: string    
        value:    
          type: string    
      type: object    
    materialPrice:    
      description: Price of the material.    
      properties:    
        observedAt:    
          format: date-time    
          type: string    
        type:    
          type: string    
        value:    
          type: number    
      type: object    
    materialQuantity:    
      description: Quantity of the material.    
      properties:    
        observedAt:    
          format: date-time    
          type: string    
        type:    
          type: string    
        unitCode:    
          type: string    
        value:    
          type: number    
      type: object    
    materialToSellOrBuy:    
      description: Material to sell or buy.    
      properties:    
        observedAt:    
          format: date-time    
          type: string    
        type:    
          type: string    
        value:    
          type: string    
      type: object    
    materialTypeL0:    
      description: Facility Input Categories, Level 0 material type.    
      properties:    
        observedAt:    
          format: date-time    
          type: string    
        type:    
          type: string    
        value:    
          type: string    
      type: object    
    materialTypeL1:    
      description: Facility Output Categories, Level 1 material type.    
      properties:    
        observedAt:    
          format: date-time    
          type: string    
        type:    
          type: string    
        value:    
          type: string    
      type: object    
    name:    
      description: The name of this item    
      type: string    
      x-ngsi:    
        type: Property    
    ownedBy:    
      description: 'Reference relationship: owner of the material.'    
      properties:    
        object:    
          type: string    
        observedAt:    
          format: date-time    
          type: string    
        type:    
          type: string    
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
    physicalFormCategory:    
      description: 'To categorize materials based on their physical form: byWeight, byDimensions, bySurface.'    
      properties:    
        observedAt:    
          format: date-time    
          type: string    
        type:    
          type: string    
        value:    
          description: 'Categorizes materials based on their physical form: byWeight, byDimensions, or bySurface.'    
          enum:    
            - byWeight    
            - byDimensions    
            - bySurface    
          type: string    
      type: object    
    productionFacility:    
      description: 'Reference relationship: production facility related to the material.'    
      properties:    
        object:    
          type: string    
        observedAt:    
          format: date-time    
          type: string    
        type:    
          type: string    
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
    type:    
      description: NGSI Entity type.    
      type: string    
  required:    
    - id    
    - type    
    - materialAdTitle    
    - materialTypeL0    
    - materialTypeL1    
    - physicalFormCategory    
    - imageURL    
    - materialPrice    
    - availableFrom    
    - materialAdType    
    - materialDescription    
    - materialAdStatus    
    - materialQuantity    
    - ownedBy    
    - productionFacility    
    - materialToSellOrBuy    
    - CountryCode    
  type: object    
  x-derived-from: ''    
  x-disclaimer: Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program    
  x-license-url: https://github.com/smart-data-models/circuloos_data_model/blob/master/leather/LICENSE.md    
  x-model-schema: https://raw.githubusercontent.com/TO_ADD_LATER/intra-communication/example/schema.json    
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
Not available the example of a leather in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
<!-- /80-Examples -->  
