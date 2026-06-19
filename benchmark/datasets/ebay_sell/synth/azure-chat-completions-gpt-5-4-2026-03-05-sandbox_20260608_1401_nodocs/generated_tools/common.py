import os
import time
from typing import Any, Dict, Optional

import requests


class EbayClient:
    def __init__(self) -> None:
        env = os.getenv("EBAY_ENVIRONMENT", "SANDBOX").upper()
        self.base_url = "https://api.ebay.com" if env == "PRODUCTION" else "https://api.sandbox.ebay.com"
        self.client_id = os.getenv("EBAY_APP_ID", "")
        self.client_secret = os.getenv("EBAY_CERT_ID", "")
        self.refresh_token = os.getenv("EBAY_REFRESH_TOKEN", "")
        self._access_token: Optional[str] = None
        self._expires_at: float = 0.0

    def _token_error(self) -> Optional[Dict[str, Any]]:
        missing = []
        if not self.client_id:
            missing.append("EBAY_APP_ID")
        if not self.client_secret:
            missing.append("EBAY_CERT_ID")
        if not self.refresh_token:
            missing.append("EBAY_REFRESH_TOKEN")
        if missing:
            return {"error": f"Missing required environment variables: {', '.join(missing)}"}
        return None

    def get_access_token(self) -> str:
        if self._access_token and time.time() < self._expires_at - 60:
            return self._access_token
        token_error = self._token_error()
        if token_error:
            raise RuntimeError(token_error["error"])
        response = requests.post(
            f"{self.base_url}/identity/v1/oauth2/token",
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            auth=(self.client_id, self.client_secret),
            data={
                "grant_type": "refresh_token",
                "refresh_token": self.refresh_token,
                "scope": " ".join([
                    "https://api.ebay.com/oauth/api_scope",
                    "https://api.ebay.com/oauth/api_scope/sell.account",
                    "https://api.ebay.com/oauth/api_scope/sell.inventory",
                    "https://api.ebay.com/oauth/api_scope/sell.fulfillment",
                    "https://api.ebay.com/oauth/api_scope/sell.marketing",
                    "https://api.ebay.com/oauth/api_scope/sell.finances",
                    "https://api.ebay.com/oauth/api_scope/sell.fulfillment.readonly",
                    "https://api.ebay.com/oauth/api_scope/sell.account.readonly",
                    "https://api.ebay.com/oauth/api_scope/sell.inventory.readonly",
                    "https://api.ebay.com/oauth/api_scope/sell.marketing.readonly",
                    "https://api.ebay.com/oauth/api_scope/sell.finances.readonly",
                ])
            },
            timeout=60,
        )
        response.raise_for_status()
        payload = response.json()
        self._access_token = payload["access_token"]
        self._expires_at = time.time() + int(payload.get("expires_in", 7200))
        return self._access_token

    def request(
        self,
        method: str,
        path: str,
        *,
        params: Optional[Dict[str, Any]] = None,
        json_body: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Dict[str, Any]:
        token_error = self._token_error()
        if token_error:
            return token_error
        try:
            token = self.get_access_token()
            request_headers = {
                "Authorization": f"Bearer {token}",
                "Accept": "application/json",
                "Content-Type": "application/json",
            }
            if headers:
                request_headers.update(headers)
            response = requests.request(
                method,
                f"{self.base_url}{path}",
                params=params,
                json=json_body,
                headers=request_headers,
                timeout=120,
            )
            if response.status_code == 204:
                return {"success": True, "status_code": 204}
            content_type = response.headers.get("Content-Type", "")
            body: Any
            if "json" in content_type:
                body = response.json()
            else:
                body = {"text": response.text}
            if response.ok:
                return body if isinstance(body, dict) else {"data": body}
            return {
                "error": f"HTTP {response.status_code}",
                "status_code": response.status_code,
                "details": body,
            }
        except requests.HTTPError as exc:
            return {"error": str(exc)}
        except requests.RequestException as exc:
            return {"error": f"Request failed: {exc}"}
        except Exception as exc:
            return {"error": str(exc)}


client = EbayClient()
