from __future__ import annotations

import base64
import json
import os
from typing import Any, Callable, Dict, Optional
from urllib import error, parse, request

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("jira-cloud-rest-v3")

BASE_URL = os.environ.get("JIRA_BASE_URL", "").rstrip("/") + "/rest/api/3"
EMAIL = os.environ.get("JIRA_EMAIL", "")
API_TOKEN = os.environ.get("JIRA_API_TOKEN", "")


def _auth_header() -> str:
    token = base64.b64encode(f"{EMAIL}:{API_TOKEN}".encode()).decode()
    return f"Basic {token}"


def jira_request(method: str, path: str, query: Optional[Dict[str, Any]] = None, body: Any = None) -> Any:
    url = BASE_URL + path
    if query:
        q = {k: v for k, v in query.items() if v is not None}
        url += "?" + parse.urlencode(q, doseq=True)
    data = None
    headers = {"Accept": "application/json", "Authorization": _auth_header()}
    if body is not None:
        headers["Content-Type"] = "application/json"
        data = json.dumps(body).encode()
    req = request.Request(url, data=data, headers=headers, method=method)
    try:
        with request.urlopen(req) as resp:
            raw = resp.read().decode()
            return json.loads(raw) if raw else None
    except error.HTTPError as e:
        raw = e.read().decode()
        raise RuntimeError(f"Jira API error {e.code}: {raw}") from None


@mcp.tool()
def get_issue(issue_id_or_key: str, fields: Optional[str] = None, expand: Optional[str] = None) -> Any:
    return jira_request("GET", f"/issue/{parse.quote(issue_id_or_key, safe='')}", {"fields": fields, "expand": expand})


@mcp.tool()
def create_issue(fields: Dict[str, Any], update: Optional[Dict[str, Any]] = None, transition: Optional[Dict[str, Any]] = None, properties: Optional[list] = None, historyMetadata: Optional[Dict[str, Any]] = None, updateHistory: Optional[bool] = None) -> Any:
    body = {"fields": fields}
    if update is not None:
        body["update"] = update
    if transition is not None:
        body["transition"] = transition
    if properties is not None:
        body["properties"] = properties
    if historyMetadata is not None:
        body["historyMetadata"] = historyMetadata
    return jira_request("POST", "/issue", {"updateHistory": updateHistory}, body)


@mcp.tool()
def search_issues(jql: str, startAt: Optional[int] = None, maxResults: Optional[int] = None, fields: Optional[str] = None, expand: Optional[str] = None) -> Any:
    return jira_request("GET", "/search", {"jql": jql, "startAt": startAt, "maxResults": maxResults, "fields": fields, "expand": expand})


from generated_tools import issues as _issues  # noqa: F401
from generated_tools import projects as _projects  # noqa: F401


if __name__ == "__main__":
    mcp.run()
