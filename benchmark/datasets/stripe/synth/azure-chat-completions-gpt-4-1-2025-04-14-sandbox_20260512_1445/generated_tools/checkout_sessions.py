import os
import requests
from fastmcp import tool

STRIPE_API_KEY = os.environ.get("STRIPE_API_KEY")
BASE_URL = "https://api.stripe.com/v1"
HEADERS = {
    "Authorization": f"Bearer {STRIPE_API_KEY}",
    "Content-Type": "application/x-www-form-urlencoded"
}

@tool("create_checkout_session")
def create_checkout_session(line_items: list, mode: str, success_url: str, automatic_tax: dict = None, client_reference_id: str = None, customer: str = None, customer_email: str = None, metadata: dict = None, return_url: str = None, ui_mode: str = None, currency: str = None, cancel_url: str = None, payment_intent_data: dict = None, payment_method_types: list = None, invoice_creation: dict = None, discounts: list = None, shipping_address_collection: dict = None, shipping_options: list = None, submit_type: str = None, subscription_data: dict = None, tax_id_collection: dict = None):
    """
    Create a Checkout Session object.
    """
    data = {
        "mode": mode,
        "success_url": success_url,
    }
    for i, item in enumerate(line_items):
        for k, v in item.items():
            data[f"line_items[{i}][{k}]"] = v
    if automatic_tax:
        for k, v in automatic_tax.items():
            data[f"automatic_tax[{k}]"] = v
    if client_reference_id:
        data["client_reference_id"] = client_reference_id
    if customer:
        data["customer"] = customer
    if customer_email:
        data["customer_email"] = customer_email
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    if return_url:
        data["return_url"] = return_url
    if ui_mode:
        data["ui_mode"] = ui_mode
    if currency:
        data["currency"] = currency
    if cancel_url:
        data["cancel_url"] = cancel_url
    if payment_intent_data:
        for k, v in payment_intent_data.items():
            data[f"payment_intent_data[{k}]"] = v
    if payment_method_types:
        for i, method in enumerate(payment_method_types):
            data[f"payment_method_types[{i}]"] = method
    if invoice_creation:
        for k, v in invoice_creation.items():
            data[f"invoice_creation[{k}]"] = v
    if discounts:
        for i, discount in enumerate(discounts):
            for k, v in discount.items():
                data[f"discounts[{i}][{k}]"] = v
    if shipping_address_collection:
        for k, v in shipping_address_collection.items():
            data[f"shipping_address_collection[{k}]"] = v
    if shipping_options:
        for i, option in enumerate(shipping_options):
            data[f"shipping_options[{i}]"] = option
    if submit_type:
        data["submit_type"] = submit_type
    if subscription_data:
        for k, v in subscription_data.items():
            data[f"subscription_data[{k}]"] = v
    if tax_id_collection:
        for k, v in tax_id_collection.items():
            data[f"tax_id_collection[{k}]"] = v
    try:
        resp = requests.post(f"{BASE_URL}/checkout/sessions", data=data, headers=HEADERS)
        resp.raise_for_status()
        return resp.json()
    except requests.HTTPError as e:
        return {"error": str(e), "details": resp.text}

@tool("retrieve_checkout_session")
def retrieve_checkout_session(session_id: str):
    """
    Retrieve a Checkout Session object.
    """
    try:
        resp = requests.get(f"{BASE_URL}/checkout/sessions/{session_id}", headers=HEADERS)
        resp.raise_for_status()
        return resp.json()
    except requests.HTTPError as e:
        return {"error": str(e), "details": resp.text}

@tool("update_checkout_session")
def update_checkout_session(session_id: str, metadata: dict = None, invoice_creation: dict = None, discounts: list = None, shipping_address_collection: dict = None, shipping_options: list = None, submit_type: str = None, subscription_data: dict = None, tax_id_collection: dict = None):
    """
    Update a Checkout Session object.
    """
    data = {}
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    if invoice_creation:
        for k, v in invoice_creation.items():
            data[f"invoice_creation[{k}]"] = v
    if discounts:
        for i, discount in enumerate(discounts):
            for k, v in discount.items():
                data[f"discounts[{i}][{k}]"] = v
    if shipping_address_collection:
        for k, v in shipping_address_collection.items():
            data[f"shipping_address_collection[{k}]"] = v
    if shipping_options:
        for i, option in enumerate(shipping_options):
            data[f"shipping_options[{i}]"] = option
    if submit_type:
        data["submit_type"] = submit_type
    if subscription_data:
        for k, v in subscription_data.items():
            data[f"subscription_data[{k}]"] = v
    if tax_id_collection:
        for k, v in tax_id_collection.items():
            data[f"tax_id_collection[{k}]"] = v
    try:
        resp = requests.post(f"{BASE_URL}/checkout/sessions/{session_id}", data=data, headers=HEADERS)
        resp.raise_for_status()
        return resp.json()
    except requests.HTTPError as e:
        return {"error": str(e), "details": resp.text}
