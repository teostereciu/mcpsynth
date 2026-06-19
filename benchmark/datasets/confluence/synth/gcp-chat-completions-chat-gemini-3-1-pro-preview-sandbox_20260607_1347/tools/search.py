from typing import Any, Dict
from server import mcp
from confluence_client import client

@mcp.tool()
def search_content(cql: str, limit: int = 25) -> Dict[str, Any]:
    """Search for content using CQL."""
    return client.request("GET", "/rest/api/search", params={"cql": cql, "limit": limit})
