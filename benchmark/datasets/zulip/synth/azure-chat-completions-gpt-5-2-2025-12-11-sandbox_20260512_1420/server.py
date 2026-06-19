from typing import Any, Dict, List, Optional, Union

from mcp.server.fastmcp import FastMCP

from generated_tools import drafts, files, messages, scheduled, streams, users

mcp = FastMCP("zulip")


# Messages
@mcp.tool()
def zulip_send_message(
    type: str,
    to: Union[str, int, List[Union[str, int]]],
    content: str,
    topic: Optional[str] = None,
    queue_id: Optional[str] = None,
    local_id: Optional[str] = None,
    read_by_sender: Optional[bool] = None,
) -> Dict[str, Any]:
    return messages.send_message(type=type, to=to, content=content, topic=topic, queue_id=queue_id, local_id=local_id, read_by_sender=read_by_sender)


@mcp.tool()
def zulip_get_messages(
    anchor: Union[int, str] = "newest",
    num_before: int = 30,
    num_after: int = 0,
    narrow: Optional[List[Dict[str, Any]]] = None,
    client_gravatar: Optional[bool] = None,
    apply_markdown: Optional[bool] = None,
    use_first_unread_anchor: Optional[bool] = None,
) -> Dict[str, Any]:
    return messages.get_messages(
        anchor=anchor,
        num_before=num_before,
        num_after=num_after,
        narrow=narrow,
        client_gravatar=client_gravatar,
        apply_markdown=apply_markdown,
        use_first_unread_anchor=use_first_unread_anchor,
    )


@mcp.tool()
def zulip_get_message(message_id: int) -> Dict[str, Any]:
    return messages.get_message(message_id)


@mcp.tool()
def zulip_update_message(
    message_id: int,
    content: Optional[str] = None,
    topic: Optional[str] = None,
    propagate_mode: Optional[str] = None,
    send_notification_to_old_thread: Optional[bool] = None,
    send_notification_to_new_thread: Optional[bool] = None,
) -> Dict[str, Any]:
    return messages.update_message(
        message_id=message_id,
        content=content,
        topic=topic,
        propagate_mode=propagate_mode,
        send_notification_to_old_thread=send_notification_to_old_thread,
        send_notification_to_new_thread=send_notification_to_new_thread,
    )


@mcp.tool()
def zulip_delete_message(message_id: int) -> Dict[str, Any]:
    return messages.delete_message(message_id)


@mcp.tool()
def zulip_render_message(content: str) -> Dict[str, Any]:
    return messages.render_message(content)


@mcp.tool()
def zulip_add_reaction(
    message_id: int,
    emoji_name: str,
    emoji_code: Optional[str] = None,
    reaction_type: Optional[str] = None,
) -> Dict[str, Any]:
    return messages.add_reaction(message_id=message_id, emoji_name=emoji_name, emoji_code=emoji_code, reaction_type=reaction_type)


@mcp.tool()
def zulip_remove_reaction(
    message_id: int,
    emoji_name: str,
    emoji_code: Optional[str] = None,
    reaction_type: Optional[str] = None,
) -> Dict[str, Any]:
    return messages.remove_reaction(message_id=message_id, emoji_name=emoji_name, emoji_code=emoji_code, reaction_type=reaction_type)


@mcp.tool()
def zulip_update_message_flags(messages_ids: List[int], op: str, flag: str) -> Dict[str, Any]:
    return messages.update_message_flags(messages=messages_ids, op=op, flag=flag)


@mcp.tool()
def zulip_mark_all_as_read() -> Dict[str, Any]:
    return messages.mark_all_as_read()


@mcp.tool()
def zulip_mark_stream_as_read(stream_id: int) -> Dict[str, Any]:
    return messages.mark_stream_as_read(stream_id)


@mcp.tool()
def zulip_mark_topic_as_read(stream_id: int, topic_name: str) -> Dict[str, Any]:
    return messages.mark_topic_as_read(stream_id, topic_name)


# Streams / subscriptions / topics
@mcp.tool()
def zulip_get_streams(include_public: Optional[bool] = None, include_subscribed: Optional[bool] = None) -> Dict[str, Any]:
    return streams.get_streams(include_public=include_public, include_subscribed=include_subscribed)


@mcp.tool()
def zulip_get_stream_id(stream: str) -> Dict[str, Any]:
    return streams.get_stream_id(stream)


@mcp.tool()
def zulip_get_stream_by_id(stream_id: int) -> Dict[str, Any]:
    return streams.get_stream_by_id(stream_id)


@mcp.tool()
def zulip_create_stream(name: str, description: Optional[str] = None, invite_only: Optional[bool] = None, is_web_public: Optional[bool] = None) -> Dict[str, Any]:
    return streams.create_stream(name=name, description=description, invite_only=invite_only, is_web_public=is_web_public)


@mcp.tool()
def zulip_update_stream(stream_id: int, new_name: Optional[str] = None, description: Optional[str] = None, is_private: Optional[bool] = None) -> Dict[str, Any]:
    return streams.update_stream(stream_id=stream_id, new_name=new_name, description=description, is_private=is_private)


@mcp.tool()
def zulip_archive_stream(stream_id: int) -> Dict[str, Any]:
    return streams.archive_stream(stream_id)


@mcp.tool()
def zulip_get_subscriptions(include_subscribers: Optional[bool] = None) -> Dict[str, Any]:
    return streams.get_subscriptions(include_subscribers=include_subscribers)


@mcp.tool()
def zulip_subscribe(
    subscriptions: List[Dict[str, Any]],
    principals: Optional[List[Union[int, str]]] = None,
    authorization_errors_fatal: Optional[bool] = None,
    invite_only: Optional[bool] = None,
    announce: Optional[bool] = None,
    is_web_public: Optional[bool] = None,
) -> Dict[str, Any]:
    return streams.subscribe(
        subscriptions=subscriptions,
        principals=principals,
        authorization_errors_fatal=authorization_errors_fatal,
        invite_only=invite_only,
        announce=announce,
        is_web_public=is_web_public,
    )


@mcp.tool()
def zulip_unsubscribe(subscriptions: List[str], principals: Optional[List[Union[int, str]]] = None) -> Dict[str, Any]:
    return streams.unsubscribe(subscriptions=subscriptions, principals=principals)


@mcp.tool()
def zulip_get_subscribers(stream_id: int) -> Dict[str, Any]:
    return streams.get_subscribers(stream_id)


@mcp.tool()
def zulip_get_stream_topics(stream_id: int) -> Dict[str, Any]:
    return streams.get_stream_topics(stream_id)


@mcp.tool()
def zulip_delete_topic(stream_id: int, topic_name: str) -> Dict[str, Any]:
    return streams.delete_topic(stream_id, topic_name)


# Users
@mcp.tool()
def zulip_get_own_user() -> Dict[str, Any]:
    return users.get_own_user()


@mcp.tool()
def zulip_get_user(user_id: int, client_gravatar: Optional[bool] = None) -> Dict[str, Any]:
    return users.get_user(user_id=user_id, client_gravatar=client_gravatar)


@mcp.tool()
def zulip_get_user_by_email(email: str) -> Dict[str, Any]:
    return users.get_user_by_email(email)


@mcp.tool()
def zulip_get_users(client_gravatar: Optional[bool] = None, include_custom_profile_fields: Optional[bool] = None) -> Dict[str, Any]:
    return users.get_users(client_gravatar=client_gravatar, include_custom_profile_fields=include_custom_profile_fields)


@mcp.tool()
def zulip_update_status(text: Optional[str] = None, emoji_name: Optional[str] = None, emoji_code: Optional[str] = None, reaction_type: Optional[str] = None) -> Dict[str, Any]:
    return users.update_status(text=text, emoji_name=emoji_name, emoji_code=emoji_code, reaction_type=reaction_type)


@mcp.tool()
def zulip_get_user_presence(user_id_or_email: Union[int, str]) -> Dict[str, Any]:
    return users.get_user_presence(user_id_or_email)


@mcp.tool()
def zulip_get_presence() -> Dict[str, Any]:
    return users.get_presence()


@mcp.tool()
def zulip_update_presence(status: str, ping_only: Optional[bool] = None, new_user_input: Optional[bool] = None) -> Dict[str, Any]:
    return users.update_presence(status=status, ping_only=ping_only, new_user_input=new_user_input)


@mcp.tool()
def zulip_mute_user(user_id: int) -> Dict[str, Any]:
    return users.mute_user(user_id)


@mcp.tool()
def zulip_unmute_user(user_id: int) -> Dict[str, Any]:
    return users.unmute_user(user_id)


@mcp.tool()
def zulip_get_alert_words() -> Dict[str, Any]:
    return users.get_alert_words()


@mcp.tool()
def zulip_add_alert_words(words: List[str]) -> Dict[str, Any]:
    return users.add_alert_words(words)


@mcp.tool()
def zulip_remove_alert_words(words: List[str]) -> Dict[str, Any]:
    return users.remove_alert_words(words)


# Scheduled messages
@mcp.tool()
def zulip_get_scheduled_messages() -> Dict[str, Any]:
    return scheduled.get_scheduled_messages()


@mcp.tool()
def zulip_create_scheduled_message(
    type: str,
    to: Union[int, List[int]],
    content: str,
    scheduled_delivery_timestamp: int,
    topic: Optional[str] = None,
    read_by_sender: Optional[bool] = None,
) -> Dict[str, Any]:
    return scheduled.create_scheduled_message(
        type=type,
        to=to,
        content=content,
        scheduled_delivery_timestamp=scheduled_delivery_timestamp,
        topic=topic,
        read_by_sender=read_by_sender,
    )


@mcp.tool()
def zulip_update_scheduled_message(
    scheduled_message_id: int,
    content: Optional[str] = None,
    topic: Optional[str] = None,
    scheduled_delivery_timestamp: Optional[int] = None,
) -> Dict[str, Any]:
    return scheduled.update_scheduled_message(
        scheduled_message_id=scheduled_message_id,
        content=content,
        topic=topic,
        scheduled_delivery_timestamp=scheduled_delivery_timestamp,
    )


@mcp.tool()
def zulip_delete_scheduled_message(scheduled_message_id: int) -> Dict[str, Any]:
    return scheduled.delete_scheduled_message(scheduled_message_id)


# Drafts
@mcp.tool()
def zulip_get_drafts() -> Dict[str, Any]:
    return drafts.get_drafts()


@mcp.tool()
def zulip_create_drafts(drafts_list: List[Dict[str, Any]]) -> Dict[str, Any]:
    return drafts.create_drafts(drafts_list)


@mcp.tool()
def zulip_edit_draft(draft_id: int, draft: Dict[str, Any]) -> Dict[str, Any]:
    return drafts.edit_draft(draft_id, draft)


@mcp.tool()
def zulip_delete_draft(draft_id: int) -> Dict[str, Any]:
    return drafts.delete_draft(draft_id)


# Files
@mcp.tool()
def zulip_upload_file(path: str) -> Dict[str, Any]:
    return files.upload_file(path)


@mcp.tool()
def zulip_get_file_temporary_url(realm_id_str: str, filename: str) -> Dict[str, Any]:
    return files.get_file_temporary_url(realm_id_str, filename)


if __name__ == "__main__":
    mcp.run()
