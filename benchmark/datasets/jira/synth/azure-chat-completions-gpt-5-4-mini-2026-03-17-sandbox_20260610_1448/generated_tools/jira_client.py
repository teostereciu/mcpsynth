import base64
import json
import os
from typing import Any, Dict, Optional
from urllib import request, parse, error


class JiraClient:
    def __init__(self) -> None:
        base_url = os.environ.get("JIRA_BASE_URL", "").rstrip("/")
        if not base_url:
            raise RuntimeError("JIRA_BASE_URL is required")
        self.base_url = base_url + "/rest/api/3"
        email = os.environ.get("JIRA_EMAIL", "")
        token = os.environ.get("JIRA_API_TOKEN", "")
        if not email or not token:
            raise RuntimeError("JIRA_EMAIL and JIRA_API_TOKEN are required")
        auth = base64.b64encode(f"{email}:{token}".encode()).decode()
        self.headers = {
            "Authorization": f"Basic {auth}",
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

    def request(self, method: str, path: str, params: Optional[Dict[str, Any]] = None, body: Any = None) -> Any:
        url = self.base_url + path
        if params:
            qs = parse.urlencode([(k, v) for k, v in params.items() if v is not None], doseq=True)
            if qs:
                url += "?" + qs
        data = None if body is None else json.dumps(body).encode()
        req = request.Request(url, data=data, headers=self.headers, method=method)
        try:
            with request.urlopen(req) as resp:
                raw = resp.read().decode()
                return json.loads(raw) if raw else None
        except error.HTTPError as e:
            raw = e.read().decode()
            raise RuntimeError(f"Jira API error {e.code}: {raw}") from None
