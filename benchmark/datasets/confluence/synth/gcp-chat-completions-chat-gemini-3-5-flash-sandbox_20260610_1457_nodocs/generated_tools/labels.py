from typing import Any, Dict, List
from confluence_client import ConfluenceClient

def get_labels(client: ConfluenceClient, content_id: str, content_type: str = "page") -> Dict[str, Any]:
    """
    Get labels for a page or blogpost.
    
    Args:
        content_id: Numeric ID of the content.
        content_type: Type of content ('page' or 'blogpost').
    """
    path_type = "pages" if content_type == "page" else "blogposts"
    return client.get(f"/api/v2/{path_type}/{content_id}/labels")

def add_labels(client: ConfluenceClient, content_id: str, labels: List[str], content_type: str = "page") -> Dict[str, Any]:
    """
    Add labels to a page or blogpost.
    
    Args:
        content_id: Numeric ID of the content.
        labels: List of label names to add.
        content_type: Type of content ('page' or 'blogpost').
    """
    path_type = "pages" if content_type == "page" else "blogposts"
    payload = [{"prefix": "global", "name": label} for label in labels]
    return client.post(f"/api/v2/{path_type}/{content_id}/labels", json_data=payload)

def remove_label(client: ConfluenceClient, content_id: str, label_name: str, content_type: str = "page") -> Dict[str, Any]:
    """
    Remove a label from a page or blogpost.
    
    Args:
        content_id: Numeric ID of the content.
        label_name: Name of the label to remove.
        content_type: Type of content ('page' or 'blogpost').
    """
    path_type = "pages" if content_type == "page" else "blogposts"
    return client.delete(f"/api/v2/{path_type}/{content_id}/labels/{label_name}")
