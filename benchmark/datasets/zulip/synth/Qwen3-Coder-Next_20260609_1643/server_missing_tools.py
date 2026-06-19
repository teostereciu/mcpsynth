#!/usr/bin/env python3
"""Zulip MCP Server - A Model Context Protocol server for Zulip REST API."""

import os
import json
import requests
from typing import Any, Dict, List, Optional
from mcp.server.fastmcp import FastMCP

# Environment variables
ZULIP_EMAIL = os.environ.get("ZULIP_EMAIL")
ZULIP_API_KEY = os.environ.get("ZULIP_API_KEY")
ZULIP_SITE = os.environ.get("ZULIP_SITE")

if not all([ZULIP_EMAIL, ZULIP_API_KEY, ZULIP_SITE]):
    raise ValueError("ZULIP_EMAIL, ZULIP_API_KEY, and ZULIP_SITE environment variables must be set")

# Base URL for Zulip API
BASE_URL = f"{ZULIP_SITE.rstrip('/')}/api/v1"

# Create MCP server
mcp = FastMCP("zulip")

# Helper function to make HTTP requests to Zulip API
def zulip_request(
    method: str,
    endpoint: str,
    params: Optional[Dict[str, Any]] = None,
    data: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """Make a request to the Zulip API."""
    url = f"{BASE_URL}{endpoint}"
    auth = (ZULIP_EMAIL, ZULIP_API_KEY)
    
    try:
        if method.upper() in ["GET", "DELETE"]:
            response = requests.request(method, url, params=params, auth=auth)
        else:
            response = requests.request(method, url, json=data, params=params, auth=auth)
        
        # Parse JSON response or return text for non-JSON
        try:
            return response.json()
        except json.JSONDecodeError:
            return {"raw_response": response.text}
            
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}

# ============================================================================
# Missing tools to append
# ============================================================================

@mcp.tool()
def get_user_channels(user_id: int) -> Dict[str, Any]:
    """Get channels a user is subscribed to.
    
    Args:
        user_id: The ID of the user.
    """
    return zulip_request("GET", f"/users/{user_id}/channels")


@mcp.tool()
def create_invite_link(
    invite_expires_in_minutes: int,
    invite_as: Optional[int] = None,
    stream_ids: Optional[List[int]] = None,
    group_ids: Optional[List[int]] = None,
    include_realm_default_subscriptions: Optional[bool] = None,
    welcome_message_custom_text: Optional[str] = None,
) -> Dict[str, Any]:
    """Create a reusable invitation link.
    
    Args:
        invite_expires_in_minutes: Number of minutes before the invitation expires.
        invite_as: Role for invited users (100: Owner, 200: Admin, 300: Moderator, 400: Member, 600: Guest).
        stream_ids: List of channel IDs to subscribe new users to.
        group_ids: List of user group IDs to add new users to.
        include_realm_default_subscriptions: Whether to subscribe new users to default channels.
        welcome_message_custom_text: Custom welcome message for new users.
    """
    data = {"invite_expires_in_minutes": invite_expires_in_minutes}
    
    if invite_as is not None:
        data["invite_as"] = invite_as
    if stream_ids is not None:
        data["stream_ids"] = json.dumps(stream_ids)
    if group_ids is not None:
        data["group_ids"] = json.dumps(group_ids)
    if include_realm_default_subscriptions is not None:
        data["include_realm_default_subscriptions"] = str(include_realm_default_subscriptions).lower()
    if welcome_message_custom_text is not None:
        data["welcome_message_custom_text"] = welcome_message_custom_text
    
    return zulip_request("POST", "/invites/multiuse", data=data)


@mcp.tool()
def resend_email_invite(invite_id: int) -> Dict[str, Any]:
    """Resend an email invitation.
    
    Args:
        invite_id: The ID of the invitation to resend.
    """
    return zulip_request("POST", f"/invites/{invite_id}/resend")


@mcp.tool()
def revoke_email_invite(invite_id: int) -> Dict[str, Any]:
    """Revoke an email invitation.
    
    Args:
        invite_id: The ID of the invitation to revoke.
    """
    return zulip_request("DELETE", f"/invites/{invite_id}")


@mcp.tool()
def revoke_invite_link(invite_id: int) -> Dict[str, Any]:
    """Revoke a reusable invitation link.
    
    Args:
        invite_id: The ID of the invitation link to revoke.
    """
    return zulip_request("DELETE", f"/invites/multiuse/{invite_id}")
