from typing import Any, Dict, List, Optional, Union

from mcp.server.fastmcp import FastMCP

from generated_tools.client import ZulipClient
from generated_tools import messages, reactions, streams, topics, users, scheduled_messages, drafts, files

mcp = FastMCP("zulip")


def _client() -> ZulipClient:
    return ZulipClient()


@mcp.tool()
def send_message(
    type: str,
    to: Union[str, int, List[Union[str, int]]],
    content: str,
    topic: Optional[str] = None,
    queue_id: Optional[str] = None,
    local_id: Optional[str] = None,
    read_by_sender: Optional[bool] = None,
) -> Dict[str, Any]:
    return messages.send_message(_client(), type=type, to=to, content=content, topic=topic, queue_id=queue_id, local_id=local_id, read_by_sender=read_by_sender)


@mcp.tool()
def update_message(
    message_id: int,
    content: Optional[str] = None,
    topic: Optional[str] = None,
    propagate_mode: Optional[str] = None,
    send_notification_to_old_thread: Optional[bool] = None,
    send_notification_to_new_thread: Optional[bool] = None,
    prev_content_sha256: Optional[str] = None,
    stream_id: Optional[int] = None,
) -> Dict[str, Any]:
    return messages.update_message(
        _client(),
        message_id=message_id,
        content=content,
        topic=topic,
        propagate_mode=propagate_mode,
        send_notification_to_old_thread=send_notification_to_old_thread,
        send_notification_to_new_thread=send_notification_to_new_thread,
        prev_content_sha256=prev_content_sha256,
        stream_id=stream_id,
    )


@mcp.tool()
def delete_message(message_id: int) -> Dict[str, Any]:
    return messages.delete_message(_client(), message_id=message_id)


@mcp.tool()
def get_messages(
    anchor: Optional[str] = None,
    num_before: Optional[int] = None,
    num_after: Optional[int] = None,
    narrow: Optional[List[Dict[str, Any]]] = None,
    include_anchor: Optional[bool] = None,
    client_gravatar: Optional[bool] = None,
    apply_markdown: Optional[bool] = None,
    message_ids: Optional[List[int]] = None,
    allow_empty_topic_name: Optional[bool] = None,
    anchor_date: Optional[str] = None,
) -> Dict[str, Any]:
    return messages.get_messages(
        _client(),
        anchor=anchor,
        num_before=num_before,
        num_after=num_after,
        narrow=narrow,
        include_anchor=include_anchor,
        client_gravatar=client_gravatar,
        apply_markdown=apply_markdown,
        message_ids=message_ids,
        allow_empty_topic_name=allow_empty_topic_name,
        anchor_date=anchor_date,
    )


@mcp.tool()
def get_message(message_id: int, apply_markdown: Optional[bool] = None, allow_empty_topic_name: Optional[bool] = None) -> Dict[str, Any]:
    return messages.get_message(_client(), message_id=message_id, apply_markdown=apply_markdown, allow_empty_topic_name=allow_empty_topic_name)


@mcp.tool()
def add_reaction(message_id: int, emoji_name: str, emoji_code: Optional[str] = None, reaction_type: Optional[str] = None) -> Dict[str, Any]:
    return reactions.add_reaction(_client(), message_id=message_id, emoji_name=emoji_name, emoji_code=emoji_code, reaction_type=reaction_type)


@mcp.tool()
def remove_reaction(message_id: int, emoji_name: Optional[str] = None, emoji_code: Optional[str] = None, reaction_type: Optional[str] = None) -> Dict[str, Any]:
    return reactions.remove_reaction(_client(), message_id=message_id, emoji_name=emoji_name, emoji_code=emoji_code, reaction_type=reaction_type)


@mcp.tool()
def get_streams(
    include_public: Optional[bool] = None,
    include_web_public: Optional[bool] = None,
    include_subscribed: Optional[bool] = None,
    exclude_archived: Optional[bool] = None,
    include_all: Optional[bool] = None,
    include_default: Optional[bool] = None,
    include_owner_subscribed: Optional[bool] = None,
    include_can_access_content: Optional[bool] = None,
) -> Dict[str, Any]:
    return streams.get_streams(
        _client(),
        include_public=include_public,
        include_web_public=include_web_public,
        include_subscribed=include_subscribed,
        exclude_archived=exclude_archived,
        include_all=include_all,
        include_default=include_default,
        include_owner_subscribed=include_owner_subscribed,
        include_can_access_content=include_can_access_content,
    )


@mcp.tool()
def subscribe(
    subscriptions: List[Dict[str, Any]],
    principals: Optional[List[Union[str, int]]] = None,
    authorization_errors_fatal: Optional[bool] = None,
    announce: Optional[bool] = None,
    invite_only: Optional[bool] = None,
    is_web_public: Optional[bool] = None,
    is_default_stream: Optional[bool] = None,
    history_public_to_subscribers: Optional[bool] = None,
    message_retention_days: Optional[Union[str, int]] = None,
    topics_policy: Optional[str] = None,
    can_add_subscribers_group: Optional[Union[int, Dict[str, Any]]] = None,
    can_remove_subscribers_group: Optional[Union[int, Dict[str, Any]]] = None,
    can_administer_channel_group: Optional[Union[int, Dict[str, Any]]] = None,
) -> Dict[str, Any]:
    return streams.subscribe(
        _client(),
        subscriptions=subscriptions,
        principals=principals,
        authorization_errors_fatal=authorization_errors_fatal,
        announce=announce,
        invite_only=invite_only,
        is_web_public=is_web_public,
        is_default_stream=is_default_stream,
        history_public_to_subscribers=history_public_to_subscribers,
        message_retention_days=message_retention_days,
        topics_policy=topics_policy,
        can_add_subscribers_group=can_add_subscribers_group,
        can_remove_subscribers_group=can_remove_subscribers_group,
        can_administer_channel_group=can_administer_channel_group,
    )


@mcp.tool()
def unsubscribe(subscriptions: List[str], principals: Optional[List[Union[str, int]]] = None) -> Dict[str, Any]:
    return streams.unsubscribe(_client(), subscriptions=subscriptions, principals=principals)


@mcp.tool()
def update_stream(
    stream_id: int,
    description: Optional[str] = None,
    new_name: Optional[str] = None,
    is_private: Optional[bool] = None,
    is_web_public: Optional[bool] = None,
    history_public_to_subscribers: Optional[bool] = None,
    is_default_stream: Optional[bool] = None,
    message_retention_days: Optional[Union[str, int]] = None,
    is_archived: Optional[bool] = None,
    folder_id: Optional[Union[int, None]] = None,
    topics_policy: Optional[str] = None,
    can_add_subscribers_group: Optional[Dict[str, Any]] = None,
    can_remove_subscribers_group: Optional[Dict[str, Any]] = None,
    can_administer_channel_group: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    return streams.update_stream(
        _client(),
        stream_id=stream_id,
        description=description,
        new_name=new_name,
        is_private=is_private,
        is_web_public=is_web_public,
        history_public_to_subscribers=history_public_to_subscribers,
        is_default_stream=is_default_stream,
        message_retention_days=message_retention_days,
        is_archived=is_archived,
        folder_id=folder_id,
        topics_policy=topics_policy,
        can_add_subscribers_group=can_add_subscribers_group,
        can_remove_subscribers_group=can_remove_subscribers_group,
        can_administer_channel_group=can_administer_channel_group,
    )


@mcp.tool()
def archive_stream(stream_id: int) -> Dict[str, Any]:
    return streams.archive_stream(_client(), stream_id=stream_id)


@mcp.tool()
def get_stream_topics(stream_id: int, allow_empty_topic_name: Optional[bool] = None) -> Dict[str, Any]:
    return topics.get_stream_topics(_client(), stream_id=stream_id, allow_empty_topic_name=allow_empty_topic_name)


@mcp.tool()
def delete_topic(stream_id: int, topic_name: str) -> Dict[str, Any]:
    return topics.delete_topic(_client(), stream_id=stream_id, topic_name=topic_name)


@mcp.tool()
def update_user_topic_visibility(stream_id: int, topic: str, visibility_policy: int) -> Dict[str, Any]:
    return topics.update_user_topic_visibility(_client(), stream_id=stream_id, topic=topic, visibility_policy=visibility_policy)


@mcp.tool()
def mute_topic_legacy(topic: str, op: str, stream: Optional[str] = None, stream_id: Optional[int] = None) -> Dict[str, Any]:
    return topics.mute_topic_legacy(_client(), topic=topic, op=op, stream=stream, stream_id=stream_id)


@mcp.tool()
def get_users(
    client_gravatar: Optional[bool] = None,
    include_custom_profile_fields: Optional[bool] = None,
    user_ids: Optional[List[int]] = None,
) -> Dict[str, Any]:
    return users.get_users(_client(), client_gravatar=client_gravatar, include_custom_profile_fields=include_custom_profile_fields, user_ids=user_ids)


@mcp.tool()
def get_own_user() -> Dict[str, Any]:
    return users.get_own_user(_client())


@mcp.tool()
def get_user_presence(user_id_or_email: str) -> Dict[str, Any]:
    return users.get_user_presence(_client(), user_id_or_email=user_id_or_email)


@mcp.tool()
def get_realm_presence() -> Dict[str, Any]:
    return users.get_realm_presence(_client())


@mcp.tool()
def get_scheduled_messages() -> Dict[str, Any]:
    return scheduled_messages.get_scheduled_messages(_client())


@mcp.tool()
def create_scheduled_message(
    type: str,
    to: Union[int, List[int]],
    content: str,
    scheduled_delivery_timestamp: int,
    topic: Optional[str] = None,
    read_by_sender: Optional[bool] = None,
) -> Dict[str, Any]:
    return scheduled_messages.create_scheduled_message(
        _client(),
        type=type,
        to=to,
        content=content,
        scheduled_delivery_timestamp=scheduled_delivery_timestamp,
        topic=topic,
        read_by_sender=read_by_sender,
    )


@mcp.tool()
def update_scheduled_message(
    scheduled_message_id: int,
    type: Optional[str] = None,
    to: Optional[Union[int, List[int]]] = None,
    content: Optional[str] = None,
    topic: Optional[str] = None,
    scheduled_delivery_timestamp: Optional[int] = None,
) -> Dict[str, Any]:
    return scheduled_messages.update_scheduled_message(
        _client(),
        scheduled_message_id=scheduled_message_id,
        type=type,
        to=to,
        content=content,
        topic=topic,
        scheduled_delivery_timestamp=scheduled_delivery_timestamp,
    )


@mcp.tool()
def delete_scheduled_message(scheduled_message_id: int) -> Dict[str, Any]:
    return scheduled_messages.delete_scheduled_message(_client(), scheduled_message_id=scheduled_message_id)


@mcp.tool()
def get_drafts() -> Dict[str, Any]:
    return drafts.get_drafts(_client())


@mcp.tool()
def create_drafts(drafts_list: List[Dict[str, Any]]) -> Dict[str, Any]:
    return drafts.create_drafts(_client(), drafts=drafts_list)


@mcp.tool()
def edit_draft(draft_id: int, draft_obj: Dict[str, Any]) -> Dict[str, Any]:
    return drafts.edit_draft(_client(), draft_id=draft_id, draft=draft_obj)


@mcp.tool()
def delete_draft(draft_id: int) -> Dict[str, Any]:
    return drafts.delete_draft(_client(), draft_id=draft_id)


@mcp.tool()
def upload_file(file_path: str) -> Dict[str, Any]:
    return files.upload_file(_client(), file_path=file_path)


@mcp.tool()
def get_file_temporary_url(realm_id_str: int, filename: str) -> Dict[str, Any]:
    return files.get_file_temporary_url(_client(), realm_id_str=realm_id_str, filename=filename)


if __name__ == "__main__":
    mcp.run()
