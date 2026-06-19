"""Confluence v1+v2 Users API tools."""
import os
import requests
from mcp.server.fastmcp import FastMCP

def _auth():
    return (os.environ["JIRA_EMAIL"], os.environ["JIRA_API_TOKEN"])

def _base():
    return os.environ["CONFLUENCE_BASE_URL"].rstrip("/")

def _v1(path: str) -> str:
    return f"{_base()}/rest/api{path}"

def _v2(path: str) -> str:
    return f"{_base()}/api/v2{path}"

def register(mcp: FastMCP):

    @mcp.tool()
    def get_current_user() -> dict:
        """Get the currently authenticated user's profile."""
        try:
            r = requests.get(_v1("/user/current"), auth=_auth())
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "status_code": e.response.status_code}

    @mcp.tool()
    def get_user_by_account_id(account_id: str) -> dict:
        """Get a user's profile by their Atlassian account ID."""
        try:
            r = requests.get(_v1("/user"), params={"accountId": account_id}, auth=_auth())
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "status_code": e.response.status_code}

    @mcp.tool()
    def get_users_bulk(account_ids: list) -> dict:
        """Get user details for multiple account IDs at once (v2 API).
        account_ids: list of Atlassian account ID strings."""
        payload = {"accountIds": account_ids}
        try:
            r = requests.post(_v2("/users-bulk"), json=payload, auth=_auth())
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "status_code": e.response.status_code}

    @mcp.tool()
    def get_user_group_memberships(account_id: str, max_results: int = 25, start: int = 0) -> dict:
        """Get the groups that a user is a member of."""
        params = {"accountId": account_id, "max_results": max_results, "start": start}
        try:
            r = requests.get(_v1("/user/memberof"), params=params, auth=_auth())
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "status_code": e.response.status_code}
