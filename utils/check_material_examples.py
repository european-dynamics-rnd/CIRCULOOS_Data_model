#!/usr/bin/env python3
"""Check every material/ model: its example validates against its schema, and
its context maps the circularity-commons terms to the commons namespace.

Run from anywhere: python3 utils/check_material_examples.py
CIRCULOOS $refs resolve to the local repo copy, so this works before pushing.
"""
import json
import os
import sys

import jsonref
import jsonschema

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO_RAW = "https://raw.githubusercontent.com/european-dynamics-rnd/CIRCULOOS_Data_model/main/"
MATERIAL = os.path.join(REPO, "material")
COMMONS = os.path.join(MATERIAL, "circularity-commons.json")


def loader(uri):
    if uri.startswith(REPO_RAW):
        return json.load(open(os.path.join(REPO, uri[len(REPO_RAW):])))
    return jsonref.jsonloader(uri)


def properties(schema):
    props = dict(schema.get("properties", {}))
    for branch in schema.get("allOf", []):
        props.update(properties(branch))
    return props


def key_values(entity, props):
    """Normalized NGSI-LD to the shape the material schemas describe: numeric
    attributes stay {value, unitCode}, everything else becomes its bare value."""
    out = {}
    for k, attr in entity.items():
        if k == "@context" or not isinstance(attr, dict):
            out[k] = attr
        elif props.get(k, {}).get("type") == "object":
            out[k] = attr
        else:
            out[k] = attr.get("object", attr.get("value"))
    return out


def main():
    commons = json.load(open(COMMONS))
    commons_terms = commons["definitions"]["Circularity-Commons"]["properties"]
    failures = 0
    for name in sorted(os.listdir(MATERIAL)):
        folder = os.path.join(MATERIAL, name)
        if not os.path.isfile(os.path.join(folder, "schema.json")):
            continue
        schema = jsonref.replace_refs(json.load(open(os.path.join(folder, "schema.json"))),
                                      loader=loader, proxies=False)
        example = json.load(open(os.path.join(folder, "examples", "example-normalized.jsonld")))
        try:
            jsonschema.validate(key_values(example, properties(schema)), schema)
        except jsonschema.ValidationError as e:
            failures += 1
            print(f"{name}: example invalid at {'/'.join(map(str, e.absolute_path))}: {e.message}")

        context = json.load(open(os.path.join(folder, "context.jsonld")))["@context"]
        wrong = [t for t in commons_terms if t in context and not context[t].startswith(commons["$id"])]
        if wrong:
            failures += 1
            print(f"{name}: context maps commons terms outside {commons['$id']}: {wrong}")
        print(f"{name}: checked")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
