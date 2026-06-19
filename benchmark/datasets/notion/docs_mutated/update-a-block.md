# update-a-block

*Source: https://developers.notion.com/reference/update-a-block*

---

##### Notion API

##### Objects

##### Endpoints

##### Webhook events

### ​Success

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
import{Client}from"@notionhq/client"constnotion=newClient({auth:process.env.NOTION_API_KEY})constresponse=awaitnotion.blocks.update({block_id:"c02fc1d3-db8b-45c5-a222-27595b15aea7",paragraph:{rich_text:[{text:{content:"Updated paragraph text"} }]}})
```

```
{"object":"<string>","id":"3c90c3cc-0d44-4b50-8888-8dd25736052a"}
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
- Table
- Column
- Option 30
- Option 1
- Child Page
- Child Database
- Column List
- Meeting Notes
- Link Preview
- Unsupported