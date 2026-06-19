# comment-display-name

*Source: https://developers.notion.com/reference/comment-display-name*

---

##### Notion API

##### Objects

##### Endpoints

##### Webhook events

## ​Request format (input)

### ​Object properties

## ​Response format (output)

```
{"parent": {"page_id":"d0a1ffaf-a4d8-4acf-a1ed-abae6e110418"},"rich_text": [{"text": {"content":"Thanks for checking us out!"}}],"display_name": {"type":"custom","custom": {"name":"Notion Bot"}}}
```

```
{...existingparametersomitted,"display_name": {"type":"custom","resolved_name":"Notion Bot"}}
```
- Status
- Community
- Blog
- Introduction
- Integration capabilities
- Webhooks
- Request limits
- Status codes
- Versioning
- Block
- Page
- Database
- Data source
- View
- CommentOverviewComment attachmentComment display name
- File
- User
- Parent
- Emoji
- Unfurl attribute (Link Previews)
- Overview
- Comment attachment
- Comment display name
- Authentication
- Blocks
- Pages
- Databases
- Data sources
- Databases (deprecated)
- Comments
- Views
- File Uploads
- Search
- Users
- File uploads
- Request format (input)
- Object properties
- Response format (output)
- "integration": name of theintegration
- "user": name of the user who authenticated the integration (only forPublic Integrations)
- "custom": any custom name

[TABLE]
Parameter | Type | Description | Example value
type | string(enum) | Possible type values are:"integration","user", or"custom" | "user"
custom | object | If the type is"custom", include a custom object specifying the custom name"custom": { "name": <Custom Name> } | "custom": { "name": "Notion Bot" }
[/TABLE]

[TABLE]
Field | Type | Description | Example value
type | string(enum) | Possible type values are:"integration","user", or"custom" | "custom"
resolved_name | string | The custom display name shown in a comment | "Notion Bot"
[/TABLE]