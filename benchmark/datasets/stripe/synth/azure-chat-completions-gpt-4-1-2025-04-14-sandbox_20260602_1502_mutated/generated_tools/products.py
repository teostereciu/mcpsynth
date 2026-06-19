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
def create_product(name: str, active: bool = True, description: str = None, metadata: dict = None):
    """
    Create a Product object.
    Required: name
    Optional: active, description, metadata
    """
    url = f"{BASE_URL}/products"
    data = {"name": name}
    if active is not None:
        data["active"] = str(active).lower()
    if description:
        data["description"] = description
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    resp = requests.post(url, headers=HEADERS, data=data)
    return _handle_response(resp)

@mcp_tool
def retrieve_product(product_id: str):
    """
    Retrieve a Product object by ID.
    """
    url = f"{BASE_URL}/products/{product_id}"
    resp = requests.get(url, headers=HEADERS)
    return _handle_response(resp)

@mcp_tool
def update_product(product_id: str, name: str = None, active: bool = None, description: str = None, metadata: dict = None):
    """
    Update a Product object. Optional fields: name, active, description, metadata
    """
    url = f"{BASE_URL}/products/{product_id}"
    data = {}
    if name:
        data["name"] = name
    if active is not None:
        data["active"] = str(active).lower()
    if description:
        data["description"] = description
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    resp = requests.post(url, headers=HEADERS, data=data)
    return _handle_response(resp)
