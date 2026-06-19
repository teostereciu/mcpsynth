from typing import Any, Dict, Optional

from .github_client import GitHubClient


def list_workflow_runs_for_repo(
    client: GitHubClient,
    *,
    owner: str,
    repo: str,
    actor: Optional[str] = None,
    branch: Optional[str] = None,
    event: Optional[str] = None,
    status: Optional[str] = None,
    per_page: int = 30,
    page: int = 1,
    created: Optional[str] = None,
    exclude_pull_requests: bool = False,
    check_suite_id: Optional[int] = None,
    head_sha: Optional[str] = None,
) -> Any:
    params: Dict[str, Any] = {"per_page": per_page, "page": page}
    if actor is not None:
        params["actor"] = actor
    if branch is not None:
        params["branch"] = branch
    if event is not None:
        params["event"] = event
    if status is not None:
        params["status"] = status
    if created is not None:
        params["created"] = created
    if exclude_pull_requests:
        params["exclude_pull_requests"] = True
    if check_suite_id is not None:
        params["check_suite_id"] = check_suite_id
    if head_sha is not None:
        params["head_sha"] = head_sha

    return client.request("GET", f"/repos/{owner}/{repo}/actions/runs", params=params)


def get_workflow_run(client: GitHubClient, *, owner: str, repo: str, run_id: int) -> Any:
    return client.request("GET", f"/repos/{owner}/{repo}/actions/runs/{run_id}")


def cancel_workflow_run(client: GitHubClient, *, owner: str, repo: str, run_id: int) -> Any:
    return client.request("POST", f"/repos/{owner}/{repo}/actions/runs/{run_id}/cancel")


def rerun_workflow_run(client: GitHubClient, *, owner: str, repo: str, run_id: int) -> Any:
    return client.request("POST", f"/repos/{owner}/{repo}/actions/runs/{run_id}/rerun")


def rerun_job(client: GitHubClient, *, owner: str, repo: str, job_id: int, enable_debug_logging: bool = False) -> Any:
    payload: Dict[str, Any] = {"enable_debug_logging": enable_debug_logging}
    return client.request("POST", f"/repos/{owner}/{repo}/actions/jobs/{job_id}/rerun", json=payload)
