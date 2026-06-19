"""eBay Commerce Translation API tools — app-token authenticated."""
from __future__ import annotations
import os
from typing import List
import requests
from .auth import get_app_token

SANDBOX = os.getenv("EBAY_ENVIRONMENT", "SANDBOX").upper() == "SANDBOX"
BASE = "https://api.sandbox.ebay.com" if SANDBOX else "https://api.ebay.com"


def _headers() -> dict:
    token = get_app_token()
    return {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }


def translate_text(
    text: List[str],
    from_language: str,
    to_language: str,
    translation_context: str,
) -> dict:
    """Translate listing title or description text between languages.

    Args:
        text: List containing the text string(s) to translate (currently one at a time).
        from_language: Source language code (e.g. 'en', 'de', 'fr').
        to_language: Target language code (e.g. 'en', 'de', 'zh_HANT').
        translation_context: Either 'ITEM_TITLE' (max 1000 chars) or
                             'ITEM_DESCRIPTION' (max 20000 chars).
    """
    url = f"{BASE}/commerce/translation/v1_beta/translate"
    payload = {
        "from": from_language,
        "to": to_language,
        "text": text,
        "translationContext": translation_context,
    }
    try:
        resp = requests.post(url, headers=_headers(), json=payload, timeout=30)
        if resp.ok:
            return resp.json()
        return {"error": resp.text, "status_code": resp.status_code}
    except Exception as e:
        return {"error": str(e)}
