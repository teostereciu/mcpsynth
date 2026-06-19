import os
import requests
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
app = FastMCP()

# Base URL for Stripe API
BASE_URL = "https://api.stripe.com"

# Stripe API Key from environment variable
STRIPE_API_KEY = os.environ.get("STRIPE_API_KEY")
if not STRIPE_API_KEY:
    raise ValueError("STRIPE_API_KEY environment variable not set.")

# Helper function for making Stripe API requests
def _make_stripe_request(method, path, data=None):
    headers = {
        "Authorization": f"Bearer {STRIPE_API_KEY}",
        "Content-Type": "application/x-www-form-urlencoded",
    }
    url = f"{BASE_URL}{path}"

    try:
        if method == "GET":
            response = requests.get(url, headers=headers, params=data)
        elif method == "POST":
            response = requests.post(url, headers=headers, data=data)
        elif method == "DELETE":
            response = requests.delete(url, headers=headers, data=data)
        else:
            return {"error": f"Unsupported HTTP method: {method}"}

        response.raise_for_status()  # Raise an exception for HTTP errors

        # Stripe API often returns JSON, but sometimes just success/error
        try:
            return response.json()
        except requests.exceptions.JSONDecodeError:
            return {"message": "Success", "status_code": response.status_code}

    except requests.exceptions.HTTPError as e:
        try:
            error_json = e.response.json()
            return {"error": error_json}
        except requests.exceptions.JSONDecodeError:
            return {"error": str(e), "status_code": e.response.status_code}
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

# Placeholder for grounding.json content
grounding_data = {}

# This will be populated by generated tools
# For example:
# @app.tool()
# def create_payment_intent(amount: int, currency: str):
#     """Creates a new Payment Intent."""
#     return _make_stripe_request("POST", "/v1/payment_intents", {"amount": amount, "currency": currency})

# Run the server
if __name__ == "__main__":
    app.run()
