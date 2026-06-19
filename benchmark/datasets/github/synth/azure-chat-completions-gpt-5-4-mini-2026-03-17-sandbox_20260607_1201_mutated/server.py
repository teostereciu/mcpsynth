import os
import requests
from typing import Any, Dict
from mcp.server.fastmcp import FastMCP

BASE_URL = os.getenv("GITHUB_API_BASE_URL", "https://api.github.com").rstrip("/")
TOKEN = os.getenv("GITHUB_TOKEN", "")
API_VERSION = "2026-03-10"

mcp = FastMCP("github-rest-api")


def _headers() -> Dict[str, str]:
    headers = {"Accept": "application/vnd.github+json", "X-GitHub-Api-Version": API_VERSION}
    if TOKEN:
        headers["Authorization"] = f"Bearer {TOKEN}"
    return headers


def _request(method: str, path: str, *, params: Dict[str, Any] = None, json: Dict[str, Any] = None) -> Any:
    try:
        resp = requests.request(method, f"{BASE_URL}{path}", headers=_headers(), params=params, json=json, timeout=30)
        if resp.status_code >= 400:
            return {"error": f"GitHub API error {resp.status_code}", "details": resp.text}
        if not resp.text:
            return {}
        return resp.json()
    except requests.RequestException as e:
        return {"error": str(e)}


@mcp.tool()
def list_repository_issues(owner: str, repo: str, state: str = "open", per_page: int = 30, page: int = 1):
    return _request("GET", f"/repos/{owner}/{repo}/issues", params={"state": state, "per_page": per_page, "page": page})


@mcp.tool()
def get_issue(owner: str, repo: str, issue_number: int):
    return _request("GET", f"/repos/{owner}/{repo}/issues/{issue_number}")


@mcp.tool()
def create_issue(owner: str, repo: str, title: str, body: str = None, labels=None, assignees=None, milestone=None):
    payload = {"title": title}
    if body is not None:
        payload["body"] = body
    if labels is not None:
        payload["labels"] = labels
    if assignees is not None:
        payload["assignees"] = assignees
    if milestone is not None:
        payload["milestone"] = milestone
    return _request("POST", f"/repos/{owner}/{repo}/issues", json=payload)


@mcp.tool()
def update_issue(owner: str, repo: str, issue_number: int, title: str = None, body: str = None, state: str = None):
    payload = {k: v for k, v in {"title": title, "body": body, "state": state}.items() if v is not None}
    return _request("PATCH", f"/repos/{owner}/{repo}/issues/{issue_number}", json=payload)


@mcp.tool()
def add_issue_comment(owner: str, repo: str, issue_number: int, body: str):
    return _request("POST", f"/repos/{owner}/{repo}/issues/{issue_number}/comments", json={"body": body})


@mcp.tool()
def list_pull_requests(owner: str, repo: str, state: str = "open", per_page: int = 30, page: int = 1):
    return _request("GET", f"/repos/{owner}/{repo}/pulls", params={"state": state, "per_page": per_page, "page": page})


@mcp.tool()
def create_pull_request(owner: str, repo: str, title: str, head: str, base: str, body: str = None, draft: bool = False):
    payload = {"title": title, "head": head, "base": base, "draft": draft}
    if body is not None:
        payload["body"] = body
    return _request("POST", f"/repos/{owner}/{repo}/pulls", json=payload)


@mcp.tool()
def merge_pull_request(owner: str, repo: str, pull_number: int, merge_method: str = "merge"):
    return _request("PUT", f"/repos/{owner}/{repo}/pulls/{pull_number}/merge", json={"merge_method": merge_method})


if __name__ == "__main__":
    mcp.run(transport="stdio")
