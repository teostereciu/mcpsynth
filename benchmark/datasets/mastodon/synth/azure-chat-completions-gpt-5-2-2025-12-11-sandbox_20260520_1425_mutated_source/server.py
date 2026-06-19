import os
import re
import json
from typing import Any, Dict, Optional

import httpx
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP

load_dotenv()

mcp = FastMCP("mastodon")


def _base_url() -> str:
    base = os.getenv("MASTODON_BASE_URL", "").strip()
    if not base:
        raise ValueError("MASTODON_BASE_URL is required, e.g. https://mastodon.social")
    return base.rstrip("/")


def _token() -> Optional[str]:
    tok = os.getenv("MASTODON_ACCESS_TOKEN", "").strip()
    return tok or None


def _headers(extra: Optional[Dict[str, str]] = None) -> Dict[str, str]:
    h: Dict[str, str] = {
        "Accept": "application/json",
        "User-Agent": os.getenv("MASTODON_USER_AGENT", "mastodon-mcp/1.0"),
    }
    tok = _token()
    if tok:
        h["Authorization"] = f"Bearer {tok}"
    if extra:
        h.update({k: v for k, v in extra.items() if v is not None})
    return h


def _parse_link_header(link: str) -> Dict[str, str]:
    # RFC5988-ish: <url>; rel="next", <url>; rel="prev"
    out: Dict[str, str] = {}
    for part in link.split(","):
        part = part.strip()
        m = re.match(r"<([^>]+)>;\s*rel=\"([^\"]+)\"", part)
        if m:
            url, rel = m.group(1), m.group(2)
            out[rel] = url
    return out


def _request(
    method: str,
    path: str,
    *,
    params: Optional[Dict[str, Any]] = None,
    json_body: Optional[Dict[str, Any]] = None,
    form: Optional[Dict[str, Any]] = None,
    files: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None,
    timeout: float = 30.0,
) -> Dict[str, Any]:
    url = _base_url() + path
    with httpx.Client(timeout=timeout, headers=_headers(headers)) as client:
        resp = client.request(method, url, params=params, json=json_body, data=form, files=files)

    content_type = resp.headers.get("content-type", "")
    data: Any
    if "application/json" in content_type:
        data = resp.json()
    else:
        data = resp.text

    result: Dict[str, Any] = {
        "ok": 200 <= resp.status_code < 300,
        "status": resp.status_code,
        "data": data,
        "headers": {
            "content_type": content_type,
        },
    }

    if "link" in resp.headers:
        result["headers"]["link"] = resp.headers["link"]
        result["pagination"] = _parse_link_header(resp.headers["link"])

    if not result["ok"]:
        # Mastodon often returns {error: ...}
        raise RuntimeError(json.dumps(result, ensure_ascii=False))

    return result


@mcp.tool()
def mastodon_request(
    method: str,
    path: str,
    params: Optional[Dict[str, Any]] = None,
    json_body: Optional[Dict[str, Any]] = None,
    form: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None,
) -> Dict[str, Any]:
    """Generic Mastodon REST API request.

    Args:
      method: HTTP method (GET, POST, PUT, PATCH, DELETE)
      path: API path starting with /api/... or /oauth/...
      params: Query parameters
      json_body: JSON body (for application/json)
      form: Form body (for application/x-www-form-urlencoded)
      headers: Extra headers (e.g. {"Idempotency-Key": "..."})

    Returns:
      {ok, status, data, headers, pagination?}
    """
    if not path.startswith("/"):
        path = "/" + path
    return _request(method.upper(), path, params=params, json_body=json_body, form=form, headers=headers)


# ---- Convenience tools (common agent workflows) ----

@mcp.tool()
def apps_create(client_name: str, redirect_uris: str, scopes: Optional[str] = None, website: Optional[str] = None) -> Dict[str, Any]:
    """Create an OAuth application (POST /api/v1/apps)."""
    form = {
        "client_name": client_name,
        "redirect_uris": redirect_uris,
    }
    if scopes is not None:
        form["scopes"] = scopes
    if website is not None:
        form["website"] = website
    return _request("POST", "/api/v1/apps", form=form)


@mcp.tool()
def oauth_token(password_grant: bool = False, **kwargs: Any) -> Dict[str, Any]:
    """Obtain an OAuth token (POST /oauth/token).

    Supports multiple grant types. Provide fields as kwargs.

    Common:
      - grant_type: "authorization_code" | "password" | "client_credentials" | "refresh_token"
      - client_id, client_secret
      - redirect_uri, code
      - username, password
      - scope
      - refresh_token

    If password_grant=True, will set grant_type=password if not provided.
    """
    form = dict(kwargs)
    if password_grant and "grant_type" not in form:
        form["grant_type"] = "password"
    if "grant_type" not in form:
        raise ValueError("grant_type is required")
    return _request("POST", "/oauth/token", form=form)


@mcp.tool()
def oauth_revoke(token: str, client_id: Optional[str] = None, client_secret: Optional[str] = None) -> Dict[str, Any]:
    """Revoke an OAuth token (POST /oauth/revoke)."""
    form: Dict[str, Any] = {"token": token}
    if client_id is not None:
        form["client_id"] = client_id
    if client_secret is not None:
        form["client_secret"] = client_secret
    return _request("POST", "/oauth/revoke", form=form)


@mcp.tool()
def accounts_verify_credentials() -> Dict[str, Any]:
    """Get the current account (GET /api/v1/accounts/verify_credentials)."""
    return _request("GET", "/api/v1/accounts/verify_credentials")


@mcp.tool()
def accounts_update_credentials(
    display_name: Optional[str] = None,
    note: Optional[str] = None,
    locked: Optional[bool] = None,
    bot: Optional[bool] = None,
    discoverable: Optional[bool] = None,
    hide_collections: Optional[bool] = None,
    fields: Optional[list] = None,
) -> Dict[str, Any]:
    """Update current account (PATCH /api/v1/accounts/update_credentials).

    Note: This endpoint accepts multipart for avatars/headers; this helper covers common text fields.
    """
    form: Dict[str, Any] = {}
    if display_name is not None:
        form["display_name"] = display_name
    if note is not None:
        form["note"] = note
    if locked is not None:
        form["locked"] = "true" if locked else "false"
    if bot is not None:
        form["bot"] = "true" if bot else "false"
    if discoverable is not None:
        form["discoverable"] = "true" if discoverable else "false"
    if hide_collections is not None:
        form["hide_collections"] = "true" if hide_collections else "false"
    if fields is not None:
        # expects list of {name, value}
        for i, f in enumerate(fields):
            if "name" in f:
                form[f"fields_attributes[{i}][name]"] = f["name"]
            if "value" in f:
                form[f"fields_attributes[{i}][value]"] = f["value"]
    return _request("PATCH", "/api/v1/accounts/update_credentials", form=form)


@mcp.tool()
def statuses_create(
    status: str,
    visibility: Optional[str] = None,
    in_reply_to_id: Optional[str] = None,
    quoted_status_id: Optional[str] = None,
    sensitive: Optional[bool] = None,
    spoiler_text: Optional[str] = None,
    language: Optional[str] = None,
    media_ids: Optional[list] = None,
    poll: Optional[dict] = None,
    scheduled_at: Optional[str] = None,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    """Create a status (POST /api/v1/statuses)."""
    form: Dict[str, Any] = {"status": status}
    if visibility is not None:
        form["visibility"] = visibility
    if in_reply_to_id is not None:
        form["in_reply_to_id"] = in_reply_to_id
    if quoted_status_id is not None:
        form["quoted_status_id"] = quoted_status_id
    if sensitive is not None:
        form["sensitive"] = "true" if sensitive else "false"
    if spoiler_text is not None:
        form["spoiler_text"] = spoiler_text
    if language is not None:
        form["language"] = language
    if scheduled_at is not None:
        form["scheduled_at"] = scheduled_at
    if media_ids:
        for i, mid in enumerate(media_ids):
            form[f"media_ids[{i}]"] = str(mid)
    if poll:
        # poll: {options: [...], expires_in, multiple, hide_totals}
        if "expires_in" in poll:
            form["poll[expires_in]"] = str(poll["expires_in"])
        if "multiple" in poll:
            form["poll[multiple]"] = "true" if poll["multiple"] else "false"
        if "hide_totals" in poll:
            form["poll[hide_totals]"] = "true" if poll["hide_totals"] else "false"
        if "options" in poll and isinstance(poll["options"], list):
            for i, opt in enumerate(poll["options"]):
                form[f"poll[options][{i}]"] = opt
    headers = {"Idempotency-Key": idempotency_key} if idempotency_key else None
    return _request("POST", "/api/v1/statuses", form=form, headers=headers)


@mcp.tool()
def statuses_get(id: str) -> Dict[str, Any]:
    """Get a status (GET /api/v1/statuses/:id)."""
    return _request("GET", f"/api/v1/statuses/{id}")


@mcp.tool()
def statuses_delete(id: str, delete_media: Optional[bool] = None) -> Dict[str, Any]:
    """Delete a status (DELETE /api/v1/statuses/:id)."""
    params = {}
    if delete_media is not None:
        params["delete_media"] = "true" if delete_media else "false"
    return _request("DELETE", f"/api/v1/statuses/{id}", params=params or None)


@mcp.tool()
def statuses_favourite(id: str) -> Dict[str, Any]:
    """Favourite a status (POST /api/v1/statuses/:id/favourite)."""
    return _request("POST", f"/api/v1/statuses/{id}/favourite")


@mcp.tool()
def statuses_unfavourite(id: str) -> Dict[str, Any]:
    """Unfavourite a status (POST /api/v1/statuses/:id/unfavourite)."""
    return _request("POST", f"/api/v1/statuses/{id}/unfavourite")


@mcp.tool()
def statuses_reblog(id: str) -> Dict[str, Any]:
    """Reblog a status (POST /api/v1/statuses/:id/reblog)."""
    return _request("POST", f"/api/v1/statuses/{id}/reblog")


@mcp.tool()
def statuses_unreblog(id: str) -> Dict[str, Any]:
    """Unreblog a status (POST /api/v1/statuses/:id/unreblog)."""
    return _request("POST", f"/api/v1/statuses/{id}/unreblog")


@mcp.tool()
def timelines_home(limit: Optional[int] = None, local: Optional[bool] = None) -> Dict[str, Any]:
    """Home timeline (GET /api/v1/timelines/home)."""
    params: Dict[str, Any] = {}
    if limit is not None:
        params["limit"] = limit
    if local is not None:
        params["local"] = "true" if local else "false"
    return _request("GET", "/api/v1/timelines/home", params=params or None)


@mcp.tool()
def timelines_public(limit: Optional[int] = None, local: Optional[bool] = None, remote: Optional[bool] = None, only_media: Optional[bool] = None) -> Dict[str, Any]:
    """Public timeline (GET /api/v1/timelines/public)."""
    params: Dict[str, Any] = {}
    if limit is not None:
        params["limit"] = limit
    if local is not None:
        params["local"] = "true" if local else "false"
    if remote is not None:
        params["remote"] = "true" if remote else "false"
    if only_media is not None:
        params["only_media"] = "true" if only_media else "false"
    return _request("GET", "/api/v1/timelines/public", params=params or None)


@mcp.tool()
def notifications_list(limit: Optional[int] = None, types: Optional[list] = None, exclude_types: Optional[list] = None, max_id: Optional[str] = None, since_id: Optional[str] = None, min_id: Optional[str] = None) -> Dict[str, Any]:
    """List notifications (GET /api/v1/notifications)."""
    params: Dict[str, Any] = {}
    if limit is not None:
        params["limit"] = limit
    if max_id is not None:
        params["max_id"] = max_id
    if since_id is not None:
        params["since_id"] = since_id
    if min_id is not None:
        params["min_id"] = min_id
    if types:
        for i, t in enumerate(types):
            params[f"types[{i}]"] = t
    if exclude_types:
        for i, t in enumerate(exclude_types):
            params[f"exclude_types[{i}]"] = t
    return _request("GET", "/api/v1/notifications", params=params or None)


@mcp.tool()
def notifications_dismiss(id: str) -> Dict[str, Any]:
    """Dismiss a notification (POST /api/v1/notifications/:id/dismiss)."""
    return _request("POST", f"/api/v1/notifications/{id}/dismiss")


@mcp.tool()
def notifications_clear() -> Dict[str, Any]:
    """Clear notifications (POST /api/v1/notifications/clear)."""
    return _request("POST", "/api/v1/notifications/clear")


@mcp.tool()
def search_v2(q: str, type: Optional[str] = None, resolve: Optional[bool] = None, limit: Optional[int] = None, offset: Optional[int] = None, following: Optional[bool] = None) -> Dict[str, Any]:
    """Search (GET /api/v2/search)."""
    params: Dict[str, Any] = {"q": q}
    if type is not None:
        params["type"] = type
    if resolve is not None:
        params["resolve"] = "true" if resolve else "false"
    if limit is not None:
        params["limit"] = limit
    if offset is not None:
        params["offset"] = offset
    if following is not None:
        params["following"] = "true" if following else "false"
    return _request("GET", "/api/v2/search", params=params)


@mcp.tool()
def media_upload(file_path: str, description: Optional[str] = None, focus: Optional[str] = None) -> Dict[str, Any]:
    """Upload media (POST /api/v2/media preferred; falls back to v1).

    Args:
      file_path: Path to local file to upload.
      description: Alt text.
      focus: "x,y" focus string.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(file_path)
    files = {"file": open(file_path, "rb")}
    form: Dict[str, Any] = {}
    if description is not None:
        form["description"] = description
    if focus is not None:
        form["focus"] = focus
    try:
        return _request("POST", "/api/v2/media", form=form or None, files=files)
    finally:
        try:
            files["file"].close()
        except Exception:
            pass


@mcp.tool()
def instance_v2() -> Dict[str, Any]:
    """Get instance info (GET /api/v2/instance)."""
    return _request("GET", "/api/v2/instance")


@mcp.tool()
def oembed(url: str, maxwidth: Optional[int] = None, maxheight: Optional[int] = None) -> Dict[str, Any]:
    """Get oEmbed for a status URL (GET /api/oembed)."""
    params: Dict[str, Any] = {"url": url}
    if maxwidth is not None:
        params["maxwidth"] = maxwidth
    if maxheight is not None:
        params["maxheight"] = maxheight
    return _request("GET", "/api/oembed", params=params)


if __name__ == "__main__":
    mcp.run()
