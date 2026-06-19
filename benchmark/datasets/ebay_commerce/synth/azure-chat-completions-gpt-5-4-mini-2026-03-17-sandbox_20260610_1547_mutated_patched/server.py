from mcp.server.fastmcp import FastMCP

from generated_tools.catalog import get_product, search_products
from generated_tools.identity import get_user
from generated_tools.media import create_document

mcp = FastMCP("ebay-commerce-api")

mcp.tool()(get_product)
mcp.tool()(search_products)
mcp.tool()(get_user)
mcp.tool()(create_document)

if __name__ == "__main__":
    mcp.run()
