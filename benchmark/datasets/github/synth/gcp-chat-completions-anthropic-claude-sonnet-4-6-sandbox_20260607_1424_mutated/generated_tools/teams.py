"""GitHub Teams tools."""
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


def register_teams_tools(mcp: FastMCP):

    @mcp.tool()
    def list_teams(org: str, per_page: int = 30, page: int = 1) -> dict:
        """List teams in an organization."""
        return _get(f"/orgs/{org}/teams", {"per_page": per_page, "page": page})

    @mcp.tool()
    def get_team_by_name(org: str, team_slug: str) -> dict:
        """Get a team by its slug."""
        return _get(f"/orgs/{org}/teams/{team_slug}")

    @mcp.tool()
    def create_team(org: str, name: str, description: str = "",
                    privacy: str = "secret", maintainers: list = None,
                    repo_names: list = None, parent_team_id: int = None) -> dict:
        """Create a team in an organization. privacy: secret|closed."""
        payload = {"name": name, "privacy": privacy}
        if description:
            payload["description"] = description
        if maintainers:
            payload["maintainers"] = maintainers
        if repo_names:
            payload["repo_names"] = repo_names
        if parent_team_id is not None:
            payload["parent_team_id"] = parent_team_id
        return _post(f"/orgs/{org}/teams", payload)

    @mcp.tool()
    def update_team(org: str, team_slug: str, name: str = None,
                    description: str = None, privacy: str = None,
                    parent_team_id: int = None) -> dict:
        """Update a team."""
        payload = {}
        if name is not None:
            payload["name"] = name
        if description is not None:
            payload["description"] = description
        if privacy is not None:
            payload["privacy"] = privacy
        if parent_team_id is not None:
            payload["parent_team_id"] = parent_team_id
        return _patch(f"/orgs/{org}/teams/{team_slug}", payload)

    @mcp.tool()
    def delete_team(org: str, team_slug: str) -> dict:
        """Delete a team."""
        return _delete(f"/orgs/{org}/teams/{team_slug}")

    @mcp.tool()
    def list_team_members(org: str, team_slug: str, role: str = "all",
                          per_page: int = 30, page: int = 1) -> dict:
        """List members of a team. role: member|maintainer|all."""
        return _get(f"/orgs/{org}/teams/{team_slug}/members",
                    {"role": role, "per_page": per_page, "page": page})

    @mcp.tool()
    def get_team_membership(org: str, team_slug: str, username: str) -> dict:
        """Get a user's membership in a team."""
        return _get(f"/orgs/{org}/teams/{team_slug}/memberships/{username}")

    @mcp.tool()
    def add_or_update_team_membership(org: str, team_slug: str, username: str,
                                      role: str = "member") -> dict:
        """Add or update a user's membership in a team. role: member|maintainer."""
        return _put(f"/orgs/{org}/teams/{team_slug}/memberships/{username}",
                    {"role": role})

    @mcp.tool()
    def remove_team_membership(org: str, team_slug: str, username: str) -> dict:
        """Remove a user from a team."""
        return _delete(f"/orgs/{org}/teams/{team_slug}/memberships/{username}")

    @mcp.tool()
    def list_team_repos(org: str, team_slug: str, per_page: int = 30, page: int = 1) -> dict:
        """List repositories a team has access to."""
        return _get(f"/orgs/{org}/teams/{team_slug}/repos",
                    {"per_page": per_page, "page": page})

    @mcp.tool()
    def check_team_repo_permissions(org: str, team_slug: str, owner: str, repo: str) -> dict:
        """Check if a team has access to a repository."""
        return _get(f"/orgs/{org}/teams/{team_slug}/repos/{owner}/{repo}")

    @mcp.tool()
    def add_or_update_team_repo(org: str, team_slug: str, owner: str, repo: str,
                                permission: str = "push") -> dict:
        """Add or update team access to a repository. permission: pull|triage|push|maintain|admin."""
        return _put(f"/orgs/{org}/teams/{team_slug}/repos/{owner}/{repo}",
                    {"permission": permission})

    @mcp.tool()
    def remove_team_repo(org: str, team_slug: str, owner: str, repo: str) -> dict:
        """Remove a repository from a team."""
        return _delete(f"/orgs/{org}/teams/{team_slug}/repos/{owner}/{repo}")

    @mcp.tool()
    def list_child_teams(org: str, team_slug: str, per_page: int = 30, page: int = 1) -> dict:
        """List child teams of a team."""
        return _get(f"/orgs/{org}/teams/{team_slug}/teams",
                    {"per_page": per_page, "page": page})
