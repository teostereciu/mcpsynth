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
def create_price(currency: str, product: str = None, unit_amount: int = None, recurring: dict = None, active: bool = True, nickname: str = None, metadata: dict = None):
    """
    Create a Price for a Product. Required: currency. One of product or product_data is required, but only product is supported here. unit_amount is required unless custom_unit_amount is used.
    """
    url = f"{BASE_URL}/prices"
    data = {"currency": currency}
    if product:
        data["product"] = product
    if unit_amount is not None:
        data["unit_amount"] = unit_amount
    if recurring:
        for k, v in recurring.items():
            data[f"recurring[{k}]"] = v
    if active is not None:
        data["active"] = str(active).lower()
    if nickname:
        data["nickname"] = nickname
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    resp = requests.post(url, headers=HEADERS, data=data)
    return _handle_response(resp)

@mcp_tool
def retrieve_price(price_id: str):
    """
    Retrieve a Price object by ID.
    """
    url = f"{BASE_URL}/prices/{price_id}"
    resp = requests.get(url, headers=HEADERS)
    return _handle_response(resp)

@mcp_tool
def update_price(price_id: str, active: bool = None, nickname: str = None, metadata: dict = None):
    """
    Update a Price object. Optional fields: active, nickname, metadata
    """
    url = f"{BASE_URL}/prices/{price_id}"
    data = {}
    if active is not None:
        data["active"] = str(active).lower()
    if nickname:
        data["nickname"] = nickname
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    resp = requests.post(url, headers=HEADERS, data=data)
    return _handle_response(resp)
