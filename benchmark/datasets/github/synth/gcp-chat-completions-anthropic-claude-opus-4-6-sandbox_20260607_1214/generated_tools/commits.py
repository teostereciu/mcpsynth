"""GitHub Commits tools."""

from typing import Any, Optional
from generated_tools.github_client import github_get, github_post


def list_commits(owner: str, repo: str, sha: Optional[str] = None, path: Optional[str] = None,
                 author: Optional[str] = None, committer: Optional[str] = None,
                 since: Optional[str] = None, until: Optional[str] = None,
                 per_page: int = 30, page: int = 1) -> Any:
    """List commits for a repository.

    Args:
        owner: Repository owner
        repo: Repository name
        sha: SHA or branch to start listing from
        path: Only commits containing this file path
        author: GitHub username or email to filter by author
        committer: GitHub username or email to filter by committer
        since: Only commits after this ISO 8601 date
        until: Only commits before this ISO 8601 date
        per_page: Results per page (max 100)
        page: Page number
    """
    params = {"per_page": per_page, "page": page}
    if sha:
        params["sha"] = sha
    if path:
        params["path"] = path
    if author:
        params["author"] = author
    if committer:
        params["committer"] = committer
    if since:
        params["since"] = since
    if until:
        params["until"] = until
    return github_get(f"/repos/{owner}/{repo}/commits", params)


def get_commit(owner: str, repo: str, ref: str) -> Any:
    """Get a commit.

    Args:
        owner: Repository owner
        repo: Repository name
        ref: Commit SHA, branch name, or tag name
    """
    return github_get(f"/repos/{owner}/{repo}/commits/{ref}")


def compare_commits(owner: str, repo: str, basehead: str, per_page: int = 30, page: int = 1) -> Any:
    """Compare two commits.

    Args:
        owner: Repository owner
        repo: Repository name
        basehead: Base and head to compare in format 'base...head'
        per_page: Results per page (max 100)
        page: Page number
    """
    return github_get(f"/repos/{owner}/{repo}/compare/{basehead}", {"per_page": per_page, "page": page})


def list_branches_for_head_commit(owner: str, repo: str, commit_sha: str) -> Any:
    """List branches for a HEAD commit.

    Args:
        owner: Repository owner
        repo: Repository name
        commit_sha: Commit SHA
    """
    return github_get(f"/repos/{owner}/{repo}/commits/{commit_sha}/branches-where-head")


def list_pull_requests_for_commit(owner: str, repo: str, commit_sha: str,
                                  per_page: int = 30, page: int = 1) -> Any:
    """List pull requests associated with a commit.

    Args:
        owner: Repository owner
        repo: Repository name
        commit_sha: Commit SHA
        per_page: Results per page (max 100)
        page: Page number
    """
    return github_get(f"/repos/{owner}/{repo}/commits/{commit_sha}/pulls",
                      {"per_page": per_page, "page": page})


def get_combined_status(owner: str, repo: str, ref: str, per_page: int = 30, page: int = 1) -> Any:
    """Get the combined status for a specific reference.

    Args:
        owner: Repository owner
        repo: Repository name
        ref: Commit SHA, branch name, or tag name
        per_page: Results per page (max 100)
        page: Page number
    """
    return github_get(f"/repos/{owner}/{repo}/commits/{ref}/status",
                      {"per_page": per_page, "page": page})


def list_commit_statuses(owner: str, repo: str, ref: str, per_page: int = 30, page: int = 1) -> Any:
    """List commit statuses for a reference.

    Args:
        owner: Repository owner
        repo: Repository name
        ref: Commit SHA, branch name, or tag name
        per_page: Results per page (max 100)
        page: Page number
    """
    return github_get(f"/repos/{owner}/{repo}/commits/{ref}/statuses",
                      {"per_page": per_page, "page": page})


def create_commit_status(owner: str, repo: str, sha: str, state: str,
                         target_url: Optional[str] = None, description: Optional[str] = None,
                         context: str = "default") -> Any:
    """Create a commit status.

    Args:
        owner: Repository owner
        repo: Repository name
        sha: Commit SHA
        state: Status state (error, failure, pending, success)
        target_url: URL to associate with the status
        description: Short description
        context: Status context identifier
    """
    data = {"state": state, "context": context}
    if target_url:
        data["target_url"] = target_url
    if description:
        data["description"] = description
    return github_post(f"/repos/{owner}/{repo}/statuses/{sha}", data)
