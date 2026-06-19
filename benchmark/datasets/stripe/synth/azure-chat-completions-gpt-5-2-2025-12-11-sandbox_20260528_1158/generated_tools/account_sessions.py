from typing import Any, Dict

from .stripe_client import stripe_request


def create_account_session(account: str, components: Dict[str, Any]) -> Dict[str, Any]:
    return stripe_request(
        "POST",
        "/v1/account_sessions",
        params={"account": account, "components": components},
    )
