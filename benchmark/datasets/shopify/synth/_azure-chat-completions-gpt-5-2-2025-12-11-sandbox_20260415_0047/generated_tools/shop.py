from typing import Any, Dict, Optional

from . import mcp
from .http import ShopifyClient, unwrap_envelope


@mcp.tool()
def get_shop_info(fields: Optional[str] = None) -> Dict[str, Any]:
    """Retrieve shop configuration.

    Args:
        fields: Optional comma-separated list of fields.

    Returns:
        Shop object.
    """
    client = ShopifyClient()
    params = {"fields": fields} if fields else None
    data = client.request("GET", "/shop.json", params=params)
    return unwrap_envelope(data)
