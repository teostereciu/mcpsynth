from typing import Any, Dict, List, Optional

from .slack_client import get_client


def chat_post_message(
    channel: str,
    text: Optional[str] = None,
    blocks: Optional[List[Dict[str, Any]]] = None,
    attachments: Optional[List[Dict[str, Any]]] = None,
    thread_ts: Optional[str] = None,
    reply_broadcast: Optional[bool] = None,
    mrkdwn: Optional[bool] = None,
    unfurl_links: Optional[bool] = None,
    unfurl_media: Optional[bool] = None,
    metadata: Optional[Dict[str, Any]] = None,
    icon_emoji: Optional[str] = None,
    icon_url: Optional[str] = None,
    username: Optional[str] = None,
    parse: Optional[str] = None,
    link_names: Optional[bool] = None,
    markdown_text: Optional[str] = None,
    current_draft_last_updated_ts: Optional[str] = None,
    as_user: Optional[bool] = None,
) -> Dict[str, Any]:
    payload: Dict[str, Any] = {"channel": channel}
    if text is not None:
        payload["text"] = text
    if blocks is not None:
        payload["blocks"] = blocks
    if attachments is not None:
        payload["attachments"] = attachments
    if thread_ts is not None:
        payload["thread_ts"] = thread_ts
    if reply_broadcast is not None:
        payload["reply_broadcast"] = reply_broadcast
    if mrkdwn is not None:
        payload["mrkdwn"] = mrkdwn
    if unfurl_links is not None:
        payload["unfurl_links"] = unfurl_links
    if unfurl_media is not None:
        payload["unfurl_media"] = unfurl_media
    if metadata is not None:
        payload["metadata"] = metadata
    if icon_emoji is not None:
        payload["icon_emoji"] = icon_emoji
    if icon_url is not None:
        payload["icon_url"] = icon_url
    if username is not None:
        payload["username"] = username
    if parse is not None:
        payload["parse"] = parse
    if link_names is not None:
        payload["link_names"] = link_names
    if markdown_text is not None:
        payload["markdown_text"] = markdown_text
    if current_draft_last_updated_ts is not None:
        payload["current_draft_last_updated_ts"] = current_draft_last_updated_ts
    if as_user is not None:
        payload["as_user"] = as_user

    return get_client().request("POST", "/chat.postMessage", json=payload)


def chat_update(
    channel: str,
    ts: str,
    text: Optional[str] = None,
    blocks: Optional[List[Dict[str, Any]]] = None,
    attachments: Optional[List[Dict[str, Any]]] = None,
    unfurled_attachments: Optional[List[Dict[str, Any]]] = None,
    markdown_text: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    link_names: Optional[bool] = None,
    parse: Optional[str] = None,
    reply_broadcast: Optional[bool] = None,
    file_ids: Optional[List[str]] = None,
    as_user: Optional[bool] = None,
) -> Dict[str, Any]:
    payload: Dict[str, Any] = {"channel": channel, "ts": ts}
    if text is not None:
        payload["text"] = text
    if blocks is not None:
        payload["blocks"] = blocks
    if attachments is not None:
        payload["attachments"] = attachments
    if unfurled_attachments is not None:
        payload["unfurled_attachments"] = unfurled_attachments
    if markdown_text is not None:
        payload["markdown_text"] = markdown_text
    if metadata is not None:
        payload["metadata"] = metadata
    if link_names is not None:
        payload["link_names"] = link_names
    if parse is not None:
        payload["parse"] = parse
    if reply_broadcast is not None:
        payload["reply_broadcast"] = reply_broadcast
    if file_ids is not None:
        payload["file_ids"] = file_ids
    if as_user is not None:
        payload["as_user"] = as_user

    return get_client().request("POST", "/chat.update", json=payload)


def chat_delete(channel: str, ts: str, as_user: Optional[bool] = None) -> Dict[str, Any]:
    payload: Dict[str, Any] = {"channel": channel, "ts": ts}
    if as_user is not None:
        payload["as_user"] = as_user
    return get_client().request("POST", "/chat.delete", json=payload)
