import os
import requests
from mcp_tools import mcp_tool

BASE_URL = "https://api.stripe.com/v1"
API_KEY = os.environ.get("STRIPE_API_KEY")
HEADERS = {"Authorization": f"Bearer {API_KEY}"}

def _handle_response(resp):
    try:
        resp.raise_for_status()
        return resp.json()
    except requests.HTTPError:
        try:
            return {"error": resp.json()}
        except Exception:
            return {"error": resp.text}

@mcp_tool
def create_subscription(customer: str, items: list, currency: str = None, description: str = None, metadata: dict = None):
    """
    Create a Subscription for a customer.
    Required: customer (str), items (list of dicts with 'price' and optional 'quantity')
    Optional: currency (str), description (str), metadata (dict)
    """
    url = f"{BASE_URL}/subscriptions"
    data = {"customer": customer}
    if currency:
        data["currency"] = currency
    if description:
        data["description"] = description
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    for idx, item in enumerate(items):
        for k, v in item.items():
            data[f"items[{idx}][{k}]"] = v
    resp = requests.post(url, headers=HEADERS, data=data)
    return _handle_response(resp)

@mcp_tool
def retrieve_subscription(subscription_id: str):
    """
    Retrieve a Subscription object by ID.
    """
    url = f"{BASE_URL}/subscriptions/{subscription_id}"
    resp = requests.get(url, headers=HEADERS)
    return _handle_response(resp)

@mcp_tool
def update_subscription(subscription_id: str, description: str = None, metadata: dict = None):
    """
    Update a Subscription object. Only description and metadata are supported here.
    """
    url = f"{BASE_URL}/subscriptions/{subscription_id}"
    data = {}
    if description:
        data["description"] = description
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    resp = requests.post(url, headers=HEADERS, data=data)
    return _handle_response(resp)
