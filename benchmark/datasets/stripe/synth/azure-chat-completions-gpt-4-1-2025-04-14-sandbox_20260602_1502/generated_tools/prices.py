import os
import requests
from typing import Any, Dict

STRIPE_API_KEY = os.environ.get("STRIPE_API_KEY")
BASE_URL = "https://api.stripe.com/v1"

HEADERS = {
    "Authorization": f"Bearer {STRIPE_API_KEY}",
    "Content-Type": "application/x-www-form-urlencoded"
}

def create_price(currency: str, product: str = None, unit_amount: int = None, **kwargs) -> Dict[str, Any]:
    """
    Create a new price for an existing product.
    Required: currency (str), product (str or product_data), unit_amount (int or custom_unit_amount)
    Optional: active (bool), metadata (dict), nickname (str), recurring (dict), tax_behavior (str), billing_scheme (str), currency_options (dict), custom_unit_amount (dict), lookup_key (str), tiers (list), tiers_mode (str), transfer_lookup_key (bool), transform_quantity (dict), unit_amount_decimal (str)
    Returns: Price object or error dict
    """
    url = f"{BASE_URL}/prices"
    data = {"currency": currency}
    if product is not None:
        data["product"] = product
    if unit_amount is not None:
        data["unit_amount"] = unit_amount
    for k, v in kwargs.items():
        if v is not None:
            if isinstance(v, dict):
                for subk, subv in v.items():
                    data[f"{k}[{subk}]"] = subv
            elif isinstance(v, list):
                for idx, subv in enumerate(v):
                    data[f"{k}[{idx}]"] = subv
            else:
                data[k] = v
    try:
        resp = requests.post(url, data=data, headers=HEADERS)
        if resp.status_code >= 400:
            return {"error": resp.text}
        return resp.json()
    except Exception as e:
        return {"error": str(e)}

def update_price(price_id: str, **kwargs) -> Dict[str, Any]:
    """
    Update a price by ID.
    Optional: active (bool), metadata (dict), nickname (str), tax_behavior (str), currency_options (dict), lookup_key (str), transfer_lookup_key (bool)
    Returns: Price object or error dict
    """
    url = f"{BASE_URL}/prices/{price_id}"
    data = {}
    for k, v in kwargs.items():
        if v is not None:
            if isinstance(v, dict):
                for subk, subv in v.items():
                    data[f"{k}[{subk}]"] = subv
            elif isinstance(v, list):
                for idx, subv in enumerate(v):
                    data[f"{k}[{idx}]"] = subv
            else:
                data[k] = v
    try:
        resp = requests.post(url, data=data, headers=HEADERS)
        if resp.status_code >= 400:
            return {"error": resp.text}
        return resp.json()
    except Exception as e:
        return {"error": str(e)}

def get_price(price_id: str) -> Dict[str, Any]:
    """
    Retrieve a price by ID.
    Returns: Price object or error dict
    """
    url = f"{BASE_URL}/prices/{price_id}"
    try:
        resp = requests.get(url, headers=HEADERS)
        if resp.status_code >= 400:
            return {"error": resp.text}
        return resp.json()
    except Exception as e:
        return {"error": str(e)}
