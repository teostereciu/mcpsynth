import os
import requests

BASE_URL = os.environ.get("ZULIP_SITE", "") + "/api/v1"
AUTH = (os.environ.get("ZULIP_EMAIL"), os.environ.get("ZULIP_API_KEY"))


def upload_file(filepath: str):
    """Upload a single file and get the corresponding URL."""
    url = f"{BASE_URL}/user_uploads"
    try:
        with open(filepath, "rb") as f:
            files = {"filename": f}
            response = requests.post(url, auth=AUTH, files=files)
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
    return ["upload_file"]
