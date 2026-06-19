from __future__ import annotations

from typing import Any, Dict

from .ebay_client import EbayClient


def translate_text(from_lang: str, to_lang: str, text: str, translation_context: str) -> Dict[str, Any]:
    """POST /translate

    translation_context: ITEM_TITLE or ITEM_DESCRIPTION

    OAuth scope: https://api.ebay.com/oauth/api_scope (app token)
    """
    client = EbayClient.for_standard_api(user_scoped=False)
    return client.request(
        "POST",
        "/commerce/translation/v1_beta/translate",
        json={"from": from_lang, "to": to_lang, "text": [text], "translationContext": translation_context},
    )
