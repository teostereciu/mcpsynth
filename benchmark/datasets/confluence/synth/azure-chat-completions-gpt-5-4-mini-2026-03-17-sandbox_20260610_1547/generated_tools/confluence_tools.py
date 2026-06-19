from __future__ import annotations

from typing import Any, Dict, Optional

from generated_tools.confluence_client import get_client


client = get_client()


def _req(method: str, path: str, params: Optional[Dict[str, Any]] = None, json_body: Any = None):
    return client.request(method, path, params=params, json_body=json_body)


def list_spaces(**kwargs):
    return _req("GET", "/api/v2/spaces", params=kwargs)


def get_space(space_id: str, **kwargs):
    return _req("GET", f"/api/v2/spaces/{space_id}", params=kwargs)


def create_space(payload: Dict[str, Any]):
    return _req("POST", "/api/v2/spaces", json_body=payload)


def list_pages(**kwargs):
    return _req("GET", "/api/v2/pages", params=kwargs)


def get_page(page_id: str, **kwargs):
    return _req("GET", f"/api/v2/pages/{page_id}", params=kwargs)


def create_page(payload: Dict[str, Any], **kwargs):
    return _req("POST", "/api/v2/pages", params=kwargs, json_body=payload)


def update_page(page_id: str, payload: Dict[str, Any]):
    return _req("PUT", f"/api/v2/pages/{page_id}", json_body=payload)


def delete_page(page_id: str, **kwargs):
    return _req("DELETE", f"/api/v2/pages/{page_id}", params=kwargs)


def list_blog_posts(**kwargs):
    return _req("GET", "/api/v2/blogposts", params=kwargs)


def create_blog_post(payload: Dict[str, Any], **kwargs):
    return _req("POST", "/api/v2/blogposts", params=kwargs, json_body=payload)


def get_blog_post(blog_post_id: str, **kwargs):
    return _req("GET", f"/api/v2/blogposts/{blog_post_id}", params=kwargs)


def update_blog_post(blog_post_id: str, payload: Dict[str, Any]):
    return _req("PUT", f"/api/v2/blogposts/{blog_post_id}", json_body=payload)


def delete_blog_post(blog_post_id: str, **kwargs):
    return _req("DELETE", f"/api/v2/blogposts/{blog_post_id}", params=kwargs)
