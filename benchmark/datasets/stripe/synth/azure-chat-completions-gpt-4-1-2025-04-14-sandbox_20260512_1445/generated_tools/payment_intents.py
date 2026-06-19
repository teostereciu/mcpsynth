import os
import requests
from fastmcp import tool

STRIPE_API_KEY = os.environ.get("STRIPE_API_KEY")
BASE_URL = "https://api.stripe.com/v1"
HEADERS = {
    "Authorization": f"Bearer {STRIPE_API_KEY}",
    "Content-Type": "application/x-www-form-urlencoded"
}

@tool("create_payment_intent")
def create_payment_intent(amount: int, currency: str, customer: str = None, description: str = None, metadata: dict = None, receipt_email: str = None, setup_future_usage: str = None, shipping: dict = None, statement_descriptor: str = None, statement_descriptor_suffix: str = None, automatic_payment_methods: dict = None, confirm: bool = False, payment_method: str = None):
    """
    Create a PaymentIntent object.
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
    if setup_future_usage:
        data["setup_future_usage"] = setup_future_usage
    if shipping:
        for k, v in shipping.items():
            data[f"shipping[{k}]"] = v
    if statement_descriptor:
        data["statement_descriptor"] = statement_descriptor
    if statement_descriptor_suffix:
        data["statement_descriptor_suffix"] = statement_descriptor_suffix
    if automatic_payment_methods:
        for k, v in automatic_payment_methods.items():
            data[f"automatic_payment_methods[{k}]"] = v
    if confirm:
        data["confirm"] = "true"
    if payment_method:
        data["payment_method"] = payment_method

    try:
        resp = requests.post(f"{BASE_URL}/payment_intents", data=data, headers=HEADERS)
        resp.raise_for_status()
        return resp.json()
    except requests.HTTPError as e:
        return {"error": str(e), "details": resp.text}

@tool("retrieve_payment_intent")
def retrieve_payment_intent(payment_intent_id: str):
    """
    Retrieve a PaymentIntent object.
    """
    try:
        resp = requests.get(f"{BASE_URL}/payment_intents/{payment_intent_id}", headers=HEADERS)
        resp.raise_for_status()
        return resp.json()
    except requests.HTTPError as e:
        return {"error": str(e), "details": resp.text}

@tool("update_payment_intent")
def update_payment_intent(payment_intent_id: str, description: str = None, metadata: dict = None, receipt_email: str = None, shipping: dict = None):
    """
    Update a PaymentIntent object.
    """
    data = {}
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
        resp = requests.post(f"{BASE_URL}/payment_intents/{payment_intent_id}", data=data, headers=HEADERS)
        resp.raise_for_status()
        return resp.json()
    except requests.HTTPError as e:
        return {"error": str(e), "details": resp.text}

@tool("cancel_payment_intent")
def cancel_payment_intent(payment_intent_id: str):
    """
    Cancel a PaymentIntent object.
    """
    try:
        resp = requests.post(f"{BASE_URL}/payment_intents/{payment_intent_id}/cancel", headers=HEADERS)
        resp.raise_for_status()
        return resp.json()
    except requests.HTTPError as e:
        return {"error": str(e), "details": resp.text}
