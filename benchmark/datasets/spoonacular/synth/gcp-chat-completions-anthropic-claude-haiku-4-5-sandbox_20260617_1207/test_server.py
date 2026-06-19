#!/usr/bin/env python3
"""Quick test to verify server.py is complete."""

import ast
import sys

try:
    with open("server.py", "r") as f:
        code = f.read()
    
    # Try to parse the file as Python code
    ast.parse(code)
    print("✓ server.py is syntactically valid Python")
    
    # Check for key elements
    if "if __name__" in code:
        print("✓ server.py has main block")
    else:
        print("✗ server.py missing main block")
        sys.exit(1)
    
    if "mcp.run()" in code:
        print("✓ server.py calls mcp.run()")
    else:
        print("✗ server.py missing mcp.run()")
        sys.exit(1)
    
    # Count decorators
    decorator_count = code.count("@mcp.tool()")
    print(f"✓ Found {decorator_count} @mcp.tool() decorators")
    
    if decorator_count < 80:
        print("✗ Expected at least 80 tools")
        sys.exit(1)
    
    print("\n✓ All checks passed!")
    
except SyntaxError as e:
    print(f"✗ Syntax error in server.py: {e}")
    sys.exit(1)
except Exception as e:
    print(f"✗ Error: {e}")
    sys.exit(1)
