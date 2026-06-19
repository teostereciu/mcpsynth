"""GitHub Deployments and Deployment Statuses tools."""
import os
import requests
from mcp.server.fastmcp import FastMCP

BASE_URL = os.environ.get("GITHUB_API_BASE_URL", "https://api.github.com")
TOKEN = os.environ.get("GITHUB_TOKEN", "")

def _headers():
    h = {"Accept": "application/vnd.github+json", "X-GitHub-Api-Version": "2022-11-28"}
    if TOKEN:
        h["Authorization"] = f"Bearer {TOKEN}"
    return h

def _get(path, params=None):
    try:
        r = requests.get(f"{BASE_URL}{path}", headers=_headers(), params=params, timeout=30)
        if r.status_code == 204:
            return {"status": "no_content"}
        return r.json()
    except Exception as e:
        return {"error": str(e)}

def _post(path, json=None):
    try:
        r = requests.post(f"{BASE_URL}{path}", headers=_headers(), json=json, timeout=30)
        if r.status_code == 204:
            return {"status": "no_content"}
        return r.json()
    except Exception as e:
        return {"error": str(e)}

def _delete(path, json=None):
    try:
        r = requests.delete(f"{BASE_URL}{path}", headers=_headers(), json=json, timeout=30)
        if r.status_code == 204:
            return {"status": "no_content"}
        return r.json()
    except Exception as e:
        return {"error": str(e)}


def register_deployments_tools(mcp: FastMCP):

    @mcp.tool()
    def list_deployments(owner: str, repo: str, sha: str = "", ref: str = "",
                         task: str = "", environment: str = "",
                         per_page: int = 30, page: int = 1) -> dict:
        """List deployments for a repository."""
        params = {"per_page": per_page, "page": page}
        if sha:
            params["sha"] = sha
        if ref:
            params["ref"] = ref
        if task:
            params["task"] = task
        if environment:
            params["environment"] = environment
        return _get(f"/repos/{owner}/{repo}/deployments", params)

    @mcp.tool()
    def get_deployment(owner: str, repo: str, deployment_id: int) -> dict:
        """Get a deployment by ID."""
        return _get(f"/repos/{owner}/{repo}/deployments/{deployment_id}")

    @mcp.tool()
    def create_deployment(owner: str, repo: str, ref: str,
                          task: str = "deploy", environment: str = "production",
                          description: str = "", auto_merge: bool = True,
                          required_contexts: list = None,
                          payload: dict = None,
                          transient_environment: bool = False,
                          production_environment: bool = None) -> dict:
        """Create a deployment. ref can be a branch, tag, or SHA."""
        deploy_payload = {
            "ref": ref,
            "task": task,
            "environment": environment,
            "auto_merge": auto_merge,
            "transient_environment": transient_environment,
        }
        if description:
            deploy_payload["description"] = description
        if required_contexts is not None:
            deploy_payload["required_contexts"] = required_contexts
        if payload is not None:
            deploy_payload["payload"] = payload
        if production_environment is not None:
            deploy_payload["production_environment"] = production_environment
        return _post(f"/repos/{owner}/{repo}/deployments", deploy_payload)

    @mcp.tool()
    def delete_deployment(owner: str, repo: str, deployment_id: int) -> dict:
        """Delete a deployment. Only inactive deployments can be deleted."""
        return _delete(f"/repos/{owner}/{repo}/deployments/{deployment_id}")

    @mcp.tool()
    def list_deployment_statuses(owner: str, repo: str, deployment_id: int,
                                 per_page: int = 30, page: int = 1) -> dict:
        """List statuses for a deployment."""
        return _get(f"/repos/{owner}/{repo}/deployments/{deployment_id}/statuses",
                    {"per_page": per_page, "page": page})

    @mcp.tool()
    def get_deployment_status(owner: str, repo: str, deployment_id: int,
                              status_id: int) -> dict:
        """Get a deployment status."""
        return _get(f"/repos/{owner}/{repo}/deployments/{deployment_id}/statuses/{status_id}")

    @mcp.tool()
    def create_deployment_status(owner: str, repo: str, deployment_id: int,
                                 state: str, log_url: str = "",
                                 description: str = "", environment: str = "",
                                 environment_url: str = "",
                                 auto_inactive: bool = True) -> dict:
        """Create a deployment status.
        state: error|failure|inactive|in_progress|queued|pending|success."""
        payload = {"state": state, "auto_inactive": auto_inactive}
        if log_url:
            payload["log_url"] = log_url
        if description:
            payload["description"] = description
        if environment:
            payload["environment"] = environment
        if environment_url:
            payload["environment_url"] = environment_url
        return _post(f"/repos/{owner}/{repo}/deployments/{deployment_id}/statuses", payload)

    @mcp.tool()
    def list_deployment_environments(owner: str, repo: str,
                                     per_page: int = 30, page: int = 1) -> dict:
        """List environments for a repository."""
        return _get(f"/repos/{owner}/{repo}/environments",
                    {"per_page": per_page, "page": page})

    @mcp.tool()
    def get_deployment_environment(owner: str, repo: str, environment_name: str) -> dict:
        """Get a deployment environment."""
        return _get(f"/repos/{owner}/{repo}/environments/{environment_name}")

    @mcp.tool()
    def delete_deployment_environment(owner: str, repo: str, environment_name: str) -> dict:
        """Delete a deployment environment."""
        return _delete(f"/repos/{owner}/{repo}/environments/{environment_name}")
