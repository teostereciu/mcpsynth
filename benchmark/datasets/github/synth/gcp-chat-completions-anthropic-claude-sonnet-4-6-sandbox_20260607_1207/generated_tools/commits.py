"""GitHub Commits and Commit Statuses tools."""
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


def register_commits_tools(mcp: FastMCP):

    @mcp.tool()
    def list_commits(owner: str, repo: str, sha: str = None, path: str = None,
                     author: str = None, committer: str = None,
                     since: str = None, until: str = None,
                     per_page: int = 30, page: int = 1) -> dict:
        """List commits for a repository. Filter by branch/SHA, file path, author, or date range."""
        params = {"per_page": per_page, "page": page}
        if sha:
            params["sha"] = sha
        if path:
            params["path"] = path
        if author:
            params["author"] = author
        if committer:
            params["committer"] = committer
        if since:
            params["since"] = since
        if until:
            params["until"] = until
        return _get(f"/repos/{owner}/{repo}/commits", params)

    @mcp.tool()
    def get_commit(owner: str, repo: str, ref: str) -> dict:
        """Get a specific commit by SHA, branch, or tag."""
        return _get(f"/repos/{owner}/{repo}/commits/{ref}")

    @mcp.tool()
    def compare_commits(owner: str, repo: str, base: str, head: str,
                        per_page: int = 30, page: int = 1) -> dict:
        """Compare two commits, branches, or tags."""
        return _get(f"/repos/{owner}/{repo}/compare/{base}...{head}",
                    {"per_page": per_page, "page": page})

    @mcp.tool()
    def list_branches_for_head_commit(owner: str, repo: str, commit_sha: str) -> dict:
        """List branches where the given commit SHA is the HEAD."""
        return _get(f"/repos/{owner}/{repo}/commits/{commit_sha}/branches-where-head")

    @mcp.tool()
    def list_pull_requests_for_commit(owner: str, repo: str, commit_sha: str,
                                      per_page: int = 30, page: int = 1) -> dict:
        """List pull requests associated with a commit."""
        return _get(f"/repos/{owner}/{repo}/commits/{commit_sha}/pulls",
                    {"per_page": per_page, "page": page})

    @mcp.tool()
    def list_commit_comments(owner: str, repo: str, commit_sha: str,
                             per_page: int = 30, page: int = 1) -> dict:
        """List comments for a specific commit."""
        return _get(f"/repos/{owner}/{repo}/commits/{commit_sha}/comments",
                    {"per_page": per_page, "page": page})

    @mcp.tool()
    def create_commit_comment(owner: str, repo: str, commit_sha: str, body: str,
                              path: str = None, position: int = None,
                              line: int = None) -> dict:
        """Create a comment on a commit."""
        payload = {"body": body}
        if path:
            payload["path"] = path
        if position is not None:
            payload["position"] = position
        if line is not None:
            payload["line"] = line
        return _post(f"/repos/{owner}/{repo}/commits/{commit_sha}/comments", payload)

    # --- Commit Statuses ---

    @mcp.tool()
    def create_commit_status(owner: str, repo: str, sha: str, state: str,
                             target_url: str = None, description: str = None,
                             context: str = "default") -> dict:
        """Create a commit status. state: error, failure, pending, success."""
        payload = {"state": state, "context": context}
        if target_url:
            payload["target_url"] = target_url
        if description:
            payload["description"] = description
        return _post(f"/repos/{owner}/{repo}/statuses/{sha}", payload)

    @mcp.tool()
    def get_combined_status(owner: str, repo: str, ref: str) -> dict:
        """Get the combined status for a specific reference (branch, tag, or SHA)."""
        return _get(f"/repos/{owner}/{repo}/commits/{ref}/status")

    @mcp.tool()
    def list_commit_statuses(owner: str, repo: str, ref: str,
                             per_page: int = 30, page: int = 1) -> dict:
        """List statuses for a specific reference."""
        return _get(f"/repos/{owner}/{repo}/commits/{ref}/statuses",
                    {"per_page": per_page, "page": page})
