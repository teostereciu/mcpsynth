from typing import Any, Dict, Optional

from .slack_client import SlackWebAPIClient, _clean_dict


def chat_post_message(
    channel: str,
    text: Optional[str] = None,
    blocks: Optional[Any] = None,
    attachments: Optional[Any] = None,
    thread_ts: Optional[str] = None,
    reply_broadcast: Optional[bool] = None,
    mrkdwn: Optional[bool] = None,
    parse: Optional[str] = None,
    link_names: Optional[bool] = None,
    unfurl_links: Optional[bool] = None,
    unfurl_media: Optional[bool] = None,
    username: Optional[str] = None,
    icon_emoji: Optional[str] = None,
    icon_url: Optional[str] = None,
    metadata: Optional[Any] = None,
    markdown_text: Optional[str] = None,
    current_draft_last_updated_ts: Optional[str] = None,
    client: Optional[SlackWebAPIClient] = None,
) -> Dict[str, Any]:
    client = client or SlackWebAPIClient()
    payload = _clean_dict(
        {
            "channel": channel,
            "text": text,
            "blocks": blocks,
            "attachments": attachments,
            "thread_ts": thread_ts,
            "reply_broadcast": reply_broadcast,
            "mrkdwn": mrkdwn,
            "parse": parse,
            "link_names": link_names,
            "unfurl_links": unfurl_links,
            "unfurl_media": unfurl_media,
            "username": username,
            "icon_emoji": icon_emoji,
            "icon_url": icon_url,
            "metadata": metadata,
            "markdown_text": markdown_text,
            "current_draft_last_updated_ts": current_draft_last_updated_ts,
        }
    )
    return client.post("chat.postMessage", payload)


def chat_delete(
    channel: str,
    ts: str,
    as_user: Optional[bool] = None,
    client: Optional[SlackWebAPIClient] = None,
) -> Dict[str, Any]:
    client = client or SlackWebAPIClient()
    payload = _clean_dict({"channel": channel, "ts": ts, "as_user": as_user})
    return client.post("chat.delete", payload)


def chat_schedule_message(
    channel: str,
    post_at: int,
    text: Optional[str] = None,
    blocks: Optional[Any] = None,
    attachments: Optional[Any] = None,
    thread_ts: Optional[str] = None,
    reply_broadcast: Optional[bool] = None,
    parse: Optional[str] = None,
    link_names: Optional[bool] = None,
    unfurl_links: Optional[bool] = None,
    unfurl_media: Optional[bool] = None,
    as_user: Optional[bool] = None,
    markdown_text: Optional[str] = None,
    metadata: Optional[Any] = None,
    client: Optional[SlackWebAPIClient] = None,
) -> Dict[str, Any]:
    client = client or SlackWebAPIClient()
    payload = _clean_dict(
        {
            "channel": channel,
            "post_at": post_at,
            "text": text,
            "blocks": blocks,
            "attachments": attachments,
            "thread_ts": thread_ts,
            "reply_broadcast": reply_broadcast,
            "parse": parse,
            "link_names": link_names,
            "unfurl_links": unfurl_links,
            "unfurl_media": unfurl_media,
            "as_user": as_user,
            "markdown_text": markdown_text,
            "metadata": metadata,
        }
    )
    return client.post("chat.scheduleMessage", payload)


def chat_update(
    channel: str,
    ts: str,
    text: Optional[str] = None,
    blocks: Optional[Any] = None,
    attachments: Optional[Any] = None,
    unfurled_attachments: Optional[Any] = None,
    as_user: Optional[bool] = None,
    markdown_text: Optional[str] = None,
    metadata: Optional[Any] = None,
    link_names: Optional[bool] = None,
    parse: Optional[str] = None,
    reply_broadcast: Optional[bool] = None,
    file_ids: Optional[Any] = None,
    client: Optional[SlackWebAPIClient] = None,
) -> Dict[str, Any]:
    client = client or SlackWebAPIClient()
    payload = _clean_dict(
        {
            "channel": channel,
            "ts": ts,
            "text": text,
            "blocks": blocks,
            "attachments": attachments,
            "unfurled_attachments": unfurled_attachments,
            "as_user": as_user,
            "markdown_text": markdown_text,
            "metadata": metadata,
            "link_names": link_names,
            "parse": parse,
            "reply_broadcast": reply_broadcast,
            "file_ids": file_ids,
        }
    )
    return client.post("chat.update", payload)
