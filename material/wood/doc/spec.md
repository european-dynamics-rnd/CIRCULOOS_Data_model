<!-- 10-Header -->  
Entity: leather  
===============<!-- /10-Header -->  
<!-- 15-License -->  
[Open License](https://github.com/smart-data-models//circuloos_data_model/blob/master/leather/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Global description: **CIRCULOOS data model for wood**  
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
- `alternateName[string]`: An alternative name for this item  - `areaServed[string]`: The geographic area where a service or offered item is provided  . Model: [https://schema.org/Text](https://schema.org/Text)- `bendingStrength[object]`: The maximum stress the wood can withstand before breaking when subjected to a bending force.   	  
	- `value[number]`: Property. https://schema.org/Number.  Default: 0.0    
- `compressiveStrength[object]`: The maximum compressive force that wood can withstand.   	  
	- `value[number]`: Property. https://schema.org/Number.  Default: 0.0    
- `dataProvider[string]`: A sequence of characters identifying the provider of the harmonised data entity  - `dateCreated[date-time]`: Entity creation timestamp. This will usually be allocated by the storage platform  - `dateModified[date-time]`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform  - `density[object]`: The mass per unit volume of the wood, critical for calculating weight and structural integrity.   	  
	- `value[number]`: Property. https://schema.org/Number.  Default: 0.0    
- `description[string]`: A description of this item  - `flameSpreadIndex[object]`: A measure of the material’s propensity to burn and spread flames, important for fire safety considerations. ASTM E84   	  
	- `value[number]`: Property. https://schema.org/Number.  Default: 0.0    
- `hardness[object]`:  The resistance of the wood to indentation or scratching, important for wear and durability.   	  
	- `value[number]`: Property. https://schema.org/Number.  Default: 0.0    
- `id[*]`: Unique identifier of the entity  - `location[*]`: GeoProperty. Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon  - `modulusOfElasticity[object]`: The measure of the wood's stiffness, indicating how much it will deform under stress.   	  
	- `value[number]`: Property. https://schema.org/Number.  Default: 0.0    
- `moistureContent[object]`: The amount of moisture in the wood, affecting its dimensional stability and strength.   	  
	- `value[number]`: Property. https://schema.org/Number.  Default: 0.0    
- `name[string]`: The name of this item  - `opticalProperties-color[object]`: Characteristics related to appearance.   	  
	- `value[string]`: Property. https://schema.org/Number.  Default: 0.0    
- `opticalProperties-grainPattern[object]`: Characteristics related to appearance.   	  
	- `value[string]`: Property. https://schema.org/Number.  Default: 0.0    
- `owner[array]`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  - `seeAlso[*]`: list of uri pointing to additional resources about the item  - `source[string]`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object  - `species[string]`: The type of wood (e.g., Oak, Pine, Birch).   - `tensileStrength[object]`: he maximum stress that the wood can withstand while being stretched before breaking.   	  
	- `value[number]`: Property. https://schema.org/Number.  Default: 0.0    
- `thermalConductivity[object]`: The rate at which heat passes through the wood, important for thermal insulation applications.   	  
	- `value[number]`: Property. https://schema.org/Number.  Default: 0.0    
- `thermalExpansionCoefficient[object]`: The rate at which the wood expands with temperature, critical in applications involving temperature changes.   	  
	- `value[number]`: Property. https://schema.org/Number.  Default: 0.0    
- `type[*]`: NGSI Entity type. It has to be wood  - `waterAbsorption[object]`: The amount of water absorbed by the wood over a specified period, influencing dimensional stability and strength.   	  
	- `value[number]`: Property. https://schema.org/Number.  Default: 0.0    
<!-- /30-PropertiesList -->  
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
leather:    
  description: CIRCULOOS data model for wood    
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
    bendingStrength:    
      description: 'The maximum stress the wood can withstand before breaking when subjected to a bending force. '    
      properties:    
        value:    
          description: 'Property. https://schema.org/Number.  Default: 0.0'    
          type: number    
      type: object    
      x-ngsi:    
        type: Property    
    compressiveStrength:    
      description: 'The maximum compressive force that wood can withstand. '    
      properties:    
        value:    
          description: 'Property. https://schema.org/Number.  Default: 0.0'    
          type: number    
      type: object    
      x-ngsi:    
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
    density:    
      description: 'The mass per unit volume of the wood, critical for calculating weight and structural integrity. '    
      properties:    
        value:    
          description: 'Property. https://schema.org/Number.  Default: 0.0'    
          type: number    
      type: object    
      x-ngsi:    
        type: Property    
    description:    
      description: A description of this item    
      type: string    
      x-ngsi:    
        type: Property    
    flameSpreadIndex:    
      description: 'A measure of the material’s propensity to burn and spread flames, important for fire safety considerations. ASTM E84 '    
      properties:    
        value:    
          description: 'Property. https://schema.org/Number.  Default: 0.0'    
          type: number    
      type: object    
      x-ngsi:    
        type: Property    
    hardness:    
      description: ' The resistance of the wood to indentation or scratching, important for wear and durability. '    
      properties:    
        value:    
          description: 'Property. https://schema.org/Number.  Default: 0.0'    
          type: number    
      type: object    
      x-ngsi:    
        type: Property    
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
        type: Property    
    location:    
      description: GeoProperty. Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon    
      oneOf:    
        - description: GeoProperty. Geojson reference to the item. Point    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
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
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
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
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
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
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
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
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
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
    modulusOfElasticity:    
      description: 'The measure of the wood''s stiffness, indicating how much it will deform under stress. '    
      properties:    
        value:    
          description: 'Property. https://schema.org/Number.  Default: 0.0'    
          type: number    
      type: object    
      x-ngsi:    
        type: Property    
    moistureContent:    
      description: 'The amount of moisture in the wood, affecting its dimensional stability and strength. '    
      properties:    
        value:    
          description: 'Property. https://schema.org/Number.  Default: 0.0'    
          type: number    
      type: object    
      x-ngsi:    
        type: Property    
    name:    
      description: The name of this item    
      type: string    
      x-ngsi:    
        type: Property    
    opticalProperties-color:    
      description: 'Characteristics related to appearance. '    
      properties:    
        value:    
          description: 'Property. https://schema.org/Number.  Default: 0.0'    
          type: string    
      type: object    
      x-ngsi:    
        type: Property    
    opticalProperties-grainPattern:    
      description: 'Characteristics related to appearance. '    
      properties:    
        value:    
          description: 'Property. https://schema.org/Number.  Default: 0.0'    
          type: string    
      type: object    
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
        description: Property. Unique identifier of the entity    
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
    species:    
      description: 'The type of wood (e.g., Oak, Pine, Birch). '    
      type: string    
      x-ngsi:    
        type: Property    
    tensileStrength:    
      description: 'he maximum stress that the wood can withstand while being stretched before breaking. '    
      properties:    
        value:    
          description: 'Property. https://schema.org/Number.  Default: 0.0'    
          type: number    
      type: object    
      x-ngsi:    
        type: Property    
    thermalConductivity:    
      description: 'The rate at which heat passes through the wood, important for thermal insulation applications. '    
      properties:    
        value:    
          description: 'Property. https://schema.org/Number.  Default: 0.0'    
          type: number    
      type: object    
      x-ngsi:    
        type: Property    
    thermalExpansionCoefficient:    
      description: 'The rate at which the wood expands with temperature, critical in applications involving temperature changes. '    
      properties:    
        value:    
          description: 'Property. https://schema.org/Number.  Default: 0.0'    
          type: number    
      type: object    
      x-ngsi:    
        type: Property    
    type:    
      description: NGSI Entity type. It has to be wood    
      enum:    
        - wood    
      x-ngsi:    
        type: Property    
    waterAbsorption:    
      description: 'The amount of water absorbed by the wood over a specified period, influencing dimensional stability and strength. '    
      properties:    
        value:    
          description: 'Property. https://schema.org/Number.  Default: 0.0'    
          type: number    
      type: object    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
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
    "id": "ngsi-ld:wood:wood1",  
    "type": "wood",  
    "species": "Oak",  
    "density": {  
        "type": "Number",  
        "value": "0.75",  
        "unitCode": "23"  
    },  
    "moistureContent": {  
        "type": "Number",  
        "value": "12",  
        "unitCode": "P1"  
    },  
    "tensileStrength": {  
        "type": "Number",  
        "value": "90",  
        "unitCode": "MPA"  
    },  
    "compressiveStrength": {  
        "type": "Number",  
        "value": "50",  
        "unitCode": "MPA"  
    },  
    "bendingStrength": {  
        "type": "Number",  
        "value": "120",  
        "unitCode": "MPA"  
    },  
    "modulusOfElasticity": {  
        "type": "Number",  
        "value": "11000",  
        "unitCode": "MPA"  
    },  
    "hardness": {  
        "type": "Number",  
        "value": "670",  
        "unitCode": "NEW"  
    },  
    "thermalConductivity": {  
        "type": "Number",  
        "value": "0.16",  
        "unitCode": "D53"  
    },  
    "thermalExpansionCoefficient": {  
        "type": "Number",  
        "value": "3.5",  
        "unitCode": "F51"  
    },  
    "waterAbsorption": {  
        "type": "Number",  
        "value": "40",  
        "unitCode": "P1"  
    },  
    "flameSpreadIndex": {  
        "type": "Number",  
        "value": "100"  
    },  
    "opticalProperties-color": {  
        "type": "String",  
        "value": "Light Brown"  
    },  
    "opticalProperties-grainPattern": {  
        "type": "String",  
        "value": "Straight"  
    }  
}  
```  
</details><!-- /80-Examples -->  
