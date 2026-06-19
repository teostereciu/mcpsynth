import os
import requests
from fastmcp import tool

STRIPE_API_KEY = os.environ.get("STRIPE_API_KEY")
BASE_URL = "https://api.stripe.com/v1"
HEADERS = {
    "Authorization": f"Bearer {STRIPE_API_KEY}",
    "Content-Type": "application/x-www-form-urlencoded"
}

@tool("create_charge")
def create_charge(amount: int, currency: str, customer: str = None, description: str = None, metadata: dict = None, receipt_email: str = None, shipping: dict = None, source: str = None, statement_descriptor: str = None, statement_descriptor_suffix: str = None, application_fee_amount: int = None, capture: bool = True, on_behalf_of: str = None, transfer_data: dict = None, transfer_group: str = None):
    """
    Create a Charge object (deprecated, use Payment Intents for new integrations).
    """
    data = {
        "amount": amount,
        "currency": currency,
    }
    if customer:
        data["customer"] = customer
    if description:
        data["description"] = description
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    if receipt_email:
        data["receipt_email"] = receipt_email
    if shipping:
        for k, v in shipping.items():
            data[f"shipping[{k}]"] = v
    if source:
        data["source"] = source
    if statement_descriptor:
        data["statement_descriptor"] = statement_descriptor
    if statement_descriptor_suffix:
        data["statement_descriptor_suffix"] = statement_descriptor_suffix
    if application_fee_amount:
        data["application_fee_amount"] = application_fee_amount
    if capture is not None:
        data["capture"] = "true" if capture else "false"
    if on_behalf_of:
        data["on_behalf_of"] = on_behalf_of
    if transfer_data:
        for k, v in transfer_data.items():
            data[f"transfer_data[{k}]"] = v
    if transfer_group:
        data["transfer_group"] = transfer_group

    try:
        resp = requests.post(f"{BASE_URL}/charges", data=data, headers=HEADERS)
        resp.raise_for_status()
        return resp.json()
    except requests.HTTPError as e:
        return {"error": str(e), "details": resp.text}

@tool("retrieve_charge")
def retrieve_charge(charge_id: str):
    """
    Retrieve a Charge object.
    """
    try:
        resp = requests.get(f"{BASE_URL}/charges/{charge_id}", headers=HEADERS)
        resp.raise_for_status()
        return resp.json()
    except requests.HTTPError as e:
        return {"error": str(e), "details": resp.text}

@tool("update_charge")
def update_charge(charge_id: str, customer: str = None, description: str = None, metadata: dict = None, receipt_email: str = None, shipping: dict = None):
    """
    Update a Charge object.
    """
    data = {}
    if customer:
        data["customer"] = customer
    if description:
        data["description"] = description
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    if receipt_email:
        data["receipt_email"] = receipt_email
    if shipping:
        for k, v in shipping.items():
            data[f"shipping[{k}]"] = v
    try:
        resp = requests.post(f"{BASE_URL}/charges/{charge_id}", data=data, headers=HEADERS)
        resp.raise_for_status()
        return resp.json()
    except requests.HTTPError as e:
        return {"error": str(e), "details": resp.text}
