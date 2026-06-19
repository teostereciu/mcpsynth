from typing import Any, Dict, List

from .http import EbayAuth, request_json


AUTH = EbayAuth()


def translate(from_lang: str, to_lang: str, text: str, translation_context: str) -> Dict[str, Any]:
    """POST /commerce/translation/v1_beta/translate"""
    token = AUTH.get_app_token("https://api.ebay.com/oauth/api_scope")
    if token.startswith("{"):
        return {"error": "oauth_error", "details": token}

    payload: Dict[str, Any] = {
        "from": from_lang,
        "to": to_lang,
        "text": [text],
        "translationContext": translation_context,
    }
    return request_json(
        method="POST",
        path="/commerce/translation/v1_beta/translate",
        json_body=payload,
        access_token=token,
    )
