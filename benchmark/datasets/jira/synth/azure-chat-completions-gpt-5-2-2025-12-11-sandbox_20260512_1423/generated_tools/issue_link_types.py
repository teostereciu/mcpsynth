from typing import Any, Dict

from ._client import get_client


def get_issue_link_types() -> Any:
    """GET /issueLinkType"""
    return get_client().request("GET", "/issueLinkType")


def get_issue_link_type(issue_link_type_id: str) -> Any:
    """GET /issueLinkType/{issueLinkTypeId}"""
    return get_client().request("GET", f"/issueLinkType/{issue_link_type_id}")


def create_issue_link_type(name: str, inward: str, outward: str) -> Any:
    """POST /issueLinkType"""
    return get_client().request("POST", "/issueLinkType", json_body={"name": name, "inward": inward, "outward": outward})


def update_issue_link_type(issue_link_type_id: str, name: str, inward: str, outward: str) -> Any:
    """PUT /issueLinkType/{issueLinkTypeId}"""
    return get_client().request(
        "PUT",
        f"/issueLinkType/{issue_link_type_id}",
        json_body={"name": name, "inward": inward, "outward": outward},
    )


def delete_issue_link_type(issue_link_type_id: str) -> Any:
    """DELETE /issueLinkType/{issueLinkTypeId}"""
    return get_client().request("DELETE", f"/issueLinkType/{issue_link_type_id}")
