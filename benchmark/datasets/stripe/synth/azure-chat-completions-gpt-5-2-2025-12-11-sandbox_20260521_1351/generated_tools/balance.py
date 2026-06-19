from typing import Any, Dict, Optional

from .http_client import stripe_request


def retrieve_balance(*, account: Optional[str] = None) -> Dict[str, Any]:
    return stripe_request("GET", "/v1/balance", params={}, account=account)
