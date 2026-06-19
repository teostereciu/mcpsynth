from mcp.server.fastmcp import FastMCP
import os, requests, json

mcp = FastMCP("mastodon")
BASE_URL = os.environ.get("MASTODON_BASE_URL", "https://mastodon.social").rstrip("/") + "/api/v1"
TOKEN = os.environ.get("MASTODON_ACCESS_TOKEN")


def _headers(auth=True):
    h = {"Accept": "application/json"}
    if auth and TOKEN:
        h["Authorization"] = f"Bearer {TOKEN}"
    return h


def _request(method, path, *, auth=True, params=None, data=None, files=None):
    r = requests.request(method, BASE_URL + path, headers=_headers(auth), params=params, data=data, files=files, timeout=60)
    try:
        body = r.json()
    except Exception:
        body = r.text
    return {"status_code": r.status_code, "headers": dict(r.headers), "body": body}


@mcp.tool()
def get_instance():
    return _request("GET", "/instance", auth=False)


@mcp.tool()
def verify_credentials():
    return _request("GET", "/accounts/verify_credentials")


@mcp.tool()
def get_profile():
    return _request("GET", "/profile")


@mcp.tool()
def search(q: str, type: str | None = None, resolve: bool | None = None, following: bool | None = None, account_id: str | None = None, exclude_unreviewed: bool | None = None, max_id: str | None = None, min_id: str | None = None, limit: int | None = None, offset: int | None = None):
    params = {k: v for k, v in {"q": q, "type": type, "resolve": resolve, "following": following, "account_id": account_id, "exclude_unreviewed": exclude_unreviewed, "max_id": max_id, "min_id": min_id, "limit": limit, "offset": offset}.items() if v is not None}
    return _request("GET", "/search", params=params)


@mcp.tool()
def get_status(id: str): return _request("GET", f"/statuses/{id}", auth=False)
@mcp.tool()
def get_status_context(id: str): return _request("GET", f"/statuses/{id}/context", auth=False)
@mcp.tool()
def post_status(status: str | None = None, in_reply_to_id: str | None = None, sensitive: bool | None = None, spoiler_text: str | None = None, visibility: str | None = None, language: str | None = None, scheduled_at: str | None = None, quoted_status_id: str | None = None, quote_approval_policy: str | None = None):
    data = {k: v for k, v in {"status": status, "in_reply_to_id": in_reply_to_id, "sensitive": sensitive, "spoiler_text": spoiler_text, "visibility": visibility, "language": language, "scheduled_at": scheduled_at, "quoted_status_id": quoted_status_id, "quote_approval_policy": quote_approval_policy}.items() if v is not None}
    return _request("POST", "/statuses", data=data)


@mcp.tool()
def delete_status(id: str, delete_media: bool | None = None):
    params = {k: v for k, v in {"delete_media": delete_media}.items() if v is not None}
    return _request("DELETE", f"/statuses/{id}", params=params)


for name, path in [("favourite_status", "/statuses/{id}/favourite"), ("unfavourite_status", "/statuses/{id}/unfavourite"), ("boost_status", "/statuses/{id}/reblog"), ("unboost_status", "/statuses/{id}/unreblog"), ("bookmark_status", "/statuses/{id}/bookmark"), ("unbookmark_status", "/statuses/{id}/unbookmark")]:
    def _make(p):
        @mcp.tool(name=name)
        def _fn(id: str): return _request("POST", p.format(id=id))
        return _fn
    _make(path)


@mcp.tool()
def get_notifications(max_id: str | None = None, since_id: str | None = None, min_id: str | None = None, limit: int | None = None, types: list[str] | None = None, exclude_types: list[str] | None = None, account_id: str | None = None, include_filtered: bool | None = None):
    params = {}
    for k, v in {"max_id": max_id, "since_id": since_id, "min_id": min_id, "limit": limit, "account_id": account_id, "include_filtered": include_filtered}.items():
        if v is not None: params[k] = v
    if types: params.update({"types[]": types})
    if exclude_types: params.update({"exclude_types[]": exclude_types})
    return _request("GET", "/notifications", params=params)


@mcp.tool()
def get_lists(): return _request("GET", "/lists")


if __name__ == "__main__":
    mcp.run()
