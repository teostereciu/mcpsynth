from mcp.server.fastmcp import FastMCP

from generated_tools.inventory import create_or_replace_inventory_item, get_inventory_item

mcp = FastMCP("ebay-sell")


@mcp.tool()
def inventory_create_or_replace_inventory_item(
    seller_sku: str,
    inventory_item: dict,
    content_language: str = "en-US",
):
    return create_or_replace_inventory_item(seller_sku, inventory_item, content_language=content_language)


@mcp.tool()
def inventory_get_inventory_item(seller_sku: str):
    return get_inventory_item(seller_sku)


if __name__ == "__main__":
    mcp.run()
