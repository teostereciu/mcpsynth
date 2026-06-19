"""eBay Commerce Translation API tools."""
from mcp.server.fastmcp import FastMCP
from .auth import get_app_token, get_base_url

def register(mcp: FastMCP):

    @mcp.tool()
    def translate_text(
        text: list,
        from_language: str,
        to_language: str,
        translation_context: str,
    ) -> dict:
        """Translate listing title or description text from one language to another.

        Args:
            text: List containing the text string(s) to translate. Currently only
                  one string is supported per call.
            from_language: Source language code (e.g. 'en', 'de', 'fr', 'zh_HANT').
            to_language: Target language code (e.g. 'de', 'fr', 'zh_HANT', 'en').
            translation_context: Context for translation. Valid values:
                                 'ITEM_TITLE' (max 1000 chars) or
                                 'ITEM_DESCRIPTION' (max 20,000 chars).
        """
        import requests
        token = get_app_token()
        if "error" in token:
            return token
        url = f"{get_base_url()}/commerce/translation/v1_beta/translate"
        headers = {
            "Authorization": f"Bearer {token['access_token']}",
            "Content-Type": "application/json",
        }
        payload = {
            "from": from_language,
            "to": to_language,
            "text": text,
            "translationContext": translation_context,
        }
        try:
            resp = requests.post(url, headers=headers, json=payload, timeout=30)
            if resp.status_code == 200:
                return resp.json()
            return {"error": resp.text, "status_code": resp.status_code}
        except Exception as e:
            return {"error": str(e)}
