#!/usr/bin/env python3
"""
Confluence MCP Server - Main Entry Point

This script starts the Confluence MCP server.

Environment variables:
    CONFLUENCE_BASE_URL: Base URL for Confluence Cloud API (default: https://api.atlassian.com/ex/confluence)
    CONFLUENCE_ACCESS_TOKEN: OAuth 2.0 access token for Confluence API
    API_VERSION: API version to use (default: 2)
    PORT: Port to run the server on (default: 8000)
    HOST: Host to bind to (default: 0.0.0.0)
"""

import asyncio
import logging
import os
import sys

import uvicorn

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi import FastAPI
from server import app, state

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/v2")
async def api_v2_docs():
    """API v2 documentation."""
    return {
        "version": "2",
        "base_url": os.getenv("CONFLUENCE_BASE_URL", "https://api.atlassian.com/ex/confluence"),
        "endpoints": [
            "/wiki/api/v2/pages",
            "/wiki/api/v2/spaces",
            "/wiki/api/v2/users-bulk",
            "/wiki/api/v2/search",
            "/wiki/api/v2/attachments",
            "/wiki/api/v2/footer-comments",
            "/wiki/api/v2/labels",
            "/wiki/api/v2/tasks",
            "/wiki/api/v2/blogposts",
            "/wiki/api/v2/whiteboards",
        ]
    }


async def initialize_server():
    """Initialize the MCP server."""
    access_token = os.getenv("CONFLUENCE_ACCESS_TOKEN")
    if access_token:
        await state.initialize(access_token)
        logger.info("MCP server initialized successfully")
    else:
        logger.warning("CONFLUENCE_ACCESS_TOKEN not set. API endpoints will return 500 errors until token is provided.")


async def shutdown_server():
    """Shutdown the MCP server."""
    await state.close()
    logger.info("MCP server shutdown complete")


def main():
    """Main entry point."""
    port = int(os.getenv("PORT", "8000"))
    host = os.getenv("HOST", "0.0.0.0")

    logger.info(f"Starting Confluence MCP Server on {host}:{port}")
    logger.info(f"Confluence Base URL: {os.getenv('CONFLUENCE_BASE_URL', 'https://api.atlassian.com/ex/confluence')}")

    uvicorn.run(
        "main:app",
        host=host,
        port=port,
        reload=False,
        log_level="info",
    )


if __name__ == "__main__":
    main()
