"""GitHub Git Database (low-level git objects) tools."""
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


def register_git_objects_tools(mcp: FastMCP):

    # --- Git Commits ---

    @mcp.tool()
    def create_git_commit(owner: str, repo: str, message: str, tree: str,
                          parents: list = None, author_name: str = None,
                          author_email: str = None, author_date: str = None) -> dict:
        """Create a low-level git commit object. tree is the SHA of the tree object."""
        payload = {"message": message, "tree": tree}
        if parents:
            payload["parents"] = parents
        if author_name and author_email:
            author = {"name": author_name, "email": author_email}
            if author_date:
                author["date"] = author_date
            payload["author"] = author
        return _post(f"/repos/{owner}/{repo}/git/commits", payload)

    @mcp.tool()
    def get_git_commit(owner: str, repo: str, commit_sha: str) -> dict:
        """Get a git commit object by SHA."""
        return _get(f"/repos/{owner}/{repo}/git/commits/{commit_sha}")

    # --- Git Trees ---

    @mcp.tool()
    def get_git_tree(owner: str, repo: str, tree_sha: str, recursive: bool = False) -> dict:
        """Get a git tree object. Set recursive=True to get all files recursively."""
        params = {}
        if recursive:
            params["recursive"] = "1"
        return _get(f"/repos/{owner}/{repo}/git/trees/{tree_sha}", params or None)

    @mcp.tool()
    def create_git_tree(owner: str, repo: str, tree: list, base_tree: str = None) -> dict:
        """Create a git tree object. tree is a list of objects with path, mode, type, sha/content."""
        payload = {"tree": tree}
        if base_tree:
            payload["base_tree"] = base_tree
        return _post(f"/repos/{owner}/{repo}/git/trees", payload)

    # --- Git Blobs ---

    @mcp.tool()
    def get_git_blob(owner: str, repo: str, file_sha: str) -> dict:
        """Get a git blob object by SHA."""
        return _get(f"/repos/{owner}/{repo}/git/blobs/{file_sha}")

    @mcp.tool()
    def create_git_blob(owner: str, repo: str, content: str,
                        encoding: str = "utf-8") -> dict:
        """Create a git blob object. encoding: utf-8 or base64."""
        return _post(f"/repos/{owner}/{repo}/git/blobs",
                     {"content": content, "encoding": encoding})

    # --- Git Tags ---

    @mcp.tool()
    def get_git_tag(owner: str, repo: str, tag_sha: str) -> dict:
        """Get a git tag object by SHA."""
        return _get(f"/repos/{owner}/{repo}/git/tags/{tag_sha}")

    @mcp.tool()
    def create_git_tag(owner: str, repo: str, tag: str, message: str,
                       object_sha: str, object_type: str = "commit",
                       tagger_name: str = None, tagger_email: str = None,
                       tagger_date: str = None) -> dict:
        """Create a git tag object. object_type: commit, tree, or blob."""
        payload = {"tag": tag, "message": message, "object": object_sha, "type": object_type}
        if tagger_name and tagger_email:
            tagger = {"name": tagger_name, "email": tagger_email}
            if tagger_date:
                tagger["date"] = tagger_date
            payload["tagger"] = tagger
        return _post(f"/repos/{owner}/{repo}/git/tags", payload)
