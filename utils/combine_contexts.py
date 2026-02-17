import json
import sys
import os
import urllib.request


def load_sources_from_file(sources_file):
    with open(sources_file, 'r') as file:
        return [
            line.strip()
            for line in file
            if line.strip() and not line.strip().startswith('#')
        ]

def load_context(source):
    if source.startswith('http://') or source.startswith('https://'):
        with urllib.request.urlopen(source) as response:
            data = json.load(response)
    else:
        with open(source, 'r') as file:
            data = json.load(file)
    return data['@context'] if '@context' in data else data

def combine_contexts(context_sources):
    combined = {}
    for src in context_sources:
        ctx = load_context(src)
        if isinstance(ctx, dict):
            combined.update(ctx)
        elif isinstance(ctx, list):
            for item in ctx:
                if isinstance(item, dict):
                    combined.update(item)
    return {'@context': combined}

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python combine_contexts.py output.jsonld context1.jsonld [context2.jsonld ...]")
        print("  python combine_contexts.py output.jsonld [sources_file.txt]")
        sys.exit(1)

    output_file = sys.argv[1]

    if len(sys.argv) == 2:
        sources_file = os.path.join(os.path.dirname(__file__), "merging_context.txt")
        if not os.path.exists(sources_file):
            print(f"Sources file not found: {sources_file}")
            sys.exit(1)
        context_files = load_sources_from_file(sources_file)
    elif len(sys.argv) == 3 and sys.argv[2].endswith('.txt'):
        sources_file = sys.argv[2]
        if not os.path.exists(sources_file):
            print(f"Sources file not found: {sources_file}")
            sys.exit(1)
        context_files = load_sources_from_file(sources_file)
    else:
        context_files = sys.argv[2:]

    if not context_files:
        print("No context sources provided.")
        sys.exit(1)

    combined = combine_contexts(context_files)
    with open(output_file, 'w') as f:
        json.dump(combined, f, indent=4)
    print(f"Combined context written to {output_file}")
