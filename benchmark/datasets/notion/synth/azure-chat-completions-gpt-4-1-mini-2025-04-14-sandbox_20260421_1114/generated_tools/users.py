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


def retrieve_user(user_id: str):
    """Retrieve a user by ID."""
    url = f"{BASE_URL}/users/{user_id}"

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.HTTPError as e:
        return {"error": str(e), "status_code": response.status_code, "response": response.text}


def list_users(start_cursor=None, page_size=50):
    """List all users."""
    url = f"{BASE_URL}/users"
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


def retrieve_bot_user():
    """Retrieve the bot user associated with the current token."""
    url = f"{BASE_URL}/users/me"

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.HTTPError as e:
        return {"error": str(e), "status_code": response.status_code, "response": response.text}


def list_tools():
    return [
        "retrieve_user",
        "list_users",
        "retrieve_bot_user",
    ]
