import os
import requests
from typing import Any, Dict, List, Optional

CLOCKIFY_API_KEY = os.environ.get("CLOCKIFY_API_KEY")
BASE_URL = "https://api.clockify.me/api/v1"
HEADERS = {"X-Api-Key": CLOCKIFY_API_KEY}

def list_projects(workspaceId: str, page: int = 1, page_size: int = 50) -> Any:
    """List projects in a workspace."""
    try:
        params = {"page": page, "page-size": page_size}
        resp = requests.get(f"{BASE_URL}/workspaces/{workspaceId}/projects", headers=HEADERS, params=params)
        return resp.json()
    except Exception as e:
        return {"error": str(e)}

def create_project(workspaceId: str, name: str, billable: bool = False, clientId: Optional[str] = None, color: Optional[str] = None, isPublic: bool = False, note: Optional[str] = None) -> Any:
    """Create a new project in a workspace."""
    try:
        data = {"name": name, "billable": billable, "isPublic": isPublic}
        if clientId:
            data["clientId"] = clientId
        if color:
            data["color"] = color
        if note:
            data["note"] = note
        resp = requests.post(f"{BASE_URL}/workspaces/{workspaceId}/projects", headers=HEADERS, json=data)
        return resp.json()
    except Exception as e:
        return {"error": str(e)}

def update_project(workspaceId: str, projectId: str, name: Optional[str] = None, billable: Optional[bool] = None, archived: Optional[bool] = None, clientId: Optional[str] = None, color: Optional[str] = None, isPublic: Optional[bool] = None, note: Optional[str] = None) -> Any:
    """Update a project in a workspace."""
    try:
        data = {}
        if name is not None:
            data["name"] = name
        if billable is not None:
            data["billable"] = billable
        if archived is not None:
            data["archived"] = archived
        if clientId is not None:
            data["clientId"] = clientId
        if color is not None:
            data["color"] = color
        if isPublic is not None:
            data["isPublic"] = isPublic
        if note is not None:
            data["note"] = note
        resp = requests.put(f"{BASE_URL}/workspaces/{workspaceId}/projects/{projectId}", headers=HEADERS, json=data)
        return resp.json()
    except Exception as e:
        return {"error": str(e)}

def delete_project(workspaceId: str, projectId: str) -> Any:
    """Delete a project from a workspace."""
    try:
        resp = requests.delete(f"{BASE_URL}/workspaces/{workspaceId}/projects/{projectId}", headers=HEADERS)
        if resp.status_code == 200:
            return {"success": True}
        else:
            return {"error": resp.text}
    except Exception as e:
        return {"error": str(e)}