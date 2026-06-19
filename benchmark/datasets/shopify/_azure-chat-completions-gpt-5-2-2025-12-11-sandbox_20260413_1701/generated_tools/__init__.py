"""Shopify Admin REST API MCP server tools."""

from fastmcp import FastMCP

from .client import ShopifyAdminClient

mcp = FastMCP("shopify-admin")

# Shared client instance (reads env vars at call time)
client = ShopifyAdminClient()

# Import tool modules so decorators register tools
from . import shop  # noqa: E402,F401
from . import products  # noqa: E402,F401
from . import orders  # noqa: E402,F401
from . import customers  # noqa: E402,F401
from . import inventory  # noqa: E402,F401
from . import discounts  # noqa: E402,F401
from . import fulfillment  # noqa: E402,F401
from . import webhooks  # noqa: E402,F401
from . import content  # noqa: E402,F401
from . import finance  # noqa: E402,F401
from . import store_config  # noqa: E402,F401
