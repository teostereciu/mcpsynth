# Scenario solutions

## Auth / configuration

Set environment variables:

- `CONFLUENCE_BASE_URL` = `https://your-domain.atlassian.net`
- Either:
  - `CONFLUENCE_BEARER_TOKEN` (OAuth 2.0 access token)
  - or `CONFLUENCE_EMAIL` + `CONFLUENCE_API_TOKEN` (API token for basic auth)

Run:

```bash
python server.py
```

## Scenario: Find pages by keyword and label them

1) Search with CQL:

- Tool: `confluence_v1_search`
- Args:
  - `cql`: `type=page AND text~"onboarding"`
  - `limit`: 25

2) Add a label to a page:

- Tool: `confluence_v1_add_labels_to_content`
- Args:
  - `id`: `<contentId>`
  - `labels`: `[{"prefix":"global","name":"onboarding"}]`

## Scenario: Create a space and a page

1) Create space:

- Tool: `confluence_v2_post_spaces`
- Body example:

```json
{
  "key": "ENG",
  "name": "Engineering",
  "type": "global"
}
```

2) Create page:

- Tool: `confluence_v2_post_pages`
- Body example:

```json
{
  "spaceId": 12345,
  "status": "current",
  "title": "Runbook",
  "body": {
    "representation": "storage",
    "value": "<p>Hello</p>"
  }
}
```

## Scenario: Use an endpoint not covered by a dedicated tool

Use `confluence_request`.

Example: get content by id (v1):

```json
{
  "method": "GET",
  "path": "/wiki/rest/api/content/123456",
  "query": {"expand": "body.storage,version"}
}
```
