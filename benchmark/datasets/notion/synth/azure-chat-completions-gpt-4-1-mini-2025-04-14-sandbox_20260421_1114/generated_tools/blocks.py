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


def retrieve_block(block_id: str):
    """Retrieve a block by ID."""
    url = f"{BASE_URL}/blocks/{block_id}"

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.HTTPError as e:
        return {"error": str(e), "status_code": response.status_code, "response": response.text}


def retrieve_block_children(block_id: str, start_cursor=None, page_size=50):
    """Retrieve children blocks of a block."""
    url = f"{BASE_URL}/blocks/{block_id}/children"
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


def append_block_children(block_id: str, children: list, position=None):
    """Append children blocks to a block."""
    url = f"{BASE_URL}/blocks/{block_id}/children"
    body = {"children": children}
    if position is not None:
        body["position"] = position

    try:
        response = requests.patch(url, headers=headers, json=body)
        response.raise_for_status()
        return response.json()
    except requests.HTTPError as e:
        return {"error": str(e), "status_code": response.status_code, "response": response.text}


def update_block(block_id: str, block_type: str, block_data: dict):
    """Update a block."""
    url = f"{BASE_URL}/blocks/{block_id}"
    body = {block_type: block_data}

    try:
        response = requests.patch(url, headers=headers, json=body)
        response.raise_for_status()
        return response.json()
    except requests.HTTPError as e:
        return {"error": str(e), "status_code": response.status_code, "response": response.text}


def delete_block(block_id: str):
    """Delete a block."""
    url = f"{BASE_URL}/blocks/{block_id}"

    try:
        response = requests.delete(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.HTTPError as e:
        return {"error": str(e), "status_code": response.status_code, "response": response.text}


def list_tools():
    return [
        "retrieve_block",
        "retrieve_block_children",
        "append_block_children",
        "update_block",
        "delete_block",
    ]
