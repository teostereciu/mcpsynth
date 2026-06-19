"""
eBay Commerce Translation API tools.
Base URL: https://api.sandbox.ebay.com/commerce/translation/v1_beta
Auth: App token (client_credentials)
"""

import requests
from .auth import app_headers, _base_url


def _translation_url(path: str) -> str:
    return f"{_base_url()}/commerce/translation/v1_beta{path}"


def translate(
    text: list[str],
    from_language: str,
    to_language: str,
    translation_context: str,
) -> dict:
    """
    Translate listing title or description text from one language to another.

    text: list containing the text to translate (currently only one string supported).
    from_language: source language code, e.g. 'en', 'de', 'fr', 'zh_HANS', 'es', 'it'.
    to_language: target language code, e.g. 'de', 'en', 'fr', 'zh_HANS', 'es', 'it'.
    translation_context: 'ITEM_TITLE' (max 1000 chars) or 'ITEM_DESCRIPTION' (max 20,000 chars).

    Returns from, to, and translations array with originalText and translatedText.
    """
    try:
        headers = app_headers()
        headers["Content-Type"] = "application/json"
        resp = requests.post(
            _translation_url("/translate"),
            headers=headers,
            json={
                "from": from_language,
                "to": to_language,
                "text": text,
                "translationContext": translation_context,
            },
            timeout=30,
        )
        if resp.status_code == 200:
            return resp.json()
        return {"error": resp.text, "status_code": resp.status_code}
    except Exception as e:
        return {"error": str(e)}
