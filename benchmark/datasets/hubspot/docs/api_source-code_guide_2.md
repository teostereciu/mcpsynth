# Source Code API

*Source: https://developers.hubspot.com/docs/api-reference/latest/cms/source-code/guide*

---

Source code

# Source Code API

Create, fetch, update, and delete, files in the HubSpot developer file system. Additionally you can validate files for different types of errors & warnings

Scope requirements

##

​

Basic Features

The CMS Source Code API allows you to interact with the files stored in your HubSpot [Developer File System](/docs/cms/start-building/introduction/overview#developer-file-system). These files include all of the templates, modules, CSS, JS, and other CMS assets seen in the Design Manager. Through this API, you can:

  * Upload new files to their HubSpot account, or upload changes to existing files.
  * Download or delete CMS assets from their account.
  * Fetch metadata for each file or folder in the Design Manager.
  * Validate file contents for use in HubSpot CMS, including HubL syntax.
  * Upload zip files as file packages and extract them inside the account.

With this API you can edit all your CMS assets locally as well as build tooling to help you move even faster.

##

​

Environment and path

The Source Code API endpoints use the `environment` and `path` parameters to identify files in the CMS Developer File System. These parameters are generally specified in the endpoint path itself, as in `/cms/source-code/2026-03/{environment}/content/{path}`. The `environment` parameter refers to whether you are interacting with the unpublished or live version of each file. For unpublished changes, use `draft`. For live changes, use `published`.

Note that uploading to `published` is equivalent to pressing the “Publish” button in the Design Manager. As such, whatever is currently in `draft` will be cleared.

The `path` parameter refers to the location of the file in the CMS Developer File System. Top level assets are not preceded by a `/` character as you would see in a UNIX based operating system. When uploading a new file, this should be the desired location where the file should be created. When retrieving or uploading changes to an existing file, this should match the path of the existing file. We use the local file formats for all asset types, which means that certain types of assets are broken up into multiple files. For instance, a module is actually represented as a directory ending in the `.module` suffix, so to retrieve the HTML for a module, one would need to use the path `foo.module/module.html`. See the [local development documentation](/docs/developer-tooling/local-development/hubspot-cli/reference) for further information.

##

​

Downloading a file

To download a file from your HubSpot account, make a `GET` request to `/cms/source-code/2026-03/{environment}/content/{path}` and set the header to `Accept: application/octet-stream`. File data will be downloaded in binary format. You cannot download the entire contents of a folder. Instead, you must fetch the folder metadata and retrieve each of its children individually.

##

​

Fetching file and folder metadata

To fetch file and folder metadata, such as path, filename, and created/updated timestamps, make a `GET` request to `/cms/source-code/2026-03/{environment}/metadata/{path}` and set the header to `Accept: application/json`. File and folder metadata will be returned in a JSON object:

  * Folder metadata will be indicated by the `folder: true` property.
  * The `children` array will show the names of files and subfolders within the folder. These filenames can be used to traverse the folder tree: simply fetch one folder metadata and recursively fetch the children of the folder and all subfolders.


##

​

Uploading a file

To upload a local file to your HubSpot account, make a `PUT` request to `/cms/source-code/2026-03/{environment}/content/{path}`. You must upload the file using the `multipart/form-data` content type, and the binary file data must be included as a field named `file`. For example:

  * **Uploading a new file:** PUT `/cms/source-code/2026-03/published/content/my-new-file.html` `Content-Type: multipart/form-data` `Form Data: { file: [_binary file data_] }`
  * **Updating an existing file draft:** PUT `/cms/source-code/2026-03/draft/content/path/to/existing-file.html` `Content-Type: multipart/form-data` `Form Data: { file: [_binary file data_] }`

HubSpot currently supports the following file types:

  * `css`
  * `js`
  * `json`
  * `html`
  * `txt`
  * `md`
  * `jpg`
  * `jpeg`
  * `png`
  * `gif`
  * `map`
  * `svg`
  * `ttf`
  * `woff`
  * `woff2`
  * `zip`


##

​

Validating file contents

To validate the contents of a local file, make a `POST` request to `/cms/source-code/2026-03/{environment}/validate/{path}`. You must upload the file using the `multipart/form-data` content type, and the binary file data must be included as a field named `file`. This can be used to validate HubL in a template/module or JSON for a theme or module. If there are validation errors, you will receive a `400` response with the list of relevant errors. These are the same warnings and errors you would see within the design manager.

Note that invalid files will be rejected if you try and publish them directly. It is recommended to validate files first before publishing.

**For example:** POST `/cms/source-code/2026-03/published/validate/my-file.html` `Content-Type: multipart/form-data` `Form Data: { file: [_binary file data_] }`

##

​

Deleting a file

To delete a file, make a `DELETE` request to `/cms/source-code/2026-03/{environment}/content/{path}`. Deleting from the `published` environment will remove the file entirely, while deleting from the `draft` environment will simply clear out any unpublished changes. Note that deleting published files will immediately impact live content if used anywhere, so make sure to remove all existing references to the file before deleting.

##

​

Extracting a file package

To extract a zip file, make a `POST` request to `/cms/source-code/2026-03/extract/{path}`. The `path` must be a zip file already uploaded to the account. The extraction process is asynchronous and can take up to a minute depending on how many and how large the compressed files are. The contents of the zip are extracted in place to the same folder that contains the zip file, and the original zip file is not deleted automatically upon successful extraction.

Last modified on March 30, 2026

Was this page helpful?

YesNo

⌘I

[facebook](https://www.facebook.com/hubspot)[instagram](https://www.instagram.com/hubspot)[youtube](https://youtube.com/user/HubSpot)[x](https://x.com/HubSpot)[linkedin](https://www.linkedin.com/company/hubspot)[medium](https://medium.com/@HubSpot)