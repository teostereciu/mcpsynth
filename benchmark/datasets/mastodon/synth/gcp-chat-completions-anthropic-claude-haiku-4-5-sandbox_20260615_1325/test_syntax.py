#!/usr/bin/env python3
"""Quick syntax check for server.py"""
import ast
import sys

try:
    with open('server.py', 'r') as f:
        code = f.read()
    ast.parse(code)
    print("✓ server.py syntax is valid")
    
    # Count the number of function definitions
    tree = ast.parse(code)
    functions = [node for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]
    print(f"✓ Found {len(functions)} functions")
    
    # Check for main entry point
    if any(f.name == '<module>' for f in ast.walk(tree)):
        print("✓ Module-level code present")
    
    sys.exit(0)
except SyntaxError as e:
    print(f"✗ Syntax error: {e}")
    sys.exit(1)
except Exception as e:
    print(f"✗ Error: {e}")
    sys.exit(1)
