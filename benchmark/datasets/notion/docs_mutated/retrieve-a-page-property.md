# retrieve-a-page-property

*Source: https://developers.notion.com/reference/retrieve-a-page-property*

---

##### Notion API

##### Objects

##### Endpoints

##### Webhook events

## ​Property Item Objects

### ​Simple Properties

### ​Paginated Properties

### ​Rollup Properties

### ​Errors

#### Authorizations

#### Headers

#### Path Parameters

#### Query Parameters

#### Response
Bearer authentication header of the formBearer <token>, where<token>is your auth token.
TheAPI versionto use for this request. The latest version is2026-03-11.

```
import{Client}from"@notionhq/client"constnotion=newClient({auth:process.env.NOTION_API_KEY})constresponse=awaitnotion.pages.properties.retrieve({page_id:"b55c9c91-384d-452b-81db-d1ef79372b75",property_id:"aBcD"})
```

```
{"type":"<string>","number":123,"object":"<string>","id":"<string>"}
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
- PagesPOSTCreate a pageGETRetrieve a pageGETRetrieve a page property itemPOSTMove a pageUpdate pageMarkdown content
- Databases
- Data sources
- Databases (deprecated)
- Comments
- Views
- File Uploads
- Search
- Users
- POSTCreate a page
- GETRetrieve a page
- GETRetrieve a page property item
- POSTMove a page
- Update page
- Markdown content
- Pages
- File uploads
- title
- rich_text
- relation
- people
- show_unique(Show unique values)
- unique(Count unique values)
- median(Median)
- Number
- Url
- Select
- Multi Select
- Date
- Email
- Phone Number
- Checkbox
- Files
- Created By
- Created Time
- Last Edited By
- Last Edited Time
- Formula
- Button
- Unique Id
- Verification
- Place
- Title
- Rich Text
- People
- Relation
- Rollup
- Property Item