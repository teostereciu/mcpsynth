import os
import requests

SLACK_API_BASE = "https://slack.com/api"
SLACK_BOT_TOKEN = os.environ.get("SLACK_BOT_TOKEN")

def _slack_headers():
    return {
        "Authorization": f"Bearer {SLACK_BOT_TOKEN}",
        "Content-Type": "application/json"
    }

def list_conversations(types="public_channel", cursor=None, exclude_archived=False, limit=100, team_id=None):
    """
    List all channels/conversations in a Slack team.
    Args:
        types (str): Comma-separated types (public_channel, private_channel, mpim, im)
        cursor (str): Pagination cursor
        exclude_archived (bool): Exclude archived channels
        limit (int): Max results (<=1000)
        team_id (str): Team ID (optional)
    Returns:
        dict: Slack API response
    """
    payload = {
        "types": types,
        "exclude_archived": exclude_archived,
        "limit": limit
    }
    if cursor:
        payload["cursor"] = cursor
    if team_id:
        payload["team_id"] = team_id
    try:
        resp = requests.get(f"{SLACK_API_BASE}/conversations.list", headers=_slack_headers(), params=payload)
        return resp.json()
    except Exception as e:
        return {"error": str(e)}

def conversation_info(channel, include_locale=False, include_num_members=False):
    """
    Retrieve information about a conversation.
    Args:
        channel (str): Conversation ID
        include_locale (bool): Include locale
        include_num_members (bool): Include member count
    Returns:
        dict: Slack API response
    """
    payload = {"channel": channel}
    if include_locale:
        payload["include_locale"] = True
    if include_num_members:
        payload["include_num_members"] = True
    try:
        resp = requests.get(f"{SLACK_API_BASE}/conversations.info", headers=_slack_headers(), params=payload)
        return resp.json()
    except Exception as e:
        return {"error": str(e)}

def open_conversation(users=None, channel=None, return_im=False, prevent_creation=False):
    """
    Open or resume a direct message or multi-person direct message.
    Args:
        users (list or str): List of user IDs or comma-separated string
        channel (str): IM or MPIM channel ID
        return_im (bool): Return full IM channel definition
        prevent_creation (bool): Do not create a DM/MPIM if it doesn't exist
    Returns:
        dict: Slack API response
    """
    payload = {}
    if users:
        if isinstance(users, list):
            payload["users"] = ",".join(users)
        else:
            payload["users"] = users
    if channel:
        payload["channel"] = channel
    if return_im:
        payload["return_im"] = True
    if prevent_creation:
        payload["prevent_creation"] = True
    try:
        resp = requests.post(f"{SLACK_API_BASE}/conversations.open", json=payload, headers=_slack_headers())
        return resp.json()
    except Exception as e:
        return {"error": str(e)}

def create_conversation(name, is_private=False, team_id=None):
    """
    Initiate a public or private channel-based conversation.
    Args:
        name (str): Name of the channel
        is_private (bool): Create a private channel
        team_id (str): Team ID (optional)
    Returns:
        dict: Slack API response
    """
    payload = {"name": name, "is_private": is_private}
    if team_id:
        payload["team_id"] = team_id
    try:
        resp = requests.post(f"{SLACK_API_BASE}/conversations.create", json=payload, headers=_slack_headers())
        return resp.json()
    except Exception as e:
        return {"error": str(e)}

def invite_to_conversation(channel, users, force=False):
    """
    Invite users to a channel.
    Args:
        channel (str): Channel ID
        users (list or str): List of user IDs or comma-separated string
        force (bool): Continue inviting valid users if some are invalid
    Returns:
        dict: Slack API response
    """
    if isinstance(users, list):
        users = ",".join(users)
    payload = {"channel": channel, "users": users, "force": force}
    try:
        resp = requests.post(f"{SLACK_API_BASE}/conversations.invite", json=payload, headers=_slack_headers())
        return resp.json()
    except Exception as e:
        return {"error": str(e)}

def conversation_members(channel, cursor=None, limit=100):
    """
    Retrieve members of a conversation.
    Args:
        channel (str): Conversation ID
        cursor (str): Pagination cursor
        limit (int): Max number of items (<=1000)
    Returns:
        dict: Slack API response
    """
    payload = {"channel": channel, "limit": limit}
    if cursor:
        payload["cursor"] = cursor
    try:
        resp = requests.get(f"{SLACK_API_BASE}/conversations.members", headers=_slack_headers(), params=payload)
        return resp.json()
    except Exception as e:
        return {"error": str(e)}

def conversation_replies(channel, ts, cursor=None, include_all_metadata=False, inclusive=False, latest=None, limit=1000, oldest=None):
    """
    Retrieve a thread of messages posted to a conversation.
    Args:
        channel (str): Conversation ID
        ts (str): Thread parent message timestamp
        cursor (str): Pagination cursor
        include_all_metadata (bool): Return all metadata
        inclusive (bool): Include messages with oldest/latest timestamps
        latest (str): Only messages before this Unix timestamp
        limit (int): Max number of items (<=1000)
        oldest (str): Only messages after this Unix timestamp
    Returns:
        dict: Slack API response
    """
    payload = {"channel": channel, "ts": ts, "limit": limit}
    if cursor:
        payload["cursor"] = cursor
    if include_all_metadata:
        payload["include_all_metadata"] = True
    if inclusive:
        payload["inclusive"] = True
    if latest:
        payload["latest"] = latest
    if oldest:
        payload["oldest"] = oldest
    try:
        resp = requests.get(f"{SLACK_API_BASE}/conversations.replies", headers=_slack_headers(), params=payload)
        return resp.json()
    except Exception as e:
        return {"error": str(e)}

def conversation_history(channel, cursor=None, include_all_metadata=False, inclusive=False, latest=None, limit=100, oldest=None):
    """
    Fetch a conversation's history of messages and events.
    Args:
        channel (str): Conversation ID
        cursor (str): Pagination cursor
        include_all_metadata (bool): Return all metadata
        inclusive (bool): Include messages with oldest/latest timestamps
        latest (str): Only messages before this Unix timestamp
        limit (int): Max number of items (<=999)
        oldest (str): Only messages after this Unix timestamp
    Returns:
        dict: Slack API response
    """
    payload = {"channel": channel, "limit": limit}
    if cursor:
        payload["cursor"] = cursor
    if include_all_metadata:
        payload["include_all_metadata"] = True
    if inclusive:
        payload["inclusive"] = True
    if latest:
        payload["latest"] = latest
    if oldest:
        payload["oldest"] = oldest
    try:
        resp = requests.get(f"{SLACK_API_BASE}/conversations.history", headers=_slack_headers(), params=payload)
        return resp.json()
    except Exception as e:
        return {"error": str(e)}
