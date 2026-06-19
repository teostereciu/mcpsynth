import base64
import json
import os
from typing import Any, Dict, Optional

import requests
from fastmcp import FastMCP

mcp = FastMCP("jira-cloud")

BASE_URL = os.environ.get("JIRA_BASE_URL", "").rstrip("/") + "/rest/api/3"
EMAIL = os.environ.get("JIRA_EMAIL", "")
API_TOKEN = os.environ.get("JIRA_API_TOKEN", "")
AUTH = (EMAIL, API_TOKEN)
HEADERS = {"Accept": "application/json", "Content-Type": "application/json"}


def _request(method: str, path: str, *, params: Optional[Dict[str, Any]] = None, json_body: Any = None) -> Any:
    if not BASE_URL.startswith("http"):
        return {"error": "JIRA_BASE_URL is not set"}
    url = f"{BASE_URL}{path}"
    try:
        resp = requests.request(method, url, params=params, json=json_body, headers=HEADERS, auth=AUTH, timeout=30)
        if resp.status_code >= 400:
            try:
                return {"error": resp.json()}
            except Exception:
                return {"error": resp.text}
        if resp.status_code == 204 or not resp.content:
            return {"ok": True}
        return resp.json()
    except requests.RequestException as e:
        return {"error": str(e)}


@mcp.tool()
def get_myself() -> Any:
    return _request("GET", "/myself")


@mcp.tool()
def search_issues(jql: str, max_results: int = 50, start_at: int = 0) -> Any:
    return _request("GET", "/search", params={"jql": jql, "maxResults": max_results, "startAt": start_at})


@mcp.tool()
def get_issue(issue_id_or_key: str, fields: Optional[str] = None) -> Any:
    params = {"fields": fields} if fields else None
    return _request("GET", f"/issue/{issue_id_or_key}", params=params)


@mcp.tool()
def create_issue(fields: Dict[str, Any]) -> Any:
    return _request("POST", "/issue", json_body={"fields": fields})


@mcp.tool()
def update_issue(issue_id_or_key: str, fields: Dict[str, Any]) -> Any:
    return _request("PUT", f"/issue/{issue_id_or_key}", json_body={"fields": fields})


@mcp.tool()
def delete_issue(issue_id_or_key: str) -> Any:
    return _request("DELETE", f"/issue/{issue_id_or_key}")


@mcp.tool()
def add_comment(issue_id_or_key: str, body: str) -> Any:
    return _request("POST", f"/issue/{issue_id_or_key}/comment", json_body={"body": body})


@mcp.tool()
def list_comments(issue_id_or_key: str) -> Any:
    return _request("GET", f"/issue/{issue_id_or_key}/comment")


@mcp.tool()
def add_worklog(issue_id_or_key: str, time_spent: str, comment: Optional[str] = None) -> Any:
    payload = {"timeSpent": time_spent}
    if comment:
        payload["comment"] = comment
    return _request("POST", f"/issue/{issue_id_or_key}/worklog", json_body=payload)


@mcp.tool()
def transition_issue(issue_id_or_key: str, transition_id: str) -> Any:
    return _request("POST", f"/issue/{issue_id_or_key}/transitions", json_body={"transition": {"id": transition_id}})


@mcp.tool()
def assign_issue(issue_id_or_key: str, account_id: str) -> Any:
    return _request("PUT", f"/issue/{issue_id_or_key}/assignee", json_body={"accountId": account_id})


@mcp.tool()
def add_watcher(issue_id_or_key: str, account_id: str) -> Any:
    return _request("POST", f"/issue/{issue_id_or_key}/watchers", json_body=account_id)


@mcp.tool()
def remove_watcher(issue_id_or_key: str, account_id: str) -> Any:
    return _request("DELETE", f"/issue/{issue_id_or_key}/watchers", params={"accountId": account_id})


@mcp.tool()
def list_projects() -> Any:
    return _request("GET", "/project/search")


@mcp.tool()
def get_project(project_id_or_key: str) -> Any:
    return _request("GET", f"/project/{project_id_or_key}")


@mcp.tool()
def list_issue_types() -> Any:
    return _request("GET", "/issuetype")


@mcp.tool()
def list_priorities() -> Any:
    return _request("GET", "/priority")


@mcp.tool()
def list_statuses() -> Any:
    return _request("GET", "/status")


@mcp.tool()
def list_filters() -> Any:
    return _request("GET", "/filter/search")


@mcp.tool()
def get_filter(filter_id: str) -> Any:
    return _request("GET", f"/filter/{filter_id}")


if __name__ == "__main__":
    mcp.run()
