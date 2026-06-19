"""
Stripe Refunds tools.
"""
import os
import requests

STRIPE_API_KEY = os.environ.get("STRIPE_API_KEY", "")
BASE_URL = "https://api.stripe.com/v1"


def _auth():
    return (STRIPE_API_KEY, "")


def _handle(resp: requests.Response) -> dict:
    try:
        return resp.json()
    except Exception:
        return {"error": resp.text}


def create_refund(
    charge: str = None,
    payment_intent: str = None,
    amount: int = None,
    reason: str = None,
    metadata: dict = None,
    refund_application_fee: bool = None,
    reverse_transfer: bool = None,
) -> dict:
    """Create a Refund for a Charge or PaymentIntent."""
    data = {}
    if charge:
        data["charge"] = charge
    if payment_intent:
        data["payment_intent"] = payment_intent
    if amount is not None:
        data["amount"] = amount
    if reason:
        data["reason"] = reason
    if refund_application_fee is not None:
        data["refund_application_fee"] = str(refund_application_fee).lower()
    if reverse_transfer is not None:
        data["reverse_transfer"] = str(reverse_transfer).lower()
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    resp = requests.post(f"{BASE_URL}/refunds", data=data, auth=_auth())
    return _handle(resp)


def get_refund(refund_id: str) -> dict:
    """Retrieve a Refund by ID."""
    resp = requests.get(f"{BASE_URL}/refunds/{refund_id}", auth=_auth())
    return _handle(resp)


def update_refund(refund_id: str, metadata: dict = None) -> dict:
    """Update a Refund's metadata."""
    data = {}
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    resp = requests.post(f"{BASE_URL}/refunds/{refund_id}", data=data, auth=_auth())
    return _handle(resp)


def cancel_refund(refund_id: str) -> dict:
    """Cancel a Refund (only possible for refunds in 'requires_action' state)."""
    resp = requests.post(
        f"{BASE_URL}/refunds/{refund_id}/cancel", data={}, auth=_auth()
    )
    return _handle(resp)


def list_refunds(
    charge: str = None,
    payment_intent: str = None,
    limit: int = None,
    starting_after: str = None,
    ending_before: str = None,
) -> dict:
    """List Refunds."""
    params = {}
    if charge:
        params["charge"] = charge
    if payment_intent:
        params["payment_intent"] = payment_intent
    if limit is not None:
        params["limit"] = limit
    if starting_after:
        params["starting_after"] = starting_after
    if ending_before:
        params["ending_before"] = ending_before
    resp = requests.get(f"{BASE_URL}/refunds", params=params, auth=_auth())
    return _handle(resp)
