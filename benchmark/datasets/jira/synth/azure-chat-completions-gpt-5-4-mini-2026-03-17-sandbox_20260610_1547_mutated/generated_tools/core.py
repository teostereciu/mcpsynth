import os
import base64
import json
from typing import Any, Dict, Optional
from urllib import request, parse, error

BASE_URL = os.environ.get("JIRA_BASE_URL", "").rstrip("/") + "/rest/api/3"
EMAIL = os.environ.get("JIRA_EMAIL", "")
TOKEN = os.environ.get("JIRA_API_TOKEN", "")


def _auth_header() -> str:
    token = base64.b64encode(f"{EMAIL}:{TOKEN}".encode()).decode()
    return f"Basic {token}"


def jira_request(method: str, path: str, query: Optional[Dict[str, Any]] = None, body: Any = None) -> Any:
    url = BASE_URL + path
    if query:
        qs = parse.urlencode([(k, v) for k, v in query.items() if v is not None], doseq=True)
        if qs:
            url += "?" + qs
    data = None
    headers = {"Accept": "application/json", "Authorization": _auth_header()}
    if body is not None:
        data = json.dumps(body).encode()
        headers["Content-Type"] = "application/json"
    req = request.Request(url, data=data, headers=headers, method=method)
    try:
        with request.urlopen(req) as resp:
            raw = resp.read().decode()
            return json.loads(raw) if raw else {"status": resp.status}
    except error.HTTPError as e:
        raw = e.read().decode()
        raise RuntimeError(f"Jira API error {e.code}: {raw}")
