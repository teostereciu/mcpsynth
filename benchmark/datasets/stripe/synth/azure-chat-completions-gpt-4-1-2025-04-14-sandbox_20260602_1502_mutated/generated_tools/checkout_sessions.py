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
def create_checkout_session(line_items: list, mode: str, success_url: str, cancel_url: str = None, customer: str = None, customer_email: str = None, metadata: dict = None):
    """
    Create a Checkout Session.
    Required: line_items (list of dicts), mode (str), success_url (str)
    Optional: cancel_url (str), customer (str), customer_email (str), metadata (dict)
    """
    url = f"{BASE_URL}/checkout/sessions"
    data = {
        "mode": mode,
        "success_url": success_url
    }
    if cancel_url:
        data["cancel_url"] = cancel_url
    if customer:
        data["customer"] = customer
    if customer_email:
        data["customer_email"] = customer_email
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    for idx, item in enumerate(line_items):
        for k, v in item.items():
            data[f"line_items[{idx}][{k}]"] = v
    resp = requests.post(url, headers=HEADERS, data=data)
    return _handle_response(resp)

@mcp_tool
def retrieve_checkout_session(session_id: str):
    """
    Retrieve a Checkout Session by ID.
    """
    url = f"{BASE_URL}/checkout/sessions/{session_id}"
    resp = requests.get(url, headers=HEADERS)
    return _handle_response(resp)
