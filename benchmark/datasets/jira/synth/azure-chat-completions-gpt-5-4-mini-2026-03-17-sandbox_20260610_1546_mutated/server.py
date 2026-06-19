from mcp.server.fastmcp import FastMCP
import os
import base64
import json
import urllib.request
import urllib.error
from typing import Any

mcp = FastMCP("jira-cloud")

BASE_URL = os.environ.get("JIRA_BASE_URL", "").rstrip("/")
EMAIL = os.environ.get("JIRA_EMAIL", "")
API_TOKEN = os.environ.get("JIRA_API_TOKEN", "")


def _auth_header() -> str:
    token = base64.b64encode(f"{EMAIL}:{API_TOKEN}".encode()).decode()
    return f"Basic {token}"


def jira_request(method: str, path: str, params: dict[str, Any] | None = None, body: Any | None = None) -> Any:
    url = f"{BASE_URL}/rest/api/3{path}"
    if params:
        qs = "&".join(f"{urllib.parse.quote(str(k))}={urllib.parse.quote(str(v))}" for k, v in params.items() if v is not None)
        if qs:
            url += "?" + qs
    data = None
    headers = {"Accept": "application/json", "Authorization": _auth_header()}
    if body is not None:
        data = json.dumps(body).encode()
        headers["Content-Type"] = "application/json"
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req) as resp:
            raw = resp.read().decode()
            return json.loads(raw) if raw else None
    except urllib.error.HTTPError as e:
        raw = e.read().decode()
        raise RuntimeError(f"Jira API error {e.code}: {raw}")


@mcp.tool()
def jira_get_issue(issue_id_or_key: str, fields: str | None = None, expand: str | None = None):
    return jira_request("GET", f"/issue/{issue_id_or_key}", {"fields": fields, "expand": expand})


@mcp.tool()
def jira_create_issue(payload: dict[str, Any]):
    return jira_request("POST", "/issue", body=payload)


@mcp.tool()
def jira_update_issue(issue_id_or_key: str, payload: dict[str, Any]):
    return jira_request("PUT", f"/issue/{issue_id_or_key}", body=payload)


@mcp.tool()
def jira_delete_issue(issue_id_or_key: str):
    return jira_request("DELETE", f"/issue/{issue_id_or_key}")


@mcp.tool()
def jira_search_issues(jql: str, start_at: int = 0, max_results: int = 50, fields: str | None = None):
    return jira_request("GET", "/search", {"jql": jql, "startAt": start_at, "maxResults": max_results, "fields": fields})


if __name__ == "__main__":
    mcp.run()
