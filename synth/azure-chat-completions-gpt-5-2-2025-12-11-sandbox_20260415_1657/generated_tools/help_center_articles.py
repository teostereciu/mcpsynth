from typing import Any, Dict, Optional

from ._client import get_client


def hc_list_articles(
    label_names: Optional[str] = None,
    sort_by: Optional[str] = None,
    sort_order: Optional[str] = None,
    start_time: Optional[int] = None,
    page: Optional[int] = None,
    per_page: Optional[int] = None,
) -> Dict[str, Any]:
    """GET /api/v2/help_center/articles"""
    client = get_client()
    params: Dict[str, Any] = {}
    if label_names is not None:
        params["label_names"] = label_names
    if sort_by is not None:
        params["sort_by"] = sort_by
    if sort_order is not None:
        params["sort_order"] = sort_order
    if start_time is not None:
        params["start_time"] = start_time
    if page is not None:
        params["page"] = page
    if per_page is not None:
        params["per_page"] = per_page
    return client.request("GET", f"{client.base_help_center}/articles", params=params)  # type: ignore


def hc_show_article(article_id: int) -> Dict[str, Any]:
    """GET /api/v2/help_center/articles/{article_id}"""
    client = get_client()
    return client.request("GET", f"{client.base_help_center}/articles/{article_id}")  # type: ignore


def hc_list_articles_in_section(section_id: int, locale: Optional[str] = None) -> Dict[str, Any]:
    """GET /api/v2/help_center/{locale}/sections/{section_id}/articles OR /api/v2/help_center/sections/{section_id}/articles"""
    client = get_client()
    if locale:
        url = f"{client.base_help_center}/{locale}/sections/{section_id}/articles"
    else:
        url = f"{client.base_help_center}/sections/{section_id}/articles"
    return client.request("GET", url)  # type: ignore


def hc_create_article_in_section(section_id: int, article: Dict[str, Any], locale: Optional[str] = None) -> Dict[str, Any]:
    """POST /api/v2/help_center/sections/{section_id}/articles

    Body: {"article": {...}}
    """
    client = get_client()
    if locale:
        url = f"{client.base_help_center}/{locale}/sections/{section_id}/articles"
    else:
        url = f"{client.base_help_center}/sections/{section_id}/articles"
    return client.request("POST", url, json={"article": article})  # type: ignore


def hc_update_article(article_id: int, article: Dict[str, Any], locale: Optional[str] = None) -> Dict[str, Any]:
    """PUT /api/v2/help_center/articles/{article_id} (or locale variant)

    Body: {"article": {...}}
    """
    client = get_client()
    if locale:
        url = f"{client.base_help_center}/{locale}/articles/{article_id}"
    else:
        url = f"{client.base_help_center}/articles/{article_id}"
    return client.request("PUT", url, json={"article": article})  # type: ignore


def hc_archive_article(article_id: int, locale: Optional[str] = None) -> Dict[str, Any]:
    """DELETE /api/v2/help_center/articles/{article_id} (or locale variant)"""
    client = get_client()
    if locale:
        url = f"{client.base_help_center}/{locale}/articles/{article_id}"
    else:
        url = f"{client.base_help_center}/articles/{article_id}"
    return client.request("DELETE", url)  # type: ignore
