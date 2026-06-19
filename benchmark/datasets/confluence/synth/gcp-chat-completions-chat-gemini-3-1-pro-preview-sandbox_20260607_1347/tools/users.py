from typing import Any, Dict
from server import mcp
from confluence_client import client

@mcp.tool()
def get_current_user() -> Dict[str, Any]:
    """Get the current user."""
    return client.request("GET", "/rest/api/user/current")

@mcp.tool()
def get_user_by_account_id(account_id: str) -> Dict[str, Any]:
    """Get a user by their account ID."""
    return client.request("GET", "/rest/api/user", params={"accountId": account_id})
