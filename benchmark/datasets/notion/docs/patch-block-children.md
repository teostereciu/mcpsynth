# patch-block-children

*Source: https://developers.notion.com/reference/patch-block-children*

---

##### Notion API

##### Objects

##### Endpoints

##### Webhook events

### ​Controlling insert position

### ​Errors

#### Authorizations

#### Headers

#### Path Parameters

#### Body

#### Response
Bearer authentication header of the formBearer <token>, where<token>is your auth token.
TheAPI versionto use for this request. The latest version is2026-03-11.
Showchild attributes

```
import{Client}from"@notionhq/client"constnotion=newClient({auth:process.env.NOTION_API_KEY})constresponse=awaitnotion.blocks.children.append({block_id:"c02fc1d3-db8b-45c5-a222-27595b15aea7",children:[{type:"paragraph",paragraph:{rich_text:[{text:{content:"Hello, world!"} }]}}]})
```

```
{"type":"<string>","block": {},"object":"<string>","next_cursor":"<string>","has_more":true,"results": [{"object":"<string>","id":"3c90c3cc-0d44-4b50-8888-8dd25736052a"}]}
```

```
{"children": [/* blocks */],"position": {"type":"start"}}
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
- BlocksPATCHAppend block childrenGETRetrieve a blockGETRetrieve block childrenPATCHUpdate a blockDELDelete a block
- Pages
- Databases
- Data sources
- Databases (deprecated)
- Comments
- Views
- File Uploads
- Search
- Users
- PATCHAppend block children
- GETRetrieve a block
- GETRetrieve block children
- PATCHUpdate a block
- DELDelete a block
- File uploads
- Before:{ "children": [...], "after": "<block_id>" }
- After:{ "children": [...], "position": { "type": "after_block", "after_block": { "id": "<block_id>" } } }
- Embed
- Bookmark
- Image
- Video
- Pdf
- Audio
- Code
- Equation
- Divider
- Breadcrumb
- Tab
- Table Of Contents
- Link To Page
- Table Row
- Table
- Column List
- Column
- Heading 1
- Heading 2
- Heading 3
- Paragraph
- Bulleted List Item
- Numbered List Item
- Quote
- To Do
- Toggle
- Template
- Callout
- Synced Block
- Option 1
- Option 2
- Option 3
- Child Page
- Child Database
- Meeting Notes
- Link Preview
- Unsupported

[TABLE]
Position type | Description
{ "type": "end" } | Insert at the end of the parent’s children (default behavior)
{ "type": "start" } | Insert at the beginning of the parent’s children
{ "type": "after_block", "after_block": { "id": "<block_id>" } } | Insert after the specified block
[/TABLE]