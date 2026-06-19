from __future__ import annotations

from typing import Any, Dict, Optional

from . import mcp
from .jira_client import JiraClient


@mcp.tool()
def jira_jql_autocomplete_data(project_ids: Optional[list[int]] = None, include_collapsed_fields: Optional[bool] = None) -> Dict[str, Any]:
    """Get JQL field/function reference data.

    GET /rest/api/3/jql/autocompletedata (no filters)
    POST /rest/api/3/jql/autocompletedata (with filters)
    """

    client = JiraClient()
    if project_ids is None and include_collapsed_fields is None:
        return client.request("GET", "/jql/autocompletedata")

    payload: Dict[str, Any] = {}
    if project_ids is not None:
        payload["projectIds"] = project_ids
    if include_collapsed_fields is not None:
        payload["includeCollapsedFields"] = include_collapsed_fields
    return client.request("POST", "/jql/autocompletedata", json=payload)


@mcp.tool()
def jira_jql_autocomplete_suggestions(
    field_name: str,
    field_value: Optional[str] = None,
    predicate_name: Optional[str] = None,
    predicate_value: Optional[str] = None,
) -> Dict[str, Any]:
    """Get JQL autocomplete suggestions.

    GET /rest/api/3/jql/autocompletedata/suggestions
    """

    client = JiraClient()
    params: Dict[str, Any] = {"fieldName": field_name}
    if field_value is not None:
        params["fieldValue"] = field_value
    if predicate_name is not None:
        params["predicateName"] = predicate_name
    if predicate_value is not None:
        params["predicateValue"] = predicate_value
    return client.request("GET", "/jql/autocompletedata/suggestions", params=params)


@mcp.tool()
def jira_jql_parse(queries: list[str], validation: str = "strict") -> Dict[str, Any]:
    """Parse and validate JQL queries.

    POST /rest/api/3/jql/parse?validation=...
    """

    client = JiraClient()
    return client.request("POST", "/jql/parse", params={"validation": validation}, json={"queries": queries})


@mcp.tool()
def jira_jql_convert_user_identifiers(query_strings: list[str]) -> Dict[str, Any]:
    """Convert user identifiers to account IDs in JQL.

    POST /rest/api/3/jql/pdcleaner
    """

    client = JiraClient()
    return client.request("POST", "/jql/pdcleaner", json={"queryStrings": query_strings})


@mcp.tool()
def jira_jql_sanitize(queries: list[Dict[str, Any]]) -> Dict[str, Any]:
    """Sanitize JQL queries.

    POST /rest/api/3/jql/sanitize

    Args:
        queries: List of JqlQueryToSanitize objects.
    """

    client = JiraClient()
    return client.request("POST", "/jql/sanitize", json={"queries": queries})
