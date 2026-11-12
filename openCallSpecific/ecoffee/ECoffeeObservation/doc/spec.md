<!-- 10-Header -->  
Entity: ECoffeeObservation  
==========================<!-- /10-Header -->  
<!-- 15-License -->  
[Open License](https://raw.githubusercontent.com/european-dynamics-rnd/CIRCULOOS_Data_model/refs/heads/main/LICENSE)  
<!-- /15-License -->  
<!-- 20-Description -->  
Global description: **CIRCULOOS data model for the life-cycle inventory of the eCoffee value chain. It covers the AS-IS disposal route of spent coffee grains, their collection by EUSKOVAZZA, drying, and their valorisation into a biocide product at FUMIHOGAR and a sheep feed at AZTI, recording the material masses, transport distances and energy consumptions of each step for digital product and LCA models.**  
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
- `alternateName[string]`: An alternative name for this item  - `aluminiumPackagingMass[*]`: Expected unitCode: GRM. Mass of aluminium packaging used per product or batch. It is used to quantify packaging material demand and related lifecycle impacts.  - `areaServed[string]`: The geographic area where a service or offered item is provided  . Model: [https://schema.org/Text](https://schema.org/Text)- `barleyInputMass[*]`: Expected unitCode: KGM. Mass of barley sourced from Spain for the sheep feed formulation. It is used to quantify a conventional agricultural ingredient in the feed recipe.  - `barleyTransportDistance[*]`: Expected unitCode: KMT. Truck transport distance from the milling company to AZTI for barley. It is used to model inbound logistics for this feed ingredient.  - `biocideOutputMass[*]`: Expected unitCode: KGM. Mass of biocide product produced by FUMIHOGAR. It is used to define the final product output containing recovered dried spent coffee grains.  - `biomassHeatConsumption[*]`: Expected unitCode: KWH. Heat energy supplied from biomass for the AZTI drying process. It is used to model thermal energy demand and renewable heat contribution in the lifecycle inventory.  - `collectedSpentCoffeeGrainInputMass[*]`: Expected unitCode: KGM. Mass of spent coffee grain entering the EUSKOVAZZA collection/process boundary. It is used to quantify the main recovered organic input available for subsequent valorisation steps.  - `collectedSpentCoffeeGrainMass[*]`: Expected unitCode: KGM. Mass of spent coffee grain successfully collected as an output from EUSKOVAZZA. It indicates the recoverable material transferred to the next partner or process step.  - `collectionTransportDistance[*]`: Expected unitCode: KMT. Distance travelled from coffee-ground generation points to the processing facility using a van or small truck. It is used to model logistics activity and transport-related environmental impacts.  - `dataProvider[string]`: A sequence of characters identifying the provider of the harmonised data entity  - `dateCreated[date-time]`: Entity creation timestamp. This will usually be allocated by the storage platform  - `dateModified[date-time]`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform  - `description[string]`: A description of this item  - `disposalTransportDistance[*]`: Expected unitCode: KMT. Distance travelled from spent coffee grain generation points to the final disposal destination. It is used to model logistics activity and transport-related environmental impacts in the current scenario.  - `distillersDriedGrainsInputMass[*]`: Expected unitCode: KGM. Mass of distillers dried grains included as an average-market feed ingredient. It is used to quantify co-product feed material within the formulation.  - `distillersDriedGrainsTransportDistance[*]`: Expected unitCode: KMT. Truck transport distance from the milling company to AZTI for distillers dried grains. It is used to model inbound logistics for this feed ingredient.  - `driedCoffeeGrainFeedInputMass2[*]`: Expected unitCode: KGM. Mass of dried coffee grains received by AZTI used as an input in the sheep feed formulation. It is used to track recovered coffee-derived biomass replacing or complementing conventional feed ingredients.  - `driedCoffeeGrainInputMass1[*]`: Expected unitCode: KGM. Mass of dried coffee grains received by FUMIHOGAR as an input material. It is used to track incorporation of recovered coffee-derived material into the biocide product process.  - `driedCoffeeGrainOutputMass[*]`: Expected unitCode: KGM. Mass of dried coffee grains produced after the drying process. It is used to track moisture-reduced material available for downstream product formulation.  - `fossilIncinerationHeatConsumption[*]`: Expected unitCode: 3B. Heat energy required for incineration supplied from fossil fuels. It is used to quantify thermal energy demand and fossil-energy contribution in the AS-IS end-of-life treatment route.  - `id[string]`: Unique entity identifier of the eCoffee value chain record, with the format urn:ngsi-ld:ECoffeeObservation:<recordId>.  - `location[*]`: GeoProperty. Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon  - `maizeBoatTransportDistance[*]`: Expected unitCode: SMI. Sea transport distance for maize from the milling company or origin route to AZTI. It is used to model overseas logistics and transport-related impacts.  - `maizeInputMass[*]`: Expected unitCode: KGM. Mass of maize sourced from Brazil for the sheep feed formulation. It is used to quantify an imported agricultural ingredient in the feed product model.  - `molassesInputMass[*]`: Expected unitCode: KGM. Mass of molasses sourced from Spain for the sheep feed formulation. It is used to quantify a carbohydrate-rich binding or energy ingredient in the feed recipe.  - `molassesTransportDistance[*]`: Expected unitCode: KMT. Truck transport distance from the milling company to AZTI for molasses. It is used to model logistics activity for this supplied ingredient.  - `name[string]`: The name of this item  - `oatsInputMass[*]`: Expected unitCode: KGM. Mass of oats sourced from Spain for the sheep feed formulation. It is used to quantify a conventional cereal ingredient in the digital feed recipe.  - `oatsTransportDistance[*]`: Expected unitCode: KMT. Truck transport distance from the milling company to AZTI for oats. It is used to calculate logistics activity for this ingredient.  - `owner[array]`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  - `packagingTransportDistance[*]`: Expected unitCode: KMT. Transport distance for packaging materials to the production site by light truck. It is used to account for logistics impacts linked to packaging supply.  - `potassiumNitrateInputMass[*]`: Expected unitCode: KGM. Mass of potassium nitrate used as a formulation ingredient in the biocide process. It is used to identify and quantify a key chemical input in the product recipe.  - `potsassiumsupplierToFumihogarTransportDistance[*]`: Expected unitCode: KMT. Transport distance from the supplier facility to FUMIHOGAR by light truck. It is used to model inbound logistics for supplied formulation materials.  - `processingToAztiTransportDistance[*]`: Expected unitCode: KMT. Distance from the processing facility to AZTI for dried coffee grain transfer. A value of zero indicates no transport distance is assigned within the defined process boundary.  - `processingToFumihogarTransportDistance[*]`: Expected unitCode: KMT. Transport distance from the processing facility to FUMIHOGAR by light truck. It is used to calculate logistics activity associated with moving dried coffee grains to the manufacturing site.  - `rapeseedMealInputMass[*]`: Expected unitCode: KGM. Mass of rapeseed meal sourced from France for the sheep feed formulation. It is used to quantify protein-rich feed material in the product recipe.  - `rapeseedMealTransportDistance[*]`: Expected unitCode: KMT. Truck transport distance from the milling company to AZTI for rapeseed meal. It is used to calculate transport activity for this ingredient.  - `rapeseedOilInputMass[*]`: Expected unitCode: KGM. Mass of rapeseed oil sourced from France for the sheep feed formulation. It is used to quantify oil-based nutritional input in the feed recipe.  - `rapeseedOilTransportDistance[*]`: Expected unitCode: KMT. Truck transport distance from the milling company to AZTI for rapeseed oil. It is used to model inbound logistics for this ingredient.  - `renewableBiocidesProcessElectricityCompumption[*]`: Expected unitCode: KWH. Represents renewable electricity consumed per unit of product. It is used to normalize manufacturing energy demand at product-unit level for digital product and LCA models.  - `renewableDryingElectricityConsumption[*]`: Expected unitCode: KWH. Electricity consumed for drying operations, supplied from renewable sources. It is used to quantify process energy demand and distinguish renewable electricity from fossil-based energy.  - `renewableFeedProcessElectricityConsumption[*]`: Expected unitCode: KWH. Renewable electricity consumed in the sheep feed production process at AZTI. It is used to quantify process energy demand associated with feed preparation.  - `seeAlso[*]`: list of uri pointing to additional resources about the item  - `sheepFeedOutputMass[*]`: Expected unitCode: KGM. Mass of sheep feed produced, including dried spent coffee grains. It is used to define the final feed product output in the digital lifecycle model.  - `source[string]`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object  - `spentCoffeeGrainInputMass[*]`: Expected unitCode: TNE. Mass of spent coffee grains generated within the AS-IS process boundary. It is used to quantify the main organic waste stream before any valorisation or alternative treatment.  - `type[string]`: NGSI Entity type. It has to be ECoffeeObservation  <!-- /30-PropertiesList -->  
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
ECoffeeObservation:    
  description: CIRCULOOS data model for the life-cycle inventory of the eCoffee value chain. It covers the AS-IS disposal route of spent coffee grains, their collection by EUSKOVAZZA, drying, and their valorisation into a biocide product at FUMIHOGAR and a sheep feed at AZTI, recording the material masses, transport distances and energy consumptions of each step for digital product and LCA models.    
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
    aluminiumPackagingMass:    
      allOf:    
        - anyOf:    
            - type: number    
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
      description: 'Expected unitCode: GRM. Mass of aluminium packaging used per product or batch. It is used to quantify packaging material demand and related lifecycle impacts.'    
      x-ngsi:    
        type: Property    
    areaServed:    
      description: The geographic area where a service or offered item is provided    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    barleyInputMass:    
      allOf:    
        - anyOf:    
            - type: number    
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
      description: 'Expected unitCode: KGM. Mass of barley sourced from Spain for the sheep feed formulation. It is used to quantify a conventional agricultural ingredient in the feed recipe.'    
      x-ngsi:    
        type: Property    
    barleyTransportDistance:    
      allOf:    
        - anyOf:    
            - type: number    
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
      description: 'Expected unitCode: KMT. Truck transport distance from the milling company to AZTI for barley. It is used to model inbound logistics for this feed ingredient.'    
      x-ngsi:    
        type: Property    
    biocideOutputMass:    
      allOf:    
        - anyOf:    
            - type: number    
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
      description: 'Expected unitCode: KGM. Mass of biocide product produced by FUMIHOGAR. It is used to define the final product output containing recovered dried spent coffee grains.'    
      x-ngsi:    
        type: Property    
    biomassHeatConsumption:    
      allOf:    
        - anyOf:    
            - type: number    
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
      description: 'Expected unitCode: KWH. Heat energy supplied from biomass for the AZTI drying process. It is used to model thermal energy demand and renewable heat contribution in the lifecycle inventory.'    
      x-ngsi:    
        type: Property    
    collectedSpentCoffeeGrainInputMass:    
      allOf:    
        - anyOf:    
            - type: number    
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
      description: 'Expected unitCode: KGM. Mass of spent coffee grain entering the EUSKOVAZZA collection/process boundary. It is used to quantify the main recovered organic input available for subsequent valorisation steps.'    
      x-ngsi:    
        type: Property    
    collectedSpentCoffeeGrainMass:    
      allOf:    
        - anyOf:    
            - type: number    
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
      description: 'Expected unitCode: KGM. Mass of spent coffee grain successfully collected as an output from EUSKOVAZZA. It indicates the recoverable material transferred to the next partner or process step.'    
      x-ngsi:    
        type: Property    
    collectionTransportDistance:    
      allOf:    
        - anyOf:    
            - type: number    
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
      description: 'Expected unitCode: KMT. Distance travelled from coffee-ground generation points to the processing facility using a van or small truck. It is used to model logistics activity and transport-related environmental impacts.'    
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
    disposalTransportDistance:    
      allOf:    
        - anyOf:    
            - type: number    
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
      description: 'Expected unitCode: KMT. Distance travelled from spent coffee grain generation points to the final disposal destination. It is used to model logistics activity and transport-related environmental impacts in the current scenario.'    
      x-ngsi:    
        type: Property    
    distillersDriedGrainsInputMass:    
      allOf:    
        - anyOf:    
            - type: number    
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
      description: 'Expected unitCode: KGM. Mass of distillers dried grains included as an average-market feed ingredient. It is used to quantify co-product feed material within the formulation.'    
      x-ngsi:    
        type: Property    
    distillersDriedGrainsTransportDistance:    
      allOf:    
        - anyOf:    
            - type: number    
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
      description: 'Expected unitCode: KMT. Truck transport distance from the milling company to AZTI for distillers dried grains. It is used to model inbound logistics for this feed ingredient.'    
      x-ngsi:    
        type: Property    
    driedCoffeeGrainFeedInputMass2:    
      allOf:    
        - anyOf:    
            - type: number    
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
      description: 'Expected unitCode: KGM. Mass of dried coffee grains received by AZTI used as an input in the sheep feed formulation. It is used to track recovered coffee-derived biomass replacing or complementing conventional feed ingredients.'    
      x-ngsi:    
        type: Property    
    driedCoffeeGrainInputMass1:    
      allOf:    
        - anyOf:    
            - type: number    
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
      description: 'Expected unitCode: KGM. Mass of dried coffee grains received by FUMIHOGAR as an input material. It is used to track incorporation of recovered coffee-derived material into the biocide product process.'    
      x-ngsi:    
        type: Property    
    driedCoffeeGrainOutputMass:    
      allOf:    
        - anyOf:    
            - type: number    
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
      description: 'Expected unitCode: KGM. Mass of dried coffee grains produced after the drying process. It is used to track moisture-reduced material available for downstream product formulation.'    
      x-ngsi:    
        type: Property    
    fossilIncinerationHeatConsumption:    
      allOf:    
        - anyOf:    
            - type: number    
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
      description: 'Expected unitCode: 3B. Heat energy required for incineration supplied from fossil fuels. It is used to quantify thermal energy demand and fossil-energy contribution in the AS-IS end-of-life treatment route.'    
      x-ngsi:    
        type: Property    
    id:    
      description: Unique entity identifier of the eCoffee value chain record, with the format urn:ngsi-ld:ECoffeeObservation:<recordId>.    
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
    maizeBoatTransportDistance:    
      allOf:    
        - anyOf:    
            - type: number    
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
      description: 'Expected unitCode: SMI. Sea transport distance for maize from the milling company or origin route to AZTI. It is used to model overseas logistics and transport-related impacts.'    
      x-ngsi:    
        type: Property    
    maizeInputMass:    
      allOf:    
        - anyOf:    
            - type: number    
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
      description: 'Expected unitCode: KGM. Mass of maize sourced from Brazil for the sheep feed formulation. It is used to quantify an imported agricultural ingredient in the feed product model.'    
      x-ngsi:    
        type: Property    
    molassesInputMass:    
      allOf:    
        - anyOf:    
            - type: number    
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
      description: 'Expected unitCode: KGM. Mass of molasses sourced from Spain for the sheep feed formulation. It is used to quantify a carbohydrate-rich binding or energy ingredient in the feed recipe.'    
      x-ngsi:    
        type: Property    
    molassesTransportDistance:    
      allOf:    
        - anyOf:    
            - type: number    
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
      description: 'Expected unitCode: KMT. Truck transport distance from the milling company to AZTI for molasses. It is used to model logistics activity for this supplied ingredient.'    
      x-ngsi:    
        type: Property    
    name:    
      description: The name of this item    
      type: string    
      x-ngsi:    
        type: Property    
    oatsInputMass:    
      allOf:    
        - anyOf:    
            - type: number    
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
      description: 'Expected unitCode: KGM. Mass of oats sourced from Spain for the sheep feed formulation. It is used to quantify a conventional cereal ingredient in the digital feed recipe.'    
      x-ngsi:    
        type: Property    
    oatsTransportDistance:    
      allOf:    
        - anyOf:    
            - type: number    
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
      description: 'Expected unitCode: KMT. Truck transport distance from the milling company to AZTI for oats. It is used to calculate logistics activity for this ingredient.'    
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
    packagingTransportDistance:    
      allOf:    
        - anyOf:    
            - type: number    
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
      description: 'Expected unitCode: KMT. Transport distance for packaging materials to the production site by light truck. It is used to account for logistics impacts linked to packaging supply.'    
      x-ngsi:    
        type: Property    
    potassiumNitrateInputMass:    
      allOf:    
        - anyOf:    
            - type: number    
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
      description: 'Expected unitCode: KGM. Mass of potassium nitrate used as a formulation ingredient in the biocide process. It is used to identify and quantify a key chemical input in the product recipe.'    
      x-ngsi:    
        type: Property    
    potsassiumsupplierToFumihogarTransportDistance:    
      allOf:    
        - anyOf:    
            - type: number    
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
      description: 'Expected unitCode: KMT. Transport distance from the supplier facility to FUMIHOGAR by light truck. It is used to model inbound logistics for supplied formulation materials.'    
      x-ngsi:    
        type: Property    
    processingToAztiTransportDistance:    
      allOf:    
        - anyOf:    
            - type: number    
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
      description: 'Expected unitCode: KMT. Distance from the processing facility to AZTI for dried coffee grain transfer. A value of zero indicates no transport distance is assigned within the defined process boundary.'    
      x-ngsi:    
        type: Property    
    processingToFumihogarTransportDistance:    
      allOf:    
        - anyOf:    
            - type: number    
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
      description: 'Expected unitCode: KMT. Transport distance from the processing facility to FUMIHOGAR by light truck. It is used to calculate logistics activity associated with moving dried coffee grains to the manufacturing site.'    
      x-ngsi:    
        type: Property    
    rapeseedMealInputMass:    
      allOf:    
        - anyOf:    
            - type: number    
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
      description: 'Expected unitCode: KGM. Mass of rapeseed meal sourced from France for the sheep feed formulation. It is used to quantify protein-rich feed material in the product recipe.'    
      x-ngsi:    
        type: Property    
    rapeseedMealTransportDistance:    
      allOf:    
        - anyOf:    
            - type: number    
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
      description: 'Expected unitCode: KMT. Truck transport distance from the milling company to AZTI for rapeseed meal. It is used to calculate transport activity for this ingredient.'    
      x-ngsi:    
        type: Property    
    rapeseedOilInputMass:    
      allOf:    
        - anyOf:    
            - type: number    
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
      description: 'Expected unitCode: KGM. Mass of rapeseed oil sourced from France for the sheep feed formulation. It is used to quantify oil-based nutritional input in the feed recipe.'    
      x-ngsi:    
        type: Property    
    rapeseedOilTransportDistance:    
      allOf:    
        - anyOf:    
            - type: number    
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
      description: 'Expected unitCode: KMT. Truck transport distance from the milling company to AZTI for rapeseed oil. It is used to model inbound logistics for this ingredient.'    
      x-ngsi:    
        type: Property    
    renewableBiocidesProcessElectricityCompumption:    
      allOf:    
        - anyOf:    
            - type: number    
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
      description: 'Expected unitCode: KWH. Represents renewable electricity consumed per unit of product. It is used to normalize manufacturing energy demand at product-unit level for digital product and LCA models.'    
      x-ngsi:    
        type: Property    
    renewableDryingElectricityConsumption:    
      allOf:    
        - anyOf:    
            - type: number    
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
      description: 'Expected unitCode: KWH. Electricity consumed for drying operations, supplied from renewable sources. It is used to quantify process energy demand and distinguish renewable electricity from fossil-based energy.'    
      x-ngsi:    
        type: Property    
    renewableFeedProcessElectricityConsumption:    
      allOf:    
        - anyOf:    
            - type: number    
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
      description: 'Expected unitCode: KWH. Renewable electricity consumed in the sheep feed production process at AZTI. It is used to quantify process energy demand associated with feed preparation.'    
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
    sheepFeedOutputMass:    
      allOf:    
        - anyOf:    
            - type: number    
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
      description: 'Expected unitCode: KGM. Mass of sheep feed produced, including dried spent coffee grains. It is used to define the final feed product output in the digital lifecycle model.'    
      x-ngsi:    
        type: Property    
    source:    
      description: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object    
      type: string    
      x-ngsi:    
        type: Property    
    spentCoffeeGrainInputMass:    
      allOf:    
        - anyOf:    
            - type: number    
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
      description: 'Expected unitCode: TNE. Mass of spent coffee grains generated within the AS-IS process boundary. It is used to quantify the main organic waste stream before any valorisation or alternative treatment.'    
      x-ngsi:    
        type: Property    
    type:    
      description: NGSI Entity type. It has to be ECoffeeObservation    
      enum:    
        - ECoffeeObservation    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: ''    
  x-disclaimer: Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program    
  x-license-url: https://github.com/smart-data-models/circuloos_data_model/blob/master/ECoffeeObservation/LICENSE.md    
  x-model-schema: https://raw.githubusercontent.com/european-dynamics-rnd/CIRCULOOS_Data_model/main/openCallSpecific/ecoffee/ECoffeeObservation/schema.json    
  x-model-tags: ecoffee    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Example payloads    
#### ECoffeeObservation NGSI-LD key-values Example    
Here is an example of a ECoffeeObservation in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:ECoffeeObservation:ecoffee-001",  
  "type": "ECoffeeObservation",  
  "spentCoffeeGrainInputMass": 1000,  
  "disposalTransportDistance": 100,  
  "fossilIncinerationHeatConsumption": 100000,  
  "collectionTransportDistance": 100,  
  "collectedSpentCoffeeGrainMass": 1000,  
  "collectedSpentCoffeeGrainInputMass": 1000,  
  "renewableDryingElectricityConsumption": 53.58,  
  "biomassHeatConsumption": 659.99,  
  "driedCoffeeGrainOutputMass": 401,  
  "driedCoffeeGrainInputMass1": 75,  
  "processingToFumihogarTransportDistance": 100,  
  "potassiumNitrateInputMass": 25,  
  "potsassiumsupplierToFumihogarTransportDistance": 100,  
  "aluminiumPackagingMass": 4,  
  "packagingTransportDistance": 100,  
  "renewableBiocidesProcessElectricityCompumption": 0.015,  
  "biocideOutputMass": 100,  
  "driedCoffeeGrainFeedInputMass2": 100,  
  "processingToAztiTransportDistance": 0,  
  "barleyInputMass": 190,  
  "barleyTransportDistance": 500,  
  "oatsInputMass": 240,  
  "oatsTransportDistance": 500,  
  "maizeInputMass": 150,  
  "maizeBoatTransportDistance": 700,  
  "distillersDriedGrainsInputMass": 50,  
  "distillersDriedGrainsTransportDistance": 200,  
  "rapeseedMealInputMass": 160,  
  "rapeseedMealTransportDistance": 1500,  
  "rapeseedOilInputMass": 50,  
  "rapeseedOilTransportDistance": 1500,  
  "molassesInputMass": 30,  
  "molassesTransportDistance": 500,  
  "renewableFeedProcessElectricityConsumption": 18,  
  "sheepFeedOutputMass": 1000,  
  "@context": [  
    "https://raw.githubusercontent.com/european-dynamics-rnd/CIRCULOOS_Data_model/main/utils/circuloos_data_platform.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context-v1.8.jsonld"  
  ]  
}  
```  
</details>  
#### ECoffeeObservation NGSI-LD normalized Example    
Here is an example of a ECoffeeObservation in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "@context": [  
    "https://raw.githubusercontent.com/european-dynamics-rnd/CIRCULOOS_Data_model/main/utils/circuloos_data_platform.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context-v1.8.jsonld"  
  ],  
  "id": "urn:ngsi-ld:ECoffeeObservation:ecoffee-001",  
  "type": "ECoffeeObservation",  
  "spentCoffeeGrainInputMass": {  
    "type": "Property",  
    "value": 1000,  
    "unitCode": "TNE",  
    "observedAt": "2026-06-11T10:15:07.446Z"  
  },  
  "disposalTransportDistance": {  
    "type": "Property",  
    "value": 100,  
    "unitCode": "KMT",  
    "observedAt": "2026-06-11T10:15:07.446Z"  
  },  
  "fossilIncinerationHeatConsumption": {  
    "type": "Property",  
    "value": 100000,  
    "unitCode": "3B",  
    "observedAt": "2026-06-11T10:15:07.446Z"  
  },  
  "collectionTransportDistance": {  
    "type": "Property",  
    "value": 100,  
    "unitCode": "KMT",  
    "observedAt": "2026-06-11T10:15:07.446Z"  
  },  
  "collectedSpentCoffeeGrainMass": {  
    "type": "Property",  
    "value": 1000,  
    "unitCode": "KGM",  
    "observedAt": "2026-06-11T10:15:07.446Z"  
  },  
  "collectedSpentCoffeeGrainInputMass": {  
    "type": "Property",  
    "value": 1000,  
    "unitCode": "KGM",  
    "observedAt": "2026-06-11T10:15:07.446Z"  
  },  
  "renewableDryingElectricityConsumption": {  
    "type": "Property",  
    "value": 53.58,  
    "unitCode": "KWH",  
    "observedAt": "2026-06-11T10:15:07.446Z"  
  },  
  "biomassHeatConsumption": {  
    "type": "Property",  
    "value": 659.99,  
    "unitCode": "KWH",  
    "observedAt": "2026-06-11T10:15:07.446Z"  
  },  
  "driedCoffeeGrainOutputMass": {  
    "type": "Property",  
    "value": 401,  
    "unitCode": "KGM",  
    "observedAt": "2026-06-11T10:15:07.446Z"  
  },  
  "driedCoffeeGrainInputMass1": {  
    "type": "Property",  
    "value": 75,  
    "unitCode": "KGM",  
    "observedAt": "2026-06-11T10:15:07.446Z"  
  },  
  "processingToFumihogarTransportDistance": {  
    "type": "Property",  
    "value": 100,  
    "unitCode": "KMT",  
    "observedAt": "2026-06-11T10:15:07.446Z"  
  },  
  "potassiumNitrateInputMass": {  
    "type": "Property",  
    "value": 25,  
    "unitCode": "KGM",  
    "observedAt": "2026-06-11T10:15:07.446Z"  
  },  
  "potsassiumsupplierToFumihogarTransportDistance": {  
    "type": "Property",  
    "value": 100,  
    "unitCode": "KMT",  
    "observedAt": "2026-06-11T10:15:07.446Z"  
  },  
  "aluminiumPackagingMass": {  
    "type": "Property",  
    "value": 4,  
    "unitCode": "GRM",  
    "observedAt": "2026-06-11T10:15:07.446Z"  
  },  
  "packagingTransportDistance": {  
    "type": "Property",  
    "value": 100,  
    "unitCode": "KMT",  
    "observedAt": "2026-06-11T10:15:07.446Z"  
  },  
  "renewableBiocidesProcessElectricityCompumption": {  
    "type": "Property",  
    "value": 0.015,  
    "unitCode": "KWH",  
    "observedAt": "2026-06-11T10:15:07.446Z"  
  },  
  "biocideOutputMass": {  
    "type": "Property",  
    "value": 100,  
    "unitCode": "KGM",  
    "observedAt": "2026-06-11T10:15:07.446Z"  
  },  
  "driedCoffeeGrainFeedInputMass2": {  
    "type": "Property",  
    "value": 100,  
    "unitCode": "KGM",  
    "observedAt": "2026-06-11T10:15:07.446Z"  
  },  
  "processingToAztiTransportDistance": {  
    "type": "Property",  
    "value": 0,  
    "unitCode": "KMT",  
    "observedAt": "2026-06-11T10:15:07.446Z"  
  },  
  "barleyInputMass": {  
    "type": "Property",  
    "value": 190,  
    "unitCode": "KGM",  
    "observedAt": "2026-06-11T10:15:07.446Z"  
  },  
  "barleyTransportDistance": {  
    "type": "Property",  
    "value": 500,  
    "unitCode": "KMT",  
    "observedAt": "2026-06-11T10:15:07.446Z"  
  },  
  "oatsInputMass": {  
    "type": "Property",  
    "value": 240,  
    "unitCode": "KGM",  
    "observedAt": "2026-06-11T10:15:07.446Z"  
  },  
  "oatsTransportDistance": {  
    "type": "Property",  
    "value": 500,  
    "unitCode": "KMT",  
    "observedAt": "2026-06-11T10:15:07.446Z"  
  },  
  "maizeInputMass": {  
    "type": "Property",  
    "value": 150,  
    "unitCode": "KGM",  
    "observedAt": "2026-06-11T10:15:07.446Z"  
  },  
  "maizeBoatTransportDistance": {  
    "type": "Property",  
    "value": 700,  
    "unitCode": "SMI",  
    "observedAt": "2026-06-11T10:15:07.446Z"  
  },  
  "distillersDriedGrainsInputMass": {  
    "type": "Property",  
    "value": 50,  
    "unitCode": "KGM",  
    "observedAt": "2026-06-11T10:15:07.446Z"  
  },  
  "distillersDriedGrainsTransportDistance": {  
    "type": "Property",  
    "value": 200,  
    "unitCode": "KMT",  
    "observedAt": "2026-06-11T10:15:07.446Z"  
  },  
  "rapeseedMealInputMass": {  
    "type": "Property",  
    "value": 160,  
    "unitCode": "KGM",  
    "observedAt": "2026-06-11T10:15:07.446Z"  
  },  
  "rapeseedMealTransportDistance": {  
    "type": "Property",  
    "value": 1500,  
    "unitCode": "KMT",  
    "observedAt": "2026-06-11T10:15:07.446Z"  
  },  
  "rapeseedOilInputMass": {  
    "type": "Property",  
    "value": 50,  
    "unitCode": "KGM",  
    "observedAt": "2026-06-11T10:15:07.446Z"  
  },  
  "rapeseedOilTransportDistance": {  
    "type": "Property",  
    "value": 1500,  
    "unitCode": "KMT",  
    "observedAt": "2026-06-11T10:15:07.446Z"  
  },  
  "molassesInputMass": {  
    "type": "Property",  
    "value": 30,  
    "unitCode": "KGM",  
    "observedAt": "2026-06-11T10:15:07.446Z"  
  },  
  "molassesTransportDistance": {  
    "type": "Property",  
    "value": 500,  
    "unitCode": "KMT",  
    "observedAt": "2026-06-11T10:15:07.446Z"  
  },  
  "renewableFeedProcessElectricityConsumption": {  
    "type": "Property",  
    "value": 18,  
    "unitCode": "KWH",  
    "observedAt": "2026-06-11T10:15:07.446Z"  
  },  
  "sheepFeedOutputMass": {  
    "type": "Property",  
    "value": 1000,  
    "unitCode": "KGM",  
    "observedAt": "2026-06-11T10:15:07.446Z"  
  }  
}  
```  
</details><!-- /80-Examples -->  
