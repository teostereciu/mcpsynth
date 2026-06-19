from typing import Any, Dict, Optional

from .ebay_auth import request_json


# Translation API (application token)


def translate(text: str, from_language: str, to_language: str, translation_context: str = "ITEM_TITLE") -> Dict[str, Any]:
    """POST /commerce/translation/v1/translate"""
    status, body = request_json(
        "POST",
        "/commerce/translation/v1/translate",
        json={
            "from": from_language,
            "to": to_language,
            "text": [text],
            "translationContext": translation_context,
        },
        user=False,
    )
    return {"status": status, "data": body}
