import os
from typing import Any, Dict, List, Optional, Union

from mcp.server.fastmcp import FastMCP

from generated_tools.http_client import ZulipClient
from generated_tools import messages


mcp = FastMCP("zulip")


def _client() -> ZulipClient:
    return ZulipClient(
        site=os.environ.get("ZULIP_SITE"),
        email=os.environ.get("ZULIP_EMAIL"),
        api_key=os.environ.get("ZULIP_API_KEY"),
    )


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
    """Send a channel/direct message."""
    return messages.send_message(
        _client(),
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
    anchor: Optional[Union[int, str]] = None,
    include_anchor: Optional[bool] = None,
    anchor_date: Optional[str] = None,
    num_before: Optional[int] = None,
    num_after: Optional[int] = None,
    filter_spec: Optional[List[Dict[str, Any]]] = None,
    client_gravatar: Optional[bool] = None,
    apply_markdown: Optional[bool] = None,
    message_ids: Optional[List[int]] = None,
    allow_empty_topic_name: Optional[bool] = None,
) -> Dict[str, Any]:
    """Fetch messages matching a narrow/filter_spec."""
    return messages.get_messages(
        _client(),
        anchor=anchor,
        include_anchor=include_anchor,
        anchor_date=anchor_date,
        num_before=num_before,
        num_after=num_after,
        filter_spec=filter_spec,
        client_gravatar=client_gravatar,
        apply_markdown=apply_markdown,
        message_ids=message_ids,
        allow_empty_topic_name=allow_empty_topic_name,
    )


if __name__ == "__main__":
    mcp.run()
