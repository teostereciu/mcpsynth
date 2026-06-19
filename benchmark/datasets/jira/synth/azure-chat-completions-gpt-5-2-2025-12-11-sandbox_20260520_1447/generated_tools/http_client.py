import os
import base64
from typing import Any, Dict, Optional, Union

import requests


class JiraClient:
    def __init__(self):
        base = os.environ.get("JIRA_BASE_URL", "").rstrip("/")
        if not base:
            raise RuntimeError("JIRA_BASE_URL is not set")
        self.base_url = f"{base}/rest/api/3"
        email = os.environ.get("JIRA_EMAIL", "")
        token = os.environ.get("JIRA_API_TOKEN", "")
        if not email or not token:
            raise RuntimeError("JIRA_EMAIL/JIRA_API_TOKEN are not set")
        auth = base64.b64encode(f"{email}:{token}".encode("utf-8")).decode("ascii")
        self._headers = {
            "Authorization": f"Basic {auth}",
            "Accept": "application/json",
        }

    def request(
        self,
        method: str,
        path: str,
        *,
        params: Optional[Dict[str, Any]] = None,
        json: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        timeout: int = 60,
    ) -> Union[Dict[str, Any], list, str]:
        url = self.base_url + path
        h = dict(self._headers)
        if headers:
            h.update(headers)
        if json is not None:
            h.setdefault("Content-Type", "application/json")
        try:
            resp = requests.request(method, url, params=params, json=json, headers=h, timeout=timeout)
        except requests.RequestException as e:
            return {"error": str(e)}

        if resp.status_code >= 400:
            try:
                data = resp.json()
            except Exception:
                data = resp.text
            return {"error": f"HTTP {resp.status_code}", "details": data}

        if resp.status_code == 204:
            return {"ok": True}

        ctype = resp.headers.get("Content-Type", "")
        if "application/json" in ctype:
            try:
                return resp.json()
            except Exception:
                return {"error": "Failed to parse JSON", "details": resp.text}
        return resp.text
