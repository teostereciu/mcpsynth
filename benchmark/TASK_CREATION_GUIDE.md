# Task Creation Guidelines

Tasks are the unit of measurement for tool quality. A good task produces a **clean signal**:
a pass means the tool worked correctly; a fail means it did not. Tasks that are ambiguous,
infeasible, or dominated by agent reasoning noise undermine the study.

---

## Difficulty calibration

The benchmark is designed so that a **well-implemented MCP server** (complete tool coverage,
accurate docstrings, well-structured responses) should achieve **90–100% pass rate** on its
dataset. The **current generation of synthesized servers** is expected to score **40–60%**,
revealing gaps in coverage, parameter documentation, and response structure.

This spread is what makes the benchmark useful: it demonstrates that tool quality varies and
is measurable. Tasks that are trivially passable by any implementation provide no signal;
tasks that are impossible for even a good implementation are noise. Calibrate towards the
middle: a capable agent on a good server should pass, a capable agent on a weak server
should fail.

---

## Prompt writing principles

### 1. Goal-oriented, not step-by-step
Describe what to accomplish, not which tool to call. A well-documented MCP server should
guide the agent to the correct endpoint through tool names and descriptions alone. Omitting
tool names and parameter names from prompts directly tests documentation quality.

```yaml
# Bad — tells the agent which tool and parameter to use
prompt: >
  Call the search tool with query "wireless headphones" and limit=5.
  Report the itemId of each result.

# Good — describes the goal; tool docs guide the rest
prompt: >
  Search for "wireless headphones" on eBay. Report the title, price, and
  item ID of the first 5 results.
```

### 2. State API constraints; omit mechanics
Some API requirements are invisible without domain knowledge (e.g. Notion pages require a
parent, Stripe amounts are in cents, eBay sandbox may return empty results). These must be
stated in the prompt — omitting them would make tasks fail for the wrong reason. What should
**not** be stated is how to satisfy the constraint: which tool to use, what the parameter
is called, or how it is structured. Those come from tool docs.

```yaml
# Bad — gives away the mechanics
prompt: >
  Search for an accessible parent page, extract its page_id, and pass it
  as the parent parameter to create_page. Create a page titled "Test".

# Good — states the constraint, omits the mechanics
prompt: >
  Under an accessible parent page, create a page titled "Test". Report its ID.
```

### 3. Only provide values that cannot be derived from tools
Test tokens (e.g. `tok_visa`), specific category IDs, and sandbox-specific constants are
domain knowledge that does not appear in any tool description. Provide these. Do not provide
parameter names, enum values, or endpoint paths that a well-documented tool would expose.

### 4. Synthesis over echo
Where possible, ask the agent to compare, rank, count, or filter results rather than just
reporting the first API response. Synthesis tasks fail when tool responses are malformed or
incomplete, which is a meaningful tool quality signal.

```yaml
# Weak — passes as long as any weather response is returned
prompt: >
  Get the weather for London. Report what you find.

# Stronger — requires two calls and a comparison
prompt: >
  Get the current humidity in Singapore and in Phoenix, USA. Report the
  humidity percentage for each and which is currently more humid.
```

### 5. Limit chain length
Tasks should not require more than six sequentially dependent API calls. Longer chains make
failure attribution harder: did the agent fail because of a later tool, or because it failed
to parse an earlier response? The sweet spot is 2–4 steps. Go up to 6 for complex workflow
tasks (e.g. create customer → product → price → subscribe → verify), but every step in the
chain should exercise a distinct and meaningful tool, not just repeat the same call.

### 6. Expected values must be specific
The `expected` field is passed to the judge as a verification hint. Choose values that only
appear in the response if the agent called the correct tool with correct parameters:

- **Good**: `cus_`, `feels_like`, `Agent Child Page`, `Kai` — specific to correct execution
- **Weak**: `type`, `object`, `data` — appear in virtually any API response
- **Never**: trivially guessable strings like city names that appear regardless of tool use

---

## Before adding a task — checklist

### Feasibility with the bench setup
- **Credential type**: Can this endpoint be called with the test credentials? Bot accounts,
  sandbox keys, and OAuth refresh tokens each have different scopes. Verify before adding.
  - *Example*: Zulip bot accounts cannot call `POST /users/me/status` — do not add tasks for it.
  - *Example*: eBay Identity API requires user OAuth, not app credentials — skip or mark accordingly.
- **Sandbox/test mode**: Does the API have a sandbox? If not, is it safe to run against production?
  Write tasks must use clearly test-namespaced resources (see Cleanability below).
- **Rate limits**: Will running 10+ tasks hit a rate limit? Prefer endpoints with generous quotas.
- **Required setup**: Does the task assume pre-existing data (e.g. "list orders" when sandbox has none)?
  Either seed the data or phrase the task to accept an empty result gracefully.

### Usefulness — does it exercise real functionality?
- Prefer operations a developer would actually perform: creating resources, querying data,
  executing workflows.
- Skip purely administrative operations that are unlikely to be part of a synthesized MCP server
  (e.g. account settings, billing, user management of the account itself).
- Error-handling tasks are useful but should be limited to 1–2 per dataset.

### Frequency — how common is this operation?
- **Core operations** (CRUD on main resources) must be covered — these are the most likely to be
  synthesized and the most likely to be used.
- **Multi-step workflows** (create → update → retrieve, or A → B using A's output) are high value:
  they test parameter passing and response parsing, not just individual calls.
- **Niche operations** (e.g. batch APIs, pagination, webhook registration) are intentionally good
  additions — they are *less* likely to appear in a naive human implementation, so they
  discriminate well between strong and weak tools.

### Endpoint mapping difficulty
- **Clear mapping** (1 obvious endpoint): simple, tests basic coverage.
- **Moderate mapping** (agent must choose among 2–3 plausible tools): tests schema clarity.
- **Hard mapping** (requires chaining, inference, or non-obvious parameter): use sparingly,
  and only if the failure mode is unambiguously a tool issue, not agent reasoning.
- Avoid tasks where success depends entirely on the agent guessing a parameter value that is
  not in any tool description — those become AGENT_REASONING noise.

### Step count
| Steps | Character | Guidance |
|---|---|---|
| 1 | Smoke test | Include several — confirms basic tool presence and schema |
| 2–4 | Workflow | Sweet spot — tests chaining without excessive noise |
| 5–6 | Complex workflow | OK for multi-resource flows; every step must be meaningful |
| 7+ | Too long | Split into two tasks |

### Cleanability
- Every write task must create resources identifiable as test artifacts:
  - Use name prefixes: `"Agent Eval Test *"`, `"agent-eval-*"`, `"AGENT-TEST-*"`
  - Use distinct emails: `"*@example-mcp-eval.com"`
  - Use SKUs/IDs with a clear prefix: `"AGENT-TEST-SKU-001"`
- Avoid writing to shared resources that affect other users (e.g. posting to a public channel
  is fine; modifying org-level settings is not).
- If a task creates data that cannot be cleaned up (e.g. sent SMS), flag it in the comment.

### Verifiability — can we define `expected`?
- Every task should have an `expected` field: a substring that must appear in the final answer
  or a tool result if the task succeeded.
- Good `expected` values: resource ID prefixes (`cus_`, `CH`), key field names (`status`, `email`),
  a specific value that must be returned (`pending`, `hola`).
- If you cannot define a concrete `expected`, the task is probably too open-ended or the success
  criterion is ambiguous — tighten the prompt.

### Discriminative power — does it separate good from bad tools?
- **High value**: tasks that require correct type handling (boolean vs string, nested objects),
  correct enum values, or pagination — these catch implementation bugs.
- **High value**: niche endpoints that a basic synthesis might miss entirely (TOOL_COVERAGE signal).
- **Low value**: tasks where any response counts as success (e.g. "call this endpoint and report
  what you get") — too easy to game, produces no signal.
- **Low value**: tasks that depend on live data that varies (e.g. "get the latest price") —
  hard to judge without ground truth.

---

## Verdict categories and what they mean for you

| Verdict | Meaning | Action when you see many of these |
|---|---|---|
| **pass** | Tool worked correctly | Good — keep the task |
| **fail** | Tool issue (schema, impl, or coverage) | Good signal — investigate the tool |
| **undefined** | Agent reasoning error, ambiguous task, or infra issue | Review: is the task too hard to map? Is the prompt ambiguous? |

A high rate of `undefined` results on a dataset suggests the tasks are too reasoning-heavy
or the prompts are ambiguous. Aim for `undefined` < 20% of tasks per dataset.

---

## Template for a new task

```yaml
- id: <verb>_<resource>           # snake_case, imperative
  prompt: >
    <Goal description. State any necessary API constraints (e.g. "under an accessible
    parent page"). Do not name tools, parameters, or endpoints.>
    <What to report in the final answer.>
  expected: <specific substring that only appears if the task succeeded>
  tags: [read|write, multi-step?, workflow?, error-handling?]
  # Notes: why this task is here, what it discriminates, cleanup notes, caveats.
```

---

## Quick anti-patterns

- **No `expected`**: task has no verifiable success criterion.
- **Trivial `expected`**: value appears in any API response, not just correct ones.
- **Step-by-step instructions**: telling the agent which tool to call defeats the purpose.
- **Omitting API constraints**: agent can't know Notion requires a parent — tell it.
- **Assumes pre-existing data**: "list the orders you created last week" — sandbox is empty.
- **Scope creep**: task requires 7+ steps — break it into two tasks.
- **Admin operations**: "change the org timezone" — wrong scope for most credentials.
- **Unstable data**: "report the current BTC price" — cannot verify correctness.
- **Identity endpoints with bot credentials**: many APIs restrict `/me`-style endpoints to
  user OAuth tokens. Verify before adding.
