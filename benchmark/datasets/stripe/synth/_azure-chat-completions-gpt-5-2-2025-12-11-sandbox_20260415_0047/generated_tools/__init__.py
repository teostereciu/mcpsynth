"""Stripe MCP server tools package."""

from __future__ import annotations

from fastmcp import FastMCP

mcp = FastMCP("stripe-mcp")

# Import modules to register tools
from . import core  # noqa: E402,F401
from . import payments  # noqa: E402,F401
from . import customers  # noqa: E402,F401
from . import billing  # noqa: E402,F401
from . import checkout  # noqa: E402,F401
from . import tax  # noqa: E402,F401
from . import radar  # noqa: E402,F401
from . import financial_connections  # noqa: E402,F401
from . import balance_tools  # noqa: E402,F401
from . import webhooks  # noqa: E402,F401
