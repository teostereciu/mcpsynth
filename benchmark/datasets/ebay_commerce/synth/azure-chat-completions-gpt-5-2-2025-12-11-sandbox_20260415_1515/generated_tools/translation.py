from typing import Any, Dict, Optional

from .http_client import EbayHttpClient


class TranslationTools:
    def __init__(self, client: Optional[EbayHttpClient] = None):
        self.client = client or EbayHttpClient()

    def translate(self, *, from_lang: str, to_lang: str, text: str, translation_context: str) -> Dict[str, Any]:
        body = {
            "from": from_lang,
            "to": to_lang,
            "text": [text],
            "translationContext": translation_context,
        }
        return self.client.request(
            "POST",
            "/commerce/translation/v1_beta/translate",
            token_type="app",
            scope="https://api.ebay.com/oauth/api_scope",
            json_body=body,
            headers={"Content-Type": "application/json"},
        )
