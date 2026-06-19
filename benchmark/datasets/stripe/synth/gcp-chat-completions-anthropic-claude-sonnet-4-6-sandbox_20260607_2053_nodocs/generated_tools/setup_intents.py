"""
Stripe Setup Intents tools.
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


def create_setup_intent(
    customer: str = None,
    payment_method: str = None,
    payment_method_types: list = None,
    usage: str = None,
    description: str = None,
    metadata: dict = None,
    confirm: bool = None,
    return_url: str = None,
) -> dict:
    """Create a SetupIntent for saving a payment method."""
    data = {}
    if customer:
        data["customer"] = customer
    if payment_method:
        data["payment_method"] = payment_method
    if payment_method_types:
        for i, pm in enumerate(payment_method_types):
            data[f"payment_method_types[{i}]"] = pm
    if usage:
        data["usage"] = usage
    if description:
        data["description"] = description
    if confirm is not None:
        data["confirm"] = str(confirm).lower()
    if return_url:
        data["return_url"] = return_url
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    resp = requests.post(f"{BASE_URL}/setup_intents", data=data, auth=_auth())
    return _handle(resp)


def get_setup_intent(setup_intent_id: str) -> dict:
    """Retrieve a SetupIntent by ID."""
    resp = requests.get(f"{BASE_URL}/setup_intents/{setup_intent_id}", auth=_auth())
    return _handle(resp)


def update_setup_intent(
    setup_intent_id: str,
    customer: str = None,
    payment_method: str = None,
    description: str = None,
    metadata: dict = None,
) -> dict:
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
    resp = requests.post(
        f"{BASE_URL}/setup_intents/{setup_intent_id}", data=data, auth=_auth()
    )
    return _handle(resp)


def confirm_setup_intent(
    setup_intent_id: str,
    payment_method: str = None,
    return_url: str = None,
) -> dict:
    """Confirm a SetupIntent."""
    data = {}
    if payment_method:
        data["payment_method"] = payment_method
    if return_url:
        data["return_url"] = return_url
    resp = requests.post(
        f"{BASE_URL}/setup_intents/{setup_intent_id}/confirm",
        data=data,
        auth=_auth(),
    )
    return _handle(resp)


def cancel_setup_intent(
    setup_intent_id: str, cancellation_reason: str = None
) -> dict:
    """Cancel a SetupIntent."""
    data = {}
    if cancellation_reason:
        data["cancellation_reason"] = cancellation_reason
    resp = requests.post(
        f"{BASE_URL}/setup_intents/{setup_intent_id}/cancel",
        data=data,
        auth=_auth(),
    )
    return _handle(resp)


def list_setup_intents(
    customer: str = None,
    payment_method: str = None,
    limit: int = None,
    starting_after: str = None,
    ending_before: str = None,
) -> dict:
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
    if ending_before:
        params["ending_before"] = ending_before
    resp = requests.get(f"{BASE_URL}/setup_intents", params=params, auth=_auth())
    return _handle(resp)
