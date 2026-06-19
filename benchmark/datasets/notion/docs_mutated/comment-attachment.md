# comment-attachment

*Source: https://developers.notion.com/reference/comment-attachment*

---

##### Notion API

##### Objects

##### Endpoints

##### Webhook events

## ​Request format (input)

### ​Object properties

## ​Response format (output)

```
{"parent": {"page_id":"d0a1ffaf-a4d8-4acf-a1ed-abae6e110418"},"rich_text": [{"text": {"content":"Thanks for the helpful page!"}},],"attachments": {"file_upload_id":"2e2cdb8b-9897-4a6c-a935-82922b1cfb87"}}
```

```
{"category":"video","file": {"url":"https://s3.us-west-2.amazonaws.com/...","expiry_time":"2025-06-10T21:26:03.070Z"}}
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
- CommentOverviewComment attachmentComment display name
- File
- User
- Parent
- Emoji
- Unfurl attribute (Link Previews)
- Overview
- Comment attachment
- Comment display name
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
- Request format (input)
- Object properties
- Response format (output)

[TABLE]
Parameter | Type | Description | Example value
file_upload_id | string(UUID) | ID of aFile Uploadwith a status of"uploaded" | "2e2cdb8b-9897-4a6c-a935-82922b1cfb87"
type | string(optional) | Possible type values are:"file_upload" | "file_upload"
[/TABLE]

[TABLE]
Field | Type | Description | Example value
category | string(enum) | The category of this attachment. Possible type values are:"audio","image","pdf","productivity", and"video" | "audio"
file | object | Afile objectcontaining type-specific configuration. | {"url": "<https://s3.us-west-2.amazonaws.com/...">, "expiry_time": "2025-06-10T21:26:03.070Z"}
[/TABLE]