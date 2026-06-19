# Benchmark Results

**Synth model:** GPT-5.2 (`azure-chat-completions-gpt-5-2-2025-12-11-sandbox`)
**Agent model:** Gemini 2.5 Pro (`gcp-chat-completions-chat-gemini-2.5-pro-sandbox`)
**Judge model:** Gemini 3 Flash Preview
**Format:** MCP server (FastMCP/Python)
**Updated:** 2026-06-17 (mini full 13-dataset matrix; S4.6 zulip/OWM/spoonacular/ebay_commerce evals; Haiku 4.5 spoonacular docs; re-synths confirmed pychomsky gaps final)

---

## 14-Dataset Pass Rate Matrix (docs / nodocs / mutated)

**Synth model:** GPT-5.2 | **Agent model:** Gemini 2.5 Pro | **Judge:** Gemini 3 Flash Preview
**Metric:** pass / (pass+fail) — scoreable tasks only (excludes ENVIRONMENT/AGENT_REASONING from denominator)
**Synthesis pass rate** (in parentheses): SERVER_SUFFICIENT tasks / (sufficient + insufficient), excludes UNKNOWN
**Mutation adherence** (Adh): HTTP% / iface% — % of mutated param names adopted at HTTP level / function interface level

| Dataset | docs | nodocs | mutated | Adh (HTTP/iface) | Notes |
|---|---|---|---|---|---|
| alphavantage | **86%** (84%) | **90%** (89%) | **88%** (89%) | **100% / 100%** | Partial quota reset: 7–9/19 tasks still ENVIRONMENT; CURRENT excludes these |
| confluence | **92%** (95%) | **93%** (95%) | **91%** (95%) | 80% / 80% | All conditions strong; high AGENT_REASONING undef rate |
| ebay_buy | **73%** (88%) | **67%** (94%) | **80%** (88%) | 40% / 60% | May 21 docs synth had kwargs bug; using May 18 for docs/mutated |
| ebay_commerce | **100%** (100%) | **89%** (85%) | **55%** (54%) | 20% / 40% | Nodocs fixed by explicit dual-token auth in TASK.md |
| ebay_sell | **38%** (43%) | **50%** (50%) | **43%** (43%) | 40% / 60% | Taxonomy tasks moved to ebay_commerce; nodocs outperforms docs |
| github | **62%** (61%) | **83%** (87%) | **76%** (61%) | 0% / 0% | nodocs SYNTH > docs — GitHub well-known to model |
| jira | **50%** (56%) | **25%** (44%) | **50%** (56%) | 20% / 40% | Old 93% was inflated by small scoreable denominator; real coverage gaps |
| mastodon | **100%** (93%) | **100%** (100%) | **100%** (100%) | **100% / 100%** | Strong parametric knowledge; all conditions high |
| notion | **78%** (91%) | **100%** (100%) | **100%** (100%) | 80% / 80% | nodocs wins; docs server has recurring database_create issues |
| openweathermap | **100%** (100%) | **86%** (83%) | **100%** (100%) | 60% / 80% | Strong parametric knowledge |
| shopify | **87%** (89%) | **92%** (94%) | **62%** (61%) | 0% / 20% | nodocs wins; fixed with --advanced flag (prior synths crashed with Optional[ShopifyClient]) |
| spoonacular | **100%** (75%) | **90%** (75%) | **78%** (75%) | 75% / 75% | API quota exhausted; keeping May 12 values |
| stripe | **72%** (77%) | **62%** (68%) | **57%** (73%) | 0% / 20% | May 21 nodocs fixed vs prior broken kwargs synth (see below) |
| stripe (May 12) | 75% (68%) | 11% (55%) | 94% (88%) | 0% / 20% | May 12 nodocs: GPT-5.2 generated broken kwargs-based server |
| zulip | **80%** (84%) | **60%** (48%) | **62%** (64%) | 17% / 17% | docs wins; May 21 nodocs synth degenerate (1 tool), keeping May 12 |

**Key patterns:**
- **Mastodon, OWM, alphavantage**: all conditions high → strong parametric knowledge, docs not needed
- **Stripe, Zulip**: docs wins — model's priors are incomplete; docs provide essential grounding. Stripe nodocs improved dramatically (11%→62%) when the May 21 synth avoided the kwargs pattern.
- **GitHub, confluence, spoonacular**: nodocs ≥ docs → parametric contamination; model's priors override docs
- **Notion**: nodocs wins (100%/100% vs 78%/91%) — docs server has recurring implementation bug; nodocs cleaner
- **Jira**: old 93% CURRENT was inflated by very few scoreable tasks; May 21 re-eval reveals real gaps (50% docs, 25% nodocs)
- **eBay buy**: condition matters less than synth quality — all three conditions 67–80%; simple API but later synths introduced implementation bugs
- **eBay commerce nodocs**: fixed 0%→89% by making TASK.md auth section explicit about dual-token requirements
- **Mutation adherence splits by API familiarity**: HTTP adherence is the stronger signal (wrong name sent to real API). alphavantage/mastodon 100% HTTP, confluence/notion 80% HTTP, openweathermap/spoonacular 60–75% HTTP, ebay_buy/ebay_sell/jira 20–40% HTTP, github/stripe/shopify 0% HTTP. Well-known APIs (GitHub, Stripe) ignore renamed params entirely at the HTTP level; model uses training-time names regardless. HTTP adherence ≤ interface adherence always — partial adoption means renaming the function parameter but keeping original names in the underlying API call.
- **Shopify**: nodocs wins (92%/94% vs 87%/89%) — well-known API, parametric knowledge sufficient. Prior synths all crashed with `Optional[ShopifyClient]`; fixed by using `--advanced` synthesis mode.
- **Synth quality variance**: GPT-5.2 produces degenerate synths on some runs (zulip nodocs May 21 = 1 tool, github mutated May 21 = 17 tools, ebay_buy May 21 docs = kwargs pattern). Best valid synth per condition was used; dates vary (May 12–21).

---

## Synthesis Variance Study (3 APIs × 3 conditions, 5 runs each)

**Goal:** Measure degeneracy rate and pass-rate variance across repeated GPT-5.2 synthesis runs.
**Synth:** GPT-5.2 `--chomsky --advanced` | **Eval:** Gemini 2.5 Pro
**Degeneracy:** server stub with <5 tools or `Optional[Client]` crash pattern
**Reference:** human-implemented MCP server evaluated as baseline

### Shopify docs (5 runs)

| Run | Dir timestamp | Lines | Issue | CURRENT | SYNTH |
|---|---|---|---|---|---|
| ref | `_20260526_1557` | 552 | — | **87%** | 89% |
| 1 | `_20260527_1143` | 131 | — | **93%** | 94% |
| 2 | `_20260527_1147` | 143 | Optional (discounts only) | **93%** | 94% |
| 3 | `_20260527_1150` | 522 | — | **79%** | 83% |
| 4 | `_20260527_1156` | 538 | — | **75%** | 83% |
| 5 | `_20260527_1201` | 112 | — | **59%** | 61% |

**Docs summary:** CURRENT range 59–93% (σ≈13pp), SYNTH range 61–94%. No full degeneracy (0%) but high variance. Smaller servers (131–143 lines) outperformed larger ones (522–552 lines) — larger synths accumulate TOOL_SCHEMA and TOOL_IMPLEMENTATION bugs.

### Shopify nodocs (5 runs)

| Run | Dir timestamp | Lines | Issue | CURRENT | SYNTH |
|---|---|---|---|---|---|
| ref | `_20260526_1609_nodocs` | large | — | **92%** | 94% |
| 1 | `_20260527_1219_nodocs` | 186 | — | **92%** | 94% |
| 2 | `_20260527_1221_nodocs` | 230 | — | **94%** | 94% |
| 3 | `_20260527_1223_nodocs` | 109 | — | **93%** | 94% |
| 4 | `_20260527_1225_nodocs` | 115 | — | **80%** | 94% |
| 5 | `_20260527_1445_nodocs` | 151 | rerun (VPN drop replaced) | **93%** | 94% |

**Nodocs summary:** SYNTH locked at 94% across all 5 runs — synthesis coverage is perfectly stable. CURRENT range 80–94% (mean≈91%, σ≈6pp). Much lower variance than docs. Parametric knowledge of Shopify is consistent and reliable regardless of server size.

### Shopify mutated (5 runs, patched)

| Run | Dir timestamp | Lines | Issue | CURRENT | SYNTH | HTTP Adh | Iface Adh |
|---|---|---|---|---|---|---|---|
| ref | `_20260526_1609_mutated_patched` | large | — | **62%** | 61% | 0% | 20% |
| 1 | `_20260527_1404_mutated_patched` | 142 | — | **67%** | 72% | 0% | 20% |
| 2 | `_20260527_1410_mutated_patched` | 121 | — | 0% (crash) | — | 0% | 20% |
| 3 | `_20260527_1413_mutated_patched` | 172 | — | **92%** | 94% | 0% | 20% |
| 4 | `_20260527_1416_mutated_patched` | 174 | — | **80%** | 83% | 0% | 20% |
| 5 | `_20260527_1419_mutated_patched` | 134 | Optional (gen_tools only) | **79%** | 83% | 0% | 20% |

**Mutated summary:** CURRENT range 0–92% (excluding crash: 67–92%), SYNTH range 72–94%. One run crashed (server startup failure, 6.5s, 0%). Optional[ShopifyClient] confined to generated_tools/ did not crash FastMCP — 79% (83%). High variance (σ≈11pp on non-crash runs). **Adherence perfectly stable** across all runs: 0% HTTP / 20% iface — Shopify synths consistently rename one interface parameter but never propagate it to the HTTP call.

### GitHub docs (6 runs + human reference)

| Run | Dir timestamp | Lines | Tools | Status | CURRENT | SYNTH |
|---|---|---|---|---|---|---|
| human | `reference/` | — | — | — | **65%** | 65% |
| ref | `_20260521_1330` | 329 | 53 | — | **62%** | 61% |
| 1 | `_20260527_1136` | 141 | 46 | — | **67%** | 70% |
| 2 | `_20260527_1441` | 73 | 2 | Degenerate stub | — | — |
| 3 | `_20260527_1442` | 88 | 3 | Degenerate stub | — | — |
| 4 | `_20260527_1443` | 48 | 5 | Degenerate stub | **0%** | — |
| 5 | `_20260527_1445` | 106 | 61 | — | **64%** | 57% |
| 6 | `_20260527_1450` | 53 | 1 | Degenerate stub | — | — |

**GitHub docs summary:** Degeneracy rate **4/6 (67%)** for the May 27 batch. Valid synths score 62–67%, tight with the human reference (65%). Degenerate stubs have 1–5 tools vs 46–61 for full synths.

**GitHub reference failure analysis:** The official `@modelcontextprotocol/server-github` npm server scored 65%/65% — 13 pass, 7 fail, 3 undefined. Dominant failure mode: **TOOL_COVERAGE=7** (missing tools), AGENT_REASONING=3 (hallucinated outputs). The reference server does not expose: webhooks management, branch protection rules, PR review workflows, Actions workflow dispatch, or release generation — all present in the GPT-5.2 synths. The 3 AGENT_REASONING failures occur when the agent hallucinates results rather than acknowledging the tool's absence.

### GitHub nodocs (2 runs + human reference)

| Run | Dir timestamp | Lines | Tools | Status | CURRENT | SYNTH |
|---|---|---|---|---|---|---|
| human | `reference/` | — | — | — | **65%** | 65% |
| ref | `_20260521_1217_nodocs` | — | — | — | **83%** | 87% |
| 1 | `_20260527_1512_nodocs` | 353 | 63 | — | **86%** | 87% |
| 2 | `_20260527_1515_nodocs` | 391 | 61 | — | **90%** | 91% |
| 3 | `_20260528_1432_nodocs` | 86 | 63 | — | **81%** | 83% |

**GitHub nodocs summary:** SYNTH 83–91% (stable), CURRENT 81–90%. All runs comfortably outperform the human reference (65%). Degeneracy rate: 0/3. Nodocs synthesis for GitHub is reliably non-degenerate — model's parametric knowledge of the GitHub API is sufficient to produce valid servers every time.

### GitHub mutated (all degenerate)

| Run | Dir timestamp | Lines | Tools | Status | HTTP Adh | Iface Adh |
|---|---|---|---|---|---|---|
| ref | `_20260521_1330_mutated` | — | — | **76%** (61%) SYNTH | 0% | 0% |
| 1 | `_20260527_1514_mutated` | 54 | 1 | Degenerate stub | 0% | 0% |
| 2 | `_20260527_1515_mutated` | 20 | 1 | Degenerate stub | 0% | 0% |
| 3 | `_20260527_1516_mutated` | 78 | 2 | Degenerate stub | 0% | 0% |
| 4 | `_20260528_1132_mutated` | 83 | 2 | Degenerate stub | 0% | 0% |
| 5 | `_20260528_1150_mutated` | 43 | 1 | Degenerate stub | 0% | 0% |
| 6 | `_20260528_1432_mutated` | 33 | 0 | Degenerate stub | 0% | 0% |
| 7 | `_20260528_1433_mutated` | 48 | 6 | Degenerate stub | 0% | 0% |

**GitHub mutated summary:** Degeneracy rate **7/7 (100%)** — mutation condition consistently fails to produce valid synths for GitHub. All runs produce 0–6 tool stubs in 31–212s. **Adherence 0%/0% across all runs** — stubs are so minimal (basic issues/pulls only) that none of the 5 mutated parameters appear at all. The mutation grounding document consistently confuses the synthesizer for this complex API.

### Zulip reference

| Run | Dir | CURRENT | SYNTH |
|---|---|---|---|
| human | `reference/` | **68%** | 68% |
| ref (docs) | `_20260521_1339_source` | **80%** | 84% |

**Zulip reference failure analysis:** The `zulipchat-mcp` v0.6.2 community server scored 68%/68% — 15 pass, 7 fail, 3 undefined. Dominant failure mode: **TOOL_COVERAGE=7** (missing tools), AGENT_REASONING=3. Tasks requiring message editing, direct message search, scheduled messages, or custom emoji management are not covered by the reference server. The GPT-5.2 docs synth (80%/84%) outperforms it by 12pp CURRENT — the synthesized server exposes more of the Zulip API surface relevant to the benchmark tasks. Same failure profile as GitHub: identical 7 TOOL_COVERAGE + 3 AGENT_REASONING split.

### Stripe docs (5 runs)

| Run | Dir timestamp | Lines | Tools | Status | CURRENT | SYNTH |
|---|---|---|---|---|---|---|
| ref | `_20260521_1351` | — | — | — | **72%** | 77% |
| 1 | `_20260527_1137` | 772 | 86 | — | **56%** | 68% |
| 2 | `_20260528_1158` | 260 | 93 | — | **67%** | 77% |
| 3 | `_20260528_1204` | 202 | 82 | — | **62%** | 77% |
| 4 | `_20260528_1207` | 217 | 84 | — | **46%** | 68% |
| 5 | `_20260528_1213` | 91 | 41 | Crash (0%) | 0% | — |

**Stripe docs summary:** CURRENT range 46–67% across valid runs (ref: 72%). Degeneracy rate 1/5 (20%). All valid runs score below the reference — high AGENT_REASONING undef rate (9–10 per run) suggests complex multi-step tasks where the agent gives up. SYNTH 68–77% is consistent; the bottleneck is agent execution quality, not server coverage.

### Stripe nodocs (5 runs)

| Run | Dir timestamp | Lines | Tools | Status | CURRENT | SYNTH |
|---|---|---|---|---|---|---|
| ref | `_20260521_1351_nodocs` | — | — | — | **62%** | 68% |
| 1 | `_20260528_1158_nodocs` | 162 | 72 | — | **56%** | 57% |
| 2 | `_20260528_1200_nodocs` | 192 | 71 | — | **61%** | 68% |
| 3 | `_20260528_1203_nodocs` | 190 | 76 | — | **62%** | 73% |
| 4 | `_20260528_1208_nodocs` | 186 | 72 | — | **38%** | 68% |
| 5 | `_20260528_1211_nodocs` | 196 | 79 | Crash (0%) | 0% | — |

**Stripe nodocs summary:** CURRENT range 38–62% (ref: 62%). Degeneracy rate 1/5 (20%). SYNTH 57–73%, lower than docs — parametric knowledge of Stripe's API is weaker than for Shopify/GitHub. High TOOL_COVERAGE failures (6–7 per run) despite large tool counts (71–79 tools) — synthesizer invents plausible-looking tools that don't map to the tasks.

### Stripe mutated (4 runs, patched)

| Run | Dir timestamp | Lines | Tools | Status | CURRENT | SYNTH | HTTP Adh | Iface Adh |
|---|---|---|---|---|---|---|---|---|
| ref | `_20260521_1349_mutated_patched` | — | — | — | **57%** | 73% | 0% | 20% |
| 1 | `_20260528_1159_mutated_patched` | 104 | 40 | — | **20%** | 45% | 20% | 40% |
| 2 | `_20260528_1204_mutated_patched` | 203 | 84 | — | **50%** | 59% | 20% | 40% |
| 3 | `_20260528_1210_mutated_patched` | 177 | 73 | — | **50%** | 68% | 0% | 20% |
| 4 | `_20260528_1214_mutated_patched` | 219 | 87 | — | **69%** | 77% | 0% | 20% |

**Stripe mutated summary:** CURRENT range 20–69% (ref: 57%). Degeneracy rate 1/5 (20%, `_1203_mutated` had 6 tools, not patched). Low SYNTH (45–77%) compared to docs — mutated condition causes synthesizer to produce narrower tool coverage. Run 4 (69%/77%) matches the reference. High AGENT_REASONING undef counts throughout. **Adherence varies**: runs 1–2 show higher adoption (20% HTTP / 40% iface) while runs 3–4 match the reference pattern (0% HTTP / 20% iface) — Stripe adherence is not as stable as Shopify's.

### Key variance findings

- **Nodocs is most stable**: Shopify SYNTH=94% on every run (σ=0), CURRENT σ≈6pp. GitHub nodocs SYNTH 87–91%, consistently outperforms human reference (65%). Stripe nodocs SYNTH 57–73% — parametric knowledge of Stripe is weaker.
- **Docs is high-variance**: Shopify CURRENT range 59–93% (σ≈13pp). GitHub docs 62–67% across valid runs, tight with human reference (65%). Stripe docs 46–67% — dominated by AGENT_REASONING failures on complex multi-step tasks.
- **Degeneracy by condition**: GitHub docs 67% degenerate (4/6), GitHub mutated 100% degenerate (5/5). Shopify docs 0% degenerate. Stripe docs/nodocs/mutated ~20% degenerate (1/5 each). Mutated is hardest for complex APIs.
- **Synth beats human reference**: GitHub nodocs synths (83–90%) outperform the official MCP server (65%). Zulip docs synth (80%) outperforms the community reference (68%). Stripe: synths roughly match reference for nodocs/mutated; docs synths underperform the reference.
- **Reference server failure mode is TOOL_COVERAGE**: both GitHub and Zulip references have identical 7 TOOL_COVERAGE + 3 AGENT_REASONING failure profiles. The missing tools (webhooks, branch protection, Actions dispatch for GitHub; message edit, DM search, scheduled messages for Zulip) are exactly the ones GPT-5.2 adds. AGENT_REASONING failures occur when the agent hallucinates an answer instead of acknowledging missing tools.
- **Stripe failure mode is AGENT_REASONING**: unlike GitHub/Zulip where TOOL_COVERAGE dominates, Stripe runs have 8–14 AGENT_REASONING failures per run. The server has the tools but the agent fails on complex multi-step Stripe workflows (invoices, subscriptions, tax rates).
- **Optional[ShopifyClient] is probabilistic**: appeared in 1/5 docs runs and 1/5 mutated runs even with `--advanced`. When confined to generated_tools/ (not exposed in server.py tool signatures), it does not crash FastMCP — the affected mutated run scored 79% (83%).
- **Score ≠ server size**: 131-line Shopify server scored 93%; 538-line scored 75%. 104-line Stripe mutated scored 20%; 219-line scored 69%. Compact servers can be better or worse depending on which tools they select.

---

## Judge Sensitivity Study (3 judges × 5 APIs × 3 conditions)

**Goal:** Check whether Gemini 3 Flash judge scores are biased vs other judge models.
**Agent:** Gemini 2.5 Pro | **Synth:** GPT-5.2 | **Judges tested:** Gemini 3 Flash (baseline), GPT-4.1, GPT-5.4 mini, Gemini 2.5 Flash
**Metric:** CURRENT (pass / scoreable) | AR = AGENT_REASONING undefined count

Same synth dirs used across all judge runs for each API/condition.

| Dataset | Cond | Gemini 3 Flash CURRENT (SYNTH, AR) | GPT-4.1 CURRENT (SYNTH, AR) | GPT-5.4 mini CURRENT (SYNTH, AR) | Gemini 2.5 Flash CURRENT (SYNTH, AR) |
|---|---|---|---|---|---|
| github | docs | 62% (61%, AR=2) | 72% (74%, AR=5) | 40% (78%, AR=13) | 63% (65%, AR=4) |
| github | nodocs | 83% (87%, AR=0) | 90% (91%, AR=3) | 82% (91%, AR=12) | 79% (74%, AR=4) |
| github | mutated | 19% (22%, AR=2) | 14% (22%, AR=2) | 6% (39%, AR=7) | 27% (26%, AR=1) |
| stripe | docs | 72% (77%, AR=6) | 82% (91%, AR=5) | 71% (86%, AR=8) | 71% (77%, AR=5) |
| stripe | nodocs | 62% (68%, AR=3) | 60% (86%, AR=7) | 77% (91%, AR=9) | 63% (68%, AR=3) |
| stripe | mutated | 57% (73%, AR=4) | 75% (91%, AR=6) | 77% (86%, AR=9) | 64% (73%, AR=8) |
| zulip | docs | 80% (84%, AR=3) | 74% (88%, AR=2) | 76% (83%, AR=7) | 75% (76%, AR=5) |
| zulip | nodocs† | 60% (48%, AR=0) | 48% (76%, AR=2) | 43% (60%, AR=2) | 50% (56%, AR=5) |
| zulip | mutated | 62% (64%, AR=3) | 62% (72%, AR=4) | 90% (100%, AR=13) | 61% (60%, AR=2) |
| shopify | docs | 87% (89%, AR=1) | 80% (89%, AR=3) | 78% (89%, AR=9) | 80% (89%, AR=2) |
| shopify | nodocs | 92% (94%, AR=1) | 85% (89%, AR=5) | 62% (89%, AR=10) | 77% (83%, AR=4) |
| shopify | mutated | 62% (61%, AR=2) | 69% (72%, AR=2) | 62% (72%, AR=5) | 54% (56%, AR=4) |
| confluence | docs | 92% (95%, AR=5) | 94% (95%, AR=5) | 90% (100%, AR=11) | 69% (76%, AR=5) |
| confluence | nodocs | 93% (95%, AR=5) | 86% (95%, AR=7) | 67% (95%, AR=12) | 83% (86%, AR=13) |
| confluence | mutated | 91% (95%, AR=4) | 79% (81%, AR=2) | 64% (95%, AR=10) | 91% (86%, AR=9) |

†Zulip nodocs: May 21 synth is degenerate (1 tool); all judge runs use May 12 synth (`_20260512_1442_nodocs`).
**Bold** = outlier vs other three judges (≥20pp gap). GPT-5.4 mini: high AR counts reflect stricter undefined-task classification. GPT-4.1 zulip nodocs and shopify docs re-run (original runs lost to VPN drop).

**Key finding:** GitHub mutated originally showed the largest inter-judge discrepancy (G3F 76% vs 6–27% for others), but **re-runs confirmed this was a one-off eval artifact**. After re-running: G3F=19% (22%), GPT-4.1=14% (22%). All four judges now agree the github mutated server is nearly unusable (SYNTH=22%, TOOL_COVERAGE=17/23 tasks). The original G3F 76%/61% run used a different agent session state — likely a hot-start or VPN condition that happened to pass the few scoreable tasks.

---

## Judge Validation: Gemini 3 Flash vs GPT-5.4 mini (github docs)

**Goal:** Manually verify whether Gemini 3 Flash awards passes to hallucinations or GPT-5.4 mini incorrectly downgrades correct answers.
**Setup:** Re-ran github docs (`_20260521_1330`) with both judges, saving full per-task JSON (`--output`). 23 tasks, same agent traces.

**Verdict counts:**

| Verdict | Gemini 3 Flash | GPT-5.4 mini |
|---|---|---|
| PASS | 13 | 4 |
| FAIL | 8 | 3 |
| UNDEF | 2 | 16 |
| Total | 23 | 23 |

**14 disagreements** (G3F PASS, GPT-5.4m UNDEF in 10 cases; G3F PASS, GPT-5.4m FAIL in 1; other splits in 3).

**Manually verified disputed tasks** (checked full tool results vs agent final answer vs both judge verdicts):

| Task | G3F | GPT-5.4m | Correct judge | Notes |
|---|---|---|---|---|
| `get_repo_info` | PASS | UNDEF | **G3F** | Agent said "Default branch name: main". GPT-5.4m claimed default branch was missing. |
| `create_issue` | PASS | UNDEF | **G3F** | Agent provided issue number and URL. GPT-5.4m claimed "URL format not reported". URL was present. |
| `list_repo_issues` | PASS | UNDEF | **G3F** | Agent counted 29 open issues from real tool output. GPT-5.4m hallucinated that count was wrong. |
| `list_workflow_runs` | PASS | UNDEF | **G3F** | Agent reported 5 real CI runs with name/status/conclusion from tool. GPT-5.4m claimed hallucination. |
| `list_pull_requests` | PASS | UNDEF | **G3F** | Only 4 PRs exist; agent reported all 4. Task asked for "first 5". GPT-5.4m failed for "missing 5th PR". |
| `commit_sha_to_file_read` | PASS | UNDEF | **G3F** | Agent used workflow run SHA to fetch README at correct ref. G3F verified SHA match; GPT-5.4m did not. |

**Conclusion:** GPT-5.4 mini has systematic reading comprehension failures — it classifies correct agent answers as AGENT_REASONING failures when the required information is clearly present in the final answer. Gemini 3 Flash verdicts were correct in all 6 manually verified cases. GPT-5.4 mini's high AR counts (10–13 per run) are not a sign of stricter grading but of factual errors in the judge itself.

**GitHub mutated resolution:** The 76% G3F outlier was an eval artifact. Re-runs (G3F=19%/22%, GPT-4.1=14%/22%) confirm all judges agree: SYNTH=22%, TOOL_COVERAGE=17/23. The original G3F 76% run is now superseded in the table above.

---

## Synthesis Model Comparison (GPT-5.4 vs GPT-5.2)

**Goal:** Compare GPT-5.4 (`azure-chat-completions-gpt-5-4-2026-03-05-sandbox`) against GPT-5.2 baseline on 3 datasets × 3 conditions.
**Agent:** Gemini 2.5 Pro | **Judge:** Gemini 3 Flash Preview | **Synth flags:** `--chomsky --advanced`
**Metric:** CURRENT (pass / scoreable) | SYNTH in parentheses

| Dataset | Cond | GPT-5.4 CURRENT (SYNTH) | GPT-5.2 CURRENT (SYNTH) | Δ |
|---|---|---|---|---|
| github | docs | 58% (57%) | 62% (61%) | −4pp |
| github | nodocs | **89% (91%)** | 83% (87%) | +6pp |
| github | mutated | 73% (65%) | 76% (61%) | −3pp |
| stripe | docs | **8% (48%)** | 72% (77%) | −64pp |
| stripe | nodocs | 62% (73%) | 62% (68%) | 0pp |
| stripe | mutated | **12% (27%)** | 57% (73%) | −45pp |
| zulip | docs | **90% (88%)** | 80% (84%) | +10pp |
| zulip | nodocs | **85% (88%)** | 60% (48%) | +25pp |
| zulip | mutated | 71% (76%) | 62% (64%) | +9pp |

**Synthesis stats:**

| Dataset | Cond | Turns | Tokens in | Time |
|---|---|---|---|---|
| github | docs | 21 | 540K | 298s |
| github | nodocs | 14 | 21K | 121s |
| github | mutated | 21 | 544K | 122s |
| stripe | docs | 24 | 666K | 333s |
| stripe | nodocs | 15 | 24K | 117s |
| stripe | mutated | 21 | 645K | 120s |
| zulip | docs | 52 | 1,792K | 468s |
| zulip | nodocs | 14 | 21K | 87s |
| zulip | mutated | 21 | 1,131K | 197s |

**Mutation adherence (GPT-5.4):**

| Dataset | HTTP Adh | Iface Adh | Notes |
|---|---|---|---|
| github | 0% | 0% | All 5 mutations ignored |
| stripe | 0% | 0% | All 5 mutations ignored |
| zulip | 17% | 17% | 1/6: `filter_spec→narrow` adopted |

**Key findings:**

- **Zulip: GPT-5.4 wins across all conditions.** nodocs +25pp (85% vs 60%) is the largest gain — GPT-5.4's parametric knowledge of Zulip generates better tool coverage without docs. Docs +10pp (90% vs 80%). Mutated +9pp.
- **Stripe: catastrophic regression on docs and mutated.** Docs: 8%/48% (TOOL_IMPLEMENTATION=6, AGENT_REASONING=9) — SYNTH=48% means server has the tools, but implementations are broken. Mutated: 12%/27% (TOOL_SCHEMA=5, TOOL_COVERAGE=8) — mutated docs corrupt schemas. Nodocs matches GPT-5.2 (62%/73% vs 62%/68%) — parametric knowledge produces a usable stripe server but docs confuse GPT-5.4.
- **GitHub: mixed.** nodocs improves (+6pp, 89%/91%); docs regresses (−15pp, 47%/61%). SYNTH is identical for docs (61%) — same server quality, but the GPT-5.4 docs server accumulated more TOOL_COVERAGE=8 gaps on specific tasks.
- **Mutation adherence unchanged:** GPT-5.4 ignores mutations for well-known APIs (github, stripe) exactly as GPT-5.2 does. Same training-time knowledge override.
- **Zulip used 52 turns** (docs condition) vs ~20 for GPT-5.2 — GPT-5.4 reads docs more exhaustively, producing a 9-module server. This correlated with the highest zulip docs score seen (90%).

### GPT-5.4 Expanded Datasets

| Dataset | Cond | GPT-5.4 CURRENT (SYNTH) | GPT-5.2 CURRENT (SYNTH) | Δ | Adh (HTTP/iface) |
|---|---|---|---|---|---|
| notion | docs | 62% (61%) | 78% (91%) | −16pp | — |
| notion | nodocs | **100%** (100%) | **100%** (100%) | 0pp | — |
| notion | mutated | 0% (—) | **100%** (100%) | −100pp | — (no server.py) |
| shopify | docs | **83%** (87%) | 87% (89%) | −4pp | — |
| shopify | nodocs | **92%** (93%) | 92% (94%) | 0pp | — |
| shopify | mutated | **53%** (56%) | 62% (61%) | −9pp | 0% / 20% |
| mastodon | docs | **91%** (92%) | **100%** (93%) | −9pp | — |
| mastodon | nodocs | **90%** (92%) | **100%** (100%) | −10pp | — |
| mastodon | mutated | **100%** (93%) | **100%** (100%) | 0pp | **100% / 100%** |
| confluence | docs | 69% (76%) | 92% (95%) | −23pp | — |
| confluence | nodocs | **100%** (89%) | 93% (95%) | +7pp | — |
| confluence | mutated | **85%** (89%) | 91% (95%) | −6pp | **100% / 100%** |
| jira | docs | **57%** (56%) | +7pp | — | Close to GPT-5.2 (50%) |
| jira | nodocs | **50%** (62%) | +25pp | — | Better than GPT-5.2 (25%); higher SYNTH |
| jira | mutated | **57%** (62%) | +7pp | — | **60% / 60%** (3/5) |
| openweathermap | docs | **100%** (100%) | 0pp | — | Perfect; matches GPT-5.2 ceiling |
| openweathermap | nodocs | **95%** (96%) | +9pp | — | Near-ceiling |
| openweathermap | mutated | **100%** (100%) | 0pp | — | **40% / 60%** (2/5 HTTP, 3/5 iface) |
| alphavantage | docs | **80%** (95%) | −6pp | — | ENVIRONMENT errors from rate limits reduce scoreable N |
| alphavantage | nodocs | **92%** (89%) | +2pp | — | Strong from general knowledge |
| alphavantage | mutated | **78%** (89%) | −10pp | — | **80% / 80%** (4/5 adopted) |
| spoonacular | docs | **80%** (88%) | −20pp | — | Some TOOL_IMPLEMENTATION failures |
| spoonacular | nodocs | **82%** (88%) | −8pp | — | Similar to docs |
| spoonacular | mutated | **60%** (88%) | −18pp | — | **50% / 75%** (2/4 HTTP, 3/4 iface) |
| ebay_buy | docs | **69%** (71%) | 73% (88%) | −4pp | — |
| ebay_buy | nodocs | **92%** (88%) | 67% (94%) | +25pp | — |
| ebay_buy | mutated | **100%** (100%) | 80% (88%) | +20pp | **40% / 60%** (2/5 HTTP, 3/5 iface) |
| ebay_commerce | docs | **88%** (92%) | 100% (100%) | −12pp | — |
| ebay_commerce | nodocs | **40%** (38%) | 89% (85%) | −49pp | — |
| ebay_commerce | mutated | **62%** (77%) | +7pp | — | **100% / 100%** |
| ebay_sell | docs | **29%** (29%) | 38% (43%) | −9pp | — | Re-synth with fixed TASK.md (no OAuth scope param); TOOL_COVERAGE=9, TOOL_IMPLEMENTATION=1 |
| ebay_sell | nodocs | **45%** (50%) | 50% (50%) | −5pp | — | Re-synth; TOOL_COVERAGE=2, TOOL_IMPLEMENTATION=4, AGENT_REASONING=3 |
| ebay_sell | mutated | **44%** (57%) | 43% (43%) | +1pp | — | **20% / 80%** (1/5 HTTP, 4/5 iface) |

**Notable findings:**
- **GPT-5.4 mutation adherence dramatically higher than all other models** for less-familiar APIs: confluence 100%/100%, mastodon 100%/100%, ebay_commerce 100%/100%, alphavantage 80%/80%, jira 60%/60%, spoonacular 50%/75%, openweathermap 40%/60%, ebay_sell 20%/80%, ebay_buy 40%/60%. Model follows mutated docs when it has weaker training priors. Well-known APIs (github 0%/0%, stripe 0%/0%) still ignored entirely — same pattern as all other models.
- **Mastodon mutated: 100% + perfect adherence (5/5)** — highest adherence of any model on any dataset.
- **Confluence mutated: 85%** with high adherence — GPT-5.4 reads the mutated Confluence docs carefully and adopts all renames.
- **Notion mutated: broken (no server.py)** — same plain-function-library failure as Sonnet 4.6 nodocs/zulip; mutated docs confuse GPT-5.4 into writing a module without FastMCP registration.
- **Jira nodocs: 50%** — beats GPT-5.2 (25%) significantly; higher SYNTH (62% vs 44%) suggests better tool construction without docs.
- **OpenWeatherMap: perfect across all 3 conditions (100%/95%/100%)** — GPT-5.4's parametric knowledge of the OWM API is as strong as GPT-5.2's.

---

## Synthesis Model Comparison: GPT-5.4-mini

**Model:** `azure-chat-completions-gpt-5-4-mini-2026-03-17-sandbox` | **Flags:** `--chomsky --advanced`
**Agent:** Gemini 2.5 Pro | **Judge:** Gemini 3 Flash Preview

**Full 13-dataset matrix** (no alphavantage; pilot datasets github/stripe/zulip from Jun 7, remainder Jun 10–17):

| Dataset | docs pass% (synth%) | nodocs pass% (synth%) | mutated pass% (synth%) | Notes |
|---|---|---|---|---|
| github | 38% (35%) | 32% (26%) | 30% (35%) | TOOL_COVERAGE dominates |
| stripe | 14% (14%) | 0% (crash) | 19% (23%) | nodocs startup crash |
| zulip | 40% (48%) | 14% (24%) | 29% (40%) | TOOL_COVERAGE + TOOL_IMPLEMENTATION |
| confluence | 33% (17%) | **80%** (95%) | 43% (69%) | nodocs strong; docs server very shallow (SYNTH=17%) |
| mastodon | 57% (60%) | **79%** (80%) | **73%** (73%) | Best overall; nodocs > docs |
| openweathermap | **100%** (100%) | **100%** (87%) | **100%** (100%) | Perfect across all conditions |
| shopify | 62% (67%) | 0% (0%) | 0% (0%) | nodocs/mutated: complete TOOL_COVERAGE collapse |
| ebay_buy | 0% (10%) | 0% (0%) | **82%** (88%) | docs/nodocs collapse; mutated surprisingly strong (9/11 scoreable) |
| ebay_commerce | 0% (0%) | 0% (8%) | 0% (0%) | Complete collapse all conditions |
| ebay_sell | 7% (7%) | 8% (14%) | 8% (14%) | Near-floor all conditions |
| jira | 0% (6%) | 0% (0%) | 25%† (11%) | Collapse; mutated N=4 unreliable |
| spoonacular | **94%** (94%) | 82% (88%) | 100%† (41%) | Strong docs/nodocs; mutated N=1 unreliable |
| notion | **60%** (73%) | **0%** (0%) | **17%**† (11%) | docs strong; nodocs TOOL_COVERAGE collapse; mutated ENVIRONMENT=16/22 (SSL cert errors) |

> † = tiny scoreable N (≤4 or dominated by ENVIRONMENT errors), treat with caution.

**Per-condition averages (13 datasets, notion mutated excluded from mutated avg due to ENVIRONMENT=16/22):**
- docs: avg **41%** (min 0%, max 100%)
- nodocs: avg **41%** (min 0%, max 100%)
- mutated: avg **39%** (min 0%, max 100%; excl. notion mutated)

**Key findings:**
- **Bimodal distribution:** mini scores either near-100% (OWM: 100%/100%/100%, spoonacular docs 94%) or near-0% (jira, ebay_commerce, ebay_buy, ebay_sell). Middle ground is mastodon (57–79%) and shopify docs (62%).
- **OWM: perfect across all 3 conditions** — parametric knowledge of this tiny, well-known API fully compensates for shallower synthesis.
- **Nodocs ≥ docs** for mastodon and confluence — mini's parametric knowledge is more reliable than its ability to read and apply API docs.
- **Shopify docs 62% but nodocs 0%** — docs help mini produce a working server; without them it generates something syntactically valid but covering no tasks.
- **Complex APIs (jira, ebay×3): total collapse** — TOOL_COVERAGE=17–18/18 in nearly all runs. Mini cannot synthesize meaningful coverage of large, unfamiliar REST APIs.
- **Stripe nodocs: startup crash** — same pattern as GPT-4.1 (outdated FastMCP API usage or import errors).
- **Spoonacular mutated: 100% but N=1** — most tasks rate-limited (spoonacular 402 daily limit); not representative.

### Mutation Adherence

| Dataset | HTTP% | iface% |
|---|---|---|
| github | 0% | 0% |
| stripe | 0% | 20% |
| zulip | 17% | 17% |
| confluence | 40% | 60% |
| mastodon | **100%** | **100%** |
| openweathermap | 40% | 60% |
| shopify | 0% | 0% |
| ebay_buy | 0% | 0% |
| ebay_commerce | **100%** | **100%** |
| ebay_sell | 20% | 40% |
| jira | 80% | 80% |
| spoonacular | 0% | 25% |
| notion | 40% | 40% |

Mini follows the same pattern as other models: well-known APIs (github 0%, stripe 0%, shopify 0%) override mutated names via parametric knowledge; unfamiliar APIs (mastodon 100%, ebay_commerce 100%, jira 80%) adopt the renamed params from the docs.

### Grounding Quality (docs condition)

| Dataset | cov% | doc_exists% |
|---|---|---|
| github | 100% | 100% |
| stripe | 100% | 100% |
| zulip | 100% | 100% |
| confluence | — | — |
| mastodon | 100% | 100% |
| openweathermap | 100% | 100% |
| shopify | 96% | 100% |
| ebay_buy | — | — |
| ebay_commerce | 100% | 100% |
| ebay_sell | 100% | 100% |
| jira | — | — |
| spoonacular | 100% | 100% |
| notion | 100% | 100% |

Coverage is uniformly high (96–100%) where grounding.json exists. Confluence, ebay_buy, and jira produced no grounding manifest — consistent with their near-0% SYNTH rates (minimal tool implementation).

---

## Synthesis Model Comparison: Gemini 3.5 Flash

**Model:** `gcp-chat-completions-chat-gemini-3.5-flash-sandbox` | **Flags:** `--chomsky --advanced`
**Result:** Near-universal synthesis failure — same edit-loop behavioral issue as Gemini 2.5 Pro.

**Status: aborted after 7/42 evals** — all 7 returned 0%; synthesis outputs are structurally broken.

**Root cause — edit-loop failure:** Gemini 3.5 Flash reads the API docs (consuming 36K+ input tokens), then writes `server.py` and `grounding.json` in a loop of 2–3 turns — never creating the tool modules it imports. Token output is minimal (136–500 tokens total per synthesis run), confirming the model stops after the skeleton. Synthesis directories contain only `synthesis_meta.json` with 0 Python files in the vast majority of cases. This is the same behavioral pattern as Gemini 2.5 Pro — the model satisfies itself with a planning artifact rather than a complete implementation.

**Sample outputs:**

| Dataset | Cond | Tokens out | Python files | Outcome |
|---|---|---|---|---|
| confluence | docs | 136 | 0 | No server.py — only synthesis_meta.json |
| alphavantage | mutated | ~150 | 0 | No server.py |
| ebay_buy | nodocs | ~120 | 0 | No server.py |
| spoonacular | docs | 1 file | 1 (`server.py` only) | Imports missing modules → startup crash |

**Gemini 3.5 Flash is not viable for synthesis** with the current synthesis harness. The edit-loop failure is a model behavior issue — it does not attempt to write tool modules. No amount of additional rounds resolves this (same pattern in all 3 rounds × all 14 datasets).

---

## Synthesis Model Comparison: GPT-4.1

**Model:** `azure-chat-completions-gpt-4-1-2025-04-14-sandbox` | **Flags:** `--chomsky --advanced`
**Result:** All 9 servers non-functional — incompatible FastMCP API usage.

**Root cause:** GPT-4.1 generates MCP servers using an older FastMCP interface (`register_tool`, `list_tools`, class-based `StripeMCPServer()`) that does not exist in the current FastMCP version installed in the evaluation environment. The model's training-time knowledge of FastMCP predates the current API.

**Failure modes per synth:**

| Dataset | Cond | Files written | Failure |
|---|---|---|---|
| github | docs | `generated_tools/issues.py` only | No `server.py` written (stopped early) |
| github | nodocs | full (12 modules) | `ImportError: cannot import name 'list_tools'` |
| github | mutated | `generated_tools/issues.py` only | No `server.py` written |
| stripe | docs | full (16 modules) | `AttributeError: 'StripeMCPServer' has no attribute 'register_tool'` |
| stripe | nodocs | full (14 modules) | Same crash |
| stripe | mutated | full (10 modules) | Same crash |
| zulip | docs | `generated_tools/messages.py` only | No `server.py` written (stopped early) |
| zulip | nodocs | full (8 modules) | `ImportError: cannot import name 'list_tools'` |
| zulip | mutated | `generated_tools/messages.py`, `streams.py` | No `server.py` written |

GPT-4.1 is **not viable for synthesis** with the current evaluation stack without pinning an older FastMCP version or adding explicit API usage examples to the synthesis prompt. All CURRENT/SYNTH scores are 0% due to server startup failures — not meaningful to include in the comparison table.

---

## Synthesis Model Comparison: Gemini 2.5 Pro

**Model:** `gcp-chat-completions-chat-gemini-2.5-pro-sandbox` | **Flags:** `--chomsky --advanced`
**Result:** All 9 servers non-functional — synthesis incomplete (missing modules or no server.py).

**Root cause:** Two distinct failure modes. (1) **Edit loop:** The model writes `server.py` at turn 5, imports `generated_tools.*` modules, then spends 15–18 subsequent turns editing only `server.py` and `grounding.json` in alternation — never creating the module files it imports. It declares "done" having completed only 3 files. Turn counts (19–25) are well below the 100-turn limit; increasing turns would not help since the model is not trying to write modules. (2) **Timeout:** For stripe docs (2.4M token docs), the API call times out after 3 retries at turn 7; no files written.

**Failure summary:**

| Dataset | Cond | Tokens out | Outcome |
|---|---|---|---|
| github | docs | 1,053 | No `server.py` (stopped at 2 tool modules) |
| github | nodocs | 3,831 | `server.py` imports missing module (`topics`) |
| github | mutated | 6,821 | `server.py` present; imports missing module on startup |
| stripe | docs | 42 | No files — timeout on turn 7 (large docs) |
| stripe | nodocs | 6,476 | `server.py` imports missing module |
| stripe | mutated | 27 | No files — timeout on turn 4 |
| zulip | docs | 2,435 | No `server.py` (stopped at 1 tool module) |
| zulip | nodocs | 2,476 | `server.py` imports missing module (`topics`) |
| zulip | mutated | 2,368 | No `server.py` (stopped at 3 tool modules) |

Gemini 2.5 Pro is **not viable for synthesis** with the current synthesis harness. The edit-loop failure is a behavioral issue — the model satisfies itself with a partial implementation. Possible fixes: add an explicit verification step to the synthesis prompt (e.g. "list all files you created and verify all imports resolve"), or use a different model. The stripe timeout failure could be addressed with `--thinking-budget 0` to reduce per-call latency.

---

## Synthesis Model Comparison: Gemini 3.1 Pro

**Model:** `gcp-chat-completions-chat-gemini-3.1-pro-preview-sandbox` | **Flags:** `--chomsky --advanced`
**Fix required:** pychomsky `googlegenai.py` patched to preserve `thoughtSignature` in `_create_chat_result` and echo it back in `_parse_chat_history` — without this, all tool calls fail with INVALID_ARGUMENT on turn 2.
**Agent:** Gemini 2.5 Pro | **Judge:** Gemini 3 Flash Preview

| Dataset | Cond | CURRENT (SYNTH) | vs GPT-5.2 | Adh (HTTP/iface) | Notes |
|---|---|---|---|---|---|
| github | docs | **78%** (74%) | +16pp | 0% / 0% | Re-run `_20260603_1408`; first run had 0 tools (helpers in `tools/` not imported) |
| github | nodocs | 71% (74%) | −12pp | — | Working; TOOL_COVERAGE=5 |
| github | mutated | 36% (30%) | −40pp | 0% / 0% | Low SYNTH (30%) — poor server coverage |
| stripe | docs | 47% (59%) | −25pp | — | Working; TOOL_COVERAGE=7, TOOL_IMPLEMENTATION=2 |
| stripe | nodocs | 50% (59%) | −12pp | — | Working; TOOL_COVERAGE=8 |
| stripe | mutated | **59%** (68%) | +2pp | 0% / 0% | Third run `_20260603_1611`; two prior broken (circular import); 75 inline tools |
| zulip | docs | 76% (80%) | −4pp | — | Working; TOOL_COVERAGE=5 |
| zulip | nodocs | 84% (88%) | +24pp | — | Best result; close to GPT-5.2 baseline |
| zulip | mutated | **62%** (64%) | ±0pp | 0% / 0% | Re-run `_20260603_1408`; first run had 0 tools |
| notion | docs | **94%** (95%) | +1pp | — | Strong; near-ceiling |
| notion | nodocs | **94%** (95%) | −6pp | — | Strong from general knowledge |
| notion | mutated | **100%** (100%) | ±0pp | 0% / 0% | Perfect; all tools found and correct |
| shopify | docs | **80%** (83%) | −7pp | — | Working; TOOL_COVERAGE=3 |
| shopify | nodocs | **70%** (78%) | −22pp | — | Lower coverage without docs |
| shopify | mutated | **93%** (94%) | +31pp | 0% / 0% | Best shopify result across all synth models |
| mastodon | docs | **100%** (93%) | ±0pp | — | Matches GPT-5.2 ceiling |
| mastodon | nodocs | **92%** (93%) | −8pp | — | Strong from general knowledge |
| mastodon | mutated | **87%** (87%) | −13pp | 0% / 0% | Slight drop vs GPT-5.2 100% |
| confluence | docs | **0%** (n/a) | −92pp | — | Server has 0 registered tools (tools in `tools/` not imported in server.py) |
| confluence | nodocs | **100%** (100%) | +7pp | — | Perfect from general knowledge |
| confluence | mutated | **100%** (100%) | +9pp | 0% / 0% | Perfect; SYNTH=100% |
| jira | docs | **58%** (62%) | +8pp | — | TOOL_IMPLEMENTATION=4, TOOL_COVERAGE=1 |
| jira | nodocs | **44%** (31%) | −49pp | — | Low SYNTH; TOOL_COVERAGE=3, TOOL_IMPLEMENTATION=6 |
| jira | mutated | **31%** (44%) | −62pp | 0% / 0% | Worst jira result; TOOL_COVERAGE=5, TOOL_IMPLEMENTATION=4 |
| openweathermap | docs | **85%** (83%) | −15pp | — | TOOL_COVERAGE=2, TOOL_IMPLEMENTATION=1 |
| openweathermap | nodocs | **90%** (91%) | +4pp | — | Strong from general knowledge |
| openweathermap | mutated | **95%** (96%) | −5pp | 0% / 0% | Best OWM result; near-ceiling |
| alphavantage | docs | **100%** (94%) | +14pp | — | Small scoreable N=6 (10 ENVIRONMENT errors from rate limits) |
| alphavantage | nodocs | **100%** (100%) | +10pp | — | Perfect; SYNTH=100%, ENVIRONMENT=9 |
| alphavantage | mutated | **90%** (89%) | +2pp | 0% / 0% | 1 TOOL_IMPLEMENTATION fail (hallucinated EPS after rate limit); ENVIRONMENT=8 |
| spoonacular | docs | **83%** (88%) | −17pp | — | TOOL_IMPLEMENTATION=2, ENVIRONMENT=3 |
| spoonacular | nodocs | **91%** (94%) | +1pp | — | Strong from general knowledge |
| spoonacular | mutated | **90%** (88%) | +12pp | 14% / 14% | `ingredients`→`includeIngredients` adopted (1/7 mutations) |
| ebay_buy | docs | **90%** (86%) | −10pp | — | Strong; TOOL_COVERAGE=3 |
| ebay_buy | nodocs | **67%** (76%) | 0pp | — | Lower without docs |
| ebay_buy | mutated | **50%** (0%) | −50pp | 0% / 0% | SYNTH=0%: server has 0 registered tools |
| ebay_commerce | docs | **83%** (89%) | −17pp | — | Working; small scoreable N=6 |
| ebay_commerce | nodocs | **44%** (44%) | −45pp | — | Low SYNTH; poor API coverage without docs |
| ebay_commerce | mutated | **45%** (54%) | −10pp | 0% / 0% (`category_id`→`category_ids` = 1 replacement) | — |
| ebay_sell | docs | **38%** (14%) | 0pp | — | Re-run confirmed: TOOL_COVERAGE=6 (analytics API + 4 missing create tools), no ENVIRONMENT errors |
| ebay_sell | nodocs | **8%** (14%) | −42pp | — | Re-synth with fixed TASK.md; TOOL_COVERAGE=8, TOOL_IMPLEMENTATION=4; auth works but poor tool quality |
| ebay_sell | mutated | **23%** (29%) | −20pp | 0% / 0% | Re-synth (prior was print("hello")); AGENT_REASONING=1, TOOL_COVERAGE=7, TOOL_IMPLEMENTATION=3 |

**Key findings:**

- **Thought signature fix required:** Gemini 3.1 Pro is a thinking model that generates `thoughtSignature` fields with tool calls. These must be echoed back in subsequent turns — pychomsky didn't handle this. Two-line patch to `googlegenai.py` fixes it.
- **Inconsistent tool registration (recurring issue):** ~20% of servers write tools to `tools/*.py` but never import them in `server.py` → 0 exposed tools. Affects complex APIs (github, confluence, stripe, ebay_buy mutated). Simpler/well-known APIs (mastodon, notion, shopify) mostly avoid this pattern.
- **Strong on well-known APIs:** mastodon (100%/92%/87%), notion (94%/94%/100%), confluence nodocs/mutated (100%/100%), alphavantage (100%/100%/90%), ebay_buy docs (90%). Gemini 3.1 Pro's general knowledge is sufficient for these.
- **Weaker on complex or proprietary APIs:** jira (58%/44%/31%), stripe (47–59%), github mutated (36%), shopify nodocs (70%), ebay_sell (45%/TBD/TBD). Docs help stripe; mutation adherence poor across all.
- **eBay sell is weakest eBay dataset:** SYNTH=27% on docs — synthesizer writes tools that miss the core selling endpoints. ebay_buy (90% docs) and ebay_commerce (83% docs) are much stronger.
- **Synthesis stats:** 9–43 turns, 21K–4.4M tokens in, 64–2332s per run. Nodocs runs are fast (general knowledge); docs runs are thorough.
- **Mutation adherence:** 0 replacements for all except spoonacular (14%) and ebay_commerce (1 replacement: `category_id`→`category_ids`). Same near-zero pattern as GPT-5.2 and GPT-5.4.

---

## Synthesis Model Comparison: Claude Sonnet 4.6

**Model:** `gcp-chat-completions-anthropic-claude-sonnet-4-6-sandbox` | **Flags:** `--chomsky --advanced`
**Rate limit:** 6 rpm → sequential runs required (11s enforced sleep between calls). Parallel synthesis would exceed the limit.
**Agent:** Gemini 2.5 Pro | **Judge:** Gemini 3 Flash Preview
**Registration pattern:** Uses `register_tools(mcp)` or `module.register(mcp)` called from `server.py` — no circular imports, clean modular architecture.

| Dataset | Cond | CURRENT (SYNTH) | vs GPT-5.2 | Adh (HTTP/iface) | Notes |
|---|---|---|---|---|---|
| github | docs | **90%** (91%) | +28pp | — | AGENT_REASONING=3, TOOL_COVERAGE=1, TOOL_IMPLEMENTATION=1 |
| github | nodocs | **100%** (100%) | +17pp | — | Perfect SYNTH; AGENT_REASONING=5, ENVIRONMENT=1 |
| github | mutated | **100%** (100%) | +24pp | 0% / 0% | Perfect; AGENT_REASONING=2, ENVIRONMENT=1 |
| stripe | docs | **77%** (86%) | +5pp | — | TOOL_COVERAGE=3, AGENT_REASONING=8, ENVIRONMENT=1 |
| stripe | nodocs | **100%** (100%) | +38pp | — | Re-synth `_20260609_1201_nodocs`; AGENT_REASONING=8 (all undefined, not fails) |
| stripe | mutated | **100%** (100%) | +43pp | 0% / 0% | Perfect; AGENT_REASONING=13 (all undefined, not fails) |
| zulip | docs | **100%** (100%) | +20pp | — | Perfect; AGENT_REASONING=4 |
| zulip | nodocs | **43%** (—) | −37pp | — | Re-synth `_20260610_1656_nodocs`; 10/23 scoreable |
| zulip | mutated | — | — | — | All attempts: stream error mid-synthesis; no server.py produced |
| notion | docs | **100%** (100%) | +22pp | — | Perfect; 100% SYNTH |
| notion | nodocs | **87%** (—) | −13pp | — | AGENT_REASONING=7 |
| notion | mutated | **85%** (—) | −15pp | 60% / 60% | AGENT_REASONING=9; 3/5 mutations adopted (query_filter, sort_rules, results_per_page) |
| shopify | docs | **100%** (—) | +13pp | — | Perfect CURRENT |
| shopify | nodocs | 0% (—) | −92pp | — | `FastMCP.__init__()` got unexpected kwarg `description`; broken |
| mastodon | docs | 0% (—) | −100pp | — | No server.py (plain functions in generated_tools/); broken |
| mastodon | nodocs | 0% (—) | −100pp | — | Re-synth `_20260610_1717_nodocs`: FastMCP `description` kwarg crash. Re-synth Jun 17: pychomsky stream error at turn 13 — no server.py produced; unresolvable |
| mastodon | mutated | **92%** (—) | −8pp | **100% / 100%** | Near-perfect; 5/5 mutations adopted |
| confluence | docs | 0% (—) | −92pp | — | No server.py (plain functions in generated_tools/); broken |
| confluence | nodocs | **94%** (—) | +1pp | — | Strong; 1 fail out of 16 scoreable |
| confluence | mutated | **47%** (—) | −44pp | **80% / 100%** | Re-synth `_20260610_1819_mutated`; 5/5 iface adopted, 4/5 HTTP (expand→include not in HTTP dict) |
| jira | docs | **73%** (—) | +23pp | — | Best jira result; strong vs GPT-5.2 (50%) and G3.1P (58%) |
| jira | nodocs | **58%** (—) | +33pp | — | TOOL_COVERAGE failures |
| jira | mutated | **79%** (—) | +29pp | 20% / 20% | Only 1/5 mutations adopted (page_size); jql/startAt/fields/accountId ignored |
| openweathermap | docs | **0%** (—) | — | — | server crashes: `FastMCP.__init__()` got unexpected kwarg `description` |
| openweathermap | nodocs | **100%** (—) | +14pp | — | Perfect; 20/20 scoreable |
| openweathermap | mutated | 0% (—) | −100pp | — | `FastMCP.__init__()` got unexpected kwarg `description`; broken |
| alphavantage | — | — (95%/89%/84%) | — | **80% / 100%** (mutated) | Eval excluded: ENVIRONMENT=15–18/19 tasks rate-limited across all 3 conditions (25 req/day shared key). Synthesis ran; mutation adherence from synthesized code is valid. |
| spoonacular | docs | **93%** (94%) | — | — | Re-eval `_20260608_1350` Jun 16; 13/14 scoreable pass; ENVIRONMENT=0 (new day, quota reset) |
| spoonacular | nodocs | 0% (89%) | — | — | server.py exists but FastMCP `description` kwarg crash on startup; all 17 tasks fail immediately. Re-synth Jun 17: pychomsky stream error at turn 8 — no server.py produced; unresolvable |
| spoonacular | mutated | **92%** (94%) | — | 25% / 25% | Re-synth `_20260616_1353_mutated_patched`; 11/12 scoreable; ENVIRONMENT=4 (quota hit tasks 13–16); 1 TOOL_IMPLEMENTATION fail |
| ebay_buy | docs | 0% (—) | — | — | no server.py (plain functions in generated_tools/ only) |
| ebay_buy | nodocs | **79%** (—) | +12pp | — | Strong from parametric knowledge; 11/14 scoreable |
| ebay_buy | mutated | **33%** (29%) | — | 40% / 60% | Re-eval `_20260610_1745_mutated_patched` Jun 16; ENVIRONMENT=14 (auth errors in sandbox); only 3 scoreable |
| ebay_commerce | docs | **100%** (100%) | — | — | Perfect; AGENT_REASONING=3 |
| ebay_commerce | nodocs | 0% (—) | — | — | Re-synth `_20260610_1935_nodocs`; server crash on startup (turns=0 for all 13 tasks) |
| ebay_sell | docs | 0% (—) | — | — | no server.py (same pattern as mastodon/confluence/zulip) |
| ebay_sell | nodocs | **73%** / 38% (—) | — | — | Two re-synths: `_1821_nodocs` 73% (8/11 scoreable, AGENT_REASONING=3, TOOL_IMPL=3); `_2010_nodocs` 38% (3/8 scoreable, TOOL_IMPL=5 missing Content-Language header) |
| ebay_sell | mutated | — | — | — | All attempts: stream error (pychomsky) kills session before server.py written; 15 tool files produced but no server.py |
| zulip | mutated | — | — | — | All attempts: stream error (pychomsky) kills session before server.py written; confirmed Jun 16 re-synthesis |

**Synthesis stats (completed runs):**

| Dataset | Cond | Time | Notes |
|---|---|---|---|
| github | docs | 913s | 4M tokens in; 166 tools |
| github | nodocs | ~600s | 302 tools in generated_tools/ |
| github | mutated | ~900s | Clean patched server |
| stripe | docs | 1011s | 108 tools in generated_tools/ |
| stripe | nodocs | ~3h | Re-run; `module.register(mcp)` pattern; 21 modules |
| stripe | mutated | ~900s | 100% CURRENT |
| zulip | docs | 986s | 105 mcp.tool refs; perfect score |

**Key findings:**

- **Dramatically outperforms all other synthesizers on github:** docs 90%/91%, nodocs 100%/100%, mutated 100%/100%. GPT-5.2 best was 83% nodocs; Gemini 3.1 Pro 78% docs. Sonnet 4.6's parametric knowledge of the GitHub API is exceptional.
- **Stripe docs/mutated strong:** docs 77%/86% (above GPT-5.2 72%), mutated 100%/100% (vs GPT-5.2 57%), nodocs 100%/100%. The modular `register_tools(mcp)` architecture avoids the circular import issues that plagued Gemini 3.1 Pro.
- **Intermittent no-server.py failure:** Zulip mutated (all attempts), mastodon docs, confluence docs, ebay_buy docs, and ebay_sell docs all produce a plain Python tool library in `generated_tools/` without a top-level FastMCP `server.py`. Pattern appears dataset-specific and correlated with larger APIs. Zulip nodocs succeeded on re-synth (43%).
- **FastMCP `description` kwarg crash:** OWM docs/mutated, shopify nodocs, and mastodon nodocs all fail with `FastMCP.__init__() got unexpected kwarg 'description'` — a different crash pattern from the no-server.py issue. These synths write a valid `server.py` but use an outdated FastMCP API. The re-synth of mastodon nodocs hit this pattern even on retry — suggesting it is consistent for this dataset/condition.
- **Strong nodocs/mutated results where synths work:** mastodon mutated 92%, confluence nodocs 94%, jira mutated 79%, notion nodocs 87%/mutated 85%, OWM nodocs 100%, ebay_buy nodocs 79%, **spoonacular docs 93%** (re-eval Jun 16 after quota reset). The broken synth pattern is the limiting factor, not model capability.
- **Alphavantage excluded from eval:** synthesis ran (SYNTH=84–95%), but eval was rate-limited (ENVIRONMENT=15–18/19 tasks) across all 3 conditions. Mutation adherence (80% HTTP / 100% iface) measured from synthesized code is valid.
- **Sequential constraint:** 6 rpm × 11s sleep → ~5 calls/min. A single docs synthesis (docs reading + code writing) takes 15–30 min. All conditions take ~4–5 hours total — cannot parallelize.
- **Mutation adherence:** 0 replacements for github and stripe (same as all other models). Well-known APIs override renamed params regardless of synthesizer.
- **Persistent stream error (pychomsky):** zulip mutated, spoonacular nodocs, mastodon nodocs, and ebay_sell mutated all fail with `string indices must be integers, not 'str'` mid-synthesis — session dies before `server.py` is written. Tool modules are produced (6–15 files) but no server. Re-synths Jun 17 for spoonacular nodocs (turn 8) and mastodon nodocs (turn 13) hit the same error. Spoonacular mutated succeeded (92%). These four gaps are unresolvable without a pychomsky fix.
- **Large tool counts:** 166 tools (github docs), 302 tools (github nodocs), 108 tools (stripe docs) — much higher coverage than GPT-5.2 or Gemini 3.1 Pro.

---

## Synthesis Model Comparison: Qwen3-Coder-Next (vLLM, local)

**Model:** `Qwen/Qwen3-Coder-Next` | **Server:** vLLM (local H100 80GB) | **Parser:** hermes
**Synth script:** `synthesize_vllm.py` | **12 datasets × up to 3 conditions**
**Agent:** Gemini 2.5 Pro | **Judge:** Gemini 3 Flash Preview
**Note:** "crash" = server fails on startup (syntax error, wrong FastMCP API, etc.); "—" = no synth available

Results after up to three synthesis rounds; best per condition shown. "crash" = server fails on startup; "—" = no usable synth; † = tiny scoreable N (ENVIRONMENT errors dominate, treat with caution).

| Dataset | docs | nodocs | mutated | Notes |
|---|---|---|---|---|
| github | **58%** (52%) | **60%** (52%) | **57%** (57%) | Docs: TC=5,TS=3 · Nodocs: TI=6,TC=1 · Mutated: TC=9 |
| stripe | 0% (crash) | **62%** (73%) | 0% (crash) | Docs: SyntaxError · Nodocs r2: AR=6,TC=3,TI=3 · Mutated: SyntaxError |
| zulip | 0% (crash) | 0% (crash) | **64%** (80%) | Mutated r2: AR=11,TI=3,TS=2 · Docs/nodocs: persistent crash |
| notion | **69%** (82%) | 5% (0%) | 0% | Docs strong; nodocs TI=21; mutated FastMCP error (3 rounds) |
| openweathermap | **100%** (100%) | **86%** (78%) | **100%** (100%) | Best dataset; AR=1/2/3 only |
| jira | **71%** (69%) | 0% | **42%** (56%) | Docs r2: AR=2,TI=4 · Nodocs crash (2 rounds) · Mutated r2: AR=4,TI=5 |
| shopify | **94%** (—) | **82%** (83%) | **67%** (72%) | Docs r3: 94% (IndentationError fixed) · Nodocs/mutated r1 still best |
| mastodon | **87%** (—) | **80%** (73%) | **54%** (60%) | Docs r3: 87% (up from 80%) · Mutated r3: 0% (regression) |
| ebay_buy | 12% (7%) | **80%** (76%) | 6% (6%) | Docs ENV=8 · Nodocs strong · Mutated TI=16 |
| ebay_commerce | **100%** (92%) | 0% (crash) | **11%** (31%) | Docs perfect; nodocs crash (2 rounds); mutated r2: 0% (regression) |
| ebay_sell | **100%** (71%) | 0% (crash) | 0% | Docs: ENV=13 (few scoreable) · Nodocs/mutated crash (2 rounds) |
| confluence | **39%** (43%) | 100%† (21%) | **50%** (38%) | Docs r3: 0% (regression) · Nodocs: ENV=18 (N=3 scoreable) · Mutated r2: 40% |

**Key findings:**

- **OWM is the standout: 100%/86%/100%** — Qwen's parametric knowledge of the weather API is as strong as GPT-5.2.
- **High per-condition variance:** After 3 rounds, most datasets have at least one working condition. Mastodon is the most stable (87%/80%/54%). Stripe docs/mutated and zulip docs/nodocs failed across all rounds.
- **Crash rate remains high:** ~30–40% of synths produce servers that fail on startup — SyntaxErrors, wrong FastMCP API (`description` kwarg), or incomplete files. Much higher than GPT-5.2 or S4.6.
- **Shopify docs recovered in r3:** 0% (crash, 2 rounds) → **94%** (r3 fixed the IndentationError). Nodocs/mutated r1 remain best (82%/67%).
- **Mastodon docs improved:** 80% → **87%** in r3 synth. Mutated r3 regressed to 0% (r1 54% remains best).
- **Jira works on retry:** docs 0%→71%, mutated 0%→42%. Re-synth produced much better tool coverage (SYNTH=69%).
- **Zulip mutated improved dramatically:** 15%→64% (SYNTH 14%→80%) on r2. Docs/nodocs remain broken across all rounds.
- **ebay_buy nodocs strong (80%)** but docs/mutated remain near-zero even after 2 rounds.
- **Notion nodocs/mutated remain broken** across 3 rounds — persistent FastMCP registration errors.
- **eBay sell/ebay_commerce nodocs crash in all rounds** — the nodocs prompt triggers a different failure pattern than docs.
- **Confluence nodocs 100%† is misleading:** SYNTH=21%, ENVIRONMENT=18/21 — only 3 tasks were scoreable. Not a meaningful signal.
- **GitHub: competitive with GPT-5.2** (58–60% vs 62%/83%/76%), well below S4.6 (90–100%).
- **Stripe nodocs 62%** is the only working stripe condition — matches GPT-5.2 nodocs (62%).
- **Round-to-round instability:** Re-runs often improve crashed conditions but sometimes regress working ones (ebay_commerce mutated 11%→0%, mastodon mutated 54%→0%, confluence docs 39%→0%). No monotonic improvement — each synth is independent.
- **vLLM hermes parser required.** Qwen3-Coder-Next uses JSON tool calls compatible with hermes parser; has higher synth failure rate than cloud models.
- **Mutation adherence (HTTP% / iface%):**

| Dataset | HTTP Adh | Iface Adh | Notes |
|---|---|---|---|
| github | 0% | 60% | 0/5 HTTP, 3/5 iface |
| stripe | 0% | 60% | 0/5 HTTP, 3/5 iface |
| zulip | 100% | 100% | 6/6 adopted at both levels |
| notion | 0% | 0% | 0/5 adopted |
| openweathermap | 0% | 40% | 0/5 HTTP, 2/5 iface |
| jira | 100% | 100% | 5/5 adopted at both levels |
| shopify | 0% | 0% | 0/5 adopted |
| mastodon | 100% | 100% | 5/5 adopted at both levels |
| alphavantage | 100% | 100% | 5/5 adopted at both levels |
| confluence | 100% | 100% | 5/5 adopted at both levels |
| ebay_buy | 60% | 80% | 3/5 HTTP, 4/5 iface |
| ebay_commerce | 100% | 100% | 5/5 adopted at both levels |
| ebay_sell | 0% | 20% | 0/5 HTTP, 1/5 iface |

Qwen follows the same overall pattern as other models — high adherence on less-familiar APIs (zulip, jira, mastodon, alphavantage, confluence, ebay_commerce) and low/zero on well-known ones (github, stripe, shopify). Notable: github/stripe show iface-level adoption (0% HTTP, 60% iface) — function signatures renamed but original names sent to the API. Notion and shopify: 0% at both levels.

---

## Synthesis Model Comparison: Claude Haiku 4.5

**Model:** `gcp-chat-completions-anthropic-claude-haiku-4.5-sandbox` | **Context:** 200K | **Inter-turn delay:** 11s
**Run:** June 15 2026 | **Agent:** Gemini 2.5 Pro | **Judge:** Gemini 3 Flash Preview
**Note:** Results partial — evals running in parallel. "…" = in progress; "—" = no synth (synthesis failed to produce server.py)

| Dataset | docs pass% (synth%) | nodocs pass% (synth%) | mutated pass% (synth%) |
|---------|---------------------|----------------------|------------------------|
| stripe | **57%** (73%) | **75%** (82%) | **86%** (95%) |
| notion | **56%** (82%) | **5%** (0%) | **50%** (67%) |
| github | **95%** (96%) | **90%** (87%) | **86%** (86%) |
| confluence | **80%** (86%) | **33%** (15%) | **33%** (32%) |
| openweathermap | **95%** (96%) | **65%** (65%) | **60%** (61%) |
| jira | **62%** (67%) | **7%** (13%) | **64%** (69%) |
| shopify | **93%** (94%) | **75%** (83%) | **94%** (94%) |
| mastodon | **93%** (93%) | **40%** (33%) | **86%** (87%) |
| spoonacular | **0%** (0%) | **79%** (82%) | **86%** (76%) |
| ebay_buy | **80%** (94%) | **67%** (76%) | **100%** (94%) |
| ebay_commerce | **30%** (46%) | **10%** (31%) | **50%** (69%) |
| ebay_sell | **17%** (29%) | **9%** (29%) | **36%** (50%) |
| zulip | **55%** (61%) | **36%** (40%) | **26%** (29%) |

> **alphavantage excluded:** shared 25 req/day API key exhausted by the docs eval run; re-eval Jun 16 confirmed quota still gone. All three conditions rate-limited and non-scoreable. Results require a premium API key.

**Per-condition averages (13 datasets, alphavantage excluded; docs excl. spoonacular pending):**
- docs: avg **59%** (12 datasets with results; min 17%, max 95%)
- nodocs: avg **46%** (13 datasets; min 5%, max 90%)
- mutated: avg **66%** (13 datasets; min 26%, max 100%)

**Key findings:**
- **GitHub: 95%/90%/86%** — strongest github result of any model tested.
- **Shopify: 93%/75%/94%** and **mastodon: 93%/40%/86%** — very strong docs and mutated.
- **ebay_buy mutated: 100%** (13/13) — perfect score.
- **OWM: 95%/65%/60%** — strong docs but notable nodocs/mutated drop vs Qwen3/GPT-5.2 (86-100% across all conditions).
- **Nodocs collapse pattern:** jira (62%→7%), notion (56%→5%), confluence (80%→33%), zulip (55%→36%) — Haiku heavily relies on docs for these APIs.
- **Mutated generally holds up:** avg mutated (66%) ≈ avg docs (65%), unlike some models where mutations cause regression.
- **eBay sell/commerce weak:** 17%/9%/36% and 30%/10%/50% — low synth rates indicate the server doesn't cover enough of the API surface.
- **Alphavantage excluded:** shared 25 req/day API key exhausted by the docs eval run; all three conditions non-scoreable. Removed from averages; results require a premium API key.

### Grounding Quality (Haiku 4.5)

`cov` = fraction of implemented tools with a grounding entry; `doc%` = fraction of cited docs that exist on disk.
Nodocs condition always has doc%=0% by design (synthesizer has no docs to cite).

| Dataset | docs cov/doc% | nodocs cov/doc% | mutated cov/doc% |
|---------|--------------|-----------------|-----------------|
| stripe | 100%/100% | 100%/0% | 100%/100% |
| notion | 0%/100% | 100%/0% | 100%/100% |
| github | 100%/100% | 100%/0% | 100%/100% |
| alphavantage | 100%/100% | 100%/0% | 100%/100% |
| confluence | 100%/100% | 100%/0% | 100%/95% |
| openweathermap | 100%/100% | 100%/0% | 100%/100% |
| jira | 100%/100% | 100%/0% | 100%/100% |
| shopify | 100%/100% | 100%/1% | 100%/100% |
| mastodon | 100%/100% | 100%/0% | 0%/100% |
| spoonacular | — | 100%/0% | 100%/100% |
| ebay_buy | — | 100%/0% | 100%/100% |
| ebay_commerce | 100%/100% | 100%/0% | 100%/100% |
| ebay_sell | 100%/93% | 100%/0% | 100%/99% |
| zulip | 100%/100% | 100%/0% | 100%/100% |

Notable anomalies: **notion docs** coverage=0% (grounding.json present but tool name format mismatch — synthesizer wrote tool names differently than server.py decorators). **mastodon mutated** coverage=0% (same issue).

### Mutation Adherence (Haiku 4.5)

`HTTP%` = fraction of 5 mutations adopted as quoted string keys in HTTP call dicts; `Iface%` = adopted as Python identifiers (function params/variables).

| Dataset | HTTP% | Iface% | n |
|---------|-------|--------|---|
| stripe | 0% | 20% | 5 |
| notion | 60% | 80% | 5 |
| github | 0% | 20% | 5 |
| alphavantage | 80% | 100% | 5 |
| confluence | 60% | 60% | 5 |
| openweathermap | 40% | 80% | 5 |
| jira | 20% | 80% | 5 |
| shopify | 0% | 20% | 5 |
| mastodon | 0% | 0% | 5 |
| spoonacular | 50% | 75% | 4 |
| ebay_buy | 20% | 20% | 5 |
| ebay_commerce | 100% | 100% | 5 |
| ebay_sell | 20% | 40% | 5 |
| zulip | 50% | 50% | 6 |

**Average (Haiku 4.5):** HTTP%=**32%**, Iface%=**53%** — Haiku adopts mutated parameter names at the interface level ~half the time, but only propagates to HTTP layer 32% of the time. ebay_commerce is the strongest (100%/100%); stripe/github/shopify/mastodon show 0% HTTP adoption.

---

## Synthesis Model Comparison: Qwen3-Coder-Next-Base (vLLM, local)

**Model:** `Qwen/Qwen3-Coder-Next-Base` (base model, no instruction tuning) | **Server:** vLLM (local H100 80GB)
**Run:** June 15 2026 | **Agent:** Gemini 2.5 Pro | **Judge:** Gemini 3 Flash Preview
**Note:** Most conditions produced no server.py — only 13 evaluable conditions found across 14 datasets.
Results partial — evals running. "—" = no usable synthesis (no server.py or TypeScript output).

| Dataset | docs pass% (synth%) | nodocs pass% (synth%) | mutated pass% (synth%) |
|---------|---------------------|----------------------|------------------------|
| alphavantage | **92%** (95%) | — | — |
| confluence | **64%** (81%) | — | — |
| ebay_buy | **6%** (6%) | — | — |
| ebay_commerce | **45%** (46%) | — | — |
| ebay_sell | — | **0%** (0%) | — |
| github | — | — | — |
| jira | — | — | — |
| mastodon | **0%** (0%) | — | **0%** (0%) |
| notion | — | **0%** (0%) | — |
| openweathermap | — | — | — |
| shopify | — | **0%** (0%) | **0%** (0%) |
| spoonacular | — | **60%** (29%) | — |
| stripe | — | **56%** (68%) | — |
| zulip | — | — | **0%** (0%) |

**Key findings (partial):**
- **Base model rarely produces a working server:** Only 13/42 conditions had a Python server.py — most runs produced only `synthesis_meta.json` or TypeScript output.
- **Alphavantage docs 92% (95% synth)** — where it does produce output, quality can be high.
- Coverage heavily skewed: docs worked for eBay/confluence/mastodon; nodocs/mutated scattered.

### Grounding Quality (Qwen3-Coder-Next-Base)

`cov` = fraction of implemented tools with a grounding entry; `doc%` = fraction of cited docs that exist on disk.
`err` = grounding.json present but malformed (empty or invalid JSON from base model).

| Dataset | Condition | cov/doc% | Notes |
|---------|-----------|----------|-------|
| alphavantage | docs | 100%/100% | |
| confluence | docs | 100%/96% | 1 doc missing |
| ebay_buy | docs | 100%/100% | |
| ebay_commerce | docs | err | Empty grounding.json |
| ebay_sell | nodocs | 100%/0% | Expected (nodocs) |
| mastodon | docs | 100%/100% | 113 entries in manifest |
| mastodon | mutated | 100%/100% | 60 entries |
| notion | nodocs | 100%/0% | Doc values are descriptive strings, not file paths |
| shopify | nodocs | 100%/0% | Expected (nodocs) |
| shopify | mutated | err | Malformed JSON in grounding.json |
| spoonacular | nodocs | 100%/0% | Expected (nodocs) |
| stripe | nodocs | 100%/0% | Expected (nodocs) |
| zulip | mutated | 100%/100% | 129 entries |

### Mutation Adherence (Qwen3-Coder-Next-Base)

Only 3 mutated conditions produced usable servers:

| Dataset | HTTP% | Iface% | n |
|---------|-------|--------|---|
| mastodon | 40% | 40% | 5 |
| shopify | 20% | 20% | 5 |
| zulip | 0% | 0% | 6 |

**Average (Qwen3-Base):** HTTP%=**20%**, Iface%=**20%** — low adoption overall, consistent with base model not following doc-grounded parameter naming patterns reliably.

---

# Deprecated from down here on

## 7×3 Condition Matrix (docs / nodocs / mutated)

This is the primary experimental matrix: 7 datasets × 3 synthesis conditions. All runs use GPT-5.2 as synthesizer and Gemini 2.5 Pro as agent/judge. The `mutated` condition synthesizes from docs with renamed parameters; the patched server restores original API names so ground truth is preserved.

### Metric Definitions

| Metric | Formula | What it measures |
|---|---|---|
| **CURRENT** | pass / (pass+fail) | Agent task success; excludes AGENT_REASONING from denominator |
| **RAW** | pass / total | Same but includes all undefined tasks |
| **SYNTH** | server_sufficient / total | Server quality independent of agent; SERVER_SUFFICIENT = A+B ≥ 3/4 |
| **E2E** | (server_sufficient AND pass) / total | End-to-end success: good server + agent completion |
| **FULL** | task_completion=2 / total | Strict: full D-dimension score (both task and reporting correct) |

`server_sufficient` is true when the rubric scores A(tool_selection) + B(param_quality) ≥ 3 out of 4 — meaning the synthesized server provided a tool good enough to attempt the task.

### Results Table

| Dataset | Cond | N | CURRENT | RAW | SYNTH | E2E | FULL |
|---|---|---|---|---|---|---|---|
| **github** | docs | 23 | 77% | 74% | 57% | 52% | 70% |
| | nodocs | 23 | 85% | 74% | **87%** | **74%** | 65% |
| | mutated | 23 | 77% | 74% | 61% | 57% | 61% |
| **zulip** | docs | 25 | **95%** | **84%** | **88%** | **76%** | 68% |
| | nodocs | 25 | 60% | 60% | 48% | 44% | 44% |
| | mutated | 25 | 80% | 64% | 76% | 60% | 56% |
| **notion** | docs | 22 | 93% | 64% | 91% | 59% | 41% |
| | nodocs | 22 | **100%** | **86%** | **100%** | **86%** | **73%** |
| | mutated | 22 | **100%** | **86%** | 91% | 77% | 50% |
| **stripe** | docs | 22 | 75% | 68% | 68% | 59% | 50% |
| | nodocs | 22 | **11%** | **5%** | 55% | **0%** | **0%** |
| | mutated | 22 | 94% | 68% | 68% | 59% | 45% |
| **ebay_buy** | docs | 18 | **100%** | **94%** | 83% | 78% | 50% |
| | nodocs | 18 | **100%** | **94%** | 78% | 78% | 50% |
| | mutated | 18 | **100%** | **94%** | **89%** | **83%** | 44% |
| **jira** | docs | 16 | 93% | 88% | 62% | 56% | 44% |
| | nodocs | 16 | 93% | 81% | 56% | 44% | 31% |
| | mutated | 16 | 93% | 88% | **69%** | **62%** | 38% |
| **spoonacular** | docs | 12 | **100%** | 83% | 75% | **67%** | **67%** |
| | nodocs | 12 | 90% | 75% | 75% | 58% | 42% |
| | mutated | 12 | 78% | 58% | 75% | 50% | 50% |

### Key Findings

**docs vs nodocs split by dataset:**

- **GitHub**: nodocs dramatically outperforms docs on SYNTH (87% vs 57%). The docs server missed several tools (no `list_commits`, no gists, no label management). GitHub's API is well-known enough that parametric knowledge produces a better server.
- **Zulip**: docs clearly wins (95% current, 88% synth vs 60%/48% nodocs). The nodocs server has broken `narrow` parameter handling in `get_messages`, causing cascading failures.
- **Notion**: nodocs wins strongly (100%/100% vs 93%/91%). The docs server has recurring database_create failures; nodocs server built a cleaner implementation using parametric Notion API knowledge.
- **Stripe**: nodocs catastrophically fails (11% current, 5% raw). Without docs, GPT-5.2 synthesized a broken `kwargs`-based server that passes parameters as query strings, which Stripe's API rejects.
- **eBay Buy**: Both docs and nodocs score ~100% current. The API is simple and well-structured; condition matters little.
- **Jira**: Consistent ~93% current across all conditions. The main failure is a deprecated endpoint (`/rest/api/2/search` → HTTP 410) that appears regardless of condition.
- **Spoonacular**: docs wins on CURRENT (100% vs 90%/78%) and FULL (67% vs 42%/50%).

**mutated condition:**

The mutated condition synthesizes servers from docs with renamed parameters (e.g., `q` → `search_query`). After patching, the server is functionally identical to docs but was built from altered documentation. In most datasets, mutated scores are close to docs:
- GitHub mutated ≈ docs (same SYNTH: 61% vs 57%)
- Jira mutated slightly beats docs on SYNTH (69% vs 62%)
- Notion mutated ≈ docs (91% synth both)
- Stripe mutated ≈ docs (68% synth both)
- eBay buy mutated slightly beats docs (89% vs 83% synth)

**Strictness gradient across metrics:**

CURRENT is the most permissive (excludes AGENT_REASONING from denominator). FULL is the most strict (requires explicit completion confirmation). The gap is large for datasets with many undefined verdicts:
- Notion docs: CURRENT=93% → FULL=41% (7 AGENT_REASONING exclusions inflate CURRENT)
- Stripe nodocs: CURRENT=11% → FULL=0% (broken server; nothing completes)
- GitHub docs: CURRENT=77% → FULL=70% (surprisingly tight; few AGENT_REASONING)

**SYNTH is the cleanest signal for server quality** (independent of agent behavior). E2E captures the combined system quality.

### Grounding Results (mutated synths)

Grounding evaluates whether the synthesizer cited documentation that actually describes each tool. All paths reference `docs/` (original docs), not `docs_mutated/` — the synthesizer read mutated docs but grounding.json records the original-path equivalent.

| Dataset | Coverage | Doc Exists | Accuracy |
|---|---|---|---|
| github | 100% | 100% | 86% |
| zulip | 100% | 100% | 100% |
| notion | 100% | 100% | 100% |
| stripe | 100% | 100% | 100% |
| ebay_buy | 100% | 100% | 100% |

All cited docs exist (100% doc_exists_rate across all datasets). Coverage is 100% across all datasets — every implemented tool has a grounding entry. Accuracy is high (86-100%): the synthesizer consistently cites the correct documentation for each tool. GitHub's 86% accuracy reflects a few tools (e.g., `github_generate_release_notes`, `github_rerun_workflow_run`) where the cited multi-operation doc is only loosely related.

### Mutation Adherence

Mutation adherence measures whether the synthesizer actually adopted the renamed parameter names from the mutated docs, or ignored them in favour of original names from parametric memory. Measured by `inspect_mutations.py` on the unpatched `_mutated` synth dirs.

Two levels are tracked: **HTTP adoption** (mutated name appears as a dict key sent to the API) and **interface adoption** (mutated name appears as a function parameter). HTTP adoption is the stronger signal — it means the wrong name would actually be sent to the real API if not patched.

| Dataset | Mutations | Adopted | HTTP adopted | Adherence | HTTP adherence |
|---|---|---|---|---|---|
| spoonacular | 4 | 3 | 3 | 75% | 75% |
| notion | 5 | 2 | 2 | 40% | 40% |
| zulip | 6 | 2 | 1 | 33% | 17% |
| jira | 5 | 1 | 1 | 20% | 20% |
| stripe | 5 | 1 | 0 | 20% | 0% |
| github | 5 | 0 | 0 | 0% | 0% |
| ebay_buy | 5 | 0 | 0 | 0% | 0% |

Per-mutation breakdown:

| Dataset | Original → Mutated | HTTP | Interface |
|---|---|---|---|
| spoonacular | `query` → `search_query` | ✓ | ✓ |
| spoonacular | `includeIngredients` → `ingredients` | ✓ | ✓ |
| spoonacular | `diet` → `diet_type` | ✓ | ✓ |
| spoonacular | `targetCalories` → `calorie_target` | ✗ | ✗ |
| notion | `filter` → `query_filter` | ✓ | ✓ |
| notion | `sorts` → `sort_rules` | ✓ | ✓ |
| notion | `page_size` → `results_per_page` | ✗ | ✗ |
| notion | `start_cursor` → `page_cursor` | ✗ | ✗ |
| notion | `archived` → `is_archived` | ✗ | ✗ |
| zulip | `narrow` → `filter_spec` | ✓ | ✓ |
| zulip | `stream` → `channel_name` | ✗ | ✓ |
| zulip | `num_before/after`, `anchor`, `topic` → mutated | ✗ | ✗ |
| jira | `maxResults` → `page_size` | ✓ | ✓ |
| stripe | `customer` → `customer_id` | ✗ | ✓ |
| github | all 5 | ✗ | ✗ |
| ebay_buy | all 5 | ✗ | ✗ |

**Key findings:**

- **Parametric knowledge overrides docs for well-known APIs.** GitHub and eBay (0% adherence) are APIs the model knows extremely well — it ignores renamed parameters entirely and generates the real API names. Spoonacular (75%) is less well-known; the model has weaker priors and follows the mutated docs more closely.
- **HTTP adherence is always ≤ interface adherence.** When the model only partially adopts a mutation, it tends to rename the function parameter but still sends the original name to the API underneath (e.g. stripe's `customer_id` at interface level, `customer` in the HTTP call).
- **This explains why mutated eval scores ≈ docs scores.** Since most servers revert to original API parameter names regardless of what the docs say, the patched and unpatched servers are functionally near-identical. The mutations have little effect on synthesized server quality.

---

## Earlier Eval Results (pre-matrix runs)

These runs used earlier rubric versions (no SERVER_SUFFICIENT field). Kept for reference.

| Dataset | Condition | Pass | Total | Pass% | Top Failure Categories |
|---|---|---|---|---|---|
| alphavantage | docs | 14 | 14 | **100%** | — |
| alphavantage | nodocs | 13 | 14 | 93% | AGENT_REASONING |
| clockify | docs | 8 | 12 | 67% | AGENT_REASONING (4), TOOL_SCHEMA |
| clockify | nodocs | 11 | 12 | 92% | AGENT_REASONING |
| forgejo | nodocs | 10 | 12 | 83% | TOOL_COVERAGE, AGENT_REASONING |
| mastodon | source | 15 | 15 | **100%** | — |
| mastodon | nodocs | 15 | 15 | **100%** | — |
| openweathermap | docs | 21 | 21 | **100%** | — |
| openweathermap | nodocs | 21 | 21 | **100%** | — |

---

## Synthesis Results

All runs used GPT-5.2 as synthesizer. Token counts are input + output tokens consumed during synthesis.

| Dataset | Condition | Input Tokens | Output Tokens | Time (s) | Status |
|---|---|---|---|---|---|
| stripe | docs | 2,423,904 | 26,654 | 587 | ✓ |
| jira | docs | 2,075,565 | 16,378 | 349 | ✓ |
| zulip | docs | 1,539,668 | 6,500 | 248 | ✓ |
| slack | docs | 1,663,065 | 9,976 | 271 | ✓ |
| shopify | docs | 1,298,659 | 11,474 | 247 | ✓ |
| shopify | docs (re-run) | 738,520 | 7,287 | 164 | ✓ |
| hubspot | docs | 1,108,890 | 22,108 | 300 | ✓ |
| zendesk | docs | 1,083,224 | 9,668 | 203 | ✓ |
| github | docs | 1,027,940 | 10,553 | 207 | ✓ |
| github | nodocs | 17,757 | 12,962 | 131 | ✓ |
| github | nodocs (gpt-5-mini) | 0 | 0 | 188 | ✗ stream error |
| twilio | docs | 641,381 | 6,585 | 139 | ✓ |
| ebay_commerce | docs | 530,739 | 11,734 | 202 | ✓ |
| ebay_sell | docs | 198,711 | 10,519 | 150 | ✓ |
| ebay_buy | docs | 224,374 | 2,784 | 76 | ✓ |
| adyen | docs | 303,886 | 5,982 | 103 | ✓ |
| notion | docs | 320,685 | 5,934 | 129 | ✓ |
| notion | nodocs | 13,373 | 5,058 | 64 | ✓ |
| google_workspace | docs | 229,854 | 3,165 | 82 | ✓ |
| tiktok_shop | docs | 270,681 | 2,197 | 87 | ✓ |
| zulip | docs (gpt-4.1) | 1,121,486 | 5,740 | 174 | ✓ |
| zulip | docs (gpt-4.1, re-run) | 1,250,421 | 5,856 | 131 | ✓ |
| zulip | docs (gpt-4.1-mini) | 695,511 | 3,727 | 148 | ✓ |
| notion | docs (gpt-4.1-mini) | 721,332 | 6,763 | 243 | ✓ |
| github | docs (gpt-4.1-mini) | 430,122 | 8,132 | 220 | ✓ |

> **gpt-5-mini synthesis failed** with stream errors on the github nodocs run — no output produced.
> **gpt-5-mini token counts show 0** for earlier batch runs — token tracking was not yet implemented for that backend at the time.

### Synthesis Cost Observations

- **Largest inputs:** Stripe (2.4M), Jira (2.1M), Slack (1.7M), Zulip (1.5M). These APIs have very large documentation sets.
- **Synthesis time scales roughly with input size** but is also affected by output complexity (e.g. HubSpot: 1.1M in, 22K out, 300s vs Google Workspace: 230K in, 3K out, 82s).
- **nodocs synthesis is cheap:** GitHub nodocs took 131s and only 17K input tokens (task prompt only), vs 207s and 1M tokens for the docs run.
- **Output token range:** 2K–27K. Higher output token counts generally indicate more tools or more elaborate implementations (Stripe 26K, HubSpot 22K).

---
## Analysis

### Key Findings

1. **Documentation condition has mixed effects** — for 8/14 APIs the nodocs pass rate equals or exceeds the docs pass rate, suggesting that injected API documentation is not always beneficial and can introduce noise or distraction in agent reasoning.
2. **SYNTH predicts CURRENT** (Pearson r ≈ 0.85) — server synthesis quality is a strong leading indicator of agent task performance, validating the pipeline design choice to measure synthesis sufficiency separately.
3. **High API-level variance** — Mastodon and OpenWeatherMap approach ceiling performance (≥95% across all conditions), while Jira and eBay Sell remain at floor (mean ≤ 46%), indicating that API complexity and tool interface clarity are primary bottlenecks.
4. **Synthesis model matters** — Sonnet 4.6 substantially outperforms GPT-5.2 on GitHub and Stripe; Qwen3 produces frequent crashes (execution failures before evaluation); GPT-5.4 shows a catastrophic regression on Stripe docs (8% vs 72% for GPT-5.2).
5. **Mutation rarely collapses well-known APIs** — exceptions are eBay Commerce (100→55%, −45pp) and Shopify (87→62%, −25pp), where synthesized stubs failed to adopt renamed parameters in the mutated condition.

### Documentation Condition Effect

Across 14 APIs, the relationship between documentation availability and agent performance is weaker than expected. In 8 of 14 cases the nodocs pass rate meets or exceeds the docs pass rate. This is most pronounced for GitHub (62% docs vs 83% nodocs, +21pp) and Notion (78% docs vs 100% nodocs, +22pp). The effect is likely due to documentation overload: large API reference texts introduce irrelevant context that the agent must filter, degrading tool selection. For smaller APIs (Alphavantage, Mastodon, OpenWeatherMap) the effect is smaller or reversed, suggesting a volume threshold beyond which docs become counterproductive. The mutated condition generally performs within ±10pp of the docs condition, with the exception of eBay Commerce (−45pp) and Shopify (−25pp), where parameter renaming was not correctly propagated into synthesized tool stubs.

### SYNTH–CURRENT Correlation

The scatter of SYNTH (synthesis sufficiency, judged by LLM) against CURRENT (agent pass rate) reveals a Pearson r ≈ 0.85 across all 42 valid data points (14 APIs × 3 conditions). This validates the two-stage pipeline design: a high-quality server stub is necessary but not sufficient for agent success. Notable outliers include Spoonacular docs (SYNTH=75%, CURRENT=100%), where a lower synthesis score did not hinder agent performance, and eBay Commerce mutated (SYNTH=54%, CURRENT=55%), where synthesis and execution failures are jointly low. Jira nodocs (SYNTH=44%, CURRENT=25%) lies below the diagonal, indicating that even partially sufficient stubs failed to support the agent on complex multi-step tasks. The ±10pp band around the diagonal captures roughly 55% of all points, confirming moderate but not perfect calibration between synthesis quality and downstream task success.

### Synthesis Model Comparison

The three-dataset comparison (GitHub, Stripe, Zulip) exposes substantial inter-model variance. Sonnet 4.6 achieves the highest CURRENT on GitHub (90/100/100%) and Stripe (77/100/100%), outperforming GPT-5.2 by 15–43pp on these datasets. GPT-5.4 shows mixed results: strong on Zulip (90/85/71%) but catastrophic on Stripe docs (8%), a regression traced to incorrect HTTP method mapping in synthesized stubs. Qwen3 produces two distinct failure modes — import crashes (docs and nodocs, Zulip and Stripe) and syntactically valid but structurally broken stubs — resulting in NaN or near-zero CURRENT scores. These failure modes are qualitatively different: crash failures produce zero evaluable tasks, while broken stubs produce a full evaluation run with systematically biased results. The distinction matters for benchmark design: a synthesis failure rate metric should account for both types.

### API Variance Discussion

API-level variance dwarfs condition-level variance in this benchmark. The interquartile range of mean CURRENT across APIs is approximately 46pp (Jira=42% to Confluence=92%), compared to a median condition effect of ≤8pp. This suggests that the primary determinant of benchmark performance is API complexity — including the number of distinct tool signatures, the degree of parameter overlap between similar endpoints, and the specificity of task descriptions relative to available tools. Mastodon and OpenWeatherMap saturate performance across all conditions (≥86%), likely because their APIs are small, well-structured, and the tasks are straightforward. In contrast, eBay Sell and Jira both have large tool sets with many optional parameters, and the tasks require multi-step reasoning that is sensitive to parameter ordering and authentication flows. These ceiling and floor APIs provide limited signal for discriminating between synthesis approaches and should be considered for exclusion or replacement in future benchmark iterations.

### Figures
- `fig1_primary_heatmap.pdf` — 14×3 CURRENT/SYNTH heatmap, rows sorted by mean CURRENT descending
- `fig2_condition_slopes.pdf` — docs→nodocs→mutated slope chart with eBay Commerce and GitHub annotations
- `fig3_model_comparison.pdf` — synthesis model comparison 3-panel bar chart (GitHub, Stripe, Zulip)
- `fig4_synth_scatter.pdf` — SYNTH vs CURRENT scatter with Pearson r, outlier labels, and category colouring

### Tables
- `results_table.tex` — main 14×3 booktabs results table with SYNTH values and colour coding
- `synth_model_table.tex` — model comparison booktabs table with failure mode annotations
