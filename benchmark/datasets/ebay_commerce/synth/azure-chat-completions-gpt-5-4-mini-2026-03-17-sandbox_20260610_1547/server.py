from mcp.server.fastmcp import FastMCP

from generated_tools.catalog import get_product, search_products
from generated_tools.charity import get_charity_org, get_charity_orgs
from generated_tools.identity import get_user

mcp = FastMCP("ebay-commerce-api")

mcp.tool()(search_products)
mcp.tool()(get_product)
mcp.tool()(get_user)
mcp.tool()(get_charity_org)
mcp.tool()(get_charity_orgs)

if __name__ == "__main__":
    mcp.run()
