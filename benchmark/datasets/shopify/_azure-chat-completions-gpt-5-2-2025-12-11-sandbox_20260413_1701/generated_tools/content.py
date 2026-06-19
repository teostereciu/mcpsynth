from __future__ import annotations

from typing import Any, Dict, Optional

from . import mcp, client


@mcp.tool()
def get_theme(theme_id: int) -> Dict[str, Any]:
    """Get a theme by ID."""
    return client.request("GET", f"/themes/{theme_id}.json")


@mcp.tool()
def list_themes() -> Any:
    """List themes."""
    return client.request("GET", "/themes.json")


@mcp.tool()
def get_asset(theme_id: int, key: str) -> Dict[str, Any]:
    """Get a theme asset by key."""
    return client.request("GET", f"/themes/{theme_id}/assets.json", params={"asset[key]": key})


@mcp.tool()
def update_asset(theme_id: int, asset: Dict[str, Any]) -> Dict[str, Any]:
    """Create/update a theme asset."""
    return client.request("PUT", f"/themes/{theme_id}/assets.json", body={"asset": asset})
