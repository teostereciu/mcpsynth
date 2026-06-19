# authentication

*Source: https://developers.notion.com/reference/authentication*

---

##### Notion API

##### Objects

##### Endpoints

##### Webhook events

```
curl 'https://api.notion.com/v1/users' \-H 'Authorization: Bearer '"$NOTION_ACCESS_TOKEN"'' \-H "Notion-Version: 2026-03-11"
```

```
const{Client}=require('@notionhq/client');constclient=newClient({auth:process.env.NOTION_ACCESS_TOKEN});
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