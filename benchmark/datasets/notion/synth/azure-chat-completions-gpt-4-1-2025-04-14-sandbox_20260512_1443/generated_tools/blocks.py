import os
import requests

NOTION_API_KEY = os.environ.get('NOTION_API_KEY')
NOTION_VERSION = '2026-03-11'
BASE_URL = 'https://api.notion.com/v1'


def retrieve_block(block_id):
    """Retrieve a Notion block by ID."""
    url = f"{BASE_URL}/blocks/{block_id}"
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


def get_block_children(block_id, start_cursor=None, page_size=50):
    """Retrieve children blocks for a given block ID."""
    url = f"{BASE_URL}/blocks/{block_id}/children"
    headers = {
        "Authorization": f"Bearer {NOTION_API_KEY}",
        "Notion-Version": NOTION_VERSION
    }
    params = {}
    if start_cursor:
        params['start_cursor'] = start_cursor
    params['page_size'] = page_size
    try:
        resp = requests.get(url, headers=headers, params=params)
        if resp.status_code != 200:
            return {"error": resp.text}
        return resp.json()
    except Exception as e:
        return {"error": str(e)}


def delete_block(block_id):
    """Delete a Notion block by ID."""
    url = f"{BASE_URL}/blocks/{block_id}"
    headers = {
        "Authorization": f"Bearer {NOTION_API_KEY}",
        "Notion-Version": NOTION_VERSION
    }
    try:
        resp = requests.delete(url, headers=headers)
        if resp.status_code != 200:
            return {"error": resp.text}
        return resp.json()
    except Exception as e:
        return {"error": str(e)}


def update_block(block_id, **kwargs):
    """Update a Notion block by ID. Use kwargs for block fields (e.g. paragraph, heading_1, etc)."""
    url = f"{BASE_URL}/blocks/{block_id}"
    headers = {
        "Authorization": f"Bearer {NOTION_API_KEY}",
        "Notion-Version": NOTION_VERSION,
        "Content-Type": "application/json"
    }
    payload = kwargs
    try:
        resp = requests.patch(url, headers=headers, json=payload)
        if resp.status_code != 200:
            return {"error": resp.text}
        return resp.json()
    except Exception as e:
        return {"error": str(e)}
