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


def create_page(parent: dict, properties: dict, icon=None, cover=None, children=None, template_id=None, **kwargs):
    """Create a new page."""
    url = f"{BASE_URL}/pages"
    body = {
        "parent": parent,
        "properties": properties,
    }
    if icon is not None:
        body["icon"] = icon
    if cover is not None:
        body["cover"] = cover
    if children is not None:
        body["children"] = children
    if template_id is not None:
        body["template_id"] = template_id
    body.update(kwargs)

    try:
        response = requests.post(url, headers=headers, json=body)
        response.raise_for_status()
        return response.json()
    except requests.HTTPError as e:
        return {"error": str(e), "status_code": response.status_code, "response": response.text}


def retrieve_page(page_id: str, property_ids=None):
    """Retrieve a page by ID."""
    url = f"{BASE_URL}/pages/{page_id}"
    params = {}
    if property_ids:
        params["property_ids"] = ",".join(property_ids) if isinstance(property_ids, list) else property_ids

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()
    except requests.HTTPError as e:
        return {"error": str(e), "status_code": response.status_code, "response": response.text}


def update_page(page_id: str, properties=None, icon=None, cover=None, in_trash=None, is_locked=None, erase_content=None, **kwargs):
    """Update a page."""
    url = f"{BASE_URL}/pages/{page_id}"
    body = {}
    if properties is not None:
        body["properties"] = properties
    if icon is not None:
        body["icon"] = icon
    if cover is not None:
        body["cover"] = cover
    if in_trash is not None:
        body["in_trash"] = in_trash
    if is_locked is not None:
        body["is_locked"] = is_locked
    if erase_content is not None:
        body["erase_content"] = erase_content
    body.update(kwargs)

    try:
        response = requests.patch(url, headers=headers, json=body)
        response.raise_for_status()
        return response.json()
    except requests.HTTPError as e:
        return {"error": str(e), "status_code": response.status_code, "response": response.text}


def trash_page(page_id: str):
    """Trash (archive) a page."""
    return update_page(page_id, in_trash=True)


def restore_page(page_id: str):
    """Restore a trashed page."""
    return update_page(page_id, in_trash=False)


def list_tools():
    return [
        "create_page",
        "retrieve_page",
        "update_page",
        "trash_page",
        "restore_page",
    ]
