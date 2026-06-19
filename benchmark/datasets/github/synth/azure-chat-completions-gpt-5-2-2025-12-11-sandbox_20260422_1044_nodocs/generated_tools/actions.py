from typing import Any, Dict, Optional

from .github_client import GitHubClient, parse_owner_repo


def list_workflows(owner_repo: str, per_page: int = 100, max_pages: int = 3) -> Dict[str, Any]:
    try:
        owner, repo = parse_owner_repo(owner_repo)
    except ValueError as e:
        return {"error": str(e)}
    # This endpoint returns an object with workflows; no pagination helper
    params = {"per_page": per_page, "page": 1}
    return GitHubClient().request("GET", f"/repos/{owner}/{repo}/actions/workflows", params=params)


def get_workflow(owner_repo: str, workflow_id_or_file: str) -> Dict[str, Any]:
    try:
        owner, repo = parse_owner_repo(owner_repo)
    except ValueError as e:
        return {"error": str(e)}
    return GitHubClient().request("GET", f"/repos/{owner}/{repo}/actions/workflows/{workflow_id_or_file}")


def list_workflow_runs(owner_repo: str, workflow_id_or_file: Optional[str] = None, branch: Optional[str] = None, event: Optional[str] = None, status: Optional[str] = None, per_page: int = 100) -> Dict[str, Any]:
    try:
        owner, repo = parse_owner_repo(owner_repo)
    except ValueError as e:
        return {"error": str(e)}
    params: Dict[str, Any] = {"per_page": per_page}
    if branch is not None:
        params["branch"] = branch
    if event is not None:
        params["event"] = event
    if status is not None:
        params["status"] = status
    if workflow_id_or_file:
        path = f"/repos/{owner}/{repo}/actions/workflows/{workflow_id_or_file}/runs"
    else:
        path = f"/repos/{owner}/{repo}/actions/runs"
    return GitHubClient().request("GET", path, params=params)


def get_workflow_run(owner_repo: str, run_id: int) -> Dict[str, Any]:
    try:
        owner, repo = parse_owner_repo(owner_repo)
    except ValueError as e:
        return {"error": str(e)}
    return GitHubClient().request("GET", f"/repos/{owner}/{repo}/actions/runs/{run_id}")


def rerun_workflow_run(owner_repo: str, run_id: int) -> Dict[str, Any]:
    try:
        owner, repo = parse_owner_repo(owner_repo)
    except ValueError as e:
        return {"error": str(e)}
    return GitHubClient().request("POST", f"/repos/{owner}/{repo}/actions/runs/{run_id}/rerun")


def cancel_workflow_run(owner_repo: str, run_id: int) -> Dict[str, Any]:
    try:
        owner, repo = parse_owner_repo(owner_repo)
    except ValueError as e:
        return {"error": str(e)}
    return GitHubClient().request("POST", f"/repos/{owner}/{repo}/actions/runs/{run_id}/cancel")


def dispatch_workflow(owner_repo: str, workflow_id_or_file: str, ref: str, inputs: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    try:
        owner, repo = parse_owner_repo(owner_repo)
    except ValueError as e:
        return {"error": str(e)}
    payload: Dict[str, Any] = {"ref": ref}
    if inputs is not None:
        payload["inputs"] = inputs
    return GitHubClient().request("POST", f"/repos/{owner}/{repo}/actions/workflows/{workflow_id_or_file}/dispatches", json=payload)
