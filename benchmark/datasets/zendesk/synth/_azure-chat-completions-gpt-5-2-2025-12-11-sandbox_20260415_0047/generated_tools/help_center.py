"""Help Center API tools (Guide).

Note: Help Center endpoints are still under /api/v2, but prefixed with /help_center.
"""

from __future__ import annotations

from typing import Any, Dict, Optional

from .http import zendesk_delete, zendesk_get, zendesk_post, zendesk_put


def _unwrap(obj: Dict[str, Any], key: str) -> Dict[str, Any]:
    if not isinstance(obj, dict):
        return {"error": "invalid_response", "description": "Expected dict response"}
    if "error" in obj and "status" in obj:
        return obj
    return obj.get(key) or obj


def hc_articles_list(per_page: int = 25, page: Optional[int] = None, sort_by: Optional[str] = None, sort_order: Optional[str] = None, label_names: Optional[str] = None) -> Dict[str, Any]:
    """List Help Center articles.

    Maps to GET /api/v2/help_center/articles
    """
    params: Dict[str, Any] = {"per_page": per_page}
    if page is not None:
        params["page"] = page
    if sort_by:
        params["sort_by"] = sort_by
    if sort_order:
        params["sort_order"] = sort_order
    if label_names:
        params["label_names"] = label_names
    return zendesk_get("/help_center/articles", params=params)


def hc_articles_show(article_id: int) -> Dict[str, Any]:
    """Show a Help Center article.

    Maps to GET /api/v2/help_center/articles/{id}
    """
    return _unwrap(zendesk_get(f"/help_center/articles/{article_id}"), "article")


def hc_articles_create_in_section(section_id: int, title: str, body: str, locale: str = "en-us", additional_fields: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Create an article in a section.

    Maps to POST /api/v2/help_center/sections/{section_id}/articles
    """
    article: Dict[str, Any] = {"title": title, "body": body, "locale": locale}
    if additional_fields:
        article.update(additional_fields)
    return _unwrap(zendesk_post(f"/help_center/sections/{section_id}/articles", {"article": article}), "article")


def hc_articles_update(article_id: int, fields: Dict[str, Any]) -> Dict[str, Any]:
    """Update an article.

    Maps to PUT /api/v2/help_center/articles/{id}
    """
    return _unwrap(zendesk_put(f"/help_center/articles/{article_id}", {"article": fields}), "article")


def hc_articles_archive(article_id: int) -> Dict[str, Any]:
    """Archive (delete) an article.

    Maps to DELETE /api/v2/help_center/articles/{id}
    """
    return zendesk_delete(f"/help_center/articles/{article_id}")


def hc_search(query: str, per_page: int = 25, page: Optional[int] = None, locale: Optional[str] = None) -> Dict[str, Any]:
    """Search Help Center articles.

    Maps to GET /api/v2/help_center/articles/search?query=...

    Note: Zendesk also documents /api/v2/guide/search (unified search). See hc_unified_search.
    """
    params: Dict[str, Any] = {"query": query, "per_page": per_page}
    if page is not None:
        params["page"] = page
    if locale:
        params["locale"] = locale
    return zendesk_get("/help_center/articles/search", params=params)


def hc_unified_search(filter_locales: str, query: Optional[str] = None, page_after: Optional[str] = None, page_size: Optional[int] = None, filters: Optional[Dict[str, str]] = None) -> Dict[str, Any]:
    """Unified Help Center search across articles, posts, and external content.

    Maps to GET /api/v2/guide/search

    Args:
      filter_locales: required, comma-separated locales (e.g., "en-us,en-gb")
      query: optional search text
      page_after: cursor token for next page
      page_size: max 50
      filters: optional mapping for filter[...] params, e.g. {"brand_ids": "73,67", "content_types": "ARTICLE"}
    """
    params: Dict[str, Any] = {"filter[locales]": filter_locales}
    if query:
        params["query"] = query
    if page_after:
        params["page[after]"] = page_after
    if page_size is not None:
        params["page[size]"] = page_size
    if filters:
        for k, v in filters.items():
            params[f"filter[{k}]"] = v
    return zendesk_get("/guide/search", params=params)
