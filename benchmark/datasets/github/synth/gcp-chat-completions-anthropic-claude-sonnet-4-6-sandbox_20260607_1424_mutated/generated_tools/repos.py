"""GitHub Repositories and Contents tools."""
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


def register_repos_tools(mcp: FastMCP):

    # ── Repository CRUD ──────────────────────────────────────────────────────

    @mcp.tool()
    def get_repo(owner: str, repo: str) -> dict:
        """Get a repository."""
        return _get(f"/repos/{owner}/{repo}")

    @mcp.tool()
    def list_org_repos(org: str, type: str = "all", sort: str = "created",
                       direction: str = "desc", per_page: int = 30, page: int = 1) -> dict:
        """List repositories for an organization."""
        return _get(f"/orgs/{org}/repos",
                    {"type": type, "sort": sort, "direction": direction,
                     "per_page": per_page, "page": page})

    @mcp.tool()
    def list_user_repos(username: str, type: str = "owner", sort: str = "full_name",
                        direction: str = "asc", per_page: int = 30, page: int = 1) -> dict:
        """List public repositories for a user."""
        return _get(f"/users/{username}/repos",
                    {"type": type, "sort": sort, "direction": direction,
                     "per_page": per_page, "page": page})

    @mcp.tool()
    def list_my_repos(visibility: str = "all", affiliation: str = "owner,collaborator,organization_member",
                      sort: str = "full_name", direction: str = "asc",
                      per_page: int = 30, page: int = 1) -> dict:
        """List repositories for the authenticated user."""
        return _get("/user/repos",
                    {"visibility": visibility, "affiliation": affiliation,
                     "sort": sort, "direction": direction,
                     "per_page": per_page, "page": page})

    @mcp.tool()
    def create_org_repo(org: str, name: str, description: str = "",
                        private: bool = False, auto_init: bool = False,
                        gitignore_template: str = "", license_template: str = "",
                        has_issues: bool = True, has_wiki: bool = True) -> dict:
        """Create a repository in an organization."""
        payload = {"name": name, "private": private, "auto_init": auto_init,
                   "has_issues": has_issues, "has_wiki": has_wiki}
        if description:
            payload["description"] = description
        if gitignore_template:
            payload["gitignore_template"] = gitignore_template
        if license_template:
            payload["license_template"] = license_template
        return _post(f"/orgs/{org}/repos", payload)

    @mcp.tool()
    def create_user_repo(name: str, description: str = "", private: bool = False,
                         auto_init: bool = False, gitignore_template: str = "",
                         license_template: str = "") -> dict:
        """Create a repository for the authenticated user."""
        payload = {"name": name, "private": private, "auto_init": auto_init}
        if description:
            payload["description"] = description
        if gitignore_template:
            payload["gitignore_template"] = gitignore_template
        if license_template:
            payload["license_template"] = license_template
        return _post("/user/repos", payload)

    @mcp.tool()
    def update_repo(owner: str, repo: str, name: str = None, description: str = None,
                    homepage: str = None, private: bool = None,
                    has_issues: bool = None, has_wiki: bool = None,
                    default_branch: str = None, archived: bool = None) -> dict:
        """Update a repository's settings."""
        payload = {}
        if name is not None:
            payload["name"] = name
        if description is not None:
            payload["description"] = description
        if homepage is not None:
            payload["homepage"] = homepage
        if private is not None:
            payload["private"] = private
        if has_issues is not None:
            payload["has_issues"] = has_issues
        if has_wiki is not None:
            payload["has_wiki"] = has_wiki
        if default_branch is not None:
            payload["default_branch"] = default_branch
        if archived is not None:
            payload["archived"] = archived
        return _patch(f"/repos/{owner}/{repo}", payload)

    @mcp.tool()
    def delete_repo(owner: str, repo: str) -> dict:
        """Delete a repository. Requires admin access."""
        return _delete(f"/repos/{owner}/{repo}")

    @mcp.tool()
    def list_repo_contributors(owner: str, repo: str, anon: str = "false",
                               per_page: int = 30, page: int = 1) -> dict:
        """List contributors to a repository."""
        return _get(f"/repos/{owner}/{repo}/contributors",
                    {"anon": anon, "per_page": per_page, "page": page})

    @mcp.tool()
    def list_repo_languages(owner: str, repo: str) -> dict:
        """List languages used in a repository."""
        return _get(f"/repos/{owner}/{repo}/languages")

    @mcp.tool()
    def list_repo_tags(owner: str, repo: str, per_page: int = 30, page: int = 1) -> dict:
        """List tags for a repository."""
        return _get(f"/repos/{owner}/{repo}/tags", {"per_page": per_page, "page": page})

    @mcp.tool()
    def list_repo_topics(owner: str, repo: str) -> dict:
        """Get all topics for a repository."""
        return _get(f"/repos/{owner}/{repo}/topics")

    @mcp.tool()
    def replace_repo_topics(owner: str, repo: str, names: list) -> dict:
        """Replace all topics for a repository."""
        return _put(f"/repos/{owner}/{repo}/topics", {"names": names})

    @mcp.tool()
    def transfer_repo(owner: str, repo: str, new_owner: str, new_name: str = "",
                      team_ids: list = None) -> dict:
        """Transfer a repository to a new owner."""
        payload = {"new_owner": new_owner}
        if new_name:
            payload["new_name"] = new_name
        if team_ids:
            payload["team_ids"] = team_ids
        return _post(f"/repos/{owner}/{repo}/transfer", payload)

    @mcp.tool()
    def create_repo_from_template(template_owner: str, template_repo: str,
                                  name: str, owner: str = "", description: str = "",
                                  private: bool = False, include_all_branches: bool = False) -> dict:
        """Create a repository from a template."""
        payload = {"name": name, "private": private,
                   "include_all_branches": include_all_branches}
        if owner:
            payload["owner"] = owner
        if description:
            payload["description"] = description
        return _post(f"/repos/{template_owner}/{template_repo}/generate", payload)

    @mcp.tool()
    def create_repo_dispatch(owner: str, repo: str, event_type: str,
                             client_payload: dict = None) -> dict:
        """Create a repository dispatch event to trigger workflows."""
        payload = {"event_type": event_type}
        if client_payload:
            payload["client_payload"] = client_payload
        return _post(f"/repos/{owner}/{repo}/dispatches", payload)

    # ── Repository Contents ──────────────────────────────────────────────────

    @mcp.tool()
    def get_repo_content(owner: str, repo: str, path: str, ref: str = "") -> dict:
        """Get the contents of a file or directory in a repository."""
        params = {}
        if ref:
            params["ref"] = ref
        return _get(f"/repos/{owner}/{repo}/contents/{path}", params)

    @mcp.tool()
    def create_or_update_file(owner: str, repo: str, path: str,
                              message: str, content: str, sha: str = "",
                              branch: str = "",
                              committer_name: str = "", committer_email: str = "") -> dict:
        """Create or update a file in a repository. content must be Base64-encoded."""
        payload = {"message": message, "content": content}
        if sha:
            payload["sha"] = sha
        if branch:
            payload["branch"] = branch
        if committer_name and committer_email:
            payload["committer"] = {"name": committer_name, "email": committer_email}
        return _put(f"/repos/{owner}/{repo}/contents/{path}", payload)

    @mcp.tool()
    def delete_file(owner: str, repo: str, path: str, message: str, sha: str,
                    branch: str = "", committer_name: str = "", committer_email: str = "") -> dict:
        """Delete a file in a repository."""
        payload = {"message": message, "sha": sha}
        if branch:
            payload["branch"] = branch
        if committer_name and committer_email:
            payload["committer"] = {"name": committer_name, "email": committer_email}
        return _delete(f"/repos/{owner}/{repo}/contents/{path}", payload)

    @mcp.tool()
    def get_readme(owner: str, repo: str, ref: str = "") -> dict:
        """Get the README for a repository."""
        params = {}
        if ref:
            params["ref"] = ref
        return _get(f"/repos/{owner}/{repo}/readme", params)
