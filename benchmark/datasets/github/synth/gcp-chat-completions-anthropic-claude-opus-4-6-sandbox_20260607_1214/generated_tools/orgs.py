"""GitHub Organizations tools."""

from typing import Any, Optional
from generated_tools.github_client import github_get, github_patch


def get_organization(org: str) -> Any:
    """Get an organization.

    Args:
        org: Organization name
    """
    return github_get(f"/orgs/{org}")


def update_organization(org: str, billing_email: Optional[str] = None,
                        company: Optional[str] = None, email: Optional[str] = None,
                        location: Optional[str] = None, name: Optional[str] = None,
                        description: Optional[str] = None, default_repository_permission: Optional[str] = None,
                        members_can_create_repositories: Optional[bool] = None,
                        blog: Optional[str] = None) -> Any:
    """Update an organization.

    Args:
        org: Organization name
        billing_email: Billing email
        company: Company name
        email: Email
        location: Location
        name: Display name
        description: Description
        default_repository_permission: Default repo permission (read, write, admin, none)
        members_can_create_repositories: Whether members can create repos
        blog: Blog URL
    """
    data = {}
    if billing_email is not None:
        data["billing_email"] = billing_email
    if company is not None:
        data["company"] = company
    if email is not None:
        data["email"] = email
    if location is not None:
        data["location"] = location
    if name is not None:
        data["name"] = name
    if description is not None:
        data["description"] = description
    if default_repository_permission is not None:
        data["default_repository_permission"] = default_repository_permission
    if members_can_create_repositories is not None:
        data["members_can_create_repositories"] = members_can_create_repositories
    if blog is not None:
        data["blog"] = blog
    return github_patch(f"/orgs/{org}", data)


def list_organizations(since: Optional[int] = None, per_page: int = 30) -> Any:
    """List organizations.

    Args:
        since: Organization ID to start after
        per_page: Results per page (max 100)
    """
    params = {"per_page": per_page}
    if since is not None:
        params["since"] = since
    return github_get("/organizations", params)


def list_user_organizations(per_page: int = 30, page: int = 1) -> Any:
    """List organizations for the authenticated user.

    Args:
        per_page: Results per page (max 100)
        page: Page number
    """
    return github_get("/user/orgs", {"per_page": per_page, "page": page})


def list_org_members(org: str, filter: str = "all", role: str = "all",
                     per_page: int = 30, page: int = 1) -> Any:
    """List organization members.

    Args:
        org: Organization name
        filter: Filter by 2FA status (2fa_disabled, all)
        role: Filter by role (all, admin, member)
        per_page: Results per page (max 100)
        page: Page number
    """
    return github_get(f"/orgs/{org}/members",
                      {"filter": filter, "role": role, "per_page": per_page, "page": page})
