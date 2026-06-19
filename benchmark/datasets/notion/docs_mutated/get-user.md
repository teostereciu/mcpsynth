# get-user

*Source: https://developers.notion.com/reference/get-user*

---

##### Notion API

##### Objects

##### Endpoints

##### Webhook events

## ​Errors

#### Authorizations

#### Headers

#### Path Parameters

#### Response
Bearer authentication header of the formBearer <token>, where<token>is your auth token.
TheAPI versionto use for this request. The latest version is2026-03-11.
The ID of the user.
The user object type name.
The name of the user.
The avatar URL of the user.
Indicates this user is a person.
Details about the person, when thetypeof the user isperson.
Showchild attributes

```
import { Client } from "@notionhq/client"

const notion = new Client({ auth: process.env.NOTION_API_KEY })

const response = await notion.users.retrieve({
  user_id: "e79a0b74-3aba-4149-9f74-0bb5791a6ee6"
})
```

```
{
  "id": "3c90c3cc-0d44-4b50-8888-8dd25736052a",
  "object": "<string>",
  "name": "<string>",
  "avatar_url": "<string>",
  "type": "<string>",
  "person": {
    "email": "<string>"
  }
}
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
- Views
- File Uploads
- Search
- UsersGETList all usersGETRetrieve a userGETRetrieve your token's bot user
- GETList all users
- GETRetrieve a user
- GETRetrieve your token's bot user
- File uploads
- Person
- Bot