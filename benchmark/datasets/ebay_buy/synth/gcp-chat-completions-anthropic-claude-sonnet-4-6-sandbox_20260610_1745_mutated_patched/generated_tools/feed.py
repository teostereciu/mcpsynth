"""
eBay Buy Feed API tools.
Covers: item feed, item group feed, item priority feed, item snapshot feed.
Note: Feed files are returned as TSV_GZIP binary content. These tools return
the raw bytes as a base64-encoded string or metadata about the response.
"""

from typing import Optional
import base64
from mcp.server.fastmcp import FastMCP
from .auth import get_auth_headers, get_base_url


def _feed_request(url: str, params: dict, marketplace_id: str,
                  byte_range: str = "bytes=0-10485760") -> dict:
    """Internal helper for feed file downloads. Returns metadata + base64 content."""
    import requests
    headers = {
        **get_auth_headers(),
        "X-EBAY-C-MARKETPLACE-ID": marketplace_id,
        "Accept": "application/json,text/tab-separated-values",
        "Range": byte_range,
    }
    try:
        resp = requests.get(url, params=params, headers=headers, timeout=60)
        if resp.status_code in (200, 206):
            content_range = resp.headers.get("Content-Range", "")
            last_modified = resp.headers.get("Last-Modified", "")
            content_b64 = base64.b64encode(resp.content).decode("utf-8")
            return {
                "status_code": resp.status_code,
                "content_range": content_range,
                "last_modified": last_modified,
                "content_type": resp.headers.get("Content-Type", ""),
                "content_length_bytes": len(resp.content),
                "content_base64": content_b64,
                "note": (
                    "Content is a TSV_GZIP file encoded as base64. "
                    "Decode and decompress to read tab-separated item data."
                ),
            }
        # Error responses are JSON
        try:
            return {"error": resp.json(), "status_code": resp.status_code}
        except Exception:
            return {"error": resp.text, "status_code": resp.status_code}
    except Exception as e:
        return {"error": str(e)}


def register_feed_tools(mcp: FastMCP) -> None:

    @mcp.tool()
    def get_item_feed(
        feed_scope: str,
        category_id: str,
        date: Optional[str] = None,
        byte_range: str = "bytes=0-10485760",
        marketplace_id: str = "EBAY_US",
    ) -> dict:
        """Download an eBay item feed file (TSV_GZIP) for a category.
        Returns newly listed items (daily) or all active items (weekly bootstrap).
        The response content is base64-encoded gzip data.

        Args:
            feed_scope: 'NEWLY_LISTED' (daily) or 'ALL_ACTIVE' (weekly bootstrap).
            category_id: Top-level eBay category ID (e.g. '625' for Cameras & Photo).
            date: Date in yyyyMMdd format (required for NEWLY_LISTED, up to 14 days ago).
            byte_range: Byte range for chunked download (default: first 10MB).
                        Format: 'bytes=start-end' (e.g. 'bytes=0-10485760').
            marketplace_id: eBay marketplace ID (default EBAY_US).
        """
        params = {"feed_scope": feed_scope, "category_id": category_id}
        if date:
            params["date"] = date
        url = f"{get_base_url()}/buy/feed/v1_beta/item"
        return _feed_request(url, params, marketplace_id, byte_range)

    @mcp.tool()
    def get_item_group_feed(
        feed_scope: str,
        category_id: str,
        date: Optional[str] = None,
        byte_range: str = "bytes=0-10485760",
        marketplace_id: str = "EBAY_US",
    ) -> dict:
        """Download an eBay item group feed file (TSV_GZIP) for a category.
        Item groups contain variations (size, color, etc.) of a parent item.
        The response content is base64-encoded gzip data.

        Args:
            feed_scope: 'NEWLY_LISTED' (daily) or 'ALL_ACTIVE' (weekly bootstrap).
            category_id: Top-level eBay category ID (e.g. '625' for Cameras & Photo).
            date: Date in yyyyMMdd format (required for NEWLY_LISTED, 3-14 days ago).
            byte_range: Byte range for chunked download (default: first 10MB).
                        Format: 'bytes=start-end'.
            marketplace_id: eBay marketplace ID (default EBAY_US).
        """
        params = {"feed_scope": feed_scope, "category_id": category_id}
        if date:
            params["date"] = date
        url = f"{get_base_url()}/buy/feed/v1_beta/item_group"
        return _feed_request(url, params, marketplace_id, byte_range)

    @mcp.tool()
    def get_item_priority_feed(
        category_id: str,
        date: str,
        byte_range: str = "bytes=0-10485760",
        marketplace_id: str = "EBAY_US",
    ) -> dict:
        """Download an eBay item priority feed file (TSV_GZIP) tracking campaign changes.
        Shows items added/removed from priority listing campaigns on a given date.
        The response content is base64-encoded gzip data.

        Args:
            category_id: Top-level eBay category ID (e.g. '625' for Cameras & Photo).
            date: Date in yyyyMMdd format (up to 14 days in the past).
            byte_range: Byte range for chunked download (default: first 10MB).
                        Format: 'bytes=start-end'.
            marketplace_id: eBay marketplace ID (default EBAY_US).
        """
        params = {"category_id": category_id, "date": date}
        url = f"{get_base_url()}/buy/feed/v1_beta/item_priority"
        return _feed_request(url, params, marketplace_id, byte_range)

    @mcp.tool()
    def get_item_snapshot_feed(
        category_id: str,
        snapshot_date: str,
        byte_range: str = "bytes=0-10485760",
        marketplace_id: str = "EBAY_US",
    ) -> dict:
        """Download an eBay hourly item snapshot feed file (TSV_GZIP).
        Contains all items that changed within a specific hour (price, quantity, etc.).
        The response content is base64-encoded gzip data.

        Args:
            category_id: Top-level eBay category ID (e.g. '625' for Cameras & Photo).
            snapshot_date: UTC datetime in format yyyy-MM-ddThh:00:00.000Z
                           (e.g. '2018-08-30T08:00:00.000Z'). File available 2 hours
                           after the specified hour.
            byte_range: Byte range for chunked download (default: first 10MB).
                        Format: 'bytes=start-end'.
            marketplace_id: eBay marketplace ID (default EBAY_US).
        """
        params = {"category_id": category_id, "snapshot_date": snapshot_date}
        url = f"{get_base_url()}/buy/feed/v1_beta/item_snapshot"
        return _feed_request(url, params, marketplace_id, byte_range)
