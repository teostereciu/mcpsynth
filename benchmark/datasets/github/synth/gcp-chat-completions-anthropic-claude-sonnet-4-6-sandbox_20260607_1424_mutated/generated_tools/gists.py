"""GitHub Gists tools."""
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


def register_gists_tools(mcp: FastMCP):

    @mcp.tool()
    def list_my_gists(since: str = "", per_page: int = 30, page: int = 1) -> dict:
        """List gists for the authenticated user."""
        params = {"per_page": per_page, "page": page}
        if since:
            params["since"] = since
        return _get("/gists", params)

    @mcp.tool()
    def list_public_gists(since: str = "", per_page: int = 30, page: int = 1) -> dict:
        """List public gists."""
        params = {"per_page": per_page, "page": page}
        if since:
            params["since"] = since
        return _get("/gists/public", params)

    @mcp.tool()
    def list_starred_gists(since: str = "", per_page: int = 30, page: int = 1) -> dict:
        """List starred gists for the authenticated user."""
        params = {"per_page": per_page, "page": page}
        if since:
            params["since"] = since
        return _get("/gists/starred", params)

    @mcp.tool()
    def get_gist(gist_id: str) -> dict:
        """Get a gist by ID."""
        return _get(f"/gists/{gist_id}")

    @mcp.tool()
    def create_gist(files: dict, description: str = "", public: bool = False) -> dict:
        """Create a gist. files is a dict of {filename: {content: '...'}}."""
        return _post("/gists", {"files": files, "description": description, "public": public})

    @mcp.tool()
    def update_gist(gist_id: str, files: dict = None, description: str = None) -> dict:
        """Update a gist. files is a dict of {filename: {content: '...'}} or {filename: null} to delete."""
        payload = {}
        if files is not None:
            payload["files"] = files
        if description is not None:
            payload["description"] = description
        return _patch(f"/gists/{gist_id}", payload)

    @mcp.tool()
    def delete_gist(gist_id: str) -> dict:
        """Delete a gist."""
        return _delete(f"/gists/{gist_id}")

    @mcp.tool()
    def star_gist(gist_id: str) -> dict:
        """Star a gist."""
        return _put(f"/gists/{gist_id}/star")

    @mcp.tool()
    def unstar_gist(gist_id: str) -> dict:
        """Unstar a gist."""
        return _delete(f"/gists/{gist_id}/star")

    @mcp.tool()
    def check_gist_starred(gist_id: str) -> dict:
        """Check if a gist is starred."""
        try:
            r = requests.get(f"{BASE_URL}/gists/{gist_id}/star",
                             headers=_headers(), timeout=30)
            if r.status_code == 204:
                return {"starred": True}
            elif r.status_code == 404:
                return {"starred": False}
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def fork_gist(gist_id: str) -> dict:
        """Fork a gist."""
        return _post(f"/gists/{gist_id}/forks")

    @mcp.tool()
    def list_gist_forks(gist_id: str, per_page: int = 30, page: int = 1) -> dict:
        """List forks of a gist."""
        return _get(f"/gists/{gist_id}/forks", {"per_page": per_page, "page": page})

    @mcp.tool()
    def list_gist_commits(gist_id: str, per_page: int = 30, page: int = 1) -> dict:
        """List commits for a gist."""
        return _get(f"/gists/{gist_id}/commits", {"per_page": per_page, "page": page})

    @mcp.tool()
    def list_user_gists(username: str, since: str = "", per_page: int = 30, page: int = 1) -> dict:
        """List public gists for a user."""
        params = {"per_page": per_page, "page": page}
        if since:
            params["since"] = since
        return _get(f"/users/{username}/gists", params)
