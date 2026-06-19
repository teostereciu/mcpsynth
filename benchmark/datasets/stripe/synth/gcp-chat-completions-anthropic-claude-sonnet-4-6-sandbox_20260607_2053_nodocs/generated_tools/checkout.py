"""
Stripe Checkout Sessions tools.
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


def create_checkout_session(
    success_url: str,
    cancel_url: str = None,
    mode: str = "payment",
    line_items: list = None,
    customer: str = None,
    customer_email: str = None,
    currency: str = None,
    payment_method_types: list = None,
    allow_promotion_codes: bool = None,
    billing_address_collection: str = None,
    shipping_address_collection_allowed_countries: list = None,
    client_reference_id: str = None,
    metadata: dict = None,
    subscription_data_trial_period_days: int = None,
    expires_at: int = None,
    ui_mode: str = None,
    return_url: str = None,
) -> dict:
    """
    Create a Checkout Session.
    line_items: list of dicts with keys 'price' and 'quantity'.
    mode: 'payment', 'subscription', or 'setup'.
    """
    data = {"success_url": success_url, "mode": mode}
    if cancel_url:
        data["cancel_url"] = cancel_url
    if line_items:
        for i, item in enumerate(line_items):
            if "price" in item:
                data[f"line_items[{i}][price]"] = item["price"]
            if "quantity" in item:
                data[f"line_items[{i}][quantity]"] = item["quantity"]
            if "price_data" in item:
                pd = item["price_data"]
                if "currency" in pd:
                    data[f"line_items[{i}][price_data][currency]"] = pd["currency"]
                if "unit_amount" in pd:
                    data[f"line_items[{i}][price_data][unit_amount]"] = pd["unit_amount"]
                if "product" in pd:
                    data[f"line_items[{i}][price_data][product]"] = pd["product"]
                if "product_data" in pd:
                    pdd = pd["product_data"]
                    if "name" in pdd:
                        data[f"line_items[{i}][price_data][product_data][name]"] = pdd["name"]
                if "recurring" in pd:
                    rec = pd["recurring"]
                    if "interval" in rec:
                        data[f"line_items[{i}][price_data][recurring][interval]"] = rec["interval"]
    if customer:
        data["customer"] = customer
    if customer_email:
        data["customer_email"] = customer_email
    if currency:
        data["currency"] = currency
    if payment_method_types:
        for i, pm in enumerate(payment_method_types):
            data[f"payment_method_types[{i}]"] = pm
    if allow_promotion_codes is not None:
        data["allow_promotion_codes"] = str(allow_promotion_codes).lower()
    if billing_address_collection:
        data["billing_address_collection"] = billing_address_collection
    if shipping_address_collection_allowed_countries:
        for i, c in enumerate(shipping_address_collection_allowed_countries):
            data[f"shipping_address_collection[allowed_countries][{i}]"] = c
    if client_reference_id:
        data["client_reference_id"] = client_reference_id
    if subscription_data_trial_period_days is not None:
        data["subscription_data[trial_period_days]"] = subscription_data_trial_period_days
    if expires_at is not None:
        data["expires_at"] = expires_at
    if ui_mode:
        data["ui_mode"] = ui_mode
    if return_url:
        data["return_url"] = return_url
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    resp = requests.post(
        f"{BASE_URL}/checkout/sessions", data=data, auth=_auth()
    )
    return _handle(resp)


def get_checkout_session(session_id: str) -> dict:
    """Retrieve a Checkout Session by ID."""
    resp = requests.get(
        f"{BASE_URL}/checkout/sessions/{session_id}", auth=_auth()
    )
    return _handle(resp)


def expire_checkout_session(session_id: str) -> dict:
    """Expire a Checkout Session."""
    resp = requests.post(
        f"{BASE_URL}/checkout/sessions/{session_id}/expire", data={}, auth=_auth()
    )
    return _handle(resp)


def list_checkout_sessions(
    payment_intent: str = None,
    subscription: str = None,
    customer: str = None,
    limit: int = None,
    starting_after: str = None,
    ending_before: str = None,
    status: str = None,
) -> dict:
    """List Checkout Sessions."""
    params = {}
    if payment_intent:
        params["payment_intent"] = payment_intent
    if subscription:
        params["subscription"] = subscription
    if customer:
        params["customer"] = customer
    if limit is not None:
        params["limit"] = limit
    if starting_after:
        params["starting_after"] = starting_after
    if ending_before:
        params["ending_before"] = ending_before
    if status:
        params["status"] = status
    resp = requests.get(
        f"{BASE_URL}/checkout/sessions", params=params, auth=_auth()
    )
    return _handle(resp)


def list_checkout_session_line_items(
    session_id: str, limit: int = None, starting_after: str = None
) -> dict:
    """List line items for a Checkout Session."""
    params = {}
    if limit is not None:
        params["limit"] = limit
    if starting_after:
        params["starting_after"] = starting_after
    resp = requests.get(
        f"{BASE_URL}/checkout/sessions/{session_id}/line_items",
        params=params,
        auth=_auth(),
    )
    return _handle(resp)
