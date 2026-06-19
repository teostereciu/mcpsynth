from typing import Any, Dict, Optional

from .ebay_client import EbayClient


class FeedTools:
    def __init__(self, client: Optional[EbayClient] = None):
        self.client = client or EbayClient()

    def create_upload_job(self, job: Dict[str, Any]) -> Dict[str, Any]:
        return self.client.request("POST", "/sell/feed/v1/upload_job", json=job)

    def get_upload_job(self, upload_job_id: str) -> Dict[str, Any]:
        return self.client.request("GET", f"/sell/feed/v1/upload_job/{upload_job_id}")

    def get_upload_jobs(self, feed_type: Optional[str] = None, limit: int = 50, offset: int = 0) -> Dict[str, Any]:
        params: Dict[str, Any] = {"limit": limit, "offset": offset}
        if feed_type:
            params["feed_type"] = feed_type
        return self.client.request("GET", "/sell/feed/v1/upload_job", params=params)

    def create_download_job(self, job: Dict[str, Any]) -> Dict[str, Any]:
        return self.client.request("POST", "/sell/feed/v1/download_job", json=job)

    def get_download_job(self, download_job_id: str) -> Dict[str, Any]:
        return self.client.request("GET", f"/sell/feed/v1/download_job/{download_job_id}")

    def get_download_jobs(self, feed_type: Optional[str] = None, limit: int = 50, offset: int = 0) -> Dict[str, Any]:
        params: Dict[str, Any] = {"limit": limit, "offset": offset}
        if feed_type:
            params["feed_type"] = feed_type
        return self.client.request("GET", "/sell/feed/v1/download_job", params=params)
