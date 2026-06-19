"""GitHub Users tools."""
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

def _patch(path, json=None):
    try:
        r = requests.patch(f"{BASE_URL}{path}", headers=_headers(), json=json, timeout=30)
        if r.status_code == 204:
            return {"status": "no_content"}
        return r.json()
    except Exception as e:
        return {"error": str(e)}


def register_users_tools(mcp: FastMCP):

    @mcp.tool()
    def get_authenticated_user() -> dict:
        """Get the authenticated user's profile."""
        return _get("/user")

    @mcp.tool()
    def update_authenticated_user(name: str = None, email: str = None,
                                  blog: str = None, company: str = None,
                                  location: str = None, hireable: bool = None,
                                  bio: str = None, twitter_username: str = None) -> dict:
        """Update the authenticated user's profile."""
        payload = {}
        if name is not None:
            payload["name"] = name
        if email is not None:
            payload["email"] = email
        if blog is not None:
            payload["blog"] = blog
        if company is not None:
            payload["company"] = company
        if location is not None:
            payload["location"] = location
        if hireable is not None:
            payload["hireable"] = hireable
        if bio is not None:
            payload["bio"] = bio
        if twitter_username is not None:
            payload["twitter_username"] = twitter_username
        return _patch("/user", payload)

    @mcp.tool()
    def get_user(username: str) -> dict:
        """Get a public user's profile by username."""
        return _get(f"/users/{username}")

    @mcp.tool()
    def get_user_by_id(account_id: int) -> dict:
        """Get a user by their numeric account ID."""
        return _get(f"/user/{account_id}")

    @mcp.tool()
    def list_users(since: int = None, per_page: int = 30) -> dict:
        """List all users (paginated by since user ID)."""
        params = {"per_page": per_page}
        if since is not None:
            params["since"] = since
        return _get("/users", params)

    @mcp.tool()
    def list_followers_of_user(username: str, per_page: int = 30, page: int = 1) -> dict:
        """List followers of a user."""
        return _get(f"/users/{username}/followers",
                    {"per_page": per_page, "page": page})

    @mcp.tool()
    def list_following_for_user(username: str, per_page: int = 30, page: int = 1) -> dict:
        """List users that a user follows."""
        return _get(f"/users/{username}/following",
                    {"per_page": per_page, "page": page})

    @mcp.tool()
    def list_my_followers(per_page: int = 30, page: int = 1) -> dict:
        """List followers of the authenticated user."""
        return _get("/user/followers", {"per_page": per_page, "page": page})

    @mcp.tool()
    def list_my_following(per_page: int = 30, page: int = 1) -> dict:
        """List users the authenticated user follows."""
        return _get("/user/following", {"per_page": per_page, "page": page})

    @mcp.tool()
    def get_user_hovercard(username: str, subject_type: str = "",
                           subject_id: str = "") -> dict:
        """Get contextual hovercard information for a user."""
        params = {}
        if subject_type:
            params["subject_type"] = subject_type
        if subject_id:
            params["subject_id"] = subject_id
        return _get(f"/users/{username}/hovercard", params)
