#!/usr/bin/env python3
"""Validate the grounding.json file."""

import json

with open('grounding.json') as f:
    data = json.load(f)

print(f"Total tools mapped: {len(data)}")
print("\nSample entries:")
for i, (tool, info) in enumerate(list(data.items())[:3]):
    print(f"{i+1}. {tool}:")
    print(f"   - doc: {info['doc']}")
    print(f"   - endpoint: {info['endpoint']}")

# Check that all tools have both doc and endpoint
missing = []
for tool, info in data.items():
    if 'doc' not in info or 'endpoint' not in info:
        missing.append(tool)

if missing:
    print(f"\n⚠️  Missing fields for tools: {missing}")
else:
    print("\n✅ All tools have proper doc and endpoint fields")
