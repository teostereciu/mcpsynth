from typing import Any, Dict

from .ebay_client import EbayClient


TRANSLATION_SCOPE = "https://api.ebay.com/oauth/api_scope"


def translate_text(
    *,
    from_language: str,
    to_language: str,
    text: str,
    translation_context: str = "ITEM_TITLE",
) -> Dict[str, Any]:
    """POST /commerce/translation/v1_beta/translate"""
    client = EbayClient()
    body: Dict[str, Any] = {
        "from": from_language,
        "to": to_language,
        "text": [text],
        "translationContext": translation_context,
    }
    return client.request(
        "POST",
        client.api_base,
        "/commerce/translation/v1_beta/translate",
        json_body=body,
        headers={"Content-Type": "application/json"},
        auth="app",
        scope=TRANSLATION_SCOPE,
    )
