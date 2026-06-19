# Benchmark Command Reference

## Model IDs (--chomsky gateway)

```
GPT-5.2:        azure-chat-completions-gpt-5-2-2025-12-11-sandbox
GPT-5.4:        azure-chat-completions-gpt-5-4-2026-03-05-sandbox
GPT-5.4 Mini:   azure-chat-completions-gpt-5-4-mini-2026-03-17-sandbox
GPT-4.1:        azure-chat-completions-gpt-4-1-2025-04-14-sandbox
Gemini 2.5 Pro: gcp-chat-completions-chat-gemini-2.5-pro-sandbox
Gemini 3.1 Pro: gcp-chat-completions-chat-gemini-3.1-pro-preview-sandbox
Gemini 2.5 Flash: gcp-chat-completions-chat-gemini-2.5-flash-sandbox
Sonnet 4.6:     gcp-chat-completions-anthropic-claude-sonnet-4.6-sandbox
Sonnet 4.5:     gcp-chat-completions-anthropic-claude-sonnet-4.5-sandbox  (NOT provisioned)
Opus 4.6:       gcp-chat-completions-anthropic-claude-opus-4.6-sandbox
Opus 4.7:       gcp-chat-completions-anthropic-claude-opus-4.7-sandbox    (NOT provisioned)
```

**Note:** Use dots in model names (e.g. `4.6`, `3.1`), not dashes.

## Synthesis

```bash
# Docs condition (default)
uv run python benchmark/scripts/synthesize.py <dataset> \
  --model <model-id> --chomsky --advanced

# No-docs condition
uv run python benchmark/scripts/synthesize.py <dataset> \
  --model <model-id> --chomsky --advanced --no-docs

# Mutated condition (run mutate_docs.py first if docs_mutated/ missing)
uv run python benchmark/scripts/synthesize.py <dataset> \
  --model <model-id> --chomsky --advanced --mutated
```

### Examples

```bash
# Gemini 3.1 Pro — docs
uv run python benchmark/scripts/synthesize.py github \
  --model gcp-chat-completions-chat-gemini-3.1-pro-preview-sandbox \
  --chomsky --advanced

# Gemini 3.1 Pro — no-docs
uv run python benchmark/scripts/synthesize.py github \
  --model gcp-chat-completions-chat-gemini-3.1-pro-preview-sandbox \
  --chomsky --advanced --no-docs

# Gemini 3.1 Pro — mutated
uv run python benchmark/scripts/synthesize.py github \
  --model gcp-chat-completions-chat-gemini-3.1-pro-preview-sandbox \
  --chomsky --advanced --mutated

# Sonnet 4.6 — docs (6 rpm limit: 11s sleep baked in, must run sequentially)
uv run python benchmark/scripts/synthesize.py github \
  --model gcp-chat-completions-anthropic-claude-sonnet-4.6-sandbox \
  --chomsky --advanced

# GPT-5.2
uv run python benchmark/scripts/synthesize.py github \
  --model azure-chat-completions-gpt-5-2-2025-12-11-sandbox \
  --chomsky --advanced
```

## Patch mutations (before eval on mutated synth)

```bash
python benchmark/scripts/patch_mutations.py <dataset> <synth-dir-name>
# Example:
python benchmark/scripts/patch_mutations.py github \
  gcp-chat-completions-chat-gemini-3.1-pro-preview-sandbox_20260607_1612_mutated
```

Dry-run (check adherence without writing):
```bash
python benchmark/scripts/patch_mutations.py <dataset> <synth-dir-name> --dry-run
```

## Eval

```bash
python benchmark/scripts/eval_agent.py <dataset> <synth-dir-name> \
  --mode mcp \
  --model gcp-chat-completions-chat-gemini-2.5-pro-sandbox \
  --judge-model gcp-chat-completions-chat-gemini-3-flash-preview-sandbox
```

## Rate limits

| Model family | Limit | Notes |
|---|---|---|
| Gemini 3.1 Pro | ~300 rpm | Run ≤6 conditions in parallel; >9 hits 429s |
| GPT-5.x | ~60 rpm | Can parallelize 3-6 conditions safely |
| Sonnet 4.6 | 6 rpm | Must run sequentially; 11s sleep between calls |

## Parallel launch pattern (Gemini 3.1 Pro, 6 at once)

```bash
G31P="gcp-chat-completions-chat-gemini-3.1-pro-preview-sandbox"

for ds in dataset1 dataset2 dataset3; do
  for cond in "docs" "nodocs"; do
    flag=$([ "$cond" = "nodocs" ] && echo "--no-docs" || echo "")
    uv run python benchmark/scripts/synthesize.py $ds \
      --model "$G31P" --chomsky --advanced $flag \
      > /tmp/synth_g31p_${ds}_${cond}.log 2>&1 &
    sleep 2
  done
done
# Wait for those to finish, then run mutated separately
for ds in dataset1 dataset2 dataset3; do
  uv run python benchmark/scripts/synthesize.py $ds \
    --model "$G31P" --chomsky --advanced --mutated \
    > /tmp/synth_g31p_${ds}_mutated.log 2>&1 &
  sleep 2
done
```

## Sequential launch pattern (Sonnet 4.6, one at a time)

```bash
S46="gcp-chat-completions-anthropic-claude-sonnet-4.6-sandbox"

for ds in github stripe zulip; do
  uv run python benchmark/scripts/synthesize.py $ds \
    --model "$S46" --chomsky --advanced \
    > /tmp/synth_s46_${ds}_docs.log 2>&1
  echo "Done $ds docs"
done
```
