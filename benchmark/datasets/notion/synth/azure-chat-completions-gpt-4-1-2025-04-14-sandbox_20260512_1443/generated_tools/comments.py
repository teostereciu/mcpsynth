import os
import requests

NOTION_API_KEY = os.environ.get('NOTION_API_KEY')
NOTION_VERSION = '2026-03-11'
BASE_URL = 'https://api.notion.com/v1'


def create_comment(parent, rich_text, files=None, display_name=None):
    """Create a comment on a page or block."""
    url = f"{BASE_URL}/comments"
    headers = {
        "Authorization": f"Bearer {NOTION_API_KEY}",
        "Notion-Version": NOTION_VERSION,
        "Content-Type": "application/json"
    }
    payload = {
        "parent": parent,
        "rich_text": rich_text
    }
    if files:
        payload["files"] = files
    if display_name:
        payload["display_name"] = display_name
    try:
        resp = requests.post(url, headers=headers, json=payload)
        if resp.status_code != 200:
            return {"error": resp.text}
        return resp.json()
    except Exception as e:
        return {"error": str(e)}


def retrieve_comment(comment_id):
    """Retrieve a comment by ID."""
    url = f"{BASE_URL}/comments/{comment_id}"
    headers = {
        "Authorization": f"Bearer {NOTION_API_KEY}",
        "Notion-Version": NOTION_VERSION
    }
    try:
        resp = requests.get(url, headers=headers)
        if resp.status_code != 200:
            return {"error": resp.text}
        return resp.json()
    except Exception as e:
        return {"error": str(e)}


def list_comments(block_id, start_cursor=None, page_size=50):
    """List comments for a block or page."""
    url = f"{BASE_URL}/comments"
    headers = {
        "Authorization": f"Bearer {NOTION_API_KEY}",
        "Notion-Version": NOTION_VERSION
    }
    params = {"block_id": block_id}
    if start_cursor:
        params["start_cursor"] = start_cursor
    params["page_size"] = page_size
    try:
        resp = requests.get(url, headers=headers, params=params)
        if resp.status_code != 200:
            return {"error": resp.text}
        return resp.json()
    except Exception as e:
        return {"error": str(e)}
