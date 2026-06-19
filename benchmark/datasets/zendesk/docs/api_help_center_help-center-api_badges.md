# Badges

*Source: https://developer.zendesk.com/api-reference/help_center/help-center-api/badges/*

---

## On this page

  * [JSON format](/api-reference/help_center/help-center-api/badges/#json-format)
  * [List Badges](/api-reference/help_center/help-center-api/badges/#list-badges)
  * [Show Badge](/api-reference/help_center/help-center-api/badges/#show-badge)
  * [Create Badge](/api-reference/help_center/help-center-api/badges/#create-badge)
  * [Request Badge Icon Upload URL](/api-reference/help_center/help-center-api/badges/#request-badge-icon-upload-url)
  * [Upload Badge Icon](/api-reference/help_center/help-center-api/badges/#upload-badge-icon)
  * [Update Badge](/api-reference/help_center/help-center-api/badges/#update-badge)
  * [Delete Badge](/api-reference/help_center/help-center-api/badges/#delete-badge)


# Badges

## On this page

  * [JSON format](/api-reference/help_center/help-center-api/badges/#json-format)
  * [List Badges](/api-reference/help_center/help-center-api/badges/#list-badges)
  * [Show Badge](/api-reference/help_center/help-center-api/badges/#show-badge)
  * [Create Badge](/api-reference/help_center/help-center-api/badges/#create-badge)
  * [Request Badge Icon Upload URL](/api-reference/help_center/help-center-api/badges/#request-badge-icon-upload-url)
  * [Upload Badge Icon](/api-reference/help_center/help-center-api/badges/#upload-badge-icon)
  * [Update Badge](/api-reference/help_center/help-center-api/badges/#update-badge)
  * [Delete Badge](/api-reference/help_center/help-center-api/badges/#delete-badge)


A badge is a reward that can be added to a user's profile in the help center. For more information, see [About Gather badges](https://support.zendesk.com/hc/en-us/articles/360045691013-About-Gather-badges) in Zendesk help.

Badges are organized by different [badge categories](/api-reference/help_center/help-center-api/badge_categories/) and are linked to users using [badge assignments](/api-reference/help_center/help-center-api/badge_assignments/).

Badges are available on the Gather Professional plan.

### JSON format

Badges have the following properties:

Name| Type| Read-only| Mandatory| Comment
---|---|---|---|---
id| string| yes| no| Automatically assigned when the badge is created
badge_category_id| string| yes| yes| The id of the badge category of the badge
name| string| no| yes| The name of the badge
description| string| no| yes| The description of the badge. May be an empty string
icon_url| string| no| no| The URL of the badge's icon
created_at| timestamp| yes| no| When the badge was created
updated_at| timestamp| yes| no| When the badge was last updated

#### Example


    {  "id": "01E86XPPRDCNHYTSVWSRMD76R0",  "badge_category_id": "01E86XPM9459S78F83VH8CD69H",  "name": "Community Superhero",  "description": "Saving the day in the community!",  "icon_url": "https://...",  "created_at": "2020-05-13T11:46:19.000Z",  "updated_at": "2020-05-13T11:46:19.000Z"}

### List Badges

  * `GET /api/v2/gather/badges`


Lists all badges.

This request can be further filtered using the `brand_id` query string parameter to only show badge categories within a particular brand.

#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
brand_id| integer| Query| false| Returns the badges for the specified brand

#### Allowed for

  * Help Center managers


#### Using curl


    curl https://{subdomain}.zendesk.com/api/v2/gather/badges \  -v -u {email_address}:{password}

#### Example Response


    Status: 200 OK
    {    "badges": [        {            "id": "01E86XPPRDCNHYTSVWSRMD76R0",            "badge_category_id": "01E86XPM9459S78F83VH8CD69H",            "name": "Community Superhero",            "description": "Saving the day in the community!",            "icon_url": "https://...",            "created_at": "2020-05-13T11:46:19.000Z",            "updated_at": "2020-05-13T11:46:19.000Z"        },        {            "id": "01E89DZ2NA6ZPMBMRPFRXC2BRY",            "badge_category_id": "01E86XPM9459S78F83VH8CD69H",            "name": "Smart Cookie",            "description": "Clever answers to difficult questions.",            "icon_url": null,            "created_at": "2020-05-14T11:08:59.000Z",            "updated_at": "2020-05-14T11:08:59.000Z"        }    ]}

### Show Badge

  * `GET /api/v2/gather/badges/{id}`


Shows information about a single badge.

#### Allowed for

  * Help Center managers


#### Using curl


    curl https://{subdomain}.zendesk.com/api/v2/gather/badges/{id} \  -v -u {email_address}:{password}

#### Example Response


    Status: 200 OK
    {    "badge": {        "id": "01E86XPPRDCNHYTSVWSRMD76R0",        "badge_category_id": "01E86XPM9459S78F83VH8CD69H",        "name": "Community Superhero",        "description": "You're saving the day in the community!",        "icon_url": "https://...",        "created_at": "2020-05-13T11:46:19.000Z",        "updated_at": "2020-05-13T11:46:19.000Z"    }}

### Create Badge

  * `POST /api/v2/gather/badges`


To create a badge without an icon, omit `icon_upload_id`, or set it to null.

To create a badge with an icon:

  1. Request a badge icon upload URL.
  2. Upload the icon to the provided URL with the attached headers.
  3. Send the `POST /api/v2/gather/badges` request while setting the `icon_upload_id` to the value of `badge_icon_upload.id` from the response of step 1.


The base64-based upload mechanism involving `icon_url` has been deprecated.

#### Allowed for

  * Help Center managers


#### Using curl


    curl https://{subdomain}.zendesk.com/api/v2/gather/badges \  -d '{"badge": { "badge_category_id": "...", "name": "Community Superhero", "description": "Saving the day in the community!", "icon_upload_id": "01EYV0KR9EA8VGFMFDMEKPT15C"}}' \  -v -u {email_address}:{password}  -X POST -H "Content-Type: application/json"

### Request Badge Icon Upload URL

  * `POST /api/v2/gather/badges/icon_uploads`


Returns a `badge_icon_upload` object consisting of the following properties:

Name| Type| Description
---|---|---
id| string| A string identifying the badge icon upload. Used later when creating or updating a badge
url| string| A pre-signed AWS S3 URL where the badge icon will be uploaded in a separate request. The URL expires one hour after it's created
headers| object| An object containing the signed header key-value pairs that must be included in the request to the pre-signed S3 URL when uploading the badge icon

The request body takes an object with the following properties:

Name| Type| Description
---|---|---
content_type| string| The content type of badge icon to be uploaded. Allowed types: "image/svg+xml", "image/png", "image/jpeg", or "image/gif"
file_size| integer| The badge icon size in bytes

#### Allowed for

  * Help Center managers


#### Using curl


    curl https://{subdomain}.zendesk.com/api/v2/gather/badges/icon_uploads \  -v -u {email_address}:{password} -d '{"content_type": "image/svg+xml", "file_size": 420000}'\  -X POST -H "Content-Type: application/json"

#### Example Response


    Status: 201 Created{  "badge_icon_upload": {    "id": "01EYV0KR9EA8VGFMFDMEKPT15C",    "url": "https://aus-uploaded-assets-production.s3.amazonaws.com/26/1749971/01EYV0KR9EA8VGFMFDMEKPT15C?Content-Type=image%2Fsvg%2Bxml&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAYSPZOXOPSGBVQTMA%2F20210218%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20210218T164716Z&X-Amz-Expires=3600&X-Amz-Signature=0d297b81820ffe8b609e0f801e73eb5a62b6a6108cd076d26a378a3a22e5efde&X-Amz-SignedHeaders=content-disposition%3Bhost%3Bx-amz-server-side-encryption&x-amz-server-side-encryption=AES256",    "headers": {      "Content-Disposition": "attachment; filename=\"01EYV0KR9EA8VGFMFDMEKPT15C.svg\"",      "Content-Type": "image/svg+xml",      "X-Amz-Server-Side-Encryption": "AES256"    }  }}

### Upload Badge Icon

  * `PUT {path_to_icon}`


Uploads the specified local image to the location specified by the URL returned by the Request Badge Icon Upload URL endpoint. The URL is specified in the `url` property of the `badge_icon_upload` object. Append the headers from the `headers` property of the `badge_icon_upload` object to the PUT request.

#### Using curl


    curl -X PUT -T /path/to/your/image.svg \     -H "Content-Type: image/svg+xml" \     -H "Content-Disposition: attachment; filename=\"01EYV0KR9EA8VGFMFDMEKPT15C.svg\"" \     -H "X-Amz-Server-Side-Encryption: AES256" \     -L "https://aus-uploaded-assets-production.s3.amazonaws.com/26/1749971/01EYV0KR9EA8VGFMFDMEKPT15C?Content-Type=image%2Fsvg%2Bxml&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAYSPZOXOPSGBVQTMA%2F20210218%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20210218T164716Z&X-Amz-Expires=3600&X-Amz-Signature=0d297b81820ffe8b609e0f801e73eb5a62b6a6108cd076d26a378a3a22e5efde&X-Amz-SignedHeaders=content-disposition%3Bhost%3Bx-amz-server-side-encryption&x-amz-server-side-encryption=AES256"

### Update Badge

  * `PUT /api/v2/gather/badges/{id}`


To update a badge not to have an icon, set `icon_upload_id` to null.

To leave the existing icon unchanged, omit `icon_upload_id`.

To update a badge with a new icon:

  1. Request a badge icon upload URL.
  2. Upload the icon to the provided URL with the attached headers.
  3. Send the `PUT /api/v2/gather/badges/{id}` request while setting the `icon_upload_id` to the value of `badge_icon_upload.id` from the response of step 1.


The base64-based upload mechanism involving `icon_url` has been deprecated.

#### Allowed for

  * Help Center managers


#### Using curl


    curl https://{subdomain}.zendesk.com/api/v2/gather/badges/{id} \  -v -u {email_address}:{password} -d '{"badge": { "badge_category_id": "...", "name": "Community Superhero", "description": "Saving the day in the community!"}}' \  -X PUT -H "Content-Type: application/json"

### Delete Badge

  * `DELETE /api/v2/gather/badges/{id}`


Deleting a badge also deletes all badge assignments that pertain to the badge.

#### Allowed for

  * Help Center managers


#### Using curl


    curl https://{subdomain}.zendesk.com/api/v2/gather/badges/{id} \  -v -u {email_address}:{password} -X DELETE

#### Example Response


    Status: 204 No Content

Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)