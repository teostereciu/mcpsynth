import base64
import json
import os
from typing import Any, Dict, Optional
from urllib import error, parse, request


class JiraClient:
    def __init__(self) -> None:
        base_url = os.environ.get("JIRA_BASE_URL", "").rstrip("/")
        email = os.environ.get("JIRA_EMAIL", "")
        token = os.environ.get("JIRA_API_TOKEN", "")
        if not base_url:
            raise RuntimeError("JIRA_BASE_URL is required")
        if not email or not token:
            raise RuntimeError("JIRA_EMAIL and JIRA_API_TOKEN are required")
        self.base_url = base_url
        auth = base64.b64encode(f"{email}:{token}".encode()).decode()
        self.headers = {
            "Authorization": f"Basic {auth}",
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

    def request(self, method: str, path: str, query: Optional[Dict[str, Any]] = None, body: Any = None, extra_headers: Optional[Dict[str, str]] = None) -> Any:
        url = f"{self.base_url}/rest/api/3{path}"
        if query:
            items = []
            for k, v in query.items():
                if v is None:
                    continue
                if isinstance(v, list):
                    for item in v:
                        items.append((k, str(item)))
                else:
                    items.append((k, str(v)))
            if items:
                url += "?" + parse.urlencode(items)
        data = None if body is None else json.dumps(body).encode()
        headers = dict(self.headers)
        if extra_headers:
            headers.update(extra_headers)
        req = request.Request(url, data=data, headers=headers, method=method)
        try:
            with request.urlopen(req) as resp:
                raw = resp.read()
                if not raw:
                    return None
                ctype = resp.headers.get("Content-Type", "")
                if "application/json" in ctype:
                    return json.loads(raw.decode())
                return raw.decode()
        except error.HTTPError as e:
            raw = e.read()
            detail = raw.decode() if raw else e.reason
            raise RuntimeError(f"Jira API error {e.code}: {detail}") from None
