from mcp.server.fastmcp import FastMCP

from generated_tools.browse import register as register_browse
from generated_tools.order import register as register_order

mcp = FastMCP("ebay-buy-api")
register_browse(mcp)
register_order(mcp)

if __name__ == "__main__":
    mcp.run()
