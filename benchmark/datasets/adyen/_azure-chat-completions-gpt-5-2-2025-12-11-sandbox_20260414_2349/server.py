"""Adyen MCP Server (FastMCP)."""

from __future__ import annotations

from fastmcp import FastMCP

from generated_tools.checkout import mcp as checkout_mcp
from generated_tools.management import mcp as management_mcp

mcp = FastMCP("adyen")

# Mount tool modules
mcp.mount(checkout_mcp)
mcp.mount(management_mcp)


if __name__ == "__main__":
    mcp.run()
