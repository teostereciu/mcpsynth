#!/usr/bin/env python3
"""Quick syntax check for server.py"""
import py_compile
import sys

try:
    py_compile.compile('server.py', doraise=True)
    print("✓ server.py syntax is valid")
    sys.exit(0)
except py_compile.PyCompileError as e:
    print(f"✗ Syntax error in server.py: {e}")
    sys.exit(1)
