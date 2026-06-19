from typing import Any, Dict, Optional

from .common import client


def create_image_from_url(image_url: str, classification: Optional[str] = None) -> Dict[str, Any]:
    body = {"imageUrl": image_url}
    if classification:
        body["classification"] = classification
    return client.request("POST", "/commerce/media/v1_beta/image_from_url", "user", json_body=body, use_media_base=True)


def get_image(image_id: str) -> Dict[str, Any]:
    return client.request("GET", f"/commerce/media/v1_beta/image/{image_id}", "user", use_media_base=True)


def create_video(body: Dict[str, Any]) -> Dict[str, Any]:
    return client.request("POST", "/commerce/media/v1_beta/video", "user", json_body=body, use_media_base=True)


def get_video(video_id: str) -> Dict[str, Any]:
    return client.request("GET", f"/commerce/media/v1_beta/video/{video_id}", "user", use_media_base=True)


def upload_video(video_id: str, size: Optional[int] = None, content_type: str = "application/octet-stream") -> Dict[str, Any]:
    headers = {"Content-Type": content_type}
    if size is not None:
        headers["Content-Length"] = str(size)
    return {
        "note": "Use the upload URL returned by create_video for binary upload. This MCP server exposes metadata operations only.",
        "video_id": video_id,
        "headers": headers,
    }
