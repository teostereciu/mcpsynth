from typing import Any, Dict, Optional

from .github_client import GitHubClient


def list_workflow_runs(
    client: GitHubClient,
    *,
    owner: str,
    repo: str,
    actor: Optional[str] = None,
    branch: Optional[str] = None,
    event: Optional[str] = None,
    status: Optional[str] = None,
    per_page: Optional[int] = None,
    page: Optional[int] = None,
    created: Optional[str] = None,
    exclude_pull_requests: Optional[bool] = None,
    check_suite_id: Optional[int] = None,
    head_sha: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /repos/{owner}/{repo}/actions/runs"""
    return client.request(
        "GET",
        f"/repos/{owner}/{repo}/actions/runs",
        params={
            "actor": actor,
            "branch": branch,
            "event": event,
            "status": status,
            "per_page": per_page,
            "page": page,
            "created": created,
            "exclude_pull_requests": exclude_pull_requests,
            "check_suite_id": check_suite_id,
            "head_sha": head_sha,
        },
    )


def get_workflow_run(client: GitHubClient, *, owner: str, repo: str, run_id: int) -> Dict[str, Any]:
    """GET /repos/{owner}/{repo}/actions/runs/{run_id}"""
    return client.request("GET", f"/repos/{owner}/{repo}/actions/runs/{run_id}")


def cancel_workflow_run(client: GitHubClient, *, owner: str, repo: str, run_id: int) -> Dict[str, Any]:
    """POST /repos/{owner}/{repo}/actions/runs/{run_id}/cancel"""
    return client.request("POST", f"/repos/{owner}/{repo}/actions/runs/{run_id}/cancel")


def rerun_workflow_run(
    client: GitHubClient,
    *,
    owner: str,
    repo: str,
    run_id: int,
    enable_debug_logging: Optional[bool] = None,
) -> Dict[str, Any]:
    """POST /repos/{owner}/{repo}/actions/runs/{run_id}/rerun"""
    payload: Dict[str, Any] = {}
    if enable_debug_logging is not None:
        payload["enable_debug_logging"] = enable_debug_logging
    return client.request("POST", f"/repos/{owner}/{repo}/actions/runs/{run_id}/rerun", json=payload if payload else None)


def rerun_job(
    client: GitHubClient,
    *,
    owner: str,
    repo: str,
    job_id: int,
    enable_debug_logging: Optional[bool] = None,
) -> Dict[str, Any]:
    """POST /repos/{owner}/{repo}/actions/jobs/{job_id}/rerun"""
    payload: Dict[str, Any] = {}
    if enable_debug_logging is not None:
        payload["enable_debug_logging"] = enable_debug_logging
    return client.request("POST", f"/repos/{owner}/{repo}/actions/jobs/{job_id}/rerun", json=payload if payload else None)
