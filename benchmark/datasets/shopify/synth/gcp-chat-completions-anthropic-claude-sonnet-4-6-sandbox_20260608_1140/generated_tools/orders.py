"""Shopify Admin REST API — Orders, Draft Orders, Refunds tools."""
import os, requests
from mcp.server.fastmcp import FastMCP

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

def _post(path, body=None):
    try:
        r = requests.post(f"{BASE_URL}{path}", headers=_headers(), json=body, timeout=30)
        return r.json()
    except Exception as e:
        return {"error": str(e)}

def _put(path, body):
    try:
        r = requests.put(f"{BASE_URL}{path}", headers=_headers(), json=body, timeout=30)
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


def register_orders(mcp: FastMCP):

    # ── Orders ────────────────────────────────────────────────────────────────

    @mcp.tool()
    def list_orders(
        limit: int = 50,
        status: str = "any",
        financial_status: str = None,
        fulfillment_status: str = None,
        ids: str = None,
        since_id: int = None,
        created_at_min: str = None,
        created_at_max: str = None,
        fields: str = None,
    ) -> dict:
        """Retrieve a list of orders. status: open|closed|cancelled|any."""
        params = {"limit": limit, "status": status}
        if financial_status: params["financial_status"] = financial_status
        if fulfillment_status: params["fulfillment_status"] = fulfillment_status
        if ids: params["ids"] = ids
        if since_id: params["since_id"] = since_id
        if created_at_min: params["created_at_min"] = created_at_min
        if created_at_max: params["created_at_max"] = created_at_max
        if fields: params["fields"] = fields
        return _get("/orders.json", params)

    @mcp.tool()
    def get_order(order_id: int, fields: str = None) -> dict:
        """Retrieve a specific order by ID."""
        params = {}
        if fields: params["fields"] = fields
        return _get(f"/orders/{order_id}.json", params)

    @mcp.tool()
    def count_orders(status: str = "any", financial_status: str = None, fulfillment_status: str = None) -> dict:
        """Retrieve a count of orders."""
        params = {"status": status}
        if financial_status: params["financial_status"] = financial_status
        if fulfillment_status: params["fulfillment_status"] = fulfillment_status
        return _get("/orders/count.json", params)

    @mcp.tool()
    def create_order(
        line_items: list,
        customer: dict = None,
        billing_address: dict = None,
        shipping_address: dict = None,
        financial_status: str = None,
        send_receipt: bool = False,
        send_fulfillment_receipt: bool = False,
        note: str = None,
        tags: str = None,
        inventory_behaviour: str = "bypass",
    ) -> dict:
        """Create a new order. line_items: list of {variant_id, quantity} or {title, price, quantity}."""
        order = {
            "line_items": line_items,
            "send_receipt": send_receipt,
            "send_fulfillment_receipt": send_fulfillment_receipt,
            "inventory_behaviour": inventory_behaviour,
        }
        if customer: order["customer"] = customer
        if billing_address: order["billing_address"] = billing_address
        if shipping_address: order["shipping_address"] = shipping_address
        if financial_status: order["financial_status"] = financial_status
        if note: order["note"] = note
        if tags: order["tags"] = tags
        return _post("/orders.json", {"order": order})

    @mcp.tool()
    def update_order(
        order_id: int,
        note: str = None,
        tags: str = None,
        email: str = None,
        shipping_address: dict = None,
    ) -> dict:
        """Update an existing order."""
        order = {}
        if note is not None: order["note"] = note
        if tags is not None: order["tags"] = tags
        if email is not None: order["email"] = email
        if shipping_address is not None: order["shipping_address"] = shipping_address
        return _put(f"/orders/{order_id}.json", {"order": order})

    @mcp.tool()
    def delete_order(order_id: int) -> dict:
        """Delete an order."""
        return _delete(f"/orders/{order_id}.json")

    @mcp.tool()
    def cancel_order(
        order_id: int,
        reason: str = None,
        email: bool = False,
        refund: bool = False,
        restock: bool = False,
    ) -> dict:
        """Cancel an order. reason: customer|fraud|inventory|declined|other."""
        body = {"email": email, "refund": refund, "restock": restock}
        if reason: body["reason"] = reason
        return _post(f"/orders/{order_id}/cancel.json", body)

    @mcp.tool()
    def close_order(order_id: int) -> dict:
        """Close an order."""
        return _post(f"/orders/{order_id}/close.json", {})

    @mcp.tool()
    def open_order(order_id: int) -> dict:
        """Re-open a closed order."""
        return _post(f"/orders/{order_id}/open.json", {})

    # ── Draft Orders ──────────────────────────────────────────────────────────

    @mcp.tool()
    def list_draft_orders(
        limit: int = 50,
        status: str = None,
        ids: str = None,
        fields: str = None,
    ) -> dict:
        """Retrieve a list of draft orders. status: open|invoice_sent|completed."""
        params = {"limit": limit}
        if status: params["status"] = status
        if ids: params["ids"] = ids
        if fields: params["fields"] = fields
        return _get("/draft_orders.json", params)

    @mcp.tool()
    def get_draft_order(draft_order_id: int, fields: str = None) -> dict:
        """Retrieve a single draft order."""
        params = {}
        if fields: params["fields"] = fields
        return _get(f"/draft_orders/{draft_order_id}.json", params)

    @mcp.tool()
    def count_draft_orders(status: str = None) -> dict:
        """Retrieve a count of draft orders."""
        params = {}
        if status: params["status"] = status
        return _get("/draft_orders/count.json", params)

    @mcp.tool()
    def create_draft_order(
        line_items: list,
        customer_id: int = None,
        email: str = None,
        note: str = None,
        tags: str = None,
        shipping_address: dict = None,
        billing_address: dict = None,
        applied_discount: dict = None,
        use_customer_default_address: bool = False,
    ) -> dict:
        """Create a draft order. line_items: list of {variant_id, quantity} or {title, price, quantity}."""
        draft = {"line_items": line_items, "use_customer_default_address": use_customer_default_address}
        if customer_id: draft["customer"] = {"id": customer_id}
        if email: draft["email"] = email
        if note: draft["note"] = note
        if tags: draft["tags"] = tags
        if shipping_address: draft["shipping_address"] = shipping_address
        if billing_address: draft["billing_address"] = billing_address
        if applied_discount: draft["applied_discount"] = applied_discount
        return _post("/draft_orders.json", {"draft_order": draft})

    @mcp.tool()
    def update_draft_order(
        draft_order_id: int,
        line_items: list = None,
        note: str = None,
        tags: str = None,
        email: str = None,
        applied_discount: dict = None,
    ) -> dict:
        """Update an existing draft order."""
        draft = {}
        if line_items is not None: draft["line_items"] = line_items
        if note is not None: draft["note"] = note
        if tags is not None: draft["tags"] = tags
        if email is not None: draft["email"] = email
        if applied_discount is not None: draft["applied_discount"] = applied_discount
        return _put(f"/draft_orders/{draft_order_id}.json", {"draft_order": draft})

    @mcp.tool()
    def delete_draft_order(draft_order_id: int) -> dict:
        """Delete a draft order."""
        return _delete(f"/draft_orders/{draft_order_id}.json")

    @mcp.tool()
    def complete_draft_order(draft_order_id: int, payment_pending: bool = False) -> dict:
        """Complete a draft order (converts it to an order)."""
        return _put(f"/draft_orders/{draft_order_id}/complete.json", {"payment_pending": payment_pending})

    @mcp.tool()
    def send_draft_order_invoice(
        draft_order_id: int,
        to: str = None,
        subject: str = None,
        custom_message: str = None,
    ) -> dict:
        """Send an invoice for a draft order."""
        invoice = {}
        if to: invoice["to"] = to
        if subject: invoice["subject"] = subject
        if custom_message: invoice["custom_message"] = custom_message
        return _post(f"/draft_orders/{draft_order_id}/send_invoice.json", {"draft_order_invoice": invoice})

    # ── Refunds ───────────────────────────────────────────────────────────────

    @mcp.tool()
    def list_refunds(order_id: int, fields: str = None) -> dict:
        """Retrieve a list of refunds for an order."""
        params = {}
        if fields: params["fields"] = fields
        return _get(f"/orders/{order_id}/refunds.json", params)

    @mcp.tool()
    def get_refund(order_id: int, refund_id: int, fields: str = None) -> dict:
        """Retrieve a specific refund."""
        params = {}
        if fields: params["fields"] = fields
        return _get(f"/orders/{order_id}/refunds/{refund_id}.json", params)

    @mcp.tool()
    def calculate_refund(
        order_id: int,
        refund_line_items: list = None,
        shipping: dict = None,
    ) -> dict:
        """Calculate a refund before creating it. Returns suggested transactions."""
        body = {}
        if refund_line_items: body["refund_line_items"] = refund_line_items
        if shipping: body["shipping"] = shipping
        return _post(f"/orders/{order_id}/refunds/calculate.json", {"refund": body})

    @mcp.tool()
    def create_refund(
        order_id: int,
        refund_line_items: list = None,
        transactions: list = None,
        note: str = None,
        notify: bool = False,
        shipping: dict = None,
        currency: str = None,
    ) -> dict:
        """Create a refund for an order. Use calculate_refund first to get transactions."""
        refund = {"notify": notify}
        if refund_line_items: refund["refund_line_items"] = refund_line_items
        if transactions: refund["transactions"] = transactions
        if note: refund["note"] = note
        if shipping: refund["shipping"] = shipping
        if currency: refund["currency"] = currency
        return _post(f"/orders/{order_id}/refunds.json", {"refund": refund})
