# get-self

*Source: https://developers.notion.com/reference/get-self*

---

##### Notion API

##### Objects

##### Endpoints

##### Webhook events

### ​Errors

#### Authorizations

#### Headers

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
import{Client}from"@notionhq/client"constnotion=newClient({auth:process.env.NOTION_API_KEY})constresponse=awaitnotion.users.me()
```

```
{"id":"3c90c3cc-0d44-4b50-8888-8dd25736052a","object":"<string>","name":"<string>","avatar_url":"<string>","type":"<string>","person": {"email":"<string>"}}
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