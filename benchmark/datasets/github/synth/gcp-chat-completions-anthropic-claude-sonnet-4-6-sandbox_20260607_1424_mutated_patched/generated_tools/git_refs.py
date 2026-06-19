"""GitHub Git References tools."""
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

def _delete(path, json=None):
    try:
        r = requests.delete(f"{BASE_URL}{path}", headers=_headers(), json=json, timeout=30)
        if r.status_code == 204:
            return {"status": "no_content"}
        return r.json()
    except Exception as e:
        return {"error": str(e)}


def register_git_refs_tools(mcp: FastMCP):

    @mcp.tool()
    def list_matching_git_refs(owner: str, repo: str, ref: str) -> dict:
        """List matching Git references. ref format: heads/<branch> or tags/<tag>."""
        return _get(f"/repos/{owner}/{repo}/git/matching-refs/{ref}")

    @mcp.tool()
    def get_git_ref(owner: str, repo: str, ref: str) -> dict:
        """Get a single Git reference. ref format: heads/<branch> or tags/<tag>."""
        return _get(f"/repos/{owner}/{repo}/git/ref/{ref}")

    @mcp.tool()
    def create_git_ref(owner: str, repo: str, ref: str, sha: str) -> dict:
        """Create a Git reference. ref must be fully qualified (e.g. refs/heads/branch-name)."""
        return _post(f"/repos/{owner}/{repo}/git/refs", {"ref": ref, "sha": sha})

    @mcp.tool()
    def update_git_ref(owner: str, repo: str, ref: str, sha: str,
                       force: bool = False) -> dict:
        """Update a Git reference to point to a new SHA."""
        return _patch(f"/repos/{owner}/{repo}/git/refs/{ref}",
                      {"sha": sha, "force": force})

    @mcp.tool()
    def delete_git_ref(owner: str, repo: str, ref: str) -> dict:
        """Delete a Git reference."""
        return _delete(f"/repos/{owner}/{repo}/git/refs/{ref}")
