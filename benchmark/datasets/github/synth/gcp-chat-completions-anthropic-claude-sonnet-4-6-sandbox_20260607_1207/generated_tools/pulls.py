"""GitHub Pull Requests, Reviews, and Review Requests tools."""
import os
import requests
from mcp.server.fastmcp import FastMCP

BASE_URL = os.environ.get("GITHUB_API_BASE_URL", "https://api.github.com")
TOKEN = os.environ.get("GITHUB_TOKEN", "")

HEADERS = {
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28",
}
if TOKEN:
    HEADERS["Authorization"] = f"Bearer {TOKEN}"


def _get(path, params=None):
    try:
        r = requests.get(f"{BASE_URL}{path}", headers=HEADERS, params=params, timeout=30)
        if r.status_code == 204:
            return {"status": "no_content"}
        return r.json()
    except Exception as e:
        return {"error": str(e)}


def _post(path, json=None):
    try:
        r = requests.post(f"{BASE_URL}{path}", headers=HEADERS, json=json, timeout=30)
        if r.status_code == 204:
            return {"status": "no_content"}
        return r.json()
    except Exception as e:
        return {"error": str(e)}


def _patch(path, json=None):
    try:
        r = requests.patch(f"{BASE_URL}{path}", headers=HEADERS, json=json, timeout=30)
        return r.json()
    except Exception as e:
        return {"error": str(e)}


def _put(path, json=None):
    try:
        r = requests.put(f"{BASE_URL}{path}", headers=HEADERS, json=json, timeout=30)
        if r.status_code == 204:
            return {"status": "no_content"}
        return r.json()
    except Exception as e:
        return {"error": str(e)}


def _delete(path, json=None):
    try:
        r = requests.delete(f"{BASE_URL}{path}", headers=HEADERS, json=json, timeout=30)
        if r.status_code == 204:
            return {"status": "no_content"}
        return r.json()
    except Exception as e:
        return {"error": str(e)}


def register_pulls_tools(mcp: FastMCP):

    @mcp.tool()
    def list_pull_requests(owner: str, repo: str, state: str = "open", head: str = None,
                           base: str = None, sort: str = "created", direction: str = "desc",
                           per_page: int = 30, page: int = 1) -> dict:
        """List pull requests in a repository."""
        params = {"state": state, "sort": sort, "direction": direction,
                  "per_page": per_page, "page": page}
        if head:
            params["head"] = head
        if base:
            params["base"] = base
        return _get(f"/repos/{owner}/{repo}/pulls", params)

    @mcp.tool()
    def create_pull_request(owner: str, repo: str, title: str, head: str, base: str,
                            body: str = None, draft: bool = False,
                            maintainer_can_modify: bool = True) -> dict:
        """Create a pull request."""
        payload = {"title": title, "head": head, "base": base,
                   "draft": draft, "maintainer_can_modify": maintainer_can_modify}
        if body:
            payload["body"] = body
        return _post(f"/repos/{owner}/{repo}/pulls", payload)

    @mcp.tool()
    def get_pull_request(owner: str, repo: str, pull_number: int) -> dict:
        """Get a specific pull request by number."""
        return _get(f"/repos/{owner}/{repo}/pulls/{pull_number}")

    @mcp.tool()
    def update_pull_request(owner: str, repo: str, pull_number: int, title: str = None,
                            body: str = None, state: str = None, base: str = None,
                            maintainer_can_modify: bool = None) -> dict:
        """Update a pull request (title, body, state, base branch)."""
        payload = {}
        if title is not None:
            payload["title"] = title
        if body is not None:
            payload["body"] = body
        if state is not None:
            payload["state"] = state
        if base is not None:
            payload["base"] = base
        if maintainer_can_modify is not None:
            payload["maintainer_can_modify"] = maintainer_can_modify
        return _patch(f"/repos/{owner}/{repo}/pulls/{pull_number}", payload)

    @mcp.tool()
    def list_pull_request_commits(owner: str, repo: str, pull_number: int,
                                  per_page: int = 30, page: int = 1) -> dict:
        """List commits on a pull request."""
        return _get(f"/repos/{owner}/{repo}/pulls/{pull_number}/commits",
                    {"per_page": per_page, "page": page})

    @mcp.tool()
    def list_pull_request_files(owner: str, repo: str, pull_number: int,
                                per_page: int = 30, page: int = 1) -> dict:
        """List files changed in a pull request."""
        return _get(f"/repos/{owner}/{repo}/pulls/{pull_number}/files",
                    {"per_page": per_page, "page": page})

    @mcp.tool()
    def check_pull_request_merged(owner: str, repo: str, pull_number: int) -> dict:
        """Check if a pull request has been merged."""
        try:
            r = requests.get(f"{BASE_URL}/repos/{owner}/{repo}/pulls/{pull_number}/merge",
                             headers=HEADERS, timeout=30)
            return {"merged": r.status_code == 204}
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def merge_pull_request(owner: str, repo: str, pull_number: int,
                           commit_title: str = None, commit_message: str = None,
                           merge_method: str = "merge", sha: str = None) -> dict:
        """Merge a pull request. merge_method: merge, squash, or rebase."""
        payload = {"merge_method": merge_method}
        if commit_title:
            payload["commit_title"] = commit_title
        if commit_message:
            payload["commit_message"] = commit_message
        if sha:
            payload["sha"] = sha
        return _put(f"/repos/{owner}/{repo}/pulls/{pull_number}/merge", payload)

    @mcp.tool()
    def update_pull_request_branch(owner: str, repo: str, pull_number: int,
                                   expected_head_sha: str = None) -> dict:
        """Update a pull request branch with the latest upstream changes."""
        payload = {}
        if expected_head_sha:
            payload["expected_head_sha"] = expected_head_sha
        return _put(f"/repos/{owner}/{repo}/pulls/{pull_number}/update-branch", payload or None)

    # --- Reviews ---

    @mcp.tool()
    def list_pull_request_reviews(owner: str, repo: str, pull_number: int,
                                  per_page: int = 30, page: int = 1) -> dict:
        """List reviews for a pull request."""
        return _get(f"/repos/{owner}/{repo}/pulls/{pull_number}/reviews",
                    {"per_page": per_page, "page": page})

    @mcp.tool()
    def create_pull_request_review(owner: str, repo: str, pull_number: int,
                                   event: str = None, body: str = None,
                                   commit_id: str = None, comments: list = None) -> dict:
        """Create a review for a pull request. event: APPROVE, REQUEST_CHANGES, COMMENT."""
        payload = {}
        if event:
            payload["event"] = event
        if body:
            payload["body"] = body
        if commit_id:
            payload["commit_id"] = commit_id
        if comments:
            payload["comments"] = comments
        return _post(f"/repos/{owner}/{repo}/pulls/{pull_number}/reviews", payload)

    @mcp.tool()
    def get_pull_request_review(owner: str, repo: str, pull_number: int,
                                review_id: int) -> dict:
        """Get a specific review for a pull request."""
        return _get(f"/repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id}")

    @mcp.tool()
    def submit_pull_request_review(owner: str, repo: str, pull_number: int,
                                   review_id: int, event: str, body: str = None) -> dict:
        """Submit a pending pull request review. event: APPROVE, REQUEST_CHANGES, COMMENT."""
        payload = {"event": event}
        if body:
            payload["body"] = body
        return _post(f"/repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id}/events",
                     payload)

    @mcp.tool()
    def dismiss_pull_request_review(owner: str, repo: str, pull_number: int,
                                    review_id: int, message: str) -> dict:
        """Dismiss a pull request review."""
        return _put(f"/repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id}/dismissals",
                    {"message": message})

    # --- Review Requests ---

    @mcp.tool()
    def list_review_requests(owner: str, repo: str, pull_number: int,
                             per_page: int = 30, page: int = 1) -> dict:
        """List requested reviewers for a pull request."""
        return _get(f"/repos/{owner}/{repo}/pulls/{pull_number}/requested_reviewers",
                    {"per_page": per_page, "page": page})

    @mcp.tool()
    def request_reviewers(owner: str, repo: str, pull_number: int,
                          reviewers: list = None, team_reviewers: list = None) -> dict:
        """Request reviewers for a pull request."""
        payload = {}
        if reviewers:
            payload["reviewers"] = reviewers
        if team_reviewers:
            payload["team_reviewers"] = team_reviewers
        return _post(f"/repos/{owner}/{repo}/pulls/{pull_number}/requested_reviewers", payload)

    @mcp.tool()
    def remove_review_requests(owner: str, repo: str, pull_number: int,
                               reviewers: list = None, team_reviewers: list = None) -> dict:
        """Remove requested reviewers from a pull request."""
        payload = {}
        if reviewers:
            payload["reviewers"] = reviewers
        if team_reviewers:
            payload["team_reviewers"] = team_reviewers
        return _delete(f"/repos/{owner}/{repo}/pulls/{pull_number}/requested_reviewers", payload)

    # --- PR Comments ---

    @mcp.tool()
    def list_pull_request_review_comments(owner: str, repo: str, pull_number: int,
                                          sort: str = "created", direction: str = "asc",
                                          per_page: int = 30, page: int = 1) -> dict:
        """List review comments on a pull request."""
        return _get(f"/repos/{owner}/{repo}/pulls/{pull_number}/comments",
                    {"sort": sort, "direction": direction, "per_page": per_page, "page": page})

    @mcp.tool()
    def create_pull_request_review_comment(owner: str, repo: str, pull_number: int,
                                           body: str, commit_id: str, path: str,
                                           line: int = None, side: str = None,
                                           position: int = None) -> dict:
        """Create a review comment on a pull request diff."""
        payload = {"body": body, "commit_id": commit_id, "path": path}
        if line is not None:
            payload["line"] = line
        if side:
            payload["side"] = side
        if position is not None:
            payload["position"] = position
        return _post(f"/repos/{owner}/{repo}/pulls/{pull_number}/comments", payload)
