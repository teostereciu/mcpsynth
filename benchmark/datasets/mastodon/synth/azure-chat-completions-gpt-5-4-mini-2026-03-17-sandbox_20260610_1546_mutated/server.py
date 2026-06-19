import os
from typing import Any, Dict

import httpx
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("mastodon")


def _base_url() -> str:
    return os.environ.get("MASTODON_BASE_URL", "").rstrip("/")


def _token() -> str:
    return os.environ.get("MASTODON_ACCESS_TOKEN", "")


def _client() -> httpx.Client:
    headers = {}
    if _token():
        headers["Authorization"] = f"Bearer {_token()}"
    return httpx.Client(base_url=f"{_base_url()}/api/v1", headers=headers, timeout=60.0)


def _request(method: str, path: str, *, params: Dict[str, Any] | None = None, data: Dict[str, Any] | None = None) -> Any:
    with _client() as client:
        resp = client.request(method, path, params=params, data=data)
        resp.raise_for_status()
        if resp.text:
            return resp.json()
        return None


@mcp.tool()
def get_instance() -> Any:
    return _request("GET", "/instance")


@mcp.tool()
def verify_account_credentials() -> Any:
    return _request("GET", "/accounts/verify_credentials")


@mcp.tool()
def update_account_credentials(**kwargs: Any) -> Any:
    return _request("PATCH", "/accounts/update_credentials", data=kwargs)


@mcp.tool()
def get_status(id: str) -> Any:
    return _request("GET", f"/statuses/{id}")


@mcp.tool()
def get_status_context(id: str) -> Any:
    return _request("GET", f"/statuses/{id}/context")


@mcp.tool()
def create_status(**kwargs: Any) -> Any:
    return _request("POST", "/statuses", data=kwargs)


@mcp.tool()
def delete_status(id: str, delete_media: bool | None = None) -> Any:
    params = {"delete_media": delete_media} if delete_media is not None else None
    return _request("DELETE", f"/statuses/{id}", params=params)


@mcp.tool()
def favourite_status(id: str) -> Any:
    return _request("POST", f"/statuses/{id}/favourite")


@mcp.tool()
def unfavourite_status(id: str) -> Any:
    return _request("POST", f"/statuses/{id}/unfavourite")


@mcp.tool()
def boost_status(id: str) -> Any:
    return _request("POST", f"/statuses/{id}/reblog")


@mcp.tool()
def unboost_status(id: str) -> Any:
    return _request("POST", f"/statuses/{id}/unreblog")


@mcp.tool()
def bookmark_status(id: str) -> Any:
    return _request("POST", f"/statuses/{id}/bookmark")


@mcp.tool()
def unbookmark_status(id: str) -> Any:
    return _request("POST", f"/statuses/{id}/unbookmark")


@mcp.tool()
def search(q: str, type: str | None = None) -> Any:
    params = {"q": q}
    if type:
        params["type"] = type
    return _request("GET", "/search", params=params)


if __name__ == "__main__":
    mcp.run()
