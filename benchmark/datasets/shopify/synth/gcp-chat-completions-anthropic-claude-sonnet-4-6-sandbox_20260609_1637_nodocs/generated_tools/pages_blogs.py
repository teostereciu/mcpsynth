"""Shopify Admin REST API — Pages, Blogs, Articles tools."""

import os, requests
from mcp.server.fastmcp import FastMCP

def _session():
    token = os.environ["SHOPIFY_ACCESS_TOKEN"]
    store = os.environ["SHOPIFY_STORE_URL"]
    base  = f"https://{store}/admin/api/2026-01"
    s = requests.Session()
    s.headers.update({"X-Shopify-Access-Token": token, "Content-Type": "application/json"})
    return s, base

def register(mcp: FastMCP):

    # ── Pages ─────────────────────────────────────────────────────────────────

    @mcp.tool()
    def list_pages(limit: int = 50, published_status: str = "any") -> dict:
        """List store pages. published_status: published|unpublished|any."""
        s, base = _session()
        r = s.get(f"{base}/pages.json",
                  params={"limit": limit, "published_status": published_status})
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    @mcp.tool()
    def get_page(page_id: str) -> dict:
        """Get a page by ID."""
        s, base = _session()
        r = s.get(f"{base}/pages/{page_id}.json")
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    @mcp.tool()
    def create_page(title: str, body_html: str = "",
                    published: bool = False) -> dict:
        """Create a new page."""
        s, base = _session()
        data: dict = {"title": title, "published": published}
        if body_html:
            data["body_html"] = body_html
        r = s.post(f"{base}/pages.json", json={"page": data})
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    @mcp.tool()
    def update_page(page_id: str, title: str = "", body_html: str = "",
                    published: bool = None) -> dict:
        """Update a page."""
        s, base = _session()
        data: dict = {}
        if title:              data["title"]     = title
        if body_html:          data["body_html"] = body_html
        if published is not None: data["published"] = published
        r = s.put(f"{base}/pages/{page_id}.json", json={"page": data})
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    @mcp.tool()
    def delete_page(page_id: str) -> dict:
        """Delete a page."""
        s, base = _session()
        r = s.delete(f"{base}/pages/{page_id}.json")
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return {"deleted": True, "page_id": page_id}

    # ── Blogs ─────────────────────────────────────────────────────────────────

    @mcp.tool()
    def list_blogs(limit: int = 50) -> dict:
        """List all blogs."""
        s, base = _session()
        r = s.get(f"{base}/blogs.json", params={"limit": limit})
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    @mcp.tool()
    def get_blog(blog_id: str) -> dict:
        """Get a blog by ID."""
        s, base = _session()
        r = s.get(f"{base}/blogs/{blog_id}.json")
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    @mcp.tool()
    def create_blog(title: str, commentable: str = "no") -> dict:
        """Create a blog. commentable: no|moderate|yes."""
        s, base = _session()
        r = s.post(f"{base}/blogs.json",
                   json={"blog": {"title": title, "commentable": commentable}})
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    @mcp.tool()
    def delete_blog(blog_id: str) -> dict:
        """Delete a blog."""
        s, base = _session()
        r = s.delete(f"{base}/blogs/{blog_id}.json")
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return {"deleted": True, "blog_id": blog_id}

    # ── Articles ──────────────────────────────────────────────────────────────

    @mcp.tool()
    def list_articles(blog_id: str, limit: int = 50,
                      published_status: str = "any") -> dict:
        """List articles in a blog."""
        s, base = _session()
        r = s.get(f"{base}/blogs/{blog_id}/articles.json",
                  params={"limit": limit, "published_status": published_status})
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    @mcp.tool()
    def get_article(blog_id: str, article_id: str) -> dict:
        """Get an article by ID."""
        s, base = _session()
        r = s.get(f"{base}/blogs/{blog_id}/articles/{article_id}.json")
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    @mcp.tool()
    def create_article(blog_id: str, title: str, body_html: str = "",
                       author: str = "", tags: str = "",
                       published: bool = False) -> dict:
        """Create an article in a blog."""
        s, base = _session()
        data: dict = {"title": title, "published": published}
        if body_html: data["body_html"] = body_html
        if author:    data["author"]    = author
        if tags:      data["tags"]      = tags
        r = s.post(f"{base}/blogs/{blog_id}/articles.json", json={"article": data})
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    @mcp.tool()
    def update_article(blog_id: str, article_id: str, title: str = "",
                       body_html: str = "", tags: str = "",
                       published: bool = None) -> dict:
        """Update a blog article."""
        s, base = _session()
        data: dict = {}
        if title:              data["title"]     = title
        if body_html:          data["body_html"] = body_html
        if tags:               data["tags"]      = tags
        if published is not None: data["published"] = published
        r = s.put(f"{base}/blogs/{blog_id}/articles/{article_id}.json",
                  json={"article": data})
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return r.json()

    @mcp.tool()
    def delete_article(blog_id: str, article_id: str) -> dict:
        """Delete a blog article."""
        s, base = _session()
        r = s.delete(f"{base}/blogs/{blog_id}/articles/{article_id}.json")
        if not r.ok:
            return {"error": r.text, "status_code": r.status_code}
        return {"deleted": True, "article_id": article_id}
