from typing import Any, Dict

from .jira_client import JiraClient


def list_issue_link_types():
    """GET /issueLinkType"""
    client = JiraClient()
    return client.request("GET", "/issueLinkType")


def get_issue_link_type(issueLinkTypeId: str):
    """GET /issueLinkType/{issueLinkTypeId}"""
    client = JiraClient()
    return client.request("GET", f"/issueLinkType/{issueLinkTypeId}")


def create_issue_link_type(name: str, inward: str, outward: str):
    """POST /issueLinkType"""
    client = JiraClient()
    return client.request("POST", "/issueLinkType", json={"name": name, "inward": inward, "outward": outward})


def update_issue_link_type(issueLinkTypeId: str, name: str, inward: str, outward: str):
    """PUT /issueLinkType/{issueLinkTypeId}"""
    client = JiraClient()
    return client.request("PUT", f"/issueLinkType/{issueLinkTypeId}", json={"name": name, "inward": inward, "outward": outward})


def delete_issue_link_type(issueLinkTypeId: str):
    """DELETE /issueLinkType/{issueLinkTypeId}"""
    client = JiraClient()
    return client.request("DELETE", f"/issueLinkType/{issueLinkTypeId}")
