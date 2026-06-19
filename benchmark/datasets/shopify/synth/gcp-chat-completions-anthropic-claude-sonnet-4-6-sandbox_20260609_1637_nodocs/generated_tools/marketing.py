"""Shopify Admin REST API — Marketing Events, Gift Cards, Customer Saved Searches."""

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

    # ── Gift Cards ────────────────────────────────────────────────────────────

    @mcp.tool()
    def list_gift_cards(status: str = "enabled", limit: int = 50) -> dict:
        """List gift cards. status: enabled|disabled|all."""
        s, base = _session()
        r = s.get(f"{base}/gift_cards.json",
                  params={"status": status, "limit": limit})
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    @mcp.tool()
    def get_gift_card(gift_card_id: str) -> dict:
        """Get a gift card by ID."""
        s, base = _session()
        r = s.get(f"{base}/gift_cards/{gift_card_id}.json")
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    @mcp.tool()
    def create_gift_card(initial_value: str, code: str = "",
                         note: str = "", expires_on: str = "",
                         customer_id: str = "") -> dict:
        """Create a gift card. initial_value: e.g. '25.00'."""
        s, base = _session()
        data: dict = {"initial_value": initial_value}
        if code:        data["code"]        = code
        if note:        data["note"]        = note
        if expires_on:  data["expires_on"]  = expires_on
        if customer_id: data["customer_id"] = customer_id
        r = s.post(f"{base}/gift_cards.json", json={"gift_card": data})
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    @mcp.tool()
    def disable_gift_card(gift_card_id: str) -> dict:
        """Disable a gift card."""
        s, base = _session()
        r = s.post(f"{base}/gift_cards/{gift_card_id}/disable.json")
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    @mcp.tool()
    def search_gift_cards(query: str, limit: int = 50) -> dict:
        """Search gift cards by code."""
        s, base = _session()
        r = s.get(f"{base}/gift_cards/search.json",
                  params={"query": query, "limit": limit})
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    # ── Customer Saved Searches ───────────────────────────────────────────────

    @mcp.tool()
    def list_customer_saved_searches(limit: int = 50) -> dict:
        """List customer saved searches (segments)."""
        s, base = _session()
        r = s.get(f"{base}/customer_saved_searches.json", params={"limit": limit})
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    @mcp.tool()
    def create_customer_saved_search(name: str, query: str) -> dict:
        """Create a customer saved search (segment).
        query example: 'accepts_marketing:true AND country:US'."""
        s, base = _session()
        r = s.post(f"{base}/customer_saved_searches.json",
                   json={"customer_saved_search": {"name": name, "query": query}})
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    @mcp.tool()
    def delete_customer_saved_search(saved_search_id: str) -> dict:
        """Delete a customer saved search."""
        s, base = _session()
        r = s.delete(f"{base}/customer_saved_searches/{saved_search_id}.json")
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return {"deleted": True, "saved_search_id": saved_search_id}

    # ── Marketing Events ──────────────────────────────────────────────────────

    @mcp.tool()
    def list_marketing_events(limit: int = 50) -> dict:
        """List marketing events."""
        s, base = _session()
        r = s.get(f"{base}/marketing_events.json", params={"limit": limit})
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    @mcp.tool()
    def create_marketing_event(event_type: str, marketing_channel: str,
                               paid: bool = False, started_at: str = "",
                               ended_at: str = "", currency: str = "",
                               budget: str = "", budget_type: str = "") -> dict:
        """Create a marketing event.
        event_type: ad|post|message|retargeting|transactional|affiliate|loyalty|newsletter|abandoned_cart.
        marketing_channel: search|display|social|email|referral."""
        s, base = _session()
        data: dict = {"event_type": event_type,
                      "marketing_channel": marketing_channel,
                      "paid": paid}
        if started_at:   data["started_at"]   = started_at
        if ended_at:     data["ended_at"]     = ended_at
        if currency:     data["currency"]     = currency
        if budget:       data["budget"]       = budget
        if budget_type:  data["budget_type"]  = budget_type
        r = s.post(f"{base}/marketing_events.json",
                   json={"marketing_event": data})
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()
