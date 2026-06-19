from typing import Any, Dict, Optional

from .slack_client import SlackWebAPIClient, _clean_dict


def files_list(
    channel: Optional[str] = None,
    user: Optional[str] = None,
    types: Optional[str] = None,
    ts_from: Optional[str] = None,
    ts_to: Optional[str] = None,
    count: Optional[int] = None,
    page: Optional[int] = None,
    show_files_hidden_by_limit: Optional[bool] = None,
    team_id: Optional[str] = None,
    client: Optional[SlackWebAPIClient] = None,
) -> Dict[str, Any]:
    client = client or SlackWebAPIClient()
    params = _clean_dict(
        {
            "channel": channel,
            "user": user,
            "types": types,
            "ts_from": ts_from,
            "ts_to": ts_to,
            "count": count,
            "page": page,
            "show_files_hidden_by_limit": show_files_hidden_by_limit,
            "team_id": team_id,
        }
    )
    return client.get("files.list", params)


def files_get_upload_url_external(
    filename: str,
    length: int,
    snippet_type: Optional[str] = None,
    alt_txt: Optional[str] = None,
    client: Optional[SlackWebAPIClient] = None,
) -> Dict[str, Any]:
    client = client or SlackWebAPIClient()
    payload = _clean_dict(
        {
            "filename": filename,
            "length": length,
            "snippet_type": snippet_type,
            "alt_txt": alt_txt,
        }
    )
    return client.post("files.getUploadURLExternal", payload)


def files_complete_upload_external(
    files: Any,
    channel_id: Optional[str] = None,
    channels: Optional[str] = None,
    thread_ts: Optional[str] = None,
    initial_comment: Optional[str] = None,
    blocks: Optional[Any] = None,
    client: Optional[SlackWebAPIClient] = None,
) -> Dict[str, Any]:
    client = client or SlackWebAPIClient()
    payload = _clean_dict(
        {
            "files": files,
            "channel_id": channel_id,
            "channels": channels,
            "thread_ts": thread_ts,
            "initial_comment": initial_comment,
            "blocks": blocks,
        }
    )
    return client.post("files.completeUploadExternal", payload)


# Deprecated by Slack; prefer files.getUploadURLExternal + files.completeUploadExternal.
# Included for compatibility.
def files_upload(
    channels: Optional[str] = None,
    content: Optional[str] = None,
    filename: Optional[str] = None,
    filetype: Optional[str] = None,
    initial_comment: Optional[str] = None,
    thread_ts: Optional[str] = None,
    title: Optional[str] = None,
    client: Optional[SlackWebAPIClient] = None,
) -> Dict[str, Any]:
    client = client or SlackWebAPIClient()
    payload = _clean_dict(
        {
            "channels": channels,
            "content": content,
            "filename": filename,
            "filetype": filetype,
            "initial_comment": initial_comment,
            "thread_ts": thread_ts,
            "title": title,
        }
    )
    return client.post("files.upload", payload)
