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


def create_token(**kwargs):
    """Create a token."""
    url = f"{BASE_URL}/auth/token"
    body = kwargs

    try:
        response = requests.post(url, headers=headers, json=body)
        response.raise_for_status()
        return response.json()
    except requests.HTTPError as e:
        return {"error": str(e), "status_code": response.status_code, "response": response.text}


def introspect_token(token: str, **kwargs):
    """Introspect a token."""
    url = f"{BASE_URL}/auth/token/introspect"
    body = {"token": token}
    body.update(kwargs)

    try:
        response = requests.post(url, headers=headers, json=body)
        response.raise_for_status()
        return response.json()
    except requests.HTTPError as e:
        return {"error": str(e), "status_code": response.status_code, "response": response.text}


def revoke_token(token: str, **kwargs):
    """Revoke a token."""
    url = f"{BASE_URL}/auth/token/revoke"
    body = {"token": token}
    body.update(kwargs)

    try:
        response = requests.post(url, headers=headers, json=body)
        response.raise_for_status()
        return response.json()
    except requests.HTTPError as e:
        return {"error": str(e), "status_code": response.status_code, "response": response.text}


def refresh_token(token: str, **kwargs):
    """Refresh a token."""
    url = f"{BASE_URL}/auth/token/refresh"
    body = {"token": token}
    body.update(kwargs)

    try:
        response = requests.post(url, headers=headers, json=body)
        response.raise_for_status()
        return response.json()
    except requests.HTTPError as e:
        return {"error": str(e), "status_code": response.status_code, "response": response.text}


def list_tools():
    return [
        "create_token",
        "introspect_token",
        "revoke_token",
        "refresh_token",
    ]
