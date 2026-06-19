"""
Confluence MCP Server Implementation

This module implements an MCP (Model Context Protocol) server for Confluence Cloud,
providing endpoints for common Confluence operations including content management,
space operations, user management, and more.

Based on Confluence Cloud REST API documentation:
https://developer.atlassian.com/cloud/confluence/rest/
"""

import os
import logging
from typing import Optional, Dict, Any, List
from fastapi import FastAPI, HTTPException, Header, Query
from pydantic import BaseModel, Field
import httpx
from contextlib import asynccontextmanager

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# API Configuration
BASE_URL = os.getenv("CONFLUENCE_BASE_URL", "https://api.atlassian.com/ex/confluence")
API_VERSION = os.getenv("API_VERSION", "2")

# MCP Server Configuration
MCP_SERVER_NAME = "confluence-mcp-server"
MCP_SERVER_VERSION = "1.0.0"


# Pydantic Models for Request/Response Bodies

class ContentResponse(BaseModel):
    id: str
    type: str
    status: str
    title: str
    space_id: str = Field(alias="spaceId")
    body: Optional[Dict[str, Any]] = None
    _links: Optional[Dict[str, Any]] = None


class SpaceResponse(BaseModel):
    id: str
    key: str
    name: str
    type: str
    status: str
    author_id: str = Field(alias="authorId")
    created_at: str = Field(alias="createdAt")
    homepage_id: str = Field(alias="homepageId")
    description: Optional[Dict[str, Any]] = None
    icon: Optional[Dict[str, Any]] = None
    _links: Optional[Dict[str, Any]] = None


class PageRequest(BaseModel):
    space_id: str = Field(alias="spaceId")
    status: str = "current"
    title: str
    parent_id: Optional[str] = Field(default=None, alias="parentId")
    body: Optional[Dict[str, Any]] = None
    subtype: Optional[str] = None


class PageUpdateRequest(BaseModel):
    id: str
    status: str
    title: str
    space_id: str = Field(alias="spaceId")
    body: Dict[str, Any]
    version: Dict[str, Any]


class SearchResponse(BaseModel):
    results: List[ContentResponse]
    start: int
    limit: int
    size: int
    total_size: int = Field(alias="totalSize")
    cql_query: str = Field(alias="cqlQuery")
    _links: Optional[Dict[str, Any]] = None


class UserResponse(BaseModel):
    account_id: str = Field(alias="accountId")
    account_type: str = Field(alias="accountType")
    email: Optional[str] = None
    display_name: str = Field(alias="displayName")
    public_name: str = Field(alias="publicName")
    profile_picture: Optional[Dict[str, Any]] = Field(alias="profilePicture", default=None)
    time_zone: Optional[str] = Field(alias="timeZone", default=None)
    is_external_collaborator: bool = Field(alias="isExternalCollaborator", default=False)
    is_guest: bool = Field(alias="isGuest", default=False)


class SearchRequest(BaseModel):
    cql: str
    cqlcontext: Optional[str] = None
    cursor: Optional[str] = None
    next: Optional[bool] = None
    prev: Optional[bool] = None
    limit: Optional[int] = 25
    start: Optional[int] = 0
    include_archived_spaces: Optional[bool] = None
    exclude_current_spaces: Optional[bool] = None
    excerpt: Optional[str] = None


class ContentExpandParams(BaseModel):
    expand: Optional[str] = None
    status: Optional[str] = None
    version: Optional[int] = None
    include_labels: Optional[bool] = None
    include_properties: Optional[bool] = None
    include_operations: Optional[bool] = None
    include_likes: Optional[bool] = None
    include_versions: Optional[bool] = None


# MCP Server State
class MCPState:
    def __init__(self):
        self.http_client: Optional[httpx.AsyncClient] = None
        self.access_token: Optional[str] = None
        self.host: str = BASE_URL

    async def initialize(self, access_token: str):
        """Initialize the MCP server with access token."""
        self.access_token = access_token
        self.http_client = httpx.AsyncClient(
            headers={
                "Authorization": f"Bearer {access_token}",
                "Accept": "application/json",
                "Content-Type": "application/json",
            },
            timeout=30.0
        )
        logger.info("MCP server initialized successfully")

    async def close(self):
        """Close the MCP server."""
        if self.http_client:
            await self.http_client.aclose()
            logger.info("MCP server closed")


# Create FastAPI app
state = MCPState()

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan manager."""
    access_token = os.getenv("CONFLUENCE_ACCESS_TOKEN")
    if access_token:
        await state.initialize(access_token)
    yield
    await state.close()


app = FastAPI(
    title=MCP_SERVER_NAME,
    description="MCP Server for Confluence Cloud API",
    version=MCP_SERVER_VERSION,
    lifespan=lifespan
)


# Health Check Endpoint
@app.get("/health", tags=["Health"])
async def health_check():
    """Health check endpoint for MCP server."""
    return {"status": "healthy", "server": MCP_SERVER_NAME, "version": MCP_SERVER_VERSION}


# Content Endpoints

@app.get("/wiki/api/v2/pages", response_model=List[ContentResponse], tags=["Pages"])
async def get_pages(
    limit: int = Query(25, description="Maximum number of results"),
    cursor: Optional[str] = Query(None, description="Cursor for pagination"),
    space_id: Optional[List[str]] = Query(None, alias="space-id", description="Filter by space ID"),
    status: Optional[List[str]] = Query(None, description="Filter by status"),
    title: Optional[str] = Query(None, description="Filter by title"),
    sort: Optional[str] = Query(None, description="Sort order"),
):
    """Get all pages."""
    if not state.http_client:
        raise HTTPException(status_code=500, detail="Server not initialized")
    
    params = {
        "limit": limit,
        "cursor": cursor,
        "space-id": space_id,
        "status": status,
        "title": title,
        "sort": sort,
    }
    
    try:
        response = await state.http_client.get(f"{state.host}/wiki/api/v2/pages", params=params)
        response.raise_for_status()
        return response.json().get("results", [])
    except httpx.HTTPStatusError as e:
        logger.error(f"HTTP error: {e}")
        raise HTTPException(status_code=e.response.status_code, detail=str(e))


@app.post("/wiki/api/v2/pages", response_model=ContentResponse, tags=["Pages"])
async def create_page(page: PageRequest):
    """Create a new page."""
    if not state.http_client:
        raise HTTPException(status_code=500, detail="Server not initialized")
    
    try:
        response = await state.http_client.post(
            f"{state.host}/wiki/api/v2/pages",
            json=page.dict(exclude_none=True, by_alias=True)
        )
        response.raise_for_status()
        return response.json()
    except httpx.HTTPStatusError as e:
        logger.error(f"HTTP error: {e}")
        raise HTTPException(status_code=e.response.status_code, detail=str(e))


@app.get("/wiki/api/v2/pages/{page_id}", response_model=ContentResponse, tags=["Pages"])
async def get_page(
    page_id: str,
    body_format: Optional[str] = Query(None, alias="body-format"),
    get_draft: Optional[bool] = Query(None, alias="get-draft"),
    include_labels: Optional[bool] = Query(None, alias="include-labels"),
    include_properties: Optional[bool] = Query(None, alias="include-properties"),
):
    """Get a specific page by ID."""
    if not state.http_client:
        raise HTTPException(status_code=500, detail="Server not initialized")
    
    params = {
        "body-format": body_format,
        "get-draft": get_draft,
        "include-labels": include_labels,
        "include-properties": include_properties,
    }
    
    try:
        response = await state.http_client.get(
            f"{state.host}/wiki/api/v2/pages/{page_id}",
            params={k: v for k, v in params.items() if v is not None}
        )
        response.raise_for_status()
        return response.json()
    except httpx.HTTPStatusError as e:
        logger.error(f"HTTP error: {e}")
        raise HTTPException(status_code=e.response.status_code, detail=str(e))


@app.put("/wiki/api/v2/pages/{page_id}", response_model=ContentResponse, tags=["Pages"])
async def update_page(page_id: str, page: PageUpdateRequest):
    """Update an existing page."""
    if not state.http_client:
        raise HTTPException(status_code=500, detail="Server not initialized")
    
    try:
        response = await state.http_client.put(
            f"{state.host}/wiki/api/v2/pages/{page_id}",
            json=page.dict(exclude_none=True, by_alias=True)
        )
        response.raise_for_status()
        return response.json()
    except httpx.HTTPStatusError as e:
        logger.error(f"HTTP error: {e}")
        raise HTTPException(status_code=e.response.status_code, detail=str(e))


@app.delete("/wiki/api/v2/pages/{page_id}", status_code=204, tags=["Pages"])
async def delete_page(page_id: str, purge: Optional[bool] = Query(None), draft: Optional[bool] = Query(None)):
    """Delete a page."""
    if not state.http_client:
        raise HTTPException(status_code=500, detail="Server not initialized")
    
    params = {
        "purge": purge,
        "draft": draft,
    }
    
    try:
        response = await state.http_client.delete(
            f"{state.host}/wiki/api/v2/pages/{page_id}",
            params={k: v for k, v in params.items() if v is not None}
        )
        response.raise_for_status()
        return None
    except httpx.HTTPStatusError as e:
        logger.error(f"HTTP error: {e}")
        raise HTTPException(status_code=e.response.status_code, detail=str(e))


# Space Endpoints

@app.get("/wiki/api/v2/spaces", response_model=List[SpaceResponse], tags=["Spaces"])
async def get_spaces(
    limit: int = Query(25, description="Maximum number of results"),
    cursor: Optional[str] = Query(None, description="Cursor for pagination"),
    keys: Optional[List[str]] = Query(None, description="Filter by space keys"),
    type: Optional[str] = Query(None, description="Filter by space type"),
    status: Optional[str] = Query(None, description="Filter by status"),
):
    """Get all spaces."""
    if not state.http_client:
        raise HTTPException(status_code=500, detail="Server not initialized")
    
    params = {
        "limit": limit,
        "cursor": cursor,
        "keys": keys,
        "type": type,
        "status": status,
    }
    
    try:
        response = await state.http_client.get(f"{state.host}/wiki/api/v2/spaces", params=params)
        response.raise_for_status()
        return response.json().get("results", [])
    except httpx.HTTPStatusError as e:
        logger.error(f"HTTP error: {e}")
        raise HTTPException(status_code=e.response.status_code, detail=str(e))


@app.post("/wiki/api/v2/spaces", response_model=SpaceResponse, tags=["Spaces"])
async def create_space(name: str, key: str, alias: Optional[str] = None, description: Optional[Dict[str, Any]] = None):
    """Create a new space."""
    if not state.http_client:
        raise HTTPException(status_code=500, detail="Server not initialized")
    
    payload = {
        "name": name,
        "key": key,
        "alias": alias,
        "description": description,
    }
    
    try:
        response = await state.http_client.post(
            f"{state.host}/wiki/api/v2/spaces",
            json={k: v for k, v in payload.items() if v is not None}
        )
        response.raise_for_status()
        return response.json()
    except httpx.HTTPStatusError as e:
        logger.error(f"HTTP error: {e}")
        raise HTTPException(status_code=e.response.status_code, detail=str(e))


@app.get("/wiki/api/v2/spaces/{space_id}", response_model=SpaceResponse, tags=["Spaces"])
async def get_space(space_id: str):
    """Get a specific space by ID."""
    if not state.http_client:
        raise HTTPException(status_code=500, detail="Server not initialized")
    
    try:
        response = await state.http_client.get(f"{state.host}/wiki/api/v2/spaces/{space_id}")
        response.raise_for_status()
        return response.json()
    except httpx.HTTPStatusError as e:
        logger.error(f"HTTP error: {e}")
        raise HTTPException(status_code=e.response.status_code, detail=str(e))


# User Endpoints

@app.get("/wiki/api/v2/users-bulk", response_model=List[UserResponse], tags=["Users"])
async def get_users_bulk(account_ids: List[str]):
    """Get user details for multiple account IDs."""
    if not state.http_client:
        raise HTTPException(status_code=500, detail="Server not initialized")
    
    try:
        response = await state.http_client.post(
            f"{state.host}/wiki/api/v2/users-bulk",
            json={"accountIds": account_ids}
        )
        response.raise_for_status()
        return response.json().get("results", [])
    except httpx.HTTPStatusError as e:
        logger.error(f"HTTP error: {e}")
        raise HTTPException(status_code=e.response.status_code, detail=str(e))


# Search Endpoints

@app.get("/wiki/api/v2/search", response_model=SearchResponse, tags=["Search"])
async def search_content(
    cql: str = Query(..., description="Confluence Query Language query"),
    limit: int = Query(25, description="Maximum number of results"),
    cursor: Optional[str] = Query(None, description="Cursor for pagination"),
):
    """Search content using CQL."""
    if not state.http_client:
        raise HTTPException(status_code=500, detail="Server not initialized")
    
    params = {
        "cql": cql,
        "limit": limit,
        "cursor": cursor,
    }
    
    try:
        response = await state.http_client.get(f"{state.host}/wiki/api/v2/search", params=params)
        response.raise_for_status()
        return response.json()
    except httpx.HTTPStatusError as e:
        logger.error(f"HTTP error: {e}")
        raise HTTPException(status_code=e.response.status_code, detail=str(e))


# Attachment Endpoints

@app.get("/wiki/api/v2/attachments", response_model=List[Dict[str, Any]], tags=["Attachments"])
async def get_attachments(
    limit: int = Query(25, description="Maximum number of results"),
    cursor: Optional[str] = Query(None, description="Cursor for pagination"),
    status: Optional[List[str]] = Query(None, description="Filter by status"),
    media_type: Optional[str] = Query(None, description="Filter by media type"),
    filename: Optional[str] = Query(None, description="Filter by filename"),
    sort: Optional[str] = Query(None, description="Sort order"),
):
    """Get all attachments."""
    if not state.http_client:
        raise HTTPException(status_code=500, detail="Server not initialized")
    
    params = {
        "limit": limit,
        "cursor": cursor,
        "status": status,
        "mediaType": media_type,
        "filename": filename,
        "sort": sort,
    }
    
    try:
        response = await state.http_client.get(f"{state.host}/wiki/api/v2/attachments", params=params)
        response.raise_for_status()
        return response.json().get("results", [])
    except httpx.HTTPStatusError as e:
        logger.error(f"HTTP error: {e}")
        raise HTTPException(status_code=e.response.status_code, detail=str(e))


# Comment Endpoints

@app.get("/wiki/api/v2/footer-comments", response_model=List[Dict[str, Any]], tags=["Comments"])
async def get_footer_comments(
    limit: int = Query(25, description="Maximum number of results"),
    cursor: Optional[str] = Query(None, description="Cursor for pagination"),
    sort: Optional[str] = Query(None, description="Sort order"),
):
    """Get all footer comments."""
    if not state.http_client:
        raise HTTPException(status_code=500, detail="Server not initialized")
    
    params = {
        "limit": limit,
        "cursor": cursor,
        "sort": sort,
    }
    
    try:
        response = await state.http_client.get(f"{state.host}/wiki/api/v2/footer-comments", params=params)
        response.raise_for_status()
        return response.json().get("results", [])
    except httpx.HTTPStatusError as e:
        logger.error(f"HTTP error: {e}")
        raise HTTPException(status_code=e.response.status_code, detail=str(e))


# Label Endpoints

@app.get("/wiki/api/v2/labels", response_model=List[Dict[str, Any]], tags=["Labels"])
async def get_labels(
    limit: int = Query(25, description="Maximum number of results"),
    cursor: Optional[str] = Query(None, description="Cursor for pagination"),
    prefix: Optional[str] = Query(None, description="Filter by prefix"),
    sort: Optional[str] = Query(None, description="Sort order"),
):
    """Get all labels."""
    if not state.http_client:
        raise HTTPException(status_code=500, detail="Server not initialized")
    
    params = {
        "limit": limit,
        "cursor": cursor,
        "prefix": prefix,
        "sort": sort,
    }
    
    try:
        response = await state.http_client.get(f"{state.host}/wiki/api/v2/labels", params=params)
        response.raise_for_status()
        return response.json().get("results", [])
    except httpx.HTTPStatusError as e:
        logger.error(f"HTTP error: {e}")
        raise HTTPException(status_code=e.response.status_code, detail=str(e))


# Task Endpoints

@app.get("/wiki/api/v2/tasks", response_model=List[Dict[str, Any]], tags=["Tasks"])
async def get_tasks(
    limit: int = Query(25, description="Maximum number of results"),
    cursor: Optional[str] = Query(None, description="Cursor for pagination"),
    status: Optional[str] = Query(None, description="Filter by status"),
):
    """Get all tasks."""
    if not state.http_client:
        raise HTTPException(status_code=500, detail="Server not initialized")
    
    params = {
        "limit": limit,
        "cursor": cursor,
        "status": status,
    }
    
    try:
        response = await state.http_client.get(f"{state.host}/wiki/api/v2/tasks", params=params)
        response.raise_for_status()
        return response.json().get("results", [])
    except httpx.HTTPStatusError as e:
        logger.error(f"HTTP error: {e}")
        raise HTTPException(status_code=e.response.status_code, detail=str(e))


# Operation Endpoints

@app.get("/wiki/api/v2/pages/{page_id}/operations", response_model=Dict[str, Any], tags=["Operations"])
async def get_page_operations(page_id: str):
    """Get permitted operations for a page."""
    if not state.http_client:
        raise HTTPException(status_code=500, detail="Server not initialized")
    
    try:
        response = await state.http_client.get(f"{state.host}/wiki/api/v2/pages/{page_id}/operations")
        response.raise_for_status()
        return response.json()
    except httpx.HTTPStatusError as e:
        logger.error(f"HTTP error: {e}")
        raise HTTPException(status_code=e.response.status_code, detail=str(e))


# Blog Post Endpoints

@app.get("/wiki/api/v2/blogposts", response_model=List[ContentResponse], tags=["Blog Posts"])
async def get_blog_posts(
    limit: int = Query(25, description="Maximum number of results"),
    cursor: Optional[str] = Query(None, description="Cursor for pagination"),
    space_id: Optional[List[str]] = Query(None, alias="space-id", description="Filter by space ID"),
    status: Optional[List[str]] = Query(None, description="Filter by status"),
    title: Optional[str] = Query(None, description="Filter by title"),
):
    """Get all blog posts."""
    if not state.http_client:
        raise HTTPException(status_code=500, detail="Server not initialized")
    
    params = {
        "limit": limit,
        "cursor": cursor,
        "space-id": space_id,
        "status": status,
        "title": title,
    }
    
    try:
        response = await state.http_client.get(f"{state.host}/wiki/api/v2/blogposts", params=params)
        response.raise_for_status()
        return response.json().get("results", [])
    except httpx.HTTPStatusError as e:
        logger.error(f"HTTP error: {e}")
        raise HTTPException(status_code=e.response.status_code, detail=str(e))


@app.post("/wiki/api/v2/blogposts", response_model=ContentResponse, tags=["Blog Posts"])
async def create_blog_post(
    space_id: str = Field(..., alias="spaceId"),
    status: str = "current",
    title: str = Field(...),
    body: Optional[Dict[str, Any]] = None,
):
    """Create a new blog post."""
    if not state.http_client:
        raise HTTPException(status_code=500, detail="Server not initialized")
    
    payload = {
        "spaceId": space_id,
        "status": status,
        "title": title,
        "body": body,
    }
    
    try:
        response = await state.http_client.post(
            f"{state.host}/wiki/api/v2/blogposts",
            json={k: v for k, v in payload.items() if v is not None}
        )
        response.raise_for_status()
        return response.json()
    except httpx.HTTPStatusError as e:
        logger.error(f"HTTP error: {e}")
        raise HTTPException(status_code=e.response.status_code, detail=str(e))


# Whiteboard Endpoints

@app.get("/wiki/api/v2/whiteboards", response_model=List[Dict[str, Any]], tags=["Whiteboards"])
async def get_whiteboards(
    limit: int = Query(25, description="Maximum number of results"),
    cursor: Optional[str] = Query(None, description="Cursor for pagination"),
):
    """Get all whiteboards."""
    if not state.http_client:
        raise HTTPException(status_code=500, detail="Server not initialized")
    
    params = {
        "limit": limit,
        "cursor": cursor,
    }
    
    try:
        response = await state.http_client.get(f"{state.host}/wiki/api/v2/whiteboards", params=params)
        response.raise_for_status()
        return response.json().get("results", [])
    except httpx.HTTPStatusError as e:
        logger.error(f"HTTP error: {e}")
        raise HTTPException(status_code=e.response.status_code, detail=str(e))


@app.post("/wiki/api/v2/whiteboards", response_model=Dict[str, Any], tags=["Whiteboards"])
async def create_whiteboard(
    space_id: str = Field(..., alias="spaceId"),
    title: str = Field(...),
    parent_id: Optional[str] = Field(default=None, alias="parentId"),
    template_key: Optional[str] = None,
    locale: Optional[str] = None,
):
    """Create a new whiteboard."""
    if not state.http_client:
        raise HTTPException(status_code=500, detail="Server not initialized")
    
    payload = {
        "spaceId": space_id,
        "title": title,
        "parentId": parent_id,
        "templateKey": template_key,
        "locale": locale,
    }
    
    try:
        response = await state.http_client.post(
            f"{state.host}/wiki/api/v2/whiteboards",
            json={k: v for k, v in payload.items() if v is not None}
        )
        response.raise_for_status()
        return response.json()
    except httpx.HTTPStatusError as e:
        logger.error(f"HTTP error: {e}")
        raise HTTPException(status_code=e.response.status_code, detail=str(e))


# Custom Content Endpoints

@app.get("/wiki/api/v2/custom-content", response_model=List[Dict[str, Any]], tags=["Custom Content"])
async def get_custom_content(
    type: str = Query(..., description="Filter by type"),
    limit: int = Query(25, description="Maximum number of results"),
    cursor: Optional[str] = Query(None, description="Cursor for pagination"),
):
    """Get custom content by type."""
    if not state.http_client:
        raise HTTPException(status_code=500, detail="Server not initialized")
    
    params = {
        "type": type,
        "limit": limit,
        "cursor": cursor,
    }
    
    try:
        response = await state.http_client.get(f"{state.host}/wiki/api/v2/custom-content", params=params)
        response.raise_for_status()
        return response.json().get("results", [])
    except httpx.HTTPStatusError as e:
        logger.error(f"HTTP error: {e}")
        raise HTTPException(status_code=e.response.status_code, detail=str(e))


@app.post("/wiki/api/v2/custom-content", response_model=Dict[str, Any], tags=["Custom Content"])
async def create_custom_content(
    type: str = Field(...),
    status: str = "current",
    title: str = Field(...),
    space_id: Optional[str] = Field(default=None, alias="spaceId"),
    page_id: Optional[str] = Field(default=None, alias="pageId"),
    blogpost_id: Optional[str] = Field(default=None, alias="blogPostId"),
    body: Optional[Dict[str, Any]] = None,
):
    """Create custom content."""
    if not state.http_client:
        raise HTTPException(status_code=500, detail="Server not initialized")
    
    payload = {
        "type": type,
        "status": status,
        "title": title,
        "spaceId": space_id,
        "pageId": page_id,
        "blogPostId": blogpost_id,
        "body": body,
    }
    
    try:
        response = await state.http_client.post(
            f"{state.host}/wiki/api/v2/custom-content",
            json={k: v for k, v in payload.items() if v is not None}
        )
        response.raise_for_status()
        return response.json()
    except httpx.HTTPStatusError as e:
        logger.error(f"HTTP error: {e}")
        raise HTTPException(status_code=e.response.status_code, detail=str(e))


# Version Endpoints

@app.get("/wiki/api/v2/pages/{page_id}/versions", response_model=List[Dict[str, Any]], tags=["Versions"])
async def get_page_versions(
    page_id: str,
    limit: int = Query(25, description="Maximum number of results"),
    cursor: Optional[str] = Query(None, description="Cursor for pagination"),
):
    """Get versions for a page."""
    if not state.http_client:
        raise HTTPException(status_code=500, detail="Server not initialized")
    
    params = {
        "limit": limit,
        "cursor": cursor,
    }
    
    try:
        response = await state.http_client.get(
            f"{state.host}/wiki/api/v2/pages/{page_id}/versions", params=params
        )
        response.raise_for_status()
        return response.json().get("results", [])
    except httpx.HTTPStatusError as e:
        logger.error(f"HTTP error: {e}")
        raise HTTPException(status_code=e.response.status_code, detail=str(e))


# Content Properties Endpoints

@app.get("/wiki/api/v2/pages/{page_id}/properties", response_model=List[Dict[str, Any]], tags=["Content Properties"])
async def get_page_properties(
    page_id: str,
    limit: int = Query(25, description="Maximum number of results"),
    cursor: Optional[str] = Query(None, description="Cursor for pagination"),
):
    """Get content properties for a page."""
    if not state.http_client:
        raise HTTPException(status_code=500, detail="Server not initialized")
    
    params = {
        "limit": limit,
        "cursor": cursor,
    }
    
    try:
        response = await state.http_client.get(
            f"{state.host}/wiki/api/v2/pages/{page_id}/properties", params=params
        )
        response.raise_for_status()
        return response.json().get("results", [])
    except httpx.HTTPStatusError as e:
        logger.error(f"HTTP error: {e}")
        raise HTTPException(status_code=e.response.status_code, detail=str(e))


@app.post("/wiki/api/v2/pages/{page_id}/properties", response_model=Dict[str, Any], tags=["Content Properties"])
async def create_page_property(
    page_id: str,
    key: str = Field(...),
    value: Optional[Any] = None,
):
    """Create content property for a page."""
    if not state.http_client:
        raise HTTPException(status_code=500, detail="Server not initialized")
    
    payload = {"key": key, "value": value}
    
    try:
        response = await state.http_client.post(
            f"{state.host}/wiki/api/v2/pages/{page_id}/properties", json=payload
        )
        response.raise_for_status()
        return response.json()
    except httpx.HTTPStatusError as e:
        logger.error(f"HTTP error: {e}")
        raise HTTPException(status_code=e.response.status_code, detail=str(e))


# Space Permissions Endpoints

@app.get("/wiki/api/v2/spaces/{space_id}/permissions", response_model=List[Dict[str, Any]], tags=["Space Permissions"])
async def get_space_permissions(
    space_id: str,
    limit: int = Query(25, description="Maximum number of results"),
    cursor: Optional[str] = Query(None, description="Cursor for pagination"),
):
    """Get space permissions for a space."""
    if not state.http_client:
        raise HTTPException(status_code=500, detail="Server not initialized")
    
    params = {
        "limit": limit,
        "cursor": cursor,
    }
    
    try:
        response = await state.http_client.get(
            f"{state.host}/wiki/api/v2/spaces/{space_id}/permissions", params=params
        )
        response.raise_for_status()
        return response.json().get("results", [])
    except httpx.HTTPStatusError as e:
        logger.error(f"HTTP error: {e}")
        raise HTTPException(status_code=e.response.status_code, detail=str(e))


# Data Policies Endpoints

@app.get("/wiki/api/v2/data-policies/metadata", response_model=Dict[str, Any], tags=["Data Policies"])
async def get_data_policies_metadata():
    """Get data policy metadata for the workspace."""
    if not state.http_client:
        raise HTTPException(status_code=500, detail="Server not initialized")
    
    try:
        response = await state.http_client.get(f"{state.host}/wiki/api/v2/data-policies/metadata")
        response.raise_for_status()
        return response.json()
    except httpx.HTTPStatusError as e:
        logger.error(f"HTTP error: {e}")
        raise HTTPException(status_code=e.response.status_code, detail=str(e))


@app.get("/wiki/api/v2/data-policies/spaces", response_model=List[Dict[str, Any]], tags=["Data Policies"])
async def get_data_policies_spaces(
    limit: int = Query(25, description="Maximum number of results"),
    cursor: Optional[str] = Query(None, description="Cursor for pagination"),
):
    """Get spaces with data policies."""
    if not state.http_client:
        raise HTTPException(status_code=500, detail="Server not initialized")
    
    params = {
        "limit": limit,
        "cursor": cursor,
    }
    
    try:
        response = await state.http_client.get(
            f"{state.host}/wiki/api/v2/data-policies/spaces", params=params
        )
        response.raise_for_status()
        return response.json().get("results", [])
    except httpx.HTTPStatusError as e:
        logger.error(f"HTTP error: {e}")
        raise HTTPException(status_code=e.response.status_code, detail=str(e))


# Long-running Task Endpoints

@app.get("/wiki/api/v2/longtask", response_model=List[Dict[str, Any]], tags=["Long-running Tasks"])
async def get_long_tasks(
    key: Optional[str] = Query(None, description="Filter by key"),
    limit: int = Query(25, description="Maximum number of results"),
    cursor: Optional[str] = Query(None, description="Cursor for pagination"),
):
    """Get long-running tasks."""
    if not state.http_client:
        raise HTTPException(status_code=500, detail="Server not initialized")
    
    params = {
        "key": key,
        "limit": limit,
        "cursor": cursor,
    }
    
    try:
        response = await state.http_client.get(f"{state.host}/wiki/api/v2/longtask", params=params)
        response.raise_for_status()
        return response.json().get("results", [])
    except httpx.HTTPStatusError as e:
        logger.error(f"HTTP error: {e}")
        raise HTTPException(status_code=e.response.status_code, detail=str(e))


@app.get("/wiki/api/v2/longtask/{task_id}", response_model=Dict[str, Any], tags=["Long-running Tasks"])
async def get_long_task(task_id: str):
    """Get a specific long-running task."""
    if not state.http_client:
        raise HTTPException(status_code=500, detail="Server not initialized")
    
    try:
        response = await state.http_client.get(f"{state.host}/wiki/api/v2/longtask/{task_id}")
        response.raise_for_status()
        return response.json()
    except httpx.HTTPStatusError as e:
        logger.error(f"HTTP error: {e}")
        raise HTTPException(status_code=e.response.status_code, detail=str(e))


# Archive Content Endpoint

@app.post("/wiki/api/v2/content/archive", response_model=Dict[str, Any], tags=["Content"])
async def archive_content(pages: List[str] = Field(..., description="List of page IDs to archive")):
    """Archive pages."""
    if not state.http_client:
        raise HTTPException(status_code=500, detail="Server not initialized")
    
    payload = {"pages": pages}
    
    try:
        response = await state.http_client.post(
            f"{state.host}/wiki/api/v2/content/archive", json=payload
        )
        response.raise_for_status()
        return response.json()
    except httpx.HTTPStatusError as e:
        logger.error(f"HTTP error: {e}")
        raise HTTPException(status_code=e.response.status_code, detail=str(e))


# Run server
if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", "8000"))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=False)