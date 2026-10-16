<!-- 10-Header -->  
Entity: leather  
===============<!-- /10-Header -->  
<!-- 15-License -->  
[Open License](https://raw.githubusercontent.com/european-dynamics-rnd/CIRCULOOS_Data_model/refs/heads/main/LICENSE)  
<!-- /15-License -->  
<!-- 20-Description -->  
Global description: **Representing leather material for the CIRCULOOS project**  
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
- `alternateName[string]`: An alternative name for this item  - `area[object]`: Unit: given by unitCode, MTK (m2) or FTK (ft2, the usual leather trade unit). Usable surface area of the leather.   	  
	- `value[number]`: Property. https://schema.org/Number.    
- `areaServed[string]`: The geographic area where a service or offered item is provided  . Model: [https://schema.org/Text](https://schema.org/Text)- `batchNumber[string]`: Lot/batch number of this quantity of material, for traceability back to its source.  - `biobasedContent[object]`: Unit: %. Share of the material derived from biomass (EN 16785-1).  	  
	- `value[number]`: Property. https://schema.org/Number.    
- `certifications[array]`: Certificates covering this material.  - `chainOfCustodyModel[string]`: Chain of custody model (ISO 22095) behind the recycled or bio-based content claims of this material.  - `color[string]`: The final color of the leather.  - `composition[array]`: Main components of the material and their mass shares.  - `contaminationLevel[string]`: Overall contamination level of the lot (foreign materials, dirt, labels, etc.).  - `dataProvider[string]`: A sequence of characters identifying the provider of the harmonised data entity  - `dateCreated[date-time]`: Entity creation timestamp. This will usually be allocated by the storage platform  - `dateModified[date-time]`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform  - `description[string]`: A description of this item  - `endOfWasteReference[string]`: The end-of-waste criteria (EU or national regulation, permit) under which the material stopped being waste.  - `hardness[string]`: Overall hardness of the leather  - `hazardous[boolean]`: Whether the material is classified as hazardous.  - `id[*]`: Unique identifier of the entity  - `leatherCut[string]`: The cut or surface of the leather: grain side, split, nubuck, suede or fur.  - `location[*]`: GeoProperty. Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon  - `materialSource[string]`: Where the leather comes from in the value chain: cutting offcuts, tannery production scrap (shavings, trimmings), used products, or unsold stock.  - `materialStatus[string]`: Legal status of the material under the EU Waste Framework Directive 2008/98/EC: primary (virgin) material, by-product (Art. 5), waste, or material that has reached end-of-waste status (Art. 6). Receiving waste needs a waste permit.  - `name[string]`: The name of this item  - `origin[string]`: The source that the leather was originated  - `owner[array]`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  - `pieceFormat[string]`: Shape of the piece: a full hide, a standard cut of it, or an irregular offcut.  - `postConsumerRecycledContent[object]`: Unit: %. Share of recycled material recovered from products after their use (ISO 14021). The share counted by recycled content targets such as the PPWR, Regulation (EU) 2025/40.  	  
	- `value[number]`: Property. https://schema.org/Number.    
- `preConsumerRecycledContent[object]`: Unit: %. Share of recycled material recovered from manufacturing scrap, before reaching a consumer (ISO 14021).  	  
	- `value[number]`: Property. https://schema.org/Number.    
- `qualityStandard[string]`: Standard the material is characterised or traced against, e.g. EN 15343 (traceability of recycled plastics) or EN 15345 (PP recyclates).  - `quantity[object]`: Unit: given by unitCode, e.g. KGM (kg), TNE (t), MTQ (m3), MTK (m2), C62 (pieces). Quantity of material in this lot.  	  
	- `value[number]`: Property. https://schema.org/Number.    
- `recycledContent[object]`: Unit: %. Total share of recycled material (ISO 14021).  	  
	- `value[number]`: Property. https://schema.org/Number.    
- `recycledTimes[integer]`: The number of times this material has already been through a recycling loop.  - `refDigitalProductPassport[uri]`: Digital Product Passport (EU ESPR, Regulation (EU) 2024/1781) of the product this material comes from or belongs to.  - `refEnvironmentalFootprint[uri]`: environmental_footprint_indicator entity holding the environmental footprint (LCA indicators) of this material.  - `refParentMaterial[array]`: Material entities (lots) this material was produced from. Following the links back gives the material loop history.  - `refProcess[uri]`: Process or process event entity that produced this material.  - `seeAlso[*]`: list of uri pointing to additional resources about the item  - `source[string]`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object  - `substancesOfConcern[array]`: Substances of concern present in the material, as required by the EU ESPR Digital Product Passport.  - `suitableRecoveryRoutes[array]`: Circular strategies (R-ladder) the material is suitable for. Used to match offers with demand.  - `surfaceFinishWithCovering[boolean]`: Leather finished (with covering) or not finished  - `tannedProcess[string]`: The tanning process used. chromeFree covers wet-white leather.  - `thickness[object]`: Unit: mm. The thickness of the leather.   	  
	- `value[number]`: Property. https://schema.org/Number.    
- `type[string]`: NGSI Entity type. It has to be leather  - `wasteCode[string]`: European List of Waste code (Commission Decision 2000/532/EC), e.g. 07 02 13 for waste plastic. A trailing * marks hazardous waste. Only when materialStatus is waste.  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Required properties  
- `area`  - `color`  - `id`  - `type`  <!-- /35-RequiredProperties -->  
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
  description: Representing leather material for the CIRCULOOS project    
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
    area:    
      description: 'Unit: given by unitCode, MTK (m2) or FTK (ft2, the usual leather trade unit). Usable surface area of the leather. '    
      properties:    
        value:    
          description: Property. https://schema.org/Number.    
          minimum: 0    
          type: number    
      type: object    
      x-ngsi:    
        type: Property    
    areaServed:    
      description: The geographic area where a service or offered item is provided    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    batchNumber:    
      description: Lot/batch number of this quantity of material, for traceability back to its source.    
      type: string    
      x-ngsi:    
        type: Property    
    biobasedContent:    
      description: 'Unit: %. Share of the material derived from biomass (EN 16785-1).'    
      properties:    
        value:    
          description: Property. https://schema.org/Number.    
          maximum: 100    
          minimum: 0    
          type: number    
      type: object    
      x-ngsi:    
        type: Property    
    certifications:    
      description: Certificates covering this material.    
      items:    
        properties:    
          certificateId:    
            description: Property. Certificate number.    
            type: string    
          issuer:    
            description: Property. Certification body that issued the certificate.    
            type: string    
          scheme:    
            description: Property. Certification scheme, e.g. ISCC PLUS, EuCertPlast, RecyClass, GRS, FSC, PEFC, LWG.    
            type: string    
          validUntil:    
            description: Property. Expiry date of the certificate.    
            format: date    
            type: string    
        required:    
          - scheme    
        type: object    
      type: array    
      x-ngsi:    
        type: Property    
    chainOfCustodyModel:    
      description: Chain of custody model (ISO 22095) behind the recycled or bio-based content claims of this material.    
      enum:    
        - identityPreserved    
        - segregated    
        - controlledBlending    
        - massBalance    
        - bookAndClaim    
      type: string    
      x-ngsi:    
        type: Property    
    color:    
      description: The final color of the leather.    
      type: string    
      x-ngsi:    
        type: Property    
    composition:    
      description: Main components of the material and their mass shares.    
      items:    
        properties:    
          casNumber:    
            description: Property. CAS registry number of the component, when it has one.    
            type: string    
          name:    
            description: Property. Name of the component.    
            type: string    
          share:    
            description: 'Property. Unit: %. Mass share of the component in the material.'    
            maximum: 100    
            minimum: 0    
            type: number    
        required:    
          - name    
        type: object    
      type: array    
      x-ngsi:    
        type: Property    
    contaminationLevel:    
      description: Overall contamination level of the lot (foreign materials, dirt, labels, etc.).    
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
    description:    
      description: A description of this item    
      type: string    
      x-ngsi:    
        type: Property    
    endOfWasteReference:    
      description: The end-of-waste criteria (EU or national regulation, permit) under which the material stopped being waste.    
      type: string    
      x-ngsi:    
        type: Property    
    hardness:    
      description: Overall hardness of the leather    
      enum:    
        - soft    
        - medium    
        - hard    
      type: string    
      x-ngsi:    
        type: Property    
    hazardous:    
      description: Whether the material is classified as hazardous.    
      type: boolean    
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
    leatherCut:    
      description: 'The cut or surface of the leather: grain side, split, nubuck, suede or fur.'    
      enum:    
        - grainside    
        - split    
        - nubuck    
        - suede    
        - furs    
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
    materialSource:    
      description: 'Where the leather comes from in the value chain: cutting offcuts, tannery production scrap (shavings, trimmings), used products, or unsold stock.'    
      enum:    
        - preConsumerOffcut    
        - productionScrap    
        - postConsumer    
        - deadstock    
      type: string    
      x-ngsi:    
        type: Property    
    materialStatus:    
      description: 'Legal status of the material under the EU Waste Framework Directive 2008/98/EC: primary (virgin) material, by-product (Art. 5), waste, or material that has reached end-of-waste status (Art. 6). Receiving waste needs a waste permit.'    
      enum:    
        - primary    
        - byProduct    
        - waste    
        - endOfWaste    
      type: string    
      x-ngsi:    
        type: Property    
    name:    
      description: The name of this item    
      type: string    
      x-ngsi:    
        type: Property    
    origin:    
      description: The source that the leather was originated    
      enum:    
        - cow    
        - pig    
        - horse    
        - other animals    
        - vegan    
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
    pieceFormat:    
      description: 'Shape of the piece: a full hide, a standard cut of it, or an irregular offcut.'    
      enum:    
        - fullHide    
        - side    
        - bend    
        - shoulder    
        - belly    
        - offcut    
      type: string    
      x-ngsi:    
        type: Property    
    postConsumerRecycledContent:    
      description: 'Unit: %. Share of recycled material recovered from products after their use (ISO 14021). The share counted by recycled content targets such as the PPWR, Regulation (EU) 2025/40.'    
      properties:    
        value:    
          description: Property. https://schema.org/Number.    
          maximum: 100    
          minimum: 0    
          type: number    
      type: object    
      x-ngsi:    
        type: Property    
    preConsumerRecycledContent:    
      description: 'Unit: %. Share of recycled material recovered from manufacturing scrap, before reaching a consumer (ISO 14021).'    
      properties:    
        value:    
          description: Property. https://schema.org/Number.    
          maximum: 100    
          minimum: 0    
          type: number    
      type: object    
      x-ngsi:    
        type: Property    
    qualityStandard:    
      description: Standard the material is characterised or traced against, e.g. EN 15343 (traceability of recycled plastics) or EN 15345 (PP recyclates).    
      type: string    
      x-ngsi:    
        type: Property    
    quantity:    
      description: 'Unit: given by unitCode, e.g. KGM (kg), TNE (t), MTQ (m3), MTK (m2), C62 (pieces). Quantity of material in this lot.'    
      properties:    
        value:    
          description: Property. https://schema.org/Number.    
          minimum: 0    
          type: number    
      type: object    
      x-ngsi:    
        type: Property    
    recycledContent:    
      description: 'Unit: %. Total share of recycled material (ISO 14021).'    
      properties:    
        value:    
          description: Property. https://schema.org/Number.    
          maximum: 100    
          minimum: 0    
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
    refDigitalProductPassport:    
      description: Digital Product Passport (EU ESPR, Regulation (EU) 2024/1781) of the product this material comes from or belongs to.    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
    refEnvironmentalFootprint:    
      description: environmental_footprint_indicator entity holding the environmental footprint (LCA indicators) of this material.    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
    refParentMaterial:    
      description: Material entities (lots) this material was produced from. Following the links back gives the material loop history.    
      items:    
        format: uri    
        type: string    
      type: array    
      x-ngsi:    
        type: Relationship    
    refProcess:    
      description: Process or process event entity that produced this material.    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
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
    substancesOfConcern:    
      description: Substances of concern present in the material, as required by the EU ESPR Digital Product Passport.    
      items:    
        properties:    
          casNumber:    
            description: Property. CAS registry number of the substance.    
            type: string    
          concentration:    
            description: 'Property. Unit: mg/kg. Measured concentration of the substance in the material.'    
            minimum: 0    
            type: number    
          ecNumber:    
            description: Property. EC number of the substance.    
            type: string    
          name:    
            description: Property. Name of the substance.    
            type: string    
          regulation:    
            description: 'Property. Regulation listing the substance: REACH candidate list (SVHC), REACH Annex XVII restriction (e.g. Cr(VI) in leather), EU POPs Regulation 2019/1021 (e.g. brominated flame retardants), or other.'    
            enum:    
              - REACH-SVHC    
              - REACH-AnnexXVII    
              - POP    
              - other    
            type: string    
        required:    
          - name    
        type: object    
      type: array    
      x-ngsi:    
        type: Property    
    suitableRecoveryRoutes:    
      description: Circular strategies (R-ladder) the material is suitable for. Used to match offers with demand.    
      items:    
        enum:    
          - reuse    
          - repair    
          - refurbish    
          - remanufacture    
          - repurpose    
          - recycle    
          - energyRecovery    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
    surfaceFinishWithCovering:    
      description: Leather finished (with covering) or not finished    
      type: boolean    
      x-ngsi:    
        type: Property    
    tannedProcess:    
      description: The tanning process used. chromeFree covers wet-white leather.    
      enum:    
        - chrome    
        - vegetable    
        - chromeFree    
        - aldehyde    
        - synthetic    
        - mixed    
      type: string    
      x-ngsi:    
        type: Property    
    thickness:    
      description: 'Unit: mm. The thickness of the leather. '    
      properties:    
        value:    
          description: Property. https://schema.org/Number.    
          minimum: 0    
          type: number    
      type: object    
      x-ngsi:    
        type: Property    
    type:    
      description: NGSI Entity type. It has to be leather    
      enum:    
        - leather    
      type: string    
      x-ngsi:    
        type: Property    
    wasteCode:    
      description: European List of Waste code (Commission Decision 2000/532/EC), e.g. 07 02 13 for waste plastic. A trailing * marks hazardous waste. Only when materialStatus is waste.    
      pattern: ^[0-9]{2} [0-9]{2} [0-9]{2}\*?$    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - color    
    - area    
  type: object    
  x-derived-from: ''    
  x-disclaimer: Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program    
  x-license-url: https://github.com/smart-data-models/circuloos_data_model/blob/master/leather/LICENSE.md    
  x-model-schema: https://raw.githubusercontent.com/european-dynamics-rnd/CIRCULOOS_Data_model/main/material/leather/schema.json    
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
    "id": "urn:ngsi-ld:leather:IDAS1313",  
    "type": "leather",  
    "origin": {  
        "type": "Property",  
        "value": "cow"  
    },  
    "color": {  
        "type": "Property",  
        "value": "black"  
    },  
    "thickness": {  
        "type": "Property",  
        "value": 0.3,  
        "unitCode": "MMT"  
    },  
    "tannedProcess": {  
        "type": "Property",  
        "value": "chrome"  
    },  
    "surfaceFinishWithCovering": {  
        "type": "Property",  
        "value": true  
    },  
    "hardness": {  
        "type": "Property",  
        "value": "medium"  
    },  
    "recycledTimes": {  
        "type": "Property",  
        "value": 2  
    },  
    "materialSource": {  
        "type": "Property",  
        "value": "preConsumerOffcut"  
    },  
    "area": {  
        "type": "Property",  
        "value": 0.35,  
        "unitCode": "MTK"  
    },  
    "pieceFormat": {  
        "type": "Property",  
        "value": "offcut"  
    },  
    "leatherCut": {  
        "type": "Property",  
        "value": "split"  
    },  
    "materialStatus": {  
        "type": "Property",  
        "value": "waste"  
    },  
    "wasteCode": {  
        "type": "Property",  
        "value": "04 01 08"  
    },  
    "hazardous": {  
        "type": "Property",  
        "value": false  
    },  
    "quantity": {  
        "type": "Property",  
        "value": 85,  
        "unitCode": "KGM"  
    },  
    "substancesOfConcern": {  
        "type": "Property",  
        "value": [  
            {  
                "name": "Chromium(VI)",  
                "casNumber": "18540-29-9",  
                "concentration": 1.2,  
                "regulation": "REACH-AnnexXVII"  
            }  
        ]  
    },  
    "composition": {  
        "type": "Property",  
        "value": [  
            {  
                "name": "Collagen",  
                "share": 80  
            },  
            {  
                "name": "Chromium(III) oxide",  
                "casNumber": "1308-38-9",  
                "share": 4  
            }  
        ]  
    },  
    "suitableRecoveryRoutes": {  
        "type": "Property",  
        "value": [  
            "repurpose",  
            "recycle"  
        ]  
    },  
    "certifications": {  
        "type": "Property",  
        "value": [  
            {  
                "scheme": "LWG",  
                "certificateId": "LWG-GR-0042",  
                "issuer": "Leather Working Group",  
                "validUntil": "2027-01-31"  
            }  
        ]  
    },  
    "location": {  
        "type": "GeoProperty",  
        "value": {  
            "type": "Point",  
            "coordinates": [  
                23.7275,  
                37.9838  
            ]  
        }  
    },  
    "@context": [  
        "https://raw.githubusercontent.com/european-dynamics-rnd/CIRCULOOS_Data_model/main/material/leather/context.jsonld",  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context-v1.8.jsonld"  
    ]  
}  
```  
</details><!-- /80-Examples -->  
