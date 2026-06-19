"""Shopify Admin REST API — Orders, Draft Orders, Refunds, Transactions tools."""
import os, requests
from typing import Optional, Any

BASE_URL = f"https://{os.environ.get('SHOPIFY_STORE_URL', '')}/admin/api/2026-01"

def _headers():
    return {
        "X-Shopify-Access-Token": os.environ.get("SHOPIFY_ACCESS_TOKEN", ""),
        "Content-Type": "application/json",
    }

def _get(path, params=None):
    try:
        r = requests.get(f"{BASE_URL}{path}", headers=_headers(), params=params, timeout=30)
        return r.json()
    except Exception as e:
        return {"error": str(e)}

def _post(path, payload):
    try:
        r = requests.post(f"{BASE_URL}{path}", headers=_headers(), json=payload, timeout=30)
        return r.json()
    except Exception as e:
        return {"error": str(e)}

def _put(path, payload):
    try:
        r = requests.put(f"{BASE_URL}{path}", headers=_headers(), json=payload, timeout=30)
        return r.json()
    except Exception as e:
        return {"error": str(e)}

def _delete(path):
    try:
        r = requests.delete(f"{BASE_URL}{path}", headers=_headers(), timeout=30)
        if r.status_code == 200:
            return r.json()
        return {"status": r.status_code}
    except Exception as e:
        return {"error": str(e)}


# ── Orders ────────────────────────────────────────────────────────────────────

def list_orders(limit: int = 50, status: Optional[str] = None,
                financial_status: Optional[str] = None,
                fulfillment_status: Optional[str] = None,
                created_at_min: Optional[str] = None,
                created_at_max: Optional[str] = None,
                ids: Optional[str] = None) -> dict:
    """Retrieve a list of orders. status: open|closed|cancelled|any."""
    params: dict[str, Any] = {"limit": limit}
    if status: params["status"] = status
    if financial_status: params["financial_status"] = financial_status
    if fulfillment_status: params["fulfillment_status"] = fulfillment_status
    if created_at_min: params["created_at_min"] = created_at_min
    if created_at_max: params["created_at_max"] = created_at_max
    if ids: params["ids"] = ids
    return _get("/orders.json", params)

def get_order(order_id: int) -> dict:
    """Retrieve a specific order by ID."""
    return _get(f"/orders/{order_id}.json")

def count_orders(status: Optional[str] = None) -> dict:
    """Retrieve a count of orders."""
    params = {}
    if status: params["status"] = status
    return _get("/orders/count.json", params)

def create_order(line_items: list, customer: Optional[dict] = None,
                 billing_address: Optional[dict] = None,
                 shipping_address: Optional[dict] = None,
                 financial_status: Optional[str] = None,
                 send_receipt: bool = False,
                 send_fulfillment_receipt: bool = False,
                 note: Optional[str] = None,
                 tags: Optional[str] = None) -> dict:
    """Create a new order."""
    order: dict[str, Any] = {"line_items": line_items,
                              "send_receipt": send_receipt,
                              "send_fulfillment_receipt": send_fulfillment_receipt}
    if customer: order["customer"] = customer
    if billing_address: order["billing_address"] = billing_address
    if shipping_address: order["shipping_address"] = shipping_address
    if financial_status: order["financial_status"] = financial_status
    if note: order["note"] = note
    if tags: order["tags"] = tags
    return _post("/orders.json", {"order": order})

def update_order(order_id: int, note: Optional[str] = None,
                 email: Optional[str] = None, tags: Optional[str] = None,
                 shipping_address: Optional[dict] = None) -> dict:
    """Update an existing order."""
    order: dict[str, Any] = {"id": order_id}
    if note is not None: order["note"] = note
    if email is not None: order["email"] = email
    if tags is not None: order["tags"] = tags
    if shipping_address is not None: order["shipping_address"] = shipping_address
    return _put(f"/orders/{order_id}.json", {"order": order})

def delete_order(order_id: int) -> dict:
    """Delete an order."""
    return _delete(f"/orders/{order_id}.json")

def cancel_order(order_id: int, reason: Optional[str] = None,
                 email: bool = False, refund: bool = False) -> dict:
    """Cancel an order. reason: customer|fraud|inventory|declined|other."""
    payload: dict[str, Any] = {"email": email, "refund": refund}
    if reason: payload["reason"] = reason
    return _post(f"/orders/{order_id}/cancel.json", payload)

def close_order(order_id: int) -> dict:
    """Close an order."""
    return _post(f"/orders/{order_id}/close.json", {})

def open_order(order_id: int) -> dict:
    """Re-open a closed order."""
    return _post(f"/orders/{order_id}/open.json", {})


# ── Draft Orders ──────────────────────────────────────────────────────────────

def list_draft_orders(limit: int = 50, status: Optional[str] = None) -> dict:
    """Retrieve a list of draft orders."""
    params: dict[str, Any] = {"limit": limit}
    if status: params["status"] = status
    return _get("/draft_orders.json", params)

def get_draft_order(draft_order_id: int) -> dict:
    """Retrieve a single draft order."""
    return _get(f"/draft_orders/{draft_order_id}.json")

def count_draft_orders() -> dict:
    """Retrieve a count of draft orders."""
    return _get("/draft_orders/count.json")

def create_draft_order(line_items: list, customer: Optional[dict] = None,
                       customer_id: Optional[int] = None,
                       email: Optional[str] = None,
                       shipping_address: Optional[dict] = None,
                       billing_address: Optional[dict] = None,
                       note: Optional[str] = None,
                       tags: Optional[str] = None,
                       applied_discount: Optional[dict] = None,
                       use_customer_default_address: bool = False) -> dict:
    """Create a new draft order."""
    draft: dict[str, Any] = {"line_items": line_items,
                              "use_customer_default_address": use_customer_default_address}
    if customer: draft["customer"] = customer
    if customer_id: draft["customer_id"] = customer_id
    if email: draft["email"] = email
    if shipping_address: draft["shipping_address"] = shipping_address
    if billing_address: draft["billing_address"] = billing_address
    if note: draft["note"] = note
    if tags: draft["tags"] = tags
    if applied_discount: draft["applied_discount"] = applied_discount
    return _post("/draft_orders.json", {"draft_order": draft})

def update_draft_order(draft_order_id: int, line_items: Optional[list] = None,
                       note: Optional[str] = None, email: Optional[str] = None,
                       tags: Optional[str] = None,
                       applied_discount: Optional[dict] = None,
                       shipping_address: Optional[dict] = None) -> dict:
    """Update an existing draft order."""
    draft: dict[str, Any] = {"id": draft_order_id}
    if line_items is not None: draft["line_items"] = line_items
    if note is not None: draft["note"] = note
    if email is not None: draft["email"] = email
    if tags is not None: draft["tags"] = tags
    if applied_discount is not None: draft["applied_discount"] = applied_discount
    if shipping_address is not None: draft["shipping_address"] = shipping_address
    return _put(f"/draft_orders/{draft_order_id}.json", {"draft_order": draft})

def complete_draft_order(draft_order_id: int, payment_pending: bool = False) -> dict:
    """Complete a draft order (convert to order)."""
    return _put(f"/draft_orders/{draft_order_id}/complete.json",
                {"payment_pending": payment_pending})

def send_draft_order_invoice(draft_order_id: int, to: Optional[str] = None,
                             subject: Optional[str] = None,
                             custom_message: Optional[str] = None) -> dict:
    """Send an invoice for a draft order."""
    invoice: dict[str, Any] = {}
    if to: invoice["to"] = to
    if subject: invoice["subject"] = subject
    if custom_message: invoice["custom_message"] = custom_message
    return _post(f"/draft_orders/{draft_order_id}/send_invoice.json",
                 {"draft_order_invoice": invoice})

def delete_draft_order(draft_order_id: int) -> dict:
    """Delete a draft order."""
    return _delete(f"/draft_orders/{draft_order_id}.json")


# ── Refunds ───────────────────────────────────────────────────────────────────

def list_refunds(order_id: int) -> dict:
    """Retrieve a list of refunds for an order."""
    return _get(f"/orders/{order_id}/refunds.json")

def get_refund(order_id: int, refund_id: int) -> dict:
    """Retrieve a specific refund."""
    return _get(f"/orders/{order_id}/refunds/{refund_id}.json")

def calculate_refund(order_id: int, refund_line_items: Optional[list] = None,
                     shipping: Optional[dict] = None) -> dict:
    """Calculate a refund before creating it."""
    payload: dict[str, Any] = {}
    if refund_line_items: payload["refund_line_items"] = refund_line_items
    if shipping: payload["shipping"] = shipping
    return _post(f"/orders/{order_id}/refunds/calculate.json", {"refund": payload})

def create_refund(order_id: int, transactions: Optional[list] = None,
                  refund_line_items: Optional[list] = None,
                  shipping: Optional[dict] = None,
                  note: Optional[str] = None,
                  notify: bool = False,
                  currency: Optional[str] = None) -> dict:
    """Create a refund for an order."""
    refund: dict[str, Any] = {"notify": notify}
    if transactions: refund["transactions"] = transactions
    if refund_line_items: refund["refund_line_items"] = refund_line_items
    if shipping: refund["shipping"] = shipping
    if note: refund["note"] = note
    if currency: refund["currency"] = currency
    return _post(f"/orders/{order_id}/refunds.json", {"refund": refund})


# ── Transactions ──────────────────────────────────────────────────────────────

def list_transactions(order_id: int) -> dict:
    """Retrieve a list of transactions for an order."""
    return _get(f"/orders/{order_id}/transactions.json")

def get_transaction(order_id: int, transaction_id: int) -> dict:
    """Retrieve a specific transaction."""
    return _get(f"/orders/{order_id}/transactions/{transaction_id}.json")

def count_transactions(order_id: int) -> dict:
    """Retrieve a count of transactions for an order."""
    return _get(f"/orders/{order_id}/transactions/count.json")

def create_transaction(order_id: int, kind: str, amount: Optional[str] = None,
                       currency: Optional[str] = None,
                       parent_id: Optional[int] = None,
                       gateway: Optional[str] = None,
                       test: bool = False) -> dict:
    """Create a transaction for an order. kind: authorization|capture|sale|void|refund."""
    txn: dict[str, Any] = {"kind": kind, "test": test}
    if amount: txn["amount"] = amount
    if currency: txn["currency"] = currency
    if parent_id: txn["parent_id"] = parent_id
    if gateway: txn["gateway"] = gateway
    return _post(f"/orders/{order_id}/transactions.json", {"transaction": txn})
