from typing import Any, Dict
from server import mcp
from confluence_client import client
import os

@mcp.tool()
def get_attachments(page_id: str, limit: int = 25) -> Dict[str, Any]:
    """Get attachments for a page."""
    return client.request("GET", f"/api/v2/pages/{page_id}/attachments", params={"limit": limit})

@mcp.tool()
def upload_attachment(page_id: str, file_path: str, comment: str = "") -> Dict[str, Any]:
    """Upload an attachment to a page."""
    url = f"{client.base_url}/rest/api/content/{page_id}/child/attachment"
    headers = {"X-Atlassian-Token": "nocheck"}
    
    try:
        with open(file_path, "rb") as f:
            files = {"file": (os.path.basename(file_path), f)}
            data = {"comment": comment}
            response = client.session.post(url, headers=headers, files=files, data=data)
            
            if not response.ok:
                try:
                    return {"error": f"HTTP {response.status_code}", "details": response.json()}
                except ValueError:
                    return {"error": f"HTTP {response.status_code}", "details": response.text}
            return response.json()
    except Exception as e:
        return {"error": str(e)}

@mcp.tool()
def download_attachment(attachment_id: str, download_path: str) -> Dict[str, Any]:
    """Download an attachment."""
    # First get the attachment metadata to find the download URL
    meta = client.request("GET", f"/api/v2/attachments/{attachment_id}")
    if "error" in meta:
        return meta
        
    download_url = meta.get("downloadLink")
    if not download_url:
        return {"error": "Could not find download link for attachment"}
        
    url = f"{client.base_url}{download_url}"
    try:
        response = client.session.get(url, stream=True)
        if not response.ok:
            return {"error": f"HTTP {response.status_code}", "details": response.text}
            
        with open(download_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        return {"success": True, "path": download_path}
    except Exception as e:
        return {"error": str(e)}
