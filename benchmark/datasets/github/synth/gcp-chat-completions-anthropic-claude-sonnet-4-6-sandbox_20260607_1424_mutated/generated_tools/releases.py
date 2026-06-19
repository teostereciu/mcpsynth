"""GitHub Releases tools."""
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


def register_releases_tools(mcp: FastMCP):

    @mcp.tool()
    def list_releases(owner: str, repo: str, per_page: int = 30, page: int = 1) -> dict:
        """List releases for a repository."""
        return _get(f"/repos/{owner}/{repo}/releases",
                    {"per_page": per_page, "page": page})

    @mcp.tool()
    def get_release(owner: str, repo: str, release_id: int) -> dict:
        """Get a release by ID."""
        return _get(f"/repos/{owner}/{repo}/releases/{release_id}")

    @mcp.tool()
    def get_release_by_tag(owner: str, repo: str, tag: str) -> dict:
        """Get a release by tag name."""
        return _get(f"/repos/{owner}/{repo}/releases/tags/{tag}")

    @mcp.tool()
    def get_latest_release(owner: str, repo: str) -> dict:
        """Get the latest published release for a repository."""
        return _get(f"/repos/{owner}/{repo}/releases/latest")

    @mcp.tool()
    def create_release(owner: str, repo: str, tag_name: str,
                       name: str = "", body: str = "",
                       target_commitish: str = "",
                       draft: bool = False, prerelease: bool = False,
                       generate_release_notes: bool = False,
                       make_latest: str = "true") -> dict:
        """Create a release. make_latest: true|false|legacy."""
        payload = {"tag_name": tag_name, "draft": draft, "prerelease": prerelease,
                   "generate_release_notes": generate_release_notes,
                   "make_latest": make_latest}
        if name:
            payload["name"] = name
        if body:
            payload["body"] = body
        if target_commitish:
            payload["target_commitish"] = target_commitish
        return _post(f"/repos/{owner}/{repo}/releases", payload)

    @mcp.tool()
    def update_release(owner: str, repo: str, release_id: int,
                       tag_name: str = None, name: str = None, body: str = None,
                       draft: bool = None, prerelease: bool = None,
                       make_latest: str = None) -> dict:
        """Update a release."""
        payload = {}
        if tag_name is not None:
            payload["tag_name"] = tag_name
        if name is not None:
            payload["name"] = name
        if body is not None:
            payload["body"] = body
        if draft is not None:
            payload["draft"] = draft
        if prerelease is not None:
            payload["prerelease"] = prerelease
        if make_latest is not None:
            payload["make_latest"] = make_latest
        return _patch(f"/repos/{owner}/{repo}/releases/{release_id}", payload)

    @mcp.tool()
    def delete_release(owner: str, repo: str, release_id: int) -> dict:
        """Delete a release."""
        return _delete(f"/repos/{owner}/{repo}/releases/{release_id}")

    @mcp.tool()
    def generate_release_notes(owner: str, repo: str, tag_name: str,
                               target_commitish: str = "",
                               previous_tag_name: str = "") -> dict:
        """Generate release notes content for a release."""
        payload = {"tag_name": tag_name}
        if target_commitish:
            payload["target_commitish"] = target_commitish
        if previous_tag_name:
            payload["previous_tag_name"] = previous_tag_name
        return _post(f"/repos/{owner}/{repo}/releases/generate-notes", payload)

    @mcp.tool()
    def list_release_assets(owner: str, repo: str, release_id: int,
                            per_page: int = 30, page: int = 1) -> dict:
        """List assets for a release."""
        return _get(f"/repos/{owner}/{repo}/releases/{release_id}/assets",
                    {"per_page": per_page, "page": page})

    @mcp.tool()
    def get_release_asset(owner: str, repo: str, asset_id: int) -> dict:
        """Get a release asset."""
        return _get(f"/repos/{owner}/{repo}/releases/assets/{asset_id}")

    @mcp.tool()
    def update_release_asset(owner: str, repo: str, asset_id: int,
                             name: str = None, label: str = None) -> dict:
        """Update a release asset name or label."""
        payload = {}
        if name is not None:
            payload["name"] = name
        if label is not None:
            payload["label"] = label
        return _patch(f"/repos/{owner}/{repo}/releases/assets/{asset_id}", payload)

    @mcp.tool()
    def delete_release_asset(owner: str, repo: str, asset_id: int) -> dict:
        """Delete a release asset."""
        return _delete(f"/repos/{owner}/{repo}/releases/assets/{asset_id}")
