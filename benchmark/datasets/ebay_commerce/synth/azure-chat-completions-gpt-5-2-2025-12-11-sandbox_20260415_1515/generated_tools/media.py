from __future__ import annotations

import os
from typing import Any, Dict, Optional

from .http_client import EbayHttpClient


class MediaTools:
    def __init__(self, client: Optional[EbayHttpClient] = None):
        self.client = client or EbayHttpClient()

    # Images
    def create_image_from_url(self, image_url: str) -> Dict[str, Any]:
        return self.client.request(
            "POST",
            "/commerce/media/v1_beta/image/create_image_from_url",
            base="media",
            token_type="user",
            scope="https://api.ebay.com/oauth/api_scope/sell.inventory",
            json_body={"imageUrl": image_url},
            headers={"Content-Type": "application/json"},
        )

    def create_image_from_file(self, file_path: str, *, form_field: str = "image") -> Dict[str, Any]:
        if not os.path.exists(file_path):
            return {"error": f"File not found: {file_path}"}
        with open(file_path, "rb") as f:
            files = {form_field: (os.path.basename(file_path), f)}
            return self.client.request(
                "POST",
                "/commerce/media/v1_beta/image/create_image_from_file",
                base="media",
                token_type="user",
                scope="https://api.ebay.com/oauth/api_scope/sell.inventory",
                files=files,
                headers={"Accept": "application/json"},
            )

    def get_image(self, image_id: str) -> Dict[str, Any]:
        return self.client.request(
            "GET",
            f"/commerce/media/v1_beta/image/{image_id}",
            base="media",
            token_type="user",
            scope="https://api.ebay.com/oauth/api_scope/sell.inventory",
        )

    # Videos
    def create_video(self, *, title: str, size: int) -> Dict[str, Any]:
        body = {"title": title, "size": size}
        return self.client.request(
            "POST",
            "/commerce/media/v1_beta/video",
            base="media",
            token_type="user",
            scope="https://api.ebay.com/oauth/api_scope/sell.inventory",
            json_body=body,
            headers={"Content-Type": "application/json"},
        )

    def upload_video(self, video_id: str, file_path: str) -> Dict[str, Any]:
        if not os.path.exists(file_path):
            return {"error": f"File not found: {file_path}"}
        with open(file_path, "rb") as f:
            data = f.read()
        return self.client.request(
            "PUT",
            f"/commerce/media/v1_beta/video/{video_id}/upload",
            base="media",
            token_type="user",
            scope="https://api.ebay.com/oauth/api_scope/sell.inventory",
            data=data,
            headers={"Content-Type": "application/octet-stream"},
        )

    def get_video(self, video_id: str) -> Dict[str, Any]:
        return self.client.request(
            "GET",
            f"/commerce/media/v1_beta/video/{video_id}",
            base="media",
            token_type="user",
            scope="https://api.ebay.com/oauth/api_scope/sell.inventory",
        )

    # Documents
    def create_document(self, *, title: str, size: int) -> Dict[str, Any]:
        body = {"title": title, "size": size}
        return self.client.request(
            "POST",
            "/commerce/media/v1_beta/document",
            base="api",
            token_type="user",
            scope="https://api.ebay.com/oauth/api_scope/sell.inventory",
            json_body=body,
            headers={"Content-Type": "application/json"},
        )

    def create_document_from_url(self, *, url: str) -> Dict[str, Any]:
        return self.client.request(
            "POST",
            "/commerce/media/v1_beta/document/create_document_from_url",
            base="api",
            token_type="user",
            scope="https://api.ebay.com/oauth/api_scope/sell.inventory",
            json_body={"url": url},
            headers={"Content-Type": "application/json"},
        )

    def upload_document(self, document_id: str, file_path: str) -> Dict[str, Any]:
        if not os.path.exists(file_path):
            return {"error": f"File not found: {file_path}"}
        with open(file_path, "rb") as f:
            data = f.read()
        return self.client.request(
            "PUT",
            f"/commerce/media/v1_beta/document/{document_id}/upload",
            base="api",
            token_type="user",
            scope="https://api.ebay.com/oauth/api_scope/sell.inventory",
            data=data,
            headers={"Content-Type": "application/octet-stream"},
        )

    def get_document(self, document_id: str) -> Dict[str, Any]:
        return self.client.request(
            "GET",
            f"/commerce/media/v1_beta/document/{document_id}",
            base="api",
            token_type="user",
            scope="https://api.ebay.com/oauth/api_scope/sell.inventory",
        )
