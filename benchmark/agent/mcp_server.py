"""MCP server session management for the agent harness.

Handles server startup (Python or TypeScript) and provides a synchronous
interface around the async MCP ClientSession.
"""

from __future__ import annotations

import asyncio
import json
import os
from pathlib import Path
from typing import Any


class MCPServerSession:
    """Synchronous wrapper around an async MCP client session.

    Manages the event loop, server process lifetime, and stdio transport.
    Use as a context manager:

        with MCPServerSession(server_dir) as session:
            tools = session.list_tools()
            result = session.call_tool("my_tool", {"arg": "value"})
    """

    def __init__(self, server_dir: str | Path, env: dict[str, str] | None = None):
        self.server_dir = Path(server_dir)
        self.env = {**os.environ, **(env or {})}
        self._loop: asyncio.AbstractEventLoop | None = None
        self._stdio_ctx = None
        self._session_ctx = None
        self._session = None

    def _detect_server(self) -> tuple[str, list[str]]:
        """Detect the server type and return (command, args).

        Detection order:
          1. mcp_cmd.json  — arbitrary command spec: {"command": "npx", "args": [...]}
          2. server.py     — Python (FastMCP or plain MCP)
          3. build/index.js — compiled TypeScript (node)
        """
        mcp_cmd_json = self.server_dir / "mcp_cmd.json"
        server_py = self.server_dir / "server.py"
        index_js = self.server_dir / "build" / "index.js"

        if mcp_cmd_json.exists():
            spec = json.loads(mcp_cmd_json.read_text())
            # env_map: {"TARGET_VAR": "SOURCE_VAR"} — copy SOURCE into TARGET
            for target, source in spec.get("env_map", {}).items():
                if source in self.env and target not in self.env:
                    self.env[target] = self.env[source]
            return spec["command"], spec.get("args", [])
        elif server_py.exists():
            return "python", [str(server_py)]
        elif index_js.exists():
            return "node", [str(index_js)]
        else:
            raise FileNotFoundError(
                f"No server found in {self.server_dir}. "
                f"Expected mcp_cmd.json, server.py, or build/index.js."
            )

    def __enter__(self) -> "MCPServerSession":
        from mcp import ClientSession, StdioServerParameters
        from mcp.client.stdio import stdio_client

        command, args = self._detect_server()
        params = StdioServerParameters(command=command, args=args, env=self.env)

        self._loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self._loop)

        self._stdio_ctx = stdio_client(params)
        read, write = self._loop.run_until_complete(self._stdio_ctx.__aenter__())

        self._session_ctx = ClientSession(read, write)
        self._session = self._loop.run_until_complete(self._session_ctx.__aenter__())
        self._loop.run_until_complete(self._session.initialize())

        return self

    def __exit__(self, *exc_info):
        if self._session_ctx:
            try:
                self._loop.run_until_complete(self._session_ctx.__aexit__(*exc_info))
            except Exception:
                pass
        if self._stdio_ctx:
            try:
                self._loop.run_until_complete(self._stdio_ctx.__aexit__(*exc_info))
            except Exception:
                pass
        if self._loop:
            self._loop.close()
            self._loop = None

    @staticmethod
    def _sanitize_schema(schema: Any) -> Any:
        """Recursively strip JSON Schema fields that Gemini rejects.

        Gemini's function calling API does not support $defs, $ref, $schema,
        additionalProperties, or $id. Reference servers (e.g. official Notion
        and GitHub npm packages) emit these, causing 400 INVALID_ARGUMENT errors.
        """
        _STRIP_KEYS = {"$defs", "$schema", "$id", "additionalProperties"}
        if isinstance(schema, dict):
            out = {}
            for k, v in schema.items():
                if k in _STRIP_KEYS:
                    continue
                if k == "$ref":
                    # Can't inline $ref without the $defs context — drop the field
                    continue
                out[k] = MCPServerSession._sanitize_schema(v)
            return out
        if isinstance(schema, list):
            return [MCPServerSession._sanitize_schema(item) for item in schema]
        return schema

    def list_tools(self) -> list[dict[str, Any]]:
        """Return list of tool dicts with name, description, inputSchema."""
        async def _list():
            result = await self._session.list_tools()
            return result.tools

        tools = self._loop.run_until_complete(_list())
        return [
            {
                "name": t.name,
                "description": t.description or "",
                "input_schema": self._sanitize_schema(
                    t.inputSchema if hasattr(t, "inputSchema") else {}
                ),
            }
            for t in tools
        ]

    def call_tool(self, name: str, arguments: dict[str, Any] | None = None) -> Any:
        """Call a tool and return parsed result (JSON dict/list or string)."""
        async def _call():
            result = await self._session.call_tool(name, arguments or {})
            if result.content:
                text = result.content[0].text
                try:
                    return json.loads(text)
                except (json.JSONDecodeError, TypeError):
                    return text
            return None

        return self._loop.run_until_complete(_call())
