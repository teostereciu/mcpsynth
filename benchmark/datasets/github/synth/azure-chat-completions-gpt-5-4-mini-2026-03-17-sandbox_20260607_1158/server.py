import base64
import os
from typing import Any, Dict, Optional

import requests
from mcp.server.fastmcp import FastMCP

BASE_URL = os.getenv("GITHUB_API_BASE_URL", "https://api.github.com").rstrip("/")
TOKEN = os.getenv("GITHUB_TOKEN")
API_VERSION = "2022-11-28"

mcp = FastMCP("github-rest-api")


def _headers(accept: str = "application/vnd.github+json") -> Dict[str, str]:
    headers = {
        "Accept": accept,
        "X-GitHub-Api-Version": API_VERSION,
    }
    if TOKEN:
        headers["Authorization"] = f"Bearer {TOKEN}"
    return headers


def _request(method: str, path: str, *, params: Optional[dict] = None, json: Any = None, accept: str = "application/vnd.github+json"):
    try:
        resp = requests.request(method, f"{BASE_URL}{path}", headers=_headers(accept), params=params, json=json, timeout=60)
        if resp.status_code >= 400:
            try:
                return {"error": resp.json()}
            except Exception:
                return {"error": resp.text, "status": resp.status_code}
        if resp.status_code == 204:
            return {"ok": True}
        try:
            return resp.json()
        except Exception:
            return resp.text
    except requests.RequestException as e:
        return {"error": str(e)}


@mcp.tool()
def list_repository_issues(owner: str, repo: str, state: str = "open", per_page: int = 30, page: int = 1):
    return _request("GET", f"/repos/{owner}/{repo}/issues", params={"state": state, "per_page": per_page, "page": page})


@mcp.tool()
def create_issue(owner: str, repo: str, title: str, body: Optional[str] = None, assignees: Optional[list] = None, labels: Optional[list] = None, milestone: Optional[int] = None):
    payload = {"title": title}
    for k, v in [("body", body), ("assignees", assignees), ("labels", labels), ("milestone", milestone)]:
        if v is not None:
            payload[k] = v
    return _request("POST", f"/repos/{owner}/{repo}/issues", json=payload)


@mcp.tool()
def get_issue(owner: str, repo: str, issue_number: int):
    return _request("GET", f"/repos/{owner}/{repo}/issues/{issue_number}")


@mcp.tool()
def update_issue(owner: str, repo: str, issue_number: int, title: Optional[str] = None, body: Optional[str] = None, state: Optional[str] = None):
    payload = {k: v for k, v in {"title": title, "body": body, "state": state}.items() if v is not None}
    return _request("PATCH", f"/repos/{owner}/{repo}/issues/{issue_number}", json=payload)


@mcp.tool()
def list_pull_requests(owner: str, repo: str, state: str = "open", per_page: int = 30, page: int = 1):
    return _request("GET", f"/repos/{owner}/{repo}/pulls", params={"state": state, "per_page": per_page, "page": page})


@mcp.tool()
def create_pull_request(owner: str, repo: str, title: str, head: str, base: str, body: Optional[str] = None, draft: Optional[bool] = None):
    payload = {"title": title, "head": head, "base": base}
    for k, v in [("body", body), ("draft", draft)]:
        if v is not None:
            payload[k] = v
    return _request("POST", f"/repos/{owner}/{repo}/pulls", json=payload)


@mcp.tool()
def get_pull_request(owner: str, repo: str, pull_number: int):
    return _request("GET", f"/repos/{owner}/{repo}/pulls/{pull_number}")


@mcp.tool()
def merge_pull_request(owner: str, repo: str, pull_number: int, commit_title: Optional[str] = None, merge_method: Optional[str] = None):
    payload = {k: v for k, v in {"commit_title": commit_title, "merge_method": merge_method}.items() if v is not None}
    return _request("PUT", f"/repos/{owner}/{repo}/pulls/{pull_number}/merge", json=payload)


@mcp.tool()
def list_repository_releases(owner: str, repo: str, per_page: int = 30, page: int = 1):
    return _request("GET", f"/repos/{owner}/{repo}/releases", params={"per_page": per_page, "page": page})


@mcp.tool()
def create_release(owner: str, repo: str, tag_name: str, name: Optional[str] = None, body: Optional[str] = None, draft: Optional[bool] = None, prerelease: Optional[bool] = None):
    payload = {"tag_name": tag_name}
    for k, v in [("name", name), ("body", body), ("draft", draft), ("prerelease", prerelease)]:
        if v is not None:
            payload[k] = v
    return _request("POST", f"/repos/{owner}/{repo}/releases", json=payload)


@mcp.tool()
def search_code(query: str, per_page: int = 30, page: int = 1):
    return _request("GET", "/search/code", params={"q": query, "per_page": per_page, "page": page})


@mcp.tool()
def list_repository_workflows(owner: str, repo: str, per_page: int = 30, page: int = 1):
    return _request("GET", f"/repos/{owner}/{repo}/actions/workflows", params={"per_page": per_page, "page": page})


@mcp.tool()
def list_workflow_runs(owner: str, repo: str, workflow_id: str, per_page: int = 30, page: int = 1):
    return _request("GET", f"/repos/{owner}/{repo}/actions/workflows/{workflow_id}/runs", params={"per_page": per_page, "page": page})


@mcp.tool()
def list_repository_webhooks(owner: str, repo: str):
    return _request("GET", f"/repos/{owner}/{repo}/hooks")


@mcp.tool()
def create_repository_webhook(owner: str, repo: str, config: dict, events: Optional[list] = None, active: bool = True):
    payload = {"config": config, "active": active}
    if events is not None:
        payload["events"] = events
    return _request("POST", f"/repos/{owner}/{repo}/hooks", json=payload)


@mcp.tool()
def get_branch_protection(owner: str, repo: str, branch: str):
    return _request("GET", f"/repos/{owner}/{repo}/branches/{branch}/protection")


grounding = {
    "list_repository_issues": {"doc": "docs/api_issues-issues.md", "endpoint": "GET /repos/{owner}/{repo}/issues"},
    "create_issue": {"doc": "docs/api_issues-issues.md", "endpoint": "POST /repos/{owner}/{repo}/issues"},
    "get_issue": {"doc": "docs/api_issues-issues.md", "endpoint": "GET /repos/{owner}/{repo}/issues/{issue_number}"},
    "update_issue": {"doc": "docs/api_issues-issues.md", "endpoint": "PATCH /repos/{owner}/{repo}/issues/{issue_number}"},
    "list_pull_requests": {"doc": "docs/api_pulls-pulls.md", "endpoint": "GET /repos/{owner}/{repo}/pulls"},
    "create_pull_request": {"doc": "docs/api_pulls-pulls.md", "endpoint": "POST /repos/{owner}/{repo}/pulls"},
    "get_pull_request": {"doc": "docs/api_pulls-pulls.md", "endpoint": "GET /repos/{owner}/{repo}/pulls/{pull_number}"},
    "merge_pull_request": {"doc": "docs/api_pulls-pulls.md", "endpoint": "PUT /repos/{owner}/{repo}/pulls/{pull_number}/merge"},
    "list_repository_releases": {"doc": "docs/api_releases-releases.md", "endpoint": "GET /repos/{owner}/{repo}/releases"},
    "create_release": {"doc": "docs/api_releases-releases.md", "endpoint": "POST /repos/{owner}/{repo}/releases"},
    "search_code": {"doc": "docs/api_search-search.md", "endpoint": "GET /search/code"},
    "list_repository_workflows": {"doc": "docs/api_actions-workflows.md", "endpoint": "GET /repos/{owner}/{repo}/actions/workflows"},
    "list_workflow_runs": {"doc": "docs/api_actions-workflow-runs.md", "endpoint": "GET /repos/{owner}/{repo}/actions/workflows/{workflow_id}/runs"},
    "list_repository_webhooks": {"doc": "docs/api_repos-webhooks.md", "endpoint": "GET /repos/{owner}/{repo}/hooks"},
    "create_repository_webhook": {"doc": "docs/api_repos-webhooks.md", "endpoint": "POST /repos/{owner}/{repo}/hooks"},
    "get_branch_protection": {"doc": "docs/api_branches-branch-protection.md", "endpoint": "GET /repos/{owner}/{repo}/branches/{branch}/protection"},
}


if __name__ == "__main__":
    mcp.run()
