"""Tools for eBay Commerce Media API (apim.* domain)."""

from __future__ import annotations

from typing import Any, Dict, Optional

import requests

from .http import EbayApiError, error_dict, get_media_base_url, request_json


_MEDIA_SCOPE = "https://api.ebay.com/oauth/api_scope/sell.inventory"


def create_image_from_url(image_url: str) -> Dict[str, Any]:
    """Upload an image to EPS from a public HTTPS URL.

    Returns the API JSON plus best-effort extracted imageId.
    """
    try:
        data = request_json(
            method="POST",
            base_url=get_media_base_url(),
            path="/commerce/media/v1_beta/image/create_image_from_url",
            json_body={"imageUrl": image_url},
            user_auth=True,
            scope=_MEDIA_SCOPE,
        )
        image_id = None
        eps_url = data.get("imageUrl")
        if isinstance(eps_url, str) and eps_url:
            image_id = eps_url.rstrip("/").split("/")[-1]
        if image_id:
            data["imageId"] = image_id
        return data
    except EbayApiError as e:
        return error_dict(e)


def get_image(image_id: str) -> Dict[str, Any]:
    """Get image metadata by image ID."""
    try:
        return request_json(
            method="GET",
            base_url=get_media_base_url(),
            path=f"/commerce/media/v1_beta/image/{image_id}",
            user_auth=True,
            scope=_MEDIA_SCOPE,
        )
    except EbayApiError as e:
        return error_dict(e)


def create_document_from_url(document_url: str) -> Dict[str, Any]:
    """Upload a document from a public HTTPS URL.

    Returns the API JSON plus best-effort extracted documentId.
    """
    try:
        data = request_json(
            method="POST",
            base_url=get_media_base_url(),
            path="/commerce/media/v1_beta/document/create_document_from_url",
            json_body={"documentUrl": document_url},
            user_auth=True,
            scope=_MEDIA_SCOPE,
        )
        document_id = None
        doc_url = data.get("documentUrl")
        if isinstance(doc_url, str) and doc_url:
            document_id = doc_url.rstrip("/").split("/")[-1]
        if document_id:
            data["documentId"] = document_id
        return data
    except EbayApiError as e:
        return error_dict(e)


def get_document(document_id: str) -> Dict[str, Any]:
    """Get document metadata by document ID."""
    try:
        return request_json(
            method="GET",
            base_url=get_media_base_url(),
            path=f"/commerce/media/v1_beta/document/{document_id}",
            user_auth=True,
            scope=_MEDIA_SCOPE,
        )
    except EbayApiError as e:
        return error_dict(e)


def upload_document(file_path: str, content_type: str = "application/pdf") -> Dict[str, Any]:
    """Upload a local document file.

    Note: Provided for completeness; scenarios use create_document_from_url.
    """
    try:
        # Media upload endpoints are multipart/binary; implement minimal.
        from .http import get_user_access_token

        token = get_user_access_token(scope=_MEDIA_SCOPE)
        url = f"{get_media_base_url()}/commerce/media/v1_beta/document/upload_document"
        with open(file_path, "rb") as f:
            resp = requests.post(
                url,
                headers={"Authorization": f"Bearer {token}", "Content-Type": content_type},
                data=f,
                timeout=120,
            )
        if resp.status_code == 204:
            return {}
        if not resp.ok:
            raise EbayApiError(f"eBay API error {resp.status_code} for POST /document/upload_document")
        return resp.json() if resp.content else {}
    except Exception as e:
        return error_dict(e)
