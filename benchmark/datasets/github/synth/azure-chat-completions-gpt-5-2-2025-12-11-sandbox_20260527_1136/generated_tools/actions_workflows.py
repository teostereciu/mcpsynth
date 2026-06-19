from typing import Any, Dict, Optional, Union

from .http_client import request_json, parse_owner_repo


# docs/api_actions-workflows.md

def list_workflows(
    *,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
    per_page: int = 30,
    page: int = 1,
    accept: Optional[str] = None,
) -> Any:
    o, r = parse_owner_repo(owner, repo, owner_repo)
    if not o or not r:
        return {"error": "owner/repo is required (or set GITHUB_TEST_REPO)"}
    return request_json(
        "GET",
        f"/repos/{o}/{r}/actions/workflows",
        accept=accept,
        params={"per_page": per_page, "page": page},
    )


# docs/api_actions-workflows.md

def get_workflow(
    *,
    workflow_id: Union[int, str],
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
    accept: Optional[str] = None,
) -> Any:
    o, r = parse_owner_repo(owner, repo, owner_repo)
    if not o or not r:
        return {"error": "owner/repo is required (or set GITHUB_TEST_REPO)"}
    return request_json(
        "GET",
        f"/repos/{o}/{r}/actions/workflows/{workflow_id}",
        accept=accept,
    )


# docs/api_actions-workflows.md

def disable_workflow(
    *,
    workflow_id: Union[int, str],
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
    accept: Optional[str] = None,
) -> Any:
    o, r = parse_owner_repo(owner, repo, owner_repo)
    if not o or not r:
        return {"error": "owner/repo is required (or set GITHUB_TEST_REPO)"}
    return request_json(
        "PUT",
        f"/repos/{o}/{r}/actions/workflows/{workflow_id}/disable",
        accept=accept,
    )


# docs/api_actions-workflows.md

def enable_workflow(
    *,
    workflow_id: Union[int, str],
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
    accept: Optional[str] = None,
) -> Any:
    o, r = parse_owner_repo(owner, repo, owner_repo)
    if not o or not r:
        return {"error": "owner/repo is required (or set GITHUB_TEST_REPO)"}
    return request_json(
        "PUT",
        f"/repos/{o}/{r}/actions/workflows/{workflow_id}/enable",
        accept=accept,
    )


# docs/api_actions-workflows.md

def create_workflow_dispatch(
    *,
    workflow_id: Union[int, str],
    ref: str,
    inputs: Optional[Dict[str, Any]] = None,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
    accept: Optional[str] = None,
) -> Any:
    o, r = parse_owner_repo(owner, repo, owner_repo)
    if not o or not r:
        return {"error": "owner/repo is required (or set GITHUB_TEST_REPO)"}
    payload: Dict[str, Any] = {"ref": ref}
    if inputs is not None:
        payload["inputs"] = inputs
    return request_json(
        "POST",
        f"/repos/{o}/{r}/actions/workflows/{workflow_id}/dispatches",
        accept=accept,
        json=payload,
    )


# docs/api_actions-workflows.md

def get_workflow_usage(
    *,
    workflow_id: Union[int, str],
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
    accept: Optional[str] = None,
) -> Any:
    o, r = parse_owner_repo(owner, repo, owner_repo)
    if not o or not r:
        return {"error": "owner/repo is required (or set GITHUB_TEST_REPO)"}
    return request_json(
        "GET",
        f"/repos/{o}/{r}/actions/workflows/{workflow_id}/timing",
        accept=accept,
    )
