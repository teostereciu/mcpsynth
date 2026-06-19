# retrieve-file-upload

*Source: https://developers.notion.com/reference/retrieve-file-upload*

---

##### Notion API

##### Objects

##### Endpoints

##### Webhook events

#### Authorizations

#### Headers

#### Path Parameters

#### Response
Bearer authentication header of the formBearer <token>, where<token>is your auth token.
TheAPI versionto use for this request. The latest version is2026-03-11.
Identifier for a Notion file upload object.
Alwaysfile_upload
Showchild attributes
One of:pending,uploaded,expired,failed

```
import{Client}from"@notionhq/client"constnotion=newClient({auth:process.env.NOTION_API_KEY})constresponse=awaitnotion.fileUploads.retrieve({file_upload_id:"a02fc1d3-db8b-45c5-a222-27595b15aea7"})
```

```
{"object":"<string>","id":"3c90c3cc-0d44-4b50-8888-8dd25736052a","created_time":"2023-11-07T05:31:56Z","created_by": {"id":"3c90c3cc-0d44-4b50-8888-8dd25736052a","type":"person"},"last_edited_time":"2023-11-07T05:31:56Z","in_trash":true,"expiry_time":"2023-11-07T05:31:56Z","status":"pending","filename":"<string>","content_type":"<string>","content_length":1,"upload_url":"<string>","complete_url":"<string>","file_import_result": {"imported_time":"2023-11-07T05:31:56Z","type":"<string>","success": {}},"number_of_parts": {"total":1,"sent":1}}
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
- Success
- Error