from mcp.server.fastmcp import FastMCP
import json

mcp = FastMCP("ebay-buy-api")

@mcp.tool()
def search_items(q: str = None, category_ids: str = None, limit: int = 10, offset: int = 0):
    return {"q": q, "category_ids": category_ids, "limit": limit, "offset": offset}

@mcp.tool()
def get_item(listing_id: str, fieldgroups: str = None):
    return {"listing_id": listing_id, "fieldgroups": fieldgroups}

@mcp.tool()
def get_guest_checkout_session(checkoutSessionId: str):
    return {"checkoutSessionId": checkoutSessionId}

if __name__ == "__main__":
    mcp.run()
