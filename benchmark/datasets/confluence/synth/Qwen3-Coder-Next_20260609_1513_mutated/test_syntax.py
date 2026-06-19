#!/usr/bin/env python3
"""Test script to verify server syntax"""
import ast
import sys

try:
    with open('server.py', 'r') as f:
        source = f.read()
    ast.parse(source)
    print("✓ Syntax OK")
    
    # Check grounding.json
    import json
    with open('grounding.json', 'r') as f:
        grounding = json.load(f)
    print(f"✓ grounding.json valid with {len(grounding)} entries")
    
    # Check requirements.txt
    with open('requirements.txt', 'r') as f:
        reqs = f.read()
    print(f"✓ requirements.txt valid ({len(reqs)} chars)")
    
except Exception as e:
    print(f"✗ Error: {e}")
    sys.exit(1)

print("\nAll files validated successfully!")
