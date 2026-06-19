# move-page

*Source: https://developers.notion.com/reference/move-page*

---

##### Notion API

##### Objects

##### Endpoints

##### Webhook events

## ​Authentication

## ​Path parameters

## ​Body parameters

### ​Page parent

### ​Database parent

## ​Example requests

### ​Move page under another page

### ​Move page into a database

#### Authorizations

#### Headers

#### Path Parameters

#### Body

#### Response
Bearer authentication header of the formBearer <token>, where<token>is your auth token.
TheAPI versionto use for this request. The latest version is2026-03-11.
The ID of the page to move.
The new parent of the page.
Showchild attributes
The page object type name.
The ID of the page.

```
import { Client } from "@notionhq/client"

const notion = new Client({ auth: process.env.NOTION_API_KEY })

const response = await notion.pages.move({
  page_id: "b55c9c91-384d-452b-81db-d1ef79372b75",
  parent: {
    page_id: "3c357473-a281-49a4-88c0-10d2b245a589"
  }
})
```

```
{
  "object": "<string>",
  "id": "3c90c3cc-0d44-4b50-8888-8dd25736052a"
}
```

```
{"parent": {"type":"page_id","page_id":"<parent-page-id>"}}
```

```
{"parent": {"type":"data_source_id","data_source_id":"<database-data-source-id>"}}
```

```
curl-XPOSThttps://api.notion.com/v1/pages/195de9221179449fab8075a27c979105/move\-H"Authorization: Bearer secret_xxx"\-H"Notion-Version: 2026-03-11"\-H"Content-Type: application/json"\-d'{"parent": {"type": "page_id","page_id": "f336d0bc-b841-465b-8045-024475c079dd"}}'
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
- PagesPOSTCreate a pageGETRetrieve a pageGETRetrieve a page property itemPOSTMove a pageUpdate pageMarkdown content
- Databases
- Data sources
- Databases (deprecated)
- Comments
- Views
- File Uploads
- Search
- Users
- POSTCreate a page
- GETRetrieve a page
- GETRetrieve a page property item
- POSTMove a page
- Update page
- Markdown content
- Pages
- File uploads
- Type:string(UUIDv4)
- Description: The ID of the page to moveThis must be a regular Notion page, and not a database. Moving databases or other block types in the API is not currently supported.
- Format: UUIDs can be provided with or without dashes
- Example:195de9221179449fab8075a27c979105or195de922-1179-449f-ab80-75a27c979105
- This must be a regular Notion page, and not a database. Moving databases or other block types in the API is not currently supported.
- Type:object
- Description: The new parent location for the page.The bot must have edit access to the new parent.
- The bot must have edit access to the new parent.
- type: Always"page_id"
- page_id: UUID of the parent page (with or without dashes)
- type: Always"data_source_id"
- data_source_id: UUID of the database’s data source (with or without dashes)
- Option 1
- Option 2