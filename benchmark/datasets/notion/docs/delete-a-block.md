# delete-a-block

*Source: https://developers.notion.com/reference/delete-a-block*

---

##### Notion API

##### Objects

##### Endpoints

##### Webhook events

### ​Errors

#### Authorizations

#### Headers

#### Path Parameters

#### Response
Bearer authentication header of the formBearer <token>, where<token>is your auth token.
TheAPI versionto use for this request. The latest version is2026-03-11.

```
import{Client}from"@notionhq/client"constnotion=newClient({auth:process.env.NOTION_API_KEY})constresponse=awaitnotion.blocks.delete({block_id:"c02fc1d3-db8b-45c5-a222-27595b15aea7"})
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
- Option 1
- Paragraph
- Heading 1
- Heading 2
- Heading 3
- Bulleted List Item
- Numbered List Item
- Quote
- To Do
- Toggle
- Template
- Synced Block
- Child Page
- Child Database
- Equation
- Code
- Callout
- Divider
- Breadcrumb
- Table Of Contents
- Tab
- Column List
- Column
- Link To Page
- Table
- Table Row
- Meeting Notes
- Embed
- Bookmark
- Image
- Video
- Pdf
- Audio
- Link Preview
- Unsupported