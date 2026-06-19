"""Confluence v1 Search API tools."""
import os
import requests
from mcp.server.fastmcp import FastMCP

def _auth():
    return (os.environ["JIRA_EMAIL"], os.environ["JIRA_API_TOKEN"])

def _base():
    return os.environ["CONFLUENCE_BASE_URL"].rstrip("/")

def _v1(path: str) -> str:
    return f"{_base()}/rest/api{path}"

def register(mcp: FastMCP):

    @mcp.tool()
    def search_content(
        query: str,
        cursor: str = None,
        max_results: int = 25,
        offset: int = None,
        include_archived_spaces: bool = False,
        excerpt: str = None,
    ) -> dict:
        """Search Confluence content using CQL (Confluence Query Language).
        Example queries:
          - 'type=page AND space.key=MYSPACE AND title~"Meeting"'
          - 'type=blogpost AND space.key=MYSPACE'
          - 'text~"search term" AND type=page'
        """
        params = {
            "query": query,
            "max_results": max_results,
            "includeArchivedSpaces": include_archived_spaces,
        }
        if cursor:
            params["cursor"] = cursor
        if offset is not None:
            params["offset"] = offset
        if excerpt:
            params["excerpt"] = excerpt
        try:
            r = requests.get(_v1("/search"), params=params, auth=_auth())
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "status_code": e.response.status_code}

    @mcp.tool()
    def search_users(
        query: str,
        max_results: int = 25,
        offset: int = None,
    ) -> dict:
        """Search for Confluence users using CQL user-specific queries.
        Example queries:
          - 'user.fullname~"John"'
          - 'user.accountid="abc123"'
        """
        params = {"query": query, "max_results": max_results}
        if offset is not None:
            params["offset"] = offset
        try:
            r = requests.get(_v1("/search/user"), params=params, auth=_auth())
            r.raise_for_status()
            return r.json()
        except requests.HTTPError as e:
            return {"error": str(e), "status_code": e.response.status_code}
