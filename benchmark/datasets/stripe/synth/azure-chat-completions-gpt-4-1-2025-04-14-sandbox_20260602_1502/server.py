import os
from mcp.server.fastmcp import FastMCP
import importlib
import inspect
import sys
import json

# Tool registry
TOOL_MODULES = [
    'generated_tools.payment_intents',
    'generated_tools.charges',
    'generated_tools.refunds',
    'generated_tools.customers',
    'generated_tools.products',
    'generated_tools.prices',
    'generated_tools.subscriptions',
    'generated_tools.invoices',
    'generated_tools.checkout_sessions',
    'generated_tools.payment_link',
    'generated_tools.accounts',
    'generated_tools.transfers',
    'generated_tools.payouts',
    'generated_tools.setup_intents',
    'generated_tools.coupons',
    'generated_tools.promotion_codes',
]

def discover_tools():
    tools = {}
    for modname in TOOL_MODULES:
        mod = importlib.import_module(modname)
        for name, func in inspect.getmembers(mod, inspect.isfunction):
            tools[name] = func
    return tools

TOOLS = discover_tools()

def list_tools():
    return list(TOOLS.keys())

# MCP server
class StripeMCPServer(FastMCP):
    def __init__(self):
        super().__init__()
        for tool_name, func in TOOLS.items():
            self.register_tool(tool_name, func)
        self.register_tool('list_tools', list_tools)

if __name__ == '__main__':
    server = StripeMCPServer()
    server.run_stdio()
