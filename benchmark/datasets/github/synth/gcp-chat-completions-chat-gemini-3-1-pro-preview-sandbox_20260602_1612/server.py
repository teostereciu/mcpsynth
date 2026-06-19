import os
import requests
from typing import Any, Dict, List, Optional, Union
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("github-mcp-server")

# Environment variables
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
GITHUB_API_BASE_URL = os.environ.get("GITHUB_API_BASE_URL", "https://api.github.com")

def make_request(method: str, path: str, **kwargs) -> Any:
    """Helper to make GitHub API requests."""
    if not GITHUB_TOKEN:
        return {"error": "GITHUB_TOKEN environment variable is not set"}
    
    url = f"{GITHUB_API_BASE_URL.rstrip('/')}/{path.lstrip('/')}"
    
    headers = kwargs.pop("headers", {})
    headers.setdefault("Accept", "application/vnd.github.v3+json")
    headers.setdefault("Authorization", f"Bearer {GITHUB_TOKEN}")
    headers.setdefault("X-GitHub-Api-Version", "2022-11-28")
    
    try:
        response = requests.request(method, url, headers=headers, **kwargs)
        
        # Return JSON if possible
        if response.content:
            try:
                return response.json()
            except ValueError:
                return {"error": f"Invalid JSON response: {response.text}"}
        
        # If no content but successful
        if response.ok:
            return {"status": "success", "code": response.status_code}
            
        return {"error": f"HTTP {response.status_code}", "details": response.text}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    mcp.run()
