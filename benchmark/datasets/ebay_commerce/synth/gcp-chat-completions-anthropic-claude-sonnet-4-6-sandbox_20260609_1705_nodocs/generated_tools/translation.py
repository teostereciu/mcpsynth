"""
eBay Commerce Translation API tools.
Uses app-token (client_credentials).
Base: /commerce/translation/v1
"""

from typing import Optional
import requests
from .auth import BASE_URL, app_headers, safe_json

_BASE = f"{BASE_URL}/commerce/translation/v1"


def translate(
    text: list,
    from_language: str,
    to_language: str,
    translation_context: Optional[str] = None,
) -> dict:
    """
    Translate one or more text strings from one language to another.

    Args:
        text: List of strings to translate (e.g. ['Hello', 'World']).
        from_language: BCP 47 source language code (e.g. 'en', 'de', 'fr').
        to_language: BCP 47 target language code (e.g. 'es', 'zh-Hant').
        translation_context: Optional context hint for the translation engine
            (e.g. 'ITEM_TITLE', 'ITEM_DESCRIPTION').
    """
    url = f"{_BASE}/translate"
    body: dict = {
        "text": text,
        "from": from_language,
        "to": to_language,
    }
    if translation_context:
        body["translationContext"] = translation_context
    resp = requests.post(url, headers=app_headers(), json=body, timeout=20)
    return safe_json(resp)
