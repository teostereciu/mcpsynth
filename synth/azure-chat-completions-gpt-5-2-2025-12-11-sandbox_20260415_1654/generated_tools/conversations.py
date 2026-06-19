from typing import Any, Dict, Optional

from .twilio_client import TwilioClient, conversations_base_url


def create_conversation(
    *,
    friendly_name: Optional[str] = None,
    unique_name: Optional[str] = None,
    attributes: Optional[str] = None,
    state: Optional[str] = None,
    timers_inactive: Optional[str] = None,
    timers_closed: Optional[str] = None,
    messaging_service_sid: Optional[str] = None,
    webhook_enabled: Optional[bool] = None,
) -> Dict[str, Any]:
    """POST /Conversations - Create a conversation."""
    client = TwilioClient()
    url = f"{conversations_base_url()}/Conversations"
    headers = None
    if webhook_enabled is not None:
        headers = {"X-Twilio-Webhook-Enabled": "true" if webhook_enabled else "false"}
    data: Dict[str, Any] = {
        "FriendlyName": friendly_name,
        "UniqueName": unique_name,
        "Attributes": attributes,
        "State": state,
        "Timers.Inactive": timers_inactive,
        "Timers.Closed": timers_closed,
        "MessagingServiceSid": messaging_service_sid,
    }
    return client.request("POST", url, data=data, headers=headers)


def fetch_conversation(sid_or_unique_name: str) -> Dict[str, Any]:
    """GET /Conversations/{Sid} - Fetch a conversation."""
    client = TwilioClient()
    url = f"{conversations_base_url()}/Conversations/{sid_or_unique_name}"
    return client.request("GET", url)


def list_conversations(
    *,
    state: Optional[str] = None,
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
    page_size: int = 50,
    page: Optional[int] = None,
    page_token: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /Conversations - List conversations."""
    client = TwilioClient()
    url = f"{conversations_base_url()}/Conversations"
    params: Dict[str, Any] = {
        "State": state,
        "StartDate": start_date,
        "EndDate": end_date,
        "PageSize": page_size,
        "Page": page,
        "PageToken": page_token,
    }
    return client.request("GET", url, params=params)


def update_conversation(
    sid_or_unique_name: str,
    *,
    friendly_name: Optional[str] = None,
    attributes: Optional[str] = None,
    state: Optional[str] = None,
    timers_inactive: Optional[str] = None,
    timers_closed: Optional[str] = None,
) -> Dict[str, Any]:
    """POST /Conversations/{Sid} - Update a conversation."""
    client = TwilioClient()
    url = f"{conversations_base_url()}/Conversations/{sid_or_unique_name}"
    data: Dict[str, Any] = {
        "FriendlyName": friendly_name,
        "Attributes": attributes,
        "State": state,
        "Timers.Inactive": timers_inactive,
        "Timers.Closed": timers_closed,
    }
    return client.request("POST", url, data=data)


def delete_conversation(sid_or_unique_name: str) -> Dict[str, Any]:
    """DELETE /Conversations/{Sid} - Delete a conversation."""
    client = TwilioClient()
    url = f"{conversations_base_url()}/Conversations/{sid_or_unique_name}"
    return client.request("DELETE", url)


def add_participant(
    conversation_sid: str,
    *,
    identity: Optional[str] = None,
    messaging_binding_address: Optional[str] = None,
    messaging_binding_proxy_address: Optional[str] = None,
    attributes: Optional[str] = None,
    role_sid: Optional[str] = None,
    webhook_enabled: Optional[bool] = None,
) -> Dict[str, Any]:
    """POST /Conversations/{ConversationSid}/Participants - Add a participant (chat identity or SMS binding)."""
    client = TwilioClient()
    url = f"{conversations_base_url()}/Conversations/{conversation_sid}/Participants"
    headers = None
    if webhook_enabled is not None:
        headers = {"X-Twilio-Webhook-Enabled": "true" if webhook_enabled else "false"}
    data: Dict[str, Any] = {
        "Identity": identity,
        "MessagingBinding.Address": messaging_binding_address,
        "MessagingBinding.ProxyAddress": messaging_binding_proxy_address,
        "Attributes": attributes,
        "RoleSid": role_sid,
    }
    return client.request("POST", url, data=data, headers=headers)


def list_participants(
    conversation_sid: str,
    *,
    page_size: int = 50,
    page: Optional[int] = None,
    page_token: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /Conversations/{ConversationSid}/Participants - List participants."""
    client = TwilioClient()
    url = f"{conversations_base_url()}/Conversations/{conversation_sid}/Participants"
    params: Dict[str, Any] = {"PageSize": page_size, "Page": page, "PageToken": page_token}
    return client.request("GET", url, params=params)


def delete_participant(conversation_sid: str, participant_sid: str) -> Dict[str, Any]:
    """DELETE /Conversations/{ConversationSid}/Participants/{Sid} - Remove a participant."""
    client = TwilioClient()
    url = f"{conversations_base_url()}/Conversations/{conversation_sid}/Participants/{participant_sid}"
    return client.request("DELETE", url)


def send_conversation_message(
    conversation_sid: str,
    *,
    author: Optional[str] = None,
    body: Optional[str] = None,
    attributes: Optional[str] = None,
    media_sid: Optional[str] = None,
    content_sid: Optional[str] = None,
    content_variables: Optional[str] = None,
    subject: Optional[str] = None,
    webhook_enabled: Optional[bool] = None,
) -> Dict[str, Any]:
    """POST /Conversations/{ConversationSid}/Messages - Send a message in a conversation."""
    client = TwilioClient()
    url = f"{conversations_base_url()}/Conversations/{conversation_sid}/Messages"
    headers = None
    if webhook_enabled is not None:
        headers = {"X-Twilio-Webhook-Enabled": "true" if webhook_enabled else "false"}
    data: Dict[str, Any] = {
        "Author": author,
        "Body": body,
        "Attributes": attributes,
        "MediaSid": media_sid,
        "ContentSid": content_sid,
        "ContentVariables": content_variables,
        "Subject": subject,
    }
    return client.request("POST", url, data=data, headers=headers)


def list_conversation_messages(
    conversation_sid: str,
    *,
    order: Optional[str] = None,
    page_size: int = 50,
    page: Optional[int] = None,
    page_token: Optional[str] = None,
) -> Dict[str, Any]:
    """GET /Conversations/{ConversationSid}/Messages - List messages."""
    client = TwilioClient()
    url = f"{conversations_base_url()}/Conversations/{conversation_sid}/Messages"
    params: Dict[str, Any] = {
        "Order": order,
        "PageSize": page_size,
        "Page": page,
        "PageToken": page_token,
    }
    return client.request("GET", url, params=params)
