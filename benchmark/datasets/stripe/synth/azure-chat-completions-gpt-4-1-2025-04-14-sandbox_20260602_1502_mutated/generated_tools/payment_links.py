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
def create_payment_link(line_items: list, metadata: dict = None):
    """
    Create a Payment Link.
    Required: line_items (list of dicts)
    Optional: metadata (dict)
    """
    url = f"{BASE_URL}/payment_links"
    data = {}
    for idx, item in enumerate(line_items):
        for k, v in item.items():
            data[f"line_items[{idx}][{k}]"] = v
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    resp = requests.post(url, headers=HEADERS, data=data)
    return _handle_response(resp)

@mcp_tool
def retrieve_payment_link(payment_link_id: str):
    """
    Retrieve a Payment Link by ID.
    """
    url = f"{BASE_URL}/payment_links/{payment_link_id}"
    resp = requests.get(url, headers=HEADERS)
    return _handle_response(resp)
