from typing import Any, Dict, List, Optional, Union

from .http_client import GitHubClient, parse_owner_repo


def get_repo_content(
    *,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
    path: str = "",
    ref: Optional[str] = None,
    accept: str = "application/vnd.github+json",
) -> Union[Dict[str, Any], List[Any], str]:
    """GET /repos/{owner}/{repo}/contents/{path}"""
    o, r = parse_owner_repo(owner, repo, owner_repo)
    client = GitHubClient()
    params: Dict[str, Any] = {}
    if ref is not None:
        params["ref"] = ref
    p = path.lstrip("/")
    endpoint = f"/repos/{o}/{r}/contents" + (f"/{p}" if p else "")
    return client.request("GET", endpoint, params=params or None, accept=accept)


def create_or_update_file(
    *,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
    path: str,
    message: str,
    content_base64: str,
    sha: Optional[str] = None,
    branch: Optional[str] = None,
    committer: Optional[Dict[str, Any]] = None,
    author: Optional[Dict[str, Any]] = None,
    accept: str = "application/vnd.github+json",
) -> Union[Dict[str, Any], List[Any], str]:
    """PUT /repos/{owner}/{repo}/contents/{path}"""
    o, r = parse_owner_repo(owner, repo, owner_repo)
    client = GitHubClient()
    payload: Dict[str, Any] = {"message": message, "content": content_base64}
    if sha is not None:
        payload["sha"] = sha
    if branch is not None:
        payload["branch"] = branch
    if committer is not None:
        payload["committer"] = committer
    if author is not None:
        payload["author"] = author
    p = path.lstrip("/")
    return client.request("PUT", f"/repos/{o}/{r}/contents/{p}", json=payload, accept=accept)


def delete_file(
    *,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
    path: str,
    message: str,
    sha: str,
    branch: Optional[str] = None,
    committer: Optional[Dict[str, Any]] = None,
    author: Optional[Dict[str, Any]] = None,
    accept: str = "application/vnd.github+json",
) -> Union[Dict[str, Any], List[Any], str]:
    """DELETE /repos/{owner}/{repo}/contents/{path}"""
    o, r = parse_owner_repo(owner, repo, owner_repo)
    client = GitHubClient()
    payload: Dict[str, Any] = {"message": message, "sha": sha}
    if branch is not None:
        payload["branch"] = branch
    if committer is not None:
        payload["committer"] = committer
    if author is not None:
        payload["author"] = author
    p = path.lstrip("/")
    return client.request("DELETE", f"/repos/{o}/{r}/contents/{p}", json=payload, accept=accept)
