"""
Stripe Payment Intents tools.
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


def create_payment_intent(
    amount: int,
    currency: str,
    customer: str = None,
    description: str = None,
    payment_method: str = None,
    payment_method_types: list = None,
    confirm: bool = None,
    return_url: str = None,
    capture_method: str = None,
    setup_future_usage: str = None,
    metadata: dict = None,
) -> dict:
    """Create a PaymentIntent. amount is in smallest currency unit (e.g. cents)."""
    data = {"amount": amount, "currency": currency}
    if customer:
        data["customer"] = customer
    if description:
        data["description"] = description
    if payment_method:
        data["payment_method"] = payment_method
    if payment_method_types:
        for i, pm in enumerate(payment_method_types):
            data[f"payment_method_types[{i}]"] = pm
    if confirm is not None:
        data["confirm"] = str(confirm).lower()
    if return_url:
        data["return_url"] = return_url
    if capture_method:
        data["capture_method"] = capture_method
    if setup_future_usage:
        data["setup_future_usage"] = setup_future_usage
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    resp = requests.post(f"{BASE_URL}/payment_intents", data=data, auth=_auth())
    return _handle(resp)


def get_payment_intent(payment_intent_id: str) -> dict:
    """Retrieve a PaymentIntent by ID."""
    resp = requests.get(f"{BASE_URL}/payment_intents/{payment_intent_id}", auth=_auth())
    return _handle(resp)


def update_payment_intent(
    payment_intent_id: str,
    amount: int = None,
    currency: str = None,
    customer: str = None,
    description: str = None,
    payment_method: str = None,
    metadata: dict = None,
) -> dict:
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
    resp = requests.post(
        f"{BASE_URL}/payment_intents/{payment_intent_id}", data=data, auth=_auth()
    )
    return _handle(resp)


def confirm_payment_intent(
    payment_intent_id: str,
    payment_method: str = None,
    return_url: str = None,
) -> dict:
    """Confirm a PaymentIntent."""
    data = {}
    if payment_method:
        data["payment_method"] = payment_method
    if return_url:
        data["return_url"] = return_url
    resp = requests.post(
        f"{BASE_URL}/payment_intents/{payment_intent_id}/confirm",
        data=data,
        auth=_auth(),
    )
    return _handle(resp)


def capture_payment_intent(
    payment_intent_id: str,
    amount_to_capture: int = None,
) -> dict:
    """Capture a PaymentIntent that requires manual capture."""
    data = {}
    if amount_to_capture is not None:
        data["amount_to_capture"] = amount_to_capture
    resp = requests.post(
        f"{BASE_URL}/payment_intents/{payment_intent_id}/capture",
        data=data,
        auth=_auth(),
    )
    return _handle(resp)


def cancel_payment_intent(
    payment_intent_id: str,
    cancellation_reason: str = None,
) -> dict:
    """Cancel a PaymentIntent."""
    data = {}
    if cancellation_reason:
        data["cancellation_reason"] = cancellation_reason
    resp = requests.post(
        f"{BASE_URL}/payment_intents/{payment_intent_id}/cancel",
        data=data,
        auth=_auth(),
    )
    return _handle(resp)


def list_payment_intents(
    customer: str = None,
    limit: int = None,
    starting_after: str = None,
    ending_before: str = None,
    created_gte: int = None,
    created_lte: int = None,
) -> dict:
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
    if created_gte is not None:
        params["created[gte]"] = created_gte
    if created_lte is not None:
        params["created[lte]"] = created_lte
    resp = requests.get(f"{BASE_URL}/payment_intents", params=params, auth=_auth())
    return _handle(resp)
