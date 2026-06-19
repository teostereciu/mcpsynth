"""Shopify Admin REST API — Shop, ScriptTags, Redirects, Themes tools."""

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

    # ── Shop ──────────────────────────────────────────────────────────────────

    @mcp.tool()
    def get_shop() -> dict:
        """Get information about the store (name, email, currency, timezone, etc.)."""
        s, base = _session()
        r = s.get(f"{base}/shop.json")
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    # ── Script Tags ───────────────────────────────────────────────────────────

    @mcp.tool()
    def list_script_tags(limit: int = 50) -> dict:
        """List all script tags."""
        s, base = _session()
        r = s.get(f"{base}/script_tags.json", params={"limit": limit})
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    @mcp.tool()
    def create_script_tag(src: str, event: str = "onload",
                          display_scope: str = "all") -> dict:
        """Create a script tag. display_scope: all|online_store|order_status."""
        s, base = _session()
        r = s.post(f"{base}/script_tags.json",
                   json={"script_tag": {"src": src, "event": event,
                                        "display_scope": display_scope}})
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    @mcp.tool()
    def delete_script_tag(script_tag_id: str) -> dict:
        """Delete a script tag."""
        s, base = _session()
        r = s.delete(f"{base}/script_tags/{script_tag_id}.json")
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return {"deleted": True, "script_tag_id": script_tag_id}

    # ── Redirects ─────────────────────────────────────────────────────────────

    @mcp.tool()
    def list_redirects(limit: int = 50) -> dict:
        """List URL redirects."""
        s, base = _session()
        r = s.get(f"{base}/redirects.json", params={"limit": limit})
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    @mcp.tool()
    def create_redirect(path: str, target: str) -> dict:
        """Create a URL redirect from path to target."""
        s, base = _session()
        r = s.post(f"{base}/redirects.json",
                   json={"redirect": {"path": path, "target": target}})
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    @mcp.tool()
    def update_redirect(redirect_id: str, path: str = "", target: str = "") -> dict:
        """Update a URL redirect."""
        s, base = _session()
        data: dict = {}
        if path:   data["path"]   = path
        if target: data["target"] = target
        r = s.put(f"{base}/redirects/{redirect_id}.json",
                  json={"redirect": data})
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    @mcp.tool()
    def delete_redirect(redirect_id: str) -> dict:
        """Delete a URL redirect."""
        s, base = _session()
        r = s.delete(f"{base}/redirects/{redirect_id}.json")
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return {"deleted": True, "redirect_id": redirect_id}

    # ── Themes ────────────────────────────────────────────────────────────────

    @mcp.tool()
    def list_themes() -> dict:
        """List all themes in the store."""
        s, base = _session()
        r = s.get(f"{base}/themes.json")
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    @mcp.tool()
    def get_theme(theme_id: str) -> dict:
        """Get a theme by ID."""
        s, base = _session()
        r = s.get(f"{base}/themes/{theme_id}.json")
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    @mcp.tool()
    def update_theme(theme_id: str, name: str = "", role: str = "") -> dict:
        """Update a theme name or role. role: main|unpublished."""
        s, base = _session()
        data: dict = {}
        if name: data["name"] = name
        if role: data["role"] = role
        r = s.put(f"{base}/themes/{theme_id}.json", json={"theme": data})
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    # ── Assets ────────────────────────────────────────────────────────────────

    @mcp.tool()
    def list_theme_assets(theme_id: str) -> dict:
        """List all assets in a theme."""
        s, base = _session()
        r = s.get(f"{base}/themes/{theme_id}/assets.json")
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    @mcp.tool()
    def get_theme_asset(theme_id: str, asset_key: str) -> dict:
        """Get a specific theme asset by key (e.g. 'templates/index.liquid')."""
        s, base = _session()
        r = s.get(f"{base}/themes/{theme_id}/assets.json",
                  params={"asset[key]": asset_key})
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    @mcp.tool()
    def upsert_theme_asset(theme_id: str, asset_key: str, value: str) -> dict:
        """Create or update a theme asset by key with text content."""
        s, base = _session()
        r = s.put(f"{base}/themes/{theme_id}/assets.json",
                  json={"asset": {"key": asset_key, "value": value}})
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    @mcp.tool()
    def delete_theme_asset(theme_id: str, asset_key: str) -> dict:
        """Delete a theme asset by key."""
        s, base = _session()
        r = s.delete(f"{base}/themes/{theme_id}/assets.json",
                     params={"asset[key]": asset_key})
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return {"deleted": True, "asset_key": asset_key}
