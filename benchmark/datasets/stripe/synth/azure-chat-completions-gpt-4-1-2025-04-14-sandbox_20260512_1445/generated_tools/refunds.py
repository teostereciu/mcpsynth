import os
import requests
from fastmcp import tool

STRIPE_API_KEY = os.environ.get("STRIPE_API_KEY")
BASE_URL = "https://api.stripe.com/v1"
HEADERS = {
    "Authorization": f"Bearer {STRIPE_API_KEY}",
    "Content-Type": "application/x-www-form-urlencoded"
}

@tool("create_refund")
def create_refund(charge: str = None, payment_intent: str = None, amount: int = None, metadata: dict = None, reason: str = None):
    """
    Create a Refund object for a charge or payment intent.
    """
    data = {}
    if charge:
        data["charge"] = charge
    if payment_intent:
        data["payment_intent"] = payment_intent
    if amount:
        data["amount"] = amount
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    if reason:
        data["reason"] = reason
    try:
        resp = requests.post(f"{BASE_URL}/refunds", data=data, headers=HEADERS)
        resp.raise_for_status()
        return resp.json()
    except requests.HTTPError as e:
        return {"error": str(e), "details": resp.text}

@tool("retrieve_refund")
def retrieve_refund(refund_id: str):
    """
    Retrieve a Refund object.
    """
    try:
        resp = requests.get(f"{BASE_URL}/refunds/{refund_id}", headers=HEADERS)
        resp.raise_for_status()
        return resp.json()
    except requests.HTTPError as e:
        return {"error": str(e), "details": resp.text}

@tool("update_refund")
def update_refund(refund_id: str, metadata: dict = None):
    """
    Update a Refund object (only metadata).
    """
    data = {}
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    try:
        resp = requests.post(f"{BASE_URL}/refunds/{refund_id}", data=data, headers=HEADERS)
        resp.raise_for_status()
        return resp.json()
    except requests.HTTPError as e:
        return {"error": str(e), "details": resp.text}
