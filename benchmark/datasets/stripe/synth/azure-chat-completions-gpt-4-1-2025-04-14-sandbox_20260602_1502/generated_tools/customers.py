import os
import requests
from typing import Any, Dict

STRIPE_API_KEY = os.environ.get("STRIPE_API_KEY")
BASE_URL = "https://api.stripe.com/v1"

HEADERS = {
    "Authorization": f"Bearer {STRIPE_API_KEY}",
    "Content-Type": "application/x-www-form-urlencoded"
}

def create_customer(**kwargs) -> Dict[str, Any]:
    """
    Create a new customer.
    Optional: address (dict), description (str), email (str), metadata (dict), name (str), payment_method (str), phone (str), shipping (dict), tax (dict), etc.
    Returns: Customer object or error dict
    """
    url = f"{BASE_URL}/customers"
    data = {}
    for k, v in kwargs.items():
        if v is not None:
            if isinstance(v, dict):
                for subk, subv in v.items():
                    data[f"{k}[{subk}]"] = subv
            else:
                data[k] = v
    try:
        resp = requests.post(url, data=data, headers=HEADERS)
        if resp.status_code >= 400:
            return {"error": resp.text}
        return resp.json()
    except Exception as e:
        return {"error": str(e)}

def update_customer(customer_id: str, **kwargs) -> Dict[str, Any]:
    """
    Update a customer by ID.
    Optional: address (dict), description (str), email (str), metadata (dict), name (str), phone (str), shipping (dict), tax (dict), etc.
    Returns: Customer object or error dict
    """
    url = f"{BASE_URL}/customers/{customer_id}"
    data = {}
    for k, v in kwargs.items():
        if v is not None:
            if isinstance(v, dict):
                for subk, subv in v.items():
                    data[f"{k}[{subk}]"] = subv
            else:
                data[k] = v
    try:
        resp = requests.post(url, data=data, headers=HEADERS)
        if resp.status_code >= 400:
            return {"error": resp.text}
        return resp.json()
    except Exception as e:
        return {"error": str(e)}

def get_customer(customer_id: str) -> Dict[str, Any]:
    """
    Retrieve a customer by ID.
    Returns: Customer object or error dict
    """
    url = f"{BASE_URL}/customers/{customer_id}"
    try:
        resp = requests.get(url, headers=HEADERS)
        if resp.status_code >= 400:
            return {"error": resp.text}
        return resp.json()
    except Exception as e:
        return {"error": str(e)}
