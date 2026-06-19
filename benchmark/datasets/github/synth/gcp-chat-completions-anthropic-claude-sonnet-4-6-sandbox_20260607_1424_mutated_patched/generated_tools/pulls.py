"""GitHub Pull Requests tools."""
import os
import requests
from mcp.server.fastmcp import FastMCP

BASE_URL = os.environ.get("GITHUB_API_BASE_URL", "https://api.github.com")
TOKEN = os.environ.get("GITHUB_TOKEN", "")

def _headers():
    h = {"Accept": "application/vnd.github+json", "X-GitHub-Api-Version": "2022-11-28"}
    if TOKEN:
        h["Authorization"] = f"Bearer {TOKEN}"
    return h

def _get(path, params=None):
    try:
        r = requests.get(f"{BASE_URL}{path}", headers=_headers(), params=params, timeout=30)
        if r.status_code == 204:
            return {"status": "no_content"}
        return r.json()
    except Exception as e:
        return {"error": str(e)}

def _post(path, json=None):
    try:
        r = requests.post(f"{BASE_URL}{path}", headers=_headers(), json=json, timeout=30)
        if r.status_code == 204:
            return {"status": "no_content"}
        return r.json()
    except Exception as e:
        return {"error": str(e)}

def _patch(path, json=None):
    try:
        r = requests.patch(f"{BASE_URL}{path}", headers=_headers(), json=json, timeout=30)
        if r.status_code == 204:
            return {"status": "no_content"}
        return r.json()
    except Exception as e:
        return {"error": str(e)}

def _put(path, json=None):
    try:
        r = requests.put(f"{BASE_URL}{path}", headers=_headers(), json=json, timeout=30)
        if r.status_code == 204:
            return {"status": "no_content"}
        return r.json()
    except Exception as e:
        return {"error": str(e)}

def _delete(path, json=None):
    try:
        r = requests.delete(f"{BASE_URL}{path}", headers=_headers(), json=json, timeout=30)
        if r.status_code == 204:
            return {"status": "no_content"}
        return r.json()
    except Exception as e:
        return {"error": str(e)}


def register_pulls_tools(mcp: FastMCP):

    @mcp.tool()
    def list_pull_requests(owner: str, repo: str, state: str = "open",
                           head: str = "", base: str = "", sort: str = "created",
                           direction: str = "desc", per_page: int = 30, page: int = 1) -> dict:
        """List pull requests in a repository. state: open|closed|all."""
        params = {"state": state, "sort": sort, "direction": direction,
                  "per_page": per_page, "page": page}
        if head:
            params["head"] = head
        if base:
            params["base"] = base
        return _get(f"/repos/{owner}/{repo}/pulls", params)

    @mcp.tool()
    def get_pull_request(owner: str, repo: str, pull_number: int) -> dict:
        """Get a single pull request by number."""
        return _get(f"/repos/{owner}/{repo}/pulls/{pull_number}")

    @mcp.tool()
    def create_pull_request(owner: str, repo: str, title: str, head: str, base: str,
                            body: str = "", draft: bool = False,
                            maintainer_can_modify: bool = True) -> dict:
        """Create a pull request. head is the branch with changes, base is the target branch."""
        payload = {"title": title, "head": head, "base": base,
                   "draft": draft, "maintainer_can_modify": maintainer_can_modify}
        if body:
            payload["body"] = body
        return _post(f"/repos/{owner}/{repo}/pulls", payload)

    @mcp.tool()
    def update_pull_request(owner: str, repo: str, pull_number: int,
                            title: str = None, body: str = None, state: str = None,
                            base: str = None, maintainer_can_modify: bool = None) -> dict:
        """Update a pull request. state: open|closed."""
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
    def list_pr_commits(owner: str, repo: str, pull_number: int,
                        per_page: int = 30, page: int = 1) -> dict:
        """List commits on a pull request."""
        return _get(f"/repos/{owner}/{repo}/pulls/{pull_number}/commits",
                    {"per_page": per_page, "page": page})

    @mcp.tool()
    def list_pr_files(owner: str, repo: str, pull_number: int,
                      per_page: int = 30, page: int = 1) -> dict:
        """List files changed in a pull request."""
        return _get(f"/repos/{owner}/{repo}/pulls/{pull_number}/files",
                    {"per_page": per_page, "page": page})

    @mcp.tool()
    def check_pr_merged(owner: str, repo: str, pull_number: int) -> dict:
        """Check if a pull request has been merged."""
        try:
            r = requests.get(f"{BASE_URL}/repos/{owner}/{repo}/pulls/{pull_number}/merge",
                             headers=_headers(), timeout=30)
            if r.status_code == 204:
                return {"merged": True}
            elif r.status_code == 404:
                return {"merged": False}
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def merge_pull_request(owner: str, repo: str, pull_number: int,
                           commit_title: str = "", commit_message: str = "",
                           merge_method: str = "merge", sha: str = "") -> dict:
        """Merge a pull request. merge_method: merge|squash|rebase."""
        payload = {"merge_method": merge_method}
        if commit_title:
            payload["commit_title"] = commit_title
        if commit_message:
            payload["commit_message"] = commit_message
        if sha:
            payload["sha"] = sha
        return _put(f"/repos/{owner}/{repo}/pulls/{pull_number}/merge", payload)

    @mcp.tool()
    def update_pr_branch(owner: str, repo: str, pull_number: int,
                         expected_head_sha: str = "") -> dict:
        """Update a pull request branch with the latest upstream changes."""
        payload = {}
        if expected_head_sha:
            payload["expected_head_sha"] = expected_head_sha
        return _put(f"/repos/{owner}/{repo}/pulls/{pull_number}/update-branch", payload)

    @mcp.tool()
    def list_pr_reviews(owner: str, repo: str, pull_number: int,
                        per_page: int = 30, page: int = 1) -> dict:
        """List reviews for a pull request."""
        return _get(f"/repos/{owner}/{repo}/pulls/{pull_number}/reviews",
                    {"per_page": per_page, "page": page})

    @mcp.tool()
    def get_pr_review(owner: str, repo: str, pull_number: int, review_id: int) -> dict:
        """Get a specific review for a pull request."""
        return _get(f"/repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id}")

    @mcp.tool()
    def create_pr_review(owner: str, repo: str, pull_number: int,
                         event: str = "COMMENT", body: str = "",
                         commit_id: str = "", comments: list = None) -> dict:
        """Create a review for a pull request. event: APPROVE|REQUEST_CHANGES|COMMENT."""
        payload = {"event": event}
        if body:
            payload["body"] = body
        if commit_id:
            payload["commit_id"] = commit_id
        if comments:
            payload["comments"] = comments
        return _post(f"/repos/{owner}/{repo}/pulls/{pull_number}/reviews", payload)

    @mcp.tool()
    def submit_pr_review(owner: str, repo: str, pull_number: int, review_id: int,
                         event: str, body: str = "") -> dict:
        """Submit a pending pull request review. event: APPROVE|REQUEST_CHANGES|COMMENT."""
        payload = {"event": event}
        if body:
            payload["body"] = body
        return _post(f"/repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id}/events", payload)

    @mcp.tool()
    def dismiss_pr_review(owner: str, repo: str, pull_number: int, review_id: int,
                          message: str) -> dict:
        """Dismiss a pull request review."""
        return _put(f"/repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id}/dismissals",
                    {"message": message})

    @mcp.tool()
    def get_pr_requested_reviewers(owner: str, repo: str, pull_number: int) -> dict:
        """Get all requested reviewers for a pull request."""
        return _get(f"/repos/{owner}/{repo}/pulls/{pull_number}/requested_reviewers")

    @mcp.tool()
    def request_pr_reviewers(owner: str, repo: str, pull_number: int,
                             reviewers: list = None, team_reviewers: list = None) -> dict:
        """Request reviewers for a pull request."""
        payload = {}
        if reviewers:
            payload["reviewers"] = reviewers
        if team_reviewers:
            payload["team_reviewers"] = team_reviewers
        return _post(f"/repos/{owner}/{repo}/pulls/{pull_number}/requested_reviewers", payload)

    @mcp.tool()
    def remove_pr_requested_reviewers(owner: str, repo: str, pull_number: int,
                                      reviewers: list = None, team_reviewers: list = None) -> dict:
        """Remove requested reviewers from a pull request."""
        payload = {}
        if reviewers:
            payload["reviewers"] = reviewers
        if team_reviewers:
            payload["team_reviewers"] = team_reviewers
        return _delete(f"/repos/{owner}/{repo}/pulls/{pull_number}/requested_reviewers", payload)

    @mcp.tool()
    def list_pr_review_comments(owner: str, repo: str, pull_number: int,
                                per_page: int = 30, page: int = 1) -> dict:
        """List review comments on a pull request."""
        return _get(f"/repos/{owner}/{repo}/pulls/{pull_number}/comments",
                    {"per_page": per_page, "page": page})

    @mcp.tool()
    def get_pr_review_comment(owner: str, repo: str, comment_id: int) -> dict:
        """Get a review comment for a pull request."""
        return _get(f"/repos/{owner}/{repo}/pulls/comments/{comment_id}")

    @mcp.tool()
    def create_pr_review_comment(owner: str, repo: str, pull_number: int,
                                 body: str, commit_id: str, path: str,
                                 position: int = None, line: int = None,
                                 side: str = "RIGHT") -> dict:
        """Create a review comment on a pull request diff."""
        payload = {"body": body, "commit_id": commit_id, "path": path, "side": side}
        if position is not None:
            payload["position"] = position
        if line is not None:
            payload["line"] = line
        return _post(f"/repos/{owner}/{repo}/pulls/{pull_number}/comments", payload)

    @mcp.tool()
    def update_pr_review_comment(owner: str, repo: str, comment_id: int, body: str) -> dict:
        """Update a review comment on a pull request."""
        return _patch(f"/repos/{owner}/{repo}/pulls/comments/{comment_id}", {"body": body})

    @mcp.tool()
    def delete_pr_review_comment(owner: str, repo: str, comment_id: int) -> dict:
        """Delete a review comment on a pull request."""
        return _delete(f"/repos/{owner}/{repo}/pulls/comments/{comment_id}")
