from typing import Any, Dict, Optional

from .ebay_client import EbayClient


class MarketingTools:
    def __init__(self, client: Optional[EbayClient] = None):
        self.client = client or EbayClient()

    # Promotions (Marketing API)
    def get_campaigns(self, marketplace_id: Optional[str] = None, limit: int = 50, offset: int = 0) -> Dict[str, Any]:
        params: Dict[str, Any] = {"limit": limit, "offset": offset}
        if marketplace_id:
            params["marketplace_id"] = marketplace_id
        return self.client.request("GET", "/sell/marketing/v1/campaign", params=params)

    def get_campaign(self, campaign_id: str) -> Dict[str, Any]:
        return self.client.request("GET", f"/sell/marketing/v1/campaign/{campaign_id}")

    def create_campaign(self, campaign: Dict[str, Any]) -> Dict[str, Any]:
        return self.client.request("POST", "/sell/marketing/v1/campaign", json=campaign)

    def update_campaign(self, campaign_id: str, campaign: Dict[str, Any]) -> Dict[str, Any]:
        return self.client.request("PUT", f"/sell/marketing/v1/campaign/{campaign_id}", json=campaign)

    def delete_campaign(self, campaign_id: str) -> Dict[str, Any]:
        return self.client.request("DELETE", f"/sell/marketing/v1/campaign/{campaign_id}")

    def get_ad_report_task(self, report_task_id: str) -> Dict[str, Any]:
        return self.client.request("GET", f"/sell/marketing/v1/ad_report_task/{report_task_id}")
