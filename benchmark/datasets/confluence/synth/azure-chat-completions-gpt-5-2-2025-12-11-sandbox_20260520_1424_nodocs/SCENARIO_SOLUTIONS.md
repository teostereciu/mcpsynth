# Scenario Solutions

## 1) Create a page in the default space under a parent
1. Resolve parent page id (if needed) via `search_cql` (e.g. `space = "SYNTH" and title ~ "Home"`).
2. Call `create_page(title, body_storage, parent_id=..., space_id=...)`.

## 2) Update a page safely
1. Call `get_page(page_id)` to inspect current content.
2. Call `update_page(page_id, title=..., body_storage=...)` (server auto-increments version if not provided).

## 3) Move a page
1. Call `move_page(page_id, target_parent_id, position="append")`.

## 4) Add and remove labels
1. `add_content_labels(content_id, ["label-a", "label-b"])`
2. `list_content_labels(content_id)`
3. `remove_content_label(content_id, "label-a")`

## 5) Upload and download an attachment
1. `upload_attachment(page_id, "/path/to/file.pdf")`
2. Find attachment id from `list_attachments(page_id)`.
3. `download_attachment(attachment_id)` returns base64 content.

## 6) Comment on a page
1. `create_page_comment(page_id, body_storage, comment_type="footer")`
2. `list_page_comments(page_id, comment_type="footer")`

## 7) Restore an older version
1. `list_page_versions(page_id)`
2. `restore_page_version(page_id, version_number)`

## 8) Store metadata on a page
1. `set_content_property(page_id, "my.key", {"any": "json"})`
2. `get_content_property(page_id, "my.key")`

## 9) Work with spaces
- `list_spaces()`
- `get_space(space_key="SYNTH")` or `get_space(space_id=123)`
- `create_space(key, name)`
- `delete_space(space_key)`

## 10) Identify users
- `get_current_user()`
- `get_user(account_id)`
