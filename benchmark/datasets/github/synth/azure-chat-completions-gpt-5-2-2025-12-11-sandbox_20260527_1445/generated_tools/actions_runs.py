from typing import Any, Dict, Optional

from ._client import gh_request, parse_owner_repo


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
    per_page: Optional[int] = None,
    page: Optional[int] = None,
) -> Any:
    o, r = parse_owner_repo(owner, repo, owner_repo)
    if not o or not r:
        return {"error": "owner/repo required (or set GITHUB_TEST_REPO)"}
    return gh_request(
        "GET",
        f"/repos/{o}/{r}/actions/runs",
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


def get_workflow_run(
    *,
    run_id: int,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
) -> Any:
    o, r = parse_owner_repo(owner, repo, owner_repo)
    if not o or not r:
        return {"error": "owner/repo required (or set GITHUB_TEST_REPO)"}
    return gh_request("GET", f"/repos/{o}/{r}/actions/runs/{run_id}")


def cancel_workflow_run(
    *,
    run_id: int,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
) -> Any:
    o, r = parse_owner_repo(owner, repo, owner_repo)
    if not o or not r:
        return {"error": "owner/repo required (or set GITHUB_TEST_REPO)"}
    return gh_request("POST", f"/repos/{o}/{r}/actions/runs/{run_id}/cancel")


def rerun_workflow_run(
    *,
    run_id: int,
    enable_debug_logging: Optional[bool] = None,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
) -> Any:
    o, r = parse_owner_repo(owner, repo, owner_repo)
    if not o or not r:
        return {"error": "owner/repo required (or set GITHUB_TEST_REPO)"}
    payload: Dict[str, Any] = {}
    if enable_debug_logging is not None:
        payload["enable_debug_logging"] = enable_debug_logging
    return gh_request("POST", f"/repos/{o}/{r}/actions/runs/{run_id}/rerun", json=payload or None)


def rerun_job(
    *,
    job_id: int,
    enable_debug_logging: Optional[bool] = None,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
) -> Any:
    o, r = parse_owner_repo(owner, repo, owner_repo)
    if not o or not r:
        return {"error": "owner/repo required (or set GITHUB_TEST_REPO)"}
    payload: Dict[str, Any] = {}
    if enable_debug_logging is not None:
        payload["enable_debug_logging"] = enable_debug_logging
    return gh_request("POST", f"/repos/{o}/{r}/actions/jobs/{job_id}/rerun", json=payload or None)
