# sort-data-source-entries

*Source: https://developers.notion.com/reference/sort-data-source-entries*

---

##### Notion API

##### Objects

##### Endpoints

##### Webhook events

## ​Sort object

### ​Property value sort

### ​Entry timestamp sort

```
{"sorts": [{"property":"created_time","direction":"ascending"},]}
```

```
const{Client}=require('@notionhq/client');constnotion=newClient({auth:process.env.NOTION_API_KEY});// replace with your own data source IDconstdataSourceId='d9824bdc-8445-4327-be8b-5b47500af6ce';constsortedRows=async()=>{constresponse=awaitnotion.dataSources.query({database_id:databaseId,sorts:[{property:"Name",direction:"ascending"}],});returnresponse;}
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
- Data sourcesPOSTCreate a data sourceGETRetrieve a data sourceGETList data source templatesUpdate a data sourceQuery a data sourcePOSTQuery a data sourceFilter data source entriesSort data source entries
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
- Query a data sourcePOSTQuery a data sourceFilter data source entriesSort data source entries
- POSTQuery a data source
- Filter data source entries
- Sort data source entries
- Data sources
- File uploads
- Sort object
- Property value sort
- Entry timestamp sort

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