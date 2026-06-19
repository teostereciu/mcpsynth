from __future__ import annotations

from typing import Any, Dict, Optional

from . import mcp, client


@mcp.tool()
def get_shop(fields: Optional[str] = None) -> Dict[str, Any]:
    """Retrieve the shop's configuration.

    Args:
        fields: Optional comma-separated list of fields to include.

    Returns:
        Shop object dict or error dict.
    """
    params = {"fields": fields} if fields else None
    return client.request("GET", "/shop.json", params=params)
