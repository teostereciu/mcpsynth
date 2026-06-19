import json
import sys

try:
    with open('grounding.json', 'r') as f:
        data = json.load(f)
    print(f"grounding.json is valid JSON with {len(data)} entries")
    print("Tools:")
    for tool in sorted(data.keys()):
        print(f"  - {tool}")
    sys.exit(0)
except json.JSONDecodeError as e:
    print(f"JSON error: {e}")
    sys.exit(1)
except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)
