#!/usr/bin/env python3
"""
Quick smoke test for a vLLM / Ollama endpoint.

Sends a single tool-calling request and verifies the model:
  1. Returns a tool call (not plain text)
  2. Accepts the tool result and produces a final answer

Usage:
    uv run python benchmark/scripts/test_vllm.py --model qwen2.5:7b
    uv run python benchmark/scripts/test_vllm.py --model deepseek-r1:8b
    uv run python benchmark/scripts/test_vllm.py \\
        --model deepseek-ai/DeepSeek-R1-Distill-Qwen-32B \\
        --url http://my-gpu-host:8000/v1
"""

import argparse
import json
import sys

import openai


TOOL = {
    "type": "function",
    "function": {
        "name": "multiply",
        "description": "Multiply two integers and return the result.",
        "parameters": {
            "type": "object",
            "properties": {
                "a": {"type": "integer"},
                "b": {"type": "integer"},
            },
            "required": ["a", "b"],
        },
    },
}

PROMPT = "What is 17 multiplied by 43? Use the multiply tool."


def run(model: str, base_url: str) -> bool:
    client = openai.OpenAI(api_key="vllm", base_url=base_url, timeout=60.0)

    print(f"Model:    {model}")
    print(f"Endpoint: {base_url}")
    print(f"Prompt:   {PROMPT!r}")
    print()

    # Turn 1: expect a tool call
    print("Turn 1: sending prompt...", flush=True)
    try:
        resp = client.chat.completions.create(
            model=model,
            max_tokens=4096,  # R1-style models emit a <think> block before the tool call
            messages=[{"role": "user", "content": PROMPT}],
            tools=[TOOL],
            tool_choice="auto",
        )
    except openai.APIConnectionError as e:
        print(f"FAIL  could not connect to {base_url}: {e}")
        return False
    except Exception as e:
        print(f"FAIL  API error: {e}")
        return False

    msg = resp.choices[0].message

    if not msg.tool_calls:
        print("FAIL  model returned no tool calls.")
        print(f"      finish_reason = {resp.choices[0].finish_reason!r}")
        print(f"      content = {msg.content!r}")
        return False

    tc = msg.tool_calls[0]
    try:
        args = json.loads(tc.function.arguments)
    except json.JSONDecodeError as e:
        print(f"FAIL  tool arguments are not valid JSON: {e}")
        print(f"      raw arguments = {tc.function.arguments!r}")
        return False

    print(f"OK    tool call: {tc.function.name}({args})")
    tool_result = str(args.get("a", 0) * args.get("b", 0))
    print(f"      result = {tool_result}")

    # Turn 2: send tool result, expect a plain text answer
    print("Turn 2: sending tool result...", flush=True)
    try:
        resp2 = client.chat.completions.create(
            model=model,
            max_tokens=256,
            messages=[
                {"role": "user", "content": PROMPT},
                {
                    "role": "assistant",
                    "content": msg.content or "",
                    "tool_calls": [
                        {
                            "id": tc.id,
                            "type": "function",
                            "function": {
                                "name": tc.function.name,
                                "arguments": tc.function.arguments,
                            },
                        }
                    ],
                },
                {"role": "tool", "tool_call_id": tc.id, "content": tool_result},
            ],
            tools=[TOOL],
            tool_choice="auto",
        )
    except Exception as e:
        print(f"FAIL  second turn API error: {e}")
        return False

    final = resp2.choices[0].message.content or ""
    print(f"OK    final answer: {final.strip()!r}")

    if "731" not in final:
        print("WARN  expected '731' in final answer (17 * 43 = 731) — model may have ignored the tool result")
    else:
        print("OK    correct answer confirmed (731)")

    return True


def main():
    parser = argparse.ArgumentParser(description="Smoke-test a vLLM/Ollama tool-calling endpoint.")
    parser.add_argument("--model", default="qwen2.5:7b", help="Model name (default: qwen2.5:7b)")
    parser.add_argument(
        "--url",
        default="http://localhost:11434/v1",
        metavar="URL",
        help="Base URL of the OpenAI-compatible API (default: http://localhost:11434/v1 for Ollama)",
    )
    args = parser.parse_args()

    ok = run(model=args.model, base_url=args.url)
    print()
    print("PASS" if ok else "FAIL")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
