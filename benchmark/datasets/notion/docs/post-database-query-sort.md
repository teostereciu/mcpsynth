# post-database-query-sort

*Source: https://developers.notion.com/reference/post-database-query-sort*

---

##### Notion API

##### Objects

##### Endpoints

##### Webhook events

## ​Sort object

### ​Property value sort

### ​Entry timestamp sort

```
{"sorts": [{"property":"Name","direction":"ascending"}]}
```

```
const{Client}=require('@notionhq/client');constnotion=newClient({auth:process.env.NOTION_API_KEY});// replace with your own database IDconstdatabaseId='d9824bdc-8445-4327-be8b-5b47500af6ce';constsortedRows=async()=>{constresponse=awaitnotion.databases.query({database_id:databaseId,sorts:[{property:"Name",direction:"ascending"}],});returnresponse;}
```

```
{"sorts": [{"property":"Food group","direction":"descending"},{"property":"Name","direction":"ascending"}]}
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
- Databases (deprecated)POSTCreate a databaseGETRetrieve a databaseGETGet databasesQuery a databasePOSTOverviewFilter database entriesSort database entriesUpdate a database
- Comments
- Views
- File Uploads
- Search
- Users
- POSTCreate a database
- GETRetrieve a database
- GETGet databases
- Query a databasePOSTOverviewFilter database entriesSort database entries
- Update a database
- POSTOverview
- Filter database entries
- Sort database entries
- File uploads
- Sort object
- Property value sort
- Entry timestamp sort
- Sort data source entries

[TABLE]
Property | Type | Description | Example value
property | string | The name of the property to sort against. | "Ingredients"
direction | string(enum) | The direction to sort. Possible values include"ascending"and"descending". | "descending"
[/TABLE]

[TABLE]
Property | Type | Description | Example value
timestamp | string(enum) | The name of the timestamp to sort against. Possible values include"created_time"and"last_edited_time". | "last_edited_time"
direction | string(enum) | The direction to sort. Possible values include"ascending"and"descending". | "descending"
[/TABLE]