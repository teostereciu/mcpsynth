# retrieve-a-page

*Source: https://developers.notion.com/reference/retrieve-a-page*

---

##### Notion API

##### Objects

##### Endpoints

##### Webhook events

### ​Parent objects: Pages vs. databases

### ​Limits

### ​Errors

#### Authorizations

#### Headers

#### Path Parameters

#### Query Parameters

#### Response
Bearer authentication header of the formBearer <token>, where<token>is your auth token.
TheAPI versionto use for this request. The latest version is2026-03-11.
The ID of the page to retrieve.
Supply a list of property IDs to filter properties in the response. Note that if a page doesn't have a property, it won't be included in the filtered response.
The page object type name.
The ID of the page.

```
import{Client}from"@notionhq/client"constnotion=newClient({auth:process.env.NOTION_API_KEY})constresponse=awaitnotion.pages.retrieve({page_id:"b55c9c91-384d-452b-81db-d1ef79372b75"})
```

```
{"object":"<string>","id":"3c90c3cc-0d44-4b50-8888-8dd25736052a"}
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
- people: response object can’t be guaranteed to return more than 25 people.
- relation: thehas_morevalue of therelationin the response object istrueif arelationcontains more than 25 related pages. Otherwise,has_moreis false.
- rich_text: response object includes a maximum of 25 populated inline page or person mentions.
- title: response object includes a maximum of 25 inline page or person mentions.
- Option 1
- Option 2