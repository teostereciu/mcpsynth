import os
import base64
import requests
from typing import Optional, Dict, Any, List
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("eBay Commerce API")

EBAY_APP_ID = os.environ.get("EBAY_APP_ID")
EBAY_CERT_ID = os.environ.get("EBAY_CERT_ID")
EBAY_REFRESH_TOKEN = os.environ.get("EBAY_REFRESH_TOKEN")
EBAY_ENVIRONMENT = os.environ.get("EBAY_ENVIRONMENT", "SANDBOX").upper()

if EBAY_ENVIRONMENT == "PRODUCTION":
    BASE_URL = "https://api.ebay.com"
    MEDIA_BASE_URL = "https://apim.ebay.com"
else:
    BASE_URL = "https://api.sandbox.ebay.com"
    MEDIA_BASE_URL = "https://apim.sandbox.ebay.com"

_app_token = None
_user_token = None

def get_auth_headers() -> Dict[str, str]:
    if not EBAY_APP_ID or not EBAY_CERT_ID:
        raise ValueError("EBAY_APP_ID and EBAY_CERT_ID must be set")
    auth_str = f"{EBAY_APP_ID}:{EBAY_CERT_ID}"
    b64_auth = base64.b64encode(auth_str.encode("utf-8")).decode("utf-8")
    return {
        "Authorization": f"Basic {b64_auth}",
        "Content-Type": "application/x-www-form-urlencoded"
    }

def get_app_token() -> str:
    global _app_token
    if _app_token:
        return _app_token
    
    url = f"{BASE_URL}/identity/v1/oauth2/token"
    data = {
        "grant_type": "client_credentials",
        "scope": "https://api.ebay.com/oauth/api_scope"
    }
    response = requests.post(url, headers=get_auth_headers(), data=data)
    if response.status_code == 200:
        _app_token = response.json().get("access_token")
        return _app_token
    else:
        raise Exception(f"Failed to get app token: {response.text}")

def get_user_token() -> str:
    global _user_token
    if _user_token:
        return _user_token
    
    if not EBAY_REFRESH_TOKEN:
        raise ValueError("EBAY_REFRESH_TOKEN must be set for user-scoped APIs")
        
    url = f"{BASE_URL}/identity/v1/oauth2/token"
    data = {
        "grant_type": "refresh_token",
        "refresh_token": EBAY_REFRESH_TOKEN
    }
    response = requests.post(url, headers=get_auth_headers(), data=data)
    if response.status_code == 200:
        _user_token = response.json().get("access_token")
        return _user_token
    else:
        raise Exception(f"Failed to get user token: {response.text}")

def make_request(method: str, endpoint: str, token_type: str = "app", is_media: bool = False, **kwargs) -> Dict[str, Any]:
    base = MEDIA_BASE_URL if is_media else BASE_URL
    url = f"{base}{endpoint}"
    
    try:
        token = get_user_token() if token_type == "user" else get_app_token()
    except Exception as e:
        return {"error": str(e)}
        
    headers = kwargs.pop("headers", {})
    headers["Authorization"] = f"Bearer {token}"
    
    try:
        response = requests.request(method, url, headers=headers, **kwargs)
        if response.status_code in (200, 201, 202):
            if response.text:
                try:
                    return response.json()
                except ValueError:
                    return {"response": response.text}
            return {"status": "success", "status_code": response.status_code}
        elif response.status_code == 204:
            return {"status": "success", "status_code": 204}
        else:
            try:
                return {"error": response.json(), "status_code": response.status_code}
            except ValueError:
                return {"error": response.text, "status_code": response.status_code}
    except Exception as e:
        return {"error": str(e)}

# Catalog (App token)
@mcp.tool()
def get_product(epid: str) -> Dict[str, Any]:
    return make_request("GET", f"/commerce/catalog/v1_beta/product/{epid}", token_type="app")

@mcp.tool()
def search_products(q: Optional[str] = None, category_ids: Optional[str] = None, limit: Optional[str] = None, offset: Optional[str] = None) -> Dict[str, Any]:
    params = {}
    if q: params["q"] = q
    if category_ids: params["category_ids"] = category_ids
    if limit: params["limit"] = limit
    if offset: params["offset"] = offset
    return make_request("GET", "/commerce/catalog/v1_beta/product_summary/search", token_type="app", params=params)

# Charity (App token)
@mcp.tool()
def get_charity_org(charity_org_id: str) -> Dict[str, Any]:
    return make_request("GET", f"/commerce/charity/v1/charity_org/{charity_org_id}", token_type="app")

@mcp.tool()
def get_charity_orgs(q: Optional[str] = None, limit: Optional[str] = None, offset: Optional[str] = None) -> Dict[str, Any]:
    params = {}
    if q: params["q"] = q
    if limit: params["limit"] = limit
    if offset: params["offset"] = offset
    return make_request("GET", "/commerce/charity/v1/charity_org", token_type="app", params=params)

# Identity (User token)
@mcp.tool()
def get_user() -> Dict[str, Any]:
    return make_request("GET", "/commerce/identity/v1/user", token_type="user")

# Media (User token, is_media=True)
@mcp.tool()
def create_document(data: Dict[str, Any]) -> Dict[str, Any]:
    return make_request("POST", "/commerce/media/v1/document", token_type="user", is_media=True, json=data)

@mcp.tool()
def create_document_from_url(data: Dict[str, Any]) -> Dict[str, Any]:
    return make_request("POST", "/commerce/media/v1/document/create_from_url", token_type="user", is_media=True, json=data)

@mcp.tool()
def get_document(document_id: str) -> Dict[str, Any]:
    return make_request("GET", f"/commerce/media/v1/document/{document_id}", token_type="user", is_media=True)

@mcp.tool()
def upload_document(document_id: str, file_data: str) -> Dict[str, Any]:
    return make_request("POST", f"/commerce/media/v1/document/{document_id}/upload", token_type="user", is_media=True, data=file_data)

@mcp.tool()
def create_image_from_file(data: Dict[str, Any]) -> Dict[str, Any]:
    return make_request("POST", "/commerce/media/v1/image/create_from_file", token_type="user", is_media=True, json=data)

@mcp.tool()
def create_image_from_url(data: Dict[str, Any]) -> Dict[str, Any]:
    return make_request("POST", "/commerce/media/v1/image/create_from_url", token_type="user", is_media=True, json=data)

@mcp.tool()
def get_image(image_id: str) -> Dict[str, Any]:
    return make_request("GET", f"/commerce/media/v1/image/{image_id}", token_type="user", is_media=True)

@mcp.tool()
def create_video(data: Dict[str, Any]) -> Dict[str, Any]:
    return make_request("POST", "/commerce/media/v1/video", token_type="user", is_media=True, json=data)

@mcp.tool()
def get_video(video_id: str) -> Dict[str, Any]:
    return make_request("GET", f"/commerce/media/v1/video/{video_id}", token_type="user", is_media=True)

@mcp.tool()
def upload_video(video_id: str, file_data: str) -> Dict[str, Any]:
    return make_request("POST", f"/commerce/media/v1/video/{video_id}/upload", token_type="user", is_media=True, data=file_data)

# Notification (User token)
@mcp.tool()
def get_notification_config() -> Dict[str, Any]:
    return make_request("GET", "/commerce/notification/v1/config", token_type="user")

@mcp.tool()
def update_notification_config(data: Dict[str, Any]) -> Dict[str, Any]:
    return make_request("PUT", "/commerce/notification/v1/config", token_type="user", json=data)

@mcp.tool()
def create_destination(data: Dict[str, Any]) -> Dict[str, Any]:
    return make_request("POST", "/commerce/notification/v1/destination", token_type="user", json=data)

@mcp.tool()
def delete_destination(destination_id: str) -> Dict[str, Any]:
    return make_request("DELETE", f"/commerce/notification/v1/destination/{destination_id}", token_type="user")

@mcp.tool()
def get_destination(destination_id: str) -> Dict[str, Any]:
    return make_request("GET", f"/commerce/notification/v1/destination/{destination_id}", token_type="user")

@mcp.tool()
def get_destinations() -> Dict[str, Any]:
    return make_request("GET", "/commerce/notification/v1/destination", token_type="user")

@mcp.tool()
def update_destination(destination_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
    return make_request("PUT", f"/commerce/notification/v1/destination/{destination_id}", token_type="user", json=data)

@mcp.tool()
def get_public_key(public_key_id: str) -> Dict[str, Any]:
    return make_request("GET", f"/commerce/notification/v1/public_key/{public_key_id}", token_type="user")

@mcp.tool()
def create_subscription(data: Dict[str, Any]) -> Dict[str, Any]:
    return make_request("POST", "/commerce/notification/v1/subscription", token_type="user", json=data)

@mcp.tool()
def create_subscription_filter(subscription_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
    return make_request("POST", f"/commerce/notification/v1/subscription/{subscription_id}/filter", token_type="user", json=data)

@mcp.tool()
def delete_subscription(subscription_id: str) -> Dict[str, Any]:
    return make_request("DELETE", f"/commerce/notification/v1/subscription/{subscription_id}", token_type="user")

@mcp.tool()
def delete_subscription_filter(subscription_id: str, filter_id: str) -> Dict[str, Any]:
    return make_request("DELETE", f"/commerce/notification/v1/subscription/{subscription_id}/filter/{filter_id}", token_type="user")

@mcp.tool()
def disable_subscription(subscription_id: str) -> Dict[str, Any]:
    return make_request("POST", f"/commerce/notification/v1/subscription/{subscription_id}/disable", token_type="user")

@mcp.tool()
def enable_subscription(subscription_id: str) -> Dict[str, Any]:
    return make_request("POST", f"/commerce/notification/v1/subscription/{subscription_id}/enable", token_type="user")

@mcp.tool()
def get_subscription(subscription_id: str) -> Dict[str, Any]:
    return make_request("GET", f"/commerce/notification/v1/subscription/{subscription_id}", token_type="user")

@mcp.tool()
def get_subscription_filter(subscription_id: str, filter_id: str) -> Dict[str, Any]:
    return make_request("GET", f"/commerce/notification/v1/subscription/{subscription_id}/filter/{filter_id}", token_type="user")

@mcp.tool()
def get_subscriptions() -> Dict[str, Any]:
    return make_request("GET", "/commerce/notification/v1/subscription", token_type="user")

@mcp.tool()
def test_subscription(subscription_id: str) -> Dict[str, Any]:
    return make_request("POST", f"/commerce/notification/v1/subscription/{subscription_id}/test", token_type="user")

@mcp.tool()
def update_subscription(subscription_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
    return make_request("PUT", f"/commerce/notification/v1/subscription/{subscription_id}", token_type="user", json=data)

@mcp.tool()
def get_topic(topic_id: str) -> Dict[str, Any]:
    return make_request("GET", f"/commerce/notification/v1/topic/{topic_id}", token_type="user")

@mcp.tool()
def get_topics() -> Dict[str, Any]:
    return make_request("GET", "/commerce/notification/v1/topic", token_type="user")

# Taxonomy (App token)
@mcp.tool()
def fetch_item_aspects(category_tree_id: str) -> Dict[str, Any]:
    return make_request("GET", f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/fetch_item_aspects", token_type="app")

@mcp.tool()
def get_category_subtree(category_tree_id: str, category_id: str) -> Dict[str, Any]:
    return make_request("GET", f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_category_subtree", token_type="app", params={"category_id": category_id})

@mcp.tool()
def get_category_suggestions(category_tree_id: str, q: str) -> Dict[str, Any]:
    return make_request("GET", f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_category_suggestions", token_type="app", params={"q": q})

@mcp.tool()
def get_category_tree(category_tree_id: str) -> Dict[str, Any]:
    return make_request("GET", f"/commerce/taxonomy/v1/category_tree/{category_tree_id}", token_type="app")

@mcp.tool()
def get_compatibility_properties(category_tree_id: str, category_id: str) -> Dict[str, Any]:
    return make_request("GET", f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_compatibility_properties", token_type="app", params={"category_id": category_id})

@mcp.tool()
def get_compatibility_property_values(category_tree_id: str, category_id: str, compatibility_property: str) -> Dict[str, Any]:
    return make_request("GET", f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_compatibility_property_values", token_type="app", params={"category_id": category_id, "compatibility_property": compatibility_property})

@mcp.tool()
def get_default_category_tree_id(marketplace_id: str) -> Dict[str, Any]:
    return make_request("GET", "/commerce/taxonomy/v1/get_default_category_tree_id", token_type="app", params={"marketplace_id": marketplace_id})

@mcp.tool()
def get_expired_categories(category_tree_id: str) -> Dict[str, Any]:
    return make_request("GET", f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_expired_categories", token_type="app")

@mcp.tool()
def get_item_aspects_for_category(category_tree_id: str, category_id: str) -> Dict[str, Any]:
    return make_request("GET", f"/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_item_aspects_for_category", token_type="app", params={"category_id": category_id})

# Translation (App token)
@mcp.tool()
def translate_language(data: Dict[str, Any]) -> Dict[str, Any]:
    return make_request("POST", "/commerce/translation/v1/language/translate", token_type="app", json=data)

if __name__ == "__main__":
    mcp.run()
