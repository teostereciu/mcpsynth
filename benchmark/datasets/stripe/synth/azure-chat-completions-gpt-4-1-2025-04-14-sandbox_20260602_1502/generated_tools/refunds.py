import os
import requests
from typing import Any, Dict

STRIPE_API_KEY = os.environ.get("STRIPE_API_KEY")
BASE_URL = "https://api.stripe.com/v1"

HEADERS = {
    "Authorization": f"Bearer {STRIPE_API_KEY}",
    "Content-Type": "application/x-www-form-urlencoded"
}

def create_refund(amount: int = None, charge: str = None, payment_intent: str = None, metadata: dict = None, reason: str = None, **kwargs) -> Dict[str, Any]:
    """
    Create a refund for a charge or payment intent.
    At least one of charge or payment_intent must be provided.
    Optional: amount (int), metadata (dict), reason (str)
    Returns: Refund object or error dict
    """
    url = f"{BASE_URL}/refunds"
    data = {}
    if amount is not None:
        data["amount"] = amount
    if charge is not None:
        data["charge"] = charge
    if payment_intent is not None:
        data["payment_intent"] = payment_intent
    if metadata is not None:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    if reason is not None:
        data["reason"] = reason
    for k, v in kwargs.items():
        if v is not None:
            data[k] = v
    try:
        resp = requests.post(url, data=data, headers=HEADERS)
        if resp.status_code >= 400:
            return {"error": resp.text}
        return resp.json()
    except Exception as e:
        return {"error": str(e)}

def update_refund(refund_id: str, metadata: dict) -> Dict[str, Any]:
    """
    Update a refund's metadata.
    Returns: Refund object or error dict
    """
    url = f"{BASE_URL}/refunds/{refund_id}"
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

def get_refund(refund_id: str) -> Dict[str, Any]:
    """
    Retrieve a refund by ID.
    Returns: Refund object or error dict
    """
    url = f"{BASE_URL}/refunds/{refund_id}"
    try:
        resp = requests.get(url, headers=HEADERS)
        if resp.status_code >= 400:
            return {"error": resp.text}
        return resp.json()
    except Exception as e:
        return {"error": str(e)}
