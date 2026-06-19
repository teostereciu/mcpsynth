"""Shopify Admin REST API — Fulfillment, Fulfillment Orders, Locations tools."""

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

    # ── Fulfillments ──────────────────────────────────────────────────────────

    @mcp.tool()
    def list_fulfillments(order_id: str, limit: int = 50) -> dict:
        """List all fulfillments for an order."""
        s, base = _session()
        r = s.get(f"{base}/orders/{order_id}/fulfillments.json",
                  params={"limit": limit})
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    @mcp.tool()
    def get_fulfillment(order_id: str, fulfillment_id: str) -> dict:
        """Get a specific fulfillment for an order."""
        s, base = _session()
        r = s.get(f"{base}/orders/{order_id}/fulfillments/{fulfillment_id}.json")
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    @mcp.tool()
    def create_fulfillment(order_id: str, location_id: str,
                           line_items_by_fulfillment_order: list,
                           tracking_number: str = "", tracking_company: str = "",
                           tracking_url: str = "", notify_customer: bool = True) -> dict:
        """Create a fulfillment for an order.
        line_items_by_fulfillment_order: list of {fulfillment_order_id} dicts."""
        s, base = _session()
        data: dict = {
            "location_id": location_id,
            "line_items_by_fulfillment_order": line_items_by_fulfillment_order,
            "notify_customer": notify_customer,
        }
        if tracking_number:  data["tracking_number"]  = tracking_number
        if tracking_company: data["tracking_company"] = tracking_company
        if tracking_url:     data["tracking_url"]     = tracking_url
        r = s.post(f"{base}/orders/{order_id}/fulfillments.json",
                   json={"fulfillment": data})
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    @mcp.tool()
    def update_fulfillment_tracking(order_id: str, fulfillment_id: str,
                                    tracking_number: str = "",
                                    tracking_company: str = "",
                                    tracking_url: str = "",
                                    notify_customer: bool = True) -> dict:
        """Update tracking info for a fulfillment."""
        s, base = _session()
        data: dict = {"notify_customer": notify_customer}
        if tracking_number:  data["tracking_number"]  = tracking_number
        if tracking_company: data["tracking_company"] = tracking_company
        if tracking_url:     data["tracking_url"]     = tracking_url
        r = s.post(
            f"{base}/orders/{order_id}/fulfillments/{fulfillment_id}/update_tracking.json",
            json={"fulfillment": data})
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    @mcp.tool()
    def cancel_fulfillment(order_id: str, fulfillment_id: str) -> dict:
        """Cancel a fulfillment."""
        s, base = _session()
        r = s.post(
            f"{base}/orders/{order_id}/fulfillments/{fulfillment_id}/cancel.json")
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    # ── Fulfillment Orders ────────────────────────────────────────────────────

    @mcp.tool()
    def list_fulfillment_orders(order_id: str) -> dict:
        """List fulfillment orders for an order."""
        s, base = _session()
        r = s.get(f"{base}/orders/{order_id}/fulfillment_orders.json")
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    @mcp.tool()
    def get_fulfillment_order(fulfillment_order_id: str) -> dict:
        """Get a specific fulfillment order by ID."""
        s, base = _session()
        r = s.get(f"{base}/fulfillment_orders/{fulfillment_order_id}.json")
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    @mcp.tool()
    def cancel_fulfillment_order(fulfillment_order_id: str) -> dict:
        """Cancel a fulfillment order."""
        s, base = _session()
        r = s.post(f"{base}/fulfillment_orders/{fulfillment_order_id}/cancel.json")
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    @mcp.tool()
    def move_fulfillment_order(fulfillment_order_id: str, new_location_id: str) -> dict:
        """Move a fulfillment order to a new location."""
        s, base = _session()
        r = s.post(
            f"{base}/fulfillment_orders/{fulfillment_order_id}/move.json",
            json={"fulfillment_order": {"new_location_id": new_location_id}})
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    @mcp.tool()
    def hold_fulfillment_order(fulfillment_order_id: str, reason: str,
                               reason_notes: str = "") -> dict:
        """Place a fulfillment hold on a fulfillment order."""
        s, base = _session()
        data: dict = {"reason": reason}
        if reason_notes:
            data["reason_notes"] = reason_notes
        r = s.post(
            f"{base}/fulfillment_orders/{fulfillment_order_id}/hold.json",
            json={"fulfillment_hold": data})
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    @mcp.tool()
    def release_fulfillment_hold(fulfillment_order_id: str) -> dict:
        """Release a fulfillment hold."""
        s, base = _session()
        r = s.post(
            f"{base}/fulfillment_orders/{fulfillment_order_id}/release_hold.json")
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    # ── Locations ─────────────────────────────────────────────────────────────

    @mcp.tool()
    def list_locations() -> dict:
        """List all locations for the store."""
        s, base = _session()
        r = s.get(f"{base}/locations.json")
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    @mcp.tool()
    def get_location(location_id: str) -> dict:
        """Get a specific location by ID."""
        s, base = _session()
        r = s.get(f"{base}/locations/{location_id}.json")
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    @mcp.tool()
    def count_locations() -> dict:
        """Count all locations."""
        s, base = _session()
        r = s.get(f"{base}/locations/count.json")
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    @mcp.tool()
    def list_location_inventory_levels(location_id: str, limit: int = 50) -> dict:
        """List inventory levels at a specific location."""
        s, base = _session()
        r = s.get(f"{base}/locations/{location_id}/inventory_levels.json",
                  params={"limit": limit})
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()
