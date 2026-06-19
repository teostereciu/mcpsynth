# create-file

*Source: https://developers.notion.com/reference/create-file*

---

##### Notion API

##### Objects

##### Endpoints

##### Webhook events

#### Authorizations

#### Headers

#### Body

#### Response
Bearer authentication header of the formBearer <token>, where<token>is your auth token.
TheAPI versionto use for this request. The latest version is2026-03-11.
How the file is being sent. Usemulti_partfor files larger than 20MB. Useexternal_urlfor files that are temporarily hosted publicly elsewhere. Default issingle_part.
Name of the file to be created. Required whenmodeismulti_part. Otherwise optional, and used to override the filename. Must include an extension, or have one inferred from thecontent_typeparameter.
"business_summary.pdf"
MIME type of the file to be created. Recommended when sending the file in multiple parts. Must match the content type of the file that's sent, and the extension of thefilenameparameter if any.
"application/pdf"
Whenmodeismulti_part, the number of parts you are uploading. This must match the number of parts as well as the finalpart_numberyou send.
Whenmodeisexternal_url, provide the HTTPS URL of a publicly accessible file to import into your workspace.
Alwaysfile_upload
Showchild attributes
One of:pending,uploaded,expired,failed

```
import{Client}from"@notionhq/client"constnotion=newClient({auth:process.env.NOTION_API_KEY})constresponse=awaitnotion.fileUploads.create({mode:"single_part",filename:"document.pdf",content_type:"application/pdf"})
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