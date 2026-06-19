# retrieve-a-database

*Source: https://developers.notion.com/reference/retrieve-a-database*

---

##### Notion API

##### Objects

##### Endpoints

##### Webhook events

### ​Errors

### ​Additional resources

#### Authorizations

#### Headers

#### Path Parameters

#### Response
Bearer authentication header of the formBearer <token>, where<token>is your auth token.
TheAPI versionto use for this request. The latest version is2026-03-11.
ID of a Notion database, a container for one or more data sources.
The database object type name.
The ID of the database.

```
import{Client}from"@notionhq/client"constnotion=newClient({auth:process.env.NOTION_API_KEY})constresponse=awaitnotion.databases.retrieve({database_id:"d9824bdc-8445-4327-be8b-5b47500af6ce"})
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
- Databases
- Data sources
- Databases (deprecated)POSTCreate a databaseGETRetrieve a databaseGETGet databasesQuery a databaseUpdate a database
- Comments
- Views
- File Uploads
- Search
- Users
- POSTCreate a database
- GETRetrieve a database
- GETGet databases
- Query a database
- Update a database
- File uploads
- Retrieve a database
- Retrieve a data source
- How to share a database with your integration
- Working with databases guide
- Option 1
- Option 2