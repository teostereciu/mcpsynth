import os
import requests

NOTION_API_KEY = os.environ.get('NOTION_API_KEY')
NOTION_VERSION = '2026-03-11'
BASE_URL = 'https://api.notion.com/v1'


def search(query, filter=None, sort=None):
    """Search pages, databases, or other objects in Notion."""
    url = f"{BASE_URL}/search"
    headers = {
        "Authorization": f"Bearer {NOTION_API_KEY}",
        "Notion-Version": NOTION_VERSION,
        "Content-Type": "application/json"
    }
    payload = {"query": query}
    if filter:
        payload["filter"] = filter
    if sort:
        payload["sort"] = sort
    try:
        resp = requests.post(url, headers=headers, json=payload)
        if resp.status_code != 200:
            return {"error": resp.text}
        return resp.json()
    except Exception as e:
        return {"error": str(e)}
