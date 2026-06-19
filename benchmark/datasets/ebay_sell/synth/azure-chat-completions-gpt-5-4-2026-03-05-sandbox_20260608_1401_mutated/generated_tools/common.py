import json
import os
import time
from typing import Any, Dict, Optional
from urllib.parse import urlencode

import requests


TOKEN_CACHE: Dict[str, Any] = {"access_token": None, "expires_at": 0.0}


class EbayClient:
    def __init__(self) -> None:
        env = os.getenv("EBAY_ENVIRONMENT", "SANDBOX").upper()
        self.base_url = "https://api.sandbox.ebay.com" if env == "SANDBOX" else "https://api.ebay.com"
        self.app_id = os.getenv("EBAY_APP_ID")
        self.cert_id = os.getenv("EBAY_CERT_ID")
        self.refresh_token = os.getenv("EBAY_REFRESH_TOKEN")

    def _token(self) -> str:
        if TOKEN_CACHE["access_token"] and TOKEN_CACHE["expires_at"] > time.time() + 60:
            return TOKEN_CACHE["access_token"]
        if not self.app_id or not self.cert_id or not self.refresh_token:
            raise ValueError("Missing one or more required environment variables: EBAY_APP_ID, EBAY_CERT_ID, EBAY_REFRESH_TOKEN")
        response = requests.post(
            f"{self.base_url}/identity/v1/oauth2/token",
            auth=(self.app_id, self.cert_id),
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            data={
                "grant_type": "refresh_token",
                "refresh_token": self.refresh_token,
                "scope": "https://api.ebay.com/oauth/api_scope/sell.account https://api.ebay.com/oauth/api_scope/sell.inventory https://api.ebay.com/oauth/api_scope/sell.fulfillment https://api.ebay.com/oauth/api_scope/sell.marketing https://api.ebay.com/oauth/api_scope/sell.finances https://api.ebay.com/oauth/api_scope/sell.feed",
            },
            timeout=60,
        )
        response.raise_for_status()
        data = response.json()
        TOKEN_CACHE["access_token"] = data["access_token"]
        TOKEN_CACHE["expires_at"] = time.time() + int(data.get("expires_in", 7200))
        return TOKEN_CACHE["access_token"]

    def request(
        self,
        method: str,
        path: str,
        *,
        params: Optional[Dict[str, Any]] = None,
        json_body: Optional[Any] = None,
        headers: Optional[Dict[str, str]] = None,
        data: Optional[Any] = None,
    ) -> Any:
        try:
            token = self._token()
            req_headers = {
                "Authorization": f"Bearer {token}",
                "Accept": "application/json",
            }
            if headers:
                req_headers.update({k: v for k, v in headers.items() if v is not None})
            response = requests.request(
                method,
                f"{self.base_url}{path}",
                params={k: v for k, v in (params or {}).items() if v is not None},
                json=json_body,
                headers=req_headers,
                data=data,
                timeout=120,
            )
            if response.status_code == 204:
                return {"status": 204, "success": True}
            content_type = response.headers.get("Content-Type", "")
            if response.ok:
                if "application/json" in content_type:
                    return response.json()
                return {"status": response.status_code, "content": response.text}
            try:
                err = response.json()
            except Exception:
                err = {"message": response.text}
            return {"error": True, "status": response.status_code, "details": err}
        except requests.HTTPError as exc:
            return {"error": str(exc)}
        except Exception as exc:
            return {"error": str(exc)}


client = EbayClient()


def clean_params(**kwargs: Any) -> Dict[str, Any]:
    return {k: v for k, v in kwargs.items() if v is not None}
