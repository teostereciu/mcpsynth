import os
import requests
from typing import Any, Dict

STRIPE_API_KEY = os.environ.get("STRIPE_API_KEY")
BASE_URL = "https://api.stripe.com/v1"

HEADERS = {
    "Authorization": f"Bearer {STRIPE_API_KEY}",
    "Content-Type": "application/x-www-form-urlencoded"
}

def create_product(name: str, **kwargs) -> Dict[str, Any]:
    """
    Create a new product.
    Required: name (str)
    Optional: active (bool), description (str), id (str), metadata (dict), tax_code (str), default_price_data (dict), images (list), marketing_features (list), package_dimensions (dict), shippable (bool), statement_descriptor (str), unit_label (str), url (str)
    Returns: Product object or error dict
    """
    url = f"{BASE_URL}/products"
    data = {"name": name}
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

def update_product(product_id: str, **kwargs) -> Dict[str, Any]:
    """
    Update a product by ID.
    Optional: active (bool), default_price (str), description (str), metadata (dict), name (str), tax_code (str), images (list), marketing_features (list), package_dimensions (dict), shippable (bool), statement_descriptor (str), unit_label (str), url (str)
    Returns: Product object or error dict
    """
    url = f"{BASE_URL}/products/{product_id}"
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

def get_product(product_id: str) -> Dict[str, Any]:
    """
    Retrieve a product by ID.
    Returns: Product object or error dict
    """
    url = f"{BASE_URL}/products/{product_id}"
    try:
        resp = requests.get(url, headers=HEADERS)
        if resp.status_code >= 400:
            return {"error": resp.text}
        return resp.json()
    except Exception as e:
        return {"error": str(e)}
