import os
import requests
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("ShopifyAdmin")

# Helper function for API requests
def make_shopify_request(method: str, endpoint: str, json_data: dict = None, params: dict = None):
    store_url = os.environ.get("SHOPIFY_STORE_URL")
    access_token = os.environ.get("SHOPIFY_ACCESS_TOKEN")
    
    if not store_url or not access_token:
        return {"error": "Missing SHOPIFY_STORE_URL or SHOPIFY_ACCESS_TOKEN environment variables"}
    
    # Remove protocol if included in store_url
    store_url = store_url.replace("https://", "").replace("http://", "")
    
    base_url = f"https://{store_url}/admin/api/2026-01"
    url = f"{base_url}{endpoint}"
    
    headers = {
        "X-Shopify-Access-Token": access_token,
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    
    try:
        response = requests.request(method, url, headers=headers, json=json_data, params=params)
        
        # Return empty dict for 204 No Content
        if response.status_code == 204:
            return {}
            
        try:
            return response.json()
        except ValueError:
            return {"error": f"Invalid JSON response. Status code: {response.status_code}", "text": response.text}
            
    except Exception as e:
        return {"error": str(e)}

# Import tool modules
import generated_tools.products
import generated_tools.orders
import generated_tools.fulfillment
import generated_tools.customers
import generated_tools.inventory
import generated_tools.discounts
import generated_tools.webhooks
import generated_tools.metafields

generated_tools.products.register_tools(mcp, make_shopify_request)
generated_tools.orders.register_tools(mcp, make_shopify_request)
generated_tools.fulfillment.register_tools(mcp, make_shopify_request)
generated_tools.customers.register_tools(mcp, make_shopify_request)
generated_tools.inventory.register_tools(mcp, make_shopify_request)
generated_tools.discounts.register_tools(mcp, make_shopify_request)
generated_tools.webhooks.register_tools(mcp, make_shopify_request)
generated_tools.metafields.register_tools(mcp, make_shopify_request)

if __name__ == "__main__":
    mcp.run()
