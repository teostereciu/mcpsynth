import py_compile
import sys

try:
    py_compile.compile('server.py', doraise=True)
    print("Syntax OK")
    sys.exit(0)
except py_compile.PyCompileError as e:
    print(f"Syntax error: {e}")
    sys.exit(1)
