# list-data-source-templates

*Source: https://developers.notion.com/reference/list-data-source-templates*

---

##### Notion API

##### Objects

##### Endpoints

##### Webhook events

#### Authorizations

#### Headers

#### Path Parameters

#### Query Parameters

#### Response
Bearer authentication header of the formBearer <token>, where<token>is your auth token.
TheAPI versionto use for this request. The latest version is2026-03-11.
ID of a Notion data source.
Filter templates by name (case-insensitive substring match).
If supplied, this endpoint will return a page of results starting after the cursor provided. If not supplied, this endpoint will return the first page of results.
The number of items from the full list desired in the response. Maximum: 100
Array of templates available in this data source.
Showchild attributes
Whether there are more templates available beyond this page.
Cursor to use for the next page of results. Null if there are no more results.

```
import{Client}from"@notionhq/client"constnotion=newClient({auth:process.env.NOTION_API_KEY})constresponse=awaitnotion.dataSources.listTemplates({data_source_id:"d9824bdc-8445-4327-be8b-5b47500af6ce"})
```

```
{"templates": [{"id":"3c90c3cc-0d44-4b50-8888-8dd25736052a","name":"<string>","is_default":true}],"has_more":true,"next_cursor":"3c90c3cc-0d44-4b50-8888-8dd25736052a"}
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

[TABLE]
Key | Data Type | Meaning
id | String(UUIDv4 format) | The ID of the template.
name | String | The display name of the template.
is_default | Boolean | Whether that template is the data source’s default.
[/TABLE]