"""MCP tools for GitHub Repositories (CRUD, forks, branches, commits, contents, tags)."""
from mcp.server.fastmcp import FastMCP
from .client import gh_get, gh_post, gh_patch, gh_delete, gh_put
import base64

def register(mcp: FastMCP):

    # --- Repository CRUD ---

    @mcp.tool()
    def get_repo(owner: str, repo: str) -> dict | list:
        """Get a repository by owner and name."""
        return gh_get(f"/repos/{owner}/{repo}")

    @mcp.tool()
    def list_user_repos(
        username: str = "",
        type: str = "owner",
        sort: str = "updated",
        direction: str = "desc",
        per_page: int = 30,
        page: int = 1,
    ) -> dict | list:
        """List repositories for a user. Leave username empty for authenticated user."""
        params = {"type": type, "sort": sort, "direction": direction,
                  "per_page": per_page, "page": page}
        if username:
            return gh_get(f"/users/{username}/repos", params=params)
        return gh_get("/user/repos", params=params)

    @mcp.tool()
    def list_org_repos(
        org: str,
        type: str = "all",
        sort: str = "updated",
        per_page: int = 30,
        page: int = 1,
    ) -> dict | list:
        """List repositories for an organization."""
        return gh_get(f"/orgs/{org}/repos",
                      params={"type": type, "sort": sort, "per_page": per_page, "page": page})

    @mcp.tool()
    def create_user_repo(
        name: str,
        description: str = "",
        private: bool = False,
        auto_init: bool = False,
        gitignore_template: str = "",
        license_template: str = "",
        has_issues: bool = True,
        has_projects: bool = True,
        has_wiki: bool = True,
    ) -> dict | list:
        """Create a repository for the authenticated user."""
        payload: dict = {"name": name, "private": private, "auto_init": auto_init,
                         "has_issues": has_issues, "has_projects": has_projects, "has_wiki": has_wiki}
        if description:
            payload["description"] = description
        if gitignore_template:
            payload["gitignore_template"] = gitignore_template
        if license_template:
            payload["license_template"] = license_template
        return gh_post("/user/repos", json=payload)

    @mcp.tool()
    def create_org_repo(
        org: str,
        name: str,
        description: str = "",
        private: bool = False,
        auto_init: bool = False,
        has_issues: bool = True,
        has_projects: bool = True,
        has_wiki: bool = True,
    ) -> dict | list:
        """Create a repository for an organization."""
        payload: dict = {"name": name, "private": private, "auto_init": auto_init,
                         "has_issues": has_issues, "has_projects": has_projects, "has_wiki": has_wiki}
        if description:
            payload["description"] = description
        return gh_post(f"/orgs/{org}/repos", json=payload)

    @mcp.tool()
    def update_repo(
        owner: str,
        repo: str,
        name: str = "",
        description: str = "",
        homepage: str = "",
        private: bool | None = None,
        has_issues: bool | None = None,
        has_projects: bool | None = None,
        has_wiki: bool | None = None,
        default_branch: str = "",
        archived: bool | None = None,
    ) -> dict | list:
        """Update repository settings."""
        payload: dict = {}
        if name:
            payload["name"] = name
        if description:
            payload["description"] = description
        if homepage:
            payload["homepage"] = homepage
        if private is not None:
            payload["private"] = private
        if has_issues is not None:
            payload["has_issues"] = has_issues
        if has_projects is not None:
            payload["has_projects"] = has_projects
        if has_wiki is not None:
            payload["has_wiki"] = has_wiki
        if default_branch:
            payload["default_branch"] = default_branch
        if archived is not None:
            payload["archived"] = archived
        return gh_patch(f"/repos/{owner}/{repo}", json=payload)

    @mcp.tool()
    def delete_repo(owner: str, repo: str) -> dict | list:
        """Delete a repository. This is irreversible."""
        return gh_delete(f"/repos/{owner}/{repo}")

    @mcp.tool()
    def fork_repo(owner: str, repo: str, organization: str = "", name: str = "") -> dict | list:
        """Fork a repository."""
        payload: dict = {}
        if organization:
            payload["organization"] = organization
        if name:
            payload["name"] = name
        return gh_post(f"/repos/{owner}/{repo}/forks", json=payload)

    @mcp.tool()
    def list_forks(owner: str, repo: str, sort: str = "newest", per_page: int = 30, page: int = 1) -> dict | list:
        """List forks of a repository."""
        return gh_get(f"/repos/{owner}/{repo}/forks",
                      params={"sort": sort, "per_page": per_page, "page": page})

    # --- Branches ---

    @mcp.tool()
    def list_branches(
        owner: str, repo: str, protected: bool | None = None, per_page: int = 30, page: int = 1
    ) -> dict | list:
        """List branches in a repository."""
        params: dict = {"per_page": per_page, "page": page}
        if protected is not None:
            params["protected"] = str(protected).lower()
        return gh_get(f"/repos/{owner}/{repo}/branches", params=params)

    @mcp.tool()
    def get_branch(owner: str, repo: str, branch: str) -> dict | list:
        """Get a branch by name."""
        return gh_get(f"/repos/{owner}/{repo}/branches/{branch}")

    @mcp.tool()
    def create_branch(owner: str, repo: str, branch_name: str, sha: str) -> dict | list:
        """Create a new branch from a commit SHA."""
        return gh_post(f"/repos/{owner}/{repo}/git/refs",
                       json={"ref": f"refs/heads/{branch_name}", "sha": sha})

    @mcp.tool()
    def delete_branch(owner: str, repo: str, branch: str) -> dict | list:
        """Delete a branch."""
        return gh_delete(f"/repos/{owner}/{repo}/git/refs/heads/{branch}")

    @mcp.tool()
    def rename_branch(owner: str, repo: str, branch: str, new_name: str) -> dict | list:
        """Rename a branch."""
        return gh_post(f"/repos/{owner}/{repo}/branches/{branch}/rename", json={"new_name": new_name})

    @mcp.tool()
    def merge_branches(
        owner: str, repo: str, base: str, head: str, commit_message: str = ""
    ) -> dict | list:
        """Merge a branch into another."""
        payload: dict = {"base": base, "head": head}
        if commit_message:
            payload["commit_message"] = commit_message
        return gh_post(f"/repos/{owner}/{repo}/merges", json=payload)

    # --- Branch Protection ---

    @mcp.tool()
    def get_branch_protection(owner: str, repo: str, branch: str) -> dict | list:
        """Get branch protection rules."""
        return gh_get(f"/repos/{owner}/{repo}/branches/{branch}/protection")

    @mcp.tool()
    def update_branch_protection(
        owner: str,
        repo: str,
        branch: str,
        required_status_checks: dict | None = None,
        enforce_admins: bool = False,
        required_pull_request_reviews: dict | None = None,
        restrictions: dict | None = None,
        required_linear_history: bool = False,
        allow_force_pushes: bool = False,
        allow_deletions: bool = False,
        required_conversation_resolution: bool = False,
    ) -> dict | list:
        """Update branch protection rules."""
        payload: dict = {
            "required_status_checks": required_status_checks,
            "enforce_admins": enforce_admins,
            "required_pull_request_reviews": required_pull_request_reviews,
            "restrictions": restrictions,
            "required_linear_history": required_linear_history,
            "allow_force_pushes": allow_force_pushes,
            "allow_deletions": allow_deletions,
            "required_conversation_resolution": required_conversation_resolution,
        }
        return gh_put(f"/repos/{owner}/{repo}/branches/{branch}/protection", json=payload)

    @mcp.tool()
    def delete_branch_protection(owner: str, repo: str, branch: str) -> dict | list:
        """Delete branch protection rules."""
        return gh_delete(f"/repos/{owner}/{repo}/branches/{branch}/protection")

    # --- Commits ---

    @mcp.tool()
    def list_commits(
        owner: str,
        repo: str,
        sha: str = "",
        path: str = "",
        author: str = "",
        since: str = "",
        until: str = "",
        per_page: int = 30,
        page: int = 1,
    ) -> dict | list:
        """List commits in a repository."""
        params: dict = {"per_page": per_page, "page": page}
        if sha:
            params["sha"] = sha
        if path:
            params["path"] = path
        if author:
            params["author"] = author
        if since:
            params["since"] = since
        if until:
            params["until"] = until
        return gh_get(f"/repos/{owner}/{repo}/commits", params=params)

    @mcp.tool()
    def get_commit(owner: str, repo: str, ref: str) -> dict | list:
        """Get a commit by SHA or ref."""
        return gh_get(f"/repos/{owner}/{repo}/commits/{ref}")

    @mcp.tool()
    def compare_commits(owner: str, repo: str, base: str, head: str) -> dict | list:
        """Compare two commits or branches."""
        return gh_get(f"/repos/{owner}/{repo}/compare/{base}...{head}")

    # --- Contents ---

    @mcp.tool()
    def get_repo_content(owner: str, repo: str, path: str, ref: str = "") -> dict | list:
        """Get file or directory contents from a repository."""
        params: dict = {}
        if ref:
            params["ref"] = ref
        return gh_get(f"/repos/{owner}/{repo}/contents/{path}", params=params)

    @mcp.tool()
    def create_or_update_file(
        owner: str,
        repo: str,
        path: str,
        message: str,
        content: str,
        sha: str = "",
        branch: str = "",
        committer_name: str = "",
        committer_email: str = "",
    ) -> dict | list:
        """Create or update a file in a repository. content must be base64-encoded."""
        payload: dict = {"message": message, "content": content}
        if sha:
            payload["sha"] = sha
        if branch:
            payload["branch"] = branch
        if committer_name and committer_email:
            payload["committer"] = {"name": committer_name, "email": committer_email}
        return gh_put(f"/repos/{owner}/{repo}/contents/{path}", json=payload)

    @mcp.tool()
    def delete_file(
        owner: str,
        repo: str,
        path: str,
        message: str,
        sha: str,
        branch: str = "",
        committer_name: str = "",
        committer_email: str = "",
    ) -> dict | list:
        """Delete a file from a repository."""
        payload: dict = {"message": message, "sha": sha}
        if branch:
            payload["branch"] = branch
        if committer_name and committer_email:
            payload["committer"] = {"name": committer_name, "email": committer_email}
        return gh_delete(f"/repos/{owner}/{repo}/contents/{path}", json=payload)

    @mcp.tool()
    def get_readme(owner: str, repo: str, ref: str = "") -> dict | list:
        """Get the README for a repository."""
        params: dict = {}
        if ref:
            params["ref"] = ref
        return gh_get(f"/repos/{owner}/{repo}/readme", params=params)

    # --- Tags & Releases (tags) ---

    @mcp.tool()
    def list_tags(owner: str, repo: str, per_page: int = 30, page: int = 1) -> dict | list:
        """List tags for a repository."""
        return gh_get(f"/repos/{owner}/{repo}/tags", params={"per_page": per_page, "page": page})

    @mcp.tool()
    def list_repo_topics(owner: str, repo: str) -> dict | list:
        """List topics for a repository."""
        return gh_get(f"/repos/{owner}/{repo}/topics")

    @mcp.tool()
    def replace_repo_topics(owner: str, repo: str, names: list[str]) -> dict | list:
        """Replace all topics for a repository."""
        return gh_put(f"/repos/{owner}/{repo}/topics", json={"names": names})

    @mcp.tool()
    def get_repo_languages(owner: str, repo: str) -> dict | list:
        """Get the languages used in a repository."""
        return gh_get(f"/repos/{owner}/{repo}/languages")

    @mcp.tool()
    def get_repo_contributors(
        owner: str, repo: str, anon: bool = False, per_page: int = 30, page: int = 1
    ) -> dict | list:
        """List contributors to a repository."""
        return gh_get(f"/repos/{owner}/{repo}/contributors",
                      params={"anon": str(anon).lower(), "per_page": per_page, "page": page})

    @mcp.tool()
    def list_repo_collaborators(
        owner: str, repo: str, affiliation: str = "all", per_page: int = 30, page: int = 1
    ) -> dict | list:
        """List collaborators for a repository."""
        return gh_get(f"/repos/{owner}/{repo}/collaborators",
                      params={"affiliation": affiliation, "per_page": per_page, "page": page})

    @mcp.tool()
    def add_repo_collaborator(
        owner: str, repo: str, username: str, permission: str = "push"
    ) -> dict | list:
        """Add a collaborator to a repository. permission: pull|triage|push|maintain|admin."""
        return gh_put(f"/repos/{owner}/{repo}/collaborators/{username}", json={"permission": permission})

    @mcp.tool()
    def remove_repo_collaborator(owner: str, repo: str, username: str) -> dict | list:
        """Remove a collaborator from a repository."""
        return gh_delete(f"/repos/{owner}/{repo}/collaborators/{username}")

    @mcp.tool()
    def get_repo_traffic_views(owner: str, repo: str, per: str = "day") -> dict | list:
        """Get repository traffic views. per: day|week."""
        return gh_get(f"/repos/{owner}/{repo}/traffic/views", params={"per": per})

    @mcp.tool()
    def get_repo_traffic_clones(owner: str, repo: str, per: str = "day") -> dict | list:
        """Get repository clone traffic. per: day|week."""
        return gh_get(f"/repos/{owner}/{repo}/traffic/clones", params={"per": per})

    @mcp.tool()
    def list_repo_stargazers(owner: str, repo: str, per_page: int = 30, page: int = 1) -> dict | list:
        """List stargazers of a repository."""
        return gh_get(f"/repos/{owner}/{repo}/stargazers",
                      params={"per_page": per_page, "page": page})

    @mcp.tool()
    def list_repo_watchers(owner: str, repo: str, per_page: int = 30, page: int = 1) -> dict | list:
        """List watchers of a repository."""
        return gh_get(f"/repos/{owner}/{repo}/subscribers",
                      params={"per_page": per_page, "page": page})

    # --- Git refs ---

    @mcp.tool()
    def list_git_refs(owner: str, repo: str, ref: str = "") -> dict | list:
        """List Git refs (branches, tags) in a repository."""
        path = f"/repos/{owner}/{repo}/git/refs"
        if ref:
            path += f"/{ref}"
        return gh_get(path)

    @mcp.tool()
    def get_git_ref(owner: str, repo: str, ref: str) -> dict | list:
        """Get a Git ref. ref should be like heads/main or tags/v1.0."""
        return gh_get(f"/repos/{owner}/{repo}/git/ref/{ref}")

    @mcp.tool()
    def update_git_ref(owner: str, repo: str, ref: str, sha: str, force: bool = False) -> dict | list:
        """Update a Git ref to point to a new SHA."""
        return gh_patch(f"/repos/{owner}/{repo}/git/refs/{ref}", json={"sha": sha, "force": force})

    # --- Git Trees & Blobs ---

    @mcp.tool()
    def get_git_tree(owner: str, repo: str, tree_sha: str, recursive: bool = False) -> dict | list:
        """Get a Git tree object."""
        params: dict = {}
        if recursive:
            params["recursive"] = "1"
        return gh_get(f"/repos/{owner}/{repo}/git/trees/{tree_sha}", params=params)

    @mcp.tool()
    def get_git_blob(owner: str, repo: str, file_sha: str) -> dict | list:
        """Get a Git blob object."""
        return gh_get(f"/repos/{owner}/{repo}/git/blobs/{file_sha}")

    @mcp.tool()
    def create_git_blob(owner: str, repo: str, content: str, encoding: str = "utf-8") -> dict | list:
        """Create a Git blob."""
        return gh_post(f"/repos/{owner}/{repo}/git/blobs", json={"content": content, "encoding": encoding})

    @mcp.tool()
    def create_git_tree(owner: str, repo: str, tree: list[dict], base_tree: str = "") -> dict | list:
        """Create a Git tree. Each tree item: {path, mode, type, sha|content}."""
        payload: dict = {"tree": tree}
        if base_tree:
            payload["base_tree"] = base_tree
        return gh_post(f"/repos/{owner}/{repo}/git/trees", json=payload)

    @mcp.tool()
    def create_git_commit(
        owner: str,
        repo: str,
        message: str,
        tree: str,
        parents: list[str],
        author_name: str = "",
        author_email: str = "",
        author_date: str = "",
    ) -> dict | list:
        """Create a Git commit object."""
        payload: dict = {"message": message, "tree": tree, "parents": parents}
        if author_name and author_email:
            author: dict = {"name": author_name, "email": author_email}
            if author_date:
                author["date"] = author_date
            payload["author"] = author
        return gh_post(f"/repos/{owner}/{repo}/git/commits", json=payload)
