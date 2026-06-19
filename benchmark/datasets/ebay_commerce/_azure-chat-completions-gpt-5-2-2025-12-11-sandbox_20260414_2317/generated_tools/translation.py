"""Tools for eBay Commerce Translation API."""

from __future__ import annotations

from typing import Any, Dict, List

from .http import request_json


def translate_text(text: str, from_language: str, to_language: str, translation_context: str) -> Dict[str, Any]:
    """Translate listing text.

    Docs: POST /commerce/translation/v1_beta/translate
    Auth: Application token

    Args:
        text: Input text (single string).
        from_language: LanguageEnum (e.g., 'en').
        to_language: LanguageEnum (e.g., 'de').
        translation_context: 'ITEM_TITLE' or 'ITEM_DESCRIPTION'.
    """

    body: Dict[str, Any] = {
        "from": from_language,
        "to": to_language,
        "translationContext": translation_context,
        "text": [text],
    }

    status, data, _ = request_json(
        "POST",
        "/commerce/translation/v1_beta/translate",
        json_body=body,
        user_auth=False,
        media=False,
    )
    return data
