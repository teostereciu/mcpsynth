import base64
from typing import Any, Dict, Optional

from .github_client import GitHubClient, parse_owner_repo


def get_repo(owner_repo: str) -> Dict[str, Any]:
    try:
        owner, repo = parse_owner_repo(owner_repo)
    except ValueError as e:
        return {"error": str(e)}
    return GitHubClient().request("GET", f"/repos/{owner}/{repo}")


def list_repos_for_user(username: str, per_page: int = 100, max_pages: int = 5) -> Dict[str, Any]:
    return GitHubClient().paginate(f"/users/{username}/repos", per_page=per_page, max_pages=max_pages)


def list_repos_for_authenticated_user(visibility: str = "all", affiliation: str = "owner,collaborator,organization_member", per_page: int = 100, max_pages: int = 5) -> Dict[str, Any]:
    params = {"visibility": visibility, "affiliation": affiliation}
    return GitHubClient().paginate("/user/repos", params=params, per_page=per_page, max_pages=max_pages)


def create_repo(name: str, description: Optional[str] = None, private: bool = False, auto_init: bool = True, has_issues: bool = True, has_projects: bool = True, has_wiki: bool = True) -> Dict[str, Any]:
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
    return GitHubClient().request("POST", "/user/repos", json=payload)


def fork_repo(owner_repo: str, organization: Optional[str] = None, name: Optional[str] = None, default_branch_only: bool = False) -> Dict[str, Any]:
    try:
        owner, repo = parse_owner_repo(owner_repo)
    except ValueError as e:
        return {"error": str(e)}
    payload: Dict[str, Any] = {"default_branch_only": default_branch_only}
    if organization is not None:
        payload["organization"] = organization
    if name is not None:
        payload["name"] = name
    return GitHubClient().request("POST", f"/repos/{owner}/{repo}/forks", json=payload)


def list_branches(owner_repo: str, protected: Optional[bool] = None, per_page: int = 100, max_pages: int = 5) -> Dict[str, Any]:
    try:
        owner, repo = parse_owner_repo(owner_repo)
    except ValueError as e:
        return {"error": str(e)}
    params: Dict[str, Any] = {}
    if protected is not None:
        params["protected"] = str(protected).lower()
    return GitHubClient().paginate(f"/repos/{owner}/{repo}/branches", params=params, per_page=per_page, max_pages=max_pages)


def get_branch(owner_repo: str, branch: str) -> Dict[str, Any]:
    try:
        owner, repo = parse_owner_repo(owner_repo)
    except ValueError as e:
        return {"error": str(e)}
    return GitHubClient().request("GET", f"/repos/{owner}/{repo}/branches/{branch}")


def list_commits(owner_repo: str, sha: Optional[str] = None, path: Optional[str] = None, author: Optional[str] = None, since: Optional[str] = None, until: Optional[str] = None, per_page: int = 100, max_pages: int = 5) -> Dict[str, Any]:
    try:
        owner, repo = parse_owner_repo(owner_repo)
    except ValueError as e:
        return {"error": str(e)}
    params: Dict[str, Any] = {}
    if sha is not None:
        params["sha"] = sha
    if path is not None:
        params["path"] = path
    if author is not None:
        params["author"] = author
    if since is not None:
        params["since"] = since
    if until is not None:
        params["until"] = until
    return GitHubClient().paginate(f"/repos/{owner}/{repo}/commits", params=params, per_page=per_page, max_pages=max_pages)


def get_commit(owner_repo: str, ref: str) -> Dict[str, Any]:
    try:
        owner, repo = parse_owner_repo(owner_repo)
    except ValueError as e:
        return {"error": str(e)}
    return GitHubClient().request("GET", f"/repos/{owner}/{repo}/commits/{ref}")


def get_contents(owner_repo: str, path: str, ref: Optional[str] = None) -> Dict[str, Any]:
    try:
        owner, repo = parse_owner_repo(owner_repo)
    except ValueError as e:
        return {"error": str(e)}
    params: Dict[str, Any] = {}
    if ref is not None:
        params["ref"] = ref
    return GitHubClient().request("GET", f"/repos/{owner}/{repo}/contents/{path.lstrip('/')}" , params=params)


def get_file_text(owner_repo: str, path: str, ref: Optional[str] = None) -> Dict[str, Any]:
    r = get_contents(owner_repo, path, ref=ref)
    if not r.get("ok"):
        return r
    data = r.get("data")
    if not isinstance(data, dict):
        return {"ok": False, "error": "Unexpected contents response", "data": data}
    if data.get("type") != "file":
        return {"ok": False, "error": "Path is not a file", "data": data}
    content = data.get("content")
    encoding = data.get("encoding")
    if encoding == "base64" and isinstance(content, str):
        try:
            raw = base64.b64decode(content.encode("utf-8"), validate=False)
            return {"ok": True, "status": 200, "data": raw.decode("utf-8", errors="replace")}
        except Exception as e:
            return {"ok": False, "error": str(e), "data": data}
    return {"ok": True, "status": 200, "data": content}


def create_or_update_file(
    owner_repo: str,
    path: str,
    message: str,
    content_text: str,
    branch: Optional[str] = None,
    sha: Optional[str] = None,
    committer: Optional[Dict[str, str]] = None,
    author: Optional[Dict[str, str]] = None,
) -> Dict[str, Any]:
    """Create or update a file via the Contents API.

    If updating, provide the current blob sha.
    """
    try:
        owner, repo = parse_owner_repo(owner_repo)
    except ValueError as e:
        return {"error": str(e)}

    b64 = base64.b64encode(content_text.encode("utf-8")).decode("utf-8")
    payload: Dict[str, Any] = {"message": message, "content": b64}
    if branch is not None:
        payload["branch"] = branch
    if sha is not None:
        payload["sha"] = sha
    if committer is not None:
        payload["committer"] = committer
    if author is not None:
        payload["author"] = author

    return GitHubClient().request("PUT", f"/repos/{owner}/{repo}/contents/{path.lstrip('/')}" , json=payload)


def delete_file(owner_repo: str, path: str, message: str, sha: str, branch: Optional[str] = None) -> Dict[str, Any]:
    try:
        owner, repo = parse_owner_repo(owner_repo)
    except ValueError as e:
        return {"error": str(e)}
    payload: Dict[str, Any] = {"message": message, "sha": sha}
    if branch is not None:
        payload["branch"] = branch
    return GitHubClient().request("DELETE", f"/repos/{owner}/{repo}/contents/{path.lstrip('/')}" , json=payload)
