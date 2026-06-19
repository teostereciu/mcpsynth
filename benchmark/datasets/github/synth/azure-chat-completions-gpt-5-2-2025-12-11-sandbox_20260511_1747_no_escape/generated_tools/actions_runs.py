from typing import Any, Dict, List, Optional, Union

from .http_client import GitHubClient, parse_owner_repo


def list_workflow_runs(
    *,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
    actor: Optional[str] = None,
    branch: Optional[str] = None,
    event: Optional[str] = None,
    status: Optional[str] = None,
    created: Optional[str] = None,
    exclude_pull_requests: Optional[bool] = None,
    check_suite_id: Optional[int] = None,
    head_sha: Optional[str] = None,
    per_page: int = 30,
    page: int = 1,
    accept: str = "application/vnd.github+json",
) -> Union[Dict[str, Any], List[Any], str]:
    """GET /repos/{owner}/{repo}/actions/runs"""
    o, r = parse_owner_repo(owner, repo, owner_repo)
    client = GitHubClient()
    params: Dict[str, Any] = {"per_page": per_page, "page": page}
    for k, v in {
        "actor": actor,
        "branch": branch,
        "event": event,
        "status": status,
        "created": created,
        "exclude_pull_requests": exclude_pull_requests,
        "check_suite_id": check_suite_id,
        "head_sha": head_sha,
    }.items():
        if v is not None:
            params[k] = v
    return client.request("GET", f"/repos/{o}/{r}/actions/runs", params=params, accept=accept)


def get_workflow_run(
    *,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
    run_id: int,
    accept: str = "application/vnd.github+json",
) -> Union[Dict[str, Any], List[Any], str]:
    """GET /repos/{owner}/{repo}/actions/runs/{run_id}"""
    o, r = parse_owner_repo(owner, repo, owner_repo)
    client = GitHubClient()
    return client.request("GET", f"/repos/{o}/{r}/actions/runs/{run_id}", accept=accept)


def cancel_workflow_run(
    *,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
    run_id: int,
    accept: str = "application/vnd.github+json",
) -> Union[Dict[str, Any], List[Any], str]:
    """POST /repos/{owner}/{repo}/actions/runs/{run_id}/cancel"""
    o, r = parse_owner_repo(owner, repo, owner_repo)
    client = GitHubClient()
    return client.request("POST", f"/repos/{o}/{r}/actions/runs/{run_id}/cancel", accept=accept)


def rerun_workflow_run(
    *,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
    run_id: int,
    enable_debug_logging: Optional[bool] = None,
    accept: str = "application/vnd.github+json",
) -> Union[Dict[str, Any], List[Any], str]:
    """POST /repos/{owner}/{repo}/actions/runs/{run_id}/rerun"""
    o, r = parse_owner_repo(owner, repo, owner_repo)
    client = GitHubClient()
    payload: Dict[str, Any] = {}
    if enable_debug_logging is not None:
        payload["enable_debug_logging"] = enable_debug_logging
    return client.request("POST", f"/repos/{o}/{r}/actions/runs/{run_id}/rerun", json=payload or None, accept=accept)


def rerun_workflow_job(
    *,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
    job_id: int,
    enable_debug_logging: Optional[bool] = None,
    accept: str = "application/vnd.github+json",
) -> Union[Dict[str, Any], List[Any], str]:
    """POST /repos/{owner}/{repo}/actions/jobs/{job_id}/rerun"""
    o, r = parse_owner_repo(owner, repo, owner_repo)
    client = GitHubClient()
    payload: Dict[str, Any] = {}
    if enable_debug_logging is not None:
        payload["enable_debug_logging"] = enable_debug_logging
    return client.request("POST", f"/repos/{o}/{r}/actions/jobs/{job_id}/rerun", json=payload or None, accept=accept)
