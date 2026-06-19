"""Confluence MCP Server.

This MCP server provides endpoints for Confluence Cloud API operations.

To run the server:
    python server.py

Environment variables:
    CONFLUENCE_BASE_URL: Base URL for Confluence Cloud API (default: https://api.atlassian.com/ex/confluence)
    CONFLUENCE_ACCESS_TOKEN: OAuth 2.0 access token for Confluence API
    API_VERSION: API version to use (default: 2)
"""

import asyncio
import logging
import os
from typing import Optional

import uvicorn
from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse

from server import app, state

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


async def get_current_user():
    """Get current user from access token."""
    if not state.access_token:
        raise HTTPException(status_code=401, detail="Not authenticated")
    return state.access_token


@app.get("/")
async def root():
    """Root endpoint."""
    return {
        "name": "Confluence MCP Server",
        "version": "1.0.0",
        "description": "MCP Server for Confluence Cloud API",
        "endpoints": [
            "/health",
            "/wiki/api/v2/pages",
            "/wiki/api/v2/spaces",
            "/wiki/api/v2/users-bulk",
            "/wiki/api/v2/search",
            "/wiki/api/v2/attachments",
            "/wiki/api/v2/footer-comments",
            "/wiki/api/v2/labels",
            "/wiki/api/v2/tasks",
        ]
    }


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {
        "status": "healthy",
        "server": "confluence-mcp-server",
        "version": "1.0.0",
        "initialized": state.access_token is not None,
    }


@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    """Handle HTTP exceptions."""
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail},
    )


@app.exception_handler(Exception)
async def generic_exception_handler(request, exc):
    """Handle generic exceptions."""
    logger.error(f"Unhandled exception: {exc}")
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal server error"},
    )


def main():
    """Main entry point."""
    port = int(os.getenv("PORT", "8000"))
    host = os.getenv("HOST", "0.0.0.0")

    logger.info(f"Starting Confluence MCP Server on {host}:{port}")

    uvicorn.run(
        "server:app",
        host=host,
        port=port,
        reload=False,
        log_level="info",
    )


if __name__ == "__main__":
    main()
