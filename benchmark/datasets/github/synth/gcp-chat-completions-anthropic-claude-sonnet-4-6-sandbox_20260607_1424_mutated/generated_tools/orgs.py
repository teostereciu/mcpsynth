"""GitHub Organizations and Collaborators tools."""
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


def register_orgs_tools(mcp: FastMCP):

    # ── Organizations ────────────────────────────────────────────────────────

    @mcp.tool()
    def list_organizations(since: int = None, per_page: int = 30) -> dict:
        """List all organizations."""
        params = {"per_page": per_page}
        if since is not None:
            params["since"] = since
        return _get("/organizations", params)

    @mcp.tool()
    def get_org(org: str) -> dict:
        """Get an organization's details."""
        return _get(f"/orgs/{org}")

    @mcp.tool()
    def update_org(org: str, name: str = None, description: str = None,
                   email: str = None, location: str = None, company: str = None,
                   blog: str = None,
                   default_repository_permission: str = None,
                   members_can_create_repositories: bool = None) -> dict:
        """Update an organization's settings."""
        payload = {}
        if name is not None:
            payload["name"] = name
        if description is not None:
            payload["description"] = description
        if email is not None:
            payload["email"] = email
        if location is not None:
            payload["location"] = location
        if company is not None:
            payload["company"] = company
        if blog is not None:
            payload["blog"] = blog
        if default_repository_permission is not None:
            payload["default_repository_permission"] = default_repository_permission
        if members_can_create_repositories is not None:
            payload["members_can_create_repositories"] = members_can_create_repositories
        return _patch(f"/orgs/{org}", payload)

    @mcp.tool()
    def list_org_members(org: str, filter: str = "all", role: str = "all",
                         per_page: int = 30, page: int = 1) -> dict:
        """List members of an organization. filter: 2fa_disabled|all. role: all|admin|member."""
        return _get(f"/orgs/{org}/members",
                    {"filter": filter, "role": role, "per_page": per_page, "page": page})

    @mcp.tool()
    def check_org_membership(org: str, username: str) -> dict:
        """Check if a user is a member of an organization."""
        try:
            r = requests.get(f"{BASE_URL}/orgs/{org}/members/{username}",
                             headers=_headers(), timeout=30)
            if r.status_code == 204:
                return {"is_member": True}
            elif r.status_code == 404:
                return {"is_member": False}
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def remove_org_member(org: str, username: str) -> dict:
        """Remove a member from an organization."""
        return _delete(f"/orgs/{org}/members/{username}")

    @mcp.tool()
    def get_org_membership(org: str, username: str) -> dict:
        """Get a user's membership in an organization."""
        return _get(f"/orgs/{org}/memberships/{username}")

    @mcp.tool()
    def set_org_membership(org: str, username: str, role: str = "member") -> dict:
        """Set a user's membership in an organization. role: member|admin."""
        return _put(f"/orgs/{org}/memberships/{username}", {"role": role})

    @mcp.tool()
    def remove_org_membership(org: str, username: str) -> dict:
        """Remove a user's membership from an organization."""
        return _delete(f"/orgs/{org}/memberships/{username}")

    @mcp.tool()
    def list_my_orgs(per_page: int = 30, page: int = 1) -> dict:
        """List organizations for the authenticated user."""
        return _get("/user/orgs", {"per_page": per_page, "page": page})

    @mcp.tool()
    def list_user_orgs(username: str, per_page: int = 30, page: int = 1) -> dict:
        """List public organizations for a user."""
        return _get(f"/users/{username}/orgs", {"per_page": per_page, "page": page})

    # ── Collaborators ────────────────────────────────────────────────────────

    @mcp.tool()
    def list_repo_collaborators(owner: str, repo: str, affiliation: str = "all",
                                permission: str = "", per_page: int = 30, page: int = 1) -> dict:
        """List collaborators for a repository. affiliation: outside|direct|all."""
        params = {"affiliation": affiliation, "per_page": per_page, "page": page}
        if permission:
            params["permission"] = permission
        return _get(f"/repos/{owner}/{repo}/collaborators", params)

    @mcp.tool()
    def check_repo_collaborator(owner: str, repo: str, username: str) -> dict:
        """Check if a user is a collaborator on a repository."""
        try:
            r = requests.get(f"{BASE_URL}/repos/{owner}/{repo}/collaborators/{username}",
                             headers=_headers(), timeout=30)
            if r.status_code == 204:
                return {"is_collaborator": True}
            elif r.status_code == 404:
                return {"is_collaborator": False}
            return r.json()
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def add_repo_collaborator(owner: str, repo: str, username: str,
                              permission: str = "push") -> dict:
        """Add a collaborator to a repository. permission: pull|triage|push|maintain|admin."""
        return _put(f"/repos/{owner}/{repo}/collaborators/{username}",
                    {"permission": permission})

    @mcp.tool()
    def remove_repo_collaborator(owner: str, repo: str, username: str) -> dict:
        """Remove a collaborator from a repository."""
        return _delete(f"/repos/{owner}/{repo}/collaborators/{username}")

    @mcp.tool()
    def get_repo_collaborator_permission(owner: str, repo: str, username: str) -> dict:
        """Get the permission level of a collaborator on a repository."""
        return _get(f"/repos/{owner}/{repo}/collaborators/{username}/permission")

    # ── Org Invitations ──────────────────────────────────────────────────────

    @mcp.tool()
    def list_pending_org_invitations(org: str, per_page: int = 30, page: int = 1) -> dict:
        """List pending invitations for an organization."""
        return _get(f"/orgs/{org}/invitations",
                    {"per_page": per_page, "page": page})

    @mcp.tool()
    def create_org_invitation(org: str, invitee_id: int = None, email: str = "",
                              role: str = "direct_member",
                              team_ids: list = None) -> dict:
        """Invite a user to an organization. Provide either invitee_id or email."""
        payload = {"role": role}
        if invitee_id is not None:
            payload["invitee_id"] = invitee_id
        if email:
            payload["email"] = email
        if team_ids:
            payload["team_ids"] = team_ids
        return _post(f"/orgs/{org}/invitations", payload)

    @mcp.tool()
    def cancel_org_invitation(org: str, invitation_id: int) -> dict:
        """Cancel an organization invitation."""
        return _delete(f"/orgs/{org}/invitations/{invitation_id}")
