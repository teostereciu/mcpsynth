# retrieve-a-data-source

*Source: https://developers.notion.com/reference/retrieve-a-data-source*

---

##### Notion API

##### Objects

##### Endpoints

##### Webhook events

### ​Finding a data source ID

### ​Errors

### ​Additional resources

#### Authorizations

#### Headers

#### Path Parameters

#### Response
Bearer authentication header of the formBearer <token>, where<token>is your auth token.
TheAPI versionto use for this request. The latest version is2026-03-11.
ID of a Notion data source.
The data source object type name.
The ID of the data source.
The properties schema of the data source.
Showchild attributes

```
import{Client}from"@notionhq/client"constnotion=newClient({auth:process.env.NOTION_API_KEY})constresponse=awaitnotion.dataSources.retrieve({data_source_id:"d9824bdc-8445-4327-be8b-5b47500af6ce"})
```

```
{"object":"<string>","id":"3c90c3cc-0d44-4b50-8888-8dd25736052a","properties": {}}
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
- Data sourcesPOSTCreate a data sourceGETRetrieve a data sourceGETList data source templatesUpdate a data sourceQuery a data source
- Databases (deprecated)
- Comments
- Views
- File Uploads
- Search
- Users
- POSTCreate a data source
- GETRetrieve a data source
- GETList data source templates
- Update a data source
- Query a data source
- Data sources
- File uploads
- How to share a database with your integration
- Working with databases guide
- Option 1
- Option 2