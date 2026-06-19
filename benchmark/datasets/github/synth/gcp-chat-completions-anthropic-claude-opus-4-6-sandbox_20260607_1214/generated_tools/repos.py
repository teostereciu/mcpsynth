"""GitHub Repositories tools."""

from typing import Any, Optional
from generated_tools.github_client import github_get, github_post, github_patch, github_put, github_delete


def get_repository(owner: str, repo: str) -> Any:
    """Get a repository.

    Args:
        owner: Repository owner
        repo: Repository name
    """
    return github_get(f"/repos/{owner}/{repo}")


def create_repository(name: str, description: Optional[str] = None, private: bool = False,
                      auto_init: bool = False, gitignore_template: Optional[str] = None,
                      license_template: Optional[str] = None, homepage: Optional[str] = None,
                      has_issues: bool = True, has_projects: bool = True, has_wiki: bool = True) -> Any:
    """Create a repository for the authenticated user.

    Args:
        name: Repository name
        description: Repository description
        private: Whether the repository is private
        auto_init: Whether to create an initial commit with README
        gitignore_template: Gitignore template name
        license_template: License template keyword
        homepage: Homepage URL
        has_issues: Enable issues
        has_projects: Enable projects
        has_wiki: Enable wiki
    """
    data = {"name": name, "private": private, "auto_init": auto_init,
            "has_issues": has_issues, "has_projects": has_projects, "has_wiki": has_wiki}
    if description:
        data["description"] = description
    if gitignore_template:
        data["gitignore_template"] = gitignore_template
    if license_template:
        data["license_template"] = license_template
    if homepage:
        data["homepage"] = homepage
    return github_post("/user/repos", data)


def create_org_repository(org: str, name: str, description: Optional[str] = None,
                          private: bool = False, auto_init: bool = False,
                          gitignore_template: Optional[str] = None,
                          license_template: Optional[str] = None) -> Any:
    """Create a repository in an organization.

    Args:
        org: Organization name
        name: Repository name
        description: Repository description
        private: Whether the repository is private
        auto_init: Whether to create an initial commit with README
        gitignore_template: Gitignore template name
        license_template: License template keyword
    """
    data = {"name": name, "private": private, "auto_init": auto_init}
    if description:
        data["description"] = description
    if gitignore_template:
        data["gitignore_template"] = gitignore_template
    if license_template:
        data["license_template"] = license_template
    return github_post(f"/orgs/{org}/repos", data)


def update_repository(owner: str, repo: str, name: Optional[str] = None,
                      description: Optional[str] = None, homepage: Optional[str] = None,
                      private: Optional[bool] = None, has_issues: Optional[bool] = None,
                      has_projects: Optional[bool] = None, has_wiki: Optional[bool] = None,
                      default_branch: Optional[str] = None, archived: Optional[bool] = None,
                      allow_squash_merge: Optional[bool] = None,
                      allow_merge_commit: Optional[bool] = None,
                      allow_rebase_merge: Optional[bool] = None,
                      delete_branch_on_merge: Optional[bool] = None) -> Any:
    """Update a repository.

    Args:
        owner: Repository owner
        repo: Repository name
        name: New repository name
        description: New description
        homepage: New homepage URL
        private: Whether the repository is private
        has_issues: Enable issues
        has_projects: Enable projects
        has_wiki: Enable wiki
        default_branch: Default branch name
        archived: Whether to archive
        allow_squash_merge: Allow squash merging
        allow_merge_commit: Allow merge commits
        allow_rebase_merge: Allow rebase merging
        delete_branch_on_merge: Auto-delete head branches after merge
    """
    data = {}
    if name is not None:
        data["name"] = name
    if description is not None:
        data["description"] = description
    if homepage is not None:
        data["homepage"] = homepage
    if private is not None:
        data["private"] = private
    if has_issues is not None:
        data["has_issues"] = has_issues
    if has_projects is not None:
        data["has_projects"] = has_projects
    if has_wiki is not None:
        data["has_wiki"] = has_wiki
    if default_branch is not None:
        data["default_branch"] = default_branch
    if archived is not None:
        data["archived"] = archived
    if allow_squash_merge is not None:
        data["allow_squash_merge"] = allow_squash_merge
    if allow_merge_commit is not None:
        data["allow_merge_commit"] = allow_merge_commit
    if allow_rebase_merge is not None:
        data["allow_rebase_merge"] = allow_rebase_merge
    if delete_branch_on_merge is not None:
        data["delete_branch_on_merge"] = delete_branch_on_merge
    return github_patch(f"/repos/{owner}/{repo}", data)


def delete_repository(owner: str, repo: str) -> Any:
    """Delete a repository.

    Args:
        owner: Repository owner
        repo: Repository name
    """
    return github_delete(f"/repos/{owner}/{repo}")


def list_organization_repositories(org: str, type: str = "all", sort: str = "created",
                                   direction: str = "desc", per_page: int = 30, page: int = 1) -> Any:
    """List repositories for an organization.

    Args:
        org: Organization name
        type: Type filter (all, public, private, forks, sources, member)
        sort: Sort by (created, updated, pushed, full_name)
        direction: Sort direction (asc, desc)
        per_page: Results per page (max 100)
        page: Page number
    """
    return github_get(f"/orgs/{org}/repos",
                      {"type": type, "sort": sort, "direction": direction,
                       "per_page": per_page, "page": page})


def list_user_repositories(username: str, type: str = "owner", sort: str = "full_name",
                           direction: str = "asc", per_page: int = 30, page: int = 1) -> Any:
    """List repositories for a user.

    Args:
        username: GitHub username
        type: Type filter (all, owner, member)
        sort: Sort by (created, updated, pushed, full_name)
        direction: Sort direction (asc, desc)
        per_page: Results per page (max 100)
        page: Page number
    """
    return github_get(f"/users/{username}/repos",
                      {"type": type, "sort": sort, "direction": direction,
                       "per_page": per_page, "page": page})


def list_repositories_for_authenticated_user(visibility: str = "all", sort: str = "full_name",
                                             direction: str = "asc", per_page: int = 30,
                                             page: int = 1) -> Any:
    """List repositories for the authenticated user.

    Args:
        visibility: Visibility filter (all, public, private)
        sort: Sort by (created, updated, pushed, full_name)
        direction: Sort direction (asc, desc)
        per_page: Results per page (max 100)
        page: Page number
    """
    return github_get("/user/repos",
                      {"visibility": visibility, "sort": sort, "direction": direction,
                       "per_page": per_page, "page": page})


def list_forks(owner: str, repo: str, sort: str = "newest", per_page: int = 30, page: int = 1) -> Any:
    """List forks of a repository.

    Args:
        owner: Repository owner
        repo: Repository name
        sort: Sort by (newest, oldest, stargazers, watchers)
        per_page: Results per page (max 100)
        page: Page number
    """
    return github_get(f"/repos/{owner}/{repo}/forks",
                      {"sort": sort, "per_page": per_page, "page": page})


def create_fork(owner: str, repo: str, organization: Optional[str] = None,
                name: Optional[str] = None, default_branch_only: bool = False) -> Any:
    """Create a fork.

    Args:
        owner: Repository owner
        repo: Repository name
        organization: Organization to fork into
        name: Name for the forked repository
        default_branch_only: Only fork the default branch
    """
    data = {"default_branch_only": default_branch_only}
    if organization:
        data["organization"] = organization
    if name:
        data["name"] = name
    return github_post(f"/repos/{owner}/{repo}/forks", data)


def get_repository_content(owner: str, repo: str, path: str, ref: Optional[str] = None) -> Any:
    """Get repository content (file, directory, symlink, or submodule).

    Args:
        owner: Repository owner
        repo: Repository name
        path: Path to content
        ref: Git reference (branch, tag, or SHA)
    """
    params = {}
    if ref:
        params["ref"] = ref
    return github_get(f"/repos/{owner}/{repo}/contents/{path}", params)


def create_or_update_file(owner: str, repo: str, path: str, message: str, content: str,
                          sha: Optional[str] = None, branch: Optional[str] = None,
                          committer_name: Optional[str] = None,
                          committer_email: Optional[str] = None) -> Any:
    """Create or update a file in a repository.

    Args:
        owner: Repository owner
        repo: Repository name
        path: File path
        message: Commit message
        content: File content (Base64 encoded)
        sha: SHA of the file being replaced (required for updates)
        branch: Branch name (defaults to default branch)
        committer_name: Committer name
        committer_email: Committer email
    """
    data = {"message": message, "content": content}
    if sha:
        data["sha"] = sha
    if branch:
        data["branch"] = branch
    if committer_name and committer_email:
        data["committer"] = {"name": committer_name, "email": committer_email}
    return github_put(f"/repos/{owner}/{repo}/contents/{path}", data)


def delete_file(owner: str, repo: str, path: str, message: str, sha: str,
                branch: Optional[str] = None) -> Any:
    """Delete a file in a repository.

    Args:
        owner: Repository owner
        repo: Repository name
        path: File path
        message: Commit message
        sha: SHA of the file to delete
        branch: Branch name
    """
    data = {"message": message, "sha": sha}
    if branch:
        data["branch"] = branch
    return github_delete(f"/repos/{owner}/{repo}/contents/{path}", data)


def get_repository_readme(owner: str, repo: str, ref: Optional[str] = None) -> Any:
    """Get the README for a repository.

    Args:
        owner: Repository owner
        repo: Repository name
        ref: Git reference (branch, tag, or SHA)
    """
    params = {}
    if ref:
        params["ref"] = ref
    return github_get(f"/repos/{owner}/{repo}/readme", params)


def list_repository_tags(owner: str, repo: str, per_page: int = 30, page: int = 1) -> Any:
    """List repository tags.

    Args:
        owner: Repository owner
        repo: Repository name
        per_page: Results per page (max 100)
        page: Page number
    """
    return github_get(f"/repos/{owner}/{repo}/tags", {"per_page": per_page, "page": page})


def list_repository_contributors(owner: str, repo: str, anon: Optional[str] = None,
                                 per_page: int = 30, page: int = 1) -> Any:
    """List repository contributors.

    Args:
        owner: Repository owner
        repo: Repository name
        anon: Set to '1' or 'true' to include anonymous contributors
        per_page: Results per page (max 100)
        page: Page number
    """
    params = {"per_page": per_page, "page": page}
    if anon:
        params["anon"] = anon
    return github_get(f"/repos/{owner}/{repo}/contributors", params)


def list_repository_languages(owner: str, repo: str) -> Any:
    """List languages for a repository.

    Args:
        owner: Repository owner
        repo: Repository name
    """
    return github_get(f"/repos/{owner}/{repo}/languages")


def get_all_repository_topics(owner: str, repo: str, per_page: int = 30, page: int = 1) -> Any:
    """Get all repository topics.

    Args:
        owner: Repository owner
        repo: Repository name
        per_page: Results per page (max 100)
        page: Page number
    """
    return github_get(f"/repos/{owner}/{repo}/topics", {"per_page": per_page, "page": page})


def replace_all_repository_topics(owner: str, repo: str, names: list) -> Any:
    """Replace all repository topics.

    Args:
        owner: Repository owner
        repo: Repository name
        names: List of topic names
    """
    return github_put(f"/repos/{owner}/{repo}/topics", {"names": names})


def list_repository_teams(owner: str, repo: str, per_page: int = 30, page: int = 1) -> Any:
    """List repository teams.

    Args:
        owner: Repository owner
        repo: Repository name
        per_page: Results per page (max 100)
        page: Page number
    """
    return github_get(f"/repos/{owner}/{repo}/teams", {"per_page": per_page, "page": page})


def list_repository_collaborators(owner: str, repo: str, affiliation: str = "all",
                                  permission: Optional[str] = None,
                                  per_page: int = 30, page: int = 1) -> Any:
    """List repository collaborators.

    Args:
        owner: Repository owner
        repo: Repository name
        affiliation: Filter by affiliation (outside, direct, all)
        permission: Filter by permission (pull, triage, push, maintain, admin)
        per_page: Results per page (max 100)
        page: Page number
    """
    params = {"affiliation": affiliation, "per_page": per_page, "page": page}
    if permission:
        params["permission"] = permission
    return github_get(f"/repos/{owner}/{repo}/collaborators", params)


def add_repository_collaborator(owner: str, repo: str, username: str,
                                permission: str = "push") -> Any:
    """Add a repository collaborator.

    Args:
        owner: Repository owner
        repo: Repository name
        username: Username to add
        permission: Permission level (pull, triage, push, maintain, admin)
    """
    return github_put(f"/repos/{owner}/{repo}/collaborators/{username}", {"permission": permission})


def remove_repository_collaborator(owner: str, repo: str, username: str) -> Any:
    """Remove a repository collaborator.

    Args:
        owner: Repository owner
        repo: Repository name
        username: Username to remove
    """
    return github_delete(f"/repos/{owner}/{repo}/collaborators/{username}")


def get_repository_permissions_for_user(owner: str, repo: str, username: str) -> Any:
    """Get repository permissions for a user.

    Args:
        owner: Repository owner
        repo: Repository name
        username: Username to check
    """
    return github_get(f"/repos/{owner}/{repo}/collaborators/{username}/permission")
