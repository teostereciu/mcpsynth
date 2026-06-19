import os
import importlib
from mcp.server.fastmcp import FastMCP, register_tool
from typing import Any, Dict
import glob

# Import all tool modules and register their functions
modules = [
    'generated_tools.payment_intents',
    'generated_tools.charges',
    'generated_tools.customers',
    'generated_tools.products',
    'generated_tools.prices',
    'generated_tools.subscriptions',
    'generated_tools.invoices',
    'generated_tools.checkout',
    'generated_tools.payment_links',
    'generated_tools.connect',
    'generated_tools.refunds',
    'generated_tools.setup_intents',
    'generated_tools.coupons',
    'generated_tools.promotion_codes',
]

def list_tools() -> Dict[str, Any]:
    """
    List all available tools.
    """
    return {name: func for name, func in FastMCP.tools.items()}

for module_name in modules:
    module = importlib.import_module(module_name)
    for attr in dir(module):
        if attr.startswith("_"):
            continue
        func = getattr(module, attr)
        if callable(func):
            register_tool(func)

register_tool(list_tools)

if __name__ == "__main__":
    FastMCP.run_stdio()
