# versioning

*Source: https://developers.notion.com/reference/versioning*

---

##### Notion API

##### Objects

##### Endpoints

##### Webhook events

## ​Frequently asked questions
How do releases of the JavaScript SDK work?
Will staying on an older API version work indefinitely?

```
curlhttps://api.notion.com/v1/users/01da9b00-e400-4959-91ce-af55307647e5\-H"Authorization: Bearer secret_t1CdN9S8yicG5eWLUOfhcWaOscVnFXns"-H"Notion-Version: 2026-03-11"
```

```
// Prior to version 2021-05-13, the rich text property is called "text""properties": {"Description": {"type":"text","text": [/* ... */]}}// In version 2021-05-13, the rich text property is now called "rich_text""properties": {"Description": {"type":"rich_text","rich_text": [/* ... */]}}
```
- Status
- Community
- Blog
- Introduction
- Integration capabilities
- Webhooks
- Request limits
- Status codes
- VersioningOverviewChanges by version
- Overview
- Changes by version
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
- Users
- File uploads
- Frequently asked questions