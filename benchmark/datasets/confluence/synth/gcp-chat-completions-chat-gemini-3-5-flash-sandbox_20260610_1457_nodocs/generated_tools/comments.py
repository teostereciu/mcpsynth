from typing import Any, Dict, Optional
from confluence_client import ConfluenceClient

def list_comments(
    client: ConfluenceClient,
    page_id: str,
    comment_type: str = "footer",
    limit: int = 20,
    cursor: Optional[str] = None
) -> Dict[str, Any]:
    """
    List comments on a page.
    
    Args:
        page_id: Numeric ID of the page.
        comment_type: Type of comments to list ('footer' or 'inline').
        limit: Maximum number of comments to return.
        cursor: Cursor for pagination.
    """
    endpoint_type = "footer-comments" if comment_type == "footer" else "inline-comments"
    params = {"limit": limit}
    if cursor:
        params["cursor"] = cursor
    return client.get(f"/api/v2/pages/{page_id}/{endpoint_type}", params=params)

def create_footer_comment(
    client: ConfluenceClient,
    page_id: str,
    body: str,
    parent_comment_id: Optional[str] = None,
    representation: str = "storage"
) -> Dict[str, Any]:
    """
    Create a footer comment on a page.
    
    Args:
        page_id: Numeric ID of the page.
        body: Content of the comment (HTML/Storage or ADF).
        parent_comment_id: Optional ID of the parent comment (for replies).
        representation: Format of the body ('storage' or 'atlas_doc_format').
    """
    payload = {
        "pageId": page_id,
        "body": {
            "representation": representation,
            "value": body
        }
    }
    if parent_comment_id:
        payload["parentCommentId"] = parent_comment_id
        
    return client.post("/api/v2/footer-comments", json_data=payload)
