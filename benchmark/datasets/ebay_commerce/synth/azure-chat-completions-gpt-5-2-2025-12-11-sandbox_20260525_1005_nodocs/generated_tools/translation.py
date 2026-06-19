from typing import Any, Dict, Optional

from .ebay_auth import auth_header, get_base_url, request_json


# Translation API (application token)


def translate(
    from_language: str,
    to_language: str,
    text: str,
    translation_context: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /commerce/translation/v1/translate"""
    url = get_base_url() + "/commerce/translation/v1/translate"
    body: Dict[str, Any] = {"from": from_language, "to": to_language, "text": [text]}
    if translation_context:
        body["translationContext"] = translation_context
    res, err = request_json("POST", url, headers={**auth_header(user=False), "Content-Type": "application/json"}, json=body)
    return err or res  # type: ignore
