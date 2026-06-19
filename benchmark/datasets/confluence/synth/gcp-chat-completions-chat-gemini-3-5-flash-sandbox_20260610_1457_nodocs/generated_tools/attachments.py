import base64
from typing import Any, Dict, Optional
from confluence_client import ConfluenceClient

def list_attachments(
    client: ConfluenceClient,
    content_id: str,
    content_type: str = "page",
    limit: int = 20,
    cursor: Optional[str] = None
) -> Dict[str, Any]:
    """
    List attachments for a page or blogpost.
    
    Args:
        content_id: Numeric ID of the content.
        content_type: Type of content ('page' or 'blogpost').
        limit: Maximum number of attachments to return.
        cursor: Cursor for pagination.
    """
    path_type = "pages" if content_type == "page" else "blogposts"
    params = {"limit": limit}
    if cursor:
        params["cursor"] = cursor
    return client.get(f"/api/v2/{path_type}/{content_id}/attachments", params=params)

def upload_attachment(
    client: ConfluenceClient,
    content_id: str,
    filename: str,
    file_content_base64: str,
    comment: Optional[str] = None,
    content_type: str = "page"
) -> Dict[str, Any]:
    """
    Upload an attachment to a page or blogpost.
    
    Args:
        content_id: Numeric ID of the content.
        filename: Name of the file to upload.
        file_content_base64: Base64 encoded content of the file.
        comment: Optional comment about the attachment.
        content_type: Type of content ('page' or 'blogpost').
    """
    path_type = "pages" if content_type == "page" else "blogposts"
    url = f"{client.base_url}/api/v2/{path_type}/{content_id}/attachments"
    
    try:
        file_data = base64.b64decode(file_content_base64)
    except Exception as e:
        return {"error": f"Failed to decode base64 file content: {str(e)}"}
    
    files = {
        "file": (filename, file_data)
    }
    
    # We must override Content-Type so requests can set the boundary for multipart/form-data
    headers = {
        "X-Atlassian-Token": "no-check",
        "Accept": "application/json"
    }
    
    # Create a temporary session or request without the default Content-Type header
    try:
        # We use client.session but override headers for this request
        # requests.Session.post merges session headers with passed headers.
        # To remove Content-Type, we can pass {"Content-Type": None}
        headers["Content-Type"] = None
        
        data = {}
        if comment:
            data["comment"] = comment
            
        response = client.session.post(url, files=files, headers=headers, data=data)
        
        try:
            res_data = response.json()
        except ValueError:
            res_data = {"text": response.text}
            
        if not response.ok:
            return {
                "error": f"HTTP {response.status_code}: {response.reason}",
                "details": res_data
            }
        return res_data
    except Exception as e:
        return {"error": f"Upload failed: {str(e)}"}

def download_attachment(client: ConfluenceClient, attachment_id: str) -> Dict[str, Any]:
    """
    Download an attachment by its ID.
    Returns the attachment metadata and base64-encoded content.
    
    Args:
        attachment_id: Numeric ID of the attachment.
    """
    # Get attachment metadata
    meta = client.get(f"/api/v2/attachments/{attachment_id}")
    if "error" in meta:
        return meta
    
    download_link = meta.get("downloadLink")
    if not download_link:
        return {"error": "Download link not found in attachment metadata."}
    
    # Construct full download URL
    download_url = f"{client.base_url}{download_link}"
    
    try:
        # Download the file content
        # We need to remove Content-Type from headers for GET, but requests handles it.
        # We also want to get raw bytes, so we don't use client.get which parses JSON.
        response = client.session.get(download_url)
        if not response.ok:
            return {"error": f"Failed to download file: HTTP {response.status_code} {response.reason}"}
        
        content_base64 = base64.b64encode(response.content).decode("utf-8")
        
        return {
            "id": attachment_id,
            "filename": meta.get("title"),
            "mediaType": meta.get("mediaType"),
            "fileSize": meta.get("fileSize"),
            "content_base64": content_base64
        }
    except Exception as e:
        return {"error": f"Download failed: {str(e)}"}
