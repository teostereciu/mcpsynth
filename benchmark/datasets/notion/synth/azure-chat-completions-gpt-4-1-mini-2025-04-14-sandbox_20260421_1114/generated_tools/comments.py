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


def create_comment(parent: dict, rich_text: list, attachments=None, display_name=None, **kwargs):
    """Create a comment."""
    url = f"{BASE_URL}/comments"
    body = {
        "parent": parent,
        "rich_text": rich_text,
    }
    if attachments is not None:
        body["attachments"] = attachments
    if display_name is not None:
        body["display_name"] = display_name
    body.update(kwargs)

    try:
        response = requests.post(url, headers=headers, json=body)
        response.raise_for_status()
        return response.json()
    except requests.HTTPError as e:
        return {"error": str(e), "status_code": response.status_code, "response": response.text}


def retrieve_comment(comment_id: str):
    """Retrieve a comment by ID."""
    url = f"{BASE_URL}/comments/{comment_id}"

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.HTTPError as e:
        return {"error": str(e), "status_code": response.status_code, "response": response.text}


def list_comments(block_id: str, start_cursor=None, page_size=50):
    """List comments for a block or page."""
    url = f"{BASE_URL}/comments"
    params = {"block_id": block_id}
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
        "create_comment",
        "retrieve_comment",
        "list_comments",
    ]
