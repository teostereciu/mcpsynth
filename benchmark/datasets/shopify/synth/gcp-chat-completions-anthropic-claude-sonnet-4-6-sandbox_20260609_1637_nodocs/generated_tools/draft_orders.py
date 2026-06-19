"""Shopify Admin REST API — Draft Orders tools."""

import os, requests
from mcp.server.fastmcp import FastMCP

def _session():
    token = os.environ["SHOPIFY_ACCESS_TOKEN"]
    store = os.environ["SHOPIFY_STORE_URL"]
    base  = f"https://{store}/admin/api/2026-01"
    s = requests.Session()
    s.headers.update({"X-Shopify-Access-Token": token, "Content-Type": "application/json"})
    return s, base

def register(mcp: FastMCP):

    @mcp.tool()
    def list_draft_orders(limit: int = 50, status: str = "", page_info: str = "") -> dict:
        """List draft orders. status: open|invoice_sent|completed."""
        s, base = _session()
        params: dict = {"limit": limit}
        if status:    params["status"]    = status
        if page_info: params["page_info"] = page_info
        r = s.get(f"{base}/draft_orders.json", params=params)
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    @mcp.tool()
    def get_draft_order(draft_order_id: str) -> dict:
        """Get a single draft order by ID."""
        s, base = _session()
        r = s.get(f"{base}/draft_orders/{draft_order_id}.json")
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    @mcp.tool()
    def create_draft_order(line_items: list, customer_id: str = "",
                           email: str = "", note: str = "",
                           use_customer_default_address: bool = True,
                           shipping_address: dict = {},
                           billing_address: dict = {},
                           applied_discount: dict = {}) -> dict:
        """Create a draft order.
        line_items: list of {variant_id, quantity} or {title, price, quantity} dicts."""
        s, base = _session()
        data: dict = {"line_items": line_items,
                      "use_customer_default_address": use_customer_default_address}
        if customer_id:       data["customer"]          = {"id": customer_id}
        if email:             data["email"]             = email
        if note:              data["note"]              = note
        if shipping_address:  data["shipping_address"]  = shipping_address
        if billing_address:   data["billing_address"]   = billing_address
        if applied_discount:  data["applied_discount"]  = applied_discount
        r = s.post(f"{base}/draft_orders.json", json={"draft_order": data})
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    @mcp.tool()
    def update_draft_order(draft_order_id: str, line_items: list = [],
                           note: str = "", email: str = "",
                           applied_discount: dict = {},
                           shipping_address: dict = {}) -> dict:
        """Update a draft order."""
        s, base = _session()
        data: dict = {}
        if line_items:       data["line_items"]       = line_items
        if note:             data["note"]             = note
        if email:            data["email"]            = email
        if applied_discount: data["applied_discount"] = applied_discount
        if shipping_address: data["shipping_address"] = shipping_address
        r = s.put(f"{base}/draft_orders/{draft_order_id}.json",
                  json={"draft_order": data})
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    @mcp.tool()
    def delete_draft_order(draft_order_id: str) -> dict:
        """Delete a draft order."""
        s, base = _session()
        r = s.delete(f"{base}/draft_orders/{draft_order_id}.json")
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return {"deleted": True, "draft_order_id": draft_order_id}

    @mcp.tool()
    def complete_draft_order(draft_order_id: str, payment_pending: bool = False) -> dict:
        """Mark a draft order as complete (converts to order)."""
        s, base = _session()
        r = s.put(f"{base}/draft_orders/{draft_order_id}/complete.json",
                  params={"payment_pending": str(payment_pending).lower()})
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    @mcp.tool()
    def send_draft_order_invoice(draft_order_id: str, to: str = "",
                                 subject: str = "", custom_message: str = "") -> dict:
        """Send an invoice email for a draft order."""
        s, base = _session()
        data: dict = {}
        if to:             data["to"]             = to
        if subject:        data["subject"]        = subject
        if custom_message: data["custom_message"] = custom_message
        r = s.post(f"{base}/draft_orders/{draft_order_id}/send_invoice.json",
                   json={"draft_order_invoice": data})
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    @mcp.tool()
    def count_draft_orders(status: str = "") -> dict:
        """Count draft orders."""
        s, base = _session()
        params = {}
        if status:
            params["status"] = status
        r = s.get(f"{base}/draft_orders/count.json", params=params)
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()
