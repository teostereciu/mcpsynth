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
def create_refund(charge: str = None, payment_intent: str = None, amount: int = None, reason: str = None, metadata: dict = None):
    """
    Create a refund for a charge or payment_intent.
    Required: charge or payment_intent
    Optional: amount (int), reason (str), metadata (dict)
    """
    url = f"{BASE_URL}/refunds"
    data = {}
    if charge:
        data["charge"] = charge
    if payment_intent:
        data["payment_intent"] = payment_intent
    if amount:
        data["amount"] = amount
    if reason:
        data["reason"] = reason
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    resp = requests.post(url, headers=HEADERS, data=data)
    return _handle_response(resp)

@mcp_tool
def retrieve_refund(refund_id: str):
    """
    Retrieve a Refund object by ID.
    """
    url = f"{BASE_URL}/refunds/{refund_id}"
    resp = requests.get(url, headers=HEADERS)
    return _handle_response(resp)

@mcp_tool
def update_refund(refund_id: str, metadata: dict = None):
    """
    Update a Refund object. Only metadata is supported here.
    """
    url = f"{BASE_URL}/refunds/{refund_id}"
    data = {}
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    resp = requests.post(url, headers=HEADERS, data=data)
    return _handle_response(resp)
