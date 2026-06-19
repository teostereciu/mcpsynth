from __future__ import annotations

from typing import Any, Dict, List, Optional, Union

from . import mcp, client


@mcp.tool()
def list_locations(limit: int = 50) -> List[Dict[str, Any]]:
    """List locations."""
    return client.request("GET", "/locations.json", params={"limit": limit})


@mcp.tool()
def get_location(location_id: Union[int, str]) -> Dict[str, Any]:
    """Get a location."""
    return client.request("GET", f"/locations/{location_id}.json")


@mcp.tool()
def list_shipping_zones() -> Any:
    """List shipping zones."""
    return client.request("GET", "/shipping_zones.json")


@mcp.tool()
def list_countries() -> Any:
    """List countries."""
    return client.request("GET", "/countries.json")


@mcp.tool()
def list_currencies() -> Any:
    """List currencies."""
    return client.request("GET", "/currencies.json")


@mcp.tool()
def list_policies() -> Any:
    """List shop policies."""
    return client.request("GET", "/policies.json")


@mcp.tool()
def list_users() -> Any:
    """List users."""
    return client.request("GET", "/users.json")
