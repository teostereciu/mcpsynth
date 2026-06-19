from mcp.server.fastmcp import FastMCP
from typing import Dict, Any, Optional
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

def _api_request(method: str, path: str, params: Optional[Dict] = None, data: Optional[Dict] = None, files: Optional[Dict] = None) -> Dict[str, Any]:
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
            files=files,
            timeout=60
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

# ==================== Media ====================

@mcp.tool()
def upload_media(file_path: str, description: Optional[str] = None, focus: Optional[str] = None) -> Dict[str, Any]:
    """Upload a media attachment for use in statuses.
    
    Args:
        file_path: Path to the media file to upload
        description: Alternative text description for accessibility
        focus: Two floating points (x,y) between -1.0 and 1.0, representing the focal point
        
    Returns:
        Dict containing attachment information with ID for use in status creation
    """
    try:
        with open(file_path, 'rb') as f:
            files = {'file': (os.path.basename(file_path), f)}
            
            data = {}
            if description:
                data["description"] = description
            if focus:
                data["focus"] = focus
                
            return _api_request("POST", "/media", data=data, files=files)
    except FileNotFoundError:
        return {"error": f"File not found: {file_path}"}
    except Exception as e:
        return {"error": str(e)}

@mcp.tool()
def update_media(media_id: str, description: Optional[str] = None, focus: Optional[str] = None) -> Dict[str, Any]:
    """Update a media attachment's metadata.
    
    Args:
        media_id: The ID of the media attachment
        description: Alternative text description for accessibility
        focus: Two floating points (x,y) between -1.0 and 1.0, representing the focal point
        
    Returns:
        Dict containing updated attachment information
    """
    data = {}
    if description:
        data["description"] = description
    if focus:
        data["focus"] = focus
        
    return _api_request("PUT", f"/media/{media_id}", data=data)

@mcp.tool()
def get_media(media_id: str) -> Dict[str, Any]:
    """Get information about a media attachment.
    
    Args:
        media_id: The ID of the media attachment
        
    Returns:
        Dict containing attachment information
    """
    return _api_request("GET", f"/media/{media_id}")
