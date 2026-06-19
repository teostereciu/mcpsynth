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


def create_database(parent: dict, title: list, description=None, is_inline=False, icon=None, cover=None, data_source=None, **kwargs):
    """Create a new database."""
    url = f"{BASE_URL}/databases"
    body = {
        "parent": parent,
        "title": title,
        "is_inline": is_inline,
    }
    if description is not None:
        body["description"] = description
    if icon is not None:
        body["icon"] = icon
    if cover is not None:
        body["cover"] = cover
    if data_source is not None:
        body["data_source"] = data_source
    body.update(kwargs)

    try:
        response = requests.post(url, headers=headers, json=body)
        response.raise_for_status()
        return response.json()
    except requests.HTTPError as e:
        return {"error": str(e), "status_code": response.status_code, "response": response.text}


def retrieve_database(database_id: str):
    """Retrieve a database by ID."""
    url = f"{BASE_URL}/databases/{database_id}"

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.HTTPError as e:
        return {"error": str(e), "status_code": response.status_code, "response": response.text}


def update_database(database_id: str, title=None, description=None, is_inline=None, icon=None, cover=None, in_trash=None, is_locked=None, **kwargs):
    """Update a database."""
    url = f"{BASE_URL}/databases/{database_id}"
    body = {}
    if title is not None:
        body["title"] = title
    if description is not None:
        body["description"] = description
    if is_inline is not None:
        body["is_inline"] = is_inline
    if icon is not None:
        body["icon"] = icon
    if cover is not None:
        body["cover"] = cover
    if in_trash is not None:
        body["in_trash"] = in_trash
    if is_locked is not None:
        body["is_locked"] = is_locked
    body.update(kwargs)

    try:
        response = requests.patch(url, headers=headers, json=body)
        response.raise_for_status()
        return response.json()
    except requests.HTTPError as e:
        return {"error": str(e), "status_code": response.status_code, "response": response.text}


def query_database(database_id: str, filter=None, sorts=None, filter_properties=None, **kwargs):
    """Query a database."""
    url = f"{BASE_URL}/databases/{database_id}/query"
    body = {}
    if filter is not None:
        body["filter"] = filter
    if sorts is not None:
        body["sorts"] = sorts
    if filter_properties is not None:
        body["filter_properties"] = filter_properties
    body.update(kwargs)

    try:
        response = requests.post(url, headers=headers, json=body)
        response.raise_for_status()
        return response.json()
    except requests.HTTPError as e:
        return {"error": str(e), "status_code": response.status_code, "response": response.text}


def list_tools():
    return [
        "create_database",
        "retrieve_database",
        "update_database",
        "query_database",
    ]
