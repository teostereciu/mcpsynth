from mcp.server.fastmcp import FastMCP

from generated_tools.customers import *
from generated_tools.fulfillment import *
from generated_tools.inventory import *
from generated_tools.meta_webhooks import *
from generated_tools.orders import *
from generated_tools.products import *

mcp = FastMCP("shopify-admin-rest")

for name, fn in list(globals().items()):
    if callable(fn) and getattr(fn, "__module__", "").startswith("generated_tools."):
        mcp.tool()(fn)


if __name__ == "__main__":
    mcp.run()
