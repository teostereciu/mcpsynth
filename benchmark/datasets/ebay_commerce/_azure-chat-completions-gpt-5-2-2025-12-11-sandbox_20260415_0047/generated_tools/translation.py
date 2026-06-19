"""Tools for eBay Commerce Translation API."""

from __future__ import annotations

from typing import Any, Dict, List

from .http import EbayApiError, error_dict, get_api_base_url, request_json


def translate_text(*, text: str, from_language: str, to_language: str, translation_context: str) -> Dict[str, Any]:
    """Translate text.

    Args:
        text: input text (single string)
        from_language: e.g. "en"
        to_language: e.g. "de"
        translation_context: "ITEM_TITLE" or "ITEM_DESCRIPTION"
    """
    try:
        body: Dict[str, Any] = {
            "from": from_language,
            "to": to_language,
            "translationContext": translation_context,
            "text": [text],
        }
        return request_json(
            method="POST",
            base_url=get_api_base_url(),
            path="/commerce/translation/v1_beta/translate",
            json_body=body,
            user_auth=False,
        )
    except EbayApiError as e:
        return error_dict(e)
