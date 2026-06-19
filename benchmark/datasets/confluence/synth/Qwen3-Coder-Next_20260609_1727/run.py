#!/usr/bin/env python3
"""MCP Server entry point for Confluence Cloud API."""

import uvicorn

if __name__ == "__main__":
    port = int(__import__("os").environ.get("PORT", "8000"))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=False)
