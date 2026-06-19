# Files API

*Source: https://developers.hubspot.com/docs/api/files/files*

---

Files

# Files API

Learn how to upload and manage files in your HubSpot account using the files API.

Scope requirements

Use HubSpot’s files tool to store files in HubSpot for both internal and external use. For example, you can use the files tools to:

  * Insert uploaded images into content such as emails, blog posts, and website pages.
  * Attach files to records using the notes APIs.
  * Store branding assets, such as logos, icons, and banners.

You can access the files tool from [within HubSpot](https://knowledge.hubspot.com/files/upload-files-to-use-in-your-hubspot-content) or via the files API. Learn more about supported file types and sizes, including compatibility with other HubSpot tools, in HubSpot’s [Knowledge Base](https://knowledge.hubspot.com/files/supported-file-types).

##

​

Upload a file

Files can be uploaded using a multipart/form-data `POST` request to `files/v3/files` with the following fields. While a specific folder ID is not required at upload, it’s recommended to upload files into a folder and not the root directory. Folder requirements at upload are subject to change in the future.

Field| Description
---|---
`file` | The file to upload. Uploaded files are subject to the limits and supported formats outlined in [this Knowledge Base article](https://knowledge.hubspot.com/files/supported-file-types).
`options`| A JSON object that controls the file’s privacy and whether it can be indexed by search engines. This field contains two sub-properties: `access`, which is required, and `ttl`, which specifies a time period after which the file will be automatically deleted. If you’re using the `ttl` field:

  * The minimum period that must be set is 1 day.
  * The maximum period that can be set is 1 year.
  * After the set period, the file will be permanently deleted. After deletion, the file cannot be recovered or restored.


`folderId`| The ID of the folder that the file will be uploaded to. Either this field _or_ `folderPath` must be provided in your request (but _not_ both).
`folderPath`| The path of the folder that the file will be uploaded to. Either this field _or_ `folderId` must be provided in your request (but _not_ both).
`fileName`| The name of the file. If no name is specified, a name will be generated from the file’s content.
`charsetHunch`| Character set encoding for the uploaded file. If not provided, it will be derived from the file.

As an example, if you wanted to upload a file with the following criteria to your HubSpot account:

  * **File name:** `cat.png`
  * **Destination folder in the HubSpot file manager:** `/library/cat_archive`
  * **File accessibility in HubSpot:** privately accessible

The following headers and request body would need to be part of your request:


    curl --request POST \
      --url 'https://api.hubapi.com/files/v3/files?=' \
      --header 'Authorization: Bearer pat-na1-00000000-0000-0000-0000-000000000000' \
      --header 'Content-type: multipart/form-data' \
      --form file=@/Users/person/Downloads/cat.png \
      --form 'options={"access": "PRIVATE"}' \
      --form folderPath=/library/cat_archive


A successful `201` response will include the `id` and `parentFolderId` of the uploaded file, which you can use to retrieve the file via a `GET` request.


    {
      "id": "122692044085",
      "createdAt": "2023-06-28T17:56:45.393Z",
      "updatedAt": "2023-06-28T17:56:45.393Z",
      "archived": false,
      "parentFolderId": "122692510820",
      "name": "cat",
      "path": "/library/cat_archive/cat.png",
      "size": 24574,
      "height": 219,
      "width": 225,
      "encoding": "png",
      "type": "IMG",
      "extension": "png",
      "defaultHostingUrl": "https://12345.fs1.hubspotusercontent-na1.net/hubfs/12345/library/cat_archive/cat.png",
      "url": "https://12345.fs1.hubspotusercontent-na1.net/hubfs/12345/library/cat_archive/cat.png",
      "isUsableInContent": true,
      "access": "PRIVATE"
    }


##

​

Check a file’s upload status

If you’re importing a file from a URL to your file manager using a `POST` request to `files/v3/files/import-from-url/async`, you can review the upload status of the file. To do so, use a `GET` request to `files/v3/files/import-from-url/async/tasks/{taskId}/status`. After making this request, you’ll receive one of the following replies:

  * `PENDING`: the file is in the queue to be uploaded. The import process has not yet started.
  * `PROCESSING`: the file is in the process of being uploaded.
  * `CANCELED`: the upload has been canceled and the file will not be uploaded. To import the file to your HubSpot account, you’ll need to upload the file again.
  * `COMPLETE`: the file has been uploaded to the files tool successfully. The uploaded file will appear in your files tool.


##

​

View a file’s details

To review the details of a file that’s been uploaded to the files tool, make a `GET` request to `files/v3/files/{fileId}`. This will return the file with details such as name, height and width, encoding, the URL, and more. If a file is set to private, the returned URL will result in a 404 error. To get a viewable URL of the file, you can make a `GET` request to `/files/v3/files/{fileId}/signed-url`. When making this request, you can include `property` parameters to return specific properties such as height and width.

#

​

Update a file

To replace an existing file with new file data, make a `PUT` request to `/files/v3/files/{fileId}`. For example, you can use this endpoint to change image content rather than having to upload a new file and update that file’s references in your content. To update file properties on an existing file, make a `PATCH` request to `/files/v3/files/{fileId}`. You can update properties such as the file name. However, you cannot update the create date of a file. By default, `createdAt` will always reflect the date that the file was originally created in HubSpot.

##

​

Delete a file

To delete a file, make a `DELETE` request to `/files/v3/files/{fileId}`. This will mark the file as deleted and make the content of the file inaccessible. To permanently delete a file using a GDPR-compliant delete, make a `DELETE` request to `/files/v3/files/{fileId}/gdpr-delete`. This will permanently delete the file’s content and metadata within 7 days. If a file is not GDPR deleted, its contents will remain on HubSpot’s servers in a private state where no one can access it. To ensure file contents are fully deleted, use the GDPR delete functionality.

##

​

Create a folder

To create a folder, make a `POST` request to `files/v3/folders`. When making the request, you can include the fields provided in the table below.

Field| Type| Description
---|---|---
`name` | String| Name of the folder you want to create.
`parentFolderId`| String| To create the folder within an existing folder, include this field with the existing folder’s ID. `parentFolderId` and `parentFolderPath` cannot be set at the same time.
`parentFolderPath`| String| To create the folder within an existing folder, include this field with the existing folder’s path. `parentFolderId` and `parentFolderPath` cannot be set at the same time.

For example, a `POST` request to `/files/v3/folders` with the following request body would create a new folder called “myNewFolder” in the parent folder with an ID of `12345`.


    {
      "name": "myNewFolder",
      "parentFolderId": 12345
    }


##

​

Attach a file to a record

When you [add a file to a record in HubSpot](https://knowledge.hubspot.com/records/add-and-remove-attachments-from-records), it creates a note with the file attached and adds it to the record timeline. To add a file to a record via API, you can [create a note](/docs/api-reference/legacy/crm/activities/notes/guide) associated with a record and attach the file to the note.

  1. Upload the file to the file manager. Copy the `id` value from the response as it’ll be used to attach the file to the note.
  2. Retrieve the `associationTypeId` for the object and notes. You’ll use this ID to associate the record when creating the note. For default objects, you can refer to [this list of type IDs for note associations](/docs/api-reference/legacy/crm/associations/associate-records/guide#note-to-object). For objects not listed, you can make a `GET` request to `/crm/v4/associations/notes/{toObjectType}/labels` and copy the `typeId` from the response.
  3. Retrieve the record ID (`hs_object_id`) of the record to which you want to attach the file. Use the [objects API](/docs/guides/crm/using-object-apis#retrieve-records) to retrieve records.
  4. Create a note, associate it with a record, and attach the file. Make a `POST` request to `/crm/v3/objects/notes`. In the request body, include an `associations` object with the `id` of the record to associate with the note, and a `properties` object with the `id` of the file to attach.

For example, to attach a file to a note on a contact record, you’d make a `POST` request to `/crm/v3/objects/notes` with the following request body:


    {
      "associations": [
        {
          "to": {
            "id": "{hs_object_id}"
          },
          "types": [
            {
              "associationCategory": "HUBSPOT_DEFINED",
              "associationTypeId": 202
            }
          ]
        }
      ],
      "properties": {
        "hs_note_body": "Example note",
        "hs_timestamp": "2021-11-12T15:48:22Z",
        "hs_attachment_ids": "{fileId}"
      }
    }


##

​

Changes in v3

If you’ve been using the previous version of this API, v3 has the following changes:

  * All files uploaded through the API will be visible in the files dashboard and the files picker. Hidden files cannot be created. However, private files and non-indexable files can still be created.
  * Listing files will not return hidden or deleted files. However, a much broader range of filters can be applied. Hidden files can still be fetched by ID, but require a new scope: `files_ui_hidden.read`.
  * Multiple files cannot be uploaded with a single request.
  * Folder update actions like moving and renaming are now asynchronous. Each request will return a token that can be used to check the status of the folder edit.
  * Endpoints that create or replace files require you to provide access levels for the files. These access levels are:
    * `PUBLIC_INDEXABLE`**:** file is publicly accessible by anyone who has the URL. Search engines can index the file.
    * `PUBLIC_NOT_INDEXABLE`**:** file is publicly accessible by anyone who has the URL. The X-Robots-Tag: noindex header will be sent whenever the file is retrieved, instructing search engines not to index the file.
    * **`PRIVATE`:** file is not publicly accessible. Requires a signed URL to display content. Search engines cannot index the file.
  * Endpoints that create files allow for a level of duplicate detections as part of the file’s upload options.
    * `ENTIRE_PORTAL`**:** search for a duplicate file in the account.
    * `EXACT_FOLDER`**:** search for a duplicate file in the provided folder.
    * `NONE`**:** do not run any duplicate validation.
    * `REJECT`**:** reject the upload if a duplicate is found.
    * `RETURN_EXISTING`**:** if a duplicate file is found, do not upload a new file and return the found duplicate instead.
    * Duplicate detection works on a `duplicateValidationScope`, which affects how we search for a duplicate.
    * This also requires a `duplicateValidationStrategy`, which dictates what happens if a duplicate is found.


Last modified on March 30, 2026

Was this page helpful?

YesNo

⌘I

[facebook](https://www.facebook.com/hubspot)[instagram](https://www.instagram.com/hubspot)[youtube](https://youtube.com/user/HubSpot)[x](https://x.com/HubSpot)[linkedin](https://www.linkedin.com/company/hubspot)[medium](https://medium.com/@HubSpot)