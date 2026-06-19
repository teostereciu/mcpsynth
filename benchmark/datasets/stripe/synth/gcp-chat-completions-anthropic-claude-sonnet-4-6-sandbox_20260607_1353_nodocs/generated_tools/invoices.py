"""Stripe Invoices tools."""
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


# ── Invoices ──────────────────────────────────────────────────────────────────

def create_invoice(
    customer: str,
    auto_advance: bool = None,
    collection_method: str = None,
    description: str = None,
    days_until_due: int = None,
    default_payment_method: str = None,
    metadata: dict = None,
):
    """Create an Invoice for a Customer."""
    data = {"customer": customer}
    if auto_advance is not None:
        data["auto_advance"] = str(auto_advance).lower()
    if collection_method:
        data["collection_method"] = collection_method
    if description:
        data["description"] = description
    if days_until_due is not None:
        data["days_until_due"] = days_until_due
    if default_payment_method:
        data["default_payment_method"] = default_payment_method
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    return _req("POST", "/invoices", data=data)


def get_invoice(invoice_id: str):
    """Retrieve an Invoice by ID."""
    return _req("GET", f"/invoices/{invoice_id}")


def update_invoice(
    invoice_id: str,
    auto_advance: bool = None,
    description: str = None,
    days_until_due: int = None,
    default_payment_method: str = None,
    metadata: dict = None,
):
    """Update an Invoice."""
    data = {}
    if auto_advance is not None:
        data["auto_advance"] = str(auto_advance).lower()
    if description:
        data["description"] = description
    if days_until_due is not None:
        data["days_until_due"] = days_until_due
    if default_payment_method:
        data["default_payment_method"] = default_payment_method
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    return _req("POST", f"/invoices/{invoice_id}", data=data)


def delete_invoice(invoice_id: str):
    """Delete a draft Invoice."""
    return _req("DELETE", f"/invoices/{invoice_id}")


def finalize_invoice(invoice_id: str, auto_advance: bool = None):
    """Finalize a draft Invoice."""
    data = {}
    if auto_advance is not None:
        data["auto_advance"] = str(auto_advance).lower()
    return _req("POST", f"/invoices/{invoice_id}/finalize", data=data)


def pay_invoice(invoice_id: str, payment_method: str = None):
    """Pay an Invoice."""
    data = {}
    if payment_method:
        data["payment_method"] = payment_method
    return _req("POST", f"/invoices/{invoice_id}/pay", data=data)


def void_invoice(invoice_id: str):
    """Void a finalized Invoice."""
    return _req("POST", f"/invoices/{invoice_id}/void")


def send_invoice(invoice_id: str):
    """Send an Invoice to the customer."""
    return _req("POST", f"/invoices/{invoice_id}/send")


def list_invoices(
    customer: str = None,
    subscription: str = None,
    status: str = None,
    limit: int = None,
    starting_after: str = None,
    ending_before: str = None,
):
    """List Invoices. status can be 'draft','open','paid','void','uncollectible'."""
    params = {}
    if customer:
        params["customer"] = customer
    if subscription:
        params["subscription"] = subscription
    if status:
        params["status"] = status
    if limit is not None:
        params["limit"] = limit
    if starting_after:
        params["starting_after"] = starting_after
    if ending_before:
        params["ending_before"] = ending_before
    return _req("GET", "/invoices", params=params)


def search_invoices(query: str, limit: int = None):
    """Search Invoices using Stripe query syntax."""
    params = {"query": query}
    if limit is not None:
        params["limit"] = limit
    return _req("GET", "/invoices/search", params=params)


def retrieve_upcoming_invoice(
    customer: str,
    subscription: str = None,
    subscription_items: list = None,
):
    """Retrieve the upcoming Invoice for a Customer."""
    params = {"customer": customer}
    if subscription:
        params["subscription"] = subscription
    if subscription_items:
        for i, item in enumerate(subscription_items):
            for k, v in item.items():
                params[f"subscription_items[{i}][{k}]"] = v
    return _req("GET", "/invoices/upcoming", params=params)


# ── Invoice Items ─────────────────────────────────────────────────────────────

def create_invoice_item(
    customer: str,
    amount: int,
    currency: str,
    description: str = None,
    invoice: str = None,
    metadata: dict = None,
):
    """Create an Invoice Item."""
    data = {"customer": customer, "amount": amount, "currency": currency}
    if description:
        data["description"] = description
    if invoice:
        data["invoice"] = invoice
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    return _req("POST", "/invoiceitems", data=data)


def delete_invoice_item(invoice_item_id: str):
    """Delete an Invoice Item."""
    return _req("DELETE", f"/invoiceitems/{invoice_item_id}")


def list_invoice_items(
    customer: str = None,
    invoice: str = None,
    limit: int = None,
):
    """List Invoice Items."""
    params = {}
    if customer:
        params["customer"] = customer
    if invoice:
        params["invoice"] = invoice
    if limit is not None:
        params["limit"] = limit
    return _req("GET", "/invoiceitems", params=params)
