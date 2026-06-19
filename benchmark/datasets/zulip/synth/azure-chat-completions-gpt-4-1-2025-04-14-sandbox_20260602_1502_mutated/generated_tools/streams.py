import os
import requests

ZULIP_SITE = os.environ.get('ZULIP_SITE')
ZULIP_EMAIL = os.environ.get('ZULIP_EMAIL')
ZULIP_API_KEY = os.environ.get('ZULIP_API_KEY')
BASE_URL = f'{ZULIP_SITE}/api/v1'

def get_streams(include_public=True, include_web_public=False, include_subscribed=True, exclude_archived=True, include_all=False, include_default=False, include_owner_subscribed=False, include_can_access_content=False):
    """
    Get all channels the user has access to.
    Args:
        include_public (bool): Include all public channels
        include_web_public (bool): Include all web-public channels
        include_subscribed (bool): Include all channels the user is subscribed to
        exclude_archived (bool): Exclude archived channels
        include_all (bool): Include all channels user has metadata access to
        include_default (bool): Include all default channels for the user's realm
        include_owner_subscribed (bool): For bots, include owner's subscriptions
        include_can_access_content (bool): Include all channels user can access content for
    Returns:
        dict: JSON response from Zulip
    """
    url = f'{BASE_URL}/streams'
    params = {
        'include_public': include_public,
        'include_web_public': include_web_public,
        'include_subscribed': include_subscribed,
        'exclude_archived': exclude_archived,
        'include_all': include_all,
        'include_default': include_default,
        'include_owner_subscribed': include_owner_subscribed,
        'include_can_access_content': include_can_access_content,
    }
    resp = requests.get(url, auth=(ZULIP_EMAIL, ZULIP_API_KEY), params=params)
    try:
        return resp.json()
    except Exception:
        return {'error': 'Invalid response', 'status_code': resp.status_code}

def archive_stream(stream_id):
    """
    Archive (delete) a channel by ID. Organization admin only.
    Args:
        stream_id (int): ID of the channel to archive
    Returns:
        dict: JSON response from Zulip
    """
    url = f'{BASE_URL}/streams/{stream_id}'
    resp = requests.delete(url, auth=(ZULIP_EMAIL, ZULIP_API_KEY))
    try:
        return resp.json()
    except Exception:
        return {'error': 'Invalid response', 'status_code': resp.status_code}

def update_stream(stream_id, description=None, new_name=None, is_private=None, is_web_public=None, history_public_to_subscribers=None, is_default_stream=None, message_retention_days=None, is_archived=None, folder_id=None, topics_policy=None, can_add_subscribers_group=None, can_remove_subscribers_group=None, can_administer_channel_group=None):
    """
    Update a channel's settings.
    Args:
        stream_id (int): Channel ID
        description (str, optional): New description
        new_name (str, optional): New channel name
        is_private (bool, optional): Make channel private
        is_web_public (bool, optional): Make channel web-public
        history_public_to_subscribers (bool, optional): Shared history for new members
        is_default_stream (bool, optional): Default channel for new users
        message_retention_days (str|int, optional): Days to retain messages
        is_archived (bool, optional): Unarchive channel
        folder_id (int, optional): Channel folder
        topics_policy (str, optional): Topics policy
        can_add_subscribers_group (dict, optional): Who can add subscribers
        can_remove_subscribers_group (dict, optional): Who can remove subscribers
        can_administer_channel_group (dict, optional): Who can administer channel
    Returns:
        dict: JSON response from Zulip
    """
    url = f'{BASE_URL}/streams/{stream_id}'
    data = {}
    if description is not None:
        data['description'] = description
    if new_name is not None:
        data['new_name'] = new_name
    if is_private is not None:
        data['is_private'] = is_private
    if is_web_public is not None:
        data['is_web_public'] = is_web_public
    if history_public_to_subscribers is not None:
        data['history_public_to_subscribers'] = history_public_to_subscribers
    if is_default_stream is not None:
        data['is_default_stream'] = is_default_stream
    if message_retention_days is not None:
        data['message_retention_days'] = message_retention_days
    if is_archived is not None:
        data['is_archived'] = is_archived
    if folder_id is not None:
        data['folder_id'] = folder_id
    if topics_policy is not None:
        data['topics_policy'] = topics_policy
    if can_add_subscribers_group is not None:
        data['can_add_subscribers_group'] = can_add_subscribers_group
    if can_remove_subscribers_group is not None:
        data['can_remove_subscribers_group'] = can_remove_subscribers_group
    if can_administer_channel_group is not None:
        data['can_administer_channel_group'] = can_administer_channel_group
    resp = requests.patch(url, auth=(ZULIP_EMAIL, ZULIP_API_KEY), data=data)
    try:
        return resp.json()
    except Exception:
        return {'error': 'Invalid response', 'status_code': resp.status_code}
