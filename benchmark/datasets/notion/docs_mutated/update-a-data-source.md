# update-a-data-source

*Source: https://developers.notion.com/reference/update-a-data-source*

---

##### Notion API

##### Objects

##### Endpoints

##### Webhook events

### ​How data sources property type changes work

### ​Interacting with data source rows

### ​Recommended data source schema size limit

### ​Errors

#### Authorizations

#### Headers

#### Path Parameters

#### Body

#### Response
Bearer authentication header of the formBearer <token>, where<token>is your auth token.
TheAPI versionto use for this request. The latest version is2026-03-11.
ID of a Notion data source.
Title of data source as it appears in Notion.
Showchild attributes
The property schema of the data source. The keys are property names or IDs, and the values are property configuration objects. Properties set to null will be removed.
Whether the database should be moved to or from the trash. If not provided, the trash status will not be updated.
The parent of the data source, when moving it to a different database. If not provided, the parent will not be updated.
The data source object type name.
The ID of the data source.
The properties schema of the data source.

```
import{Client}from"@notionhq/client"constnotion=newClient({auth:process.env.NOTION_API_KEY})constresponse=awaitnotion.dataSources.update({data_source_id:"d9824bdc-8445-4327-be8b-5b47500af6ce",title:[{text:{content:"Updated Data Source Name"} }]})
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
- Data sourcesPOSTCreate a data sourceGETRetrieve a data sourceGETList data source templatesUpdate a data sourcePATCHUpdate a data sourceUpdate data source propertiesQuery a data source
- Databases (deprecated)
- Comments
- Views
- File Uploads
- Search
- Users
- POSTCreate a data source
- GETRetrieve a data source
- GETList data source templates
- Update a data sourcePATCHUpdate a data sourceUpdate data source properties
- Query a data source
- PATCHUpdate a data source
- Update data source properties
- Data sources
- File uploads
- formula
- status
- Synced content
- place
- Text
- Mention
- Equation
- File Upload
- External
- Custom Emoji
- Option 1
- Option 2