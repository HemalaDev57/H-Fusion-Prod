#!/usr/bin/env python3
"""
Filter action_artifacts.json to only include artifacts that changed between commits.
Used by promote-action-artifacts-main workflow.
"""

import json
import sys

def flatten_artifacts(data):
    """Flatten nested artifact structure into {name: (section, subsection, version)}"""
    result = {}

    # Handle public section (nested: public -> subsection -> artifacts)
    if "public" in data and isinstance(data["public"], dict):
        for subsection, items in data["public"].items():
            if isinstance(items, dict):
                for name, version in items.items():
                    result[name] = ("public", subsection, version)

    # Handle private section (flat: private -> artifacts directly)
    if "private" in data and isinstance(data["private"], dict):
        for name, version in data["private"].items():
            # Private artifacts don't have subsections, use "private" as subsection
            result[name] = ("private", "private", version)

    return result

def main():
    if len(sys.argv) != 4:
        print("Usage: filter_changed_artifacts.py <before.json> <after.json> <output.json>")
        sys.exit(1)

    before_file = sys.argv[1]
    after_file = sys.argv[2]
    output_file = sys.argv[3]

    # Load data
    with open(before_file) as f:
        before = flatten_artifacts(json.load(f))

    with open(after_file) as f:
        after_data = json.load(f)
        after = flatten_artifacts(after_data)

    # Find changed artifacts
    changed_artifacts = []
    for name in after:
        if name not in before or before[name][2] != after[name][2]:
            changed_artifacts.append(name)
            old_ver = before.get(name, (None, None, 'NEW'))[2]
            new_ver = after[name][2]
            print(f"Changed: {name}: {old_ver} -> {new_ver}")

    if not changed_artifacts:
        print("No artifact version changes detected")
        sys.exit(1)

    print(f"\nTotal changed: {len(changed_artifacts)} out of {len(after)} artifacts")

    # Create filtered JSON with only changed artifacts
    filtered = {"public": {"actions": {}, "custom-jobs": {}, "services": {}}, "private": {}}

    for name in changed_artifacts:
        section, subsection, version = after[name]
        if section == "public":
            if subsection not in filtered["public"]:
                filtered["public"][subsection] = {}
            filtered["public"][subsection][name] = version
        elif section == "private":
            filtered["private"][name] = version

    # Add skip section from original (always needed)
    if "skip" in after_data:
        filtered["skip"] = after_data["skip"]

    # Write filtered JSON
    with open(output_file, 'w') as f:
        json.dump(filtered, f, indent=2)

    print(f"\nFiltered artifacts saved to {output_file}")
    print(json.dumps(filtered, indent=2))

if __name__ == "__main__":
    main()
