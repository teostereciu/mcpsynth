# Scenario solutions

This MCP server is designed for autonomous agents working with Confluence Cloud.

## Auth & configuration

Set environment variables:

- `CONFLUENCE_BASE_URL` = `https://<site>.atlassian.net`
- Either:
  - `CONFLUENCE_BEARER_TOKEN` (OAuth 2.0 access token)
  - OR `CONFLUENCE_EMAIL` + `CONFLUENCE_API_TOKEN` (API token)

All requests are sent to `CONFLUENCE_BASE_URL + /wiki/...`.

## Scenario 1: Find a page by title in a space and return its URL

1. Search with CQL:
   - Tool: `confluence_search_cql`
   - Example CQL: `space = "ENG" AND type = page AND title ~ "Runbook"`
2. From results, take `content.id`.
3. Fetch page details:
   - Tool: `confluence_get_page_by_id_v2`
4. Use returned `_links.webui` (or v1 `_links.webui`) to build the URL.

## Scenario 2: Create a new page under a parent

1. Create page:
   - Tool: `confluence_create_page_v2`
   - Provide `spaceId`, `title`, `parentId`, and `body` like:
     - `{"representation":"storage","value":"<p>Hello</p>"}`

## Scenario 3: Update an existing page safely (handle versioning)

1. Get current page:
   - Tool: `confluence_get_page_by_id_v2`
2. Read current version number (field varies by API response; commonly `version.number`).
3. Update with incremented version:
   - Tool: `confluence_update_page_v2`
   - Set `version_number = current + 1`

## Scenario 4: Full coverage endpoint call (not wrapped)

Use `confluence_request`.

Example: get attachments for a content item (v1):

- method: `GET`
- path: `/wiki/rest/api/content/{id}/child/attachment`
- query: `{ "limit": 25 }`

Example: list blog posts (v2):

- method: `GET`
- path: `/wiki/api/v2/blogposts`
- query: `{ "limit": 25 }`

## Scenario 5: Extract plain text from a page

- Tool: `confluence_extract_page_text_v2`
- This fetches `body.storage.value` and strips HTML tags (best-effort).

