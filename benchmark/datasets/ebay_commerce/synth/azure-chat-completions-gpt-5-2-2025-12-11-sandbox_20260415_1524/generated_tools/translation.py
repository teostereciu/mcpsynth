from typing import Any, Dict

from .ebay_client import EbayClient


TRANSLATION_SCOPE_APP = "https://api.ebay.com/oauth/api_scope"


def translate(*, from_lang: str, to_lang: str, text: str, translation_context: str) -> Dict[str, Any]:
    """Translate listing title/description text.

    POST /commerce/translation/v1_beta/translate
    OAuth: app token
    """
    client = EbayClient()
    body: Dict[str, Any] = {
        "from": from_lang,
        "to": to_lang,
        "text": [text],
        "translationContext": translation_context,
    }
    return client.request(
        "POST",
        "/commerce/translation/v1_beta/translate",
        json_body=body,
        headers={"Content-Type": "application/json"},
        scope=TRANSLATION_SCOPE_APP,
        user=False,
        is_media=False,
    )
