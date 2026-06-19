from typing import Any, Dict, Optional

from ._client import request_json, split_owner_repo


def list_workflow_runs(
    *,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
    actor: Optional[str] = None,
    branch: Optional[str] = None,
    event: Optional[str] = None,
    status: Optional[str] = None,
    per_page: int = 30,
    page: int = 1,
    created: Optional[str] = None,
    exclude_pull_requests: Optional[bool] = None,
    check_suite_id: Optional[int] = None,
    head_sha: Optional[str] = None,
    accept: Optional[str] = None,
) -> Any:
    """GET /repos/{owner}/{repo}/actions/runs

    Lists all workflow runs for a repository.
    """
    if owner is None or repo is None:
        parts = split_owner_repo(owner_repo)
        owner = owner or parts["owner"]
        repo = repo or parts["repo"]

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

    return request_json("GET", f"/repos/{owner}/{repo}/actions/runs", params=params, accept=accept)


def rerun_workflow_job(
    *,
    owner: Optional[str] = None,
    repo: Optional[str] = None,
    owner_repo: Optional[str] = None,
    job_id: int,
    enable_debug_logging: bool = False,
    accept: Optional[str] = None,
) -> Any:
    """POST /repos/{owner}/{repo}/actions/jobs/{job_id}/rerun

    Re-run a job and its dependent jobs in a workflow run.
    """
    if owner is None or repo is None:
        parts = split_owner_repo(owner_repo)
        owner = owner or parts["owner"]
        repo = repo or parts["repo"]

    payload = {"enable_debug_logging": enable_debug_logging}
    return request_json(
        "POST",
        f"/repos/{owner}/{repo}/actions/jobs/{job_id}/rerun",
        json=payload,
        accept=accept,
    )
