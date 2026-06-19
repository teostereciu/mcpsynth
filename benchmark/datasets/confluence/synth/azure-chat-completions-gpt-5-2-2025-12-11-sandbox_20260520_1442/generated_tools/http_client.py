import os
import base64
from typing import Any, Dict, Optional, Union

import requests


def _env(name: str, default: Optional[str] = None) -> str:
    val = os.getenv(name, default)
    if val is None or val == "":
        raise RuntimeError(f"Missing required environment variable: {name}")
    return val


class ConfluenceClient:
    def __init__(self):
        self.base_url = _env("CONFLUENCE_BASE_URL").rstrip("/")
        email = _env("JIRA_EMAIL")
        token = _env("JIRA_API_TOKEN")
        auth = base64.b64encode(f"{email}:{token}".encode("utf-8")).decode("ascii")
        self._headers = {
            "Authorization": f"Basic {auth}",
            "Accept": "application/json",
        }
        self._session = requests.Session()

    def request(
        self,
        method: str,
        path: str,
        *,
        params: Optional[Dict[str, Any]] = None,
        json: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        data: Any = None,
        files: Any = None,
        accept: Optional[str] = None,
    ) -> Union[Dict[str, Any], str, list]:
        url = f"{self.base_url}{path}"
        h = dict(self._headers)
        if accept:
            h["Accept"] = accept
        if headers:
            h.update(headers)

        try:
            resp = self._session.request(
                method=method,
                url=url,
                params=params,
                json=json,
                data=data,
                files=files,
                headers=h,
                timeout=60,
            )
        except requests.RequestException as e:
            return {"error": str(e), "url": url}

        if resp.status_code >= 400:
            # Try to parse JSON error body.
            try:
                body = resp.json()
            except Exception:
                body = resp.text
            return {
                "error": "Confluence API error",
                "status": resp.status_code,
                "url": url,
                "body": body,
            }

        if resp.status_code == 204:
            return {"ok": True}

        ctype = resp.headers.get("Content-Type", "")
        if "application/json" in ctype:
            try:
                return resp.json()
            except Exception:
                return {"error": "Failed to parse JSON response", "status": resp.status_code, "url": url}
        return resp.text
