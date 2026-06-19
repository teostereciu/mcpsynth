from typing import Any, Dict, Optional

from .ebay_client import EbayClient


class FinancesTools:
    def __init__(self, client: Optional[EbayClient] = None):
        self.client = client or EbayClient()

    def get_transactions(self, filter: Optional[str] = None, limit: int = 50, offset: int = 0) -> Dict[str, Any]:
        params: Dict[str, Any] = {"limit": limit, "offset": offset}
        if filter:
            params["filter"] = filter
        return self.client.request("GET", "/sell/finances/v1/transaction", params=params)

    def get_payouts(self, filter: Optional[str] = None, limit: int = 50, offset: int = 0) -> Dict[str, Any]:
        params: Dict[str, Any] = {"limit": limit, "offset": offset}
        if filter:
            params["filter"] = filter
        return self.client.request("GET", "/sell/finances/v1/payout", params=params)

    def get_payout(self, payout_id: str) -> Dict[str, Any]:
        return self.client.request("GET", f"/sell/finances/v1/payout/{payout_id}")
