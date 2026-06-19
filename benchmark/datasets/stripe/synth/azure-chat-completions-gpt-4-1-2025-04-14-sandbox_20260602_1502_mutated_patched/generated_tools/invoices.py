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
def retrieve_invoice(invoice_id: str):
    """
    Retrieve an Invoice object by ID.
    """
    url = f"{BASE_URL}/invoices/{invoice_id}"
    resp = requests.get(url, headers=HEADERS)
    return _handle_response(resp)

@mcp_tool
def create_invoice_preview(customer: str = None, subscription: str = None):
    """
    Preview an upcoming invoice for a customer or subscription.
    """
    url = f"{BASE_URL}/invoices/create_preview"
    data = {}
    if customer:
        data["customer"] = customer
    if subscription:
        data["subscription"] = subscription
    resp = requests.post(url, headers=HEADERS, data=data)
    return _handle_response(resp)
