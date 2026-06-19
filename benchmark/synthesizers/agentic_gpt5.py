"""
Agentic GPT-5: Multi-turn agent using AzureOpenAIChatWrapper with GPT-5.

Uses GPT-5 which has 180 req/min rate limit (vs Claude's 6 req/min),
allowing for much more aggressive doc reading without delays.
"""

import os
import re
import time
import tempfile
from pathlib import Path
from typing import List, Dict, Any

from benchmark.core.synthesizer import BaseSynthesizer, Document, SynthesisResult


class AgenticGPT5(BaseSynthesizer):
    """
    Synthesizer using agentic exploration with GPT-5 via AzureOpenAIChatWrapper.

    GPT-5 has 180 req/min vs Claude's 6 req/min, allowing much more doc reading.
    """

    def __init__(
        self,
        model: str = "azure-chat-completions-gpt-5-2-2025-12-11-sandbox",
        max_turns: int = 40,
    ):
        self.model = model
        self.max_turns = max_turns

    @property
    def name(self) -> str:
        return "agentic_gpt5"

    @property
    def description(self) -> str:
        return "Multi-turn GPT-5 agent with high rate limit for doc exploration"

    def synthesize(
        self,
        task_prompt: str,
        api_docs: List[Document],
        required_tools: List[str] = None,
        **kwargs
    ) -> SynthesisResult:
        """Generate tools using agentic exploration."""

        start_time = time.time()

        with tempfile.TemporaryDirectory() as tmpdir:
            tmpdir = Path(tmpdir)

            # Write task prompt
            task_file = tmpdir / "TASK.md"
            task_file.write_text(task_prompt)

            # Write API docs
            docs_dir = tmpdir / "docs"
            docs_dir.mkdir()
            for doc in api_docs:
                filename = doc.metadata.get('filename', 'doc.md')
                (docs_dir / filename).write_text(doc.content)

            # Build exploration task
            task_instruction = self._build_exploration_task(len(api_docs))

            print("🤖 Starting agentic exploration workflow (GPT-5)...", flush=True)
            print(f"   Workspace: {tmpdir}", flush=True)
            print(f"   Docs available: {len(api_docs)} files", flush=True)
            print(f"   Task written to TASK.md", flush=True)
            print("   Launching agent to explore and generate...", flush=True)

            # Run agentic loop
            result = self._run_agentic_loop(tmpdir, task_instruction)

            synthesis_time = time.time() - start_time

            # Extract code
            code = self._extract_code(tmpdir, result)

            # Save multi-file structure if it exists (before temp dir is deleted)
            package_dir = tmpdir / "generated_tools"
            multi_file_structure = None
            if package_dir.exists() and package_dir.is_dir() and (package_dir / "__init__.py").exists():
                multi_file_structure = self._preserve_multi_file_structure(package_dir)

            # Analyze exploration behavior
            steps = result.get("steps", [])
            docs_read_list = self._get_docs_read(steps)
            domains_covered = self._analyze_domain_coverage(docs_read_list)

            metadata = {
                "approach": "agentic_exploration_gpt5",
                "model": self.model,
                "max_turns": self.max_turns,

                # Turn-level metrics
                "num_turns": result.get("num_turns", 0),
                "num_steps": len(steps),

                # Exploration metrics
                "total_docs_available": len(api_docs),
                "docs_read": len(docs_read_list),
                "docs_read_list": docs_read_list,
                "read_percentage": len(docs_read_list) / len(api_docs) * 100 if api_docs else 0,
                "domains_covered": domains_covered,

                # Context compression
                "had_context_compression": result.get("had_compression", False),
                "compression_trigger_threshold": 10,

                # Step details
                "agent_steps": steps,
                "step_breakdown": self._breakdown_steps(steps),

                # Timing
                "synthesis_time": synthesis_time,
            }

            # Add multi-file structure info if available
            if multi_file_structure:
                metadata["multi_file_structure"] = multi_file_structure

            return SynthesisResult(
                code=code,
                metadata=metadata,
                token_usage={
                    "estimated_tokens": len(result.get("output", "")) // 4,
                },
                synthesis_time=synthesis_time,
                cost_estimate=len(result.get("output", "")) // 4 * 3 / 1_000_000,
            )

    def _build_exploration_task(self, num_docs: int) -> str:
        """Build the task instruction for agentic exploration."""
        return f"""You are working in a directory with:
- TASK.md: Contains the requirements for what tools to build
- docs/: A directory with {num_docs} API documentation files

Your task is to build a COMPREHENSIVE server as specified in TASK.md.

Step-by-step process:
1. Read TASK.md to understand requirements (you can re-read it anytime)
   - Check the completion checklist - that defines "done"
   - Note all required domains
   - Before finishing, re-read TASK.md to verify you met all requirements

2. Explore the docs/ directory comprehensively
   - Use list_directory to see what's available
   - Read 3-5 representative docs from EACH major domain in TASK.md
   - Read 25-40 docs TOTAL to get comprehensive understanding
   - Sample multiple operations per domain (create, get, list, update, delete)
   - Don't stop reading until you understand ALL domains mentioned in TASK.md
   - Focus on understanding API conventions, parameter patterns, response structures
   - Use docs to learn the API thoroughly, then generalize to all required tools
   - With high rate limits (180 req/min), you can afford to read more docs for accuracy

3. Generate the complete Python code as specified in TASK.md
   - ONLY start writing code AFTER you've read docs from ALL required domains
   - For 30+ tools, use multi-file structure (recommended)
   - Create separate files for each domain
   - Include ALL domains and features requested
   - Base your implementation on the ACTUAL docs you read, not prior knowledge
   - If a manifest is requested, include it as JSON in __init__.py docstring

4. Save the generated code using write_file tool:
   - For multi-file: Create generated_tools/__init__.py and ALL domain files
   - For single-file: Create generated_tools.py with all code

   IMPORTANT: If you create __init__.py that imports from multiple domain files,
   you MUST create ALL those domain files. Do not stop until every domain is implemented.

   Example multi-file structure:
   - write_file("generated_tools/__init__.py", ...) - imports, manifest, exports
   - write_file("generated_tools/helpers.py", ...) - shared utilities
   - write_file("generated_tools/messages.py", ...) - message tools
   - write_file("generated_tools/streams.py", ...) - stream tools
   - ... continue for EVERY domain listed in __init__.py

REQUIRED in ALL files:
- Import statement: `import mcp` at the top (before using @mcp.tool())
- Helper functions for API calls
- Tool functions decorated with @mcp.tool()
- Proper error handling and docstrings
- Type hints

The __init__.py must:
- Import all tools from submodules
- Export them in __all__ list
- Include the manifest in its docstring

Do NOT include the FastMCP server setup - ONLY the tool functions and helpers.

IMPORTANT - READ THIS CAREFULLY:
- You MUST read API docs before writing code. Do NOT write tools from memory.
- Read docs strategically: 3-5 endpoints per domain to understand patterns.
- Follow TASK.md requirements exactly - don't add/skip domains arbitrarily.
- If you create __init__.py with imports from multiple files, create ALL those files.
- Don't stop until all domains from your manifest are fully implemented.
- For comprehensive tasks, you may need to use all {self.max_turns} turns available.

WORKFLOW ENFORCEMENT:
Turn 1-2: Read TASK.md and list docs/
Turn 3-12: Read 15-25 comprehensive docs (2-3 per major domain)
Turn 13-19: Write ALL code files for the comprehensive implementation
Turn 20: Final review and completion

STRATEGY: Read comprehensively to understand the API deeply (15-25 docs recommended).
With high rate limits, you can read more docs for better accuracy. Focus on quality over speed."""

    def _run_agentic_loop(self, workspace: Path, initial_task: str) -> Dict[str, Any]:
        """
        Run an agentic loop where the agent uses tools to explore.

        Uses GPT-5 via AzureOpenAIChatWrapper with 180 req/min rate limit.
        """
        from pychomsky.chchat.azureopenai import AzureOpenAIChatWrapper
        from langchain_core.messages import HumanMessage, ToolMessage

        # Initialize LLM via AzureOpenAIChatWrapper (direct Azure wrapper)
        # GPT-5 uses max_completion_tokens instead of max_tokens
        llm = AzureOpenAIChatWrapper(
            model_name=self.model,
            max_completion_tokens=8192,  # GPT-5 parameter
            temperature=0.2  # Try lower temperature for more deterministic behavior
        )

        # Define tools in Anthropic format
        tools = [
            {
                "name": "read_file",
                "description": "Read a file from the workspace",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "file_path": {
                            "type": "string",
                            "description": "Path to file relative to workspace"
                        }
                    },
                    "required": ["file_path"]
                }
            },
            {
                "name": "list_directory",
                "description": "List files in a directory",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "dir_path": {
                            "type": "string",
                            "description": "Path to directory relative to workspace"
                        }
                    },
                    "required": ["dir_path"]
                }
            },
            {
                "name": "write_file",
                "description": "Write content to a file",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "file_path": {"type": "string"},
                        "content": {"type": "string"}
                    },
                    "required": ["file_path", "content"]
                }
            }
        ]

        # Bind tools to LLM
        llm_with_tools = llm.bind_tools(tools)

        # Run agentic loop
        messages = [HumanMessage(content=initial_task)]
        steps = []
        had_compression = False
        consecutive_no_action_turns = 0  # Track if agent gets stuck

        for iteration in range(self.max_turns):
            print(f"   Turn {iteration + 1}/{self.max_turns}...", flush=True)

            # No delays needed - GPT-5 has 180 req/min (vs Claude's 6 req/min)
            # Call LLM with retry logic
            response = self._call_with_retry(llm_with_tools, messages)

            # Handle rate limit graceful exit
            if response is None:
                has_written_code = any(s.get("action") == "write_file" for s in steps)
                if has_written_code:
                    print("   ⚠️ Rate limit hit, but code was already generated. Stopping gracefully.", flush=True)
                    break
                else:
                    print("   ⚠️ Rate limit hit before code generation! This is a failure.", flush=True)
                    # Don't break - let the framework handle the failure with empty output
                    break

            # Check for tool calls
            tool_calls = getattr(response, 'tool_calls', [])
            print(f"     Tools used: {len(tool_calls)}, Stop reason: {response.response_metadata.get('stop_reason', 'unknown')}", flush=True)

            # Track if agent is taking action
            if len(tool_calls) == 0:
                consecutive_no_action_turns += 1
            else:
                consecutive_no_action_turns = 0

            # Check if done
            if not tool_calls:
                # Verify a complete implementation was written
                write_file_steps = [s for s in steps if s.get("action") == "write_file"]
                has_written_code = len(write_file_steps) > 0

                # Check for complete implementation (not just helpers)
                files_written = [s.get("input", {}).get("file_path", "") for s in write_file_steps]
                has_init = any("__init__.py" in f for f in files_written)
                has_multiple_files = len(files_written) >= 3  # At least helpers + init + 1 domain

                # Count tools across all files (both MCP decorators and plain functions)
                tool_count = 0
                for step in write_file_steps:
                    content = step.get("input", {}).get("content", "")
                    file_path = step.get("input", {}).get("file_path", "")

                    # Count @mcp.tool() decorators
                    mcp_tools = content.count("@mcp.tool()")

                    # Count plain Python functions (excluding private/helper functions)
                    # Only count in domain files, not in helpers/_common files
                    plain_funcs = 0
                    if not any(x in file_path for x in ["helper", "_common", "__init__"]):
                        import re
                        # Match function definitions that are not private (don't start with _)
                        plain_funcs = len(re.findall(r'^def ([a-z][a-z0-9_]*)\(', content, re.MULTILINE))

                    tool_count += max(mcp_tools, plain_funcs)  # Use whichever is higher

                # Agent decides when it's done
                is_complete = has_written_code

                # Safety: stop if agent stuck
                if not has_written_code and consecutive_no_action_turns >= 3:
                    print(f"   ⚠️ Agent stuck - stopping", flush=True)
                    break

                # Checkpoint: if agent wrote code and is stopping (0 tools used), remind once to verify
                if has_written_code and len(tool_calls) == 0 and iteration < self.max_turns - 1:
                    # Only send this reminder once
                    if not hasattr(self, '_sent_completion_check'):
                        self._sent_completion_check = True
                        print(f"   ℹ️  Agent finished - asking to verify completion against checklist...", flush=True)
                        reminder = "Re-read TASK.md and verify you've completed ALL items in the checklist at the top before finishing."
                        messages.append(HumanMessage(content=reminder))
                        continue
                    # After checkpoint, if agent keeps returning 0 tools for 3 turns, stop
                    if consecutive_no_action_turns >= 3:
                        print("   ✓ Agent finished (no more actions after checkpoint)", flush=True)
                        break
                    continue

                # Agent truly finished
                if has_written_code and len(tool_calls) == 0:
                    print("   ✓ Agent finished", flush=True)
                    break

            # Add assistant message with tool calls
            messages.append(response)

            # Process tool calls
            has_write_file = False
            for tool_call in tool_calls:
                tool_name = tool_call['name']
                tool_args = tool_call['args']
                tool_id = tool_call['id']

                result = self._execute_tool(workspace, tool_name, tool_args)

                messages.append(ToolMessage(
                    content=result,
                    tool_call_id=tool_id
                ))

                print(f"     - {tool_name}: {tool_args}", flush=True)

                steps.append({
                    "step": len(steps) + 1,
                    "action": tool_name,
                    "input": tool_args,
                })

                if tool_name == "write_file":
                    has_write_file = True

            # Context compression check
            if iteration >= 5 and not had_compression and not has_write_file:
                num_reads = sum(1 for s in steps if s.get("action") == "read_file")
                if num_reads >= 35:  # Increased from 10 to allow more doc reading before compression
                    print(f"   📦 Compressing context ({num_reads} docs read)...", flush=True)
                    messages = self._compress_context(llm, messages)
                    had_compression = True
                    print(f"   ✅ Context compressed. Restarting with summary...", flush=True)

                    steps.append({
                        "step": len(steps) + 1,
                        "action": "context_compression",
                        "num_docs_read": num_reads,
                    })

        return {
            "output": f"Agent completed in {len(steps)} steps across {iteration + 1} turns",
            "error": "",
            "steps": steps,
            "num_turns": iteration + 1,
            "had_compression": had_compression,
        }

    def _call_with_retry(self, llm, messages, max_retries=3, timeout=120):
        """Call LLM with exponential backoff retry and timeout."""
        import sys
        from concurrent.futures import ThreadPoolExecutor, TimeoutError as FuturesTimeoutError

        for retry in range(max_retries):
            try:
                # Use ThreadPoolExecutor to add timeout to the API call
                with ThreadPoolExecutor(max_workers=1) as executor:
                    future = executor.submit(llm.invoke, messages)
                    try:
                        return future.result(timeout=timeout)
                    except FuturesTimeoutError:
                        print(f"     ⚠️ API call timed out after {timeout}s (retry {retry + 1}/{max_retries})", flush=True)
                        # Treat timeout as retriable error
                        if retry < max_retries - 1:
                            wait_time = 2 ** retry  # 1s, 2s, 4s
                            print(f"     Waiting {wait_time}s before retry...", flush=True)
                            sys.stdout.flush()
                            time.sleep(wait_time)
                            continue
                        else:
                            print(f"     ⚠️ Timeout after all retries, stopping...", flush=True)
                            return None
            except Exception as e:
                # Check if it's a rate limit error (429)
                is_rate_limit = "429" in str(e) or "Too many requests" in str(e)

                if retry < max_retries - 1:
                    # Use longer waits for rate limits
                    wait_time = (2 ** retry) * (5 if is_rate_limit else 1)  # 5s, 10s, 20s for rate limits
                    print(f"     ⚠️ Error (retry {retry + 1}/{max_retries}): {str(e)[:150]}...", flush=True)
                    print(f"     Waiting {wait_time}s before retry...", flush=True)
                    sys.stdout.flush()
                    time.sleep(wait_time)
                else:
                    # On final retry failure, if it's rate limit, just warn and return None
                    # This allows the agent to complete if code was already written
                    if is_rate_limit:
                        print(f"     ⚠️ Rate limit exceeded, stopping early...", flush=True)
                        return None
                    raise

    def _compress_context(self, llm, messages):
        """Compress conversation context using structured summary."""
        from langchain_core.messages import HumanMessage

        compression_prompt = """You've read the API documentation. Before generating code, create a structured summary of the key information you'll need.

Format your response as a JSON object with this structure:
{
  "domains": {
    "messages": {
      "endpoints": [{"name": "send_message", "method": "POST", "path": "/api/v1/messages", "key_params": [...]}],
      "auth_header": "...",
      "base_url": "..."
    },
    "streams": {...},
    "users": {...}
  },
  "common_patterns": {
    "auth": "...",
    "error_handling": "...",
    "required_imports": [...]
  }
}

Keep it concise but include all essential details for implementation."""

        messages.append(HumanMessage(content=compression_prompt))

        # Use timeout wrapper for compression call too
        summary_response = self._call_with_retry(llm, messages, timeout=180)
        if summary_response is None:
            # If compression fails, return original messages
            print("     ⚠️ Context compression timed out, continuing without compression...", flush=True)
            return messages[:-1]  # Remove compression prompt
        summary_text = summary_response.content

        # Start fresh with summary
        return [
            HumanMessage(content=f"""Based on this API summary, generate the complete Python code for MCP tools.

{summary_text}

Generate ONLY the tool functions and helpers. Do NOT include:
- FastMCP server initialization
- The if __name__ == "__main__" block

Use the write_file tool to save the code to generated_tools.py.""")
        ]

    def _execute_tool(self, workspace: Path, tool_name: str, tool_input: dict) -> str:
        """Execute a tool and return the result."""
        try:
            if tool_name == "read_file":
                file_path = workspace / tool_input["file_path"]
                if file_path.exists():
                    content = file_path.read_text()
                    if len(content) > 10000:
                        content = content[:10000] + "\n\n[... truncated ...]"
                    return content
                return f"Error: File not found: {tool_input['file_path']}"

            elif tool_name == "list_directory":
                dir_path = workspace / tool_input["dir_path"]
                if dir_path.exists() and dir_path.is_dir():
                    files = [f.name for f in sorted(dir_path.iterdir())]
                    return "\n".join(files)
                return f"Error: Directory not found: {tool_input['dir_path']}"

            elif tool_name == "write_file":
                file_path = workspace / tool_input["file_path"]
                file_path.parent.mkdir(parents=True, exist_ok=True)
                file_path.write_text(tool_input["content"])
                return f"Successfully wrote {len(tool_input['content'])} characters to {tool_input['file_path']}"

        except Exception as e:
            return f"Error executing {tool_name}: {str(e)}"

    def _extract_code(self, workspace: Path, result: Dict[str, Any]) -> str:
        """Extract generated code from workspace or result."""

        # Debug: list what's in workspace
        print(f"   🔍 Checking workspace: {workspace}", flush=True)
        for item in workspace.iterdir():
            print(f"      - {item.name} ({'dir' if item.is_dir() else 'file'})", flush=True)

        # Check for multi-file package structure
        package_dir = workspace / "generated_tools"
        print(f"   🔍 Looking for package dir: {package_dir}", flush=True)
        print(f"      Exists: {package_dir.exists()}, Is dir: {package_dir.is_dir() if package_dir.exists() else 'N/A'}", flush=True)

        if package_dir.exists() and package_dir.is_dir():
            # List what's in the package dir
            print(f"   📂 Contents of {package_dir.name}/:", flush=True)
            for item in sorted(package_dir.iterdir()):
                print(f"      - {item.name}", flush=True)

            init_file = package_dir / "__init__.py"
            if init_file.exists():
                print("   📦 Detected multi-file package structure", flush=True)
                return self._combine_package_files(package_dir)
            else:
                print(f"   ⚠️ Package dir exists but no __init__.py found", flush=True)

        # Check for single file
        code_file = workspace / "generated_tools.py"
        if code_file.exists():
            return code_file.read_text()

        # Try to extract from output
        output = result.get("output", "")
        code_match = re.search(r'```python\n(.*?)\n```', output, re.DOTALL)
        if code_match:
            return code_match.group(1).strip() + "\n"

        return ""

    def _combine_package_files(self, package_dir: Path) -> str:
        """Combine multi-file package into single importable module."""
        combined = []

        #Read __init__.py to get the manifest
        init_file = package_dir / "__init__.py"
        init_content = ""
        if init_file.exists():
            init_content = init_file.read_text()
            # Extract manifest from docstring
            import re
            manifest_match = re.search(r'"""[\s\S]*?"""', init_content, re.DOTALL)
            if manifest_match:
                combined.append(manifest_match.group(0))
                combined.append("\n\n")

        # Collect all imports from all files
        all_imports = set()
        all_imports.add("import mcp")
        all_imports.add("import os")
        all_imports.add("import requests")
        all_imports.add("import json")

        # Scan all files for import statements
        for py_file in package_dir.glob("*.py"):
            content = py_file.read_text()
            for line in content.split('\n'):
                stripped = line.strip()
                if stripped.startswith('import ') and not stripped.startswith('from .'):
                    all_imports.add(stripped)
                elif stripped.startswith('from ') and not stripped.startswith('from .'):
                    all_imports.add(stripped)

        # Write all imports
        for imp in sorted(all_imports):
            combined.append(imp + "\n")
        combined.append("\n")

        # Read helpers.py first (contains utility functions)
        helpers_file = package_dir / "helpers.py"
        if helpers_file.exists():
            combined.append("# ============================================================\n")
            combined.append("# HELPER FUNCTIONS\n")
            combined.append("# ============================================================\n\n")
            content = helpers_file.read_text()
            # Remove import lines and relative imports
            lines = [l for l in content.split('\n')
                    if not l.strip().startswith(('import ', 'from '))]
            combined.append('\n'.join(lines))
            combined.append("\n\n")

        # Read all domain files
        py_files = sorted([f for f in package_dir.glob("*.py")
                          if f.name not in ["__init__.py", "helpers.py"]])

        for py_file in py_files:
            domain_name = py_file.stem.upper().replace("_", " ")
            combined.append(f"# ============================================================\n")
            combined.append(f"# {domain_name} TOOLS\n")
            combined.append(f"# ============================================================\n\n")

            content = py_file.read_text()
            # Remove import lines and relative imports
            lines = [l for l in content.split('\n')
                    if not l.strip().startswith(('import ', 'from '))]
            combined.append('\n'.join(lines))
            combined.append("\n\n")

        print(f"   📝 Combined {len(py_files) + 2} files into single module", flush=True)
        return ''.join(combined)

    def _get_docs_read(self, steps: List[Dict[str, Any]]) -> List[str]:
        """Get list of docs that were read."""
        docs = []
        for step in steps:
            if step.get("action") == "read_file":
                file_path = step.get("input", {}).get("file_path", "")
                if "docs/" in file_path:
                    # Extract just the filename
                    docs.append(file_path.split("docs/")[-1])
        return docs

    def _analyze_domain_coverage(self, docs_read: List[str]) -> Dict[str, Any]:
        """Analyze which API domains were covered."""
        # Extract domain from filename (e.g., api_send-message.md -> messages)
        domain_map = {
            "message": "messages",
            "stream": "streams",
            "channel": "channels",
            "user": "users",
            "reaction": "reactions",
            "upload": "media",
            "render": "formatting",
            "server": "organization",
            "status": "users",
        }

        domains = {}
        for doc in docs_read:
            # Extract the main keyword from filename
            parts = doc.replace("api_", "").replace(".md", "").split("-")
            for part in parts:
                for keyword, domain in domain_map.items():
                    if keyword in part:
                        domains[domain] = domains.get(domain, 0) + 1
                        break

        return domains

    def _breakdown_steps(self, steps: List[Dict[str, Any]]) -> Dict[str, int]:
        """Break down steps by action type."""
        breakdown = {}
        for step in steps:
            action = step.get("action", "unknown")
            breakdown[action] = breakdown.get(action, 0) + 1
        return breakdown

    def _preserve_multi_file_structure(self, package_dir: Path) -> Dict[str, str]:
        """
        Preserve multi-file package structure as a dictionary.

        Returns dict mapping relative file paths to their contents.
        """
        files = {}
        for py_file in sorted(package_dir.glob("*.py")):
            relative_path = f"generated_tools/{py_file.name}"
            files[relative_path] = py_file.read_text()

        print(f"   💾 Preserved {len(files)} source files from multi-file structure", flush=True)
        return files
