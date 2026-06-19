"""
MCP tools for Jira JQL Search.
"""

from typing import Any, Dict, List, Optional
from mcp.server.fastmcp import FastMCP
from generated_tools.client import jira_get, jira_post

mcp = FastMCP("jira-search")


@mcp.tool()
def search_issues(
    jql: str,
    start_at: int = 0,
    max_results: int = 50,
    fields: Optional[str] = None,
    expand: Optional[str] = None,
    validate_query: str = "strict",
) -> Dict[str, Any]:
    """
    Search for Jira issues using JQL (Jira Query Language).

    Args:
        jql: JQL query string (e.g. 'project = PROJ AND status = "In Progress"').
        start_at: Index of the first result to return (for pagination).
        max_results: Maximum number of results to return (max 100).
        fields: Comma-separated list of fields to include in results.
                Use '*all' for all fields or '*navigable' for navigable fields.
        expand: Comma-separated list of entities to expand.
        validate_query: Query validation mode: 'strict', 'warn', 'none'.
    """
    body: Dict[str, Any] = {
        "jql": jql,
        "startAt": start_at,
        "maxResults": max_results,
        "validateQuery": validate_query,
    }
    if fields:
        body["fields"] = [f.strip() for f in fields.split(",")]
    if expand:
        body["expand"] = [e.strip() for e in expand.split(",")]
    return jira_post("/search", json=body)


@mcp.tool()
def search_issues_get(
    jql: str,
    start_at: int = 0,
    max_results: int = 50,
    fields: Optional[str] = None,
    expand: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Search for Jira issues using JQL via GET (for simpler queries).

    Args:
        jql: JQL query string.
        start_at: Index of the first result to return.
        max_results: Maximum number of results to return.
        fields: Comma-separated list of fields to include.
        expand: Comma-separated list of entities to expand.
    """
    params: Dict[str, Any] = {
        "jql": jql,
        "startAt": start_at,
        "maxResults": max_results,
    }
    if fields:
        params["fields"] = fields
    if expand:
        params["expand"] = expand
    return jira_get("/search", params=params)


@mcp.tool()
def get_field_reference() -> Dict[str, Any]:
    """
    Get a list of all available JQL fields for use in search queries.
    Returns field names, types, and supported operators.
    """
    return jira_get("/jql/autocompletedata")


@mcp.tool()
def parse_jql(
    queries: List[str],
    validation: str = "strict",
) -> Dict[str, Any]:
    """
    Parse and validate JQL queries, returning structured representations.

    Args:
        queries: List of JQL query strings to parse.
        validation: Validation mode: 'strict', 'warn', or 'none'.
    """
    return jira_post(
        "/jql/parse",
        json={"queries": queries},
        params={"validation": validation},
    )


@mcp.tool()
def get_jql_autocomplete_suggestions(
    field_name: str,
    field_value: str = "",
    predicate_name: Optional[str] = None,
    predicate_value: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Get autocomplete suggestions for a JQL field value.

    Args:
        field_name: The JQL field name to get suggestions for.
        field_value: The partial value to get suggestions for.
        predicate_name: The predicate name (for 'changed' queries).
        predicate_value: The partial predicate value.
    """
    params: Dict[str, Any] = {
        "fieldName": field_name,
        "fieldValue": field_value,
    }
    if predicate_name:
        params["predicateName"] = predicate_name
    if predicate_value:
        params["predicateValue"] = predicate_value
    return jira_get("/jql/autocompletedata/suggestions", params=params)
