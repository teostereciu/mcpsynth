"""Shopify Admin REST API — Orders, Refunds, Transactions tools."""

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

    # ── Orders ────────────────────────────────────────────────────────────────

    @mcp.tool()
    def list_orders(limit: int = 50, status: str = "any", page_info: str = "",
                    financial_status: str = "", fulfillment_status: str = "") -> dict:
        """List orders. status: open|closed|cancelled|any."""
        s, base = _session()
        params: dict = {"limit": limit, "status": status}
        if page_info:           params["page_info"]           = page_info
        if financial_status:    params["financial_status"]    = financial_status
        if fulfillment_status:  params["fulfillment_status"]  = fulfillment_status
        r = s.get(f"{base}/orders.json", params=params)
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    @mcp.tool()
    def get_order(order_id: str) -> dict:
        """Get a single order by ID."""
        s, base = _session()
        r = s.get(f"{base}/orders/{order_id}.json")
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    @mcp.tool()
    def count_orders(status: str = "any") -> dict:
        """Count orders in the store."""
        s, base = _session()
        r = s.get(f"{base}/orders/count.json", params={"status": status})
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    @mcp.tool()
    def close_order(order_id: str) -> dict:
        """Close an order."""
        s, base = _session()
        r = s.post(f"{base}/orders/{order_id}/close.json")
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    @mcp.tool()
    def reopen_order(order_id: str) -> dict:
        """Reopen a closed order."""
        s, base = _session()
        r = s.post(f"{base}/orders/{order_id}/open.json")
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    @mcp.tool()
    def cancel_order(order_id: str, reason: str = "", email: bool = False,
                     restock: bool = False) -> dict:
        """Cancel an order."""
        s, base = _session()
        data: dict = {"email": email, "restock": restock}
        if reason:
            data["reason"] = reason
        r = s.post(f"{base}/orders/{order_id}/cancel.json", json=data)
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    @mcp.tool()
    def update_order(order_id: str, note: str = "", email: str = "",
                     tags: str = "", shipping_address: dict = {}) -> dict:
        """Update order metadata (note, tags, email, shipping address)."""
        s, base = _session()
        data: dict = {}
        if note:             data["note"]             = note
        if email:            data["email"]            = email
        if tags:             data["tags"]             = tags
        if shipping_address: data["shipping_address"] = shipping_address
        r = s.put(f"{base}/orders/{order_id}.json", json={"order": data})
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    # ── Refunds ───────────────────────────────────────────────────────────────

    @mcp.tool()
    def list_refunds(order_id: str) -> dict:
        """List all refunds for an order."""
        s, base = _session()
        r = s.get(f"{base}/orders/{order_id}/refunds.json")
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    @mcp.tool()
    def get_refund(order_id: str, refund_id: str) -> dict:
        """Get a specific refund for an order."""
        s, base = _session()
        r = s.get(f"{base}/orders/{order_id}/refunds/{refund_id}.json")
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    @mcp.tool()
    def calculate_refund(order_id: str, line_items: list = [],
                         shipping: dict = {}, refund_line_items: list = []) -> dict:
        """Calculate a refund for an order without creating it."""
        s, base = _session()
        data: dict = {}
        if line_items:        data["line_items"]        = line_items
        if shipping:          data["shipping"]          = shipping
        if refund_line_items: data["refund_line_items"] = refund_line_items
        r = s.post(f"{base}/orders/{order_id}/refunds/calculate.json",
                   json={"refund": data})
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    @mcp.tool()
    def create_refund(order_id: str, note: str = "", notify: bool = False,
                      refund_line_items: list = [], transactions: list = [],
                      shipping: dict = {}) -> dict:
        """Create a refund for an order."""
        s, base = _session()
        data: dict = {"notify": notify}
        if note:               data["note"]               = note
        if refund_line_items:  data["refund_line_items"]  = refund_line_items
        if transactions:       data["transactions"]       = transactions
        if shipping:           data["shipping"]           = shipping
        r = s.post(f"{base}/orders/{order_id}/refunds.json", json={"refund": data})
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    # ── Transactions ──────────────────────────────────────────────────────────

    @mcp.tool()
    def list_transactions(order_id: str) -> dict:
        """List all transactions for an order."""
        s, base = _session()
        r = s.get(f"{base}/orders/{order_id}/transactions.json")
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    @mcp.tool()
    def get_transaction(order_id: str, transaction_id: str) -> dict:
        """Get a specific transaction for an order."""
        s, base = _session()
        r = s.get(f"{base}/orders/{order_id}/transactions/{transaction_id}.json")
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    @mcp.tool()
    def create_transaction(order_id: str, kind: str, amount: str = "",
                           currency: str = "", parent_id: str = "") -> dict:
        """Create a transaction for an order. kind: capture|void|refund|sale."""
        s, base = _session()
        data: dict = {"kind": kind}
        if amount:    data["amount"]    = amount
        if currency:  data["currency"]  = currency
        if parent_id: data["parent_id"] = parent_id
        r = s.post(f"{base}/orders/{order_id}/transactions.json",
                   json={"transaction": data})
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    # ── Order Risks ───────────────────────────────────────────────────────────

    @mcp.tool()
    def list_order_risks(order_id: str) -> dict:
        """List fraud risk assessments for an order."""
        s, base = _session()
        r = s.get(f"{base}/orders/{order_id}/risks.json")
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()
