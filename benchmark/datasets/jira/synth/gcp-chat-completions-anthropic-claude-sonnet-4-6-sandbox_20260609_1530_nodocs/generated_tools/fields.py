"""
MCP tools for Jira Fields (custom and system fields).
"""

from typing import Any, Dict, List, Optional
from mcp.server.fastmcp import FastMCP
from generated_tools.client import jira_get, jira_post, jira_put, jira_delete

mcp = FastMCP("jira-fields")


@mcp.tool()
def get_all_fields() -> Dict[str, Any]:
    """
    Get all fields (system and custom) available in Jira.
    Returns field IDs, names, types, and schema information.
    """
    return jira_get("/field")


@mcp.tool()
def get_custom_fields(
    start_at: int = 0,
    max_results: int = 50,
    type_: Optional[str] = None,
    id_: Optional[str] = None,
    query: Optional[str] = None,
    order_by: str = "contextsCount",
    expand: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Get custom fields with pagination and filtering.

    Args:
        start_at: Index of the first result to return.
        max_results: Maximum number of results to return.
        type_: Filter by field type (e.g. 'custom').
        id_: Comma-separated field IDs to filter by.
        query: Filter by field name (partial match).
        order_by: Field to sort by.
        expand: Expand options.
    """
    params: Dict[str, Any] = {
        "startAt": start_at,
        "maxResults": max_results,
        "orderBy": order_by,
    }
    if type_:
        params["type"] = type_
    if id_:
        params["id"] = id_
    if query:
        params["query"] = query
    if expand:
        params["expand"] = expand
    return jira_get("/field/search", params=params)


@mcp.tool()
def create_custom_field(
    name: str,
    field_type: str,
    description: Optional[str] = None,
    searcher_key: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Create a new custom field.

    Args:
        name: Field name.
        field_type: Field type key (e.g. 'com.atlassian.jira.plugin.system.customfieldtypes:textfield',
                    'com.atlassian.jira.plugin.system.customfieldtypes:select',
                    'com.atlassian.jira.plugin.system.customfieldtypes:datepicker').
        description: Field description.
        searcher_key: Searcher key for the field type.
    """
    body: Dict[str, Any] = {"name": name, "type": field_type}
    if description:
        body["description"] = description
    if searcher_key:
        body["searcherKey"] = searcher_key
    return jira_post("/field", json=body)


@mcp.tool()
def update_custom_field(
    field_id: str,
    name: Optional[str] = None,
    description: Optional[str] = None,
    searcher_key: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Update a custom field's configuration.

    Args:
        field_id: The custom field ID (e.g. 'customfield_10001').
        name: New field name.
        description: New field description.
        searcher_key: New searcher key.
    """
    body: Dict[str, Any] = {}
    if name is not None:
        body["name"] = name
    if description is not None:
        body["description"] = description
    if searcher_key is not None:
        body["searcherKey"] = searcher_key
    if not body:
        return {"error": "No fields provided to update."}
    return jira_put(f"/field/{field_id}", json=body)


@mcp.tool()
def delete_custom_field(field_id: str) -> Dict[str, Any]:
    """
    Delete a custom field. This is irreversible.

    Args:
        field_id: The custom field ID (e.g. 'customfield_10001').
    """
    return jira_delete(f"/field/{field_id}")


@mcp.tool()
def get_field_contexts(
    field_id: str,
    is_any_issue_type: Optional[bool] = None,
    is_global_context: Optional[bool] = None,
    context_id: Optional[str] = None,
    start_at: int = 0,
    max_results: int = 50,
) -> Dict[str, Any]:
    """
    Get contexts for a custom field.

    Args:
        field_id: The custom field ID.
        is_any_issue_type: Filter by whether context applies to any issue type.
        is_global_context: Filter by whether context is global.
        context_id: Comma-separated context IDs to filter by.
        start_at: Index of the first result to return.
        max_results: Maximum number of results to return.
    """
    params: Dict[str, Any] = {"startAt": start_at, "maxResults": max_results}
    if is_any_issue_type is not None:
        params["isAnyIssueType"] = is_any_issue_type
    if is_global_context is not None:
        params["isGlobalContext"] = is_global_context
    if context_id:
        params["contextId"] = context_id
    return jira_get(f"/field/{field_id}/context", params=params)


@mcp.tool()
def get_field_options(
    field_id: str,
    context_id: int,
    start_at: int = 0,
    max_results: int = 100,
    only_options: bool = False,
) -> Dict[str, Any]:
    """
    Get options for a custom select/multi-select field in a context.

    Args:
        field_id: The custom field ID.
        context_id: The context ID.
        start_at: Index of the first result to return.
        max_results: Maximum number of results to return.
        only_options: Return only options (not cascading options).
    """
    params: Dict[str, Any] = {
        "startAt": start_at,
        "maxResults": max_results,
        "onlyOptions": only_options,
    }
    return jira_get(f"/field/{field_id}/context/{context_id}/option", params=params)


@mcp.tool()
def create_field_option(
    field_id: str,
    context_id: int,
    options: List[Dict[str, Any]],
) -> Dict[str, Any]:
    """
    Create options for a custom select field.

    Args:
        field_id: The custom field ID.
        context_id: The context ID.
        options: List of option dicts. Each dict should have 'value' (str) and optionally
                 'disabled' (bool) and 'optionId' (str for cascading options).
                 Example: [{"value": "Option A"}, {"value": "Option B", "disabled": false}]
    """
    return jira_post(
        f"/field/{field_id}/context/{context_id}/option",
        json={"options": options},
    )


@mcp.tool()
def update_field_option(
    field_id: str,
    context_id: int,
    options: List[Dict[str, Any]],
) -> Dict[str, Any]:
    """
    Update options for a custom select field.

    Args:
        field_id: The custom field ID.
        context_id: The context ID.
        options: List of option dicts with 'id' (str) and 'value' (str) fields.
                 Example: [{"id": "10001", "value": "Updated Option"}]
    """
    return jira_put(
        f"/field/{field_id}/context/{context_id}/option",
        json={"options": options},
    )


@mcp.tool()
def delete_field_option(field_id: str, context_id: int, option_id: int) -> Dict[str, Any]:
    """
    Delete an option from a custom select field.

    Args:
        field_id: The custom field ID.
        context_id: The context ID.
        option_id: The option ID to delete.
    """
    return jira_delete(f"/field/{field_id}/context/{context_id}/option/{option_id}")
