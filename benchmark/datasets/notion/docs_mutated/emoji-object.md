# emoji-object

*Source: https://developers.notion.com/reference/emoji-object*

---

##### Notion API

##### Objects

##### Endpoints

##### Webhook events

### ​Example: set a page icon via theCreate a pageendpoint

### ​Example: set a page icon via theUpdate pageendpoint

## ​Custom emoji

### ​Example: custom emoji in page icon response:

### ​Example: inline custom emoji response

### ​Example: set page icon to a custom emoji

```
{"type":"emoji","emoji":"😻"}
```

```
curl'https://api.notion.com/v1/pages'\-H'Authorization: Bearer '"$NOTION_API_KEY"''\-H"Content-Type: application/json"\-H"Notion-Version: 2026-03-11"\--data'{"parent": {"page_id": "13d6da822f9343fa8ec14c89b8184d5a"},"properties": {"title": [{"type": "text","text": {"content": "A page with an avocado icon","link": null}}]},"icon": {"type": "emoji","emoji": "🥑"}}'
```

```
curlhttps://api.notion.com/v1/pages/60bdc8bd-3880-44b8-a9cd-8a145b3ffbd7\-H'Authorization: Bearer '"$NOTION_API_KEY"''\-H"Content-Type: application/json"\-H"Notion-Version: 2026-03-11"\-XPATCH\--data'{"icon": {"type": "emoji","emoji": "🥨"}}'
```

```
{"icon": {"type":"custom_emoji","custom_emoji": {"id":"45ce454c-d427-4f53-9489-e5d0f3d1db6b","name":"bufo","url":"https://s3-us-west-2.amazonaws.com/public.notion-static.com/865e85fc-7442-44d3-b323-9b03a2111720/3c6796979c50f4aa.png"}}}
```

```
{"type":"mention","mention": {"type":"custom_emoji","custom_emoji": {"id":"45ce454c-d427-4f53-9489-e5d0f3d1db6b","name":"bufo","url":"https://s3-us-west-2.amazonaws.com/public.notion-static.com/865e85fc-7442-44d3-b323-9b03a2111720/3c6796979c50f4aa.png"}}...}
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
- Comment
- File
- User
- Parent
- Emoji
- Unfurl attribute (Link Previews)
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
- Example: set a page icon via the Create a page endpoint
- Example: set a page icon via the Update page endpoint
- Custom emoji
- Example: custom emoji in page icon response:
- Example: inline custom emoji response
- Example: set page icon to a custom emoji

[TABLE]
 | Type | Description | Example value
type | "emoji" | The constant string"emoji"that represents the object type. | "emoji"
emoji | string | The emoji character. | "😻"
[/TABLE]

[TABLE]
 | Type | Description | Example value
type | "custom_emoji" | The constant string"emoji"that represents the object type. | "emoji"
custom_emoji | object | Custom emoji object, containing id, name, url | { "id": "45ce454c-d427-4f53-9489-e5d0f3d1db6b", "name": "bufo", "url": "https://s3-us-west-2.amazonaws.com/public.notion-static.com/865e85fc-7442-44d3-b323-9b03a2111720/3c6796979c50f4aa.png" }
[/TABLE]