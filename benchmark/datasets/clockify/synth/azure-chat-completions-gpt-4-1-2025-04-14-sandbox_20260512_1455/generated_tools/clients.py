import os
import requests
from typing import Any, Dict, List, Optional

CLOCKIFY_API_KEY = os.environ.get("CLOCKIFY_API_KEY")
BASE_URL = "https://api.clockify.me/api/v1"
HEADERS = {"X-Api-Key": CLOCKIFY_API_KEY}

def list_clients(workspaceId: str, page: int = 1, page_size: int = 50) -> Any:
    """List clients in a workspace."""
    try:
        params = {"page": page, "page-size": page_size}
        resp = requests.get(f"{BASE_URL}/workspaces/{workspaceId}/clients", headers=HEADERS, params=params)
        return resp.json()
    except Exception as e:
        return {"error": str(e)}

def create_client(workspaceId: str, name: str, address: Optional[str] = None, email: Optional[str] = None, note: Optional[str] = None) -> Any:
    """Create a new client in a workspace."""
    try:
        data = {"name": name}
        if address:
            data["address"] = address
        if email:
            data["email"] = email
        if note:
            data["note"] = note
        resp = requests.post(f"{BASE_URL}/workspaces/{workspaceId}/clients", headers=HEADERS, json=data)
        return resp.json()
    except Exception as e:
        return {"error": str(e)}