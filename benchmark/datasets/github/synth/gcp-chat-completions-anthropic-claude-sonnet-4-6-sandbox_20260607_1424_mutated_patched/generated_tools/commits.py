"""GitHub Commits and Forks tools."""
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


def register_commits_tools(mcp: FastMCP):

    @mcp.tool()
    def list_commits(owner: str, repo: str, sha: str = "", path: str = "",
                     author: str = "", committer: str = "",
                     since: str = "", until: str = "",
                     per_page: int = 30, page: int = 1) -> dict:
        """List commits for a repository. sha can be a branch name or commit SHA."""
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
        """Get a commit by SHA, branch, or tag."""
        return _get(f"/repos/{owner}/{repo}/commits/{ref}")

    @mcp.tool()
    def compare_commits(owner: str, repo: str, base: str, head: str) -> dict:
        """Compare two commits, branches, or tags."""
        return _get(f"/repos/{owner}/{repo}/compare/{base}...{head}")

    @mcp.tool()
    def list_branches_for_head_commit(owner: str, repo: str, commit_sha: str) -> dict:
        """List branches where the given commit SHA is the HEAD."""
        return _get(f"/repos/{owner}/{repo}/commits/{commit_sha}/branches-where-head")

    @mcp.tool()
    def list_prs_for_commit(owner: str, repo: str, commit_sha: str,
                            per_page: int = 30, page: int = 1) -> dict:
        """List pull requests associated with a commit."""
        return _get(f"/repos/{owner}/{repo}/commits/{commit_sha}/pulls",
                    {"per_page": per_page, "page": page})

    @mcp.tool()
    def list_commit_statuses(owner: str, repo: str, ref: str,
                             per_page: int = 30, page: int = 1) -> dict:
        """List commit statuses for a reference (SHA, branch, or tag)."""
        return _get(f"/repos/{owner}/{repo}/commits/{ref}/statuses",
                    {"per_page": per_page, "page": page})

    @mcp.tool()
    def get_combined_commit_status(owner: str, repo: str, ref: str) -> dict:
        """Get the combined status for a specific reference."""
        return _get(f"/repos/{owner}/{repo}/commits/{ref}/status")

    @mcp.tool()
    def create_commit_status(owner: str, repo: str, sha: str,
                             state: str, context: str = "default",
                             description: str = "", target_url: str = "") -> dict:
        """Create a commit status. state: error|failure|pending|success."""
        payload = {"state": state, "context": context}
        if description:
            payload["description"] = description
        if target_url:
            payload["target_url"] = target_url
        return _post(f"/repos/{owner}/{repo}/statuses/{sha}", payload)

    @mcp.tool()
    def list_commit_comments(owner: str, repo: str, commit_sha: str,
                             per_page: int = 30, page: int = 1) -> dict:
        """List comments for a commit."""
        return _get(f"/repos/{owner}/{repo}/commits/{commit_sha}/comments",
                    {"per_page": per_page, "page": page})

    @mcp.tool()
    def create_commit_comment(owner: str, repo: str, commit_sha: str,
                              body: str, path: str = "", position: int = None,
                              line: int = None) -> dict:
        """Create a comment for a commit."""
        payload = {"body": body}
        if path:
            payload["path"] = path
        if position is not None:
            payload["position"] = position
        if line is not None:
            payload["line"] = line
        return _post(f"/repos/{owner}/{repo}/commits/{commit_sha}/comments", payload)

    # ── Forks ────────────────────────────────────────────────────────────────

    @mcp.tool()
    def list_forks(owner: str, repo: str, sort: str = "newest",
                   per_page: int = 30, page: int = 1) -> dict:
        """List forks of a repository. sort: newest|oldest|stargazers|watchers."""
        return _get(f"/repos/{owner}/{repo}/forks",
                    {"sort": sort, "per_page": per_page, "page": page})

    @mcp.tool()
    def create_fork(owner: str, repo: str, organization: str = "",
                    name: str = "", default_branch_only: bool = False) -> dict:
        """Fork a repository. Optionally specify an organization to fork into."""
        payload = {"default_branch_only": default_branch_only}
        if organization:
            payload["organization"] = organization
        if name:
            payload["name"] = name
        return _post(f"/repos/{owner}/{repo}/forks", payload)
