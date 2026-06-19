from mcp_server import mcp
from github_client import make_request

@mcp.tool()
def list_workflows(owner: str, repo: str, per_page: int = 30, page: int = 1) -> dict:
    """List workflows in a repository."""
    return make_request("GET", f"/repos/{owner}/{repo}/actions/workflows", params={"per_page": per_page, "page": page})

@mcp.tool()
def list_workflow_runs(owner: str, repo: str, per_page: int = 30, page: int = 1) -> dict:
    """List workflow runs for a repository."""
    return make_request("GET", f"/repos/{owner}/{repo}/actions/runs", params={"per_page": per_page, "page": page})

@mcp.tool()
def create_workflow_dispatch(owner: str, repo: str, workflow_id: str, ref: str, inputs: dict = None) -> dict:
    """Create a workflow dispatch event."""
    payload = {"ref": ref}
    if inputs: payload["inputs"] = inputs
    return make_request("POST", f"/repos/{owner}/{repo}/actions/workflows/{workflow_id}/dispatches", json=payload)
