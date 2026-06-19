from typing import Any

from jira_client import JiraClient


def list_issue_types() -> Any:
    """GET /issuetype"""
    client = JiraClient()
    return client.request("GET", "/issuetype")


def list_priorities() -> Any:
    """GET /priority"""
    client = JiraClient()
    return client.request("GET", "/priority")


def list_statuses() -> Any:
    """GET /status"""
    client = JiraClient()
    return client.request("GET", "/status")
