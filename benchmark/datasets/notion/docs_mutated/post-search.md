# post-search

*Source: https://developers.notion.com/reference/post-search*

---

##### Notion API

##### Objects

##### Endpoints

##### Webhook events

### ​Errors

#### Authorizations

#### Headers

#### Body

#### Response
Bearer authentication header of the formBearer <token>, where<token>is your auth token.
TheAPI versionto use for this request. The latest version is2026-03-11.
Showchild attributes

```
import { Client } from "@notionhq/client"

const notion = new Client({ auth: process.env.NOTION_API_KEY })

const response = await notion.search({
  query: "meeting notes",
  query_filter: {
    property: "object",
    value: "page"
  },
  sort: {
    direction: "descending",
    timestamp: "last_edited_time"
  }
})
```

```
{
  "type": "<string>",
  "page_or_data_source": {},
  "object": "<string>",
  "next_cursor": "<string>",
  "has_more": true,
  "results": [
    {
      "object": "<string>",
      "id": "3c90c3cc-0d44-4b50-8888-8dd25736052a",
      "created_time": "2023-11-07T05:31:56Z",
      "last_edited_time": "2023-11-07T05:31:56Z",
      "in_trash": true,
      "is_archived": true,
      "is_locked": true,
      "url": "<string>",
      "public_url": "<string>",
      "parent": {
        "type": "<string>",
        "database_id": "3c90c3cc-0d44-4b50-8888-8dd25736052a"
      },
      "properties": {},
      "icon": {
        "type": "<string>",
        "emoji": "<string>"
      },
      "cover": {
        "type": "<string>",
        "file": {
          "url": "<string>",
          "expiry_time": "2023-11-07T05:31:56Z"
        }
      },
      "created_by": {
        "id": "3c90c3cc-0d44-4b50-8888-8dd25736052a",
        "object": "<string>"
      },
      "last_edited_by": {
        "id": "3c90c3cc-0d44-4b50-8888-8dd25736052a",
        "object": "<string>"
      }
    }
  ]
}
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
- SearchSearch by titlePOSTSearch by titleSearch optimizations and limitations
- Users
- Search by titlePOSTSearch by title
- Search optimizations and limitations
- POSTSearch by title
- File uploads
- Option 1
- Option 2
- Option 3
- Option 4