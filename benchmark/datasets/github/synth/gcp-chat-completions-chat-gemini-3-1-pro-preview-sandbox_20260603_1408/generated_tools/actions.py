from typing import Any, Dict, List, Optional, Union
from .client import make_request

def list_repository_workflows(owner: str, repo: str) -> Any:
    """List repository workflows."""
    return make_request("GET", f"/repos/{owner}/{repo}/actions/workflows")

def list_workflow_runs(owner: str, repo: str) -> Any:
    """List workflow runs for a repository."""
    return make_request("GET", f"/repos/{owner}/{repo}/actions/runs")

def create_workflow_dispatch(owner: str, repo: str, workflow_id: Union[int, str], ref: str, inputs: Optional[Dict[str, str]] = None) -> Any:
    """Create a workflow dispatch event."""
    data = {"ref": ref}
    if inputs is not None: data["inputs"] = inputs
    return make_request("POST", f"/repos/{owner}/{repo}/actions/workflows/{workflow_id}/dispatches", json=data)
