# Quick Start Guide - Notion API MCP Server

## 5-Minute Setup

### Step 1: Get Your Notion API Key
1. Go to https://www.notion.so/my-integrations
2. Create a new integration
3. Copy the "Internal Integration Token"

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Set Environment Variable
```bash
export NOTION_API_KEY="your-integration-token-here"
```

### Step 4: Start the Server
```bash
python server.py
```

The server is now running and ready to receive MCP protocol messages!

## Common Tasks

### Create a Page
```python
create_page(
    parent_type="database_id",
    parent_id="d9824bdc-8445-4327-be8b-5b47500af6ce",
    properties={
        "Name": {
            "title": [{"text": {"content": "My New Page"}}]
        }
    }
)
```

### Query a Database
```python
query_database(
    database_id="d9824bdc-8445-4327-be8b-5b47500af6ce",
    filter={
        "property": "Status",
        "select": {"equals": "Done"}
    }
)
```

### Add Content to a Page
```python
append_block_children(
    block_id="page-id",
    children=[
        {
            "type": "paragraph",
            "paragraph": {
                "rich_text": [
                    {"text": {"content": "Hello, world!"}}
                ]
            }
        }
    ]
)
```

### Search for Pages
```python
search(
    query="meeting notes",
    filter={"property": "object", "value": "page"}
)
```

### List Users
```python
list_users(page_size=10)
```

## Available Tools (38 Total)

### Pages
- create_page, retrieve_page, update_page, archive_page, restore_page, move_page, retrieve_page_property

### Databases
- create_database, retrieve_database, update_database, query_database

### Blocks
- retrieve_block, get_block_children, append_block_children, update_block, delete_block

### Comments
- create_comment, retrieve_comment, list_comments

### Users
- list_users, retrieve_user, get_bot_user

### Search
- search

### Data Sources
- create_data_source, retrieve_data_source, query_data_source, update_data_source, list_data_source_templates

### Views
- create_view, retrieve_view, update_view, delete_view, list_views, create_view_query, get_view_query_results, delete_view_query

### File Uploads
- create_file_upload, retrieve_file_upload, list_file_uploads, complete_file_upload

## Troubleshooting

### "NOTION_API_KEY environment variable not set"
Make sure you've set the environment variable:
```bash
export NOTION_API_KEY="your-token"
```

### "API error 404"
The resource doesn't exist. Check the ID is correct.

### "API error 401"
Your API key is invalid or expired. Get a new one from https://www.notion.so/my-integrations

### "API error 403"
Your integration doesn't have permission. Share the resource with your integration in Notion.

## Next Steps

1. Read [README.md](README.md) for detailed documentation
2. Check [IMPLEMENTATION.md](IMPLEMENTATION.md) for architecture details
3. See [grounding.json](grounding.json) for tool-to-documentation mapping
4. Review [DELIVERABLES.md](DELIVERABLES.md) for complete feature list

## Integration with Agents

The server runs over stdio and implements the MCP protocol, making it compatible with:
- Claude (via MCP)
- Other MCP-compatible agents
- Custom MCP clients

Send MCP protocol messages to interact with the server.

## Example: Full Workflow

```python
# 1. Create a database
db = create_database(
    parent_type="page_id",
    parent_id="your-page-id",
    title=[{"text": {"content": "Tasks"}}],
    properties={
        "Name": {"title": {}},
        "Status": {"select": {
            "options": [
                {"name": "To Do", "color": "red"},
                {"name": "Done", "color": "green"}
            ]
        }}
    }
)

# 2. Create a page in the database
page = create_page(
    parent_type="database_id",
    parent_id=db["id"],
    properties={
        "Name": {"title": [{"text": {"content": "Task 1"}}]},
        "Status": {"select": {"name": "To Do"}}
    }
)

# 3. Add content to the page
append_block_children(
    block_id=page["id"],
    children=[
        {
            "type": "paragraph",
            "paragraph": {
                "rich_text": [{"text": {"content": "This is the task description"}}]
            }
        }
    ]
)

# 4. Query the database
results = query_database(
    database_id=db["id"],
    filter={"property": "Status", "select": {"equals": "To Do"}}
)

# 5. Update the page
update_page(
    page_id=page["id"],
    properties={
        "Status": {"select": {"name": "Done"}}
    }
)
```

## Tips & Best Practices

1. **Use IDs without dashes**: Notion accepts UUIDs with or without dashes
2. **Pagination**: Use `start_cursor` and `page_size` for large result sets
3. **Filters**: Use complex filters with AND/OR logic for powerful queries
4. **Rich Text**: All text content uses rich text format with formatting options
5. **Error Handling**: Always check for `error` field in responses
6. **Rate Limiting**: Notion API has rate limits; implement exponential backoff

## Documentation

- **Full API Docs**: See [README.md](README.md)
- **Implementation Details**: See [IMPLEMENTATION.md](IMPLEMENTATION.md)
- **Tool Mapping**: See [grounding.json](grounding.json)
- **Notion API Reference**: https://developers.notion.com/reference

## Support

For issues:
1. Check the error message in the response
2. Verify your API key and permissions
3. Ensure the resource exists and is shared with your integration
4. Check [Notion API docs](https://developers.notion.com/) for endpoint details

---

**Ready to go!** Your Notion API MCP server is now running. 🚀
