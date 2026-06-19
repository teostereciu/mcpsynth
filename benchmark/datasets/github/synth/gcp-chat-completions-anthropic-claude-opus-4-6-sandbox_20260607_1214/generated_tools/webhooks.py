"""GitHub Webhooks tools."""

from typing import Any, Optional
from generated_tools.github_client import github_get, github_post, github_patch, github_delete


def list_repository_webhooks(owner: str, repo: str, per_page: int = 30, page: int = 1) -> Any:
    """List repository webhooks.

    Args:
        owner: Repository owner
        repo: Repository name
        per_page: Results per page (max 100)
        page: Page number
    """
    return github_get(f"/repos/{owner}/{repo}/hooks", {"per_page": per_page, "page": page})


def create_repository_webhook(owner: str, repo: str, config: dict, events: Optional[list] = None,
                               active: bool = True) -> Any:
    """Create a repository webhook.

    Args:
        owner: Repository owner
        repo: Repository name
        config: Webhook config dict with url, content_type, secret, insecure_ssl keys
        events: List of events to trigger the webhook (default: ['push'])
        active: Whether the webhook is active
    """
    data = {"config": config, "active": active}
    if events:
        data["events"] = events
    return github_post(f"/repos/{owner}/{repo}/hooks", data)


def get_repository_webhook(owner: str, repo: str, hook_id: int) -> Any:
    """Get a repository webhook.

    Args:
        owner: Repository owner
        repo: Repository name
        hook_id: Webhook ID
    """
    return github_get(f"/repos/{owner}/{repo}/hooks/{hook_id}")


def update_repository_webhook(owner: str, repo: str, hook_id: int, config: Optional[dict] = None,
                               events: Optional[list] = None, active: Optional[bool] = None,
                               add_events: Optional[list] = None,
                               remove_events: Optional[list] = None) -> Any:
    """Update a repository webhook.

    Args:
        owner: Repository owner
        repo: Repository name
        hook_id: Webhook ID
        config: New webhook config
        events: New list of events (replaces existing)
        active: Whether the webhook is active
        add_events: Events to add
        remove_events: Events to remove
    """
    data = {}
    if config:
        data["config"] = config
    if events:
        data["events"] = events
    if active is not None:
        data["active"] = active
    if add_events:
        data["add_events"] = add_events
    if remove_events:
        data["remove_events"] = remove_events
    return github_patch(f"/repos/{owner}/{repo}/hooks/{hook_id}", data)


def delete_repository_webhook(owner: str, repo: str, hook_id: int) -> Any:
    """Delete a repository webhook.

    Args:
        owner: Repository owner
        repo: Repository name
        hook_id: Webhook ID
    """
    return github_delete(f"/repos/{owner}/{repo}/hooks/{hook_id}")


def ping_repository_webhook(owner: str, repo: str, hook_id: int) -> Any:
    """Ping a repository webhook.

    Args:
        owner: Repository owner
        repo: Repository name
        hook_id: Webhook ID
    """
    return github_post(f"/repos/{owner}/{repo}/hooks/{hook_id}/pings")


def test_push_repository_webhook(owner: str, repo: str, hook_id: int) -> Any:
    """Test the push repository webhook.

    Args:
        owner: Repository owner
        repo: Repository name
        hook_id: Webhook ID
    """
    return github_post(f"/repos/{owner}/{repo}/hooks/{hook_id}/tests")


def list_webhook_deliveries(owner: str, repo: str, hook_id: int,
                            per_page: int = 30, cursor: Optional[str] = None) -> Any:
    """List deliveries for a repository webhook.

    Args:
        owner: Repository owner
        repo: Repository name
        hook_id: Webhook ID
        per_page: Results per page (max 100)
        cursor: Cursor for pagination
    """
    params = {"per_page": per_page}
    if cursor:
        params["cursor"] = cursor
    return github_get(f"/repos/{owner}/{repo}/hooks/{hook_id}/deliveries", params)


def get_webhook_delivery(owner: str, repo: str, hook_id: int, delivery_id: int) -> Any:
    """Get a delivery for a repository webhook.

    Args:
        owner: Repository owner
        repo: Repository name
        hook_id: Webhook ID
        delivery_id: Delivery ID
    """
    return github_get(f"/repos/{owner}/{repo}/hooks/{hook_id}/deliveries/{delivery_id}")


def redeliver_webhook_delivery(owner: str, repo: str, hook_id: int, delivery_id: int) -> Any:
    """Redeliver a delivery for a repository webhook.

    Args:
        owner: Repository owner
        repo: Repository name
        hook_id: Webhook ID
        delivery_id: Delivery ID
    """
    return github_post(f"/repos/{owner}/{repo}/hooks/{hook_id}/deliveries/{delivery_id}/attempts")
