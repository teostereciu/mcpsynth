# Benchmark

## Structure

```
benchmark/
├── datasets/
│   ├── zulip/          # docs/, tests/, TASK.md
│   ├── github/         # docs/, tests/, TASK.md
│   ├── notion/         # docs/, tests/, TASK.md
│   ├── stripe/         # docs/, tests/, TASK.md
│   ├── adyen/          # docs/, tests/, TASK.md
│   ├── tiktok_shop/    # docs/, tests/, TASK.md
│   ├── slack/          # docs/ (444 pages), tests/, TASK.md
│   ├── google_sheets/      # docs/ (54 pages) — Sheets API docs (shared with google_workspace)
│   ├── google_workspace/   # docs/ (77 pages), tests/, TASK.md — Gmail, Calendar, Drive, Docs, Slides, Sheets (30 scenarios)
│   ├── jira/           # docs/ (100 pages), tests/, TASK.md
│   ├── hubspot/        # docs/ (174 pages), tests/, TASK.md
│   ├── twilio/         # docs/ (117 pages), tests/, TASK.md
│   └── zendesk/        # docs/ (149 pages), tests/, TASK.md
├── synthesizers/   # Synthesizer implementations
├── scripts/
│   ├── synthesize.py   # Run synthesis for a dataset
│   └── evaluate.py     # Run eval across models/datasets
└── configs/        # Per-dataset API credentials config
```

## Synthesizers

| File | Backend | Notes |
|------|---------|-------|
| `advanced_agentic_chomsky.py` | pychomsky | Recommended; supports advanced tools and reasoning |
| `agentic_chomsky.py` | pychomsky | Simpler agentic loop |
| `agentic_gpt5.py` | Azure GPT-5 | |
| `agentic_openrouter.py` | OpenRouter | Any model via OpenRouter |

## Evaluation

```bash
# Evaluate a specific output directory
PYTEST_IMPL_DIR=benchmark/datasets/zulip/<output-dir> \
  uv run pytest benchmark/datasets/zulip/tests/ -v

# Run synthesis + eval across models (writes output/results.json)
uv run python benchmark/scripts/evaluate.py --datasets zulip github --models claude-sonnet-4-5
```
