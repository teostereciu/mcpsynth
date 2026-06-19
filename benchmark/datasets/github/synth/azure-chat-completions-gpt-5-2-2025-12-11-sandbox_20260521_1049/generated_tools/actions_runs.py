from typing import Any, Optional

from .http_client import request_json


def list_workflow_runs_for_repo(
    *,
    owner: str,
    repo: str,
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
) -> Any:
    """GET /repos/{owner}/{repo}/actions/runs - List workflow runs for a repository."""
    _, data, _ = request_json(
        "GET",
        f"/repos/{owner}/{repo}/actions/runs",
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
        accept=accept,
    )
    return data


def get_workflow_run(
    *,
    owner: str,
    repo: str,
    run_id: int,
    accept: str = "application/vnd.github+json",
) -> Any:
    """GET /repos/{owner}/{repo}/actions/runs/{run_id} - Get a workflow run."""
    _, data, _ = request_json("GET", f"/repos/{owner}/{repo}/actions/runs/{run_id}", accept=accept)
    return data


def cancel_workflow_run(
    *,
    owner: str,
    repo: str,
    run_id: int,
    accept: str = "application/vnd.github+json",
) -> Any:
    """POST /repos/{owner}/{repo}/actions/runs/{run_id}/cancel - Cancel a workflow run."""
    _, data, _ = request_json("POST", f"/repos/{owner}/{repo}/actions/runs/{run_id}/cancel", accept=accept)
    return {"cancel_requested": True} if data is None else data


def rerun_workflow_run(
    *,
    owner: str,
    repo: str,
    run_id: int,
    enable_debug_logging: bool = False,
    accept: str = "application/vnd.github+json",
) -> Any:
    """POST /repos/{owner}/{repo}/actions/runs/{run_id}/rerun - Re-run a workflow."""
    _, data, _ = request_json(
        "POST",
        f"/repos/{owner}/{repo}/actions/runs/{run_id}/rerun",
        json_body={"enable_debug_logging": enable_debug_logging},
        accept=accept,
    )
    return {"rerun_requested": True} if data is None else data


def rerun_job(
    *,
    owner: str,
    repo: str,
    job_id: int,
    enable_debug_logging: bool = False,
    accept: str = "application/vnd.github+json",
) -> Any:
    """POST /repos/{owner}/{repo}/actions/jobs/{job_id}/rerun - Re-run a job from a workflow run."""
    _, data, _ = request_json(
        "POST",
        f"/repos/{owner}/{repo}/actions/jobs/{job_id}/rerun",
        json_body={"enable_debug_logging": enable_debug_logging},
        accept=accept,
    )
    return data
