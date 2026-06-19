"""
eBay Commerce Translation API tools.
Uses app token (client_credentials).
Base: /commerce/translation/v1_beta
"""
import requests
from .auth import BASE_URL, app_headers, safe_json

TRANSLATION_BASE = f"{BASE_URL}/commerce/translation/v1_beta"


def translate(
    text: list,
    from_language: str,
    to_language: str,
    translation_context: str,
) -> dict:
    """
    Translate listing title or description text from one language to another.
    Returns the original text and translated text.

    Args:
        text: List containing the text string(s) to translate. Currently only one
              string is supported per call.
        from_language: Source language code (e.g. 'en', 'de', 'fr', 'zh_HANT').
        to_language: Target language code (e.g. 'de', 'fr', 'zh_HANT', 'en').
        translation_context: Type of content being translated.
                             Valid values: 'ITEM_TITLE' (max 1000 chars) or
                             'ITEM_DESCRIPTION' (max 20,000 chars).
    """
    try:
        body = {
            "from": from_language,
            "to": to_language,
            "text": text,
            "translationContext": translation_context,
        }
        resp = requests.post(
            f"{TRANSLATION_BASE}/translate",
            headers=app_headers(),
            json=body,
            timeout=30,
        )
        return safe_json(resp)
    except Exception as e:
        return {"error": str(e)}
