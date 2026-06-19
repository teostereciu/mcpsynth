"""Shopify Admin REST API — Fulfillment, FulfillmentOrder, Transactions tools."""
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


def register_fulfillment(mcp: FastMCP):

    # ── Transactions ──────────────────────────────────────────────────────────

    @mcp.tool()
    def list_transactions(order_id: int, fields: str = None) -> dict:
        """Retrieve a list of transactions for an order."""
        params = {}
        if fields: params["fields"] = fields
        return _get(f"/orders/{order_id}/transactions.json", params)

    @mcp.tool()
    def get_transaction(order_id: int, transaction_id: int, fields: str = None) -> dict:
        """Retrieve a specific transaction for an order."""
        params = {}
        if fields: params["fields"] = fields
        return _get(f"/orders/{order_id}/transactions/{transaction_id}.json", params)

    @mcp.tool()
    def count_transactions(order_id: int) -> dict:
        """Retrieve a count of transactions for an order."""
        return _get(f"/orders/{order_id}/transactions/count.json")

    @mcp.tool()
    def create_transaction(
        order_id: int,
        kind: str,
        amount: str = None,
        currency: str = None,
        parent_id: int = None,
        gateway: str = None,
        authorization: str = None,
        test: bool = False,
    ) -> dict:
        """Create a transaction for an order. kind: authorization|capture|sale|void|refund."""
        txn = {"kind": kind, "test": test}
        if amount: txn["amount"] = amount
        if currency: txn["currency"] = currency
        if parent_id: txn["parent_id"] = parent_id
        if gateway: txn["gateway"] = gateway
        if authorization: txn["authorization"] = authorization
        return _post(f"/orders/{order_id}/transactions.json", {"transaction": txn})

    # ── Fulfillments ──────────────────────────────────────────────────────────

    @mcp.tool()
    def list_fulfillments_by_order(order_id: int, fields: str = None) -> dict:
        """Retrieve fulfillments associated with an order."""
        params = {}
        if fields: params["fields"] = fields
        return _get(f"/orders/{order_id}/fulfillments.json", params)

    @mcp.tool()
    def list_fulfillments_by_fulfillment_order(fulfillment_order_id: int) -> dict:
        """Retrieve fulfillments associated with a fulfillment order."""
        return _get(f"/fulfillment_orders/{fulfillment_order_id}/fulfillments.json")

    @mcp.tool()
    def get_fulfillment(order_id: int, fulfillment_id: int, fields: str = None) -> dict:
        """Retrieve a single fulfillment."""
        params = {}
        if fields: params["fields"] = fields
        return _get(f"/orders/{order_id}/fulfillments/{fulfillment_id}.json", params)

    @mcp.tool()
    def count_fulfillments(order_id: int) -> dict:
        """Retrieve a count of fulfillments for an order."""
        return _get(f"/orders/{order_id}/fulfillments/count.json")

    @mcp.tool()
    def create_fulfillment(
        line_items_by_fulfillment_order: list,
        tracking_info: dict = None,
        notify_customer: bool = False,
    ) -> dict:
        """Create a fulfillment for one or many fulfillment orders.
        line_items_by_fulfillment_order: list of {fulfillment_order_id, fulfillment_order_line_items}.
        tracking_info: {number, url, company}."""
        body = {
            "fulfillment": {
                "line_items_by_fulfillment_order": line_items_by_fulfillment_order,
                "notify_customer": notify_customer,
            }
        }
        if tracking_info:
            body["fulfillment"]["tracking_info"] = tracking_info
        return _post("/fulfillments.json", body)

    @mcp.tool()
    def cancel_fulfillment(fulfillment_id: int) -> dict:
        """Cancel a fulfillment."""
        return _post(f"/fulfillments/{fulfillment_id}/cancel.json", {})

    @mcp.tool()
    def update_fulfillment_tracking(
        fulfillment_id: int,
        tracking_info: dict,
        notify_customer: bool = False,
    ) -> dict:
        """Update tracking information for a fulfillment.
        tracking_info: {number, url, company}."""
        return _post(
            f"/fulfillments/{fulfillment_id}/update_tracking.json",
            {"fulfillment": {"tracking_info": tracking_info, "notify_customer": notify_customer}},
        )

    # ── Fulfillment Orders ────────────────────────────────────────────────────

    @mcp.tool()
    def list_fulfillment_orders(order_id: int) -> dict:
        """Retrieve a list of fulfillment orders for a specific order."""
        return _get(f"/orders/{order_id}/fulfillment_orders.json")

    @mcp.tool()
    def get_fulfillment_order(fulfillment_order_id: int) -> dict:
        """Retrieve a specific fulfillment order."""
        return _get(f"/fulfillment_orders/{fulfillment_order_id}.json")

    @mcp.tool()
    def cancel_fulfillment_order(fulfillment_order_id: int) -> dict:
        """Cancel a fulfillment order."""
        return _post(f"/fulfillment_orders/{fulfillment_order_id}/cancel.json", {})

    @mcp.tool()
    def close_fulfillment_order(fulfillment_order_id: int, message: str = None) -> dict:
        """Mark a fulfillment order as incomplete."""
        body = {}
        if message: body["message"] = message
        return _post(f"/fulfillment_orders/{fulfillment_order_id}/close.json", {"fulfillment_order": body})

    @mcp.tool()
    def hold_fulfillment_order(
        fulfillment_order_id: int,
        reason: str,
        reason_notes: str = None,
        notify_merchant: bool = False,
    ) -> dict:
        """Hold fulfillment of a fulfillment order.
        reason: awaiting_payment|high_risk_of_fraud|incorrect_address|inventory_out_of_stock|other."""
        hold = {"reason": reason, "notify_merchant": notify_merchant}
        if reason_notes: hold["reason_notes"] = reason_notes
        return _post(f"/fulfillment_orders/{fulfillment_order_id}/hold.json", {"fulfillment_hold": hold})

    @mcp.tool()
    def release_fulfillment_order_hold(fulfillment_order_id: int) -> dict:
        """Release all holds on a fulfillment order."""
        return _post(f"/fulfillment_orders/{fulfillment_order_id}/release_hold.json", {})

    @mcp.tool()
    def move_fulfillment_order(fulfillment_order_id: int, new_location_id: int) -> dict:
        """Move a fulfillment order to a new location."""
        return _post(
            f"/fulfillment_orders/{fulfillment_order_id}/move.json",
            {"fulfillment_order": {"new_location_id": new_location_id}},
        )

    @mcp.tool()
    def open_fulfillment_order(fulfillment_order_id: int) -> dict:
        """Mark a fulfillment order as open."""
        return _post(f"/fulfillment_orders/{fulfillment_order_id}/open.json", {})

    @mcp.tool()
    def reschedule_fulfillment_order(fulfillment_order_id: int, new_fulfill_at: str) -> dict:
        """Reschedule the fulfill_at time of a scheduled fulfillment order (ISO 8601)."""
        return _post(
            f"/fulfillment_orders/{fulfillment_order_id}/reschedule.json",
            {"fulfillment_order": {"new_fulfill_at": new_fulfill_at}},
        )

    # ── Fulfillment Requests ──────────────────────────────────────────────────

    @mcp.tool()
    def send_fulfillment_request(
        fulfillment_order_id: int,
        message: str = None,
        notify_customer: bool = False,
        fulfillment_order_line_items: list = None,
    ) -> dict:
        """Send a fulfillment request to the fulfillment service of a fulfillment order."""
        req = {"notify_customer": notify_customer}
        if message: req["message"] = message
        if fulfillment_order_line_items: req["fulfillment_order_line_items"] = fulfillment_order_line_items
        return _post(
            f"/fulfillment_orders/{fulfillment_order_id}/fulfillment_request.json",
            {"fulfillment_request": req},
        )

    @mcp.tool()
    def accept_fulfillment_request(fulfillment_order_id: int, message: str = None) -> dict:
        """Accept a fulfillment request (fulfillment service action)."""
        body = {}
        if message: body["message"] = message
        return _post(
            f"/fulfillment_orders/{fulfillment_order_id}/fulfillment_request/accept.json",
            {"fulfillment_request": body},
        )

    @mcp.tool()
    def reject_fulfillment_request(fulfillment_order_id: int, message: str = None) -> dict:
        """Reject a fulfillment request (fulfillment service action)."""
        body = {}
        if message: body["message"] = message
        return _post(
            f"/fulfillment_orders/{fulfillment_order_id}/fulfillment_request/reject.json",
            {"fulfillment_request": body},
        )

    # ── Order Risks ───────────────────────────────────────────────────────────

    @mcp.tool()
    def list_order_risks(order_id: int) -> dict:
        """Retrieve a list of all order risks for an order."""
        return _get(f"/orders/{order_id}/risks.json")

    @mcp.tool()
    def create_order_risk(
        order_id: int,
        message: str,
        recommendation: str,
        score: str,
        source: str = "External",
        cause_cancel: bool = False,
        display: bool = True,
    ) -> dict:
        """Create an order risk for an order.
        recommendation: cancel|investigate|accept. score: 0.0-1.0."""
        risk = {
            "message": message,
            "recommendation": recommendation,
            "score": score,
            "source": source,
            "cause_cancel": cause_cancel,
            "display": display,
        }
        return _post(f"/orders/{order_id}/risks.json", {"risk": risk})
