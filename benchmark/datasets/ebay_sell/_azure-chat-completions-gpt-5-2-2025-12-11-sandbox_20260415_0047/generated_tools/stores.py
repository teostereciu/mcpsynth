from __future__ import annotations

from typing import Any, Dict, Optional

from .http import request_json

API_ROOT = "/sell/stores/v1"
SCOPE = "https://api.ebay.com/oauth/api_scope/sell.stores"


def register(mcp):
    @mcp.tool()
    def stores_get_store() -> Dict[str, Any]:
        """GET /store - Get store."""
        return request_json("GET", API_ROOT, "/store", scope=SCOPE)

    @mcp.tool()
    def stores_get_store_categories() -> Dict[str, Any]:
        """GET /store/categories - Get store categories."""
        return request_json("GET", API_ROOT, "/store/categories", scope=SCOPE)

    @mcp.tool()
    def stores_add_store_category(payload: Dict[str, Any]) -> Dict[str, Any]:
        """POST /store/categories - Add store category."""
        return request_json(
            "POST",
            API_ROOT,
            "/store/categories",
            scope=SCOPE,
            headers={"Content-Type": "application/json"},
            json_body=payload,
        )

    @mcp.tool()
    def stores_delete_store_category(category_id: str) -> Dict[str, Any]:
        """DELETE /store/categories/{category_id} - Delete store category."""
        return request_json("DELETE", API_ROOT, f"/store/categories/{category_id}", scope=SCOPE)

    @mcp.tool()
    def stores_move_store_category(payload: Dict[str, Any]) -> Dict[str, Any]:
        """POST /store/categories/move_category - Move store category."""
        return request_json(
            "POST",
            API_ROOT,
            "/store/categories/move_category",
            scope=SCOPE,
            headers={"Content-Type": "application/json"},
            json_body=payload,
        )

    @mcp.tool()
    def stores_rename_store_category(category_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """PUT /store/categories/{category_id} - Rename store category."""
        return request_json(
            "PUT",
            API_ROOT,
            f"/store/categories/{category_id}",
            scope=SCOPE,
            headers={"Content-Type": "application/json"},
            json_body=payload,
        )

    @mcp.tool()
    def stores_get_store_tasks(*, limit: Optional[int] = None, offset: Optional[int] = None) -> Dict[str, Any]:
        """GET /store/tasks - Get store tasks."""
        params: Dict[str, Any] = {}
        if limit is not None:
            params["limit"] = str(limit)
        if offset is not None:
            params["offset"] = str(offset)
        return request_json("GET", API_ROOT, "/store/tasks", scope=SCOPE, params=params or None)

    @mcp.tool()
    def stores_get_store_task(task_id: str) -> Dict[str, Any]:
        """GET /store/tasks/{task_id} - Get store task."""
        return request_json("GET", API_ROOT, f"/store/tasks/{task_id}", scope=SCOPE)
