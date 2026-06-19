# Themes

*Source: https://developer.zendesk.com/api-reference/help_center/help-center-api/theming/*

---

## On this page

  * [JSON Format for Themes](/api-reference/help_center/help-center-api/theming/#json-format-for-themes)
  * [List Themes](/api-reference/help_center/help-center-api/theming/#list-themes)
  * [Show Theme](/api-reference/help_center/help-center-api/theming/#show-theme)
  * [Publish Theme](/api-reference/help_center/help-center-api/theming/#publish-theme)
  * [Delete Theme](/api-reference/help_center/help-center-api/theming/#delete-theme)
  * [JSON Format for Jobs](/api-reference/help_center/help-center-api/theming/#json-format-for-jobs)
  * [Show Job](/api-reference/help_center/help-center-api/theming/#show-job)
  * [Create Theme Import Job](/api-reference/help_center/help-center-api/theming/#create-theme-import-job)
  * [Create Theme Update Job](/api-reference/help_center/help-center-api/theming/#create-theme-update-job)
  * [Create Theme Export Job](/api-reference/help_center/help-center-api/theming/#create-theme-export-job)


# Themes

## On this page

  * [JSON Format for Themes](/api-reference/help_center/help-center-api/theming/#json-format-for-themes)
  * [List Themes](/api-reference/help_center/help-center-api/theming/#list-themes)
  * [Show Theme](/api-reference/help_center/help-center-api/theming/#show-theme)
  * [Publish Theme](/api-reference/help_center/help-center-api/theming/#publish-theme)
  * [Delete Theme](/api-reference/help_center/help-center-api/theming/#delete-theme)
  * [JSON Format for Jobs](/api-reference/help_center/help-center-api/theming/#json-format-for-jobs)
  * [Show Job](/api-reference/help_center/help-center-api/theming/#show-job)
  * [Create Theme Import Job](/api-reference/help_center/help-center-api/theming/#create-theme-import-job)
  * [Create Theme Update Job](/api-reference/help_center/help-center-api/theming/#create-theme-update-job)
  * [Create Theme Export Job](/api-reference/help_center/help-center-api/theming/#create-theme-export-job)


The Themes API lets you manage Guide themes and integrate more complex theme development workflows with Guide.

The API consists of themes and jobs. A theme resource represents a Guide theme. Jobs are used for asynchronous operations.

If you're using multiple brands, send requests to the account domain, not the brand domain.

If you're using OAuth2 authentication, set the required scopes to `themes:read` or `themes:write` to perform read operations or all operations, respectively.

### JSON Format for Themes

Themes are represented by JSON objects with the following properties:

Name| Type| Comment
---|---|---
id| string| Automatically assigned when the theme is created
name| string| The name of the theme
version| string| The version number of the theme. Specified in the theme manifest
author| string| The author of the theme. Specified in the theme manifest
live| boolean| Whether or not the theme is currently published in Help Center
created_at| timestamp| The time at which the theme was created
updated_at| timestamp| The time at which the theme was last updated
brand_id| string| The brand id of the theme

#### Example


    {  "id": "asdf123-asdf",  "name": "Copenhagen",  "author": "Zendesk",  "version": "1.7.5",  "live": true,  "created_at": "2012-04-04T09:14:57Z",  "updated_at": "2012-04-04T09:14:57Z"}

### List Themes

  * `GET /api/v2/guide/theming/themes`
  * `GET /api/v2/guide/theming/themes?brand_id={brand_id}`


#### Allowed for

  * Guide managers


#### Using curl


    curl https://{subdomain}.zendesk.com/api/v2/guide/theming/themes?brand_id={brand_id} \  -v -u {email_address}:{password}

#### Example Response


    Status: 200 OK
    {  "themes": [    {      "id":      "asdf123-asdf",      "name":    "Copenhagen",      "author":  "Zendesk",      ...    },    ...  ]}

### Show Theme

  * `GET /api/v2/guide/theming/themes/{id}`


#### Allowed for

  * Guide managers


#### Using curl


    curl https://{subdomain}.zendesk.com/api/v2/guide/theming/themes/{id} \  -v -u {email_address}:{password}

#### Example Response


    Status: 200 OK
    {  "theme": {    "id":      "asdf123-asdf",    "name":    "Copenhagen",    "author":  "Zendesk",    ...  }}

### Publish Theme

  * `POST /api/v2/guide/theming/themes/{id}/publish`


#### Allowed for

  * Guide managers


#### Using curl


    curl https://{subdomain}.zendesk.com/api/v2/guide/theming/themes/{id}/publish \  -v -u {email_address}:{password} -X POST

#### Example Response


    Status: 200 OK
    {  "theme": {    "id":      "asdf123-asdf",    "name":    "Copenhagen",    "author":  "Zendesk",    "live":    true    ...  }}

### Delete Theme

  * `DELETE /api/v2/guide/theming/themes/{id}`


#### Allowed for

  * Guide managers


#### Using curl


    curl https://{subdomain}.zendesk.com/api/v2/guide/theming/themes/{id} \  -v -u {email_address}:{password} -X DELETE

#### Example Response


    Status: 204 No Content

### JSON Format for Jobs

Name| Type| Comment
---|---|---
status| string| The current status of the job. Possible values: "pending", "completed", or "failed"
errors| array| An array of errors if the job failed. Returns null if the job is pending or successful. See errors
data| object| Job-specific data provided on job creation

#### errors

Jobs return an `errors` array. If the job is pending or successful, the `errors` property is null. If the job was not successful, the `errors` property may contain an array of error objects. The format of error objects is as follows:

Name| Type| Comment
---|---|---
title| string| The error message
code| string| A unique identifier for the error. See Failed Job Error Codes
meta| object| An object with further error information

##### Example Error Responses


    Status: 404 Not Found
    {  "errors": [    {      "title": "Theme not found",      "code": "ThemeNotFound",      "status": "404",      "meta": {        "id": "theme_id"       }    }  ]}


    Status: 400 Bad Request
    {  "errors": [    {      "title": "The provided brand is not valid",      "code": "InvalidBrand",      "status": "400",      "meta": { ... }    }  ]}

##### Generic Error Codes

Http status| Code| Comment
---|---|---
401| InvalidOAuthScopes| The oauth scope provided does not match the required scope
400| UnavailableFeatures| The theme is attempting to use features not available in the current Guide plan
400| InvalidBrand| Incorrect brand id

##### Themes Error Codes

Http status| Code| Comment
---|---|---
404| ThemeNotFound| The provided theme id is non-existent
400| LiveThemeDeleted| A brand's live theme cannot be deleted

##### Job Error Codes

Http status| Code| Comment
---|---|---
404| JobNotFound| The provided job id is non-existent
400| TooManyThemes| Maximum number of allowed themes reached
400| NonUpdatableTheme| Attempting to update a non `api` theme

##### Failed Job Error Codes

Code| Comment
---|---
TooManyThemes| Maximum number of allowed themes reached
NameTooLong| The theme name is longer than allowed
FileNotSupported| The file is not supported, wrong extension, dir etc.
FileTooBig| An added file is bigger than the allowed
ThemeTooBig| The theme is above the maximum size
FileNameTooLong| The file name is longer than allowed
FileNotFound| A required file cannot be found
FileLimitReached| The maximum number of files have been reached
FileDeletionInProgress| Attempting to change a file that is marked for deletion
InvalidTemplates| Templates have syntax errors
InvalidSetting| Setting is not valid
TooManySettings| More than the allowed amount of settings
InvalidManifest| The manifest is not valid
UnsupportedLocale| The locale is not supported
InvalidTranslationFile| The translation file is not valid
InvalidThemeVersion| The theme version is not valid
NonUpdatableTheme| Theme cannot be updated

#### Example


    {  "status": "pending",  "errors": null,  "data": null}

### Show Job

  * `GET /api/v2/guide/theming/jobs/{id}`


#### Allowed for

  * Guide managers


#### Using curl


    curl https://{subdomain}.zendesk.com/api/v2/guide/theming/jobs/{id} \  -v -u {email_address}:{password}

#### Example Response


    Status: 200 OK
    {  "job": {    "status": "failed",    "errors": [      {        "title": "Theme not found",        "code": "ThemeNotFound",        "meta": { }      }    ]  }}

### Create Theme Import Job

  * `POST /api/v2/guide/theming/jobs/themes/imports`


The endpoint does not receive the ZIP file itself. See Theme Import Workflow for more information.

This job's `data` object has the following format:

Name| Type| Comment
---|---|---
theme_id| string| Automatically assigned when the job is created
upload.url| string| One-time URL for the storage location
upload.parameters| object| Parameters to be used when posting the ZIP file to the upload url

**Note** : The upload `parameters` should be considered unstable and provided as-is without modification.

#### Allowed for

  * Guide managers


#### Request Body Format

Name| Type| Comment
---|---|---
job.attributes.brand_id| string| The id of the brand where the theme should be imported to
job.attributes.format| enum| Valid enums ["zip"]

#### Using curl


    curl https://{subdomain}.zendesk.com/api/v2/guide/theming/jobs/themes/imports \  -d '{ "job": { "attributes": { "brand_id": "brand_id", "format":"zip" } } }' \  -H "Content-Type: application/json" \  -v -u {email_address}:{password} -X POST

#### Example Response


    Status: 202 Accepted
    {  "job": {    "id": "a66e7bde543c6b6d018f0e07a654feaf",    "status": "pending",    "errors": null,    "data": {      "theme_id": "asdf123-asdf",      "upload": {        "url": "storage.zdassets.com/storage-location",        "parameters": { ... }      }    }  }}

#### Theme Import Workflow

To import a theme:

  1. Create a theme import job with the Create Theme Import Job endpoint.

  2. Upload the file to the storage location specified in the `upload` object. Upload the file by sending a POST request to the specified upload url. Don't specify any authentication headers. The POST request's `Content-Type` must be `multipart/form-data` and each parameter in the `parameters` object must be provided as a form field in addition to a `file` field containing the ZIP file to be uploaded.

  3. Poll the job status with the Show Job endpoint to know when the theme is available for use. When the status is "completed", the theme with `theme_id` is available for use. Avoid polling too frequently to prevent being rate limited. Example: Poll every 5 seconds.


##### Example script for Theme Import Workflow

Use the following steps to create a simple theme import script using Ruby. The script doesn't include error handling.

  1. Install the following gems:

         gem install faradaygem install faraday-net_httpgem install faraday-multipart

  2. Create a local **theme_upload.rb** file. Past the following script into the file. Fill in lines 5â9 with your Zendesk account information.

         require 'faraday'require 'faraday/net_http'require 'faraday/multipart'
         subdomain = ''file_path = ''brand_id = ''email = ''password = ''
         conn = Faraday.new do |f|  f.request :json  f.request :authorization, :basic, email, password  f.response :json  f.response :logger, nil, { headers: false, bodies: true}  f.adapter :net_httpend
         response = conn.post("https://#{subdomain}.zendesk.com/api/v2/guide/theming/jobs/themes/imports",                    { 'job': { 'attributes': { 'brand_id': "#{brand_id}", 'format': 'zip' } } })
         job_id = response.body['job']['id']storage_url = response.body['job']['data']['upload']['url']storage_parameters = response.body['job']['data']['upload']['parameters']
         stor_conn = Faraday.new do |f|  f.request :multipart  f.request :url_encoded  f.adapter :net_httpend
         storage_body = storage_parameters.merge(file: Faraday::UploadIO.new(file_path, 'application/zip'))
         stor_conn.post(storage_url, storage_body)
         10.times do  job_status_response = conn.get("https://#{subdomain}.zendesk.com/api/v2/guide/theming/jobs/#{job_id}")
           puts job_status_response.body  break unless job_status_response.body['job']['status'] == 'pending'
           sleep(5)end

  3. In your shell, run the following command to add the theme to your brand:

         ruby theme_upload.rb


### Create Theme Update Job

  * `POST /api/v2/guide/theming/jobs/themes/updates`


The endpoint does not receive the ZIP file itself. See Theme Update Workflow for more information.

This job's `data` object has the following format:

Name| Type| Comment
---|---|---
upload.url| string| One-time URL for the storage location
upload.parameters| object| Parameters to be used when posting the ZIP file to the upload url

**Note** : The upload `parameters` should be considered unstable and provided as-is without modification.

#### Allowed for

  * Guide managers


#### Request Body Format

Name| Type| Comment
---|---|---
job.attributes.theme_id| string| Id of the theme to export
job.attributes.replace_settings| boolean| Whether or not to replace the current theme settings
job.attributes.format| enum| Valid enums ["zip"]

#### Using curl


    curl https://{subdomain}.zendesk.com/api/v2/guide/theming/jobs/themes/updates \  -d '{"job": { "attributes": { "theme_id": "theme_id", "replace_settings": true, "format":"zip" } } }' \  -H "Content-Type: application/json" \  -v -u {email_address}:{password} -X POST

#### Example Response


    Status: 202 Accepted
    {  "job": {    "id": "a66e7bde543c6b6d018f0e07a654feaf",    "status": "pending",    "errors": null,    "data": {      "upload": {        "url": "storage.zdassets.com/storage-location",        "parameters": { ... }      }    }  }}

#### Theme Update Workflow

To update a theme:

  1. Create an theme update job with the Create Theme Update Job endpoint.

  2. Upload the file to the storage location specified in the `upload` object. Upload the file by sending a POST request to the specified upload url. Don't specify any authentication headers. The POST request's `Content-Type` must be `multipart/form-data` and each parameter in the parameters object must be provided as a form field in addition to a `file` field containing the ZIP file to be uploaded.

  3. Poll the job status with the Show Job endpoint to know when the theme has been updated. When the status is "completed", the theme has been updated to the uploaded version. Avoid polling too frequently to prevent being rate limited. Example: Poll every 5 seconds.


### Create Theme Export Job

  * `POST /api/v2/guide/theming/jobs/themes/exports`


The endpoint does not deliver the ZIP file itself. See Theme Export Workflow for more information.

This job's `data` object has the following format:

Name| Type| Comment
---|---|---
download.url| string| Where the theme can be downloaded after the job is completed

#### Allowed for

  * Guide managers


#### Request Body Format

Name| Type| Comment
---|---|---
job.attributes.theme_id| string| Id of the theme to export
job.attributes.format| enum| Valid enums ["zip"]

#### Using curl


    curl https://{subdomain}.zendesk.com/api/v2/guide/theming/jobs/themes/exports \  -d '{ "job": { "attributes": { "theme_id": "theme_id", "format":"zip" } } }' \  -H "Content-Type: application/json" \  -v -u {email_address}:{password} -X POST

#### Example Response


    Status: 202 Accepted
    {  "job": {    "id": "a66e7bde543c6b6d018f0e07a654feaf",    "status": "pending",    "errors": null,    "data": {      "download": {        "url": "storage.zdassets.com/storage-location"      }    }  }}

#### Theme Export Workflow

To export a theme:

  1. Create an theme export job with the Create Theme Export Job endpoint.

  2. Poll the job status with the Show Job endpoint until the job is no longer "pending".

  3. When the job status is "completed", download the theme using the url from the download object.


Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)