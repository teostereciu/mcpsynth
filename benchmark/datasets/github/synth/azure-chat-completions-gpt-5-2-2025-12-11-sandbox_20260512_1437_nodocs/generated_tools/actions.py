from typing import Any, Dict, Optional

from ._client import gh_request


def list_workflows(owner: str, repo: str, *, per_page: int = 30, page: int = 1) -> Any:
    return gh_request("GET", f"/repos/{owner}/{repo}/actions/workflows", params={"per_page": per_page, "page": page})


def get_workflow(owner: str, repo: str, workflow_id: str) -> Any:
    return gh_request("GET", f"/repos/{owner}/{repo}/actions/workflows/{workflow_id}")


def list_workflow_runs(owner: str, repo: str, *, workflow_id: Optional[str] = None, actor: Optional[str] = None, branch: Optional[str] = None, event: Optional[str] = None, status: Optional[str] = None, per_page: int = 30, page: int = 1) -> Any:
    params: Dict[str, Any] = {"per_page": per_page, "page": page}
    if actor:
        params["actor"] = actor
    if branch:
        params["branch"] = branch
    if event:
        params["event"] = event
    if status:
        params["status"] = status
    if workflow_id:
        return gh_request("GET", f"/repos/{owner}/{repo}/actions/workflows/{workflow_id}/runs", params=params)
    return gh_request("GET", f"/repos/{owner}/{repo}/actions/runs", params=params)


def get_workflow_run(owner: str, repo: str, run_id: int) -> Any:
    return gh_request("GET", f"/repos/{owner}/{repo}/actions/runs/{run_id}")


def rerun_workflow_run(owner: str, repo: str, run_id: int) -> Any:
    return gh_request("POST", f"/repos/{owner}/{repo}/actions/runs/{run_id}/rerun")


def cancel_workflow_run(owner: str, repo: str, run_id: int) -> Any:
    return gh_request("POST", f"/repos/{owner}/{repo}/actions/runs/{run_id}/cancel")


def list_workflow_run_jobs(owner: str, repo: str, run_id: int, *, per_page: int = 30, page: int = 1) -> Any:
    return gh_request("GET", f"/repos/{owner}/{repo}/actions/runs/{run_id}/jobs", params={"per_page": per_page, "page": page})
