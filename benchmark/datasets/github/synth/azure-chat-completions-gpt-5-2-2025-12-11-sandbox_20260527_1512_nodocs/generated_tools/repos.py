import base64
from typing import Any, Dict, Optional

from ._client import GitHubClient, split_repo


def get_repo(repo: str) -> Any:
    owner, name = split_repo(repo)
    client = GitHubClient()
    return client.request("GET", f"/repos/{owner}/{name}")


def list_branches(repo: str, protected: Optional[bool] = None, per_page: int = 30, page: int = 1) -> Any:
    owner, name = split_repo(repo)
    client = GitHubClient()
    params: Dict[str, Any] = {"per_page": per_page, "page": page}
    if protected is not None:
        params["protected"] = str(protected).lower()
    return client.request("GET", f"/repos/{owner}/{name}/branches", params=params)


def get_branch(repo: str, branch: str) -> Any:
    owner, name = split_repo(repo)
    client = GitHubClient()
    return client.request("GET", f"/repos/{owner}/{name}/branches/{branch}")


def list_commits(repo: str, sha: Optional[str] = None, path: Optional[str] = None, author: Optional[str] = None, since: Optional[str] = None, until: Optional[str] = None, per_page: int = 30, page: int = 1) -> Any:
    owner, name = split_repo(repo)
    client = GitHubClient()
    params: Dict[str, Any] = {"per_page": per_page, "page": page}
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
    return client.request("GET", f"/repos/{owner}/{name}/commits", params=params)


def get_commit(repo: str, ref: str) -> Any:
    owner, name = split_repo(repo)
    client = GitHubClient()
    return client.request("GET", f"/repos/{owner}/{name}/commits/{ref}")


def get_content(repo: str, path: str, ref: Optional[str] = None) -> Any:
    owner, name = split_repo(repo)
    client = GitHubClient()
    params = {"ref": ref} if ref else None
    return client.request("GET", f"/repos/{owner}/{name}/contents/{path.lstrip('/')}" , params=params)


def get_file_text(repo: str, path: str, ref: Optional[str] = None) -> Any:
    """Convenience: fetch a file via contents API and decode base64 if applicable."""
    data = get_content(repo, path, ref=ref)
    if isinstance(data, dict) and data.get("content") and data.get("encoding") == "base64":
        try:
            raw = base64.b64decode(data["content"], validate=False)
            return {"path": data.get("path"), "sha": data.get("sha"), "text": raw.decode("utf-8", errors="replace")}
        except Exception as e:
            return {"error": str(e), "body": data}
    return data


def create_or_update_file(repo: str, path: str, message: str, content_text: str, branch: Optional[str] = None, sha: Optional[str] = None, committer: Optional[Dict[str, str]] = None, author: Optional[Dict[str, str]] = None) -> Any:
    owner, name = split_repo(repo)
    client = GitHubClient()
    payload: Dict[str, Any] = {
        "message": message,
        "content": base64.b64encode(content_text.encode("utf-8")).decode("ascii"),
    }
    if branch is not None:
        payload["branch"] = branch
    if sha is not None:
        payload["sha"] = sha
    if committer is not None:
        payload["committer"] = committer
    if author is not None:
        payload["author"] = author
    return client.request("PUT", f"/repos/{owner}/{name}/contents/{path.lstrip('/')}" , json=payload, expected=(200, 201))


def delete_file(repo: str, path: str, message: str, sha: str, branch: Optional[str] = None, committer: Optional[Dict[str, str]] = None, author: Optional[Dict[str, str]] = None) -> Any:
    owner, name = split_repo(repo)
    client = GitHubClient()
    payload: Dict[str, Any] = {"message": message, "sha": sha}
    if branch is not None:
        payload["branch"] = branch
    if committer is not None:
        payload["committer"] = committer
    if author is not None:
        payload["author"] = author
    return client.request("DELETE", f"/repos/{owner}/{name}/contents/{path.lstrip('/')}" , json=payload, expected=(200,))


def fork_repo(repo: str, organization: Optional[str] = None, name: Optional[str] = None, default_branch_only: Optional[bool] = None) -> Any:
    owner, rname = split_repo(repo)
    client = GitHubClient()
    payload: Dict[str, Any] = {}
    if organization is not None:
        payload["organization"] = organization
    if name is not None:
        payload["name"] = name
    if default_branch_only is not None:
        payload["default_branch_only"] = default_branch_only
    return client.request("POST", f"/repos/{owner}/{rname}/forks", json=payload, expected=(202,))


def create_repo(name: str, description: Optional[str] = None, private: bool = False, auto_init: bool = True, gitignore_template: Optional[str] = None, license_template: Optional[str] = None) -> Any:
    client = GitHubClient()
    payload: Dict[str, Any] = {"name": name, "private": private, "auto_init": auto_init}
    if description is not None:
        payload["description"] = description
    if gitignore_template is not None:
        payload["gitignore_template"] = gitignore_template
    if license_template is not None:
        payload["license_template"] = license_template
    return client.request("POST", "/user/repos", json=payload, expected=(201,))
