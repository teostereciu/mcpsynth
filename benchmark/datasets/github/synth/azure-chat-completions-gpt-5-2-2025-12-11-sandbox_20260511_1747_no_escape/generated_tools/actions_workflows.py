from typing import Any, Dict, List, Optional, Union

from .http_client import GitHubClient, parse_owner_repo


def list_repo_workflows(
    *,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
    per_page: int = 30,
    page: int = 1,
    accept: str = "application/vnd.github+json",
) -> Union[Dict[str, Any], List[Any], str]:
    """GET /repos/{owner}/{repo}/actions/workflows"""
    o, r = parse_owner_repo(owner, repo, owner_repo)
    client = GitHubClient()
    params = {"per_page": per_page, "page": page}
    return client.request("GET", f"/repos/{o}/{r}/actions/workflows", params=params, accept=accept)


def get_workflow(
    *,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
    workflow_id: Union[int, str],
    accept: str = "application/vnd.github+json",
) -> Union[Dict[str, Any], List[Any], str]:
    """GET /repos/{owner}/{repo}/actions/workflows/{workflow_id}"""
    o, r = parse_owner_repo(owner, repo, owner_repo)
    client = GitHubClient()
    return client.request("GET", f"/repos/{o}/{r}/actions/workflows/{workflow_id}", accept=accept)


def disable_workflow(
    *,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
    workflow_id: Union[int, str],
    accept: str = "application/vnd.github+json",
) -> Union[Dict[str, Any], List[Any], str]:
    """PUT /repos/{owner}/{repo}/actions/workflows/{workflow_id}/disable"""
    o, r = parse_owner_repo(owner, repo, owner_repo)
    client = GitHubClient()
    return client.request("PUT", f"/repos/{o}/{r}/actions/workflows/{workflow_id}/disable", accept=accept)


def enable_workflow(
    *,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
    workflow_id: Union[int, str],
    accept: str = "application/vnd.github+json",
) -> Union[Dict[str, Any], List[Any], str]:
    """PUT /repos/{owner}/{repo}/actions/workflows/{workflow_id}/enable"""
    o, r = parse_owner_repo(owner, repo, owner_repo)
    client = GitHubClient()
    return client.request("PUT", f"/repos/{o}/{r}/actions/workflows/{workflow_id}/enable", accept=accept)


def create_workflow_dispatch(
    *,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
    workflow_id: Union[int, str],
    ref: str,
    inputs: Optional[Dict[str, Any]] = None,
    accept: str = "application/vnd.github+json",
) -> Union[Dict[str, Any], List[Any], str]:
    """POST /repos/{owner}/{repo}/actions/workflows/{workflow_id}/dispatches"""
    o, r = parse_owner_repo(owner, repo, owner_repo)
    client = GitHubClient()
    payload: Dict[str, Any] = {"ref": ref}
    if inputs is not None:
        payload["inputs"] = inputs
    return client.request("POST", f"/repos/{o}/{r}/actions/workflows/{workflow_id}/dispatches", json=payload, accept=accept)


def get_workflow_usage(
    *,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
    workflow_id: Union[int, str],
    accept: str = "application/vnd.github+json",
) -> Union[Dict[str, Any], List[Any], str]:
    """GET /repos/{owner}/{repo}/actions/workflows/{workflow_id}/timing"""
    o, r = parse_owner_repo(owner, repo, owner_repo)
    client = GitHubClient()
    return client.request("GET", f"/repos/{o}/{r}/actions/workflows/{workflow_id}/timing", accept=accept)
