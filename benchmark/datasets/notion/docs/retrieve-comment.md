# retrieve-comment

*Source: https://developers.notion.com/reference/retrieve-comment*

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
The ID of the comment to retrieve.
The comment object type name.
The ID of the comment.

```
import{Client}from"@notionhq/client"constnotion=newClient({auth:process.env.NOTION_API_KEY})constresponse=awaitnotion.comments.retrieve({comment_id:"c02fc1d3-db8b-45c5-a222-27595b15aea7"})
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