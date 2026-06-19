"""GitHub Users tools."""

from typing import Any, Optional
from generated_tools.github_client import github_get, github_patch


def get_authenticated_user() -> Any:
    """Get the authenticated user."""
    return github_get("/user")


def update_authenticated_user(name: Optional[str] = None, email: Optional[str] = None,
                              blog: Optional[str] = None, twitter_username: Optional[str] = None,
                              company: Optional[str] = None, location: Optional[str] = None,
                              hireable: Optional[bool] = None, bio: Optional[str] = None) -> Any:
    """Update the authenticated user.

    Args:
        name: Display name
        email: Email address
        blog: Blog URL
        twitter_username: Twitter username
        company: Company name
        location: Location
        hireable: Whether hireable
        bio: Bio text
    """
    data = {}
    if name is not None:
        data["name"] = name
    if email is not None:
        data["email"] = email
    if blog is not None:
        data["blog"] = blog
    if twitter_username is not None:
        data["twitter_username"] = twitter_username
    if company is not None:
        data["company"] = company
    if location is not None:
        data["location"] = location
    if hireable is not None:
        data["hireable"] = hireable
    if bio is not None:
        data["bio"] = bio
    return github_patch("/user", data)


def get_user(username: str) -> Any:
    """Get a user by username.

    Args:
        username: GitHub username
    """
    return github_get(f"/users/{username}")


def list_users(since: Optional[int] = None, per_page: int = 30) -> Any:
    """List users.

    Args:
        since: User ID to start after
        per_page: Results per page (max 100)
    """
    params = {"per_page": per_page}
    if since is not None:
        params["since"] = since
    return github_get("/users", params)


def list_followers(username: Optional[str] = None, per_page: int = 30, page: int = 1) -> Any:
    """List followers of a user.

    Args:
        username: GitHub username (if None, lists authenticated user's followers)
        per_page: Results per page (max 100)
        page: Page number
    """
    if username:
        return github_get(f"/users/{username}/followers", {"per_page": per_page, "page": page})
    return github_get("/user/followers", {"per_page": per_page, "page": page})


def list_following(username: Optional[str] = None, per_page: int = 30, page: int = 1) -> Any:
    """List users followed by a user.

    Args:
        username: GitHub username (if None, lists authenticated user's following)
        per_page: Results per page (max 100)
        page: Page number
    """
    if username:
        return github_get(f"/users/{username}/following", {"per_page": per_page, "page": page})
    return github_get("/user/following", {"per_page": per_page, "page": page})
