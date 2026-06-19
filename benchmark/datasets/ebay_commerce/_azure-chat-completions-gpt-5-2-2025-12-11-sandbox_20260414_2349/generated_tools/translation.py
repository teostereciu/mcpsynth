from __future__ import annotations

from typing import Any, Dict, List

from .http import commerce_base_url, request_json


API_SCOPE = "https://api.ebay.com/oauth/api_scope"


def translate_text(text: str, from_language: str, to_language: str, translation_context: str) -> Dict[str, Any]:
    """POST /commerce/translation/v1_beta/translate

    Args:
        text: input text (single string)
        from_language: e.g. 'en'
        to_language: e.g. 'de'
        translation_context: ITEM_TITLE or ITEM_DESCRIPTION
    """
    body: Dict[str, Any] = {
        "from": from_language,
        "to": to_language,
        "translationContext": translation_context,
        "text": [text],
    }
    return request_json(
        "POST",
        commerce_base_url(),
        "/commerce/translation/v1_beta/translate",
        json_body=body,
        user_auth=False,
        scope=API_SCOPE,
    )
