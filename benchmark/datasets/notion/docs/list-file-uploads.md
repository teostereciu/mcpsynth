# list-file-uploads

*Source: https://developers.notion.com/reference/list-file-uploads*

---

##### Notion API

##### Objects

##### Endpoints

##### Webhook events

#### Authorizations

#### Headers

#### Query Parameters

#### Response
Bearer authentication header of the formBearer <token>, where<token>is your auth token.
TheAPI versionto use for this request. The latest version is2026-03-11.
If supplied, the endpoint will return file uploads with the specified status.
If supplied, this endpoint will return a page of results starting after the cursor provided. If not supplied, this endpoint will return the first page of results.
The number of items from the full list desired in the response. Maximum: 100
Showchild attributes
Alwaysfile_upload

```
import { Client } from "@notionhq/client"

const notion = new Client({ auth: process.env.NOTION_API_KEY })

const response = await notion.fileUploads.list({
  start_cursor: undefined,
  page_size: 50
})
```

```
{
  "object": "<string>",
  "next_cursor": "3c90c3cc-0d44-4b50-8888-8dd25736052a",
  "has_more": true,
  "results": [
    {
      "object": "<string>",
      "id": "3c90c3cc-0d44-4b50-8888-8dd25736052a",
      "created_time": "2023-11-07T05:31:56Z",
      "created_by": {
        "id": "3c90c3cc-0d44-4b50-8888-8dd25736052a",
        "type": "person"
      },
      "last_edited_time": "2023-11-07T05:31:56Z",
      "in_trash": true,
      "expiry_time": "2023-11-07T05:31:56Z",
      "status": "pending",
      "filename": "<string>",
      "content_type": "<string>",
      "content_length": 1,
      "upload_url": "<string>",
      "complete_url": "<string>",
      "file_import_result": {
        "imported_time": "2023-11-07T05:31:56Z",
        "type": "<string>",
        "success": {}
      },
      "number_of_parts": {
        "total": 1,
        "sent": 1
      }
    }
  ],
  "type": "<string>",
  "file_upload": {}
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
- File UploadsPOSTCreate a file uploadPOSTSend a file uploadPOSTComplete a file uploadGETRetrieve a file uploadGETList file uploads
- Search
- Users
- POSTCreate a file upload
- POSTSend a file upload
- POSTComplete a file upload
- GETRetrieve a file upload
- GETList file uploads
- File uploads