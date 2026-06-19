import os
import requests
from typing import Any, Dict

STRIPE_API_KEY = os.environ.get("STRIPE_API_KEY")
BASE_URL = "https://api.stripe.com/v1"

HEADERS = {
    "Authorization": f"Bearer {STRIPE_API_KEY}",
    "Content-Type": "application/x-www-form-urlencoded"
}

def create_transfer(currency: str, destination: str, amount: int, **kwargs) -> Dict[str, Any]:
    """
    Create a transfer to a connected Stripe account.
    Required: currency (str), destination (str), amount (int)
    Optional: description (str), metadata (dict), source_transaction (str), source_type (str), transfer_group (str)
    Returns: Transfer object or error dict
    """
    url = f"{BASE_URL}/transfers"
    data = {
        "currency": currency,
        "destination": destination,
        "amount": amount
    }
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

def update_transfer(transfer_id: str, metadata: dict = None, description: str = None) -> Dict[str, Any]:
    """
    Update a transfer's metadata or description.
    Returns: Transfer object or error dict
    """
    url = f"{BASE_URL}/transfers/{transfer_id}"
    data = {}
    if metadata is not None:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    if description is not None:
        data["description"] = description
    try:
        resp = requests.post(url, data=data, headers=HEADERS)
        if resp.status_code >= 400:
            return {"error": resp.text}
        return resp.json()
    except Exception as e:
        return {"error": str(e)}

def get_transfer(transfer_id: str) -> Dict[str, Any]:
    """
    Retrieve a transfer by ID.
    Returns: Transfer object or error dict
    """
    url = f"{BASE_URL}/transfers/{transfer_id}"
    try:
        resp = requests.get(url, headers=HEADERS)
        if resp.status_code >= 400:
            return {"error": resp.text}
        return resp.json()
    except Exception as e:
        return {"error": str(e)}
