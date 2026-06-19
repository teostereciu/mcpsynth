import os
import requests
from typing import Any, Dict, List, Optional

CLOCKIFY_API_KEY = os.environ.get("CLOCKIFY_API_KEY")
BASE_URL = "https://api.clockify.me/api/v1"
HEADERS = {"X-Api-Key": CLOCKIFY_API_KEY}

def list_tasks(workspaceId: str, projectId: str, page: int = 1, page_size: int = 50) -> Any:
    """List tasks in a project."""
    try:
        params = {"page": page, "page-size": page_size}
        resp = requests.get(f"{BASE_URL}/workspaces/{workspaceId}/projects/{projectId}/tasks", headers=HEADERS, params=params)
        return resp.json()
    except Exception as e:
        return {"error": str(e)}

def create_task(workspaceId: str, projectId: str, name: str, assigneeIds: Optional[List[str]] = None, estimate: Optional[str] = None, budgetEstimate: Optional[int] = None, status: Optional[str] = None, userGroupIds: Optional[List[str]] = None) -> Any:
    """Create a new task in a project."""
    try:
        data = {"name": name}
        if assigneeIds:
            data["assigneeIds"] = assigneeIds
        if estimate:
            data["estimate"] = estimate
        if budgetEstimate:
            data["budgetEstimate"] = budgetEstimate
        if status:
            data["status"] = status
        if userGroupIds:
            data["userGroupIds"] = userGroupIds
        resp = requests.post(f"{BASE_URL}/workspaces/{workspaceId}/projects/{projectId}/tasks", headers=HEADERS, json=data)
        return resp.json()
    except Exception as e:
        return {"error": str(e)}