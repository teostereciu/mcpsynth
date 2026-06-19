import base64
import json
import os
from typing import Any, Dict, Optional

import requests
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("ebay-commerce-api")

APP_TOKEN: Optional[str] = None
USER_TOKEN: Optional[str] = None


def _env(name: str, default: Optional[str] = None) -> Optional[str]:
    value = os.getenv(name, default)
    return value if value not in ("", None) else default


def _base_url() -> str:
    env = (_env("EBAY_ENVIRONMENT", "SANDBOX") or "SANDBOX").upper()
    return "https://api.ebay.com" if env == "PRODUCTION" else "https://api.sandbox.ebay.com"


def _media_base_url() -> str:
    env = (_env("EBAY_ENVIRONMENT", "SANDBOX") or "SANDBOX").upper()
    return "https://apim.ebay.com" if env == "PRODUCTION" else "https://apim.sandbox.ebay.com"


def _token(grant_type: str) -> str:
    global APP_TOKEN, USER_TOKEN
    if grant_type == "client_credentials" and APP_TOKEN:
        return APP_TOKEN
    if grant_type == "refresh_token" and USER_TOKEN:
        return USER_TOKEN

    app_id = _env("EBAY_APP_ID")
    cert_id = _env("EBAY_CERT_ID")
    if not app_id or not cert_id:
        raise RuntimeError("Missing EBAY_APP_ID or EBAY_CERT_ID")

    auth = base64.b64encode(f"{app_id}:{cert_id}".encode()).decode()
    headers = {"Authorization": f"Basic {auth}", "Content-Type": "application/x-www-form-urlencoded"}
    data = {"grant_type": grant_type, "scope": "https://api.ebay.com/oauth/api_scope"}
    if grant_type == "refresh_token":
        refresh = _env("EBAY_REFRESH_TOKEN")
        if not refresh:
            raise RuntimeError("Missing EBAY_REFRESH_TOKEN")
        data["refresh_token"] = refresh

    resp = requests.post(f"{_base_url()}/identity/v1/oauth2/token", headers=headers, data=data, timeout=60)
    if resp.status_code >= 400:
        raise RuntimeError(resp.text)
    token = resp.json()["access_token"]
    if grant_type == "client_credentials":
        APP_TOKEN = token
    else:
        USER_TOKEN = token
    return token


def _request(method: str, url: str, *, auth: str, params: Dict[str, Any] = None, json_body: Any = None, files=None):
    headers = {"Authorization": f"Bearer {auth}", "Content-Type": "application/json"}
    resp = requests.request(method, url, headers=headers, params=params, json=json_body, files=files, timeout=120)
    try:
        data = resp.json()
    except Exception:
        data = resp.text
    if resp.status_code >= 400:
        return {"error": data, "status": resp.status_code}
    return data


@mcp.tool()
def get_product(product_id: str):
    return _request("GET", f"{_base_url()}/commerce/catalog/v1_beta/product/{product_id}", auth=_token("client_credentials"))


@mcp.tool()
def search_products(q: str, limit: int = 10, category_ids: Optional[str] = None):
    params = {"q": q, "limit": limit}
    if category_ids:
        params["category_ids"] = category_ids
    return _request("GET", f"{_base_url()}/commerce/catalog/v1_beta/product_summary/search", auth=_token("client_credentials"), params=params)


@mcp.tool()
def get_charity_org(charity_org_id: str):
    return _request("GET", f"{_base_url()}/commerce/charity/v1/charity_org/{charity_org_id}", auth=_token("refresh_token"))


@mcp.tool()
def get_charity_orgs(q: Optional[str] = None, registration_id: Optional[str] = None):
    params = {}
    if q:
        params["q"] = q
    if registration_id:
        params["registration_id"] = registration_id
    return _request("GET", f"{_base_url()}/commerce/charity/v1/charity_org", auth=_token("refresh_token"), params=params)


@mcp.tool()
def get_user():
    return _request("GET", f"{_base_url()}/commerce/identity/v1/user", auth=_token("refresh_token"))


@mcp.tool()
def get_document(document_id: str):
    return _request("GET", f"{_media_base_url()}/commerce/media/v1/document/{document_id}", auth=_token("refresh_token"))


@mcp.tool()
def create_document_from_url(source_url: str, name: Optional[str] = None):
    body = {"source_url": source_url}
    if name:
        body["name"] = name
    return _request("POST", f"{_media_base_url()}/commerce/media/v1/document_from_url", auth=_token("refresh_token"), json_body=body)


@mcp.tool()
def upload_document(name: str, content: str):
    return _request("POST", f"{_media_base_url()}/commerce/media/v1/document/upload", auth=_token("refresh_token"), json_body={"name": name, "content": content})


@mcp.tool()
def create_image_from_url(source_url: str, name: Optional[str] = None):
    body = {"source_url": source_url}
    if name:
        body["name"] = name
    return _request("POST", f"{_media_base_url()}/commerce/media/v1/image_from_url", auth=_token("refresh_token"), json_body=body)


@mcp.tool()
def get_image(image_id: str):
    return _request("GET", f"{_media_base_url()}/commerce/media/v1/image/{image_id}", auth=_token("refresh_token"))


@mcp.tool()
def create_video(name: str, content: str):
    return _request("POST", f"{_media_base_url()}/commerce/media/v1/video", auth=_token("refresh_token"), json_body={"name": name, "content": content})


@mcp.tool()
def get_video(video_id: str):
    return _request("GET", f"{_media_base_url()}/commerce/media/v1/video/{video_id}", auth=_token("refresh_token"))


@mcp.tool()
def get_config():
    return _request("GET", f"{_base_url()}/commerce/notification/v1/config", auth=_token("refresh_token"))


@mcp.tool()
def update_config(config: Dict[str, Any]):
    return _request("PUT", f"{_base_url()}/commerce/notification/v1/config", auth=_token("refresh_token"), json_body=config)


@mcp.tool()
def get_destinations():
    return _request("GET", f"{_base_url()}/commerce/notification/v1/destination", auth=_token("refresh_token"))


@mcp.tool()
def create_destination(destination: Dict[str, Any]):
    return _request("POST", f"{_base_url()}/commerce/notification/v1/destination", auth=_token("refresh_token"), json_body=destination)


@mcp.tool()
def get_destination(destination_id: str):
    return _request("GET", f"{_base_url()}/commerce/notification/v1/destination/{destination_id}", auth=_token("refresh_token"))


@mcp.tool()
def update_destination(destination_id: str, destination: Dict[str, Any]):
    return _request("PUT", f"{_base_url()}/commerce/notification/v1/destination/{destination_id}", auth=_token("refresh_token"), json_body=destination)


@mcp.tool()
def delete_destination(destination_id: str):
    return _request("DELETE", f"{_base_url()}/commerce/notification/v1/destination/{destination_id}", auth=_token("refresh_token"))


@mcp.tool()
def get_public_key():
    return _request("GET", f"{_base_url()}/commerce/notification/v1/public_key", auth=_token("refresh_token"))


@mcp.tool()
def get_topics():
    return _request("GET", f"{_base_url()}/commerce/notification/v1/topic", auth=_token("refresh_token"))


@mcp.tool()
def get_topic(topic_id: str):
    return _request("GET", f"{_base_url()}/commerce/notification/v1/topic/{topic_id}", auth=_token("refresh_token"))


@mcp.tool()
def get_subscriptions():
    return _request("GET", f"{_base_url()}/commerce/notification/v1/subscription", auth=_token("refresh_token"))


@mcp.tool()
def create_subscription(subscription: Dict[str, Any]):
    return _request("POST", f"{_base_url()}/commerce/notification/v1/subscription", auth=_token("refresh_token"), json_body=subscription)


@mcp.tool()
def get_subscription(subscription_id: str):
    return _request("GET", f"{_base_url()}/commerce/notification/v1/subscription/{subscription_id}", auth=_token("refresh_token"))


@mcp.tool()
def update_subscription(subscription_id: str, subscription: Dict[str, Any]):
    return _request("PUT", f"{_base_url()}/commerce/notification/v1/subscription/{subscription_id}", auth=_token("refresh_token"), json_body=subscription)


@mcp.tool()
def delete_subscription(subscription_id: str):
    return _request("DELETE", f"{_base_url()}/commerce/notification/v1/subscription/{subscription_id}", auth=_token("refresh_token"))


@mcp.tool()
def get_default_category_tree_id():
    return _request("GET", f"{_base_url()}/commerce/taxonomy/v1/category_tree/get_default_category_tree_id", auth=_token("client_credentials"))


@mcp.tool()
def get_category_tree(category_tree_id: str):
    return _request("GET", f"{_base_url()}/commerce/taxonomy/v1/category_tree/{category_tree_id}", auth=_token("client_credentials"))


@mcp.tool()
def get_category_subtree(category_tree_id: str, category_id: str):
    return _request("GET", f"{_base_url()}/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_category_subtree", auth=_token("client_credentials"), params={"category_id": category_id})


@mcp.tool()
def get_category_suggestions(category_tree_id: str, q: str):
    return _request("GET", f"{_base_url()}/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_category_suggestions", auth=_token("client_credentials"), params={"q": q})


@mcp.tool()
def fetch_item_aspects(category_tree_id: str, q: str):
    return _request("GET", f"{_base_url()}/commerce/taxonomy/v1/category_tree/{category_tree_id}/fetch_item_aspects", auth=_token("client_credentials"), params={"q": q})


@mcp.tool()
def get_item_aspects_for_category(category_tree_id: str, category_id: str):
    return _request("GET", f"{_base_url()}/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_item_aspects_for_category", auth=_token("client_credentials"), params={"category_id": category_id})


@mcp.tool()
def get_compatibility_properties(category_tree_id: str):
    return _request("GET", f"{_base_url()}/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_compatibility_properties", auth=_token("client_credentials"))


@mcp.tool()
def get_compatibility_property_values(category_tree_id: str, category_id: str, compatibility_property: str, filter: Optional[str] = None):
    params = {"category_id": category_id, "compatibility_property": compatibility_property}
    if filter:
        params["filter"] = filter
    return _request("GET", f"{_base_url()}/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_compatibility_property_values", auth=_token("client_credentials"), params=params)


@mcp.tool()
def get_expired_categories(category_tree_id: str):
    return _request("GET", f"{_base_url()}/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_expired_categories", auth=_token("client_credentials"))


@mcp.tool()
def translate(text: str, from_language: str, to_language: str):
    return _request("POST", f"{_base_url()}/commerce/translation/v1/language/translate", auth=_token("refresh_token"), json_body={"text": text, "from_language": from_language, "to_language": to_language})


if __name__ == "__main__":
    mcp.run(transport="stdio")
