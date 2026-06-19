"""Stripe Webhook Endpoints, Tax Rates, and Shipping Rates tools."""
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


# ── Webhook Endpoints ─────────────────────────────────────────────────────────

def create_webhook_endpoint(
    url: str,
    enabled_events: list,
    description: str = None,
    metadata: dict = None,
):
    """Create a Webhook Endpoint. enabled_events: list of event types or ['*']."""
    data = {"url": url}
    for i, evt in enumerate(enabled_events):
        data[f"enabled_events[{i}]"] = evt
    if description:
        data["description"] = description
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    return _req("POST", "/webhook_endpoints", data=data)


def get_webhook_endpoint(webhook_endpoint_id: str):
    """Retrieve a Webhook Endpoint by ID."""
    return _req("GET", f"/webhook_endpoints/{webhook_endpoint_id}")


def update_webhook_endpoint(
    webhook_endpoint_id: str,
    url: str = None,
    enabled_events: list = None,
    active: bool = None,
    description: str = None,
    metadata: dict = None,
):
    """Update a Webhook Endpoint."""
    data = {}
    if url:
        data["url"] = url
    if enabled_events:
        for i, evt in enumerate(enabled_events):
            data[f"enabled_events[{i}]"] = evt
    if active is not None:
        data["active"] = str(active).lower()
    if description:
        data["description"] = description
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    return _req("POST", f"/webhook_endpoints/{webhook_endpoint_id}", data=data)


def delete_webhook_endpoint(webhook_endpoint_id: str):
    """Delete a Webhook Endpoint."""
    return _req("DELETE", f"/webhook_endpoints/{webhook_endpoint_id}")


def list_webhook_endpoints(limit: int = None, starting_after: str = None):
    """List Webhook Endpoints."""
    params = {}
    if limit is not None:
        params["limit"] = limit
    if starting_after:
        params["starting_after"] = starting_after
    return _req("GET", "/webhook_endpoints", params=params)


# ── Tax Rates ─────────────────────────────────────────────────────────────────

def create_tax_rate(
    display_name: str,
    percentage: float,
    inclusive: bool,
    country: str = None,
    state: str = None,
    description: str = None,
    metadata: dict = None,
):
    """Create a Tax Rate."""
    data = {
        "display_name": display_name,
        "percentage": percentage,
        "inclusive": str(inclusive).lower(),
    }
    if country:
        data["country"] = country
    if state:
        data["state"] = state
    if description:
        data["description"] = description
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    return _req("POST", "/tax_rates", data=data)


def get_tax_rate(tax_rate_id: str):
    """Retrieve a Tax Rate by ID."""
    return _req("GET", f"/tax_rates/{tax_rate_id}")


def update_tax_rate(
    tax_rate_id: str,
    active: bool = None,
    display_name: str = None,
    description: str = None,
    metadata: dict = None,
):
    """Update a Tax Rate."""
    data = {}
    if active is not None:
        data["active"] = str(active).lower()
    if display_name:
        data["display_name"] = display_name
    if description:
        data["description"] = description
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    return _req("POST", f"/tax_rates/{tax_rate_id}", data=data)


def list_tax_rates(active: bool = None, limit: int = None):
    """List Tax Rates."""
    params = {}
    if active is not None:
        params["active"] = str(active).lower()
    if limit is not None:
        params["limit"] = limit
    return _req("GET", "/tax_rates", params=params)


# ── Shipping Rates ────────────────────────────────────────────────────────────

def create_shipping_rate(
    display_name: str,
    fixed_amount: int = None,
    currency: str = None,
    delivery_estimate_min_value: int = None,
    delivery_estimate_min_unit: str = None,
    delivery_estimate_max_value: int = None,
    delivery_estimate_max_unit: str = None,
    metadata: dict = None,
):
    """Create a Shipping Rate."""
    data = {"display_name": display_name, "type": "fixed_amount"}
    if fixed_amount is not None and currency:
        data["fixed_amount[amount]"] = fixed_amount
        data["fixed_amount[currency]"] = currency
    if delivery_estimate_min_value is not None:
        data["delivery_estimate[minimum][value]"] = delivery_estimate_min_value
    if delivery_estimate_min_unit:
        data["delivery_estimate[minimum][unit]"] = delivery_estimate_min_unit
    if delivery_estimate_max_value is not None:
        data["delivery_estimate[maximum][value]"] = delivery_estimate_max_value
    if delivery_estimate_max_unit:
        data["delivery_estimate[maximum][unit]"] = delivery_estimate_max_unit
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    return _req("POST", "/shipping_rates", data=data)


def get_shipping_rate(shipping_rate_id: str):
    """Retrieve a Shipping Rate by ID."""
    return _req("GET", f"/shipping_rates/{shipping_rate_id}")


def list_shipping_rates(active: bool = None, limit: int = None):
    """List Shipping Rates."""
    params = {}
    if active is not None:
        params["active"] = str(active).lower()
    if limit is not None:
        params["limit"] = limit
    return _req("GET", "/shipping_rates", params=params)
