# introspect-token

*Source: https://developers.notion.com/reference/introspect-token*

---

##### Notion API

##### Objects

##### Endpoints

##### Webhook events

#### Authorizations

#### Headers

#### Body

#### Response
Basic authentication header of the formBasic <encoded-value>, where<encoded-value>is the base64-encoded stringusername:password.
TheAPI versionto use for this request. The latest version is2026-03-11.

```
import{Client}from"@notionhq/client"constnotion=newClient()constresponse=awaitnotion.oauth.introspect({client_id:process.env.OAUTH_CLIENT_ID,client_secret:process.env.OAUTH_CLIENT_SECRET,token:"access_token_to_introspect"})
```

```
{"active":true,"scope":"<string>","iat":123,"request_id":"3c90c3cc-0d44-4b50-8888-8dd25736052a"}
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
- AuthenticationOverviewPOSTCreate a tokenPOSTIntrospect a tokenPOSTRevoke a tokenPOSTRefresh a token
- Blocks
- Pages
- Databases
- Data sources
- Databases (deprecated)
- Comments
- Views
- File Uploads
- Search
- Users
- Overview
- POSTCreate a token
- POSTIntrospect a token
- POSTRevoke a token
- POSTRefresh a token
- File uploads