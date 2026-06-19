import os
import requests
from typing import Any, Dict, List, Optional

CLOCKIFY_API_KEY = os.environ.get("CLOCKIFY_API_KEY")
BASE_URL = "https://api.clockify.me/api/v1"
HEADERS = {"X-Api-Key": CLOCKIFY_API_KEY}

def get_current_user(include_memberships: bool = False) -> Any:
    """Get info about the currently logged-in user."""
    try:
        params = {"include-memberships": str(include_memberships).lower()}
        resp = requests.get(f"{BASE_URL}/user", headers=HEADERS, params=params)
        return resp.json()
    except Exception as e:
        return {"error": str(e)}

def list_workspace_users(workspaceId: str, email: Optional[str] = None, status: Optional[str] = None, page: int = 1, page_size: int = 50) -> Any:
    """List users in a workspace."""
    try:
        params = {"page": page, "page-size": page_size}
        if email:
            params["email"] = email
        if status:
            params["status"] = status
        resp = requests.get(f"{BASE_URL}/workspaces/{workspaceId}/users", headers=HEADERS, params=params)
        return resp.json()
    except Exception as e:
        return {"error": str(e)}