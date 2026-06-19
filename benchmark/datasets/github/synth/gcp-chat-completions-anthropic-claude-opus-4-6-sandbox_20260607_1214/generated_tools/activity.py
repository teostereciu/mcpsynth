"""GitHub Activity tools (starring, watching)."""

from typing import Any, Optional
from generated_tools.github_client import github_get, github_put, github_delete


def list_stargazers(owner: str, repo: str, per_page: int = 30, page: int = 1) -> Any:
    """List stargazers for a repository.

    Args:
        owner: Repository owner
        repo: Repository name
        per_page: Results per page (max 100)
        page: Page number
    """
    return github_get(f"/repos/{owner}/{repo}/stargazers", {"per_page": per_page, "page": page})


def list_starred_repositories(username: Optional[str] = None, sort: str = "created",
                              direction: str = "desc", per_page: int = 30, page: int = 1) -> Any:
    """List repositories starred by a user.

    Args:
        username: GitHub username (if None, lists authenticated user's starred repos)
        sort: Sort by (created, updated)
        direction: Sort direction (asc, desc)
        per_page: Results per page (max 100)
        page: Page number
    """
    params = {"sort": sort, "direction": direction, "per_page": per_page, "page": page}
    if username:
        return github_get(f"/users/{username}/starred", params)
    return github_get("/user/starred", params)


def check_starred(owner: str, repo: str) -> Any:
    """Check if a repository is starred by the authenticated user.

    Args:
        owner: Repository owner
        repo: Repository name
    """
    return github_get(f"/user/starred/{owner}/{repo}")


def star_repository(owner: str, repo: str) -> Any:
    """Star a repository for the authenticated user.

    Args:
        owner: Repository owner
        repo: Repository name
    """
    return github_put(f"/user/starred/{owner}/{repo}")


def unstar_repository(owner: str, repo: str) -> Any:
    """Unstar a repository for the authenticated user.

    Args:
        owner: Repository owner
        repo: Repository name
    """
    return github_delete(f"/user/starred/{owner}/{repo}")


def list_watchers(owner: str, repo: str, per_page: int = 30, page: int = 1) -> Any:
    """List watchers for a repository.

    Args:
        owner: Repository owner
        repo: Repository name
        per_page: Results per page (max 100)
        page: Page number
    """
    return github_get(f"/repos/{owner}/{repo}/subscribers", {"per_page": per_page, "page": page})


def get_repository_subscription(owner: str, repo: str) -> Any:
    """Get a repository subscription (watching status).

    Args:
        owner: Repository owner
        repo: Repository name
    """
    return github_get(f"/repos/{owner}/{repo}/subscription")


def set_repository_subscription(owner: str, repo: str, subscribed: bool = True,
                                ignored: bool = False) -> Any:
    """Set a repository subscription (watch/unwatch).

    Args:
        owner: Repository owner
        repo: Repository name
        subscribed: Whether to subscribe
        ignored: Whether to ignore notifications
    """
    return github_put(f"/repos/{owner}/{repo}/subscription",
                      {"subscribed": subscribed, "ignored": ignored})


def delete_repository_subscription(owner: str, repo: str) -> Any:
    """Delete a repository subscription (stop watching).

    Args:
        owner: Repository owner
        repo: Repository name
    """
    return github_delete(f"/repos/{owner}/{repo}/subscription")
