from typing import Any, Optional

from generated_tools.github_common import clean_params, github_request


def list_workflows(owner: str, repo: str, per_page: int = 30, page: int = 1) -> Any:
    return github_request("GET", f"/repos/{owner}/{repo}/actions/workflows", params=clean_params(per_page=per_page, page=page))


def get_workflow(owner: str, repo: str, workflow_id: str) -> Any:
    return github_request("GET", f"/repos/{owner}/{repo}/actions/workflows/{workflow_id}")


def list_workflow_runs(owner: str, repo: str, workflow_id: Optional[str] = None, actor: Optional[str] = None, branch: Optional[str] = None, event: Optional[str] = None, status: Optional[str] = None, per_page: int = 30, page: int = 1) -> Any:
    params = clean_params(actor=actor, branch=branch, event=event, status=status, per_page=per_page, page=page)
    path = f"/repos/{owner}/{repo}/actions/runs" if workflow_id is None else f"/repos/{owner}/{repo}/actions/workflows/{workflow_id}/runs"
    return github_request("GET", path, params=params)


def get_workflow_run(owner: str, repo: str, run_id: int) -> Any:
    return github_request("GET", f"/repos/{owner}/{repo}/actions/runs/{run_id}")


def rerun_workflow_run(owner: str, repo: str, run_id: int, enable_debug_logging: Optional[bool] = None) -> Any:
    return github_request("POST", f"/repos/{owner}/{repo}/actions/runs/{run_id}/rerun", json_body=clean_params(enable_debug_logging=enable_debug_logging))


def cancel_workflow_run(owner: str, repo: str, run_id: int) -> Any:
    return github_request("POST", f"/repos/{owner}/{repo}/actions/runs/{run_id}/cancel")


def dispatch_workflow(owner: str, repo: str, workflow_id: str, ref: str, inputs: Optional[dict] = None) -> Any:
    return github_request("POST", f"/repos/{owner}/{repo}/actions/workflows/{workflow_id}/dispatches", json_body=clean_params(ref=ref, inputs=inputs))
