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
def retrieve_charge(charge_id: str):
    """
    Retrieve a Charge object by ID.
    """
    url = f"{BASE_URL}/charges/{charge_id}"
    resp = requests.get(url, headers=HEADERS)
    return _handle_response(resp)

@mcp_tool
def update_charge(charge_id: str, description: str = None, metadata: dict = None, receipt_email: str = None):
    """
    Update a Charge object. Only description, metadata, and receipt_email are supported here.
    """
    url = f"{BASE_URL}/charges/{charge_id}"
    data = {}
    if description:
        data["description"] = description
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    if receipt_email:
        data["receipt_email"] = receipt_email
    resp = requests.post(url, headers=HEADERS, data=data)
    return _handle_response(resp)
