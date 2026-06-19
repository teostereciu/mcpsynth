import os
import requests
from fastmcp import tool

STRIPE_API_KEY = os.environ.get("STRIPE_API_KEY")
BASE_URL = "https://api.stripe.com/v1"
HEADERS = {
    "Authorization": f"Bearer {STRIPE_API_KEY}",
    "Content-Type": "application/x-www-form-urlencoded"
}

@tool("create_payment_link")
def create_payment_link(line_items: list, metadata: dict = None, after_completion: dict = None, allow_promotion_codes: bool = None, application_fee_amount: int = None, application_fee_percent: float = None, automatic_tax: dict = None, billing_address_collection: str = None, consent_collection: dict = None, currency: str = None, custom_fields: list = None, custom_text: dict = None, customer_creation: str = None, inactive_message: str = None, invoice_creation: dict = None, name_collection: dict = None, on_behalf_of: str = None, optional_items: list = None, payment_intent_data: dict = None, payment_method_collection: str = None, payment_method_types: list = None, phone_number_collection: dict = None, restrictions: dict = None, shipping_address_collection: dict = None, shipping_options: list = None, submit_type: str = None, subscription_data: dict = None, tax_id_collection: dict = None, transfer_data: dict = None):
    """
    Create a Payment Link object.
    """
    data = {}
    for i, item in enumerate(line_items):
        for k, v in item.items():
            data[f"line_items[{i}][{k}]"] = v
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    if after_completion:
        for k, v in after_completion.items():
            data[f"after_completion[{k}]"] = v
    if allow_promotion_codes is not None:
        data["allow_promotion_codes"] = "true" if allow_promotion_codes else "false"
    if application_fee_amount is not None:
        data["application_fee_amount"] = application_fee_amount
    if application_fee_percent is not None:
        data["application_fee_percent"] = application_fee_percent
    if automatic_tax:
        for k, v in automatic_tax.items():
            data[f"automatic_tax[{k}]"] = v
    if billing_address_collection:
        data["billing_address_collection"] = billing_address_collection
    if consent_collection:
        for k, v in consent_collection.items():
            data[f"consent_collection[{k}]"] = v
    if currency:
        data["currency"] = currency
    if custom_fields:
        for i, field in enumerate(custom_fields):
            data[f"custom_fields[{i}]"] = field
    if custom_text:
        for k, v in custom_text.items():
            data[f"custom_text[{k}]"] = v
    if customer_creation:
        data["customer_creation"] = customer_creation
    if inactive_message:
        data["inactive_message"] = inactive_message
    if invoice_creation:
        for k, v in invoice_creation.items():
            data[f"invoice_creation[{k}]"] = v
    if name_collection:
        for k, v in name_collection.items():
            data[f"name_collection[{k}]"] = v
    if on_behalf_of:
        data["on_behalf_of"] = on_behalf_of
    if optional_items:
        for i, item in enumerate(optional_items):
            data[f"optional_items[{i}]"] = item
    if payment_intent_data:
        for k, v in payment_intent_data.items():
            data[f"payment_intent_data[{k}]"] = v
    if payment_method_collection:
        data["payment_method_collection"] = payment_method_collection
    if payment_method_types:
        for i, method in enumerate(payment_method_types):
            data[f"payment_method_types[{i}]"] = method
    if phone_number_collection:
        for k, v in phone_number_collection.items():
            data[f"phone_number_collection[{k}]"] = v
    if restrictions:
        for k, v in restrictions.items():
            data[f"restrictions[{k}]"] = v
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
    if transfer_data:
        for k, v in transfer_data.items():
            data[f"transfer_data[{k}]"] = v
    try:
        resp = requests.post(f"{BASE_URL}/payment_links", data=data, headers=HEADERS)
        resp.raise_for_status()
        return resp.json()
    except requests.HTTPError as e:
        return {"error": str(e), "details": resp.text}

@tool("update_payment_link")
def update_payment_link(payment_link_id: str, active: bool = None, line_items: list = None, metadata: dict = None, after_completion: dict = None, allow_promotion_codes: bool = None, automatic_tax: dict = None, billing_address_collection: str = None, custom_fields: list = None, custom_text: dict = None, customer_creation: str = None, inactive_message: str = None, invoice_creation: dict = None, name_collection: dict = None, optional_items: list = None, payment_intent_data: dict = None, payment_method_collection: str = None, payment_method_types: list = None, phone_number_collection: dict = None, restrictions: dict = None, shipping_address_collection: dict = None, shipping_options: list = None, submit_type: str = None, subscription_data: dict = None, tax_id_collection: dict = None):
    """
    Update a Payment Link object.
    """
    data = {}
    if active is not None:
        data["active"] = "true" if active else "false"
    if line_items:
        for i, item in enumerate(line_items):
            for k, v in item.items():
                data[f"line_items[{i}][{k}]"] = v
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    if after_completion:
        for k, v in after_completion.items():
            data[f"after_completion[{k}]"] = v
    if allow_promotion_codes is not None:
        data["allow_promotion_codes"] = "true" if allow_promotion_codes else "false"
    if automatic_tax:
        for k, v in automatic_tax.items():
            data[f"automatic_tax[{k}]"] = v
    if billing_address_collection:
        data["billing_address_collection"] = billing_address_collection
    if custom_fields:
        for i, field in enumerate(custom_fields):
            data[f"custom_fields[{i}]"] = field
    if custom_text:
        for k, v in custom_text.items():
            data[f"custom_text[{k}]"] = v
    if customer_creation:
        data["customer_creation"] = customer_creation
    if inactive_message:
        data["inactive_message"] = inactive_message
    if invoice_creation:
        for k, v in invoice_creation.items():
            data[f"invoice_creation[{k}]"] = v
    if name_collection:
        for k, v in name_collection.items():
            data[f"name_collection[{k}]"] = v
    if optional_items:
        for i, item in enumerate(optional_items):
            data[f"optional_items[{i}]"] = item
    if payment_intent_data:
        for k, v in payment_intent_data.items():
            data[f"payment_intent_data[{k}]"] = v
    if payment_method_collection:
        data["payment_method_collection"] = payment_method_collection
    if payment_method_types:
        for i, method in enumerate(payment_method_types):
            data[f"payment_method_types[{i}]"] = method
    if phone_number_collection:
        for k, v in phone_number_collection.items():
            data[f"phone_number_collection[{k}]"] = v
    if restrictions:
        for k, v in restrictions.items():
            data[f"restrictions[{k}]"] = v
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
        resp = requests.post(f"{BASE_URL}/payment_links/{payment_link_id}", data=data, headers=HEADERS)
        resp.raise_for_status()
        return resp.json()
    except requests.HTTPError as e:
        return {"error": str(e), "details": resp.text}
