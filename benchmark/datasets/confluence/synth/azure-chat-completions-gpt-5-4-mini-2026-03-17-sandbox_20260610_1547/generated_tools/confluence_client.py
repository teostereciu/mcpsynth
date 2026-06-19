from __future__ import annotations

import base64
import json
import os
from dataclasses import dataclass
from typing import Any, Dict, Optional
from urllib.parse import urlencode, urljoin

import httpx


@dataclass
class ConfluenceClient:
    base_url: str
    email: Optional[str] = None
    api_token: Optional[str] = None
    timeout: float = 60.0

    def _headers(self) -> Dict[str, str]:
        headers = {"Accept": "application/json"}
        if self.email and self.api_token:
            token = base64.b64encode(f"{self.email}:{self.api_token}".encode()).decode()
            headers["Authorization"] = f"Basic {token}"
        return headers

    def request(self, method: str, path: str, *, params: Optional[Dict[str, Any]] = None, json_body: Any = None, stream: bool = False) -> Any:
        url = urljoin(self.base_url.rstrip("/") + "/", path.lstrip("/"))
        if params:
            url = f"{url}?{urlencode([(k, v) for k, v in params.items() if v is not None], doseq=True)}"
        with httpx.Client(timeout=self.timeout) as client:
            resp = client.request(method, url, headers=self._headers(), json=json_body)
            if resp.status_code == 204:
                return {"status_code": 204}
            try:
                data = resp.json()
            except Exception:
                data = {"text": resp.text}
            return {"status_code": resp.status_code, "headers": dict(resp.headers), "data": data}


def get_client() -> ConfluenceClient:
    return ConfluenceClient(
        base_url=os.environ["CONFLUENCE_BASE_URL"],
        email=os.getenv("JIRA_EMAIL"),
        api_token=os.getenv("JIRA_API_TOKEN"),
    )
