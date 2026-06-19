"""Stripe Checkout Sessions and Payment Links tools."""
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


# ── Checkout Sessions ─────────────────────────────────────────────────────────

def create_checkout_session(
    mode: str,
    success_url: str,
    cancel_url: str = None,
    line_items: list = None,
    customer: str = None,
    customer_email: str = None,
    currency: str = None,
    payment_method_types: list = None,
    allow_promotion_codes: bool = None,
    metadata: dict = None,
):
    """Create a Checkout Session. mode: 'payment', 'subscription', or 'setup'.
    line_items is a list of dicts with 'price' and 'quantity'."""
    data = {"mode": mode, "success_url": success_url}
    if cancel_url:
        data["cancel_url"] = cancel_url
    if line_items:
        for i, item in enumerate(line_items):
            for k, v in item.items():
                data[f"line_items[{i}][{k}]"] = v
    if customer:
        data["customer"] = customer
    if customer_email:
        data["customer_email"] = customer_email
    if currency:
        data["currency"] = currency
    if payment_method_types:
        for i, pmt in enumerate(payment_method_types):
            data[f"payment_method_types[{i}]"] = pmt
    if allow_promotion_codes is not None:
        data["allow_promotion_codes"] = str(allow_promotion_codes).lower()
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    return _req("POST", "/checkout/sessions", data=data)


def get_checkout_session(session_id: str):
    """Retrieve a Checkout Session by ID."""
    return _req("GET", f"/checkout/sessions/{session_id}")


def expire_checkout_session(session_id: str):
    """Expire a Checkout Session."""
    return _req("POST", f"/checkout/sessions/{session_id}/expire")


def list_checkout_sessions(
    customer: str = None,
    payment_intent: str = None,
    subscription: str = None,
    status: str = None,
    limit: int = None,
    starting_after: str = None,
):
    """List Checkout Sessions."""
    params = {}
    if customer:
        params["customer"] = customer
    if payment_intent:
        params["payment_intent"] = payment_intent
    if subscription:
        params["subscription"] = subscription
    if status:
        params["status"] = status
    if limit is not None:
        params["limit"] = limit
    if starting_after:
        params["starting_after"] = starting_after
    return _req("GET", "/checkout/sessions", params=params)


def list_checkout_session_line_items(session_id: str, limit: int = None):
    """List line items for a Checkout Session."""
    params = {}
    if limit is not None:
        params["limit"] = limit
    return _req("GET", f"/checkout/sessions/{session_id}/line_items", params=params)


# ── Payment Links ─────────────────────────────────────────────────────────────

def create_payment_link(
    line_items: list,
    allow_promotion_codes: bool = None,
    after_completion_type: str = None,
    after_completion_redirect_url: str = None,
    metadata: dict = None,
):
    """Create a Payment Link. line_items is a list of dicts with 'price' and 'quantity'."""
    data = {}
    for i, item in enumerate(line_items):
        for k, v in item.items():
            data[f"line_items[{i}][{k}]"] = v
    if allow_promotion_codes is not None:
        data["allow_promotion_codes"] = str(allow_promotion_codes).lower()
    if after_completion_type:
        data["after_completion[type]"] = after_completion_type
    if after_completion_redirect_url:
        data["after_completion[redirect][url]"] = after_completion_redirect_url
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    return _req("POST", "/payment_links", data=data)


def get_payment_link(payment_link_id: str):
    """Retrieve a Payment Link by ID."""
    return _req("GET", f"/payment_links/{payment_link_id}")


def update_payment_link(
    payment_link_id: str,
    active: bool = None,
    allow_promotion_codes: bool = None,
    metadata: dict = None,
):
    """Update a Payment Link."""
    data = {}
    if active is not None:
        data["active"] = str(active).lower()
    if allow_promotion_codes is not None:
        data["allow_promotion_codes"] = str(allow_promotion_codes).lower()
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    return _req("POST", f"/payment_links/{payment_link_id}", data=data)


def list_payment_links(active: bool = None, limit: int = None):
    """List Payment Links."""
    params = {}
    if active is not None:
        params["active"] = str(active).lower()
    if limit is not None:
        params["limit"] = limit
    return _req("GET", "/payment_links", params=params)


def list_payment_link_line_items(payment_link_id: str, limit: int = None):
    """List line items for a Payment Link."""
    params = {}
    if limit is not None:
        params["limit"] = limit
    return _req("GET", f"/payment_links/{payment_link_id}/line_items", params=params)
