from typing import Any, Dict, Optional
from confluence_client import ConfluenceClient

def search_content(
    client: ConfluenceClient,
    cql: str,
    limit: int = 20,
    cursor: Optional[str] = None
) -> Dict[str, Any]:
    """
    Search for content using Confluence Query Language (CQL).
    
    Args:
        cql: The CQL query string (e.g., 'type = page and text ~ "mcp"').
        limit: Maximum number of results to return.
        cursor: Cursor for pagination.
    """
    params = {
        "cql": cql,
        "limit": limit
    }
    if cursor:
        params["cursor"] = cursor
    return client.get("/api/v2/search/content", params=params)
