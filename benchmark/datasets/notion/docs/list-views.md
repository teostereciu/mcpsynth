# list-views

*Source: https://developers.notion.com/reference/list-views*

---

##### Notion API

##### Objects

##### Endpoints

##### Webhook events

### ​Errors

#### Authorizations

#### Headers

#### Query Parameters

#### Response
Bearer authentication header of the formBearer <token>, where<token>is your auth token.
TheAPI versionto use for this request. The latest version is2026-03-11.
ID of a Notion database (collection view block) to list views for. At least one of database_id or data_source_id is required.
ID of a data source (collection) to list all views for, including linked views across the workspace. At least one of database_id or data_source_id is required.
If supplied, this endpoint will return a page of results starting after the cursor provided. If not supplied, this endpoint will return the first page of results.
The number of items from the full list desired in the response. Maximum: 100
Showchild attributes

```
import { Client } from "@notionhq/client"

const notion = new Client({ auth: process.env.NOTION_API_KEY })

const response = await notion.views.list({
  database_id: "248104cd-477e-80fd-b757-e945d38000bd"
})
```

```
{
  "object": "<string>",
  "next_cursor": "3c90c3cc-0d44-4b50-8888-8dd25736052a",
  "has_more": true,
  "results": [
    {
      "object": "<string>",
      "id": "3c90c3cc-0d44-4b50-8888-8dd25736052a"
    }
  ],
  "type": "<string>",
  "view": {}
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
- ViewsPOSTCreate a viewGETRetrieve a viewPATCHUpdate a viewDELDelete a viewGETList viewsView queries
- File Uploads
- Search
- Users
- POSTCreate a view
- GETRetrieve a view
- PATCHUpdate a view
- DELDelete a view
- GETList views
- View queries
- File uploads
- Views