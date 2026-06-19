import base64
import os
from typing import Any, Dict, Optional

import requests


class ConfluenceClient:
    def __init__(
        self,
        base_url: Optional[str] = None,
        email: Optional[str] = None,
        api_token: Optional[str] = None,
        timeout: int = 30,
    ):
        self.base_url = (base_url or os.getenv("CONFLUENCE_BASE_URL") or "").rstrip("/")
        self.email = email or os.getenv("JIRA_EMAIL")
        self.api_token = api_token or os.getenv("JIRA_API_TOKEN")
        self.timeout = timeout

    def _auth_header(self) -> Dict[str, str]:
        if not self.email or not self.api_token:
            return {}
        token = base64.b64encode(f"{self.email}:{self.api_token}".encode("utf-8")).decode("ascii")
        return {"Authorization": f"Basic {token}"}

    def request(
        self,
        method: str,
        path: str,
        params: Optional[Dict[str, Any]] = None,
        json: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        files: Any = None,
        data: Any = None,
        stream: bool = False,
    ) -> Any:
        if not self.base_url:
            return {"error": "CONFLUENCE_BASE_URL is not set"}
        url = f"{self.base_url}{path}"
        h = {"Accept": "application/json", **self._auth_header()}
        if headers:
            h.update(headers)
        try:
            resp = requests.request(
                method=method,
                url=url,
                params=params,
                json=json,
                headers=h,
                files=files,
                data=data,
                timeout=self.timeout,
                stream=stream,
            )
        except requests.RequestException as e:
            return {"error": str(e)}

        if resp.status_code == 204:
            return {"ok": True, "status": 204}

        content_type = resp.headers.get("Content-Type", "")
        if "application/json" in content_type:
            try:
                body = resp.json()
            except ValueError:
                body = {"raw": resp.text}
        else:
            body = {"raw": resp.text}

        if resp.ok:
            return body
        return {
            "error": "request_failed",
            "status": resp.status_code,
            "body": body,
        }
