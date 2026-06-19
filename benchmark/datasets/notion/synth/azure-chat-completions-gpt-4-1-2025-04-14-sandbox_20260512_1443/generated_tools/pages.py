import os
import requests

NOTION_API_KEY = os.environ.get('NOTION_API_KEY')
NOTION_VERSION = '2026-03-11'
BASE_URL = 'https://api.notion.com/v1'


def create_page(parent, properties, **kwargs):
    """Create a new Notion page."""
    url = f"{BASE_URL}/pages"
    headers = {
        "Authorization": f"Bearer {NOTION_API_KEY}",
        "Notion-Version": NOTION_VERSION,
        "Content-Type": "application/json"
    }
    payload = {
        "parent": parent,
        "properties": properties
    }
    payload.update(kwargs)
    try:
        resp = requests.post(url, headers=headers, json=payload)
        if resp.status_code != 200:
            return {"error": resp.text}
        return resp.json()
    except Exception as e:
        return {"error": str(e)}


def update_page(page_id, **kwargs):
    """Update a Notion page by ID. Use kwargs for fields to update (e.g. properties, icon, cover, in_trash)."""
    url = f"{BASE_URL}/pages/{page_id}"
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


def trash_page(page_id):
    """Move a Notion page to trash."""
    return update_page(page_id, in_trash=True)


def restore_page(page_id):
    """Restore a trashed Notion page."""
    return update_page(page_id, in_trash=False)


def retrieve_page(page_id, property_ids=None):
    """Retrieve a Notion page by ID. Optionally filter properties by property_ids (list)."""
    url = f"{BASE_URL}/pages/{page_id}"
    headers = {
        "Authorization": f"Bearer {NOTION_API_KEY}",
        "Notion-Version": NOTION_VERSION
    }
    params = {}
    if property_ids:
        params['property_ids'] = ','.join(property_ids)
    try:
        resp = requests.get(url, headers=headers, params=params)
        if resp.status_code != 200:
            return {"error": resp.text}
        return resp.json()
    except Exception as e:
        return {"error": str(e)}
