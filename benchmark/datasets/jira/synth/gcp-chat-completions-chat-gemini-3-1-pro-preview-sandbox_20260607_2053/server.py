import os
import json
import requests
from typing import Any, Dict, List, Optional, Union
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP
mcp = FastMCP("jira")

# Environment variables
JIRA_BASE_URL = os.environ.get("JIRA_BASE_URL", "").rstrip("/")
JIRA_EMAIL = os.environ.get("JIRA_EMAIL", "")
JIRA_API_TOKEN = os.environ.get("JIRA_API_TOKEN", "")

def get_auth():
    return (JIRA_EMAIL, JIRA_API_TOKEN)

def get_base_url():
    return f"{JIRA_BASE_URL}/rest/api/3"

def make_request(method: str, endpoint: str, **kwargs) -> Dict[str, Any]:
    url = f"{get_base_url()}{endpoint}"
    auth = get_auth()
    
    headers = kwargs.pop("headers", {})
    headers["Accept"] = "application/json"
    if method in ["POST", "PUT", "PATCH"]:
        headers["Content-Type"] = "application/json"
        
    try:
        response = requests.request(method, url, auth=auth, headers=headers, **kwargs)
        
        if response.status_code == 204:
            return {"success": True}
            
        try:
            return response.json()
        except ValueError:
            if response.ok:
                return {"success": True, "text": response.text}
            return {"error": f"HTTP {response.status_code}", "text": response.text}
            
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    mcp.run()
