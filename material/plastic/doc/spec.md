<!-- 10-Header -->  
Entity: plastic  
===============<!-- /10-Header -->  
<!-- 15-License -->  
[Open License](https://raw.githubusercontent.com/european-dynamics-rnd/CIRCULOOS_Data_model/refs/heads/main/LICENSE)  
<!-- /15-License -->  
<!-- 20-Description -->  
Global description: **CIRCULOOS data model for raw plastic feedstock, covering the properties an injection molding factory needs to assess a batch before it goes into the hopper.**  
version: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## List of properties  

<sup><sub>[*] If there is not a type in an attribute is because it could have several types or different formats/patterns</sub></sup>  
- `additives[string]`: Free text list of additives present in the compound, e.g. UV stabilizer, flame retardant, colorant masterbatch.  - `address[object]`: The mailing address  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: Property. The country. For example, Spain. Model:'https://schema.org/addressCountry'    
	- `addressLocality[string]`: Property. The locality in which the street address is, and which is in the region. Model:'https://schema.org/addressLocality'    
	- `addressRegion[string]`: Property. The region in which the locality is, and which is in the country. Model:'https://schema.org/addressRegion'    
	- `district[string]`: Property. A district is a type of administrative division that, in some countries, is managed by the local government    
	- `postOfficeBoxNumber[string]`: Property. The post office box number for PO box addresses. For example, 03578. Model:'https://schema.org/postOfficeBoxNumber'    
	- `postalCode[string]`: Property. The postal code. For example, 24004. Model:'https://schema.org/https://schema.org/postalCode'    
	- `streetAddress[string]`: Property. The street address. Model:'https://schema.org/streetAddress'    
	- `streetNr[string]`: Property. Number identifying a specific property on a public street    
- `alternateName[string]`: An alternative name for this item  - `areaServed[string]`: The geographic area where a service or offered item is provided  . Model: [https://schema.org/Text](https://schema.org/Text)- `ashContent[object]`: Unit: %. Inorganic filler/ash content left after incineration, an indicator of filler load and purity.   	  
	- `value[number]`: Property. https://schema.org/Number.  Default: 0.0    
- `batchNumber[string]`: Supplier's lot/batch number, for traceability back to the source material.  - `bulkDensity[object]`: Unit: kg/m3. The density of the loose pellets/flakes as poured, needed to size the hopper and dosing.   	  
	- `value[number]`: Property. https://schema.org/Number.  Default: 0.0    
- `color[string]`: The color of the raw material.  - `contaminationLevel[string]`: Overall contamination level of the batch (foreign polymers, dirt, labels, etc.).  - `dataProvider[string]`: A sequence of characters identifying the provider of the harmonised data entity  - `dateCreated[date-time]`: Entity creation timestamp. This will usually be allocated by the storage platform  - `dateModified[date-time]`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform  - `density[object]`: Unit: g/cm3. The mass per unit volume of the solid resin.   	  
	- `value[number]`: Property. https://schema.org/Number.  Default: 0.0    
- `description[string]`: A description of this item  - `dryingRequired[boolean]`: Whether the material must be pre-dried before injection molding.  - `flexuralModulus[object]`: Unit: MPa. Stiffness of the molded material under bending.   	  
	- `value[number]`: Property. https://schema.org/Number.  Default: 0.0    
- `heatDeflectionTemperature[object]`: Unit: °C. Temperature at which the molded material deforms under a given load (HDT).   	  
	- `value[number]`: Property. https://schema.org/Number.  Default: 0.0    
- `id[*]`: Unique identifier of the entity  - `impactStrength[object]`: Unit: kJ/m2. Notched Izod impact strength of the molded material.   	  
	- `value[number]`: Property. https://schema.org/Number.  Default: 0.0    
- `location[*]`: GeoProperty. Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon  - `materialForm[string]`: The physical form the raw material is delivered in, which determines how it can be fed into the hopper.  - `meltFlowIndex[object]`: Unit: g/10min. Melt flow index (MFI/MFR), the key indicator of how easily the material flows into the mold cavity.   	  
	- `value[number]`: Property. https://schema.org/Number.  Default: 0.0    
- `meltingTemperature[object]`: Unit: °C. Melting (or processing) temperature of the resin.   	  
	- `value[number]`: Property. https://schema.org/Number.  Default: 0.0    
- `moistureContent[object]`: Unit: %. Residual moisture in the material; too high a value causes hydrolysis and surface defects if not dried before molding.   	  
	- `value[number]`: Property. https://schema.org/Number.  Default: 0.0    
- `name[string]`: The name of this item  - `origin[string]`: The source of the resin.  - `owner[array]`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  - `polymerType[string]`: The polymer resin the material is made of.  - `recommendedBarrelTemperature[object]`: Unit: °C. Recommended injection molding barrel temperature for this material.   	  
	- `value[number]`: Property. https://schema.org/Number.  Default: 0.0    
- `recommendedDryingTemperature[object]`: Unit: °C. Recommended drying temperature before processing.   	  
	- `value[number]`: Property. https://schema.org/Number.  Default: 0.0    
- `recommendedDryingTime[object]`: Unit: h. Recommended drying duration before processing.   	  
	- `value[number]`: Property. https://schema.org/Number.  Default: 0.0    
- `recommendedMoldTemperature[object]`: Unit: °C. Recommended mold (tool) temperature for this material.   	  
	- `value[number]`: Property. https://schema.org/Number.  Default: 0.0    
- `recycledContent[object]`: Unit: %. Share of recycled material in the batch.   	  
	- `value[number]`: Property. https://schema.org/Number. Default: 0.0    
- `recycledTimes[integer]`: The number of times this material has already been through a recycling loop.  - `seeAlso[*]`: list of uri pointing to additional resources about the item  - `shrinkageRate[object]`: Unit: %. Mold shrinkage of the material after cooling, needed to size the mold cavity.   	  
	- `value[number]`: Property. https://schema.org/Number.  Default: 0.0    
- `source[string]`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object  - `tensileStrength[object]`: Unit: MPa. The maximum stress the molded material can withstand while being stretched before breaking.   	  
	- `value[number]`: Property. https://schema.org/Number.  Default: 0.0    
- `type[*]`: NGSI Entity type. It has to be plastic  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Required properties  
- `id`  - `materialForm`  - `polymerType`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Data Model description of properties  
Sorted alphabetically (click for details)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
plastic:    
  description: CIRCULOOS data model for raw plastic feedstock, covering the properties an injection molding factory needs to assess a batch before it goes into the hopper.    
  properties:    
    additives:    
      description: Free text list of additives present in the compound, e.g. UV stabilizer, flame retardant, colorant masterbatch.    
      type: string    
      x-ngsi:    
        type: Property    
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
    ashContent:    
      description: 'Unit: %. Inorganic filler/ash content left after incineration, an indicator of filler load and purity. '    
      properties:    
        value:    
          description: 'Property. https://schema.org/Number.  Default: 0.0'    
          type: number    
      type: object    
      x-ngsi:    
        type: Property    
    batchNumber:    
      description: Supplier's lot/batch number, for traceability back to the source material.    
      type: string    
      x-ngsi:    
        type: Property    
    bulkDensity:    
      description: 'Unit: kg/m3. The density of the loose pellets/flakes as poured, needed to size the hopper and dosing. '    
      properties:    
        value:    
          description: 'Property. https://schema.org/Number.  Default: 0.0'    
          type: number    
      type: object    
      x-ngsi:    
        type: Property    
    color:    
      description: The color of the raw material.    
      type: string    
      x-ngsi:    
        type: Property    
    contaminationLevel:    
      description: Overall contamination level of the batch (foreign polymers, dirt, labels, etc.).    
      enum:    
        - low    
        - medium    
        - high    
      type: string    
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
      description: 'Unit: g/cm3. The mass per unit volume of the solid resin. '    
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
    dryingRequired:    
      description: Whether the material must be pre-dried before injection molding.    
      type: boolean    
      x-ngsi:    
        type: Property    
    flexuralModulus:    
      description: 'Unit: MPa. Stiffness of the molded material under bending. '    
      properties:    
        value:    
          description: 'Property. https://schema.org/Number.  Default: 0.0'    
          type: number    
      type: object    
      x-ngsi:    
        type: Property    
    heatDeflectionTemperature:    
      description: 'Unit: °C. Temperature at which the molded material deforms under a given load (HDT). '    
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
        type: Relationship    
    impactStrength:    
      description: 'Unit: kJ/m2. Notched Izod impact strength of the molded material. '    
      properties:    
        value:    
          description: 'Property. https://schema.org/Number.  Default: 0.0'    
          type: number    
      type: object    
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
    materialForm:    
      description: The physical form the raw material is delivered in, which determines how it can be fed into the hopper.    
      enum:    
        - pellet    
        - granulate    
        - regrind    
        - flake    
        - powder    
      type: string    
      x-ngsi:    
        type: Property    
    meltFlowIndex:    
      description: 'Unit: g/10min. Melt flow index (MFI/MFR), the key indicator of how easily the material flows into the mold cavity. '    
      properties:    
        value:    
          description: 'Property. https://schema.org/Number.  Default: 0.0'    
          type: number    
      type: object    
      x-ngsi:    
        type: Property    
    meltingTemperature:    
      description: 'Unit: °C. Melting (or processing) temperature of the resin. '    
      properties:    
        value:    
          description: 'Property. https://schema.org/Number.  Default: 0.0'    
          type: number    
      type: object    
      x-ngsi:    
        type: Property    
    moistureContent:    
      description: 'Unit: %. Residual moisture in the material; too high a value causes hydrolysis and surface defects if not dried before molding. '    
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
    origin:    
      description: The source of the resin.    
      enum:    
        - virgin    
        - post-industrial recycled    
        - post-consumer recycled    
        - mixed    
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
    polymerType:    
      description: The polymer resin the material is made of.    
      enum:    
        - PP    
        - HDPE    
        - LDPE    
        - PET    
        - PS    
        - ABS    
        - PVC    
        - PC    
        - PA    
        - PLA    
        - other    
      type: string    
      x-ngsi:    
        type: Property    
    recommendedBarrelTemperature:    
      description: 'Unit: °C. Recommended injection molding barrel temperature for this material. '    
      properties:    
        value:    
          description: 'Property. https://schema.org/Number.  Default: 0.0'    
          type: number    
      type: object    
      x-ngsi:    
        type: Property    
    recommendedDryingTemperature:    
      description: 'Unit: °C. Recommended drying temperature before processing. '    
      properties:    
        value:    
          description: 'Property. https://schema.org/Number.  Default: 0.0'    
          type: number    
      type: object    
      x-ngsi:    
        type: Property    
    recommendedDryingTime:    
      description: 'Unit: h. Recommended drying duration before processing. '    
      properties:    
        value:    
          description: 'Property. https://schema.org/Number.  Default: 0.0'    
          type: number    
      type: object    
      x-ngsi:    
        type: Property    
    recommendedMoldTemperature:    
      description: 'Unit: °C. Recommended mold (tool) temperature for this material. '    
      properties:    
        value:    
          description: 'Property. https://schema.org/Number.  Default: 0.0'    
          type: number    
      type: object    
      x-ngsi:    
        type: Property    
    recycledContent:    
      description: 'Unit: %. Share of recycled material in the batch. '    
      properties:    
        value:    
          description: 'Property. https://schema.org/Number. Default: 0.0'    
          type: number    
      type: object    
      x-ngsi:    
        type: Property    
    recycledTimes:    
      description: The number of times this material has already been through a recycling loop.    
      minimum: 0    
      type: integer    
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
    shrinkageRate:    
      description: 'Unit: %. Mold shrinkage of the material after cooling, needed to size the mold cavity. '    
      properties:    
        value:    
          description: 'Property. https://schema.org/Number.  Default: 0.0'    
          type: number    
      type: object    
      x-ngsi:    
        type: Property    
    source:    
      description: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object    
      type: string    
      x-ngsi:    
        type: Property    
    tensileStrength:    
      description: 'Unit: MPa. The maximum stress the molded material can withstand while being stretched before breaking. '    
      properties:    
        value:    
          description: 'Property. https://schema.org/Number.  Default: 0.0'    
          type: number    
      type: object    
      x-ngsi:    
        type: Property    
    type:    
      description: NGSI Entity type. It has to be plastic    
      enum:    
        - plastic    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - polymerType    
    - materialForm    
  type: object    
  x-derived-from: ''    
  x-disclaimer: Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program    
  x-license-url: https://github.com/smart-data-models/circuloos_data_model/blob/master/plastic/LICENSE.md    
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
Not available the example of a plastic in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
#### plastic NGSI-LD normalized Example    
Here is an example of a plastic in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:plastic:PPR2044",  
    "type": "plastic",  
    "polymerType": {  
        "type": "Property",  
        "value": "PP"  
    },  
    "materialForm": {  
        "type": "Property",  
        "value": "pellet"  
    },  
    "origin": {  
        "type": "Property",  
        "value": "post-industrial recycled"  
    },  
    "recycledContent": {  
        "type": "Property",  
        "value": "85",  
        "unitCode": "P1"  
    },  
    "recycledTimes": {  
        "type": "Property",  
        "value": "2"  
    },  
    "color": {  
        "type": "Property",  
        "value": "natural"  
    },  
    "density": {  
        "type": "Property",  
        "value": "0.91",  
        "unitCode": "23"  
    },  
    "bulkDensity": {  
        "type": "Property",  
        "value": "550",  
        "unitCode": "KMQ"  
    },  
    "meltFlowIndex": {  
        "type": "Property",  
        "value": "12"  
    },  
    "moistureContent": {  
        "type": "Property",  
        "value": "0.08",  
        "unitCode": "P1"  
    },  
    "dryingRequired": {  
        "type": "Property",  
        "value": "true"  
    },  
    "recommendedDryingTemperature": {  
        "type": "Property",  
        "value": "80",  
        "unitCode": "CEL"  
    },  
    "recommendedDryingTime": {  
        "type": "Property",  
        "value": "2",  
        "unitCode": "HUR"  
    },  
    "meltingTemperature": {  
        "type": "Property",  
        "value": "165",  
        "unitCode": "CEL"  
    },  
    "recommendedBarrelTemperature": {  
        "type": "Property",  
        "value": "220",  
        "unitCode": "CEL"  
    },  
    "recommendedMoldTemperature": {  
        "type": "Property",  
        "value": "40",  
        "unitCode": "CEL"  
    },  
    "shrinkageRate": {  
        "type": "Property",  
        "value": "1.5",  
        "unitCode": "P1"  
    },  
    "tensileStrength": {  
        "type": "Property",  
        "value": "28",  
        "unitCode": "MPA"  
    },  
    "flexuralModulus": {  
        "type": "Property",  
        "value": "1350",  
        "unitCode": "MPA"  
    },  
    "impactStrength": {  
        "type": "Property",  
        "value": "5.5"  
    },  
    "heatDeflectionTemperature": {  
        "type": "Property",  
        "value": "85",  
        "unitCode": "CEL"  
    },  
    "ashContent": {  
        "type": "Property",  
        "value": "0.4",  
        "unitCode": "P1"  
    },  
    "contaminationLevel": {  
        "type": "Property",  
        "value": "low"  
    },  
    "additives": {  
        "type": "Property",  
        "value": "UV stabilizer, antioxidant masterbatch"  
    },  
    "batchNumber": {  
        "type": "Property",  
        "value": "LOT-2026-0417"  
    },  
    "@context": [  
        "https://TOBELater/context.jsonld"  
    ]  
}  
```  
</details><!-- /80-Examples -->  
