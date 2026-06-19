import os
import requests

NOTION_API_KEY = os.environ.get('NOTION_API_KEY')
NOTION_VERSION = '2026-03-11'
BASE_URL = 'https://api.notion.com/v1'


def list_users(start_cursor=None, page_size=10):
    """List all users in the workspace."""
    url = f"{BASE_URL}/users"
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


def retrieve_user(user_id):
    """Retrieve a user by ID."""
    url = f"{BASE_URL}/users/{user_id}"
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
