from typing import Any, Dict, Optional

from .http import request_json


def list_workflows(owner: str, repo: str, *, per_page: int = 30, page: int = 1) -> Any:
    return request_json("GET", f"/repos/{owner}/{repo}/actions/workflows", params={"per_page": per_page, "page": page})


def get_workflow(owner: str, repo: str, workflow_id: int) -> Any:
    return request_json("GET", f"/repos/{owner}/{repo}/actions/workflows/{workflow_id}")


def list_workflow_runs(owner: str, repo: str, *, workflow_id: Optional[int] = None, branch: Optional[str] = None, event: Optional[str] = None, status: Optional[str] = None, per_page: int = 30, page: int = 1) -> Any:
    params: Dict[str, Any] = {"per_page": per_page, "page": page}
    if branch:
        params["branch"] = branch
    if event:
        params["event"] = event
    if status:
        params["status"] = status
    if workflow_id is None:
        return request_json("GET", f"/repos/{owner}/{repo}/actions/runs", params=params)
    return request_json("GET", f"/repos/{owner}/{repo}/actions/workflows/{workflow_id}/runs", params=params)


def get_workflow_run(owner: str, repo: str, run_id: int) -> Any:
    return request_json("GET", f"/repos/{owner}/{repo}/actions/runs/{run_id}")


def rerun_workflow_run(owner: str, repo: str, run_id: int) -> Any:
    return request_json("POST", f"/repos/{owner}/{repo}/actions/runs/{run_id}/rerun")


def cancel_workflow_run(owner: str, repo: str, run_id: int) -> Any:
    return request_json("POST", f"/repos/{owner}/{repo}/actions/runs/{run_id}/cancel")


def dispatch_workflow(owner: str, repo: str, workflow_id: int, ref: str, *, inputs: Optional[Dict[str, Any]] = None) -> Any:
    payload: Dict[str, Any] = {"ref": ref}
    if inputs is not None:
        payload["inputs"] = inputs
    return request_json("POST", f"/repos/{owner}/{repo}/actions/workflows/{workflow_id}/dispatches", json=payload)
