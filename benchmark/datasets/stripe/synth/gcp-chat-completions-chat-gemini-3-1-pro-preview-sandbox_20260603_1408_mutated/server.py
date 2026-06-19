import os
import requests
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Stripe MCP Server")

STRIPE_API_KEY = os.environ.get("STRIPE_API_KEY")
BASE_URL = "https://api.stripe.com/v1"

def make_request(method, path, data=None, params=None):
    if not STRIPE_API_KEY:
        return {"error": "STRIPE_API_KEY environment variable is not set"}
    
    url = f"{BASE_URL}{path}"
    headers = {
        "Authorization": f"Bearer {STRIPE_API_KEY}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    
    try:
        response = requests.request(method, url, headers=headers, data=data, params=params)
        return response.json()
    except Exception as e:
        return {"error": str(e)}

# Import tools from generated_tools
import generated_tools.payment_intents
import generated_tools.charges
import generated_tools.refunds
import generated_tools.customers
import generated_tools.products
import generated_tools.prices
import generated_tools.subscriptions
import generated_tools.invoices
import generated_tools.checkout_sessions
import generated_tools.payment_links
import generated_tools.connect
import generated_tools.setup_intents
import generated_tools.coupons
import generated_tools.promotion_codes

if __name__ == "__main__":
    mcp.run()
