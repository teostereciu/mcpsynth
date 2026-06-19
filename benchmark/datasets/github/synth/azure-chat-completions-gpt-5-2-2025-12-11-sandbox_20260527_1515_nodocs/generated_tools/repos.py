from typing import Any, Dict, Optional

from .github_client import GitHubClient


client = GitHubClient()


def get_repo(owner: str, repo: str) -> Dict[str, Any]:
    return client.request("GET", f"/repos/{owner}/{repo}")


def list_user_repos(username: str, *, type: str = "owner", sort: str = "full_name", per_page: int = 30, page: int = 1) -> Dict[str, Any]:
    return client.request(
        "GET",
        f"/users/{username}/repos",
        params={"type": type, "sort": sort, "per_page": per_page, "page": page},
    )


def list_org_repos(org: str, *, type: str = "all", per_page: int = 30, page: int = 1) -> Dict[str, Any]:
    return client.request(
        "GET",
        f"/orgs/{org}/repos",
        params={"type": type, "per_page": per_page, "page": page},
    )


def create_repo_for_authenticated_user(
    name: str,
    *,
    description: Optional[str] = None,
    private: bool = False,
    auto_init: bool = False,
    has_issues: bool = True,
    has_projects: bool = True,
    has_wiki: bool = True,
) -> Dict[str, Any]:
    payload: Dict[str, Any] = {
        "name": name,
        "private": private,
        "auto_init": auto_init,
        "has_issues": has_issues,
        "has_projects": has_projects,
        "has_wiki": has_wiki,
    }
    if description is not None:
        payload["description"] = description
    return client.request("POST", "/user/repos", json=payload)


def fork_repo(owner: str, repo: str, *, organization: Optional[str] = None, name: Optional[str] = None, default_branch_only: bool = False) -> Dict[str, Any]:
    payload: Dict[str, Any] = {"default_branch_only": default_branch_only}
    if organization is not None:
        payload["organization"] = organization
    if name is not None:
        payload["name"] = name
    return client.request("POST", f"/repos/{owner}/{repo}/forks", json=payload)


def list_branches(owner: str, repo: str, *, protected: Optional[bool] = None, per_page: int = 30, page: int = 1) -> Dict[str, Any]:
    params: Dict[str, Any] = {"per_page": per_page, "page": page}
    if protected is not None:
        params["protected"] = str(protected).lower()
    return client.request("GET", f"/repos/{owner}/{repo}/branches", params=params)


def get_branch(owner: str, repo: str, branch: str) -> Dict[str, Any]:
    return client.request("GET", f"/repos/{owner}/{repo}/branches/{branch}")


def get_commit(owner: str, repo: str, ref: str) -> Dict[str, Any]:
    return client.request("GET", f"/repos/{owner}/{repo}/commits/{ref}")


def list_commits(owner: str, repo: str, *, sha: Optional[str] = None, path: Optional[str] = None, per_page: int = 30, page: int = 1) -> Dict[str, Any]:
    params: Dict[str, Any] = {"per_page": per_page, "page": page}
    if sha is not None:
        params["sha"] = sha
    if path is not None:
        params["path"] = path
    return client.request("GET", f"/repos/{owner}/{repo}/commits", params=params)


def get_content(owner: str, repo: str, path: str, *, ref: Optional[str] = None) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if ref is not None:
        params["ref"] = ref
    return client.request("GET", f"/repos/{owner}/{repo}/contents/{path}", params=params)


def create_or_update_file_contents(
    owner: str,
    repo: str,
    path: str,
    message: str,
    content_base64: str,
    *,
    sha: Optional[str] = None,
    branch: Optional[str] = None,
    committer_name: Optional[str] = None,
    committer_email: Optional[str] = None,
) -> Dict[str, Any]:
    payload: Dict[str, Any] = {"message": message, "content": content_base64}
    if sha is not None:
        payload["sha"] = sha
    if branch is not None:
        payload["branch"] = branch
    if committer_name or committer_email:
        payload["committer"] = {"name": committer_name, "email": committer_email}
    return client.request("PUT", f"/repos/{owner}/{repo}/contents/{path}", json=payload)


def delete_file(owner: str, repo: str, path: str, message: str, sha: str, *, branch: Optional[str] = None) -> Dict[str, Any]:
    payload: Dict[str, Any] = {"message": message, "sha": sha}
    if branch is not None:
        payload["branch"] = branch
    return client.request("DELETE", f"/repos/{owner}/{repo}/contents/{path}", json=payload)
