import base64
import json
import os
from typing import Any, Dict, Optional, Tuple

import requests


class ConfluenceClient:
    def __init__(
        self,
        base_url: Optional[str] = None,
        email: Optional[str] = None,
        api_token: Optional[str] = None,
        timeout: int = 30,
    ):
        self.base_url = (base_url or os.environ.get("CONFLUENCE_BASE_URL") or "").rstrip("/")
        self.email = email or os.environ.get("JIRA_EMAIL")
        self.api_token = api_token or os.environ.get("JIRA_API_TOKEN")
        self.timeout = timeout

        if not self.base_url:
            raise ValueError("CONFLUENCE_BASE_URL is required (include /wiki)")
        if not self.email or not self.api_token:
            raise ValueError("JIRA_EMAIL and JIRA_API_TOKEN are required")

    def _auth_header(self) -> str:
        token = f"{self.email}:{self.api_token}".encode("utf-8")
        return "Basic " + base64.b64encode(token).decode("ascii")

    def request(
        self,
        method: str,
        path: str,
        *,
        params: Optional[Dict[str, Any]] = None,
        json_body: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        files: Any = None,
        data: Any = None,
        accept: str = "application/json",
    ) -> Tuple[int, Any, Dict[str, str]]:
        url = self.base_url + path
        h = {
            "Authorization": self._auth_header(),
            "Accept": accept,
        }
        if headers:
            h.update(headers)

        try:
            resp = requests.request(
                method,
                url,
                params=params,
                json=json_body,
                headers=h,
                files=files,
                data=data,
                timeout=self.timeout,
            )
        except requests.RequestException as e:
            return 0, {"error": str(e)}, {}

        content_type = resp.headers.get("Content-Type", "")
        if accept != "application/json" and not content_type.startswith("application/json"):
            # caller asked for non-json; return text
            return resp.status_code, resp.text, dict(resp.headers)

        if resp.status_code == 204:
            return resp.status_code, None, dict(resp.headers)

        try:
            return resp.status_code, resp.json(), dict(resp.headers)
        except ValueError:
            # not json
            return resp.status_code, {"raw": resp.text}, dict(resp.headers)


def ok_or_error(status: int, body: Any, headers: Dict[str, str]) -> Any:
    if status and 200 <= status < 300:
        return {"status": status, "data": body, "headers": headers}
    if status == 0:
        return body
    # Confluence often returns {"message":..., "statusCode":...}
    return {"error": "request failed", "status": status, "data": body, "headers": headers}
