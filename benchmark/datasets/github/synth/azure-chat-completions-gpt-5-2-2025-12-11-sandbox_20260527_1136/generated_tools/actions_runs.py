from typing import Any, Dict, Optional

from .http_client import request_json, parse_owner_repo


# docs/api_actions-workflow-runs.md

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
    accept: Optional[str] = None,
) -> Any:
    o, r = parse_owner_repo(owner, repo, owner_repo)
    if not o or not r:
        return {"error": "owner/repo is required (or set GITHUB_TEST_REPO)"}

    return request_json(
        "GET",
        f"/repos/{o}/{r}/actions/runs",
        accept=accept,
        params={
            "actor": actor,
            "branch": branch,
            "event": event,
            "status": status,
            "created": created,
            "exclude_pull_requests": exclude_pull_requests,
            "check_suite_id": check_suite_id,
            "head_sha": head_sha,
            "per_page": per_page,
            "page": page,
        },
    )


# docs/api_actions-workflow-runs.md

def get_workflow_run(
    *,
    run_id: int,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
    accept: Optional[str] = None,
) -> Any:
    o, r = parse_owner_repo(owner, repo, owner_repo)
    if not o or not r:
        return {"error": "owner/repo is required (or set GITHUB_TEST_REPO)"}
    return request_json("GET", f"/repos/{o}/{r}/actions/runs/{run_id}", accept=accept)


# docs/api_actions-workflow-runs.md

def cancel_workflow_run(
    *,
    run_id: int,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
    accept: Optional[str] = None,
) -> Any:
    o, r = parse_owner_repo(owner, repo, owner_repo)
    if not o or not r:
        return {"error": "owner/repo is required (or set GITHUB_TEST_REPO)"}
    return request_json("POST", f"/repos/{o}/{r}/actions/runs/{run_id}/cancel", accept=accept)


# docs/api_actions-workflow-runs.md

def rerun_workflow_run(
    *,
    run_id: int,
    enable_debug_logging: Optional[bool] = None,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
    accept: Optional[str] = None,
) -> Any:
    o, r = parse_owner_repo(owner, repo, owner_repo)
    if not o or not r:
        return {"error": "owner/repo is required (or set GITHUB_TEST_REPO)"}
    payload: Dict[str, Any] = {}
    if enable_debug_logging is not None:
        payload["enable_debug_logging"] = enable_debug_logging
    return request_json(
        "POST",
        f"/repos/{o}/{r}/actions/runs/{run_id}/rerun",
        accept=accept,
        json=payload if payload else None,
    )


# docs/api_actions-workflow-runs.md

def rerun_workflow_job(
    *,
    job_id: int,
    enable_debug_logging: Optional[bool] = None,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
    accept: Optional[str] = None,
) -> Any:
    o, r = parse_owner_repo(owner, repo, owner_repo)
    if not o or not r:
        return {"error": "owner/repo is required (or set GITHUB_TEST_REPO)"}
    payload: Dict[str, Any] = {}
    if enable_debug_logging is not None:
        payload["enable_debug_logging"] = enable_debug_logging
    return request_json(
        "POST",
        f"/repos/{o}/{r}/actions/jobs/{job_id}/rerun",
        accept=accept,
        json=payload if payload else None,
    )
