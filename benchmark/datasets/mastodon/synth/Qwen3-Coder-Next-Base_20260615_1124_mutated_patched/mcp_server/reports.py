from mcp.server.fastmcp import FastMCP
from typing import Dict, Any, List, Optional
import os
import requests

mcp = FastMCP("mastodon")

# Load authentication from environment variables
BASE_URL = os.getenv("MASTODON_BASE_URL", "https://mastodon.social")
ACCESS_TOKEN = os.getenv("MASTODON_ACCESS_TOKEN")

if not ACCESS_TOKEN:
    raise ValueError("MASTODON_ACCESS_TOKEN environment variable is required")

def _get_auth_headers() -> Dict[str, str]:
    """Get authorization headers for Mastodon API."""
    return {"Authorization": f"Bearer {ACCESS_TOKEN}"}

def _api_request(method: str, path: str, params: Optional[Dict] = None, data: Optional[Dict] = None) -> Dict[str, Any]:
    """Make an API request to Mastodon."""
    url = f"{BASE_URL}/api/v1{path}"
    headers = _get_auth_headers()
    
    try:
        response = requests.request(
            method=method,
            url=url,
            headers=headers,
            params=params,
            json=data,
            timeout=30
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

# ==================== Reports ====================

@mcp.tool()
def create_report(account_id: str, status_ids: Optional[List[str]] = None, comment: str = "", forward: bool = False) -> Dict[str, Any]:
    """Create a report.
    
    Args:
        account_id: The ID of the account to report
        status_ids: List of status IDs to include with the report
        comment: Additional comment about the report
        forward: Whether to forward the report to the remote admin if the account is remote
        
    Returns:
        Dict containing report information
    """
    data = {
        "account_id": account_id,
        "comment": comment,
        "forward": forward
    }
    if status_ids:
        data["status_ids[]"] = status_ids
    return _api_request("POST", "/reports", data=data)
