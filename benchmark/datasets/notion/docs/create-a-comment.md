# create-a-comment

*Source: https://developers.notion.com/reference/create-a-comment*

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
An array of rich text objects that represent the content of the comment.
Showchild attributes
The parent of the comment. This can be a page or a block.
An array of files to attach to the comment. Maximum of 3 allowed.
Display name for the comment.
The comment object type name.
The ID of the comment.

```
import{Client}from"@notionhq/client"constnotion=newClient({auth:process.env.NOTION_API_KEY})constresponse=awaitnotion.comments.create({parent:{page_id:"b55c9c91-384d-452b-81db-d1ef79372b75"},rich_text:[{text:{content:"This is a comment"} }]})
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
- Option 1
- Option 2
- Text
- Mention
- Equation
- Integration
- Custom
1. A page
2. A block
3. An existing discussion thread