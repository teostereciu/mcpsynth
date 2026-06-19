import os
import requests
from fastmcp import tool

GITHUB_API_BASE_URL = os.environ.get("GITHUB_API_BASE_URL", "https://api.github.com")
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
HEADERS = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json",
}

def handle_response(resp):
    try:
        resp.raise_for_status()
        return resp.json()
    except requests.HTTPError as e:
        return {"error": str(e), "status_code": resp.status_code, "body": resp.text}

@tool("list_workflows")
def list_workflows(owner: str, repo: str):
    """List GitHub Actions workflows for a repository."""
    url = f"{GITHUB_API_BASE_URL}/repos/{owner}/{repo}/actions/workflows"
    resp = requests.get(url, headers=HEADERS)
    return handle_response(resp)

@tool("list_workflow_runs")
def list_workflow_runs(owner: str, repo: str, workflow_id: str):
    """List runs for a workflow."""
    url = f"{GITHUB_API_BASE_URL}/repos/{owner}/{repo}/actions/workflows/{workflow_id}/runs"
    resp = requests.get(url, headers=HEADERS)
    return handle_response(resp)

@tool("dispatch_workflow")
def dispatch_workflow(owner: str, repo: str, workflow_id: str, ref: str, inputs: dict = None):
    """Trigger a workflow dispatch event."""
    url = f"{GITHUB_API_BASE_URL}/repos/{owner}/{repo}/actions/workflows/{workflow_id}/dispatches"
    data = {"ref": ref}
    if inputs:
        data["inputs"] = inputs
    resp = requests.post(url, headers=HEADERS, json=data)
    if resp.status_code in (201, 204):
        return {"success": True}
    return handle_response(resp)
