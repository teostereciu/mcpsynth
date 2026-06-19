"""Generated MCP tools for eBay Sell APIs."""

from fastmcp import FastMCP

from .client import EbaySellClient

mcp = FastMCP("ebay-sell")

# Instantiate a shared client (stateless aside from token cache)
client = EbaySellClient()

# Import tool modules to register tools via decorators
from . import account as _account  # noqa: F401
from . import analytics as _analytics  # noqa: F401
from . import compliance as _compliance  # noqa: F401
from . import feed as _feed  # noqa: F401
from . import finances as _finances  # noqa: F401
from . import fulfillment as _fulfillment  # noqa: F401
from . import inventory as _inventory  # noqa: F401
from . import logistics as _logistics  # noqa: F401
from . import marketing as _marketing  # noqa: F401
from . import metadata as _metadata  # noqa: F401
from . import negotiation as _negotiation  # noqa: F401
from . import recommendation as _recommendation  # noqa: F401
from . import stores as _stores  # noqa: F401
