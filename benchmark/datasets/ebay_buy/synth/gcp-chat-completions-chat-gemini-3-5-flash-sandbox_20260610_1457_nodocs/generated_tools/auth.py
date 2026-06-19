import os
import base64
import time
import requests
from typing import Dict, Any, Optional

class eBayAuthManager:
    def __init__(self):
        self.app_id = os.environ.get("EBAY_APP_ID")
        self.cert_id = os.environ.get("EBAY_CERT_ID")
        self.environment = os.environ.get("EBAY_ENVIRONMENT", "SANDBOX").upper()
        
        if self.environment == "PRODUCTION":
            self.base_url = "https://api.ebay.com"
        else:
            self.base_url = "https://api.sandbox.ebay.com"
            
        self._token_cache: Dict[str, Any] = {}
        self._token_expiry: float = 0.0

    def get_headers(self, scopes: Optional[str] = None) -> Dict[str, str]:
        """
        Returns the authorization headers with a valid access token.
        """
        token = self.get_access_token(scopes)
        return {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "Accept": "application/json"
        }

    def get_access_token(self, scopes: Optional[str] = None) -> str:
        """
        Retrieves an OAuth access token using client credentials.
        Caches the token and refreshes it if expired.
        """
        if not self.app_id or not self.cert_id:
            raise ValueError("EBAY_APP_ID and EBAY_CERT_ID environment variables must be set.")

        # Default scopes for Buy API
        if not scopes:
            scopes = (
                "https://api.ebay.com/oauth/api_scope/buy.browse "
                "https://api.ebay.com/oauth/api_scope/buy.deal "
                "https://api.ebay.com/oauth/api_scope/buy.feed "
                "https://api.ebay.com/oauth/api_scope/buy.order.guest"
            )

        # Check cache
        now = time.time()
        if self._token_cache and now < self._token_expiry - 60:
            return self._token_cache.get("access_token", "")

        # Request new token
        token_url = f"{self.base_url}/identity/v1/oauth2/token"
        
        # Base64 encode client_id:client_secret
        credentials = f"{self.app_id}:{self.cert_id}"
        encoded_creds = base64.b64encode(credentials.encode("utf-8")).decode("utf-8")
        
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Authorization": f"Basic {encoded_creds}"
        }
        
        data = {
            "grant_type": "client_credentials",
            "scope": scopes
        }
        
        try:
            response = requests.post(token_url, headers=headers, data=data, timeout=15)
            response.raise_for_status()
            token_data = response.json()
            
            self._token_cache = token_data
            # Cache expiry time (expires_in is usually 7200 seconds)
            expires_in = token_data.get("expires_in", 7200)
            self._token_expiry = now + expires_in
            
            return token_data.get("access_token", "")
        except Exception as e:
            raise RuntimeError(f"Failed to retrieve eBay OAuth token: {str(e)}")

# Global auth manager instance
auth_manager = eBayAuthManager()
