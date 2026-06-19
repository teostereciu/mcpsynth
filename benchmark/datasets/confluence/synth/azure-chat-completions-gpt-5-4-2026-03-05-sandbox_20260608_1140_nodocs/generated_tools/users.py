from typing import Any, Dict

from generated_tools.confluence_client import client


def get_current_user() -> Dict[str, Any]:
    return client.request("GET", "/rest/api/user/current")


def get_user_by_account_id(account_id: str) -> Dict[str, Any]:
    return client.request("GET", "/rest/api/user", params={"accountId": account_id})
