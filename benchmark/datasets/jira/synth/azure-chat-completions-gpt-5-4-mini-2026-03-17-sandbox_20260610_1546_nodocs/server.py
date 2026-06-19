import base64
import os
from typing import Any, Dict, Optional

import requests
from fastmcp import FastMCP

mcp = FastMCP("jira-cloud")


def _base_url() -> str:
    base = os.environ.get("JIRA_BASE_URL", "").rstrip("/")
    if not base:
        raise RuntimeError("JIRA_BASE_URL is required")
    return f"{base}/rest/api/3"


def _auth_headers() -> Dict[str, str]:
    email = os.environ.get("JIRA_EMAIL", "")
    token = os.environ.get("JIRA_API_TOKEN", "")
    if not email or not token:
        raise RuntimeError("JIRA_EMAIL and JIRA_API_TOKEN are required")
    basic = base64.b64encode(f"{email}:{token}".encode()).decode()
    return {"Authorization": f"Basic {basic}", "Accept": "application/json", "Content-Type": "application/json"}


def _request(method: str, path: str, *, params: Optional[Dict[str, Any]] = None, json: Any = None) -> Any:
    try:
        resp = requests.request(method, f"{_base_url()}{path}", headers=_auth_headers(), params=params, json=json, timeout=30)
        if resp.status_code >= 400:
            try:
                return {"error": resp.json()}
            except Exception:
                return {"error": resp.text, "status": resp.status_code}
        if resp.status_code == 204 or not resp.text:
            return {"ok": True}
        return resp.json()
    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def get_myself() -> Any:
    return _request("GET", "/myself")


@mcp.tool()
def search_issues(jql: str, max_results: int = 50, start_at: int = 0) -> Any:
    return _request("GET", "/search", params={"jql": jql, "maxResults": max_results, "startAt": start_at})


@mcp.tool()
def get_issue(issue_key: str) -> Any:
    return _request("GET", f"/issue/{issue_key}")


@mcp.tool()
def create_issue(fields: Dict[str, Any]) -> Any:
    return _request("POST", "/issue", json={"fields": fields})


@mcp.tool()
def update_issue(issue_key: str, fields: Dict[str, Any]) -> Any:
    return _request("PUT", f"/issue/{issue_key}", json={"fields": fields})


@mcp.tool()
def delete_issue(issue_key: str) -> Any:
    return _request("DELETE", f"/issue/{issue_key}")


@mcp.tool()
def add_comment(issue_key: str, body: str) -> Any:
    return _request("POST", f"/issue/{issue_key}/comment", json={"body": body})


@mcp.tool()
def list_projects() -> Any:
    return _request("GET", "/project/search")


@mcp.tool()
def get_project(project_id_or_key: str) -> Any:
    return _request("GET", f"/project/{project_id_or_key}")


if __name__ == "__main__":
    mcp.run()
