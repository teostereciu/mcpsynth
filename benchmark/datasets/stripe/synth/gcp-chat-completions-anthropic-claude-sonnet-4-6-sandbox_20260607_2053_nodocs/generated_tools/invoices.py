"""
Stripe Invoices tools.
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


def create_invoice(
    customer: str,
    subscription: str = None,
    auto_advance: bool = None,
    collection_method: str = None,
    days_until_due: int = None,
    description: str = None,
    footer: str = None,
    metadata: dict = None,
    default_payment_method: str = None,
    pending_invoice_items_behavior: str = None,
) -> dict:
    """Create an Invoice for a Customer."""
    data = {"customer": customer}
    if subscription:
        data["subscription"] = subscription
    if auto_advance is not None:
        data["auto_advance"] = str(auto_advance).lower()
    if collection_method:
        data["collection_method"] = collection_method
    if days_until_due is not None:
        data["days_until_due"] = days_until_due
    if description:
        data["description"] = description
    if footer:
        data["footer"] = footer
    if default_payment_method:
        data["default_payment_method"] = default_payment_method
    if pending_invoice_items_behavior:
        data["pending_invoice_items_behavior"] = pending_invoice_items_behavior
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    resp = requests.post(f"{BASE_URL}/invoices", data=data, auth=_auth())
    return _handle(resp)


def get_invoice(invoice_id: str) -> dict:
    """Retrieve an Invoice by ID."""
    resp = requests.get(f"{BASE_URL}/invoices/{invoice_id}", auth=_auth())
    return _handle(resp)


def update_invoice(
    invoice_id: str,
    auto_advance: bool = None,
    collection_method: str = None,
    days_until_due: int = None,
    description: str = None,
    footer: str = None,
    metadata: dict = None,
    default_payment_method: str = None,
) -> dict:
    """Update an Invoice."""
    data = {}
    if auto_advance is not None:
        data["auto_advance"] = str(auto_advance).lower()
    if collection_method:
        data["collection_method"] = collection_method
    if days_until_due is not None:
        data["days_until_due"] = days_until_due
    if description:
        data["description"] = description
    if footer:
        data["footer"] = footer
    if default_payment_method:
        data["default_payment_method"] = default_payment_method
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    resp = requests.post(
        f"{BASE_URL}/invoices/{invoice_id}", data=data, auth=_auth()
    )
    return _handle(resp)


def delete_invoice(invoice_id: str) -> dict:
    """Delete a draft Invoice."""
    resp = requests.delete(f"{BASE_URL}/invoices/{invoice_id}", auth=_auth())
    return _handle(resp)


def finalize_invoice(invoice_id: str, auto_advance: bool = None) -> dict:
    """Finalize a draft Invoice."""
    data = {}
    if auto_advance is not None:
        data["auto_advance"] = str(auto_advance).lower()
    resp = requests.post(
        f"{BASE_URL}/invoices/{invoice_id}/finalize", data=data, auth=_auth()
    )
    return _handle(resp)


def pay_invoice(
    invoice_id: str,
    payment_method: str = None,
    source: str = None,
    paid_out_of_band: bool = None,
) -> dict:
    """Pay an Invoice."""
    data = {}
    if payment_method:
        data["payment_method"] = payment_method
    if source:
        data["source"] = source
    if paid_out_of_band is not None:
        data["paid_out_of_band"] = str(paid_out_of_band).lower()
    resp = requests.post(
        f"{BASE_URL}/invoices/{invoice_id}/pay", data=data, auth=_auth()
    )
    return _handle(resp)


def void_invoice(invoice_id: str) -> dict:
    """Void a finalized Invoice."""
    resp = requests.post(
        f"{BASE_URL}/invoices/{invoice_id}/void", data={}, auth=_auth()
    )
    return _handle(resp)


def mark_invoice_uncollectible(invoice_id: str) -> dict:
    """Mark an Invoice as uncollectible."""
    resp = requests.post(
        f"{BASE_URL}/invoices/{invoice_id}/mark_uncollectible", data={}, auth=_auth()
    )
    return _handle(resp)


def send_invoice(invoice_id: str) -> dict:
    """Send an Invoice to the customer."""
    resp = requests.post(
        f"{BASE_URL}/invoices/{invoice_id}/send", data={}, auth=_auth()
    )
    return _handle(resp)


def list_invoices(
    customer: str = None,
    subscription: str = None,
    status: str = None,
    limit: int = None,
    starting_after: str = None,
    ending_before: str = None,
    created_gte: int = None,
    created_lte: int = None,
) -> dict:
    """List Invoices."""
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
    if created_gte is not None:
        params["created[gte]"] = created_gte
    if created_lte is not None:
        params["created[lte]"] = created_lte
    resp = requests.get(f"{BASE_URL}/invoices", params=params, auth=_auth())
    return _handle(resp)


def search_invoices(query: str, limit: int = None, page: str = None) -> dict:
    """Search Invoices using Stripe query syntax."""
    params = {"query": query}
    if limit is not None:
        params["limit"] = limit
    if page:
        params["page"] = page
    resp = requests.get(f"{BASE_URL}/invoices/search", params=params, auth=_auth())
    return _handle(resp)


def retrieve_upcoming_invoice(
    customer: str,
    subscription: str = None,
    subscription_items: list = None,
    coupon: str = None,
) -> dict:
    """Retrieve the upcoming Invoice for a Customer."""
    params = {"customer": customer}
    if subscription:
        params["subscription"] = subscription
    if coupon:
        params["coupon"] = coupon
    if subscription_items:
        for i, item in enumerate(subscription_items):
            if "price" in item:
                params[f"subscription_items[{i}][price]"] = item["price"]
            if "quantity" in item:
                params[f"subscription_items[{i}][quantity]"] = item["quantity"]
    resp = requests.get(
        f"{BASE_URL}/invoices/upcoming", params=params, auth=_auth()
    )
    return _handle(resp)


# ── Invoice Items ────────────────────────────────────────────────────────────

def create_invoice_item(
    customer: str,
    amount: int = None,
    currency: str = None,
    price: str = None,
    quantity: int = None,
    invoice: str = None,
    description: str = None,
    metadata: dict = None,
) -> dict:
    """Create an Invoice Item."""
    data = {"customer": customer}
    if amount is not None:
        data["amount"] = amount
    if currency:
        data["currency"] = currency
    if price:
        data["price"] = price
    if quantity is not None:
        data["quantity"] = quantity
    if invoice:
        data["invoice"] = invoice
    if description:
        data["description"] = description
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    resp = requests.post(f"{BASE_URL}/invoiceitems", data=data, auth=_auth())
    return _handle(resp)


def get_invoice_item(invoiceitem_id: str) -> dict:
    """Retrieve an Invoice Item."""
    resp = requests.get(f"{BASE_URL}/invoiceitems/{invoiceitem_id}", auth=_auth())
    return _handle(resp)


def update_invoice_item(
    invoiceitem_id: str,
    amount: int = None,
    description: str = None,
    metadata: dict = None,
    quantity: int = None,
    price: str = None,
) -> dict:
    """Update an Invoice Item."""
    data = {}
    if amount is not None:
        data["amount"] = amount
    if description:
        data["description"] = description
    if quantity is not None:
        data["quantity"] = quantity
    if price:
        data["price"] = price
    if metadata:
        for k, v in metadata.items():
            data[f"metadata[{k}]"] = v
    resp = requests.post(
        f"{BASE_URL}/invoiceitems/{invoiceitem_id}", data=data, auth=_auth()
    )
    return _handle(resp)


def delete_invoice_item(invoiceitem_id: str) -> dict:
    """Delete an Invoice Item."""
    resp = requests.delete(
        f"{BASE_URL}/invoiceitems/{invoiceitem_id}", auth=_auth()
    )
    return _handle(resp)


def list_invoice_items(
    customer: str = None,
    invoice: str = None,
    limit: int = None,
    starting_after: str = None,
    ending_before: str = None,
) -> dict:
    """List Invoice Items."""
    params = {}
    if customer:
        params["customer"] = customer
    if invoice:
        params["invoice"] = invoice
    if limit is not None:
        params["limit"] = limit
    if starting_after:
        params["starting_after"] = starting_after
    if ending_before:
        params["ending_before"] = ending_before
    resp = requests.get(f"{BASE_URL}/invoiceitems", params=params, auth=_auth())
    return _handle(resp)
