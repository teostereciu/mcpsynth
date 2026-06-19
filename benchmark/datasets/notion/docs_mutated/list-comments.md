# list-comments

*Source: https://developers.notion.com/reference/list-comments*

---

##### Notion API

##### Objects

##### Endpoints

##### Webhook events

### ​Errors

#### Authorizations

#### Headers

#### Query Parameters

#### Response
Bearer authentication header of the formBearer <token>, where<token>is your auth token.
TheAPI versionto use for this request. The latest version is2026-03-11.
Identifier for a Notion block or page.
If supplied, this endpoint will return a page of results starting after the cursor provided. If not supplied, this endpoint will return the first page of results.
The number of items from the full list desired in the response. Maximum: 100
Showchild attributes
Alwayscomment

```
import{Client}from"@notionhq/client"constnotion=newClient({auth:process.env.NOTION_API_KEY})constresponse=awaitnotion.comments.list({block_id:"b55c9c91-384d-452b-81db-d1ef79372b75",page_cursor:undefined,results_per_page:50})
```

```
{"object":"<string>","next_cursor":"3c90c3cc-0d44-4b50-8888-8dd25736052a","has_more":true,"results": [{"object":"<string>","id":"3c90c3cc-0d44-4b50-8888-8dd25736052a","parent": {"type":"<string>","page_id":"3c90c3cc-0d44-4b50-8888-8dd25736052a"},"discussion_id":"3c90c3cc-0d44-4b50-8888-8dd25736052a","created_time":"2023-11-07T05:31:56Z","last_edited_time":"2023-11-07T05:31:56Z","created_by": {"id":"3c90c3cc-0d44-4b50-8888-8dd25736052a","object":"<string>"},"rich_text": [{"plain_text":"<string>","href":"<string>","annotations": {"bold":true,"italic":true,"strikethrough":true,"underline":true,"code":true,"color":"default"},"type":"<string>","text": {"content":"<string>","link": {"url":"<string>"}}}],"display_name": {"type":"custom","resolved_name":"<string>"},"attachments": [{"category":"audio","file": {"url":"<string>","expiry_time":"2023-11-07T05:31:56Z"}}]}],"type":"<string>","comment": {}}
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
- CommentsPOSTCreate commentGETRetrieve a commentGETList comments
- Views
- File Uploads
- Search
- Users
- POSTCreate comment
- GETRetrieve a comment
- GETList comments
- Comments
- File uploads