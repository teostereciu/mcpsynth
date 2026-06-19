from typing import Any, Dict, Optional

from .http_client import EbayHttpClient


class IdentityTools:
    def __init__(self, client: Optional[EbayHttpClient] = None):
        self.client = client or EbayHttpClient()

    def get_user(self) -> Dict[str, Any]:
        # Docs show apiz.* host, but standard base works for most; keep path as documented.
        return self.client.request(
            "GET",
            "/commerce/identity/v1/user/",
            token_type="user",
            scope="https://api.ebay.com/oauth/api_scope/commerce.identity.readonly",
        )
