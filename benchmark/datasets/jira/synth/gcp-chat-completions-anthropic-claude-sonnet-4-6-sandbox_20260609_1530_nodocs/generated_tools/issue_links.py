"""
MCP tools for Jira Issue Links.
"""

from typing import Any, Dict, Optional
from mcp.server.fastmcp import FastMCP
from generated_tools.client import jira_get, jira_post, jira_delete

mcp = FastMCP("jira-issue-links")


@mcp.tool()
def get_issue_link(link_id: str) -> Dict[str, Any]:
    """
    Get details of a specific issue link.

    Args:
        link_id: The issue link ID.
    """
    return jira_get(f"/issueLink/{link_id}")


@mcp.tool()
def create_issue_link(
    link_type: str,
    inward_issue_key: str,
    outward_issue_key: str,
    comment: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Create a link between two Jira issues.

    Args:
        link_type: The name of the link type (e.g. 'Blocks', 'Clones', 'Duplicate',
                   'Relates', 'is blocked by'). Use get_issue_link_types to see available types.
        inward_issue_key: The key of the inward issue (e.g. 'PROJ-1').
        outward_issue_key: The key of the outward issue (e.g. 'PROJ-2').
        comment: Optional comment to add when creating the link.
    """
    body: Dict[str, Any] = {
        "type": {"name": link_type},
        "inwardIssue": {"key": inward_issue_key},
        "outwardIssue": {"key": outward_issue_key},
    }
    if comment:
        body["comment"] = {
            "body": {
                "type": "doc",
                "version": 1,
                "content": [
                    {
                        "type": "paragraph",
                        "content": [{"type": "text", "text": comment}],
                    }
                ],
            }
        }
    return jira_post("/issueLink", json=body)


@mcp.tool()
def delete_issue_link(link_id: str) -> Dict[str, Any]:
    """
    Delete an issue link.

    Args:
        link_id: The issue link ID.
    """
    return jira_delete(f"/issueLink/{link_id}")


@mcp.tool()
def get_issue_link_types() -> Dict[str, Any]:
    """
    Get all available issue link types (e.g. Blocks, Clones, Relates, Duplicate).
    Use this to find valid link type names for create_issue_link.
    """
    return jira_get("/issueLinkType")


@mcp.tool()
def get_issue_link_type(link_type_id: str) -> Dict[str, Any]:
    """
    Get details of a specific issue link type.

    Args:
        link_type_id: The issue link type ID.
    """
    return jira_get(f"/issueLinkType/{link_type_id}")


@mcp.tool()
def create_issue_link_type(
    name: str,
    inward: str,
    outward: str,
) -> Dict[str, Any]:
    """
    Create a new issue link type.

    Args:
        name: The name of the link type (e.g. 'Blocks').
        inward: The inward description (e.g. 'is blocked by').
        outward: The outward description (e.g. 'blocks').
    """
    return jira_post(
        "/issueLinkType",
        json={"name": name, "inward": inward, "outward": outward},
    )


@mcp.tool()
def update_issue_link_type(
    link_type_id: str,
    name: str,
    inward: str,
    outward: str,
) -> Dict[str, Any]:
    """
    Update an existing issue link type.

    Args:
        link_type_id: The issue link type ID.
        name: New name for the link type.
        inward: New inward description.
        outward: New outward description.
    """
    from generated_tools.client import jira_put
    return jira_put(
        f"/issueLinkType/{link_type_id}",
        json={"name": name, "inward": inward, "outward": outward},
    )


@mcp.tool()
def delete_issue_link_type(link_type_id: str) -> Dict[str, Any]:
    """
    Delete an issue link type.

    Args:
        link_type_id: The issue link type ID.
    """
    return jira_delete(f"/issueLinkType/{link_type_id}")
