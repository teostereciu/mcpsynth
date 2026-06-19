"""Shopify Admin REST API — Shipping Zones, Carrier Services, Checkouts tools."""

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

    # ── Shipping Zones ────────────────────────────────────────────────────────

    @mcp.tool()
    def list_shipping_zones() -> dict:
        """List all shipping zones."""
        s, base = _session()
        r = s.get(f"{base}/shipping_zones.json")
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    # ── Carrier Services ──────────────────────────────────────────────────────

    @mcp.tool()
    def list_carrier_services() -> dict:
        """List all carrier services."""
        s, base = _session()
        r = s.get(f"{base}/carrier_services.json")
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    @mcp.tool()
    def create_carrier_service(name: str, callback_url: str,
                               service_discovery: bool = True,
                               carrier_service_type: str = "api") -> dict:
        """Create a carrier service for custom shipping rates."""
        s, base = _session()
        data: dict = {
            "name": name,
            "callback_url": callback_url,
            "service_discovery": service_discovery,
            "carrier_service_type": carrier_service_type,
        }
        r = s.post(f"{base}/carrier_services.json",
                   json={"carrier_service": data})
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    @mcp.tool()
    def update_carrier_service(carrier_service_id: str, name: str = "",
                               callback_url: str = "",
                               active: bool = None) -> dict:
        """Update a carrier service."""
        s, base = _session()
        data: dict = {}
        if name:            data["name"]         = name
        if callback_url:    data["callback_url"] = callback_url
        if active is not None: data["active"]    = active
        r = s.put(f"{base}/carrier_services/{carrier_service_id}.json",
                  json={"carrier_service": data})
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    @mcp.tool()
    def delete_carrier_service(carrier_service_id: str) -> dict:
        """Delete a carrier service."""
        s, base = _session()
        r = s.delete(f"{base}/carrier_services/{carrier_service_id}.json")
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return {"deleted": True, "carrier_service_id": carrier_service_id}

    # ── Checkouts ─────────────────────────────────────────────────────────────

    @mcp.tool()
    def list_checkouts(limit: int = 50) -> dict:
        """List abandoned checkouts."""
        s, base = _session()
        r = s.get(f"{base}/checkouts.json", params={"limit": limit})
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    @mcp.tool()
    def count_checkouts() -> dict:
        """Count abandoned checkouts."""
        s, base = _session()
        r = s.get(f"{base}/checkouts/count.json")
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()
