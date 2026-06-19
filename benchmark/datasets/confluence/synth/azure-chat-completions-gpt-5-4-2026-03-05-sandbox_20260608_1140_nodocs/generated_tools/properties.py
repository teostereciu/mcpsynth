from typing import Any, Dict

from generated_tools.confluence_client import client


def get_page_property(page_id: str, key: str) -> Dict[str, Any]:
    return client.request("GET", f"/rest/api/content/{page_id}/property/{key}")


def set_page_property(page_id: str, key: str, value: Any) -> Dict[str, Any]:
    existing = get_page_property(page_id, key)
    if existing.get("error"):
        payload = {"key": key, "value": value}
        return client.request("POST", f"/rest/api/content/{page_id}/property", json_body=payload)
    prop_id = existing.get("id")
    version_number = ((existing.get("version") or {}).get("number") or 0) + 1
    payload = {"key": key, "value": value, "version": {"number": version_number}}
    return client.request("PUT", f"/rest/api/content/{page_id}/property/{prop_id}", json_body=payload)
