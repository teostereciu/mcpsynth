from typing import Any, Dict
from confluence_client import ConfluenceClient

def get_content_property(client: ConfluenceClient, page_id: str, key: str) -> Dict[str, Any]:
    """
    Get a content property value for a page.
    
    Args:
        page_id: Numeric ID of the page.
        key: Key of the property.
    """
    return client.get(f"/api/v2/pages/{page_id}/properties/{key}")

def set_content_property(client: ConfluenceClient, page_id: str, key: str, value: Any) -> Dict[str, Any]:
    """
    Set a content property value for a page.
    If the property already exists, it will be updated.
    
    Args:
        page_id: Numeric ID of the page.
        key: Key of the property.
        value: JSON-serializable value of the property.
    """
    # Check if property already exists
    existing = client.get(f"/api/v2/pages/{page_id}/properties/{key}")
    
    if "error" in existing:
        # Property doesn't exist (or error fetching), try creating it
        payload = {
            "key": key,
            "value": value
        }
        return client.post(f"/api/v2/pages/{page_id}/properties", json_data=payload)
    else:
        # Property exists, update it
        property_id = existing.get("id")
        version_num = existing.get("version", {}).get("number", 0) + 1
        
        payload = {
            "key": key,
            "value": value,
            "version": {
                "number": version_num,
                "message": "Updated via MCP"
            }
        }
        return client.put(f"/api/v2/pages/{page_id}/properties/{property_id}", json_data=payload)
