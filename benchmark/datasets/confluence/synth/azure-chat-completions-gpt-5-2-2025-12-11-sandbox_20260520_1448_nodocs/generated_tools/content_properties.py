from typing import Any, Dict

from .http import confluence_request


def get_content_property(content_id: int, key: str) -> Dict[str, Any]:
    return confluence_request("GET", f"/rest/api/content/{content_id}/property/{key}")


def set_content_property(content_id: int, key: str, value: Any, version_number: int | None = None) -> Dict[str, Any]:
    if version_number is None:
        existing = confluence_request("GET", f"/rest/api/content/{content_id}/property/{key}")
        if "error" not in existing and "version" in existing:
            version_number = int(existing["version"]["number"]) + 1
        else:
            version_number = 1

    payload = {"key": key, "value": value, "version": {"number": version_number}}
    # PUT creates/updates
    return confluence_request("PUT", f"/rest/api/content/{content_id}/property/{key}", json=payload)
