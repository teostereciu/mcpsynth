# file-upload

*Source: https://developers.notion.com/reference/file-upload*

---

##### Notion API

##### Objects

##### Endpoints

##### Webhook events

## ​Object properties
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
- Object properties

[TABLE]
Field | Type | Description
object | "file_upload" | 
id | UUID | ID of the FileUpload.
created_time | String | ISO 8601 timestamp when the FileUpload was created.
last_edited_time | String | ISO 8601 timestamp when the FileUpload was last modified.
expiry_time | String | Nullable. ISO 8601 timestamp when the FileUpload will expire, if the API integration that created it doesn’t complete the upload and attach to at least one block or other object in a workspace.
status | One of:-"pending"-"uploaded"-"expired"-"failed" | Enum status of the file upload.pendingstatus means awaiting upload or completion of an upload.uploadedstatus means file contents have been sent.If theexpiry_timeisnull, that means the file upload has already been attached to a block or other object.expiredandfailedfile uploads can no longer be used.failedis only used for FileUploads withmode=external_urlwhen the import was unsuccessful.
filename | String | Nullable. Name of the file, provided during theCreate a file uploadstep, or, forsingle_partuploads, can be determined from the provided filename in the form data passed to theSend a file uploadstep.A file extension is automatically added based on thecontent_typeif the filename doesn’t already have one.
content_type | String | Nullable. The MIME content type of the uploaded file. Must be provided explicitly or inferred from afilenamethat includes an extension.Forsingle_partuploads, the content type can remainnulluntil theSend a file uploadstep and inferred from thefileparameter’s content type.
content_length | Integer | Nullable. The total size of the file, in bytes. For pendingmulti_partuploads, this field is a running total based on the file segments uploaded so far and recalculated at the end during theComplete a file uploadstep.
upload_url | String | Field only included forpendingfile uploads. This is the URL to use forsending file contents.
complete_url | String | Field only included forpendingfile uploads created with amodeofmulti_part. This is the URL to use tocomplete a multi-part file upload.
file_import_result | String | Field only included for afailedoruploadedfile upload created with amodeofexternal_url. Provides details on the success or failure of importing a file into Notion using an external URL.
[/TABLE]