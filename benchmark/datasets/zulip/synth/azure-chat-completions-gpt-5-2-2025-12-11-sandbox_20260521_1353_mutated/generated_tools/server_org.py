from typing import Any, Dict

from .http_client import ZulipClient


def get_server_settings() -> Dict[str, Any]:
    """GET /server_settings

    Doc: docs/api_get-server-settings.md
    """
    client = ZulipClient()
    return client.request("GET", "/server_settings")
