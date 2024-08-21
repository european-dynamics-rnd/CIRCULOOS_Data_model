# CIRCULOOS Data model

For CIRCULOOS data model we will utilize components of the [Smart Data Models](https://github.com/smart-data-models)

## How to compine existing data models into one, @context file
@context file is needed from Orion-LD to correctly link the data 

1. Go to [Smart Data models](https://github.com/smart-data-models) and find select the data models that you need
2. From each model, copy the RAW URL of the context.jsonld ie for https://github.com/smart-data-models/dataModel.Device/tree/master  
https://raw.githubusercontent.com/smart-data-models/dataModel.Device/master/context.jsonld
3. Create a new json file with one line per data model ie for device:
  "dataModel.Device": "https://raw.githubusercontent.com/smart-data-models/dataModel.Device/master/context.jsonld", 
4. Upload it on-line (github or webserver)
5. Go to [Generate a local @context](https://smartdatamodels.org/index.php/generate-a-local-context-based-on-smart-data-models-iris/)
6. Save the json file and check for conflicts


## Create a new Data model
See files under folder custom_data_model.

1. Edit schema.json and all files in /examples to represent the new schema
2. Upload it to Git or webserver
3. For generating the model.yaml Edit and run utils/10_model.yaml_v10.py, Line 129: schemaUrl="" to point to the repository or webserver of the custom_data_model folder
4. Move generated yaml to custom_data_model and sync with Git or webserver
5. For generating the spec.md Edit and run utils/20_create_spec_v11.0.py L230: customRepository="" to point to the repository or webserver of the custom_data_model folder
6. Copy generated file to custom_data_model/doc
7. For generating the context.jsonld Edit and run 25_create_subject_context_V7.py, L323: customRepository="" to point to the repository or webserver of the custom_data_model folder
8. For updating the url for each properties with the SmartDataModel webpage. Run update_urls_to_show_smart_data_model.py.

You can use the docker-compose.yml file located on the utils folder for a local webserver based on NGINX 

## unit code aka 3 alphanumeric code to represent a physical quantity

unitCode : https://docs.peppol.eu/poacc/billing/3.0/codelist/UNECERec20/

Fiware dictionary/terms with for data models: https://github.com/smart-data-models/data-models/blob/master/terms.jsonld

