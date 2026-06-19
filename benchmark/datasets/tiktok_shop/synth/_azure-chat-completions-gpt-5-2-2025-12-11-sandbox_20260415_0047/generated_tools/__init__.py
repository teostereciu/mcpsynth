"""TikTok Shop MCP Server (FastMCP).

Tools are organized by API domain modules under generated_tools/.
"""

from __future__ import annotations

from fastmcp import FastMCP

mcp = FastMCP("tiktok-shop")

# Import modules to register tools via decorators.
from . import seller  # noqa: E402,F401
from . import products  # noqa: E402,F401
from . import orders  # noqa: E402,F401
from . import fulfillment  # noqa: E402,F401
from . import promotions  # noqa: E402,F401
from . import finance  # noqa: E402,F401
from . import customer_service  # noqa: E402,F401
from . import returns_refunds  # noqa: E402,F401
from . import webhooks  # noqa: E402,F401
from . import affiliate  # noqa: E402,F401
from . import analytics  # noqa: E402,F401
from . import fbt  # noqa: E402,F401
