from typing import Any, Dict, List, Optional, Union
from github_client import client

def list_workflows(
    owner: str,
    repo: str,
    per_page: Optional[int] = 30,
    page: Optional[int] = 1
) -> Union[List[Dict[str, Any]], Dict[str, Any]]:
    """
    List repository workflows.
    
    Parameters:
    - owner: The account owner of the repository.
    - repo: The name of the repository.
    - per_page: The number of results per page (max 100).
    - page: Page number of the results to fetch.
    """
    params = {"per_page": per_page, "page": page}
    return client.request("GET", f"/repos/{owner}/{repo}/actions/workflows", params=params)

def get_workflow(owner: str, repo: str, workflow_id: Union[int, str]) -> Union[Dict[str, Any], List[Dict[str, Any]]]:
    """
    Get a workflow.
    
    Parameters:
    - owner: The account owner of the repository.
    - repo: The name of the repository.
    - workflow_id: The ID of the workflow or the workflow file name.
    """
    return client.request("GET", f"/repos/{owner}/{repo}/actions/workflows/{workflow_id}")

def list_workflow_runs(
    owner: str,
    repo: str,
    workflow_id: Optional[Union[int, str]] = None,
    actor: Optional[str] = None,
    branch: Optional[str] = None,
    event: Optional[str] = None,
    status: Optional[str] = None,
    per_page: Optional[int] = 30,
    page: Optional[int] = 1
) -> Union[List[Dict[str, Any]], Dict[str, Any]]:
    """
    List workflow runs.
    
    Parameters:
    - owner: The account owner of the repository.
    - repo: The name of the repository.
    - workflow_id: Optional ID of the workflow or the workflow file name.
    - actor: Filter runs by user who triggered them.
    - branch: Filter runs by branch.
    - event: Filter runs by event (e.g. push, pull_request).
    - status: Filter runs by status (e.g. completed, status, success).
    - per_page: The number of results per page (max 100).
    - page: Page number of the results to fetch.
    """
    params = {"per_page": per_page, "page": page}
    if actor: params["actor"] = actor
    if branch: params["branch"] = branch
    if event: params["event"] = event
    if status: params["status"] = status

    path = f"/repos/{owner}/{repo}/actions/runs"
    if workflow_id is not None:
        path = f"/repos/{owner}/{repo}/actions/workflows/{workflow_id}/runs"

    return client.request("GET", path, params=params)

def get_workflow_run(owner: str, repo: str, run_id: int) -> Union[Dict[str, Any], List[Dict[str, Any]]]:
    """
    Get a workflow run.
    
    Parameters:
    - owner: The account owner of the repository.
    - repo: The name of the repository.
    - run_id: The unique identifier of the workflow run.
    """
    return client.request("GET", f"/repos/{owner}/{repo}/actions/runs/{run_id}")

def trigger_workflow_dispatch(
    owner: str,
    repo: str,
    workflow_id: Union[int, str],
    ref: str,
    inputs: Optional[Dict[str, Any]] = None
) -> Union[Dict[str, Any], List[Dict[str, Any]]]:
    """
    Create a workflow dispatch event (trigger a workflow run).
    
    Parameters:
    - owner: The account owner of the repository.
    - repo: The name of the repository.
    - workflow_id: The ID of the workflow or the workflow file name.
    - ref: The git reference for the workflow. The reference can be a branch or tag name.
    - inputs: Input keys and values configured in the workflow file.
    """
    data = {"ref": ref}
    if inputs is not None: data["inputs"] = inputs

    return client.request("POST", f"/repos/{owner}/{repo}/actions/workflows/{workflow_id}/dispatches", json_data=data)
