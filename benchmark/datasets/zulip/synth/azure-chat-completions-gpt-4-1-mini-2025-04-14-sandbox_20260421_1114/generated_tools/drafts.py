import os
import requests
import json

BASE_URL = os.environ.get("ZULIP_SITE", "") + "/api/v1"
AUTH = (os.environ.get("ZULIP_EMAIL"), os.environ.get("ZULIP_API_KEY"))


def create_drafts(drafts):
    """Create one or more drafts on the server."""
    url = f"{BASE_URL}/drafts"
    data = {
        "drafts": json.dumps(drafts),
    }
    try:
        response = requests.post(url, auth=AUTH, data=data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        try:
            return response.json()
        except Exception:
            return {"error": str(e)}
    except Exception as e:
        return {"error": str(e)}


def list_tools():
    return ["create_drafts"]
