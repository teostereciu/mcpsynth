from typing import Any, Dict, Optional

from ._client import GitHubClient


def list_workflow_runs(
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
) -> Dict[str, Any]:
    """GET /repos/{owner}/{repo}/actions/runs - List workflow runs for a repository."""
    c = GitHubClient()
    return c.request(
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
    )


def get_workflow_run(*, owner: str, repo: str, run_id: int) -> Dict[str, Any]:
    """GET /repos/{owner}/{repo}/actions/runs/{run_id} - Get a workflow run."""
    c = GitHubClient()
    return c.request("GET", f"/repos/{owner}/{repo}/actions/runs/{run_id}")


def cancel_workflow_run(*, owner: str, repo: str, run_id: int) -> Dict[str, Any]:
    """POST /repos/{owner}/{repo}/actions/runs/{run_id}/cancel - Cancel a workflow run."""
    c = GitHubClient()
    return c.request("POST", f"/repos/{owner}/{repo}/actions/runs/{run_id}/cancel")


def rerun_workflow_run(*, owner: str, repo: str, run_id: int, enable_debug_logging: bool = False) -> Dict[str, Any]:
    """POST /repos/{owner}/{repo}/actions/runs/{run_id}/rerun - Re-run a workflow run."""
    c = GitHubClient()
    payload = {"enable_debug_logging": enable_debug_logging}
    return c.request("POST", f"/repos/{owner}/{repo}/actions/runs/{run_id}/rerun", json=payload)


def rerun_job(*, owner: str, repo: str, job_id: int, enable_debug_logging: bool = False) -> Dict[str, Any]:
    """POST /repos/{owner}/{repo}/actions/jobs/{job_id}/rerun - Re-run a job from a workflow run."""
    c = GitHubClient()
    payload = {"enable_debug_logging": enable_debug_logging}
    return c.request("POST", f"/repos/{owner}/{repo}/actions/jobs/{job_id}/rerun", json=payload)
