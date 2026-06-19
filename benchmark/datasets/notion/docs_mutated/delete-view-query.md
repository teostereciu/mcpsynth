# delete-view-query

*Source: https://developers.notion.com/reference/delete-view-query*

---

##### Notion API

##### Objects

##### Endpoints

##### Webhook events

### ​Errors

#### Authorizations

#### Headers

#### Path Parameters

#### Response
Bearer authentication header of the formBearer <token>, where<token>is your auth token.
TheAPI versionto use for this request. The latest version is2026-03-11.
The ID of the view.
The ID of the query.
The object type.
The ID of the deleted view query.
Whether the view query was deleted.

```
import{Client}from"@notionhq/client"constnotion=newClient({auth:process.env.NOTION_API_KEY})constresponse=awaitnotion.views.queries.delete({view_id:"a3f1b2c4-5678-4def-abcd-1234567890ab",query_id:"b4e2c3d5-6789-4abc-def0-1234567890cd"})
```

```
{"object":"<string>","id":"3c90c3cc-0d44-4b50-8888-8dd25736052a","deleted":true}
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
- ViewsPOSTCreate a viewGETRetrieve a viewPATCHUpdate a viewDELDelete a viewGETList viewsView queriesPOSTCreate a view queryGETGet view query resultsDELDelete a view query
- File Uploads
- Search
- Users
- POSTCreate a view
- GETRetrieve a view
- PATCHUpdate a view
- DELDelete a view
- GETList views
- View queriesPOSTCreate a view queryGETGet view query resultsDELDelete a view query
- POSTCreate a view query
- GETGet view query results
- DELDelete a view query
- File uploads
- Views