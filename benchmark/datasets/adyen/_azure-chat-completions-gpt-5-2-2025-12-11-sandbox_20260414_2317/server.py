"""Adyen MCP Server (FastMCP).

Exposes tools from generated_tools.* modules.
"""

from __future__ import annotations

from fastmcp import FastMCP

from generated_tools.checkout import mcp as checkout_mcp
from generated_tools.management import mcp as management_mcp
from generated_tools.payments import mcp as payments_mcp

mcp = FastMCP("adyen")

# Mount sub-MCPs so all tools are discoverable from a single server.
mcp.mount(checkout_mcp)
mcp.mount(management_mcp)
mcp.mount(payments_mcp)


if __name__ == "__main__":
    mcp.run()
