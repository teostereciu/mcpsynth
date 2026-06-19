from mcp.server.fastmcp import FastMCP

from generated_tools.drafts import create_drafts, delete_draft, edit_draft, get_drafts
from generated_tools.messages import (
    add_reaction,
    check_messages_match_narrow,
    delete_message,
    get_message,
    get_message_history,
    get_messages,
    remove_reaction,
    render_message,
    send_message,
    update_message,
)
from generated_tools.scheduled import (
    create_scheduled_message,
    delete_scheduled_message,
    get_scheduled_messages,
    update_scheduled_message,
)
from generated_tools.server_events import delete_queue, get_events, get_server_settings, register_queue
from generated_tools.streams import (
    get_stream_by_id,
    get_stream_id,
    get_stream_topics,
    get_streams,
    get_subscriptions,
    subscribe,
    unsubscribe,
    update_stream,
)
from generated_tools.users import (
    create_user,
    get_own_user,
    get_presence,
    get_user,
    get_user_by_email,
    get_user_presence,
    get_users,
    update_presence,
    update_status,
    update_user,
)

mcp = FastMCP("zulip")

for fn in [
    send_message,
    get_messages,
    get_message,
    update_message,
    delete_message,
    get_message_history,
    add_reaction,
    remove_reaction,
    render_message,
    check_messages_match_narrow,
    get_scheduled_messages,
    create_scheduled_message,
    update_scheduled_message,
    delete_scheduled_message,
    get_drafts,
    create_drafts,
    edit_draft,
    delete_draft,
    get_subscriptions,
    subscribe,
    unsubscribe,
    get_streams,
    get_stream_by_id,
    get_stream_id,
    update_stream,
    get_stream_topics,
    get_own_user,
    get_user,
    get_user_by_email,
    get_users,
    create_user,
    update_user,
    update_status,
    get_presence,
    get_user_presence,
    update_presence,
    get_server_settings,
    register_queue,
    get_events,
    delete_queue,
]:
    mcp.tool()(fn)


if __name__ == "__main__":
    mcp.run()
