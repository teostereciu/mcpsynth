from typing import Any, Dict

from .ebay_http import EbayClient, json_loads_maybe


APP_SCOPE = "https://api.ebay.com/oauth/api_scope"


def translate(payload: Any) -> Dict[str, Any]:
    """POST /commerce/translation/v1/translate"""
    c = EbayClient()
    body = json_loads_maybe(payload)
    if not isinstance(body, dict):
        return {"error": "payload must be a JSON object"}
    return c.request(
        "POST",
        "/commerce/translation/v1/translate",
        json_body=body,
        app_scope=APP_SCOPE,
    )
