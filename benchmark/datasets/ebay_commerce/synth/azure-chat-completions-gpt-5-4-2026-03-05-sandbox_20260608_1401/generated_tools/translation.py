from typing import Dict, Any

from generated_tools.catalog import client


def translate(from_language: str, to_language: str, text: str, translation_context: str) -> Dict[str, Any]:
    return client.request(
        "POST",
        "/commerce/translation/v1_beta/translate",
        token_type="app",
        json_body={
            "from": from_language,
            "to": to_language,
            "text": [text],
            "translationContext": translation_context,
        },
        headers={"Content-Type": "application/json"},
    )
