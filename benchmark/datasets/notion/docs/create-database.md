# create-database

*Source: https://developers.notion.com/reference/create-database*

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
The parent page or workspace where the database will be created.
Showchild attributes
The title of the database.
The description of the database.
Whether the database should be displayed inline in the parent page. Defaults to false.
Initial data source configuration for the database.
The icon for the database.
The cover image for the database.
The database object type name.
The ID of the database.

```
import{Client}from"@notionhq/client"constnotion=newClient({auth:process.env.NOTION_API_KEY})constresponse=awaitnotion.databases.create({parent:{type:"page_id",page_id:"b55c9c91-384d-452b-81db-d1ef79372b75"},title:[{text:{content:"My Database"} }]})
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
- Blocks
- Pages
- DatabasesPOSTCreate a databasePATCHUpdate a databaseGETRetrieve a database
- Data sources
- Databases (deprecated)
- Comments
- Views
- File Uploads
- Search
- Users
- POSTCreate a database
- PATCHUpdate a database
- GETRetrieve a database
- Databases
- File uploads
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