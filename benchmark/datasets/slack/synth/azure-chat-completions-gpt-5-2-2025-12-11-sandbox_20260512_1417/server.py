from mcp.server.fastmcp import FastMCP

from generated_tools.chat import chat_delete, chat_post_message, chat_update
from generated_tools.conversations import (
    conversations_history,
    conversations_list,
    conversations_members,
    conversations_replies,
)
from generated_tools.files import (
    files_complete_upload_external,
    files_get_upload_url_external,
    files_list,
)
from generated_tools.pins import pins_add, pins_remove
from generated_tools.reactions import reactions_add, reactions_remove
from generated_tools.reminders import reminders_add, reminders_list
from generated_tools.search import search_files, search_messages
from generated_tools.team import auth_test, team_info
from generated_tools.users import (
    users_get_presence,
    users_info,
    users_list,
    users_lookup_by_email,
)


mcp = FastMCP("slack-web-api")


# Chat / Messages
@mcp.tool()
def slack_chat_post_message(**kwargs):
    return chat_post_message(**kwargs)


@mcp.tool()
def slack_chat_update(**kwargs):
    return chat_update(**kwargs)


@mcp.tool()
def slack_chat_delete(**kwargs):
    return chat_delete(**kwargs)


# Conversations
@mcp.tool()
def slack_conversations_list(**kwargs):
    return conversations_list(**kwargs)


@mcp.tool()
def slack_conversations_history(**kwargs):
    return conversations_history(**kwargs)


@mcp.tool()
def slack_conversations_replies(**kwargs):
    return conversations_replies(**kwargs)


@mcp.tool()
def slack_conversations_members(**kwargs):
    return conversations_members(**kwargs)


# Users
@mcp.tool()
def slack_users_list(**kwargs):
    return users_list(**kwargs)


@mcp.tool()
def slack_users_info(**kwargs):
    return users_info(**kwargs)


@mcp.tool()
def slack_users_lookup_by_email(**kwargs):
    return users_lookup_by_email(**kwargs)


@mcp.tool()
def slack_users_get_presence(**kwargs):
    return users_get_presence(**kwargs)


# Reactions
@mcp.tool()
def slack_reactions_add(**kwargs):
    return reactions_add(**kwargs)


@mcp.tool()
def slack_reactions_remove(**kwargs):
    return reactions_remove(**kwargs)


# Files
@mcp.tool()
def slack_files_list(**kwargs):
    return files_list(**kwargs)


@mcp.tool()
def slack_files_get_upload_url_external(**kwargs):
    return files_get_upload_url_external(**kwargs)


@mcp.tool()
def slack_files_complete_upload_external(**kwargs):
    return files_complete_upload_external(**kwargs)


# Search
@mcp.tool()
def slack_search_messages(**kwargs):
    return search_messages(**kwargs)


@mcp.tool()
def slack_search_files(**kwargs):
    return search_files(**kwargs)


# Pins
@mcp.tool()
def slack_pins_add(**kwargs):
    return pins_add(**kwargs)


@mcp.tool()
def slack_pins_remove(**kwargs):
    return pins_remove(**kwargs)


# Reminders
@mcp.tool()
def slack_reminders_add(**kwargs):
    return reminders_add(**kwargs)


@mcp.tool()
def slack_reminders_list(**kwargs):
    return reminders_list(**kwargs)


# Team/Auth
@mcp.tool()
def slack_team_info(**kwargs):
    return team_info(**kwargs)


@mcp.tool()
def slack_auth_test():
    return auth_test()


if __name__ == "__main__":
    mcp.run()
