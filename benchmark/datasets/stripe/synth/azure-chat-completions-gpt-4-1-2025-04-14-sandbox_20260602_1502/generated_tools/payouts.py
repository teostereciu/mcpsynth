import os
import requests
from typing import Any, Dict

STRIPE_API_KEY = os.environ.get("STRIPE_API_KEY")
BASE_URL = "https://api.stripe.com/v1"

HEADERS = {
    "Authorization": f"Bearer {STRIPE_API_KEY}",
    "Content-Type": "application/x-www-form-urlencoded"
}

def create_payout(amount: int, currency: str, **kwargs) -> Dict[str, Any]:
    """
    Create a payout to your own bank account.
    Required: amount (int), currency (str)
    Optional: description (str), metadata (dict), statement_descriptor (str), destination (str), method (str), payout_method (str), source_type (str)
    Returns: Payout object or error dict
    """
    url = f"{BASE_URL}/payouts"
    data = {
        "amount": amount,
        "currency": currency
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

def update_payout(payout_id: str, metadata: dict = None) -> Dict[str, Any]:
    """
    Update a payout's metadata.
    Returns: Payout object or error dict
    """
    url = f"{BASE_URL}/payouts/{payout_id}"
    data = {}
    if metadata is not None:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    try:
        resp = requests.post(url, data=data, headers=HEADERS)
        if resp.status_code >= 400:
            return {"error": resp.text}
        return resp.json()
    except Exception as e:
        return {"error": str(e)}

def get_payout(payout_id: str) -> Dict[str, Any]:
    """
    Retrieve a payout by ID.
    Returns: Payout object or error dict
    """
    url = f"{BASE_URL}/payouts/{payout_id}"
    try:
        resp = requests.get(url, headers=HEADERS)
        if resp.status_code >= 400:
            return {"error": resp.text}
        return resp.json()
    except Exception as e:
        return {"error": str(e)}
