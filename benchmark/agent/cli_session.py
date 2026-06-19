"""CLI tool session management for the agent harness.

Analogous to MCPServerSession but for a synthesized CLI tool instead of an
MCP server. Exposes a single `run_command` tool that shells out to the CLI,
and a `list_tools` method that returns that one tool in MCP-compatible format.

The eval agent is given no prior knowledge of the CLI's interface — it must
discover available subcommands by probing the tool (e.g. running --help or
reading usage output), which is itself part of what we measure.
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path
from typing import Any

# Track which impl dirs have already had their requirements installed.
# Prevents re-running pip on every task in an eval run.
_installed_dirs: set[str] = set()


# Schema for the single tool exposed to the eval agent.
# Intentionally minimal: no hint about subcommand names or flags.
_RUN_COMMAND_TOOL: dict[str, Any] = {
    "name": "run_command",
    "description": (
        "Run a command using the synthesized CLI tool located in the working directory. "
        "Pass the full argument string as you would type it after the script name. "
        "Returns the combined stdout and stderr output of the command."
    ),
    "input_schema": {
        "type": "object",
        "properties": {
            "args": {
                "type": "string",
                "description": "Arguments to pass to the CLI tool (e.g. '--help' or 'send-message --stream general --topic test --content hello')",
            }
        },
        "required": ["args"],
    },
}


class CLIServerSession:
    """Session wrapper for a synthesized CLI tool.

    Provides the same interface as MCPServerSession (list_tools / call_tool)
    so AgentHarness can use either interchangeably.

    Use as a context manager:

        with CLIServerSession(impl_dir) as session:
            tools = session.list_tools()
            result = session.call_tool("run_command", {"args": "--help"})
    """

    def __init__(self, impl_dir: str | Path, env: dict[str, str] | None = None):
        self.impl_dir = Path(impl_dir)
        self.env = {**os.environ, **(env or {})}
        self._cli_script: Path | None = None

    def _detect_cli(self) -> Path:
        """Find the synthesized CLI script in the impl directory.

        Detection order:
          1. *_cli.py       — canonical name pattern from TASK.md (e.g. zulip_cli.py, github_cli.py)
          2. cli.py         — common fallback
          3. main.py        — another common fallback
          4. any single *.py file at the top level
        """
        cli_named = list(self.impl_dir.glob("*_cli.py"))
        if len(cli_named) == 1:
            return cli_named[0]

        for name in ["cli.py", "main.py"]:
            candidate = self.impl_dir / name
            if candidate.exists():
                return candidate

        py_files = list(self.impl_dir.glob("*.py"))
        if len(py_files) == 1:
            return py_files[0]

        raise FileNotFoundError(
            f"No CLI script found in {self.impl_dir}. "
            f"Expected *_cli.py, cli.py, main.py, or a single *.py file."
        )

    def __enter__(self) -> "CLIServerSession":
        self._cli_script = self._detect_cli()
        self._install_requirements()
        return self

    def _install_requirements(self) -> None:
        """Install requirements.txt once per impl_dir into the running Python environment."""
        key = str(self.impl_dir.resolve())
        if key in _installed_dirs:
            return
        req = self.impl_dir / "requirements.txt"
        if not req.exists():
            _installed_dirs.add(key)
            return
        print(f"[cli_session] installing {req} ...", flush=True)
        try:
            # Prefer offline install — synthesized requirements often pin specific
            # versions that may already be satisfied by compatible installed packages.
            # We try with --offline first to avoid network timeouts; if the cache
            # doesn't have the exact pinned version we strip pins and retry offline.
            result = subprocess.run(
                ["uv", "pip", "install", "-q", "--offline", "-r", str(req)],
                capture_output=True,
                text=True,
            )
            if result.returncode == 0:
                print(f"[cli_session] requirements satisfied (offline).", flush=True)
            else:
                # Strip version pins and retry offline — the venv likely has compatible
                # versions already installed.
                packages = []
                for line in req.read_text().splitlines():
                    line = line.strip()
                    if line and not line.startswith("#"):
                        # Keep only the package name (drop ==, >=, etc.)
                        import re
                        name = re.split(r"[>=<!;\s]", line)[0]
                        if name:
                            packages.append(name)
                if packages:
                    result2 = subprocess.run(
                        ["uv", "pip", "install", "-q", "--offline"] + packages,
                        capture_output=True,
                        text=True,
                    )
                    if result2.returncode == 0:
                        print(f"[cli_session] requirements satisfied (offline, unpinned).", flush=True)
                    else:
                        print(f"[cli_session] warning: offline install failed, proceeding with existing environment. stderr: {result2.stderr[:200]}", flush=True)
                else:
                    print(f"[cli_session] warning: could not parse requirements, proceeding with existing environment.", flush=True)
        except Exception as e:
            print(f"[cli_session] warning: pip install error: {e}", flush=True)
        # Mark as attempted regardless of success — don't retry on every task
        _installed_dirs.add(key)

    def __exit__(self, *exc_info):
        pass

    def list_tools(self) -> list[dict[str, Any]]:
        """Return the single run_command tool."""
        return [_RUN_COMMAND_TOOL]

    def call_tool(self, name: str, arguments: dict[str, Any] | None = None) -> Any:
        """Execute run_command by shelling out to the CLI script.

        Args:
            name: must be "run_command"
            arguments: dict with key "args" (the CLI argument string)

        Returns:
            dict with "stdout", "stderr", "returncode", and "output" (combined).
        """
        if name != "run_command":
            return {"error": f"Unknown tool: {name!r}. Only 'run_command' is available."}

        args_str = (arguments or {}).get("args", "")
        import shlex
        try:
            arg_list = shlex.split(args_str)
        except ValueError as e:
            return {"error": f"Failed to parse args: {e}"}

        cmd = [sys.executable, str(self._cli_script)] + arg_list

        try:
            proc = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                env=self.env,
                cwd=str(self.impl_dir),
                timeout=30,
            )
        except subprocess.TimeoutExpired:
            return {"error": "CLI command timed out after 30 seconds"}
        except Exception as e:
            return {"error": f"Failed to run CLI: {e}"}

        combined = (proc.stdout + proc.stderr).strip()

        if proc.returncode != 0:
            # Non-zero exit: surface as an error so the harness counts it and the
            # judge sees a clear failure signal rather than inferring from text.
            return {"error": combined, "returncode": proc.returncode}

        # Try to parse JSON output if the CLI emits it
        try:
            parsed = json.loads(combined)
            return parsed
        except (json.JSONDecodeError, ValueError):
            pass

        return {
            "output": combined,
            "returncode": proc.returncode,
        }
