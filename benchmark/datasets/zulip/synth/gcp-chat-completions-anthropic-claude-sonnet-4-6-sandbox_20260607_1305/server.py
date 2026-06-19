"""Zulip MCP Server — exposes Zulip REST API as MCP tools over stdio."""
from mcp.server.fastmcp import FastMCP

# Import all tool modules
from generated_tools.messages import (
    send_message,
    get_messages,
    get_message,
    update_message,
    delete_message,
    add_reaction,
    remove_reaction,
    update_message_flags,
    get_message_history,
    mark_all_as_read,
    mark_stream_as_read,
    mark_topic_as_read,
    render_message,
    get_read_receipts,
    upload_file,
)
from generated_tools.streams import (
    get_streams,
    get_subscriptions,
    subscribe_to_stream,
    unsubscribe_from_stream,
    get_stream_by_id,
    get_stream_id,
    update_stream,
    archive_stream,
    get_stream_topics,
    delete_topic,
    get_subscribers,
    get_subscription_status,
    mute_topic,
    update_user_topic,
    get_stream_email_address,
    add_default_stream,
    remove_default_stream,
    get_user_channels,
)
from generated_tools.users import (
    get_users,
    get_user,
    get_user_by_email,
    get_own_user,
    create_user,
    update_user,
    deactivate_user,
    reactivate_user,
    deactivate_own_user,
    get_user_presence,
    get_presence,
    update_presence,
    get_user_status,
    update_status,
    mute_user,
    unmute_user,
    get_attachments,
    remove_attachment,
    get_alert_words,
    add_alert_words,
    remove_alert_words,
    set_typing_status,
)
from generated_tools.scheduled_messages import (
    get_scheduled_messages,
    create_scheduled_message,
    update_scheduled_message,
    delete_scheduled_message,
    get_reminders,
    create_message_reminder,
    delete_reminder,
    get_drafts,
    create_drafts,
    edit_draft,
    delete_draft,
    get_saved_snippets,
    create_saved_snippet,
    edit_saved_snippet,
    delete_saved_snippet,
)
from generated_tools.user_groups import (
    get_user_groups,
    create_user_group,
    update_user_group,
    deactivate_user_group,
    update_user_group_members,
    get_user_group_members,
    get_is_user_group_member,
    update_user_group_subgroups,
    get_user_group_subgroups,
)
from generated_tools.server import (
    get_server_settings,
    get_linkifiers,
    add_linkifier,
    update_linkifier,
    remove_linkifier,
    reorder_linkifiers,
    get_custom_emoji,
    upload_custom_emoji,
    deactivate_custom_emoji,
    get_custom_profile_fields,
    create_custom_profile_field,
    reorder_custom_profile_fields,
    add_code_playground,
    remove_code_playground,
    get_realm_exports,
    export_realm,
    get_realm_export_consents,
    register_event_queue,
    get_events,
    delete_event_queue,
)
from generated_tools.invitations import (
    get_invites,
    send_invites,
    create_invite_link,
    resend_email_invite,
    revoke_email_invite,
    revoke_invite_link,
)

mcp = FastMCP("zulip")

# ── Messages ─────────────────────────────────────────────────────────────────
mcp.tool()(send_message)
mcp.tool()(get_messages)
mcp.tool()(get_message)
mcp.tool()(update_message)
mcp.tool()(delete_message)
mcp.tool()(add_reaction)
mcp.tool()(remove_reaction)
mcp.tool()(update_message_flags)
mcp.tool()(get_message_history)
mcp.tool()(mark_all_as_read)
mcp.tool()(mark_stream_as_read)
mcp.tool()(mark_topic_as_read)
mcp.tool()(render_message)
mcp.tool()(get_read_receipts)
mcp.tool()(upload_file)

# ── Streams / Channels ────────────────────────────────────────────────────────
mcp.tool()(get_streams)
mcp.tool()(get_subscriptions)
mcp.tool()(subscribe_to_stream)
mcp.tool()(unsubscribe_from_stream)
mcp.tool()(get_stream_by_id)
mcp.tool()(get_stream_id)
mcp.tool()(update_stream)
mcp.tool()(archive_stream)
mcp.tool()(get_stream_topics)
mcp.tool()(delete_topic)
mcp.tool()(get_subscribers)
mcp.tool()(get_subscription_status)
mcp.tool()(mute_topic)
mcp.tool()(update_user_topic)
mcp.tool()(get_stream_email_address)
mcp.tool()(add_default_stream)
mcp.tool()(remove_default_stream)
mcp.tool()(get_user_channels)

# ── Users ─────────────────────────────────────────────────────────────────────
mcp.tool()(get_users)
mcp.tool()(get_user)
mcp.tool()(get_user_by_email)
mcp.tool()(get_own_user)
mcp.tool()(create_user)
mcp.tool()(update_user)
mcp.tool()(deactivate_user)
mcp.tool()(reactivate_user)
mcp.tool()(deactivate_own_user)
mcp.tool()(get_user_presence)
mcp.tool()(get_presence)
mcp.tool()(update_presence)
mcp.tool()(get_user_status)
mcp.tool()(update_status)
mcp.tool()(mute_user)
mcp.tool()(unmute_user)
mcp.tool()(get_attachments)
mcp.tool()(remove_attachment)
mcp.tool()(get_alert_words)
mcp.tool()(add_alert_words)
mcp.tool()(remove_alert_words)
mcp.tool()(set_typing_status)

# ── Scheduled Messages ────────────────────────────────────────────────────────
mcp.tool()(get_scheduled_messages)
mcp.tool()(create_scheduled_message)
mcp.tool()(update_scheduled_message)
mcp.tool()(delete_scheduled_message)

# ── Message Reminders ─────────────────────────────────────────────────────────
mcp.tool()(get_reminders)
mcp.tool()(create_message_reminder)
mcp.tool()(delete_reminder)

# ── Drafts ────────────────────────────────────────────────────────────────────
mcp.tool()(get_drafts)
mcp.tool()(create_drafts)
mcp.tool()(edit_draft)
mcp.tool()(delete_draft)

# ── Saved Snippets ────────────────────────────────────────────────────────────
mcp.tool()(get_saved_snippets)
mcp.tool()(create_saved_snippet)
mcp.tool()(edit_saved_snippet)
mcp.tool()(delete_saved_snippet)

# ── User Groups ───────────────────────────────────────────────────────────────
mcp.tool()(get_user_groups)
mcp.tool()(create_user_group)
mcp.tool()(update_user_group)
mcp.tool()(deactivate_user_group)
mcp.tool()(update_user_group_members)
mcp.tool()(get_user_group_members)
mcp.tool()(get_is_user_group_member)
mcp.tool()(update_user_group_subgroups)
mcp.tool()(get_user_group_subgroups)

# ── Server & Organization ─────────────────────────────────────────────────────
mcp.tool()(get_server_settings)
mcp.tool()(get_linkifiers)
mcp.tool()(add_linkifier)
mcp.tool()(update_linkifier)
mcp.tool()(remove_linkifier)
mcp.tool()(reorder_linkifiers)
mcp.tool()(get_custom_emoji)
mcp.tool()(upload_custom_emoji)
mcp.tool()(deactivate_custom_emoji)
mcp.tool()(get_custom_profile_fields)
mcp.tool()(create_custom_profile_field)
mcp.tool()(reorder_custom_profile_fields)
mcp.tool()(add_code_playground)
mcp.tool()(remove_code_playground)
mcp.tool()(get_realm_exports)
mcp.tool()(export_realm)
mcp.tool()(get_realm_export_consents)
mcp.tool()(register_event_queue)
mcp.tool()(get_events)
mcp.tool()(delete_event_queue)

# ── Invitations ───────────────────────────────────────────────────────────────
mcp.tool()(get_invites)
mcp.tool()(send_invites)
mcp.tool()(create_invite_link)
mcp.tool()(resend_email_invite)
mcp.tool()(revoke_email_invite)
mcp.tool()(revoke_invite_link)


if __name__ == "__main__":
    mcp.run(transport="stdio")
