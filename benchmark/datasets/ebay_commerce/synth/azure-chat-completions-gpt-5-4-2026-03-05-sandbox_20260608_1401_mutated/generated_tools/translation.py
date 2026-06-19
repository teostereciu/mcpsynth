from typing import Any, Dict

from .ebay_common import client


def translate_text(from_language: str, to_language: str, text: str, translation_context: str) -> Dict[str, Any]:
    return client.request(
        "POST",
        "/commerce/translation/v1_beta/translate",
        token_type="app",
        headers={"Content-Type": "application/json"},
        json_body={
            "from": from_language,
            "to": to_language,
            "text": [text],
            "translationContext": translation_context,
        },
    )
