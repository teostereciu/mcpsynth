from typing import Any, Dict, Optional

from .http_client import stripe_request


def create_login_link(
    account_id: str,
    *,
    stripe_account: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /v1/accounts/{account_id}/login_links

    Doc: docs/accounts_login_link.md (Create a login link)
    """
    return stripe_request(
        "POST",
        f"/v1/accounts/{account_id}/login_links",
        None,
        stripe_account=stripe_account,
        idempotency_key=idempotency_key,
    )
