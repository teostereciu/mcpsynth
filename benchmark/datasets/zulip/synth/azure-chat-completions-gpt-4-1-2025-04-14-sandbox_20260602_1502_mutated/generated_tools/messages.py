import os
import requests
from mcp.server.fastmcp import FastMCP

ZULIP_SITE = os.environ.get('ZULIP_SITE')
ZULIP_EMAIL = os.environ.get('ZULIP_EMAIL')
ZULIP_API_KEY = os.environ.get('ZULIP_API_KEY')
BASE_URL = f'{ZULIP_SITE}/api/v1'

def send_message(type, to, content, topic=None):
    """
    Send a channel or direct message.
    Args:
        type (str): 'direct', 'channel', 'channel_name', or 'private'
        to (str/int/list): channel name/ID or user IDs/emails
        content (str): message content
        topic (str, optional): topic for channel messages
    Returns:
        dict: JSON response from Zulip
    """
    url = f'{BASE_URL}/messages'
    data = {
        'type': type,
        'to': to,
        'content': content,
    }
    if topic:
        data['topic'] = topic
    resp = requests.post(url, auth=(ZULIP_EMAIL, ZULIP_API_KEY), data=data)
    try:
        return resp.json()
    except Exception:
        return {'error': 'Invalid response', 'status_code': resp.status_code}

def get_messages(start_message_id, before_count, after_count, filter_spec=None, anchor_dates=None, include_anchor=True, allow_empty_topic_name=False):
    """
    Fetch messages using Zulip's primary message retrieval endpoint.
    Args:
        start_message_id (str/int): anchor message id or 'newest', 'oldest', etc.
        before_count (int): messages before anchor
        after_count (int): messages after anchor
        filter_spec (list, optional): list of dicts for filtering
        anchor_dates (str, optional): ISO date/datetime
        include_anchor (bool, optional): include anchor message
        allow_empty_topic_name (bool, optional): allow empty topic name
    Returns:
        dict: JSON response from Zulip
    """
    url = f'{BASE_URL}/messages'
    params = {
        'start_message_id': start_message_id,
        'before_count': before_count,
        'after_count': after_count,
        'include_anchor': include_anchor,
        'allow_empty_topic_name': allow_empty_topic_name,
    }
    if filter_spec:
        params['filter_spec'] = filter_spec
    if anchor_dates:
        params['anchor_dates'] = anchor_dates
    resp = requests.get(url, auth=(ZULIP_EMAIL, ZULIP_API_KEY), params=params)
    try:
        return resp.json()
    except Exception:
        return {'error': 'Invalid response', 'status_code': resp.status_code}


def update_message(message_id, content=None, topic=None, propagate_mode=None, send_notification_to_old_thread=None, send_notification_to_new_thread=None, prev_content_sha256=None, stream_id=None):
    """
    Edit a message's content, topic, or channel.
    Args:
        message_id (int): ID of the message to update
        content (str, optional): new content
        topic (str, optional): new topic
        propagate_mode (str, optional): 'change_one', 'change_later', 'change_all'
        send_notification_to_old_thread (bool, optional): notify old thread
        send_notification_to_new_thread (bool, optional): notify new thread
        prev_content_sha256 (str, optional): SHA256 of previous content
        stream_id (int, optional): new channel ID
    Returns:
        dict: JSON response from Zulip
    """
    url = f'{BASE_URL}/messages/{message_id}'
    data = {}
    if content is not None:
        data['content'] = content
    if topic is not None:
        data['topic'] = topic
    if propagate_mode is not None:
        data['propagate_mode'] = propagate_mode
    if send_notification_to_old_thread is not None:
        data['send_notification_to_old_thread'] = send_notification_to_old_thread
    if send_notification_to_new_thread is not None:
        data['send_notification_to_new_thread'] = send_notification_to_new_thread
    if prev_content_sha256 is not None:
        data['prev_content_sha256'] = prev_content_sha256
    if stream_id is not None:
        data['stream_id'] = stream_id
    resp = requests.patch(url, auth=(ZULIP_EMAIL, ZULIP_API_KEY), data=data)
    try:
        return resp.json()
    except Exception:
        return {'error': 'Invalid response', 'status_code': resp.status_code}


def delete_message(message_id):
    """
    Permanently delete a message.
    Args:
        message_id (int): ID of the message to delete
    Returns:
        dict: JSON response from Zulip
    """
    url = f'{BASE_URL}/messages/{message_id}'
    resp = requests.delete(url, auth=(ZULIP_EMAIL, ZULIP_API_KEY))
    try:
        return resp.json()
    except Exception:
        return {'error': 'Invalid response', 'status_code': resp.status_code}
