"""Shopify Admin REST API — Shop, Gift Cards, Abandoned Checkouts, Events tools."""
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


def register_shop_misc(mcp: FastMCP):

    # ── Shop ──────────────────────────────────────────────────────────────────

    @mcp.tool()
    def get_shop(fields: str = None) -> dict:
        """Retrieve the shop's configuration and settings."""
        params = {}
        if fields: params["fields"] = fields
        return _get("/shop.json", params)

    # ── Gift Cards ────────────────────────────────────────────────────────────

    @mcp.tool()
    def list_gift_cards(
        status: str = None,
        limit: int = 50,
        fields: str = None,
    ) -> dict:
        """Retrieve a list of gift cards. status: enabled|disabled."""
        params = {"limit": limit}
        if status: params["status"] = status
        if fields: params["fields"] = fields
        return _get("/gift_cards.json", params)

    @mcp.tool()
    def get_gift_card(gift_card_id: int) -> dict:
        """Retrieve a single gift card by ID."""
        return _get(f"/gift_cards/{gift_card_id}.json")

    @mcp.tool()
    def count_gift_cards(status: str = None) -> dict:
        """Retrieve a count of gift cards. status: enabled|disabled."""
        params = {}
        if status: params["status"] = status
        return _get("/gift_cards/count.json", params)

    @mcp.tool()
    def search_gift_cards(query: str, limit: int = 50) -> dict:
        """Search for gift cards. e.g. query='last_characters:mnop'."""
        return _get("/gift_cards/search.json", {"query": query, "limit": limit})

    @mcp.tool()
    def create_gift_card(
        initial_value: str,
        code: str = None,
        note: str = None,
        expires_on: str = None,
        template_suffix: str = None,
        customer_id: int = None,
    ) -> dict:
        """Create a gift card. initial_value: e.g. '25.00'. code is optional (auto-generated if omitted)."""
        gc = {"initial_value": initial_value}
        if code: gc["code"] = code
        if note: gc["note"] = note
        if expires_on: gc["expires_on"] = expires_on
        if template_suffix: gc["template_suffix"] = template_suffix
        if customer_id: gc["customer_id"] = customer_id
        return _post("/gift_cards.json", {"gift_card": gc})

    @mcp.tool()
    def update_gift_card(
        gift_card_id: int,
        note: str = None,
        expires_on: str = None,
        template_suffix: str = None,
    ) -> dict:
        """Update an existing gift card (only note, expires_on, template_suffix can be changed)."""
        gc = {}
        if note is not None: gc["note"] = note
        if expires_on is not None: gc["expires_on"] = expires_on
        if template_suffix is not None: gc["template_suffix"] = template_suffix
        return _put(f"/gift_cards/{gift_card_id}.json", {"gift_card": gc})

    @mcp.tool()
    def disable_gift_card(gift_card_id: int) -> dict:
        """Disable a gift card. This action cannot be undone."""
        return _post(f"/gift_cards/{gift_card_id}/disable.json", {"gift_card": {"id": gift_card_id}})

    # ── Abandoned Checkouts ───────────────────────────────────────────────────

    @mcp.tool()
    def list_abandoned_checkouts(
        limit: int = 50,
        status: str = None,
        since_id: int = None,
        created_at_min: str = None,
        created_at_max: str = None,
        updated_at_min: str = None,
        updated_at_max: str = None,
    ) -> dict:
        """Retrieve a list of abandoned checkouts. status: open|closed."""
        params = {"limit": limit}
        if status: params["status"] = status
        if since_id: params["since_id"] = since_id
        if created_at_min: params["created_at_min"] = created_at_min
        if created_at_max: params["created_at_max"] = created_at_max
        if updated_at_min: params["updated_at_min"] = updated_at_min
        if updated_at_max: params["updated_at_max"] = updated_at_max
        return _get("/checkouts.json", params)

    # ── Events ────────────────────────────────────────────────────────────────

    @mcp.tool()
    def list_events(
        limit: int = 50,
        since_id: int = None,
        created_at_min: str = None,
        created_at_max: str = None,
        filter: str = None,
        verb: str = None,
        fields: str = None,
    ) -> dict:
        """Retrieve a list of events. filter: e.g. Product,Order. verb: e.g. create,update."""
        params = {"limit": limit}
        if since_id: params["since_id"] = since_id
        if created_at_min: params["created_at_min"] = created_at_min
        if created_at_max: params["created_at_max"] = created_at_max
        if filter: params["filter"] = filter
        if verb: params["verb"] = verb
        if fields: params["fields"] = fields
        return _get("/events.json", params)

    @mcp.tool()
    def get_event(event_id: int, fields: str = None) -> dict:
        """Retrieve a single event by ID."""
        params = {}
        if fields: params["fields"] = fields
        return _get(f"/events/{event_id}.json", params)

    @mcp.tool()
    def count_events(created_at_min: str = None, created_at_max: str = None) -> dict:
        """Retrieve a count of events."""
        params = {}
        if created_at_min: params["created_at_min"] = created_at_min
        if created_at_max: params["created_at_max"] = created_at_max
        return _get("/events/count.json", params)
