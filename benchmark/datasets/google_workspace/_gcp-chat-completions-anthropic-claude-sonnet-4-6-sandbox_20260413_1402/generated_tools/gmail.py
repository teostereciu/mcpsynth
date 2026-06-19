"""Gmail API tools for the Google Workspace MCP Server."""

import base64
from typing import Any, Optional

import requests

from generated_tools import mcp
from generated_tools.auth import (
    GMAIL_BASE,
    api_delete,
    api_get,
    api_post,
    api_put,
    handle_http_error,
    _auth_headers,
)


# ---------------------------------------------------------------------------
# Profile
# ---------------------------------------------------------------------------


@mcp.tool()
def gmail_get_profile(user_id: str = "me") -> dict:
    """Get the Gmail profile for the authenticated user.

    Returns emailAddress, messagesTotal, threadsTotal, and historyId.

    Args:
        user_id: The user's email address or 'me' for the authenticated user.
    """
    try:
        return api_get(f"{GMAIL_BASE}/{user_id}/profile")
    except requests.HTTPError as e:
        return handle_http_error(e)


# ---------------------------------------------------------------------------
# Messages
# ---------------------------------------------------------------------------


@mcp.tool()
def gmail_list_messages(
    user_id: str = "me",
    max_results: int = 100,
    label_ids: Optional[list] = None,
    q: Optional[str] = None,
    page_token: Optional[str] = None,
    include_spam_trash: bool = False,
) -> dict:
    """List messages in the user's Gmail mailbox.

    Args:
        user_id: The user's email address or 'me'.
        max_results: Maximum number of messages to return (default 100, max 500).
        label_ids: Only return messages with these label IDs (e.g. ['INBOX']).
        q: Gmail search query string (e.g. 'from:someone@example.com is:unread').
        page_token: Page token for pagination.
        include_spam_trash: Include messages from SPAM and TRASH.
    """
    try:
        params: dict[str, Any] = {
            "maxResults": max_results,
            "includeSpamTrash": include_spam_trash,
        }
        if label_ids:
            params["labelIds"] = label_ids
        if q:
            params["q"] = q
        if page_token:
            params["pageToken"] = page_token
        return api_get(f"{GMAIL_BASE}/{user_id}/messages", params=params)
    except requests.HTTPError as e:
        return handle_http_error(e)


@mcp.tool()
def gmail_get_message(
    message_id: str,
    user_id: str = "me",
    format: str = "full",
    metadata_headers: Optional[list] = None,
) -> dict:
    """Get a specific Gmail message by ID.

    Args:
        message_id: The ID of the message to retrieve.
        user_id: The user's email address or 'me'.
        format: The format to return the message in: 'full', 'metadata', 'minimal', or 'raw'.
        metadata_headers: When format is 'metadata', only include these headers.
    """
    try:
        params: dict[str, Any] = {"format": format}
        if metadata_headers:
            params["metadataHeaders"] = metadata_headers
        return api_get(f"{GMAIL_BASE}/{user_id}/messages/{message_id}", params=params)
    except requests.HTTPError as e:
        return handle_http_error(e)


@mcp.tool()
def gmail_send_message(
    to: str,
    subject: str,
    body: str,
    user_id: str = "me",
    cc: Optional[str] = None,
    bcc: Optional[str] = None,
) -> dict:
    """Send an email message via Gmail.

    Args:
        to: Recipient email address.
        subject: Email subject line.
        body: Plain-text email body.
        user_id: The user's email address or 'me'.
        cc: CC email address(es).
        bcc: BCC email address(es).
    """
    try:
        headers = f"To: {to}\r\nSubject: {subject}\r\n"
        if cc:
            headers += f"Cc: {cc}\r\n"
        if bcc:
            headers += f"Bcc: {bcc}\r\n"
        headers += "Content-Type: text/plain; charset=utf-8\r\n"
        raw_message = headers + "\r\n" + body
        encoded = base64.urlsafe_b64encode(raw_message.encode("utf-8")).decode("utf-8")
        return api_post(
            f"{GMAIL_BASE}/{user_id}/messages/send",
            payload={"raw": encoded},
        )
    except requests.HTTPError as e:
        return handle_http_error(e)


@mcp.tool()
def gmail_modify_message(
    message_id: str,
    add_label_ids: Optional[list] = None,
    remove_label_ids: Optional[list] = None,
    user_id: str = "me",
) -> dict:
    """Modify labels on a Gmail message.

    Args:
        message_id: The ID of the message to modify.
        add_label_ids: List of label IDs to add to the message.
        remove_label_ids: List of label IDs to remove from the message.
        user_id: The user's email address or 'me'.
    """
    try:
        payload: dict[str, Any] = {
            "addLabelIds": add_label_ids or [],
            "removeLabelIds": remove_label_ids or [],
        }
        return api_post(
            f"{GMAIL_BASE}/{user_id}/messages/{message_id}/modify",
            payload=payload,
        )
    except requests.HTTPError as e:
        return handle_http_error(e)


@mcp.tool()
def gmail_trash_message(message_id: str, user_id: str = "me") -> dict:
    """Move a Gmail message to the trash.

    Args:
        message_id: The ID of the message to trash.
        user_id: The user's email address or 'me'.
    """
    try:
        return api_post(f"{GMAIL_BASE}/{user_id}/messages/{message_id}/trash")
    except requests.HTTPError as e:
        return handle_http_error(e)


@mcp.tool()
def gmail_untrash_message(message_id: str, user_id: str = "me") -> dict:
    """Remove a Gmail message from the trash.

    Args:
        message_id: The ID of the message to untrash.
        user_id: The user's email address or 'me'.
    """
    try:
        return api_post(f"{GMAIL_BASE}/{user_id}/messages/{message_id}/untrash")
    except requests.HTTPError as e:
        return handle_http_error(e)


@mcp.tool()
def gmail_delete_message(message_id: str, user_id: str = "me") -> dict:
    """Permanently delete a Gmail message.

    Args:
        message_id: The ID of the message to delete.
        user_id: The user's email address or 'me'.
    """
    try:
        return api_delete(f"{GMAIL_BASE}/{user_id}/messages/{message_id}")
    except requests.HTTPError as e:
        return handle_http_error(e)


@mcp.tool()
def gmail_batch_delete_messages(ids: list, user_id: str = "me") -> dict:
    """Delete multiple Gmail messages by ID.

    Args:
        ids: List of message IDs to delete.
        user_id: The user's email address or 'me'.
    """
    try:
        resp = requests.post(
            f"{GMAIL_BASE}/{user_id}/messages/batchDelete",
            headers=_auth_headers(),
            json={"ids": ids},
        )
        resp.raise_for_status()
        return {"status": "deleted", "count": len(ids)}
    except requests.HTTPError as e:
        return handle_http_error(e)


@mcp.tool()
def gmail_batch_modify_messages(
    ids: list,
    add_label_ids: Optional[list] = None,
    remove_label_ids: Optional[list] = None,
    user_id: str = "me",
) -> dict:
    """Modify labels on multiple Gmail messages.

    Args:
        ids: List of message IDs to modify (max 1000).
        add_label_ids: Label IDs to add to all messages.
        remove_label_ids: Label IDs to remove from all messages.
        user_id: The user's email address or 'me'.
    """
    try:
        resp = requests.post(
            f"{GMAIL_BASE}/{user_id}/messages/batchModify",
            headers=_auth_headers(),
            json={
                "ids": ids,
                "addLabelIds": add_label_ids or [],
                "removeLabelIds": remove_label_ids or [],
            },
        )
        resp.raise_for_status()
        return {"status": "modified", "count": len(ids)}
    except requests.HTTPError as e:
        return handle_http_error(e)


@mcp.tool()
def gmail_get_attachment(
    message_id: str,
    attachment_id: str,
    user_id: str = "me",
) -> dict:
    """Get a Gmail message attachment.

    Args:
        message_id: The ID of the message containing the attachment.
        attachment_id: The ID of the attachment.
        user_id: The user's email address or 'me'.
    """
    try:
        return api_get(
            f"{GMAIL_BASE}/{user_id}/messages/{message_id}/attachments/{attachment_id}"
        )
    except requests.HTTPError as e:
        return handle_http_error(e)


# ---------------------------------------------------------------------------
# Labels
# ---------------------------------------------------------------------------


@mcp.tool()
def gmail_list_labels(user_id: str = "me") -> dict:
    """List all labels in the user's Gmail mailbox.

    Args:
        user_id: The user's email address or 'me'.
    """
    try:
        return api_get(f"{GMAIL_BASE}/{user_id}/labels")
    except requests.HTTPError as e:
        return handle_http_error(e)


@mcp.tool()
def gmail_get_label(label_id: str, user_id: str = "me") -> dict:
    """Get a specific Gmail label by ID.

    Args:
        label_id: The ID of the label to retrieve.
        user_id: The user's email address or 'me'.
    """
    try:
        return api_get(f"{GMAIL_BASE}/{user_id}/labels/{label_id}")
    except requests.HTTPError as e:
        return handle_http_error(e)


@mcp.tool()
def gmail_create_label(
    name: str,
    user_id: str = "me",
    message_list_visibility: str = "show",
    label_list_visibility: str = "labelShow",
) -> dict:
    """Create a new Gmail label.

    Args:
        name: The display name of the label.
        user_id: The user's email address or 'me'.
        message_list_visibility: Visibility in message list: 'show' or 'hide'.
        label_list_visibility: Visibility in label list: 'labelShow', 'labelShowIfUnread', or 'labelHide'.
    """
    try:
        return api_post(
            f"{GMAIL_BASE}/{user_id}/labels",
            payload={
                "name": name,
                "messageListVisibility": message_list_visibility,
                "labelListVisibility": label_list_visibility,
            },
        )
    except requests.HTTPError as e:
        return handle_http_error(e)


@mcp.tool()
def gmail_update_label(
    label_id: str,
    name: Optional[str] = None,
    user_id: str = "me",
    message_list_visibility: Optional[str] = None,
    label_list_visibility: Optional[str] = None,
) -> dict:
    """Update an existing Gmail label.

    Args:
        label_id: The ID of the label to update.
        name: New display name for the label.
        user_id: The user's email address or 'me'.
        message_list_visibility: Visibility in message list: 'show' or 'hide'.
        label_list_visibility: Visibility in label list: 'labelShow', 'labelShowIfUnread', or 'labelHide'.
    """
    try:
        payload: dict[str, Any] = {"id": label_id}
        if name is not None:
            payload["name"] = name
        if message_list_visibility is not None:
            payload["messageListVisibility"] = message_list_visibility
        if label_list_visibility is not None:
            payload["labelListVisibility"] = label_list_visibility
        return api_put(f"{GMAIL_BASE}/{user_id}/labels/{label_id}", payload=payload)
    except requests.HTTPError as e:
        return handle_http_error(e)


@mcp.tool()
def gmail_delete_label(label_id: str, user_id: str = "me") -> dict:
    """Delete a Gmail label.

    Args:
        label_id: The ID of the label to delete.
        user_id: The user's email address or 'me'.
    """
    try:
        return api_delete(f"{GMAIL_BASE}/{user_id}/labels/{label_id}")
    except requests.HTTPError as e:
        return handle_http_error(e)


# ---------------------------------------------------------------------------
# Drafts
# ---------------------------------------------------------------------------


@mcp.tool()
def gmail_list_drafts(
    user_id: str = "me",
    max_results: int = 100,
    q: Optional[str] = None,
    page_token: Optional[str] = None,
    include_spam_trash: bool = False,
) -> dict:
    """List drafts in the user's Gmail mailbox.

    Args:
        user_id: The user's email address or 'me'.
        max_results: Maximum number of drafts to return (default 100, max 500).
        q: Search query to filter drafts.
        page_token: Page token for pagination.
        include_spam_trash: Include drafts from SPAM and TRASH.
    """
    try:
        params: dict[str, Any] = {
            "maxResults": max_results,
            "includeSpamTrash": include_spam_trash,
        }
        if q:
            params["q"] = q
        if page_token:
            params["pageToken"] = page_token
        return api_get(f"{GMAIL_BASE}/{user_id}/drafts", params=params)
    except requests.HTTPError as e:
        return handle_http_error(e)


@mcp.tool()
def gmail_get_draft(draft_id: str, user_id: str = "me", format: str = "full") -> dict:
    """Get a specific Gmail draft by ID.

    Args:
        draft_id: The ID of the draft to retrieve.
        user_id: The user's email address or 'me'.
        format: The format to return the draft in: 'full', 'metadata', 'minimal', or 'raw'.
    """
    try:
        return api_get(
            f"{GMAIL_BASE}/{user_id}/drafts/{draft_id}",
            params={"format": format},
        )
    except requests.HTTPError as e:
        return handle_http_error(e)


@mcp.tool()
def gmail_create_draft(
    to: str,
    subject: str,
    body: str,
    user_id: str = "me",
    cc: Optional[str] = None,
    bcc: Optional[str] = None,
) -> dict:
    """Create a new Gmail draft.

    Args:
        to: Recipient email address.
        subject: Email subject line.
        body: Plain-text email body.
        user_id: The user's email address or 'me'.
        cc: CC email address(es).
        bcc: BCC email address(es).
    """
    try:
        headers = f"To: {to}\r\nSubject: {subject}\r\n"
        if cc:
            headers += f"Cc: {cc}\r\n"
        if bcc:
            headers += f"Bcc: {bcc}\r\n"
        headers += "Content-Type: text/plain; charset=utf-8\r\n"
        raw_message = headers + "\r\n" + body
        encoded = base64.urlsafe_b64encode(raw_message.encode("utf-8")).decode("utf-8")
        return api_post(
            f"{GMAIL_BASE}/{user_id}/drafts",
            payload={"message": {"raw": encoded}},
        )
    except requests.HTTPError as e:
        return handle_http_error(e)


@mcp.tool()
def gmail_update_draft(
    draft_id: str,
    to: str,
    subject: str,
    body: str,
    user_id: str = "me",
) -> dict:
    """Update an existing Gmail draft.

    Args:
        draft_id: The ID of the draft to update.
        to: Recipient email address.
        subject: Email subject line.
        body: Plain-text email body.
        user_id: The user's email address or 'me'.
    """
    try:
        raw_message = f"To: {to}\r\nSubject: {subject}\r\nContent-Type: text/plain; charset=utf-8\r\n\r\n{body}"
        encoded = base64.urlsafe_b64encode(raw_message.encode("utf-8")).decode("utf-8")
        return api_put(
            f"{GMAIL_BASE}/{user_id}/drafts/{draft_id}",
            payload={"message": {"raw": encoded}},
        )
    except requests.HTTPError as e:
        return handle_http_error(e)


@mcp.tool()
def gmail_send_draft(draft_id: str, user_id: str = "me") -> dict:
    """Send an existing Gmail draft.

    Args:
        draft_id: The ID of the draft to send.
        user_id: The user's email address or 'me'.
    """
    try:
        return api_post(
            f"{GMAIL_BASE}/{user_id}/drafts/send",
            payload={"id": draft_id},
        )
    except requests.HTTPError as e:
        return handle_http_error(e)


@mcp.tool()
def gmail_delete_draft(draft_id: str, user_id: str = "me") -> dict:
    """Delete a Gmail draft.

    Args:
        draft_id: The ID of the draft to delete.
        user_id: The user's email address or 'me'.
    """
    try:
        return api_delete(f"{GMAIL_BASE}/{user_id}/drafts/{draft_id}")
    except requests.HTTPError as e:
        return handle_http_error(e)


# ---------------------------------------------------------------------------
# Threads
# ---------------------------------------------------------------------------


@mcp.tool()
def gmail_list_threads(
    user_id: str = "me",
    max_results: int = 100,
    label_ids: Optional[list] = None,
    q: Optional[str] = None,
    page_token: Optional[str] = None,
    include_spam_trash: bool = False,
) -> dict:
    """List threads in the user's Gmail mailbox.

    Args:
        user_id: The user's email address or 'me'.
        max_results: Maximum number of threads to return (default 100, max 500).
        label_ids: Only return threads with these label IDs.
        q: Gmail search query string.
        page_token: Page token for pagination.
        include_spam_trash: Include threads from SPAM and TRASH.
    """
    try:
        params: dict[str, Any] = {
            "maxResults": max_results,
            "includeSpamTrash": include_spam_trash,
        }
        if label_ids:
            params["labelIds"] = label_ids
        if q:
            params["q"] = q
        if page_token:
            params["pageToken"] = page_token
        return api_get(f"{GMAIL_BASE}/{user_id}/threads", params=params)
    except requests.HTTPError as e:
        return handle_http_error(e)


@mcp.tool()
def gmail_get_thread(
    thread_id: str,
    user_id: str = "me",
    format: str = "full",
) -> dict:
    """Get a specific Gmail thread by ID.

    Args:
        thread_id: The ID of the thread to retrieve.
        user_id: The user's email address or 'me'.
        format: The format to return messages in: 'full', 'metadata', 'minimal'.
    """
    try:
        return api_get(
            f"{GMAIL_BASE}/{user_id}/threads/{thread_id}",
            params={"format": format},
        )
    except requests.HTTPError as e:
        return handle_http_error(e)


@mcp.tool()
def gmail_modify_thread(
    thread_id: str,
    add_label_ids: Optional[list] = None,
    remove_label_ids: Optional[list] = None,
    user_id: str = "me",
) -> dict:
    """Modify labels on a Gmail thread.

    Args:
        thread_id: The ID of the thread to modify.
        add_label_ids: Label IDs to add to the thread.
        remove_label_ids: Label IDs to remove from the thread.
        user_id: The user's email address or 'me'.
    """
    try:
        return api_post(
            f"{GMAIL_BASE}/{user_id}/threads/{thread_id}/modify",
            payload={
                "addLabelIds": add_label_ids or [],
                "removeLabelIds": remove_label_ids or [],
            },
        )
    except requests.HTTPError as e:
        return handle_http_error(e)


@mcp.tool()
def gmail_trash_thread(thread_id: str, user_id: str = "me") -> dict:
    """Move a Gmail thread to the trash.

    Args:
        thread_id: The ID of the thread to trash.
        user_id: The user's email address or 'me'.
    """
    try:
        return api_post(f"{GMAIL_BASE}/{user_id}/threads/{thread_id}/trash")
    except requests.HTTPError as e:
        return handle_http_error(e)


@mcp.tool()
def gmail_delete_thread(thread_id: str, user_id: str = "me") -> dict:
    """Permanently delete a Gmail thread.

    Args:
        thread_id: The ID of the thread to delete.
        user_id: The user's email address or 'me'.
    """
    try:
        return api_delete(f"{GMAIL_BASE}/{user_id}/threads/{thread_id}")
    except requests.HTTPError as e:
        return handle_http_error(e)


# ---------------------------------------------------------------------------
# History
# ---------------------------------------------------------------------------


@mcp.tool()
def gmail_list_history(
    start_history_id: str,
    user_id: str = "me",
    max_results: int = 100,
    label_id: Optional[str] = None,
    history_types: Optional[list] = None,
    page_token: Optional[str] = None,
) -> dict:
    """List the history of changes to the Gmail mailbox.

    Args:
        start_history_id: Required. Returns history records after this ID.
        user_id: The user's email address or 'me'.
        max_results: Maximum number of history records to return.
        label_id: Only return messages with a label matching this ID.
        history_types: History types to return: 'messageAdded', 'messageDeleted', 'labelAdded', 'labelRemoved'.
        page_token: Page token for pagination.
    """
    try:
        params: dict[str, Any] = {
            "startHistoryId": start_history_id,
            "maxResults": max_results,
        }
        if label_id:
            params["labelId"] = label_id
        if history_types:
            params["historyTypes"] = history_types
        if page_token:
            params["pageToken"] = page_token
        return api_get(f"{GMAIL_BASE}/{user_id}/history", params=params)
    except requests.HTTPError as e:
        return handle_http_error(e)


# ---------------------------------------------------------------------------
# Settings
# ---------------------------------------------------------------------------


@mcp.tool()
def gmail_get_vacation_settings(user_id: str = "me") -> dict:
    """Get Gmail vacation responder settings.

    Args:
        user_id: The user's email address or 'me'.
    """
    try:
        return api_get(f"{GMAIL_BASE}/{user_id}/settings/vacation")
    except requests.HTTPError as e:
        return handle_http_error(e)


@mcp.tool()
def gmail_update_vacation_settings(
    enable_auto_reply: bool,
    response_subject: Optional[str] = None,
    response_body_plain_text: Optional[str] = None,
    restrict_to_contacts: bool = False,
    restrict_to_domain: bool = False,
    start_time_epoch_ms: Optional[int] = None,
    end_time_epoch_ms: Optional[int] = None,
    user_id: str = "me",
) -> dict:
    """Update Gmail vacation responder settings.

    Args:
        enable_auto_reply: Whether the vacation responder is enabled.
        response_subject: Subject line of the vacation auto-reply.
        response_body_plain_text: Plain text body of the vacation auto-reply.
        restrict_to_contacts: Only send auto-reply to contacts.
        restrict_to_domain: Only send auto-reply to users in the same domain.
        start_time_epoch_ms: Start time of the vacation responder (epoch ms).
        end_time_epoch_ms: End time of the vacation responder (epoch ms).
        user_id: The user's email address or 'me'.
    """
    try:
        payload: dict[str, Any] = {
            "enableAutoReply": enable_auto_reply,
            "restrictToContacts": restrict_to_contacts,
            "restrictToDomain": restrict_to_domain,
        }
        if response_subject is not None:
            payload["responseSubject"] = response_subject
        if response_body_plain_text is not None:
            payload["responseBodyPlainText"] = response_body_plain_text
        if start_time_epoch_ms is not None:
            payload["startTime"] = str(start_time_epoch_ms)
        if end_time_epoch_ms is not None:
            payload["endTime"] = str(end_time_epoch_ms)
        return api_put(f"{GMAIL_BASE}/{user_id}/settings/vacation", payload=payload)
    except requests.HTTPError as e:
        return handle_http_error(e)


@mcp.tool()
def gmail_get_imap_settings(user_id: str = "me") -> dict:
    """Get Gmail IMAP settings.

    Args:
        user_id: The user's email address or 'me'.
    """
    try:
        return api_get(f"{GMAIL_BASE}/{user_id}/settings/imap")
    except requests.HTTPError as e:
        return handle_http_error(e)


@mcp.tool()
def gmail_get_pop_settings(user_id: str = "me") -> dict:
    """Get Gmail POP settings.

    Args:
        user_id: The user's email address or 'me'.
    """
    try:
        return api_get(f"{GMAIL_BASE}/{user_id}/settings/pop")
    except requests.HTTPError as e:
        return handle_http_error(e)


@mcp.tool()
def gmail_get_auto_forwarding(user_id: str = "me") -> dict:
    """Get Gmail auto-forwarding settings.

    Args:
        user_id: The user's email address or 'me'.
    """
    try:
        return api_get(f"{GMAIL_BASE}/{user_id}/settings/autoForwarding")
    except requests.HTTPError as e:
        return handle_http_error(e)
