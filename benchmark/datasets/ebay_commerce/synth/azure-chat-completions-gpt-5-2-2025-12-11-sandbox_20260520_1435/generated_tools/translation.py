from typing import Any, Dict

from .http_client import EbayHTTP


TRANSLATION_SCOPE_APP = "https://api.ebay.com/oauth/api_scope"


def translate(*, from_lang: str, to_lang: str, text: str, translation_context: str) -> Dict[str, Any]:
    """POST /commerce/translation/v1_beta/translate

    Doc: docs/api_commerce_translation_resources_language_methods_translate.md

    translation_context: ITEM_TITLE or ITEM_DESCRIPTION
    """
    http = EbayHTTP()
    body = {
        "from": from_lang,
        "to": to_lang,
        "text": [text],
        "translationContext": translation_context,
    }
    return http.request(
        "POST",
        http.oauth.api_base,
        "/commerce/translation/v1_beta/translate",
        scope=TRANSLATION_SCOPE_APP,
        json=body,
        headers={"Content-Type": "application/json"},
    )
