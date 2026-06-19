# update-a-view

*Source: https://developers.notion.com/reference/update-a-view*

---

##### Notion API

##### Objects

##### Endpoints

##### Webhook events

### ​Errors

#### Authorizations

#### Headers

#### Path Parameters

#### Body

#### Response
Bearer authentication header of the formBearer <token>, where<token>is your auth token.
TheAPI versionto use for this request. The latest version is2026-03-11.
ID of a Notion view.
New name for the view.
Filter to apply to the view. Uses the same format as the data source query filter. Pass null to clear the filter.
Property sorts to apply to the view. Only property-based sorts are supported. Pass null to clear the sorts.
Showchild attributes
Quick filters for the view's filter bar. Keys are property names or IDs. Set a key to a filter condition to add/update that quick filter. Set a key to null to remove it. Pass null for the entire field to clear all quick filters. Unmentioned quick filters are preserved.
View presentation configuration. The type field must match the view type. Individual nullable fields within the configuration can be set to null to clear them.
The object type name.
The ID of the view.
The parent database of the view.
The view type.

```
import{Client}from"@notionhq/client"constnotion=newClient({auth:process.env.NOTION_API_KEY})constresponse=awaitnotion.views.update({view_id:"a3f1b2c4-5678-4def-abcd-1234567890ab",name:"Updated view name"})
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
- Option 1
- Option 2
- Option 3
- Option 4
- Option 5
- Option 6
- Option 7
- Option 8
- Option 9