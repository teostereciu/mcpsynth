import os
from typing import Any, Dict

from mcp.server.fastmcp import FastMCP

from generated_tools.pulls import (
    create_pull_request,
    get_pull_request,
    list_pull_requests,
    merge_pull_request,
    update_pull_request,
)
from generated_tools.repos import (
    create_org_repository,
    create_user_repository,
    delete_repository,
    fork_repository,
    get_repository,
    list_org_repositories,
    update_repository,
)
from generated_tools.search import (
    search_code,
    search_commits,
    search_issues_and_pull_requests,
    search_repositories,
    search_users,
)


mcp = FastMCP("github-rest")


def _split_repo(full_name: str) -> Dict[str, str]:
    if not full_name or "/" not in full_name:
        return {"error": "repo must be in 'owner/repo' format"}
    owner, repo = full_name.split("/", 1)
    return {"owner": owner, "repo": repo}


@mcp.tool()
def github_get_repository(owner: str = None, repo: str = None, full_name: str = None) -> Any:
    """Get a repository.

    Source: docs/api_repos-repos.md (GET /repos/{owner}/{repo})
    """
    if full_name and (not owner or not repo):
        parts = _split_repo(full_name)
        if "error" in parts:
            return parts
        owner, repo = parts["owner"], parts["repo"]
    if not owner or not repo:
        test_repo = os.getenv("GITHUB_TEST_REPO")
        if test_repo and (not owner or not repo):
            parts = _split_repo(test_repo)
            if "error" not in parts:
                owner, repo = parts["owner"], parts["repo"]
    if not owner or not repo:
        return {"error": "owner and repo are required (or set full_name / GITHUB_TEST_REPO)"}
    return get_repository(owner, repo)


@mcp.tool()
def github_list_org_repositories(org: str, type: str = "all", sort: str = "created", direction: str = None, per_page: int = 30, page: int = 1) -> Any:
    """List repositories for an organization.

    Source: docs/api_repos-repos.md (GET /orgs/{org}/repos)
    """
    return list_org_repositories(org, type=type, sort=sort, direction=direction, per_page=per_page, page=page)


@mcp.tool()
def github_create_org_repository(org: str, name: str, description: str = None, homepage: str = None, private: bool = False, visibility: str = None) -> Any:
    """Create a repository in an organization.

    Source: docs/api_repos-repos.md (POST /orgs/{org}/repos)
    """
    return create_org_repository(org, name=name, description=description, homepage=homepage, private=private, visibility=visibility)


@mcp.tool()
def github_create_user_repository(name: str, description: str = None, homepage: str = None, private: bool = False, visibility: str = None) -> Any:
    """Create a repository for the authenticated user.

    Source: docs/api_repos-repos.md (POST /user/repos)
    """
    return create_user_repository(name=name, description=description, homepage=homepage, private=private, visibility=visibility)


@mcp.tool()
def github_update_repository(owner: str, repo: str, description: str = None, homepage: str = None, default_branch: str = None) -> Any:
    """Update repository settings.

    Source: docs/api_about-the-rest-api-breaking-changes.md (PATCH /repos/{owner}/{repo})
    """
    return update_repository(owner, repo, description=description, homepage=homepage, default_branch=default_branch)


@mcp.tool()
def github_delete_repository(owner: str, repo: str) -> Any:
    """Delete a repository.

    Source: docs/api_repos-repos.md (DELETE /repos/{owner}/{repo})
    """
    return delete_repository(owner, repo)


@mcp.tool()
def github_fork_repository(owner: str, repo: str, organization: str = None, name: str = None) -> Any:
    """Fork a repository.

    Source: docs/api_about-the-rest-api-breaking-changes.md (POST /repos/{owner}/{repo}/forks)
    """
    return fork_repository(owner, repo, organization=organization, name=name)


@mcp.tool()
def github_list_pull_requests(owner: str = None, repo: str = None, full_name: str = None, state: str = "open", base: str = None, head: str = None, sort: str = "created", direction: str = None, per_page: int = 30, page: int = 1) -> Any:
    """List pull requests.

    Source: docs/api_pulls-pulls.md (GET /repos/{owner}/{repo}/pulls)
    """
    if full_name and (not owner or not repo):
        parts = _split_repo(full_name)
        if "error" in parts:
            return parts
        owner, repo = parts["owner"], parts["repo"]
    if not owner or not repo:
        test_repo = os.getenv("GITHUB_TEST_REPO")
        if test_repo:
            parts = _split_repo(test_repo)
            if "error" not in parts:
                owner, repo = parts["owner"], parts["repo"]
    if not owner or not repo:
        return {"error": "owner and repo are required (or set full_name / GITHUB_TEST_REPO)"}
    return list_pull_requests(owner, repo, state=state, base=base, head=head, sort=sort, direction=direction, per_page=per_page, page=page)


@mcp.tool()
def github_get_pull_request(owner: str, repo: str, pull_number: int) -> Any:
    """Get a pull request.

    Source: docs/api_about-the-rest-api-breaking-changes.md (GET /repos/{owner}/{repo}/pulls/{pull_number})
    """
    return get_pull_request(owner, repo, pull_number)


@mcp.tool()
def github_create_pull_request(owner: str, repo: str, title: str, head: str, base: str, body: str = None, draft: bool = None) -> Any:
    """Create a pull request.

    Source: docs/api_about-the-rest-api-breaking-changes.md (POST /repos/{owner}/{repo}/pulls)
    """
    return create_pull_request(owner, repo, title=title, head=head, base=base, body=body, draft=draft)


@mcp.tool()
def github_update_pull_request(owner: str, repo: str, pull_number: int, title: str = None, body: str = None, state: str = None, base: str = None) -> Any:
    """Update a pull request.

    Source: docs/api_about-the-rest-api-breaking-changes.md (PATCH /repos/{owner}/{repo}/pulls/{pull_number})
    """
    return update_pull_request(owner, repo, pull_number, title=title, body=body, state=state, base=base)


@mcp.tool()
def github_merge_pull_request(owner: str, repo: str, pull_number: int, merge_method: str = None, commit_title: str = None, commit_message: str = None, sha: str = None) -> Any:
    """Merge a pull request.

    Source: docs/api_pulls-pulls.md (PUT /repos/{owner}/{repo}/pulls/{pull_number}/merge)
    """
    return merge_pull_request(owner, repo, pull_number, merge_method=merge_method, commit_title=commit_title, commit_message=commit_message, sha=sha)


@mcp.tool()
def github_search_code(q: str, per_page: int = 30, page: int = 1) -> Any:
    """Search code.

    Source: docs/api_search-search.md (GET /search/code)
    """
    return search_code(q=q, per_page=per_page, page=page)


@mcp.tool()
def github_search_issues_and_pull_requests(q: str, per_page: int = 30, page: int = 1) -> Any:
    """Search issues and pull requests.

    Source: docs/api_about-the-rest-api-breaking-changes.md (GET /search/issues)
    """
    return search_issues_and_pull_requests(q=q, per_page=per_page, page=page)


@mcp.tool()
def github_search_repositories(q: str, per_page: int = 30, page: int = 1) -> Any:
    """Search repositories.

    Source: docs/api_search-search.md (GET /search/repositories)
    """
    return search_repositories(q=q, per_page=per_page, page=page)


@mcp.tool()
def github_search_users(q: str, per_page: int = 30, page: int = 1) -> Any:
    """Search users.

    Source: docs/api_search-search.md (GET /search/users)
    """
    return search_users(q=q, per_page=per_page, page=page)


@mcp.tool()
def github_search_commits(q: str, per_page: int = 30, page: int = 1, text_match: bool = False) -> Any:
    """Search commits.

    Source: docs/api_search-search.md (GET /search/commits)
    """
    return search_commits(q=q, per_page=per_page, page=page, text_match=text_match)


if __name__ == "__main__":
    mcp.run()
