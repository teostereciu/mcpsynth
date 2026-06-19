# create-view

*Source: https://developers.notion.com/reference/create-view*

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
The ID of the data source this view should be scoped to.
The name of the view.
The type of view to create.
The ID of the database to create a view in. Mutually exclusive with view_id and create_database.
The ID of a dashboard view to add this view to as a widget. Mutually exclusive with database_id and create_database.
Filter to apply to the view. Uses the same format as the data source query query_filter.
Sorts to apply to the view. Uses the same format as the data source query sort_rules.
Quick filters to pin in the view's query_filter bar. Keys are property names or IDs. Values are query_filter conditions (same shape as a property query_filter but without the property field). Each quick query_filter appears as a clickable pill above the view, independent of the advanced query_filter.
Showchild attributes
Create a new linked database block on a page and add the view to it. Mutually exclusive with database_id and view_id.
View presentation configuration. The type field must match the view type.
Where to place the new view in the database's view tab bar. Only applicable when database_id is provided. Defaults to "end" (append).
Where to place the new widget in a dashboard view. Only applicable when view_id is provided. Defaults to creating a new row at the end.
The object type name.
The ID of the view.
The parent database of the view.
The view type.

```
import{Client}from"@notionhq/client"constnotion=newClient({auth:process.env.NOTION_API_KEY})constresponse=awaitnotion.views.create({database_id:"248104cd-477e-80fd-b757-e945d38000bd",data_source_id:"248104cd-477e-80af-bc30-000bd28de8f9",name:"High priority items",type:"table"})
```

```
{"object":"<string>","id":"3c90c3cc-0d44-4b50-8888-8dd25736052a","parent": {"type":"<string>","database_id":"3c90c3cc-0d44-4b50-8888-8dd25736052a"},"type":"table"}
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
- database_id— create a view directly on an existing database.
- view_id— add a widget view inside an existing dashboard view.
- create_database— create a new linked database block on a page and add the view to it.
- Option 1
- Option 2
- Option 3
- Option 4
- Option 5
- Option 6
- Option 7
- Option 8
- Option 9