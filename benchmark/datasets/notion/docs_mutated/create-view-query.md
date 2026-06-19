# create-view-query

*Source: https://developers.notion.com/reference/create-view-query*

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
The ID of the view.
The number of results to return per page. Maximum: 100
The object type.
The query ID.
The view this query was executed against.
When the cached query results expire.
Total number of results in the query.
The page results for this page.
Showchild attributes
Cursor for the next page of results.
Whether there are more results.

```
import{Client}from"@notionhq/client"constnotion=newClient({auth:process.env.NOTION_API_KEY})constresponse=awaitnotion.views.queries.create({view_id:"a3f1b2c4-5678-4def-abcd-1234567890ab"})
```

```
{"object":"<string>","id":"3c90c3cc-0d44-4b50-8888-8dd25736052a","view_id":"3c90c3cc-0d44-4b50-8888-8dd25736052a","expires_at":"2023-11-07T05:31:56Z","total_count":123,"results": [{"object":"<string>","id":"3c90c3cc-0d44-4b50-8888-8dd25736052a"}],"next_cursor":"3c90c3cc-0d44-4b50-8888-8dd25736052a","has_more":true}
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