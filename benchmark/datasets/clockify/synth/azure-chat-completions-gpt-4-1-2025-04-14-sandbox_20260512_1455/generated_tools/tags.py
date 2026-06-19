import os
import requests
from typing import Any, Dict, List, Optional

CLOCKIFY_API_KEY = os.environ.get("CLOCKIFY_API_KEY")
BASE_URL = "https://api.clockify.me/api/v1"
HEADERS = {"X-Api-Key": CLOCKIFY_API_KEY}

def list_tags(workspaceId: str, page: int = 1, page_size: int = 50) -> Any:
    """List tags in a workspace."""
    try:
        params = {"page": page, "page-size": page_size}
        resp = requests.get(f"{BASE_URL}/workspaces/{workspaceId}/tags", headers=HEADERS, params=params)
        return resp.json()
    except Exception as e:
        return {"error": str(e)}

def create_tag(workspaceId: str, name: str) -> Any:
    """Create a new tag in a workspace."""
    try:
        data = {"name": name}
        resp = requests.post(f"{BASE_URL}/workspaces/{workspaceId}/tags", headers=HEADERS, json=data)
        return resp.json()
    except Exception as e:
        return {"error": str(e)}