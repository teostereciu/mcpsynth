from mcp.server.fastmcp import FastMCP

from generated_tools.common import request_json
from generated_tools.media import get_image
from generated_tools.notification import get_subscriptions

mcp = FastMCP("ebay-commerce-api")


@mcp.tool()
def get_product(epid: str):
    return request_json("GET", f"/commerce/catalog/v1_beta/product/{epid}", token_type="app")


@mcp.tool()
def search_products(query: str = None, gtin: str = None, mpn: str = None, category_id: str = None, aspects: str = None, field_groups: str = None, page_size: int = None):
    params = {}
    if query is not None:
        params["query"] = query
    if gtin is not None:
        params["gtin"] = gtin
    if mpn is not None:
        params["mpn"] = mpn
    if category_id is not None:
        params["category_id"] = category_id
    if aspects is not None:
        params["aspects"] = aspects
    if field_groups is not None:
        params["field_groups"] = field_groups
    if page_size is not None:
        params["page_size"] = page_size
    return request_json("GET", "/commerce/catalog/v1_beta/product_summary/search", token_type="app", params=params)


@mcp.tool()
def get_image_tool(image_id: str):
    return get_image(image_id)


@mcp.tool()
def get_subscriptions_tool(page_size: int = None, continuation_token: str = None):
    return get_subscriptions(page_size=page_size, continuation_token=continuation_token)


if __name__ == "__main__":
    mcp.run()
