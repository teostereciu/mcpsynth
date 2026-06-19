"""GitHub Search tools."""

from typing import Any, Optional
from generated_tools.github_client import github_get


def search_code(q: str, sort: Optional[str] = None, order: str = "desc",
                per_page: int = 30, page: int = 1) -> Any:
    """Search code across GitHub repositories.

    Args:
        q: Search query (see GitHub search syntax)
        sort: Sort field (indexed)
        order: Sort order (asc, desc)
        per_page: Results per page (max 100)
        page: Page number
    """
    params = {"q": q, "order": order, "per_page": per_page, "page": page}
    if sort:
        params["sort"] = sort
    return github_get("/search/code", params)


def search_commits(q: str, sort: Optional[str] = None, order: str = "desc",
                   per_page: int = 30, page: int = 1) -> Any:
    """Search commits across GitHub.

    Args:
        q: Search query
        sort: Sort field (author-date, committer-date)
        order: Sort order (asc, desc)
        per_page: Results per page (max 100)
        page: Page number
    """
    params = {"q": q, "order": order, "per_page": per_page, "page": page}
    if sort:
        params["sort"] = sort
    return github_get("/search/commits", params)


def search_issues_and_pull_requests(q: str, sort: Optional[str] = None, order: str = "desc",
                                    per_page: int = 30, page: int = 1) -> Any:
    """Search issues and pull requests.

    Args:
        q: Search query (e.g. 'repo:owner/name is:issue state:open')
        sort: Sort field (comments, reactions, reactions-+1, reactions--1, reactions-smile, reactions-thinking_face, reactions-heart, reactions-tada, interactions, created, updated)
        order: Sort order (asc, desc)
        per_page: Results per page (max 100)
        page: Page number
    """
    params = {"q": q, "order": order, "per_page": per_page, "page": page}
    if sort:
        params["sort"] = sort
    return github_get("/search/issues", params)


def search_repositories(q: str, sort: Optional[str] = None, order: str = "desc",
                        per_page: int = 30, page: int = 1) -> Any:
    """Search repositories.

    Args:
        q: Search query (e.g. 'language:python stars:>100')
        sort: Sort field (stars, forks, help-wanted-issues, updated)
        order: Sort order (asc, desc)
        per_page: Results per page (max 100)
        page: Page number
    """
    params = {"q": q, "order": order, "per_page": per_page, "page": page}
    if sort:
        params["sort"] = sort
    return github_get("/search/repositories", params)


def search_topics(q: str, per_page: int = 30, page: int = 1) -> Any:
    """Search topics.

    Args:
        q: Search query
        per_page: Results per page (max 100)
        page: Page number
    """
    return github_get("/search/topics", {"q": q, "per_page": per_page, "page": page})


def search_users(q: str, sort: Optional[str] = None, order: str = "desc",
                 per_page: int = 30, page: int = 1) -> Any:
    """Search users.

    Args:
        q: Search query
        sort: Sort field (followers, repositories, joined)
        order: Sort order (asc, desc)
        per_page: Results per page (max 100)
        page: Page number
    """
    params = {"q": q, "order": order, "per_page": per_page, "page": page}
    if sort:
        params["sort"] = sort
    return github_get("/search/users", params)


def search_labels(q: str, repository_id: int, sort: Optional[str] = None, order: str = "desc",
                  per_page: int = 30, page: int = 1) -> Any:
    """Search labels in a repository.

    Args:
        q: Search query
        repository_id: Repository ID to search in
        sort: Sort field (created, updated)
        order: Sort order (asc, desc)
        per_page: Results per page (max 100)
        page: Page number
    """
    params = {"q": q, "repository_id": repository_id, "order": order,
              "per_page": per_page, "page": page}
    if sort:
        params["sort"] = sort
    return github_get("/search/labels", params)
