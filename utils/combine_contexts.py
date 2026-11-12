import glob
import json
import sys
import os
import urllib.request


def load_sources_from_file(sources_file):
    sources = []
    with open(sources_file, 'r') as file:
        for line in file:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            if line.startswith(('http://', 'https://')):
                sources.append(line)
            elif any(c in line for c in '*?['):
                sources += [os.path.normpath(p) for p in sorted(glob.glob(line, recursive=True))]
            else:
                sources.append(os.path.normpath(line))
    # A source listed more than once is loaded only at its last position, so an
    # explicit line placed after a glob keeps the priority it is given there.
    return list(reversed(dict.fromkeys(reversed(sources))))

def load_context(source):
    if source.startswith('http://') or source.startswith('https://'):
        with urllib.request.urlopen(source) as response:
            data = json.load(response)
    else:
        with open(source, 'r') as file:
            data = json.load(file)
    return data['@context'] if '@context' in data else data

def combine_contexts(context_sources):
    # Later sources win. A term mapped to a different value by a later source is
    # reported, as a GitHub annotation when running in Actions.
    prefix = '::warning::' if os.environ.get('GITHUB_ACTIONS') else 'WARNING: '
    combined, origin = {}, {}
    for src in context_sources:
        ctx = load_context(src)
        for item in ctx if isinstance(ctx, list) else [ctx]:
            if not isinstance(item, dict):
                continue
            for term, value in item.items():
                if term in combined and combined[term] != value:
                    print(f"{prefix}term '{term}' from {origin[term]} overridden by {src}")
                combined[term] = value
                origin[term] = src
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
