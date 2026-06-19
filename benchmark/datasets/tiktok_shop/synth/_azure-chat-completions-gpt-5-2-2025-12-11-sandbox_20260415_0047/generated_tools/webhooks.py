from __future__ import annotations

from typing import Any, Dict

from . import mcp
from .http import tiktok_request


@mcp.tool()
def webhooks_get_shop_webhooks() -> Dict[str, Any]:
    """List shop webhooks.

    API: GET /webhook/202309/webhooks
    """

    return tiktok_request("GET", "/webhook/202309/webhooks")


@mcp.tool()
def webhooks_update_shop_webhook(callback_url: str, event_types: list[str]) -> Dict[str, Any]:
    """Update shop webhook.

    API: PUT /webhook/202309/webhooks
    """

    body = {"callback_url": callback_url, "event_types": event_types}
    return tiktok_request("PUT", "/webhook/202309/webhooks", body=body)


@mcp.tool()
def webhooks_delete_shop_webhook() -> Dict[str, Any]:
    """Delete shop webhook.

    API: DELETE /webhook/202309/webhooks
    """

    return tiktok_request("DELETE", "/webhook/202309/webhooks")
