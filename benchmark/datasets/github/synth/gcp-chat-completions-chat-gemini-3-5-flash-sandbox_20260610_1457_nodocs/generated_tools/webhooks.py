from typing import Any, Dict, List, Optional, Union
from github_client import client

def list_repository_webhooks(
    owner: str,
    repo: str,
    per_page: Optional[int] = 30,
    page: Optional[int] = 1
) -> Union[List[Dict[str, Any]], Dict[str, Any]]:
    """
    List repository webhooks.
    
    Parameters:
    - owner: The account owner of the repository.
    - repo: The name of the repository.
    - per_page: The number of results per page (max 100).
    - page: Page number of the results to fetch.
    """
    params = {"per_page": per_page, "page": page}
    return client.request("GET", f"/repos/{owner}/{repo}/hooks", params=params)

def get_repository_webhook(owner: str, repo: str, hook_id: int) -> Union[Dict[str, Any], List[Dict[str, Any]]]:
    """
    Get a repository webhook.
    
    Parameters:
    - owner: The account owner of the repository.
    - repo: The name of the repository.
    - hook_id: The unique identifier of the webhook.
    """
    return client.request("GET", f"/repos/{owner}/{repo}/hooks/{hook_id}")

def create_repository_webhook(
    owner: str,
    repo: str,
    name: Optional[str] = "web",
    config: Optional[Dict[str, Any]] = None,
    events: Optional[List[str]] = None,
    active: Optional[bool] = True
) -> Union[Dict[str, Any], List[Dict[str, Any]]]:
    """
    Create a repository webhook.
    
    Parameters:
    - owner: The account owner of the repository.
    - repo: The name of the repository.
    - name: Use 'web' to create a webhook.
    - config: Key-value pairs to configure the webhook (e.g. url, content_type, secret).
    - events: Determines what events trigger the webhook. Default is ['push'].
    - active: Determines if notifications are sent when the webhook is triggered.
    """
    data = {
        "active": active
    }
    if name is not None: data["name"] = name
    if config is not None: data["config"] = config
    if events is not None: data["events"] = events

    return client.request("POST", f"/repos/{owner}/{repo}/hooks", json_data=data)

def update_repository_webhook(
    owner: str,
    repo: str,
    hook_id: int,
    config: Optional[Dict[str, Any]] = None,
    events: Optional[List[str]] = None,
    active: Optional[bool] = None
) -> Union[Dict[str, Any], List[Dict[str, Any]]]:
    """
    Update a repository webhook.
    
    Parameters:
    - owner: The account owner of the repository.
    - repo: The name of the repository.
    - hook_id: The unique identifier of the webhook.
    - config: Key-value pairs to configure the webhook (e.g. url, content_type, secret).
    - events: Determines what events trigger the webhook.
    - active: Determines if notifications are sent when the webhook is triggered.
    """
    data = {}
    if config is not None: data["config"] = config
    if events is not None: data["events"] = events
    if active is not None: data["active"] = active

    return client.request("PATCH", f"/repos/{owner}/{repo}/hooks/{hook_id}", json_data=data)

def delete_repository_webhook(owner: str, repo: str, hook_id: int) -> Union[Dict[str, Any], List[Dict[str, Any]]]:
    """
    Delete a repository webhook.
    
    Parameters:
    - owner: The account owner of the repository.
    - repo: The name of the repository.
    - hook_id: The unique identifier of the webhook.
    """
    return client.request("DELETE", f"/repos/{owner}/{repo}/hooks/{hook_id}")
