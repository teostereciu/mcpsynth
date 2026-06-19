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
    created: Optional[str] = None,
    exclude_pull_requests: Optional[bool] = None,
    check_suite_id: Optional[int] = None,
    head_sha: Optional[str] = None,
    per_page: int = 30,
    page: int = 1,
) -> Any:
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
    return client.request("GET", f"/repos/{owner}/{repo}/actions/runs", params=params)


def get_workflow_run(client: GitHubClient, *, owner: str, repo: str, run_id: int) -> Any:
    return client.request("GET", f"/repos/{owner}/{repo}/actions/runs/{run_id}")


def cancel_workflow_run(client: GitHubClient, *, owner: str, repo: str, run_id: int) -> Any:
    return client.request("POST", f"/repos/{owner}/{repo}/actions/runs/{run_id}/cancel")


def rerun_workflow_run(client: GitHubClient, *, owner: str, repo: str, run_id: int, enable_debug_logging: bool = False) -> Any:
    payload = {"enable_debug_logging": enable_debug_logging}
    return client.request("POST", f"/repos/{owner}/{repo}/actions/runs/{run_id}/rerun", json=payload)


def rerun_workflow_job(client: GitHubClient, *, owner: str, repo: str, job_id: int, enable_debug_logging: bool = False) -> Any:
    payload = {"enable_debug_logging": enable_debug_logging}
    return client.request("POST", f"/repos/{owner}/{repo}/actions/jobs/{job_id}/rerun", json=payload)
