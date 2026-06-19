import os
import requests

NOTION_API_KEY = os.getenv("NOTION_API_KEY")
BASE_URL = "https://api.notion.com/v1"
NOTION_VERSION = "2026-03-11"

headers = {
    "Authorization": f"Bearer {NOTION_API_KEY}",
    "Notion-Version": NOTION_VERSION,
    "Content-Type": "application/json",
}


def create_file_upload(mode="single_part", filename=None, content_type=None, number_of_parts=None, external_url=None, **kwargs):
    """Create a file upload."""
    url = f"{BASE_URL}/file_uploads"
    body = {
        "mode": mode,
    }
    if filename is not None:
        body["filename"] = filename
    if content_type is not None:
        body["content_type"] = content_type
    if number_of_parts is not None:
        body["number_of_parts"] = number_of_parts
    if external_url is not None:
        body["external_url"] = external_url
    body.update(kwargs)

    try:
        response = requests.post(url, headers=headers, json=body)
        response.raise_for_status()
        return response.json()
    except requests.HTTPError as e:
        return {"error": str(e), "status_code": response.status_code, "response": response.text}


def send_file_upload(file_upload_id: str, file: dict, part_number=None):
    """Send file contents for a file upload."""
    url = f"{BASE_URL}/file_uploads/{file_upload_id}/upload"
    body = {
        "file": file,
    }
    if part_number is not None:
        body["part_number"] = part_number

    try:
        response = requests.post(url, headers=headers, json=body)
        response.raise_for_status()
        return response.json()
    except requests.HTTPError as e:
        return {"error": str(e), "status_code": response.status_code, "response": response.text}


def complete_file_upload(file_upload_id: str):
    """Complete a multi-part file upload."""
    url = f"{BASE_URL}/file_uploads/{file_upload_id}/complete"

    try:
        response = requests.post(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.HTTPError as e:
        return {"error": str(e), "status_code": response.status_code, "response": response.text}


def retrieve_file_upload(file_upload_id: str):
    """Retrieve a file upload."""
    url = f"{BASE_URL}/file_uploads/{file_upload_id}"

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.HTTPError as e:
        return {"error": str(e), "status_code": response.status_code, "response": response.text}


def list_file_uploads(start_cursor=None, page_size=50):
    """List file uploads."""
    url = f"{BASE_URL}/file_uploads"
    params = {}
    if start_cursor:
        params["start_cursor"] = start_cursor
    if page_size:
        params["page_size"] = page_size

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()
    except requests.HTTPError as e:
        return {"error": str(e), "status_code": response.status_code, "response": response.text}


def list_tools():
    return [
        "create_file_upload",
        "send_file_upload",
        "complete_file_upload",
        "retrieve_file_upload",
        "list_file_uploads",
    ]
