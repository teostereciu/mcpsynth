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
def create_payment_intent(amount: int, currency: str, customer: str = None, description: str = None, payment_method: str = None, receipt_email: str = None, confirm: bool = False, metadata: dict = None):
    """
    Create a PaymentIntent object.
    Required: amount (int, smallest currency unit), currency (str)
    Optional: customer (str), description (str), payment_method (str), receipt_email (str), confirm (bool), metadata (dict)
    """
    url = f"{BASE_URL}/payment_intents"
    data = {
        "amount": amount,
        "currency": currency,
    }
    if customer:
        data["customer"] = customer
    if description:
        data["description"] = description
    if payment_method:
        data["payment_method"] = payment_method
    if receipt_email:
        data["receipt_email"] = receipt_email
    if confirm:
        data["confirm"] = "true"
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    resp = requests.post(url, headers=HEADERS, data=data)
    return _handle_response(resp)

@mcp_tool
def retrieve_payment_intent(payment_intent_id: str):
    """
    Retrieve a PaymentIntent object by ID.
    """
    url = f"{BASE_URL}/payment_intents/{payment_intent_id}"
    resp = requests.get(url, headers=HEADERS)
    return _handle_response(resp)

@mcp_tool
def update_payment_intent(payment_intent_id: str, description: str = None, metadata: dict = None):
    """
    Update a PaymentIntent object. Only description and metadata are supported here.
    """
    url = f"{BASE_URL}/payment_intents/{payment_intent_id}"
    data = {}
    if description:
        data["description"] = description
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    resp = requests.post(url, headers=HEADERS, data=data)
    return _handle_response(resp)
