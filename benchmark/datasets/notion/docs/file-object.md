# file-object

*Source: https://developers.notion.com/reference/file-object*

---

##### Notion API

##### Objects

##### Endpoints

##### Webhook events

## ​What is a file object?

### ​Notion-hosted files (type:file)

### ​Files uploaded in the API (type:file_upload)

## ​External files (type:external)

```
// Notion-hosted file (uploaded via UI){"type": "file","file": {"url": "<https://s3.us-west-2.amazonaws.com/...">,"expiry_time": "2025-04-24T22:49:22.765Z"}}// File uploaded via the Notion API{"type": "file_upload","file_upload": {"id": "43833259-72ae-404e-8441-b6577f3159b4"}}// External file{"type": "external","external": {"url": "<https://example.com/image.png">}}
```

```
{"type": "file","file": {"url": "<https://s3.us-west-2.amazonaws.com/...">,"expiry_time": "2025-04-24T22:49:22.765Z"}}
```

```
{"type": "file_upload","file_upload": {"id": "43833259-72ae-404e-8441-b6577f3159b4"}}
```

```
{"type": "external","external": {"url": "<https://example.com/photo.png">}}
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
- FileOverviewFile Upload
- User
- Parent
- Emoji
- Unfurl attribute (Link Previews)
- Overview
- File Upload
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
- What is a file object?
- Notion-hosted files (type: file)
- Files uploaded in the API (type: file_upload)
- External files (type: external)
- Files uploaded manually in the Notion UI — returned as Notion-hosted file objects (type:file)
- Files uploaded via API — created using the File Upload API (type:file_upload)
- External files — linked via a public URL (type:external)
- You’re working with existing content in a Notion workspace
- You’re accessing files that users manually added via drag-and-drop or upload
- Each time you fetch a Notion-hosted file, it includes a temporary public url valid for 1 hour.
- Don’t cache or statically reference these URLs. To refresh access, re-fetch the file object.
- Once uploaded, you can reuse the File Upload ID to attach the same file to multiple pages or blocks
- To learn more about file uploads, view theWorking with files and mediaguide
- You have an existing CDN or media server
- You have stable, permanent URLs
- Your files are publicly accessible and don’t require authentication
- You don’t want to upload files into Notion
- Pass an HTTPS URL when creating or updating file-supporting blocks or properties.
- These links never expire and will always be returned as-is in API responses.
1. You want to programmatically upload files to Notion
2. You’re building automations or file-rich integrations

[TABLE]
Field | Type | Description
type | string(enum) | The type of the file object. Possible type values are:"file","file_upload","external".
file|file_upload|external | object | An object containing type-specific configuration. Refer to the type sections below for details on type-specific values.
[/TABLE]

[TABLE]
Field | Type | Description | Example value
url | string | An authenticated HTTP GET URL to the file.The URL is valid for one hour. If the link expires, send an API request to get an updated URL. | "https://s3.us-west-2.amazonaws.com/secure.notion-static.com/9bc6c6e0-32b8-4d55-8c12-3ae931f43a01/brocolli.jpeg?..."
expiry_time | string(ISO 8601date time) | The date and time when the link expires. | "2020-03-17T19:10:04.968Z"
[/TABLE]

[TABLE]
Field | Type | Description | Example Value
id | UUID | ID of aFile Uploadobject that has astatusof"uploaded" | "43833259-72ae-404e-8441-b6577f3159b4"
[/TABLE]

[TABLE]
Field | Type | Description | Example value
url | string | A link to the externally hosted content. | "https://website.domain/files/doc.txt"
[/TABLE]