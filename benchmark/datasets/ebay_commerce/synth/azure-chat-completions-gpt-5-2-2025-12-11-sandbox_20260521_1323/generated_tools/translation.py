from typing import Any, Dict

from .http_client import EbayClient


TRANSLATION_SCOPE = "https://api.ebay.com/oauth/api_scope"


def translate(from_lang: str, to_lang: str, text: str, translation_context: str) -> Dict[str, Any]:
    """POST /commerce/translation/v1_beta/translate

    Doc: docs/api_commerce_translation_resources_language_methods_translate.md
    """
    client = EbayClient()
    return client.request(
        "POST",
        "/commerce/translation/v1_beta/translate",
        json_body={"from": from_lang, "to": to_lang, "text": [text], "translationContext": translation_context},
        scope=TRANSLATION_SCOPE,
    )
