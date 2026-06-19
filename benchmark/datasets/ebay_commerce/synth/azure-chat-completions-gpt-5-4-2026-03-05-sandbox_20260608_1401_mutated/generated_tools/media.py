from typing import Any, Dict, Optional

from .ebay_common import client


def create_document(document_type: str, languages: list[str]) -> Dict[str, Any]:
    return client.request(
        "POST",
        "/commerce/media/v1_beta/document",
        token_type="user",
        media=True,
        headers={"Content-Type": "application/json"},
        json_body={"documentType": document_type, "languages": languages},
    )


def upload_document(document_id: str, file_path: str, mime_type: Optional[str] = None) -> Dict[str, Any]:
    with open(file_path, "rb") as f:
        files = {"file": (file_path.split("/")[-1], f, mime_type or "application/octet-stream")}
        return client.request(
            "POST",
            f"/commerce/media/v1_beta/document/{document_id}/upload",
            token_type="user",
            media=True,
            files=files,
        )


def create_document_from_url(document_type: str, document_url: str, languages: list[str]) -> Dict[str, Any]:
    return client.request(
        "POST",
        "/commerce/media/v1_beta/document/create_document_from_url",
        token_type="user",
        media=True,
        headers={"Content-Type": "application/json"},
        json_body={"documentType": document_type, "documentUrl": document_url, "languages": languages},
    )


def get_document(document_id: str) -> Dict[str, Any]:
    return client.request(
        "GET",
        f"/commerce/media/v1_beta/document/{document_id}",
        token_type="user",
        media=True,
    )


def create_image_from_file(file_path: str, mime_type: Optional[str] = None) -> Dict[str, Any]:
    with open(file_path, "rb") as f:
        files = {"image": (file_path.split("/")[-1], f, mime_type or "application/octet-stream")}
        return client.request(
            "POST",
            "/commerce/media/v1_beta/image/create_image_from_file",
            token_type="user",
            media=True,
            files=files,
        )


def create_image_from_url(image_url: str) -> Dict[str, Any]:
    return client.request(
        "POST",
        "/commerce/media/v1_beta/image/create_image_from_url",
        token_type="user",
        media=True,
        headers={"Content-Type": "application/json"},
        json_body={"imageUrl": image_url},
    )


def get_image(image_id: str) -> Dict[str, Any]:
    return client.request(
        "GET",
        f"/commerce/media/v1_beta/image/{image_id}",
        token_type="user",
        media=True,
    )


def create_video(title: str, size: int, classification: list[dict], description: Optional[str] = None) -> Dict[str, Any]:
    body = {
        "title": title,
        "size": size,
        "classification": classification,
        "description": description,
    }
    return client.request(
        "POST",
        "/commerce/media/v1_beta/video",
        token_type="user",
        media=True,
        headers={"Content-Type": "application/json"},
        json_body=body,
    )


def get_video(video_id: str) -> Dict[str, Any]:
    return client.request(
        "GET",
        f"/commerce/media/v1_beta/video/{video_id}",
        token_type="user",
        media=True,
    )


def upload_video(video_id: str, file_path: str, content_range: Optional[str] = None) -> Dict[str, Any]:
    with open(file_path, "rb") as f:
        data = f.read()
    headers = {
        "Content-Type": "application/octet-stream",
        "Content-Length": str(len(data)),
        "Content-Range": content_range,
    }
    return client.request(
        "POST",
        f"/commerce/media/v1_beta/video/{video_id}/upload",
        token_type="user",
        media=True,
        headers=headers,
        data=data,
    )
