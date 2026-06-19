# create-a-token

*Source: https://developers.notion.com/reference/create-a-token*

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
Showchild attributes

```
import{Client}from"@notionhq/client"constnotion=newClient()constresponse=awaitnotion.oauth.token({client_id:process.env.OAUTH_CLIENT_ID,client_secret:process.env.OAUTH_CLIENT_SECRET,grant_type:"authorization_code",code:"abc123-authorization-code",redirect_uri:"https://example.com/callback"})
```

```
{"access_token":"<string>","token_type":"<string>","refresh_token":"<string>","bot_id":"3c90c3cc-0d44-4b50-8888-8dd25736052a","workspace_icon":"<string>","workspace_name":"<string>","workspace_id":"3c90c3cc-0d44-4b50-8888-8dd25736052a","owner": {"type":"<string>","user": {"type":"<string>","person": {"email":"<string>"},"name":"<string>","avatar_url":"<string>","id":"<string>","object":"<string>"}},"duplicated_template_id":"3c90c3cc-0d44-4b50-8888-8dd25736052a","request_id":"3c90c3cc-0d44-4b50-8888-8dd25736052a"}
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
- theredirect_uriquery parameter was set in theAuthorization URLprovided to users,or;
- there are more than oneredirect_uris included in theintegration’s settingsunderOAuth Domain & URIs.
- there is oneredirect_uriincluded in theintegration’s settingsunderOAuth Domain & URIs,andtheredirect_uriquery parameter was not included in the Authorization URL.
- Option 1
- Option 2
- Workspace