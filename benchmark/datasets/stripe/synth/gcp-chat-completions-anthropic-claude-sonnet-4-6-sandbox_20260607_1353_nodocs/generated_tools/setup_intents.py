"""Stripe Setup Intents tools."""
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


# ── Setup Intents ─────────────────────────────────────────────────────────────

def create_setup_intent(
    customer: str = None,
    payment_method: str = None,
    payment_method_types: list = None,
    usage: str = None,
    description: str = None,
    metadata: dict = None,
):
    """Create a SetupIntent to save a payment method for future use."""
    data = {}
    if customer:
        data["customer"] = customer
    if payment_method:
        data["payment_method"] = payment_method
    if payment_method_types:
        for i, pmt in enumerate(payment_method_types):
            data[f"payment_method_types[{i}]"] = pmt
    if usage:
        data["usage"] = usage
    if description:
        data["description"] = description
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    return _req("POST", "/setup_intents", data=data)


def get_setup_intent(setup_intent_id: str):
    """Retrieve a SetupIntent by ID."""
    return _req("GET", f"/setup_intents/{setup_intent_id}")


def update_setup_intent(
    setup_intent_id: str,
    customer: str = None,
    payment_method: str = None,
    description: str = None,
    metadata: dict = None,
):
    """Update a SetupIntent."""
    data = {}
    if customer:
        data["customer"] = customer
    if payment_method:
        data["payment_method"] = payment_method
    if description:
        data["description"] = description
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    return _req("POST", f"/setup_intents/{setup_intent_id}", data=data)


def confirm_setup_intent(setup_intent_id: str, payment_method: str = None, return_url: str = None):
    """Confirm a SetupIntent."""
    data = {}
    if payment_method:
        data["payment_method"] = payment_method
    if return_url:
        data["return_url"] = return_url
    return _req("POST", f"/setup_intents/{setup_intent_id}/confirm", data=data)


def cancel_setup_intent(setup_intent_id: str, cancellation_reason: str = None):
    """Cancel a SetupIntent."""
    data = {}
    if cancellation_reason:
        data["cancellation_reason"] = cancellation_reason
    return _req("POST", f"/setup_intents/{setup_intent_id}/cancel", data=data)


def list_setup_intents(
    customer: str = None,
    payment_method: str = None,
    limit: int = None,
    starting_after: str = None,
):
    """List SetupIntents."""
    params = {}
    if customer:
        params["customer"] = customer
    if payment_method:
        params["payment_method"] = payment_method
    if limit is not None:
        params["limit"] = limit
    if starting_after:
        params["starting_after"] = starting_after
    return _req("GET", "/setup_intents", params=params)
