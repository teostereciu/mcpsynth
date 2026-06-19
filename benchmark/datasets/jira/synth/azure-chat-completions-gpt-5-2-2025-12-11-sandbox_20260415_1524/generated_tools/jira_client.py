import base64
import json
import os
from typing import Any, Dict, Optional, Union

import requests


Json = Union[Dict[str, Any], list, str, int, float, bool, None]


class JiraClient:
    def __init__(
        self,
        base_url: Optional[str] = None,
        email: Optional[str] = None,
        api_token: Optional[str] = None,
        timeout: int = 60,
    ):
        self.base_url = (base_url or os.environ.get("JIRA_BASE_URL") or "").rstrip("/")
        self.email = email or os.environ.get("JIRA_EMAIL")
        self.api_token = api_token or os.environ.get("JIRA_API_TOKEN")
        self.timeout = timeout

        if not self.base_url:
            raise ValueError("JIRA_BASE_URL is required")
        if not self.email or not self.api_token:
            raise ValueError("JIRA_EMAIL and JIRA_API_TOKEN are required")

        self.api_root = f"{self.base_url}/rest/api/3"

    def _headers(self, accept: str = "application/json", content_type: Optional[str] = None) -> Dict[str, str]:
        token = base64.b64encode(f"{self.email}:{self.api_token}".encode("utf-8")).decode("ascii")
        headers = {
            "Authorization": f"Basic {token}",
            "Accept": accept,
        }
        if content_type:
            headers["Content-Type"] = content_type
        return headers

    def request(
        self,
        method: str,
        path: str,
        params: Optional[Dict[str, Any]] = None,
        json_body: Optional[Dict[str, Any]] = None,
        data: Any = None,
        headers: Optional[Dict[str, str]] = None,
        accept: str = "application/json",
        content_type: Optional[str] = None,
        files: Any = None,
    ) -> Json:
        url = f"{self.api_root}{path}" if path.startswith("/") else f"{self.api_root}/{path}"
        h = self._headers(accept=accept, content_type=content_type)
        if headers:
            h.update(headers)

        try:
            resp = requests.request(
                method=method.upper(),
                url=url,
                params=params,
                json=json_body,
                data=data,
                headers=h,
                timeout=self.timeout,
                files=files,
            )
        except requests.RequestException as e:
            return {"error": str(e)}

        if resp.status_code == 204:
            return {"status": 204}

        content_type_resp = resp.headers.get("Content-Type", "")
        text = resp.text

        if resp.status_code >= 400:
            # Jira often returns JSON error bodies.
            try:
                err = resp.json()
            except Exception:
                err = text
            return {"error": err, "status": resp.status_code}

        if "application/json" in content_type_resp:
            try:
                return resp.json()
            except Exception:
                return {"error": "Failed to parse JSON", "status": resp.status_code, "raw": text}

        return text


def clean_params(params: Optional[Dict[str, Any]]) -> Optional[Dict[str, Any]]:
    if not params:
        return None
    return {k: v for k, v in params.items() if v is not None}


def ensure_list(v: Any) -> list:
    if v is None:
        return []
    if isinstance(v, list):
        return v
    return [v]
