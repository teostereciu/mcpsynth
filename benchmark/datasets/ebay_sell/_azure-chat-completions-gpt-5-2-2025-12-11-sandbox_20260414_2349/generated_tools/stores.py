from typing import Any, Dict

from . import client as _shared
from .client import SCOPE_STORES
from . import mcp

API = "/sell/stores/v1"


@mcp.tool()
def stores_get_store(*, marketplace_id: str = "EBAY_US") -> Any:
    """GET /store"""
    return _shared.client.request(
        "GET",
        API,
        "/store",
        scope=SCOPE_STORES,
        marketplace_id=marketplace_id,
    )


@mcp.tool()
def stores_get_store_categories(*, marketplace_id: str = "EBAY_US") -> Any:
    """GET /store/category"""
    return _shared.client.request(
        "GET",
        API,
        "/store/category",
        scope=SCOPE_STORES,
        marketplace_id=marketplace_id,
    )


@mcp.tool()
def stores_add_store_category(
    category: Dict[str, Any],
    *,
    marketplace_id: str = "EBAY_US",
) -> Any:
    """POST /store/category"""
    return _shared.client.request(
        "POST",
        API,
        "/store/category",
        scope=SCOPE_STORES,
        marketplace_id=marketplace_id,
        json=category,
    )


@mcp.tool()
def stores_rename_store_category(
    category_id: str,
    request: Dict[str, Any],
    *,
    marketplace_id: str = "EBAY_US",
) -> Any:
    """POST /store/category/{categoryId}/rename"""
    return _shared.client.request(
        "POST",
        API,
        f"/store/category/{category_id}/rename",
        scope=SCOPE_STORES,
        marketplace_id=marketplace_id,
        json=request,
    )


@mcp.tool()
def stores_move_store_category(
    category_id: str,
    request: Dict[str, Any],
    *,
    marketplace_id: str = "EBAY_US",
) -> Any:
    """POST /store/category/{categoryId}/move"""
    return _shared.client.request(
        "POST",
        API,
        f"/store/category/{category_id}/move",
        scope=SCOPE_STORES,
        marketplace_id=marketplace_id,
        json=request,
    )


@mcp.tool()
def stores_delete_store_category(category_id: str, *, marketplace_id: str = "EBAY_US") -> Any:
    """DELETE /store/category/{categoryId}"""
    return _shared.client.request(
        "DELETE",
        API,
        f"/store/category/{category_id}",
        scope=SCOPE_STORES,
        marketplace_id=marketplace_id,
    )


@mcp.tool()
def stores_get_store_tasks(*, marketplace_id: str = "EBAY_US") -> Any:
    """GET /store/task"""
    return _shared.client.request(
        "GET",
        API,
        "/store/task",
        scope=SCOPE_STORES,
        marketplace_id=marketplace_id,
    )


@mcp.tool()
def stores_get_store_task(task_id: str, *, marketplace_id: str = "EBAY_US") -> Any:
    """GET /store/task/{taskId}"""
    return _shared.client.request(
        "GET",
        API,
        f"/store/task/{task_id}",
        scope=SCOPE_STORES,
        marketplace_id=marketplace_id,
    )
