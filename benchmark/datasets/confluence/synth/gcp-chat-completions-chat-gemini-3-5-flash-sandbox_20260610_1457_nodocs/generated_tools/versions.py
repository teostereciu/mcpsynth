from typing import Any, Dict, Optional
from confluence_client import ConfluenceClient

def list_versions(
    client: ConfluenceClient,
    page_id: str,
    limit: int = 20,
    cursor: Optional[str] = None
) -> Dict[str, Any]:
    """
    List all versions of a page.
    
    Args:
        page_id: Numeric ID of the page.
        limit: Maximum number of versions to return.
        cursor: Cursor for pagination.
    """
    params = {"limit": limit}
    if cursor:
        params["cursor"] = cursor
    return client.get(f"/api/v2/pages/{page_id}/versions", params=params)

def get_version(client: ConfluenceClient, page_id: str, version_number: int) -> Dict[str, Any]:
    """
    Get details of a specific page version.
    
    Args:
        page_id: Numeric ID of the page.
        version_number: Version number to retrieve.
    """
    return client.get(f"/api/v2/pages/{page_id}/versions/{version_number}")

def restore_version(
    client: ConfluenceClient,
    page_id: str,
    version_number: int,
    message: Optional[str] = None
) -> Dict[str, Any]:
    """
    Restore a page to a specific version.
    
    Args:
        page_id: Numeric ID of the page.
        version_number: Version number to restore to.
        message: Optional description/message for the restore operation.
    """
    payload = {
        "operationKey": "restore",
        "params": {
            "versionNumber": version_number,
            "message": message or f"Restored to version {version_number} via MCP"
        }
    }
    return client.post(f"/api/v2/pages/{page_id}/versions", json_data=payload)
