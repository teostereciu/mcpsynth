from typing import Any, Dict, Optional, Union

from ._client import gh_request, parse_owner_repo


def list_workflows(
    *,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
    per_page: Optional[int] = None,
    page: Optional[int] = None,
) -> Any:
    o, r = parse_owner_repo(owner, repo, owner_repo)
    if not o or not r:
        return {"error": "owner/repo required (or set GITHUB_TEST_REPO)"}
    return gh_request(
        "GET",
        f"/repos/{o}/{r}/actions/workflows",
        params={"per_page": per_page, "page": page},
    )


def get_workflow(
    *,
    workflow_id: Union[int, str],
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
) -> Any:
    o, r = parse_owner_repo(owner, repo, owner_repo)
    if not o or not r:
        return {"error": "owner/repo required (or set GITHUB_TEST_REPO)"}
    return gh_request("GET", f"/repos/{o}/{r}/actions/workflows/{workflow_id}")


def disable_workflow(
    *,
    workflow_id: Union[int, str],
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
) -> Any:
    o, r = parse_owner_repo(owner, repo, owner_repo)
    if not o or not r:
        return {"error": "owner/repo required (or set GITHUB_TEST_REPO)"}
    return gh_request("PUT", f"/repos/{o}/{r}/actions/workflows/{workflow_id}/disable")


def enable_workflow(
    *,
    workflow_id: Union[int, str],
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
) -> Any:
    o, r = parse_owner_repo(owner, repo, owner_repo)
    if not o or not r:
        return {"error": "owner/repo required (or set GITHUB_TEST_REPO)"}
    return gh_request("PUT", f"/repos/{o}/{r}/actions/workflows/{workflow_id}/enable")


def dispatch_workflow(
    *,
    workflow_id: Union[int, str],
    ref: str,
    inputs: Optional[Dict[str, Any]] = None,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
) -> Any:
    o, r = parse_owner_repo(owner, repo, owner_repo)
    if not o or not r:
        return {"error": "owner/repo required (or set GITHUB_TEST_REPO)"}
    payload: Dict[str, Any] = {"ref": ref}
    if inputs is not None:
        payload["inputs"] = inputs
    return gh_request("POST", f"/repos/{o}/{r}/actions/workflows/{workflow_id}/dispatches", json=payload)


def get_workflow_timing(
    *,
    workflow_id: Union[int, str],
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
) -> Any:
    o, r = parse_owner_repo(owner, repo, owner_repo)
    if not o or not r:
        return {"error": "owner/repo required (or set GITHUB_TEST_REPO)"}
    return gh_request("GET", f"/repos/{o}/{r}/actions/workflows/{workflow_id}/timing")
