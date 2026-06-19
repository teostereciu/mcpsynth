import os
from typing import Any, Dict, Optional

from mcp.server.fastmcp import FastMCP

from generated_tools.auth import auth_test
from generated_tools.chat import (
    chat_delete,
    chat_post_message,
    chat_schedule_message,
    chat_update,
)
from generated_tools.conversations import (
    conversations_create,
    conversations_history,
    conversations_invite,
    conversations_join,
    conversations_list,
    conversations_members,
    conversations_open,
    conversations_replies,
)
from generated_tools.files import (
    files_complete_upload_external,
    files_get_upload_url_external,
    files_list,
    files_upload,
)
from generated_tools.pins import pins_add, pins_list, pins_remove
from generated_tools.reactions import reactions_add, reactions_remove
from generated_tools.reminders import (
    reminders_add,
    reminders_complete,
    reminders_delete,
    reminders_list,
)
from generated_tools.search import search_files, search_messages
from generated_tools.team import team_info
from generated_tools.users import users_get_presence, users_list, users_lookup_by_email


mcp = FastMCP("slack-web-api")


def _require_token() -> Optional[Dict[str, Any]]:
    if not os.getenv("SLACK_BOT_TOKEN"):
        return {"ok": False, "error": "missing_env", "detail": "SLACK_BOT_TOKEN is not set"}
    return None


@mcp.tool()
def slack_auth_test() -> Dict[str, Any]:
    err = _require_token()
    if err:
        return err
    return auth_test()


# Chat / Messages
@mcp.tool()
def slack_chat_post_message(
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
) -> Dict[str, Any]:
    err = _require_token()
    if err:
        return err
    return chat_post_message(
        channel=channel,
        text=text,
        blocks=blocks,
        attachments=attachments,
        thread_ts=thread_ts,
        reply_broadcast=reply_broadcast,
        mrkdwn=mrkdwn,
        parse=parse,
        link_names=link_names,
        unfurl_links=unfurl_links,
        unfurl_media=unfurl_media,
        username=username,
        icon_emoji=icon_emoji,
        icon_url=icon_url,
        metadata=metadata,
        markdown_text=markdown_text,
        current_draft_last_updated_ts=current_draft_last_updated_ts,
    )


@mcp.tool()
def slack_chat_update(
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
) -> Dict[str, Any]:
    err = _require_token()
    if err:
        return err
    return chat_update(
        channel=channel,
        ts=ts,
        text=text,
        blocks=blocks,
        attachments=attachments,
        unfurled_attachments=unfurled_attachments,
        as_user=as_user,
        markdown_text=markdown_text,
        metadata=metadata,
        link_names=link_names,
        parse=parse,
        reply_broadcast=reply_broadcast,
        file_ids=file_ids,
    )


@mcp.tool()
def slack_chat_delete(channel: str, ts: str, as_user: Optional[bool] = None) -> Dict[str, Any]:
    err = _require_token()
    if err:
        return err
    return chat_delete(channel=channel, ts=ts, as_user=as_user)


@mcp.tool()
def slack_chat_schedule_message(
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
) -> Dict[str, Any]:
    err = _require_token()
    if err:
        return err
    return chat_schedule_message(
        channel=channel,
        post_at=post_at,
        text=text,
        blocks=blocks,
        attachments=attachments,
        thread_ts=thread_ts,
        reply_broadcast=reply_broadcast,
        parse=parse,
        link_names=link_names,
        unfurl_links=unfurl_links,
        unfurl_media=unfurl_media,
        as_user=as_user,
        markdown_text=markdown_text,
        metadata=metadata,
    )


# Conversations
@mcp.tool()
def slack_conversations_list(
    cursor: Optional[str] = None,
    exclude_archived: Optional[bool] = None,
    limit: Optional[int] = None,
    team_id: Optional[str] = None,
    types: Optional[str] = None,
) -> Dict[str, Any]:
    err = _require_token()
    if err:
        return err
    return conversations_list(
        cursor=cursor,
        exclude_archived=exclude_archived,
        limit=limit,
        team_id=team_id,
        types=types,
    )


@mcp.tool()
def slack_conversations_history(
    channel: str,
    cursor: Optional[str] = None,
    include_all_metadata: Optional[bool] = None,
    inclusive: Optional[bool] = None,
    latest: Optional[str] = None,
    limit: Optional[int] = None,
    oldest: Optional[str] = None,
) -> Dict[str, Any]:
    err = _require_token()
    if err:
        return err
    return conversations_history(
        channel=channel,
        cursor=cursor,
        include_all_metadata=include_all_metadata,
        inclusive=inclusive,
        latest=latest,
        limit=limit,
        oldest=oldest,
    )


@mcp.tool()
def slack_conversations_replies(
    channel: str,
    ts: str,
    cursor: Optional[str] = None,
    include_all_metadata: Optional[bool] = None,
    inclusive: Optional[bool] = None,
    latest: Optional[str] = None,
    limit: Optional[int] = None,
    oldest: Optional[str] = None,
) -> Dict[str, Any]:
    err = _require_token()
    if err:
        return err
    return conversations_replies(
        channel=channel,
        ts=ts,
        cursor=cursor,
        include_all_metadata=include_all_metadata,
        inclusive=inclusive,
        latest=latest,
        limit=limit,
        oldest=oldest,
    )


@mcp.tool()
def slack_conversations_members(
    channel: str,
    cursor: Optional[str] = None,
    limit: Optional[int] = None,
) -> Dict[str, Any]:
    err = _require_token()
    if err:
        return err
    return conversations_members(channel=channel, cursor=cursor, limit=limit)


@mcp.tool()
def slack_conversations_create(
    name: str,
    is_private: Optional[bool] = None,
    team_id: Optional[str] = None,
) -> Dict[str, Any]:
    err = _require_token()
    if err:
        return err
    return conversations_create(name=name, is_private=is_private, team_id=team_id)


@mcp.tool()
def slack_conversations_open(
    channel: Optional[str] = None,
    users: Optional[str] = None,
    return_im: Optional[bool] = None,
    prevent_creation: Optional[bool] = None,
) -> Dict[str, Any]:
    err = _require_token()
    if err:
        return err
    return conversations_open(
        channel=channel,
        users=users,
        return_im=return_im,
        prevent_creation=prevent_creation,
    )


@mcp.tool()
def slack_conversations_invite(
    channel: str,
    users: str,
    force: Optional[bool] = None,
) -> Dict[str, Any]:
    err = _require_token()
    if err:
        return err
    return conversations_invite(channel=channel, users=users, force=force)


@mcp.tool()
def slack_conversations_join(channel: str) -> Dict[str, Any]:
    err = _require_token()
    if err:
        return err
    return conversations_join(channel=channel)


# Users
@mcp.tool()
def slack_users_list(
    cursor: Optional[str] = None,
    include_locale: Optional[bool] = None,
    limit: Optional[int] = None,
    team_id: Optional[str] = None,
) -> Dict[str, Any]:
    err = _require_token()
    if err:
        return err
    return users_list(cursor=cursor, include_locale=include_locale, limit=limit, team_id=team_id)


@mcp.tool()
def slack_users_lookup_by_email(email: str) -> Dict[str, Any]:
    err = _require_token()
    if err:
        return err
    return users_lookup_by_email(email=email)


@mcp.tool()
def slack_users_get_presence(user: Optional[str] = None) -> Dict[str, Any]:
    err = _require_token()
    if err:
        return err
    return users_get_presence(user=user)


# Reactions
@mcp.tool()
def slack_reactions_add(channel: str, name: str, timestamp: str) -> Dict[str, Any]:
    err = _require_token()
    if err:
        return err
    return reactions_add(channel=channel, name=name, timestamp=timestamp)


@mcp.tool()
def slack_reactions_remove(
    name: str,
    channel: Optional[str] = None,
    timestamp: Optional[str] = None,
    file: Optional[str] = None,
    file_comment: Optional[str] = None,
) -> Dict[str, Any]:
    err = _require_token()
    if err:
        return err
    return reactions_remove(name=name, channel=channel, timestamp=timestamp, file=file, file_comment=file_comment)


# Files
@mcp.tool()
def slack_files_list(
    channel: Optional[str] = None,
    user: Optional[str] = None,
    types: Optional[str] = None,
    ts_from: Optional[str] = None,
    ts_to: Optional[str] = None,
    count: Optional[int] = None,
    page: Optional[int] = None,
    show_files_hidden_by_limit: Optional[bool] = None,
    team_id: Optional[str] = None,
) -> Dict[str, Any]:
    err = _require_token()
    if err:
        return err
    return files_list(
        channel=channel,
        user=user,
        types=types,
        ts_from=ts_from,
        ts_to=ts_to,
        count=count,
        page=page,
        show_files_hidden_by_limit=show_files_hidden_by_limit,
        team_id=team_id,
    )


@mcp.tool()
def slack_files_get_upload_url_external(
    filename: str,
    length: int,
    snippet_type: Optional[str] = None,
    alt_txt: Optional[str] = None,
) -> Dict[str, Any]:
    err = _require_token()
    if err:
        return err
    return files_get_upload_url_external(filename=filename, length=length, snippet_type=snippet_type, alt_txt=alt_txt)


@mcp.tool()
def slack_files_complete_upload_external(
    files: Any,
    channel_id: Optional[str] = None,
    channels: Optional[str] = None,
    thread_ts: Optional[str] = None,
    initial_comment: Optional[str] = None,
    blocks: Optional[Any] = None,
) -> Dict[str, Any]:
    err = _require_token()
    if err:
        return err
    return files_complete_upload_external(
        files=files,
        channel_id=channel_id,
        channels=channels,
        thread_ts=thread_ts,
        initial_comment=initial_comment,
        blocks=blocks,
    )


@mcp.tool()
def slack_files_upload(
    channels: Optional[str] = None,
    content: Optional[str] = None,
    filename: Optional[str] = None,
    filetype: Optional[str] = None,
    initial_comment: Optional[str] = None,
    thread_ts: Optional[str] = None,
    title: Optional[str] = None,
) -> Dict[str, Any]:
    err = _require_token()
    if err:
        return err
    return files_upload(
        channels=channels,
        content=content,
        filename=filename,
        filetype=filetype,
        initial_comment=initial_comment,
        thread_ts=thread_ts,
        title=title,
    )


# Search
@mcp.tool()
def slack_search_messages(
    query: str,
    count: Optional[int] = None,
    page: Optional[int] = None,
    cursor: Optional[str] = None,
    highlight: Optional[bool] = None,
    sort: Optional[str] = None,
    sort_dir: Optional[str] = None,
    team_id: Optional[str] = None,
) -> Dict[str, Any]:
    err = _require_token()
    if err:
        return err
    return search_messages(
        query=query,
        count=count,
        page=page,
        cursor=cursor,
        highlight=highlight,
        sort=sort,
        sort_dir=sort_dir,
        team_id=team_id,
    )


@mcp.tool()
def slack_search_files(
    query: str,
    count: Optional[int] = None,
    page: Optional[int] = None,
    highlight: Optional[bool] = None,
    sort: Optional[str] = None,
    sort_dir: Optional[str] = None,
    team_id: Optional[str] = None,
) -> Dict[str, Any]:
    err = _require_token()
    if err:
        return err
    return search_files(
        query=query,
        count=count,
        page=page,
        highlight=highlight,
        sort=sort,
        sort_dir=sort_dir,
        team_id=team_id,
    )


# Pins
@mcp.tool()
def slack_pins_add(channel: str, timestamp: str) -> Dict[str, Any]:
    err = _require_token()
    if err:
        return err
    return pins_add(channel=channel, timestamp=timestamp)


@mcp.tool()
def slack_pins_list(channel: str) -> Dict[str, Any]:
    err = _require_token()
    if err:
        return err
    return pins_list(channel=channel)


@mcp.tool()
def slack_pins_remove(channel: str, timestamp: str) -> Dict[str, Any]:
    err = _require_token()
    if err:
        return err
    return pins_remove(channel=channel, timestamp=timestamp)


# Reminders
@mcp.tool()
def slack_reminders_add(
    text: str,
    time: str,
    team_id: Optional[str] = None,
    recurrence: Optional[Any] = None,
    user: Optional[str] = None,
) -> Dict[str, Any]:
    err = _require_token()
    if err:
        return err
    return reminders_add(text=text, time=time, team_id=team_id, recurrence=recurrence, user=user)


@mcp.tool()
def slack_reminders_list(team_id: Optional[str] = None) -> Dict[str, Any]:
    err = _require_token()
    if err:
        return err
    return reminders_list(team_id=team_id)


@mcp.tool()
def slack_reminders_complete(reminder: str) -> Dict[str, Any]:
    err = _require_token()
    if err:
        return err
    return reminders_complete(reminder=reminder)


@mcp.tool()
def slack_reminders_delete(reminder: str) -> Dict[str, Any]:
    err = _require_token()
    if err:
        return err
    return reminders_delete(reminder=reminder)


# Team
@mcp.tool()
def slack_team_info(team: Optional[str] = None, domain: Optional[str] = None) -> Dict[str, Any]:
    err = _require_token()
    if err:
        return err
    return team_info(team=team, domain=domain)


if __name__ == "__main__":
    mcp.run()
