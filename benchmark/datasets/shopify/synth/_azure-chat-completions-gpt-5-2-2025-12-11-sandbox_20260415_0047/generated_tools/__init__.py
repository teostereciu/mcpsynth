from fastmcp import FastMCP

mcp = FastMCP("shopify-admin")

# Register tools
from . import shop as _shop  # noqa: F401
from . import products as _products  # noqa: F401
from . import orders as _orders  # noqa: F401
from . import customers as _customers  # noqa: F401
from . import inventory as _inventory  # noqa: F401
from . import discounts as _discounts  # noqa: F401
from . import fulfillment as _fulfillment  # noqa: F401
from . import webhooks as _webhooks  # noqa: F401
