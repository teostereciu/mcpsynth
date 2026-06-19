"""Stripe Payment Intents tools."""
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


# ── Payment Intents ──────────────────────────────────────────────────────────

def create_payment_intent(
    amount: int,
    currency: str,
    customer: str = None,
    description: str = None,
    payment_method: str = None,
    confirm: bool = None,
    return_url: str = None,
    automatic_payment_methods: bool = None,
    metadata: dict = None,
):
    """Create a PaymentIntent."""
    data = {"amount": amount, "currency": currency}
    if customer:
        data["customer"] = customer
    if description:
        data["description"] = description
    if payment_method:
        data["payment_method"] = payment_method
    if confirm is not None:
        data["confirm"] = str(confirm).lower()
    if return_url:
        data["return_url"] = return_url
    if automatic_payment_methods is not None:
        data["automatic_payment_methods[enabled]"] = str(automatic_payment_methods).lower()
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    return _req("POST", "/payment_intents", data=data)


def get_payment_intent(payment_intent_id: str):
    """Retrieve a PaymentIntent by ID."""
    return _req("GET", f"/payment_intents/{payment_intent_id}")


def update_payment_intent(
    payment_intent_id: str,
    amount: int = None,
    currency: str = None,
    customer: str = None,
    description: str = None,
    payment_method: str = None,
    metadata: dict = None,
):
    """Update a PaymentIntent."""
    data = {}
    if amount is not None:
        data["amount"] = amount
    if currency:
        data["currency"] = currency
    if customer:
        data["customer"] = customer
    if description:
        data["description"] = description
    if payment_method:
        data["payment_method"] = payment_method
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    return _req("POST", f"/payment_intents/{payment_intent_id}", data=data)


def confirm_payment_intent(
    payment_intent_id: str,
    payment_method: str = None,
    return_url: str = None,
):
    """Confirm a PaymentIntent."""
    data = {}
    if payment_method:
        data["payment_method"] = payment_method
    if return_url:
        data["return_url"] = return_url
    return _req("POST", f"/payment_intents/{payment_intent_id}/confirm", data=data)


def cancel_payment_intent(payment_intent_id: str, cancellation_reason: str = None):
    """Cancel a PaymentIntent."""
    data = {}
    if cancellation_reason:
        data["cancellation_reason"] = cancellation_reason
    return _req("POST", f"/payment_intents/{payment_intent_id}/cancel", data=data)


def capture_payment_intent(payment_intent_id: str, amount_to_capture: int = None):
    """Capture a PaymentIntent."""
    data = {}
    if amount_to_capture is not None:
        data["amount_to_capture"] = amount_to_capture
    return _req("POST", f"/payment_intents/{payment_intent_id}/capture", data=data)


def list_payment_intents(
    customer: str = None,
    limit: int = None,
    starting_after: str = None,
    ending_before: str = None,
):
    """List PaymentIntents."""
    params = {}
    if customer:
        params["customer"] = customer
    if limit is not None:
        params["limit"] = limit
    if starting_after:
        params["starting_after"] = starting_after
    if ending_before:
        params["ending_before"] = ending_before
    return _req("GET", "/payment_intents", params=params)
