import os
import time
from typing import Any, Dict, Optional, Union

import requests


class ZendeskClient:
    def __init__(
        self,
        subdomain: Optional[str] = None,
        email: Optional[str] = None,
        api_token: Optional[str] = None,
        timeout: int = 30,
    ):
        self.subdomain = subdomain or os.getenv("ZENDESK_SUBDOMAIN")
        self.email = email or os.getenv("ZENDESK_EMAIL")
        self.api_token = api_token or os.getenv("ZENDESK_API_TOKEN")
        self.timeout = timeout

        if not self.subdomain or not self.email or not self.api_token:
            raise ValueError(
                "Missing Zendesk credentials. Set ZENDESK_SUBDOMAIN, ZENDESK_EMAIL, ZENDESK_API_TOKEN."
            )

        self.base_support = f"https://{self.subdomain}.zendesk.com/api/v2"
        self.base_help_center = f"https://{self.subdomain}.zendesk.com/api/v2/help_center"

        self.session = requests.Session()
        self.session.auth = (f"{self.email}/token", self.api_token)
        self.session.headers.update({"Accept": "application/json"})

    def request(
        self,
        method: str,
        url: str,
        *,
        params: Optional[Dict[str, Any]] = None,
        json: Optional[Dict[str, Any]] = None,
        data: Any = None,
        headers: Optional[Dict[str, str]] = None,
        files: Any = None,
        retry_429: bool = True,
    ) -> Union[Dict[str, Any], str]:
        try:
            resp = self.session.request(
                method,
                url,
                params=params,
                json=json,
                data=data,
                headers=headers,
                files=files,
                timeout=self.timeout,
            )

            if resp.status_code == 429 and retry_429:
                retry_after = int(resp.headers.get("Retry-After", "1"))
                time.sleep(max(1, retry_after))
                return self.request(
                    method,
                    url,
                    params=params,
                    json=json,
                    data=data,
                    headers=headers,
                    files=files,
                    retry_429=False,
                )

            if resp.status_code >= 400:
                try:
                    payload = resp.json()
                except Exception:
                    payload = {"message": resp.text}
                return {
                    "error": True,
                    "status": resp.status_code,
                    "url": url,
                    "details": payload,
                }

            if resp.status_code == 204:
                return {"ok": True}

            ctype = resp.headers.get("Content-Type", "")
            if "application/json" in ctype:
                return resp.json()
            return resp.text
        except Exception as e:
            return {"error": True, "message": str(e), "url": url}


_client: Optional[ZendeskClient] = None


def get_client() -> ZendeskClient:
    global _client
    if _client is None:
        _client = ZendeskClient()
    return _client
