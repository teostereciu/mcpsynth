from typing import Any, Dict
from confluence_client import ConfluenceClient

def get_current_user(client: ConfluenceClient) -> Dict[str, Any]:
    """
    Get details of the currently authenticated user.
    """
    return client.get("/rest/api/user/current")

def get_user(client: ConfluenceClient, account_id: str) -> Dict[str, Any]:
    """
    Get details of a user by their account ID.
    
    Args:
        account_id: The unique Atlassian account ID of the user.
    """
    return client.get("/rest/api/user", params={"accountId": account_id})
