"""
eBay Commerce Translation API tools.
Base path: /commerce/translation/v1_beta
Auth: app token (client_credentials)
"""

from .auth import app_post

_BASE = "/commerce/translation/v1_beta"


def translate_text(
    text: list[str],
    from_language: str,
    to_language: str,
    context: str | None = None,
    marketplace_id: str | None = None,
) -> dict:
    """
    Translate one or more text strings from one language to another using eBay's
    translation service (optimized for eBay listing content).

    Args:
        text: List of text strings to translate (max 5 strings, each max 1000 chars).
        from_language: Source language code (e.g. "en", "de", "fr", "zh_Hant").
        to_language: Target language code (e.g. "en", "de", "fr", "zh_Hant").
        context: Translation context hint — ITEM_TITLE, ITEM_DESCRIPTION, or ITEM_ASPECT.
        marketplace_id: Optional eBay marketplace ID for context (e.g. EBAY_US).

    Returns:
        Dict with translations list, each containing translatedText.
    """
    body: dict = {
        "text": text,
        "from": from_language,
        "to": to_language,
    }
    if context:
        body["context"] = context
    if marketplace_id:
        body["marketplaceId"] = marketplace_id
    return app_post(f"{_BASE}/translate", json_body=body)
