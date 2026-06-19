"""
Confluence Cloud v2 Versions tools + v1 restore.
Endpoints: GET /api/v2/pages/{id}/versions, GET /api/v2/pages/{page-id}/versions/{version-number},
           GET /api/v2/blogposts/{id}/versions, GET /api/v2/blogposts/{id}/versions/{version-number},
           POST /wiki/rest/api/content/{id}/version (restore)
"""
import os
import requests
from requests.auth import HTTPBasicAuth

BASE_URL = os.environ.get("CONFLUENCE_BASE_URL", "").rstrip("/")
EMAIL = os.environ.get("JIRA_EMAIL", "")
TOKEN = os.environ.get("JIRA_API_TOKEN", "")


def _auth() -> HTTPBasicAuth:
    return HTTPBasicAuth(EMAIL, TOKEN)


def _v2(path: str) -> str:
    return f"{BASE_URL}/api/v2{path}"


def _v1(path: str) -> str:
    return f"{BASE_URL}/rest/api{path}"


def get_page_versions(
    page_id: str,
    cursor: str | None = None,
    max_results: int = 25,
    sort: str = "MODIFIED_DATE_DESC",
) -> dict:
    """Return the version history of a specific page."""
    params: dict = {"max_results": max_results, "sort": sort}
    if cursor:
        params["cursor"] = cursor
    try:
        r = requests.get(_v2(f"/pages/{page_id}/versions"), params=params, auth=_auth(), timeout=30)
        r.raise_for_status()
        return r.json()
    except requests.HTTPError as e:
        return {"error": str(e), "status_code": r.status_code, "body": r.text}
    except Exception as e:
        return {"error": str(e)}


def get_page_version_details(page_id: str, version_number: int) -> dict:
    """Return details for a specific version of a page."""
    try:
        r = requests.get(
            _v2(f"/pages/{page_id}/versions/{version_number}"),
            auth=_auth(),
            timeout=30,
        )
        r.raise_for_status()
        return r.json()
    except requests.HTTPError as e:
        return {"error": str(e), "status_code": r.status_code, "body": r.text}
    except Exception as e:
        return {"error": str(e)}


def get_blogpost_versions(
    blog_post_id: str,
    cursor: str | None = None,
    max_results: int = 25,
    sort: str = "MODIFIED_DATE_DESC",
) -> dict:
    """Return the version history of a specific blog post."""
    params: dict = {"max_results": max_results, "sort": sort}
    if cursor:
        params["cursor"] = cursor
    try:
        r = requests.get(_v2(f"/blogposts/{blog_post_id}/versions"), params=params, auth=_auth(), timeout=30)
        r.raise_for_status()
        return r.json()
    except requests.HTTPError as e:
        return {"error": str(e), "status_code": r.status_code, "body": r.text}
    except Exception as e:
        return {"error": str(e)}


def get_blogpost_version_details(blog_post_id: str, version_number: int) -> dict:
    """Return details for a specific version of a blog post."""
    try:
        r = requests.get(
            _v2(f"/blogposts/{blog_post_id}/versions/{version_number}"),
            auth=_auth(),
            timeout=30,
        )
        r.raise_for_status()
        return r.json()
    except requests.HTTPError as e:
        return {"error": str(e), "status_code": r.status_code, "body": r.text}
    except Exception as e:
        return {"error": str(e)}


def restore_content_version(
    content_id: str,
    version_number: int,
    message: str = "",
    restore_title: bool = True,
) -> dict:
    """
    Restore a historical version of content (page or blog post) to be the latest version.
    Uses v1 API. Creates a new version with the content of the historical version.
    """
    payload = {
        "operationKey": "restore",
        "params": {
            "versionNumber": version_number,
            "message": message,
            "restoreTitle": restore_title,
        },
    }
    try:
        r = requests.post(
            _v1(f"/content/{content_id}/version"),
            json=payload,
            auth=_auth(),
            timeout=30,
        )
        r.raise_for_status()
        return r.json()
    except requests.HTTPError as e:
        return {"error": str(e), "status_code": r.status_code, "body": r.text}
    except Exception as e:
        return {"error": str(e)}
