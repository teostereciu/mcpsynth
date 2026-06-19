"""Google Workspace MCP Server - generated_tools package."""

from fastmcp import FastMCP

mcp = FastMCP("Google Workspace MCP Server")

# Import all tool modules to register their tools
from generated_tools import gmail          # noqa: F401, E402
from generated_tools import calendar      # noqa: F401, E402
from generated_tools import drive         # noqa: F401, E402
from generated_tools import docs          # noqa: F401, E402
from generated_tools import slides        # noqa: F401, E402
from generated_tools import sheets        # noqa: F401, E402

__all__ = ["mcp"]
