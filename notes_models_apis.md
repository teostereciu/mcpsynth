# Models & APIs: Key Observations

## 1. Model Overview

### Synthesis models

| Model | Context | Input $/1M | Output $/1M | Type | Notes |
|---|---|---|---|---|---|
| GPT-5.2 | 400K | $1.75 | $14.00 | Reasoning (closed) | Baseline synthesizer; architecture undisclosed |
| GPT-5.4 | 1.05M | $2.50 | $15.00 | Reasoning (closed) | 1M+ context; 2× premium above 272K tokens |
| GPT-5.4-mini | 400K | $0.75 | $4.50 | Reasoning (closed) | ~6× cheaper than GPT-5.4; found non-viable in synthesis |
| Claude Sonnet 4.6 | 1M | $3.00 | $15.00 | Chat (closed) | Rate-limited to 6 req/min on Vertex; most expensive input |
| Gemini 3.1 Pro | 1M | $2.00 | $12.00 | Chat (closed) | Preview only — no production SLA |
| Gemini 3.5 Flash | 1M | $1.50 | $9.00 | Chat (closed) | Found non-viable (synthesis abandonment); suspected MoE |
| Qwen3-Coder-Next | 262K | $0.11 | $0.80 | Chat (open-weight) | MoE: 80B total / ~3B active; run on H100 80GB |

### Evaluation models (fixed across all synthesis comparisons)

| Role | Model | Context | Input $/1M | Output $/1M | Notes |
|---|---|---|---|---|---|
| Agent | Gemini 2.5 Pro | 1M | $1.25 | $10.00 | Primary agent; 60 req/min limit |
| Judge | Gemini 3 Flash | 1M | ~$0.10 | ~$0.70 | 180 req/min; preview status |

---

## 2. Key Model Observations

**Architecture transparency.** Qwen3-Coder-Next is the only model in the study with publicly confirmed architecture: sparse MoE with 80B total parameters and ~3B active per token, using a hybrid Gated DeltaNet + Gated Attention design. All closed proprietary models decline to disclose parameter counts or MoE topology.

**Cost range for synthesis.** There is a ~14× spread in input cost from cheapest (Qwen3, $0.11/1M) to most expensive (Claude Sonnet 4.6, $3.00/1M). Output token cost dominates in practice: GPT-5.4 at $15/1M out versus Qwen3 at $0.80/1M out is a ~19× difference.

**Rate limits as a practical bottleneck.** Claude models on Vertex AI are severely rate-limited at 6 req/min — approximately 30× lower throughput than GPT or Gemini models (180 req/min). At scale (14 APIs × 25 tasks), this meaningfully constrains synthesis runs.

**Context window for synthesis.** Several APIs have very large documentation sets (Adyen: 591 files, Slack: 444 files). GPT-5.2 and GPT-5.4-mini are capped at 400K tokens on the eBay internal platform, while GPT-5.4, Claude Sonnet 4.6, and Gemini models offer 1M — relevant when the full doc set approaches or exceeds the 400K threshold.

**Evaluation model stability.** The agent (Gemini 2.5 Pro) and judge (Gemini 3 Flash) are held fixed across all synthesis model comparisons. This is the correct design: it isolates synthesis quality as the sole independent variable and ensures that differences in agent pass rate are attributable to the synthesizer, not to the evaluator.

**Open-weight vs. closed.** Qwen3-Coder-Next is the only open-weight model tested and the only one that can be self-hosted. This makes its cost fully controllable and its outputs reproducible without API dependency, but requires hardware (H100 80GB) and introduces operational overhead (vLLM server management, context-window truncation at 262K).

**Viability findings.** GPT-5.4-mini and Gemini 3.5 Flash were found non-viable as synthesizers. GPT-5.4-mini exhibited systematic synthesis failures; Gemini 3.5 Flash abandoned synthesis tasks. GPT-4.1 also failed due to incompatibility with the FastMCP API. This leaves GPT-5.2, GPT-5.4, Claude Sonnet 4.6, Gemini 3.1 Pro, and Qwen3-Coder-Next as the viable comparison set.

---

## 3. API Selection: Familiarity × Complexity

The 14 REST APIs in the benchmark were chosen to span a two-dimensional design space:

- **Familiarity** — the degree to which an API is likely represented in LLM pre-training data. Proxied by the API's age, GitHub presence, Stack Overflow volume, and open-source library ecosystem (e.g., PyPI wrappers). High-familiarity APIs (GitHub, Stripe, Slack) are heavily documented online and appear in millions of public code repositories. Low-familiarity APIs (Adyen, Alpha Vantage, Spoonacular) are more niche, less discussed publicly, or enterprise-gated.

- **Complexity** — the structural surface area of the API, proxied by the number of documentation files scraped for the benchmark (each file corresponds to one endpoint or conceptual group). This captures parameter density, number of endpoints, and depth of request/response schemas.

This two-axis design is motivated by the parametric gravity hypothesis: synthesis quality should be highest for high-familiarity / low-complexity APIs (strong prior, simple target) and most dependent on documentation quality for low-familiarity / high-complexity APIs.

### API classification

| API | Familiarity | Doc files | Notes |
|---|---|---|---|
| GitHub | Very High | 181 | Ubiquitous in pre-training; octokit, PyGithub, gh CLI widely documented |
| Slack | Very High | 445 | slack-sdk; extensively covered in public tutorials and Stack Overflow |
| Stripe | High | 120 | stripe-python; rich official docs; high SO presence |
| Notion | High | 94 | notion-client; growing but younger ecosystem |
| Jira | High | 101 | jira Python lib; large enterprise presence in public docs |
| Confluence | Medium | 47 | Less represented than Jira; v1/v2 split adds ambiguity |
| Zulip | Medium | 165 | Open-source; zulip-bots, zuliprc; moderate public presence |
| Mastodon | Medium | 35 | Open-source ActivityPub; Mastodon.py; smaller ecosystem |
| OpenWeatherMap | Medium | 4 | Simple API; pyowm wrapper exists; but few endpoints |
| Spoonacular | Low–Medium | 7 | Niche food API; limited public code; grouped docs |
| Alpha Vantage | Low–Medium | 9 | Financial data API; alpha-vantage lib exists but niche |
| eBay (Buy) | Low | 28 | Commerce API; enterprise-gated; limited open-source coverage |
| eBay (Commerce) | Low | 48 | Same ecosystem; even less public coverage |
| eBay (Sell) | Low | 192 | Large, versioned, enterprise-gated; minimal public code |
| Adyen | Very Low | 593 | Enterprise payment gateway; heavily versioned; almost no public code |

See the companion figure (`api_familiarity_complexity.png`) for the scatter plot.
