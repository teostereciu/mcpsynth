"""
Stripe Charges tools.
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


def create_charge(
    amount: int,
    currency: str,
    source: str = None,
    customer: str = None,
    description: str = None,
    capture: bool = None,
    metadata: dict = None,
    receipt_email: str = None,
    statement_descriptor: str = None,
) -> dict:
    """Create a Charge directly (legacy). amount in smallest currency unit."""
    data = {"amount": amount, "currency": currency}
    if source:
        data["source"] = source
    if customer:
        data["customer"] = customer
    if description:
        data["description"] = description
    if capture is not None:
        data["capture"] = str(capture).lower()
    if receipt_email:
        data["receipt_email"] = receipt_email
    if statement_descriptor:
        data["statement_descriptor"] = statement_descriptor
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    resp = requests.post(f"{BASE_URL}/charges", data=data, auth=_auth())
    return _handle(resp)


def get_charge(charge_id: str) -> dict:
    """Retrieve a Charge by ID."""
    resp = requests.get(f"{BASE_URL}/charges/{charge_id}", auth=_auth())
    return _handle(resp)


def update_charge(
    charge_id: str,
    description: str = None,
    metadata: dict = None,
    receipt_email: str = None,
    fraud_details_user_report: str = None,
) -> dict:
    """Update a Charge."""
    data = {}
    if description:
        data["description"] = description
    if receipt_email:
        data["receipt_email"] = receipt_email
    if fraud_details_user_report:
        data["fraud_details[user_report]"] = fraud_details_user_report
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    resp = requests.post(f"{BASE_URL}/charges/{charge_id}", data=data, auth=_auth())
    return _handle(resp)


def capture_charge(
    charge_id: str,
    amount: int = None,
    receipt_email: str = None,
    statement_descriptor: str = None,
) -> dict:
    """Capture an uncaptured Charge."""
    data = {}
    if amount is not None:
        data["amount"] = amount
    if receipt_email:
        data["receipt_email"] = receipt_email
    if statement_descriptor:
        data["statement_descriptor"] = statement_descriptor
    resp = requests.post(
        f"{BASE_URL}/charges/{charge_id}/capture", data=data, auth=_auth()
    )
    return _handle(resp)


def list_charges(
    customer: str = None,
    payment_intent: str = None,
    limit: int = None,
    starting_after: str = None,
    ending_before: str = None,
    created_gte: int = None,
    created_lte: int = None,
) -> dict:
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
    if created_gte is not None:
        params["created[gte]"] = created_gte
    if created_lte is not None:
        params["created[lte]"] = created_lte
    resp = requests.get(f"{BASE_URL}/charges", params=params, auth=_auth())
    return _handle(resp)


def search_charges(query: str, limit: int = None, page: str = None) -> dict:
    """Search Charges using Stripe query syntax."""
    params = {"query": query}
    if limit is not None:
        params["limit"] = limit
    if page:
        params["page"] = page
    resp = requests.get(f"{BASE_URL}/charges/search", params=params, auth=_auth())
    return _handle(resp)
