"""eBay Commerce Media API tools (images, videos, documents).

Note: Media API uses a different base domain: apim.sandbox.ebay.com / apim.ebay.com
"""
from mcp.server.fastmcp import FastMCP
from .auth import get_user_token, get_media_base_url

def register(mcp: FastMCP):

    # ── Documents ──────────────────────────────────────────────────────────────

    @mcp.tool()
    def create_document(document_type: str, languages: list) -> dict:
        """Stage a new document resource for upload.

        Creates a document ID that is then used with upload_document.

        Args:
            document_type: Type of document, e.g. 'USER_GUIDE_OR_MANUAL' or 'SAFETY_DATA_SHEET'.
            languages: List of language codes used in the document, e.g. ['en'].
        """
        import requests
        token = get_user_token()
        if "error" in token:
            return token
        url = f"{get_media_base_url()}/commerce/media/v1_beta/document"
        headers = {
            "Authorization": f"Bearer {token['access_token']}",
            "Content-Type": "application/json",
        }
        payload = {"documentType": document_type, "languages": languages}
        try:
            resp = requests.post(url, headers=headers, json=payload, timeout=30)
            if resp.status_code in (200, 201):
                result = resp.json() if resp.text else {}
                result["location"] = resp.headers.get("Location", "")
                return result
            return {"error": resp.text, "status_code": resp.status_code}
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def create_document_from_url(document_type: str, document_url: str, languages: list) -> dict:
        """Download a document from a URL and add it to the user's account.

        Args:
            document_type: Type of document, e.g. 'USER_GUIDE_OR_MANUAL'.
            document_url: HTTPS URL of the document (.pdf, .png, .jpg, .jpeg; max 10 MB).
            languages: List of language codes used in the document, e.g. ['en'].
        """
        import requests
        token = get_user_token()
        if "error" in token:
            return token
        url = f"{get_media_base_url()}/commerce/media/v1_beta/document/create_document_from_url"
        headers = {
            "Authorization": f"Bearer {token['access_token']}",
            "Content-Type": "application/json",
        }
        payload = {
            "documentType": document_type,
            "documentUrl": document_url,
            "languages": languages,
        }
        try:
            resp = requests.post(url, headers=headers, json=payload, timeout=30)
            if resp.status_code in (200, 201):
                result = resp.json() if resp.text else {}
                result["location"] = resp.headers.get("Location", "")
                return result
            return {"error": resp.text, "status_code": resp.status_code}
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def get_document(document_id: str) -> dict:
        """Retrieve the current status and metadata of a document.

        Args:
            document_id: The unique identifier of the document (returned by create_document).
        """
        import requests
        token = get_user_token()
        if "error" in token:
            return token
        url = f"{get_media_base_url()}/commerce/media/v1_beta/document/{document_id}"
        headers = {"Authorization": f"Bearer {token['access_token']}"}
        try:
            resp = requests.get(url, headers=headers, timeout=30)
            if resp.status_code == 200:
                return resp.json()
            return {"error": resp.text, "status_code": resp.status_code}
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def upload_document(document_id: str, file_path: str) -> dict:
        """Upload a document file to an existing document resource.

        Supported formats: PDF, JPEG/JPG, PNG (max 10 MB).

        Args:
            document_id: The unique identifier of the document (from create_document).
            file_path: Local filesystem path to the document file to upload.
        """
        import requests
        token = get_user_token()
        if "error" in token:
            return token
        url = f"{get_media_base_url()}/commerce/media/v1_beta/document/{document_id}/upload"
        headers = {"Authorization": f"Bearer {token['access_token']}"}
        try:
            with open(file_path, "rb") as f:
                files = {"file": f}
                resp = requests.post(url, headers=headers, files=files, timeout=60)
            if resp.status_code in (200, 201):
                return resp.json() if resp.text else {"status": "uploaded"}
            return {"error": resp.text, "status_code": resp.status_code}
        except FileNotFoundError:
            return {"error": f"File not found: {file_path}"}
        except Exception as e:
            return {"error": str(e)}

    # ── Images ─────────────────────────────────────────────────────────────────

    @mcp.tool()
    def create_image_from_url(image_url: str) -> dict:
        """Upload a picture to eBay Picture Services (EPS) from an HTTPS URL.

        Args:
            image_url: HTTPS URL of the image (JPG, GIF, PNG, BMP, TIFF, AVIF, HEIC, WEBP).
        """
        import requests
        token = get_user_token()
        if "error" in token:
            return token
        url = f"{get_media_base_url()}/commerce/media/v1_beta/image/create_image_from_url"
        headers = {
            "Authorization": f"Bearer {token['access_token']}",
            "Content-Type": "application/json",
        }
        payload = {"imageUrl": image_url}
        try:
            resp = requests.post(url, headers=headers, json=payload, timeout=30)
            if resp.status_code in (200, 201):
                result = resp.json() if resp.text else {}
                result["location"] = resp.headers.get("Location", "")
                return result
            return {"error": resp.text, "status_code": resp.status_code}
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def create_image_from_file(file_path: str) -> dict:
        """Upload a picture file to eBay Picture Services (EPS) using multipart/form-data.

        Supported formats: JPG, GIF, PNG, BMP, TIFF, AVIF, HEIC, WEBP.

        Args:
            file_path: Local filesystem path to the image file to upload.
        """
        import requests
        token = get_user_token()
        if "error" in token:
            return token
        url = f"{get_media_base_url()}/commerce/media/v1_beta/image/create_image_from_file"
        headers = {"Authorization": f"Bearer {token['access_token']}"}
        try:
            with open(file_path, "rb") as f:
                files = {"image": f}
                resp = requests.post(url, headers=headers, files=files, timeout=60)
            if resp.status_code in (200, 201):
                result = resp.json() if resp.text else {}
                result["location"] = resp.headers.get("Location", "")
                return result
            return {"error": resp.text, "status_code": resp.status_code}
        except FileNotFoundError:
            return {"error": f"File not found: {file_path}"}
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def get_image(image_id: str) -> dict:
        """Retrieve an EPS image URL and expiration details by image ID.

        Args:
            image_id: The unique identifier of the image (from create_image_from_file/url Location header).
        """
        import requests
        token = get_user_token()
        if "error" in token:
            return token
        url = f"{get_media_base_url()}/commerce/media/v1_beta/image/{image_id}"
        headers = {"Authorization": f"Bearer {token['access_token']}"}
        try:
            resp = requests.get(url, headers=headers, timeout=30)
            if resp.status_code == 200:
                return resp.json()
            return {"error": resp.text, "status_code": resp.status_code}
        except Exception as e:
            return {"error": str(e)}

    # ── Videos ─────────────────────────────────────────────────────────────────

    @mcp.tool()
    def create_video(title: str, size: int, classification: list, description: str = "") -> dict:
        """Create a video resource (metadata only — use upload_video to upload the file).

        Args:
            title: The title of the video.
            size: The exact size in bytes of the video file to be uploaded.
            classification: List of classification values. Currently only ['ITEM'] is supported.
            description: Optional description of the video.
        """
        import requests
        token = get_user_token()
        if "error" in token:
            return token
        url = f"{get_media_base_url()}/commerce/media/v1_beta/video"
        headers = {
            "Authorization": f"Bearer {token['access_token']}",
            "Content-Type": "application/json",
        }
        payload: dict = {"title": title, "size": size, "classification": classification}
        if description:
            payload["description"] = description
        try:
            resp = requests.post(url, headers=headers, json=payload, timeout=30)
            if resp.status_code in (200, 201):
                result = resp.json() if resp.text else {}
                result["location"] = resp.headers.get("Location", "")
                return result
            return {"error": resp.text, "status_code": resp.status_code}
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def get_video(video_id: str) -> dict:
        """Retrieve a video's metadata, status, playlist URLs, and thumbnail.

        Args:
            video_id: The unique identifier of the video.
        """
        import requests
        token = get_user_token()
        if "error" in token:
            return token
        url = f"{get_media_base_url()}/commerce/media/v1_beta/video/{video_id}"
        headers = {"Authorization": f"Bearer {token['access_token']}"}
        try:
            resp = requests.get(url, headers=headers, timeout=30)
            if resp.status_code == 200:
                return resp.json()
            return {"error": resp.text, "status_code": resp.status_code}
        except Exception as e:
            return {"error": str(e)}

    @mcp.tool()
    def upload_video(video_id: str, file_path: str) -> dict:
        """Upload an MP4 video file to an existing video resource.

        The file size must exactly match the size specified in create_video.

        Args:
            video_id: The unique identifier of the video resource (from create_video Location header).
            file_path: Local filesystem path to the .mp4 video file.
        """
        import requests
        import os
        token = get_user_token()
        if "error" in token:
            return token
        url = f"{get_media_base_url()}/commerce/media/v1_beta/video/{video_id}/upload"
        headers = {
            "Authorization": f"Bearer {token['access_token']}",
            "Content-Type": "application/octet-stream",
        }
        try:
            file_size = os.path.getsize(file_path)
            headers["Content-Length"] = str(file_size)
            with open(file_path, "rb") as f:
                resp = requests.post(url, headers=headers, data=f, timeout=120)
            if resp.status_code in (200, 201):
                return {"status": "uploaded", "video_id": video_id}
            return {"error": resp.text, "status_code": resp.status_code}
        except FileNotFoundError:
            return {"error": f"File not found: {file_path}"}
        except Exception as e:
            return {"error": str(e)}
