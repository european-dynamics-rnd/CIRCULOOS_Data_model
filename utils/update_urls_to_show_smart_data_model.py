import json

#
# Run it to generate the context  jsonld 
#
with open('./smart-data-models-context.jsonld', 'r') as file:
        smart_data_model_url = json.load(file)
smart_data_model_url=smart_data_model_url['@context']


with open('./context.jsonld', 'r') as file:
        my_data_model = json.load(file)
        
my_data_model=my_data_model['@context']


for key in my_data_model:
    if key in smart_data_model_url:
        my_data_model[key] = smart_data_model_url[key]

temp={}
temp['@context']=my_data_model
with open("new_data_model.jsonld", 'w') as file:
    json.dump(temp, file, indent=4)