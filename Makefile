# Benchmark Makefile
#
# Synthesis:
#   make synth DATASET=clockify
#   make synth-nodocs DATASET=zulip
#   make synth-source DATASET=mastodon      # open-source APIs (uses source/ dir)
#   make synth-cli DATASET=notion           # CLI condition
#
# Evaluation:
#   make eval DATASET=clockify IMPL=<synth-dir-name>
#   make eval-cli DATASET=notion_cli IMPL=<synth-dir-name>
#
# Bulk synthesis (all core datasets, docs condition):
#   make synth-all
#
# Variables:
#   DATASET   — dataset name (e.g. github, clockify, mastodon)
#   IMPL      — synth dir name for eval (e.g. azure-chat-completions-gpt-5-2-2025-12-11-sandbox_20260512_1234)
#   MODEL     — model alias or full ID (default: GPT5.2)
#               Aliases: GPT5.2, GPT52, GPT4.1, GPT41, Gemini25, Gemini3Flash, Sonnet
#   MAX_TURNS — override max turns for synthesis (default: 50)

PYTHON     := uv run python
SYNTH      := benchmark/scripts/synthesize.py
EVAL       := benchmark/scripts/eval_agent.py

# Model shortcuts — override with MODEL=<id> or use a shortcut target
GPT52      := azure-chat-completions-gpt-5-2-2025-12-11-sandbox
GPT41      := azure-chat-completions-gpt-4-1-2025-04-14-sandbox
GEMINI25   := gcp-chat-completions-chat-gemini-2.5-pro-sandbox

MODEL       ?= $(GPT52)
AGENT_MODEL ?= $(GEMINI25)
MAX_TURNS   ?= 50
DATASET     ?= github
DATASETS    ?= $(MCP_DATASETS)
IMPL        ?=
SYNTH_FLAGS := --chomsky --advanced

# Core MCP datasets (docs condition)
MCP_DATASETS := github notion stripe slack zulip openweathermap jira clockify mastodon spoonacular alphavantage forgejo

# Source-condition datasets (open-source APIs)
SOURCE_DATASETS := mastodon forgejo

# CLI datasets
CLI_DATASETS := github_cli notion_cli zulip_cli mastodon_cli forgejo_cli

.PHONY: synth synth-docs synth-nodocs synth-cli \
        synth-gpt41 synth-gemini \
        eval eval-cli eval-json eval-cli-json \
        synth-all synth-all-gpt41 synth-all-gemini synth-all-nodocs \
        help

# ── Synthesis ────────────────────────────────────────────────────────────────

# Default: source/ if present, else docs/
synth:
	$(PYTHON) $(SYNTH) $(DATASET) --model $(MODEL) --max-turns $(MAX_TURNS) $(SYNTH_FLAGS)

# Force docs-based synthesis even when source/ exists (gets _docs suffix)
synth-docs:
	$(PYTHON) $(SYNTH) $(DATASET) --model $(MODEL) --max-turns $(MAX_TURNS) --docs $(SYNTH_FLAGS)

synth-nodocs:
	$(PYTHON) $(SYNTH) $(DATASET) --model $(MODEL) --max-turns $(MAX_TURNS) --no-docs $(SYNTH_FLAGS)

synth-mutated:
	$(PYTHON) $(SYNTH) $(DATASET) --model $(MODEL) --max-turns $(MAX_TURNS) --mutated $(SYNTH_FLAGS)

synth-source:
	$(PYTHON) $(SYNTH) $(DATASET) --model $(MODEL) --max-turns $(MAX_TURNS) --source $(SYNTH_FLAGS)

synth-cli:
	$(PYTHON) $(SYNTH) $(DATASET) --model $(MODEL) --max-turns $(MAX_TURNS) $(SYNTH_FLAGS)

# Model shortcut targets
synth-gpt41:
	$(PYTHON) $(SYNTH) $(DATASET) --model $(GPT41) --max-turns $(MAX_TURNS) $(SYNTH_FLAGS)

synth-gemini:
	$(PYTHON) $(SYNTH) $(DATASET) --model $(GEMINI25) --max-turns $(MAX_TURNS) $(SYNTH_FLAGS)

# ── Evaluation ───────────────────────────────────────────────────────────────

eval:
	@test -n "$(IMPL)" || (echo "Error: IMPL is required. Usage: make eval DATASET=clockify IMPL=<synth-dir>"; exit 1)
	$(PYTHON) $(EVAL) $(DATASET) $(IMPL) --model $(AGENT_MODEL)

eval-cli:
	@test -n "$(IMPL)" || (echo "Error: IMPL is required. Usage: make eval-cli DATASET=notion_cli IMPL=<synth-dir>"; exit 1)
	$(PYTHON) $(EVAL) $(DATASET) $(IMPL) --mode cli --model $(AGENT_MODEL)

eval-json:
	@test -n "$(IMPL)" || (echo "Error: IMPL is required."; exit 1)
	$(PYTHON) $(EVAL) $(DATASET) $(IMPL) --model $(AGENT_MODEL) --json \
		--output benchmark/output/$(DATASET)__$(IMPL)__agent-$(AGENT_MODEL).json

eval-cli-json:
	@test -n "$(IMPL)" || (echo "Error: IMPL is required."; exit 1)
	$(PYTHON) $(EVAL) $(DATASET) $(IMPL) --mode cli --model $(AGENT_MODEL) --json \
		--output benchmark/output/$(DATASET)__$(IMPL)__agent-$(AGENT_MODEL).json

# ── Bulk synthesis ────────────────────────────────────────────────────────────

synth-all:
	@for ds in $(DATASETS); do \
		echo "=== Synthesizing $$ds (docs) ==="; \
		$(PYTHON) $(SYNTH) $$ds --model $(MODEL) --max-turns $(MAX_TURNS) $(SYNTH_FLAGS); \
	done

synth-all-gpt41:
	$(MAKE) synth-all MODEL=$(GPT41)

synth-all-gemini:
	$(MAKE) synth-all MODEL=$(GEMINI25)

synth-all-nodocs:
	@for ds in $(DATASETS); do \
		echo "=== Synthesizing $$ds (nodocs) ==="; \
		$(PYTHON) $(SYNTH) $$ds --model $(MODEL) --max-turns $(MAX_TURNS) --no-docs $(SYNTH_FLAGS); \
	done

# ── Help ─────────────────────────────────────────────────────────────────────

help:
	@echo "Usage:"
	@echo "  make synth         DATASET=<name>              Synthesize (source/ if present, else docs/)"
	@echo "  make synth-docs    DATASET=<name>              Force docs-based synthesis (_docs suffix)"
	@echo "  make synth-nodocs  DATASET=<name>              Zero-context synthesis (_nodocs suffix)"
	@echo "  make synth-cli     DATASET=<name>              Synthesize CLI tool"
	@echo "  make eval          DATASET=<name> IMPL=<dir>   Evaluate an MCP server"
	@echo "  make eval-cli      DATASET=<name> IMPL=<dir>   Evaluate a CLI tool"
	@echo "  make eval-json     DATASET=<name> IMPL=<dir>   Evaluate MCP server and write JSON results"
	@echo "  make eval-cli-json DATASET=<name> IMPL=<dir>   Evaluate CLI tool and write JSON results"
	@echo "  make synth-all                                  Synthesize all MCP datasets (docs)"
	@echo "  make synth-all-nodocs                           Synthesize all MCP datasets (nodocs)"
	@echo ""
	@echo "Variables:"
	@echo "  DATASET    Dataset name (e.g. github, clockify, mastodon)"
	@echo "  IMPL       Synth directory name (required for eval targets)"
	@echo "  MODEL      Model to use for synthesis (default: $(MODEL))"
	@echo "  MAX_TURNS  Max agent turns for synthesis (default: $(MAX_TURNS))"
	@echo ""
	@echo "MCP datasets:    $(MCP_DATASETS)"
	@echo "Source datasets: $(SOURCE_DATASETS)"
	@echo "CLI datasets:    $(CLI_DATASETS)"
