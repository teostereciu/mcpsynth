import os
import requests
from typing import Any, Dict, List, Optional

CLOCKIFY_API_KEY = os.environ.get("CLOCKIFY_API_KEY")
BASE_URL = "https://api.clockify.me/api/v1"
HEADERS = {"X-Api-Key": CLOCKIFY_API_KEY}

def list_time_entries(workspaceId: str, userId: str, page: int = 1, page_size: int = 50) -> Any:
    """List time entries for a user in a workspace."""
    try:
        params = {"page": page, "page-size": page_size}
        resp = requests.get(f"{BASE_URL}/workspaces/{workspaceId}/users/{userId}/time-entries", headers=HEADERS, params=params)
        return resp.json()
    except Exception as e:
        return {"error": str(e)}

def create_time_entry(workspaceId: str, billable: bool, start: str, end: Optional[str] = None, projectId: Optional[str] = None, description: Optional[str] = None, tagIds: Optional[List[str]] = None, taskId: Optional[str] = None, type: Optional[str] = None) -> Any:
    """Create a new time entry in a workspace."""
    try:
        data = {"billable": billable, "start": start}
        if end:
            data["end"] = end
        if projectId:
            data["projectId"] = projectId
        if description:
            data["description"] = description
        if tagIds:
            data["tagIds"] = tagIds
        if taskId:
            data["taskId"] = taskId
        if type:
            data["type"] = type
        resp = requests.post(f"{BASE_URL}/workspaces/{workspaceId}/time-entries", headers=HEADERS, json=data)
        return resp.json()
    except Exception as e:
        return {"error": str(e)}

def update_time_entry(workspaceId: str, id: str, start: str, billable: Optional[bool] = None, end: Optional[str] = None, projectId: Optional[str] = None, description: Optional[str] = None, tagIds: Optional[List[str]] = None, taskId: Optional[str] = None, type: Optional[str] = None) -> Any:
    """Update a time entry in a workspace."""
    try:
        data = {"start": start}
        if billable is not None:
            data["billable"] = billable
        if end:
            data["end"] = end
        if projectId:
            data["projectId"] = projectId
        if description:
            data["description"] = description
        if tagIds:
            data["tagIds"] = tagIds
        if taskId:
            data["taskId"] = taskId
        if type:
            data["type"] = type
        resp = requests.put(f"{BASE_URL}/workspaces/{workspaceId}/time-entries/{id}", headers=HEADERS, json=data)
        return resp.json()
    except Exception as e:
        return {"error": str(e)}

def delete_time_entry(workspaceId: str, id: str) -> Any:
    """Delete a time entry from a workspace."""
    try:
        resp = requests.delete(f"{BASE_URL}/workspaces/{workspaceId}/time-entries/{id}", headers=HEADERS)
        if resp.status_code in [200, 204]:
            return {"success": True}
        else:
            return {"error": resp.text}
    except Exception as e:
        return {"error": str(e)}

def stop_running_timer(workspaceId: str, userId: str, end: str) -> Any:
    """Stop a currently running timer for a user on a workspace."""
    try:
        data = {"end": end}
        resp = requests.post(f"{BASE_URL}/workspaces/{workspaceId}/users/{userId}/time-entries/end", headers=HEADERS, json=data)
        return resp.json()
    except Exception as e:
        return {"error": str(e)}