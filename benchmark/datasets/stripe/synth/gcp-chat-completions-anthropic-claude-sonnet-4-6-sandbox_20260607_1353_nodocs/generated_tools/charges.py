"""Stripe Charges tools."""
import os
import requests

STRIPE_API_KEY = os.environ.get("STRIPE_API_KEY", "")
BASE_URL = "https://api.stripe.com/v1"


def _headers():
    return {"Authorization": f"Bearer {STRIPE_API_KEY}"}


def _req(method: str, path: str, params: dict = None, data: dict = None):
    url = f"{BASE_URL}{path}"
    try:
        resp = requests.request(
            method,
            url,
            headers=_headers(),
            params=params if method == "GET" else None,
            data=data if method != "GET" else None,
            timeout=30,
        )
        return resp.json()
    except Exception as e:
        return {"error": str(e)}


# ── Charges ──────────────────────────────────────────────────────────────────

def create_charge(
    amount: int,
    currency: str,
    source: str = None,
    customer: str = None,
    description: str = None,
    capture: bool = None,
    metadata: dict = None,
):
    """Create a Charge."""
    data = {"amount": amount, "currency": currency}
    if source:
        data["source"] = source
    if customer:
        data["customer"] = customer
    if description:
        data["description"] = description
    if capture is not None:
        data["capture"] = str(capture).lower()
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    return _req("POST", "/charges", data=data)


def get_charge(charge_id: str):
    """Retrieve a Charge by ID."""
    return _req("GET", f"/charges/{charge_id}")


def update_charge(
    charge_id: str,
    description: str = None,
    metadata: dict = None,
    receipt_email: str = None,
):
    """Update a Charge."""
    data = {}
    if description:
        data["description"] = description
    if receipt_email:
        data["receipt_email"] = receipt_email
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    return _req("POST", f"/charges/{charge_id}", data=data)


def capture_charge(charge_id: str, amount: int = None):
    """Capture an uncaptured Charge."""
    data = {}
    if amount is not None:
        data["amount"] = amount
    return _req("POST", f"/charges/{charge_id}/capture", data=data)


def list_charges(
    customer: str = None,
    payment_intent: str = None,
    limit: int = None,
    starting_after: str = None,
    ending_before: str = None,
):
    """List Charges."""
    params = {}
    if customer:
        params["customer"] = customer
    if payment_intent:
        params["payment_intent"] = payment_intent
    if limit is not None:
        params["limit"] = limit
    if starting_after:
        params["starting_after"] = starting_after
    if ending_before:
        params["ending_before"] = ending_before
    return _req("GET", "/charges", params=params)


# ── Refunds ───────────────────────────────────────────────────────────────────

def create_refund(
    charge: str = None,
    payment_intent: str = None,
    amount: int = None,
    reason: str = None,
    metadata: dict = None,
):
    """Create a Refund."""
    data = {}
    if charge:
        data["charge"] = charge
    if payment_intent:
        data["payment_intent"] = payment_intent
    if amount is not None:
        data["amount"] = amount
    if reason:
        data["reason"] = reason
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    return _req("POST", "/refunds", data=data)


def get_refund(refund_id: str):
    """Retrieve a Refund by ID."""
    return _req("GET", f"/refunds/{refund_id}")


def update_refund(refund_id: str, metadata: dict = None):
    """Update a Refund's metadata."""
    data = {}
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    return _req("POST", f"/refunds/{refund_id}", data=data)


def list_refunds(
    charge: str = None,
    payment_intent: str = None,
    limit: int = None,
    starting_after: str = None,
):
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
    return _req("GET", "/refunds", params=params)
