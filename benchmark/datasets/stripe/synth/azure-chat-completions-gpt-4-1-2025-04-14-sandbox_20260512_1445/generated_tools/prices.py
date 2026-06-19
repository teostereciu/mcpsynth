import os
import requests
from fastmcp import tool

STRIPE_API_KEY = os.environ.get("STRIPE_API_KEY")
BASE_URL = "https://api.stripe.com/v1"
HEADERS = {
    "Authorization": f"Bearer {STRIPE_API_KEY}",
    "Content-Type": "application/x-www-form-urlencoded"
}

@tool("create_price")
def create_price(currency: str, product: str = None, active: bool = True, metadata: dict = None, nickname: str = None, recurring: dict = None, tax_behavior: str = None, unit_amount: int = None, billing_scheme: str = None, currency_options: dict = None, custom_unit_amount: dict = None, lookup_key: str = None, product_data: dict = None, tiers: list = None, tiers_mode: str = None, transfer_lookup_key: bool = None, transform_quantity: dict = None, unit_amount_decimal: str = None):
    """
    Create a Price object.
    """
    data = {
        "currency": currency,
        "active": "true" if active else "false"
    }
    if product:
        data["product"] = product
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    if nickname:
        data["nickname"] = nickname
    if recurring:
        for k, v in recurring.items():
            data[f"recurring[{k}]"] = v
    if tax_behavior:
        data["tax_behavior"] = tax_behavior
    if unit_amount is not None:
        data["unit_amount"] = unit_amount
    if billing_scheme:
        data["billing_scheme"] = billing_scheme
    if currency_options:
        for k, v in currency_options.items():
            data[f"currency_options[{k}]"] = v
    if custom_unit_amount:
        for k, v in custom_unit_amount.items():
            data[f"custom_unit_amount[{k}]"] = v
    if lookup_key:
        data["lookup_key"] = lookup_key
    if product_data:
        for k, v in product_data.items():
            data[f"product_data[{k}]"] = v
    if tiers:
        for i, tier in enumerate(tiers):
            data[f"tiers[{i}]"] = tier
    if tiers_mode:
        data["tiers_mode"] = tiers_mode
    if transfer_lookup_key is not None:
        data["transfer_lookup_key"] = "true" if transfer_lookup_key else "false"
    if transform_quantity:
        for k, v in transform_quantity.items():
            data[f"transform_quantity[{k}]"] = v
    if unit_amount_decimal:
        data["unit_amount_decimal"] = unit_amount_decimal
    try:
        resp = requests.post(f"{BASE_URL}/prices", data=data, headers=HEADERS)
        resp.raise_for_status()
        return resp.json()
    except requests.HTTPError as e:
        return {"error": str(e), "details": resp.text}

@tool("retrieve_price")
def retrieve_price(price_id: str):
    """
    Retrieve a Price object.
    """
    try:
        resp = requests.get(f"{BASE_URL}/prices/{price_id}", headers=HEADERS)
        resp.raise_for_status()
        return resp.json()
    except requests.HTTPError as e:
        return {"error": str(e), "details": resp.text}

@tool("update_price")
def update_price(price_id: str, active: bool = None, metadata: dict = None, nickname: str = None, tax_behavior: str = None, currency_options: dict = None, lookup_key: str = None, transfer_lookup_key: bool = None):
    """
    Update a Price object.
    """
    data = {}
    if active is not None:
        data["active"] = "true" if active else "false"
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    if nickname:
        data["nickname"] = nickname
    if tax_behavior:
        data["tax_behavior"] = tax_behavior
    if currency_options:
        for k, v in currency_options.items():
            data[f"currency_options[{k}]"] = v
    if lookup_key:
        data["lookup_key"] = lookup_key
    if transfer_lookup_key is not None:
        data["transfer_lookup_key"] = "true" if transfer_lookup_key else "false"
    try:
        resp = requests.post(f"{BASE_URL}/prices/{price_id}", data=data, headers=HEADERS)
        resp.raise_for_status()
        return resp.json()
    except requests.HTTPError as e:
        return {"error": str(e), "details": resp.text}
