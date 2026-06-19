import json

from mcp.server.fastmcp import FastMCP

from generated_tools.messages import get_messages, send_message


mcp = FastMCP("zulip")


@mcp.tool()
def zulip_send_message(
    type: str,
    to,
    content: str,
    topic: str | None = None,
    queue_id: str | None = None,
    local_id: str | None = None,
    read_by_sender: bool | None = None,
):
    return send_message(
        type=type,
        to=to,
        content=content,
        topic=topic,
        queue_id=queue_id,
        local_id=local_id,
        read_by_sender=read_by_sender,
    )


@mcp.tool()
def zulip_get_messages(
    anchor: str | None = None,
    num_before: int | None = None,
    num_after: int | None = None,
    narrow=None,
    include_anchor: bool | None = None,
    client_gravatar: bool | None = None,
    apply_markdown: bool | None = None,
    message_ids=None,
    allow_empty_topic_name: bool | None = None,
    use_first_unread_anchor: bool | None = None,
    anchor_date: str | None = None,
):
    return get_messages(
        anchor=anchor,
        num_before=num_before,
        num_after=num_after,
        narrow=narrow,
        include_anchor=include_anchor,
        client_gravatar=client_gravatar,
        apply_markdown=apply_markdown,
        message_ids=message_ids,
        allow_empty_topic_name=allow_empty_topic_name,
        use_first_unread_anchor=use_first_unread_anchor,
        anchor_date=anchor_date,
    )


if __name__ == "__main__":
    mcp.run()
