# update-a-database

*Source: https://developers.notion.com/reference/update-a-database*

---

##### Notion API

##### Objects

##### Endpoints

##### Webhook events

### ​How database property type changes work

### ​Interacting with database rows

### ​Recommended database schema size limit

### ​Errors

#### Authorizations

#### Headers

#### Path Parameters

#### Body

#### Response
Bearer authentication header of the formBearer <token>, where<token>is your auth token.
TheAPI versionto use for this request. The latest version is2026-03-11.
ID of a Notion database, a container for one or more data sources.
The parent page or workspace to move the database to. If not provided, the database will not be moved.
Showchild attributes
The updated title of the database, if any. If not provided, the title will not be updated.
The updated description of the database, if any. If not provided, the description will not be updated.
Whether the database should be displayed inline in the parent page. If not provided, the inline status will not be updated.
The updated icon for the database, if any. If not provided, the icon will not be updated.
The updated cover image for the database, if any. If not provided, the cover will not be updated.
Whether the database should be moved to or from the trash. If not provided, the trash status will not be updated.
Whether the database should be locked from editing in the Notion app UI. If not provided, the locked state will not be updated.
The database object type name.
The ID of the database.

```
import { Client } from "@notionhq/client"

const notion = new Client({ auth: process.env.NOTION_API_KEY })

const response = await notion.databases.update({
  database_id: "d9824bdc-8445-4327-be8b-5b47500af6ce",
  title: [{ text: { content: "Updated Database Title" } }]
})
```

```
{
  "object": "<string>",
  "id": "3c90c3cc-0d44-4b50-8888-8dd25736052a"
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
- Databases (deprecated)POSTCreate a databaseGETRetrieve a databaseGETGet databasesQuery a databaseUpdate a databasePATCHUpdate a databaseUpdate database properties
- Comments
- Views
- File Uploads
- Search
- Users
- POSTCreate a database
- GETRetrieve a database
- GETGet databases
- Query a database
- Update a databasePATCHUpdate a databaseUpdate database properties
- PATCHUpdate a database
- Update database properties
- File uploads
- Update a database
- Update a data source
- formula
- select
- status
- Synced content
- Amulti_selectdatabase property’s options values. An option can be removed, but not updated.
- Page Id
- Workspace
- Text
- Mention
- Equation
- File Upload
- External
- Custom Emoji
- Option 1
- Option 2