# Tools on Demand: Automated MCP Server Synthesis Benchmark

Code and data for the MSc AI thesis *"Tools on Demand: Automated MCP Server Synthesis and Parametric Gravity in LLM-Driven API Integration"* (University of Amsterdam, 2026).

## What is this?

This repository contains the benchmark used to evaluate whether LLMs can automatically synthesize complete, runnable MCP servers from REST API documentation — and what happens to synthesis quality when documentation conflicts with a model's training-time knowledge of the API.

The three core questions the benchmark addresses:

1. **RQ1 — Synthesis feasibility**: Can LLMs produce MCP servers that are sufficiently complete for agents to complete real API tasks?
2. **RQ2 — Documentation necessity**: Does withholding documentation hurt? (Short answer: not always — well-known APIs perform equally or better without docs.)
3. **RQ3 — Parametric gravity**: When documentation explicitly conflicts with training-time knowledge (renamed parameters), do models follow the docs or their weights?

Results are summarised in `benchmark/RESULTS.md`.

## Repository layout

```
benchmark/
  datasets/          # 14 API datasets — docs, tasks, mutations, and synth outputs
    github/
      docs/          # raw Markdown documentation fed to the synthesizer
      tasks.yaml     # evaluation tasks (what the agent is asked to do)
      mutations.json # parameter renames used in the mutated condition
      synth/         # synthesized MCP servers (one subdirectory per run)
        <model>_<timestamp>/
          server.py  # the synthesized MCP server
          ...
    stripe/ zulip/ notion/ shopify/ confluence/ jira/ mastodon/
    alphavantage/ openweathermap/ spoonacular/
    ebay_buy/ ebay_commerce/ ebay_sell/
  configs/           # sandbox API credentials template (fill in your own keys)
  scripts/           # synthesis script
  synthesizers/      # pluggable synthesizer backends (OpenRouter, vLLM)
  RESULTS.md         # full benchmark results with per-model, per-API, per-condition PASS and SYNTH
  TASK_CREATION_GUIDE.md
```

## For thesis readers

The most relevant entry points:

- **`benchmark/RESULTS.md`** — all numerical results referenced in the thesis (PASS rates, SYNTH scores, adherence rates, variance study, judge sensitivity study).
- **`benchmark/datasets/<api>/tasks.yaml`** — the evaluation tasks for each API (what the agent is asked to do with the synthesised server).
- **`benchmark/datasets/<api>/mutations.json`** — the parameter renames used in the mutated condition (the basis of the parametric gravity analysis).
- **`benchmark/datasets/<api>/synth/<model>_<timestamp>/server.py`** — example synthesized MCP servers (one per model/condition/run).
- **`benchmark/datasets/<api>/docs/`** — the raw Markdown documentation fed to the synthesizer.

## Running synthesis yourself

Requires Python 3.12+ and [uv](https://docs.astral.sh/uv/).

```bash
uv venv && uv sync
```

Copy `.env.example` to `.env` and fill in API credentials for the datasets you want to run:

```bash
ANTHROPIC_API_KEY=sk-ant-...      # for synthesis via Claude
OPENROUTER_API_KEY=sk-or-...      # for synthesis via OpenRouter
GITHUB_TOKEN=ghp_...              # for GitHub dataset evaluation
ZULIP_EMAIL=...                   # for Zulip dataset evaluation
ZULIP_API_KEY=...
ZULIP_SITE=https://your-org.zulipchat.com
# See benchmark/configs/ for full list of required keys per dataset
```

```bash
# Synthesize a Zulip MCP server (docs condition, Claude via Anthropic API)
uv run python benchmark/scripts/synthesize.py zulip

# Synthesize without providing documentation (no-docs condition)
uv run python benchmark/scripts/synthesize.py zulip --no-docs

# Synthesize with mutated parameter names (mutated condition)
uv run python benchmark/scripts/synthesize.py zulip --mutated

# Use OpenRouter (supports any model OpenRouter carries)
uv run python benchmark/scripts/synthesize.py zulip \
    --model google/gemini-2.5-pro --openrouter

# List available datasets
uv run python benchmark/scripts/synthesize.py --list
```

Output is written to `benchmark/datasets/<dataset>/synth/<model>_<timestamp>/`.

## Note on evaluation harness

The agent evaluation harness used in the thesis relied on an internal LLM gateway and is not included here. The synthesized server outputs, task definitions, and RESULTS.md contain all the data needed to reproduce the analysis. If you want to run evaluation against a synthesized server, you can connect any MCP-compatible client to the `server.py` output directly.
