import os
import requests

SLACK_API_BASE = "https://slack.com/api"
SLACK_BOT_TOKEN = os.environ.get("SLACK_BOT_TOKEN")


def _slack_headers():
    return {
        "Authorization": f"Bearer {SLACK_BOT_TOKEN}",
        "Content-Type": "application/json"
    }


def post_message(channel, text=None, blocks=None, attachments=None, **kwargs):
    """
    Send a message to a channel, private group, or DM.
    Args:
        channel (str): Channel ID or name
        text (str): Message text
        blocks (list): Block Kit blocks
        attachments (list): Attachments
        kwargs: Other optional Slack API arguments
    Returns:
        dict: Slack API response
    """
    payload = {"channel": channel}
    if text is not None:
        payload["text"] = text
    if blocks is not None:
        payload["blocks"] = blocks
    if attachments is not None:
        payload["attachments"] = attachments
    payload.update(kwargs)
    try:
        resp = requests.post(f"{SLACK_API_BASE}/chat.postMessage", json=payload, headers=_slack_headers())
        return resp.json()
    except Exception as e:
        return {"error": str(e)}


def update_message(channel, ts, text=None, blocks=None, attachments=None, **kwargs):
    """
    Update a message in a channel.
    Args:
        channel (str): Channel ID
        ts (str): Timestamp of the message
        text (str): Updated text
        blocks (list): Updated blocks
        attachments (list): Updated attachments
        kwargs: Other optional Slack API arguments
    Returns:
        dict: Slack API response
    """
    payload = {"channel": channel, "ts": ts}
    if text is not None:
        payload["text"] = text
    if blocks is not None:
        payload["blocks"] = blocks
    if attachments is not None:
        payload["attachments"] = attachments
    payload.update(kwargs)
    try:
        resp = requests.post(f"{SLACK_API_BASE}/chat.update", json=payload, headers=_slack_headers())
        return resp.json()
    except Exception as e:
        return {"error": str(e)}


def delete_message(channel, ts, **kwargs):
    """
    Delete a message from a channel.
    Args:
        channel (str): Channel ID
        ts (str): Timestamp of the message
        kwargs: Other optional Slack API arguments
    Returns:
        dict: Slack API response
    """
    payload = {"channel": channel, "ts": ts}
    payload.update(kwargs)
    try:
        resp = requests.post(f"{SLACK_API_BASE}/chat.delete", json=payload, headers=_slack_headers())
        return resp.json()
    except Exception as e:
        return {"error": str(e)}


def schedule_message(channel, post_at, text=None, blocks=None, attachments=None, **kwargs):
    """
    Schedule a message to be sent to a channel at a future time.
    Args:
        channel (str): Channel ID
        post_at (int): Unix timestamp for scheduled time
        text (str): Message text
        blocks (list): Block Kit blocks
        attachments (list): Attachments
        kwargs: Other optional Slack API arguments
    Returns:
        dict: Slack API response
    """
    payload = {"channel": channel, "post_at": post_at}
    if text is not None:
        payload["text"] = text
    if blocks is not None:
        payload["blocks"] = blocks
    if attachments is not None:
        payload["attachments"] = attachments
    payload.update(kwargs)
    try:
        resp = requests.post(f"{SLACK_API_BASE}/chat.scheduleMessage", json=payload, headers=_slack_headers())
        return resp.json()
    except Exception as e:
        return {"error": str(e)}

def delete_scheduled_message(channel, scheduled_message_id, **kwargs):
    """
    Delete a pending scheduled message from the queue.
    Args:
        channel (str): Channel ID
        scheduled_message_id (str): Scheduled message ID
        kwargs: Other optional Slack API arguments
    Returns:
        dict: Slack API response
    """
    payload = {"channel": channel, "scheduled_message_id": scheduled_message_id}
    payload.update(kwargs)
    try:
        resp = requests.post(f"{SLACK_API_BASE}/chat.deleteScheduledMessage", json=payload, headers=_slack_headers())
        return resp.json()
    except Exception as e:
        return {"error": str(e)}

def list_scheduled_messages(channel=None, cursor=None, latest=None, limit=None, oldest=None, team_id=None):
    """
    List scheduled messages.
    Args:
        channel (str): Channel ID (optional)
        cursor (str): Pagination cursor (optional)
        latest (str): Latest timestamp (optional)
        limit (int): Max results (optional)
        oldest (str): Oldest timestamp (optional)
        team_id (str): Team ID (optional)
    Returns:
        dict: Slack API response
    """
    payload = {}
    if channel is not None:
        payload["channel"] = channel
    if cursor is not None:
        payload["cursor"] = cursor
    if latest is not None:
        payload["latest"] = latest
    if limit is not None:
        payload["limit"] = limit
    if oldest is not None:
        payload["oldest"] = oldest
    if team_id is not None:
        payload["team_id"] = team_id
    try:
        resp = requests.post(f"{SLACK_API_BASE}/chat.scheduledMessages.list", json=payload, headers=_slack_headers())
        return resp.json()
    except Exception as e:
        return {"error": str(e)}
