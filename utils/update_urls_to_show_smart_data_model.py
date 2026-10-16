import argparse
import json

#
# Run it to generate the context jsonld
#
# Usage: update_urls_to_show_smart_data_model.py [schema_url] [--shared schema.json ...]
#   schema_url  namespace for the model's own terms. Defaults to the
#               intra-communication schema, which existing models use.
#   --shared    local copy of a CIRCULOOS schema the model pulls in via allOf
#               (e.g. material/circularity-commons.json). Its terms keep that
#               schema's $id as namespace, so every model using it maps them
#               to the same IRI.
#
ap = argparse.ArgumentParser()
ap.add_argument("schema_url", nargs="?", default="https://raw.githubusercontent.com/european-dynamics-rnd/CIRCULOOS_Data_model/main/intra-communication/schema.json")
ap.add_argument("--shared", action="append", default=[])
args = ap.parse_args()

with open('./combined_subjects_context.jsonld', 'r') as file:
    smart_data_model_url = json.load(file)
smart_data_model_url = smart_data_model_url['@context']

with open('./context.jsonld', 'r') as file:
    my_data_model = json.load(file)
my_data_model = my_data_model['@context']

schema_url = args.schema_url


def terms(node):
    """Every property name declared anywhere in a schema."""
    if isinstance(node, list):
        for v in node:
            yield from terms(v)
    elif isinstance(node, dict):
        yield from node.get("properties", {})
        for v in node.values():
            yield from terms(v)


shared = {}
for path in args.shared:
    with open(path, 'r') as file:
        schema = json.load(file)
    shared.update({term: f"{schema['$id']}#/{term}" for term in terms(schema)})

for key in my_data_model:
    if key in smart_data_model_url:
        my_data_model[key] = smart_data_model_url[key]
    elif key in shared:
        my_data_model[key] = shared[key]
    else:
        my_data_model[key] = f"{schema_url}#/{key}"

temp = {}
temp['@context'] = my_data_model
with open("new_data_model.jsonld", 'w') as file:
    json.dump(temp, file, indent=4)
