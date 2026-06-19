import os
import requests

NOTION_API_KEY = os.environ.get('NOTION_API_KEY')
NOTION_VERSION = '2026-03-11'
BASE_URL = 'https://api.notion.com/v1'


def create_database(parent_id, title, **kwargs):
    """Create a new Notion database."""
    url = f"{BASE_URL}/databases"
    headers = {
        "Authorization": f"Bearer {NOTION_API_KEY}",
        "Notion-Version": NOTION_VERSION,
        "Content-Type": "application/json"
    }
    payload = {
        "parent": {"type": "page_id", "page_id": parent_id},
        "title": [{"text": {"content": title}}]
    }
    payload.update(kwargs)
    try:
        resp = requests.post(url, headers=headers, json=payload)
        if resp.status_code != 200:
            return {"error": resp.text}
        return resp.json()
    except Exception as e:
        return {"error": str(e)}


def retrieve_database(database_id):
    """Retrieve a Notion database by ID."""
    url = f"{BASE_URL}/databases/{database_id}"
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


def query_database(database_id, filter=None, sort=None, **kwargs):
    """Query a Notion database with optional filter and sort objects."""
    url = f"{BASE_URL}/databases/{database_id}/query"
    headers = {
        "Authorization": f"Bearer {NOTION_API_KEY}",
        "Notion-Version": NOTION_VERSION,
        "Content-Type": "application/json"
    }
    payload = {}
    if filter:
        payload["filter"] = filter
    if sort:
        payload["sort"] = sort
    payload.update(kwargs)
    try:
        resp = requests.post(url, headers=headers, json=payload)
        if resp.status_code != 200:
            return {"error": resp.text}
        return resp.json()
    except Exception as e:
        return {"error": str(e)}
