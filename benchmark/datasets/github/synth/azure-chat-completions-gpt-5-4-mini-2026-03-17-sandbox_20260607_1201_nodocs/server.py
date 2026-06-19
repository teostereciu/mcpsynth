import os
from typing import Any, Dict, Optional

import requests
from fastmcp import FastMCP

mcp = FastMCP("github-rest-api")
BASE_URL = os.getenv("GITHUB_API_BASE_URL", "https://api.github.com").rstrip("/")
TOKEN = os.getenv("GITHUB_TOKEN", "")
TEST_REPO = os.getenv("GITHUB_TEST_REPO", "")
HEADERS = {
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28",
}
if TOKEN:
    HEADERS["Authorization"] = f"Bearer {TOKEN}"


def _request(method: str, path: str, *, params: Optional[dict] = None, json: Any = None) -> Dict[str, Any]:
    try:
        resp = requests.request(method, f"{BASE_URL}{path}", headers=HEADERS, params=params, json=json, timeout=30)
        if resp.status_code >= 400:
            try:
                return {"error": resp.json()}
            except Exception:
                return {"error": resp.text}
        if resp.status_code == 204:
            return {"ok": True}
        try:
            return resp.json()
        except Exception:
            return {"text": resp.text}
    except requests.RequestException as e:
        return {"error": str(e)}


@mcp.tool()
def get_user() -> Dict[str, Any]:
    return _request("GET", "/user")


@mcp.tool()
def list_repositories(per_page: int = 30, page: int = 1) -> Dict[str, Any]:
    return _request("GET", "/user/repos", params={"per_page": per_page, "page": page})


@mcp.tool()
def get_repository(owner: str, repo: str) -> Dict[str, Any]:
    return _request("GET", f"/repos/{owner}/{repo}")


@mcp.tool()
def create_issue(owner: str, repo: str, title: str, body: Optional[str] = None, labels: Optional[list] = None, assignees: Optional[list] = None) -> Dict[str, Any]:
    payload: Dict[str, Any] = {"title": title}
    if body is not None:
        payload["body"] = body
    if labels is not None:
        payload["labels"] = labels
    if assignees is not None:
        payload["assignees"] = assignees
    return _request("POST", f"/repos/{owner}/{repo}/issues", json=payload)


@mcp.tool()
def get_issue(owner: str, repo: str, issue_number: int) -> Dict[str, Any]:
    return _request("GET", f"/repos/{owner}/{repo}/issues/{issue_number}")


@mcp.tool()
def update_issue(owner: str, repo: str, issue_number: int, title: Optional[str] = None, body: Optional[str] = None, state: Optional[str] = None) -> Dict[str, Any]:
    payload: Dict[str, Any] = {}
    if title is not None:
        payload["title"] = title
    if body is not None:
        payload["body"] = body
    if state is not None:
        payload["state"] = state
    return _request("PATCH", f"/repos/{owner}/{repo}/issues/{issue_number}", json=payload)


@mcp.tool()
def list_issue_comments(owner: str, repo: str, issue_number: int) -> Dict[str, Any]:
    return _request("GET", f"/repos/{owner}/{repo}/issues/{issue_number}/comments")


@mcp.tool()
def create_issue_comment(owner: str, repo: str, issue_number: int, body: str) -> Dict[str, Any]:
    return _request("POST", f"/repos/{owner}/{repo}/issues/{issue_number}/comments", json={"body": body})


@mcp.tool()
def create_pull_request(owner: str, repo: str, title: str, head: str, base: str, body: Optional[str] = None) -> Dict[str, Any]:
    payload: Dict[str, Any] = {"title": title, "head": head, "base": base}
    if body is not None:
        payload["body"] = body
    return _request("POST", f"/repos/{owner}/{repo}/pulls", json=payload)


@mcp.tool()
def get_pull_request(owner: str, repo: str, pull_number: int) -> Dict[str, Any]:
    return _request("GET", f"/repos/{owner}/{repo}/pulls/{pull_number}")


@mcp.tool()
def merge_pull_request(owner: str, repo: str, pull_number: int, commit_title: Optional[str] = None, merge_method: Optional[str] = None) -> Dict[str, Any]:
    payload: Dict[str, Any] = {}
    if commit_title is not None:
        payload["commit_title"] = commit_title
    if merge_method is not None:
        payload["merge_method"] = merge_method
    return _request("PUT", f"/repos/{owner}/{repo}/pulls/{pull_number}/merge", json=payload)


@mcp.tool()
def list_workflows(owner: str, repo: str) -> Dict[str, Any]:
    return _request("GET", f"/repos/{owner}/{repo}/actions/workflows")


@mcp.tool()
def list_workflow_runs(owner: str, repo: str, workflow_id: str) -> Dict[str, Any]:
    return _request("GET", f"/repos/{owner}/{repo}/actions/workflows/{workflow_id}/runs")


@mcp.tool()
def search_code(query: str, per_page: int = 30, page: int = 1) -> Dict[str, Any]:
    return _request("GET", "/search/code", params={"q": query, "per_page": per_page, "page": page})


@mcp.tool()
def list_branches(owner: str, repo: str) -> Dict[str, Any]:
    return _request("GET", f"/repos/{owner}/{repo}/branches")


@mcp.tool()
def get_branch_protection(owner: str, repo: str, branch: str) -> Dict[str, Any]:
    return _request("GET", f"/repos/{owner}/{repo}/branches/{branch}/protection")


@mcp.tool()
def create_release(owner: str, repo: str, tag_name: str, name: Optional[str] = None, body: Optional[str] = None, draft: bool = False, prerelease: bool = False) -> Dict[str, Any]:
    payload: Dict[str, Any] = {"tag_name": tag_name, "draft": draft, "prerelease": prerelease}
    if name is not None:
        payload["name"] = name
    if body is not None:
        payload["body"] = body
    return _request("POST", f"/repos/{owner}/{repo}/releases", json=payload)


if __name__ == "__main__":
    mcp.run()
