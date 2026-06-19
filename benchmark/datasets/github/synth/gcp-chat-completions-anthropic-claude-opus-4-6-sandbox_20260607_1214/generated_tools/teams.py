"""GitHub Teams tools."""

from typing import Any, Optional
from generated_tools.github_client import github_get, github_post, github_patch, github_put, github_delete


def list_teams(org: str, per_page: int = 30, page: int = 1) -> Any:
    """List teams for an organization.

    Args:
        org: Organization name
        per_page: Results per page (max 100)
        page: Page number
    """
    return github_get(f"/orgs/{org}/teams", {"per_page": per_page, "page": page})


def create_team(org: str, name: str, description: Optional[str] = None,
                privacy: str = "secret", permission: str = "pull",
                repo_names: Optional[list] = None, parent_team_id: Optional[int] = None) -> Any:
    """Create a team.

    Args:
        org: Organization name
        name: Team name
        description: Team description
        privacy: Privacy level (secret, closed)
        permission: Default permission (pull, push)
        repo_names: List of repository names (org/repo format)
        parent_team_id: Parent team ID for nested teams
    """
    data = {"name": name, "privacy": privacy, "permission": permission}
    if description:
        data["description"] = description
    if repo_names:
        data["repo_names"] = repo_names
    if parent_team_id:
        data["parent_team_id"] = parent_team_id
    return github_post(f"/orgs/{org}/teams", data)


def get_team_by_name(org: str, team_slug: str) -> Any:
    """Get a team by name.

    Args:
        org: Organization name
        team_slug: Team slug
    """
    return github_get(f"/orgs/{org}/teams/{team_slug}")


def update_team(org: str, team_slug: str, name: Optional[str] = None,
                description: Optional[str] = None, privacy: Optional[str] = None,
                permission: Optional[str] = None, parent_team_id: Optional[int] = None) -> Any:
    """Update a team.

    Args:
        org: Organization name
        team_slug: Team slug
        name: New team name
        description: New description
        privacy: New privacy level (secret, closed)
        permission: New default permission (pull, push)
        parent_team_id: New parent team ID
    """
    data = {}
    if name:
        data["name"] = name
    if description is not None:
        data["description"] = description
    if privacy:
        data["privacy"] = privacy
    if permission:
        data["permission"] = permission
    if parent_team_id is not None:
        data["parent_team_id"] = parent_team_id
    return github_patch(f"/orgs/{org}/teams/{team_slug}", data)


def delete_team(org: str, team_slug: str) -> Any:
    """Delete a team.

    Args:
        org: Organization name
        team_slug: Team slug
    """
    return github_delete(f"/orgs/{org}/teams/{team_slug}")


def list_team_members(org: str, team_slug: str, role: str = "all",
                      per_page: int = 30, page: int = 1) -> Any:
    """List team members.

    Args:
        org: Organization name
        team_slug: Team slug
        role: Filter by role (member, maintainer, all)
        per_page: Results per page (max 100)
        page: Page number
    """
    return github_get(f"/orgs/{org}/teams/{team_slug}/members",
                      {"role": role, "per_page": per_page, "page": page})


def list_team_repositories(org: str, team_slug: str, per_page: int = 30, page: int = 1) -> Any:
    """List team repositories.

    Args:
        org: Organization name
        team_slug: Team slug
        per_page: Results per page (max 100)
        page: Page number
    """
    return github_get(f"/orgs/{org}/teams/{team_slug}/repos",
                      {"per_page": per_page, "page": page})


def add_or_update_team_repository(org: str, team_slug: str, owner: str, repo: str,
                                  permission: str = "push") -> Any:
    """Add or update team repository permissions.

    Args:
        org: Organization name
        team_slug: Team slug
        owner: Repository owner
        repo: Repository name
        permission: Permission level (pull, triage, push, maintain, admin)
    """
    return github_put(f"/orgs/{org}/teams/{team_slug}/repos/{owner}/{repo}",
                      {"permission": permission})


def remove_team_repository(org: str, team_slug: str, owner: str, repo: str) -> Any:
    """Remove a repository from a team.

    Args:
        org: Organization name
        team_slug: Team slug
        owner: Repository owner
        repo: Repository name
    """
    return github_delete(f"/orgs/{org}/teams/{team_slug}/repos/{owner}/{repo}")
