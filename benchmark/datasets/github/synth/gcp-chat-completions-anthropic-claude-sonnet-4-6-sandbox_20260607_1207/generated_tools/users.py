"""GitHub Users tools."""
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


def _patch(path, json=None):
    try:
        r = requests.patch(f"{BASE_URL}{path}", headers=HEADERS, json=json, timeout=30)
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


def _delete(path):
    try:
        r = requests.delete(f"{BASE_URL}{path}", headers=HEADERS, timeout=30)
        if r.status_code == 204:
            return {"status": "no_content"}
        return r.json()
    except Exception as e:
        return {"error": str(e)}


def register_users_tools(mcp: FastMCP):

    @mcp.tool()
    def get_authenticated_user() -> dict:
        """Get the authenticated user's profile information."""
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
    def list_followers_of_user(username: str, per_page: int = 30, page: int = 1) -> dict:
        """List followers of a user."""
        return _get(f"/users/{username}/followers", {"per_page": per_page, "page": page})

    @mcp.tool()
    def list_following_for_user(username: str, per_page: int = 30, page: int = 1) -> dict:
        """List users that a user is following."""
        return _get(f"/users/{username}/following", {"per_page": per_page, "page": page})

    @mcp.tool()
    def list_my_followers(per_page: int = 30, page: int = 1) -> dict:
        """List followers of the authenticated user."""
        return _get("/user/followers", {"per_page": per_page, "page": page})

    @mcp.tool()
    def list_my_following(per_page: int = 30, page: int = 1) -> dict:
        """List users the authenticated user is following."""
        return _get("/user/following", {"per_page": per_page, "page": page})

    @mcp.tool()
    def follow_user(username: str) -> dict:
        """Follow a user."""
        try:
            r = requests.put(f"{BASE_URL}/user/following/{username}",
                             headers=HEADERS, timeout=30)
            if r.status_code == 204:
                return {"status": "following"}
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def unfollow_user(username: str) -> dict:
        """Unfollow a user."""
        return _delete(f"/user/following/{username}")

    @mcp.tool()
    def list_user_orgs(username: str, per_page: int = 30, page: int = 1) -> dict:
        """List public organizations for a user."""
        return _get(f"/users/{username}/orgs", {"per_page": per_page, "page": page})

    @mcp.tool()
    def list_my_orgs(per_page: int = 30, page: int = 1) -> dict:
        """List organizations for the authenticated user."""
        return _get("/user/orgs", {"per_page": per_page, "page": page})

    @mcp.tool()
    def get_org(org: str) -> dict:
        """Get an organization's public profile."""
        return _get(f"/orgs/{org}")

    @mcp.tool()
    def list_org_members(org: str, filter: str = "all", role: str = "all",
                         per_page: int = 30, page: int = 1) -> dict:
        """List members of an organization."""
        return _get(f"/orgs/{org}/members",
                    {"filter": filter, "role": role, "per_page": per_page, "page": page})

    @mcp.tool()
    def list_collaborators(owner: str, repo: str, affiliation: str = "all",
                           permission: str = None, per_page: int = 30, page: int = 1) -> dict:
        """List collaborators for a repository."""
        params = {"affiliation": affiliation, "per_page": per_page, "page": page}
        if permission:
            params["permission"] = permission
        return _get(f"/repos/{owner}/{repo}/collaborators", params)

    @mcp.tool()
    def add_collaborator(owner: str, repo: str, username: str,
                         permission: str = "push") -> dict:
        """Add a collaborator to a repository. permission: pull, triage, push, maintain, admin."""
        try:
            r = requests.put(f"{BASE_URL}/repos/{owner}/{repo}/collaborators/{username}",
                             headers=HEADERS, json={"permission": permission}, timeout=30)
            if r.status_code == 204:
                return {"status": "already_collaborator"}
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def remove_collaborator(owner: str, repo: str, username: str) -> dict:
        """Remove a collaborator from a repository."""
        return _delete(f"/repos/{owner}/{repo}/collaborators/{username}")
