# create-a-data-source

*Source: https://developers.notion.com/reference/create-a-data-source*

---

##### Notion API

##### Objects

##### Endpoints

##### Webhook events

#### Authorizations

#### Headers

#### Body

#### Response
Bearer authentication header of the formBearer <token>, where<token>is your auth token.
TheAPI versionto use for this request. The latest version is2026-03-11.
An object specifying the parent of the new data source to be created.
Showchild attributes
Property schema of data source.
Title of data source as it appears in Notion.
The data source object type name.
The ID of the data source.
The properties schema of the data source.

```
import{Client}from"@notionhq/client"constnotion=newClient({auth:process.env.NOTION_API_KEY})constresponse=awaitnotion.dataSources.create({parent:{database_id:"a1b2c3d4-e5f6-7890-abcd-ef1234567890"},title:[{text:{content:"My Data Source"} }],properties:{Name:{title:{} },Status:{select:{options:[{name:"To Do",color:"red"},{name:"Done",color:"green"}]}}}})
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
- Text
- Mention
- Equation
- File Upload
- External
- Custom Emoji
- Option 1
- Option 2