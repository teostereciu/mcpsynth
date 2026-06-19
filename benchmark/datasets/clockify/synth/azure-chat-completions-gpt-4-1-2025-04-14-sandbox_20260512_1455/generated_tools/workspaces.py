import os
import requests
from typing import Any, Dict, List, Optional

CLOCKIFY_API_KEY = os.environ.get("CLOCKIFY_API_KEY")
BASE_URL = "https://api.clockify.me/api/v1"
HEADERS = {"X-Api-Key": CLOCKIFY_API_KEY}

def list_workspaces(roles: Optional[List[str]] = None) -> Any:
    """List all workspaces. Optionally filter by roles."""
    try:
        params = {}
        if roles:
            params['roles'] = roles
        resp = requests.get(f"{BASE_URL}/workspaces", headers=HEADERS, params=params)
        return resp.json()
    except Exception as e:
        return {"error": str(e)}

def get_workspace_details(workspaceId: str) -> Any:
    """Get workspace info by workspaceId."""
    try:
        resp = requests.get(f"{BASE_URL}/workspaces/{workspaceId}", headers=HEADERS)
        return resp.json()
    except Exception as e:
        return {"error": str(e)}