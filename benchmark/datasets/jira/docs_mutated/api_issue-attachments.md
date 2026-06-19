# Jira Cloud platform

*Source: https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-attachments/*

---

Cloud

Jira Cloud platform / Reference / REST API v3

# Issue attachments

[Postman Collection](/cloud/jira/platform/jiracloud.3.postman.json)

[OpenAPI](https://dac-static.atlassian.com/cloud/jira/platform/swagger-v3.v3.json?_v=1.8453.0)

This resource represents issue attachments and the attachment settings for Jira. Use it to get the metadata for an attachment, delete an attachment, and view the metadata for the contents of an attachment. Also, use it to get the attachment settings for Jira.

Operations

[GET/rest/api/3/attachment/content/{id}](/cloud/jira/platform/rest/v3/api-group-issue-attachments/#api-rest-api-3-attachment-content-id-get)[GET/rest/api/3/attachment/meta](/cloud/jira/platform/rest/v3/api-group-issue-attachments/#api-rest-api-3-attachment-meta-get)[GET/rest/api/3/attachment/thumbnail/{id}](/cloud/jira/platform/rest/v3/api-group-issue-attachments/#api-rest-api-3-attachment-thumbnail-id-get)[GET/rest/api/3/attachment/{id}](/cloud/jira/platform/rest/v3/api-group-issue-attachments/#api-rest-api-3-attachment-id-get)[DEL/rest/api/3/attachment/{id}](/cloud/jira/platform/rest/v3/api-group-issue-attachments/#api-rest-api-3-attachment-id-delete)[GET/rest/api/3/attachment/{id}/expand/human](/cloud/jira/platform/rest/v3/api-group-issue-attachments/#api-rest-api-3-attachment-id-expand-human-get)[GET/rest/api/3/attachment/{id}/expand/raw](/cloud/jira/platform/rest/v3/api-group-issue-attachments/#api-rest-api-3-attachment-id-expand-raw-get)[POST/rest/api/3/issue/{issueIdOrKey}/attachments](/cloud/jira/platform/rest/v3/api-group-issue-attachments/#api-rest-api-3-issue-issueidorkey-attachments-post)

---

GET

## Get attachment content

Returns the contents of an attachment. A `Range` header can be set to define a range of bytes within the attachment to download. See the [HTTP Range header standard](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Range) for details.

To return a thumbnail of the attachment, use [Get attachment thumbnail](/cloud/jira/platform/rest/v3/api-group-issue-attachments/#api-rest-api-3-attachment-thumbnail-id-get).

This operation can be accessed anonymously.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** For the issue containing the attachment:

  * _Browse projects_ [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
  * If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
  * If attachments are added in private comments, the comment-level restriction will be applied.


**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-work`

**Granular** :`read:attachment:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

#### Path parameters

**id**

string

Required

#### Query parameters

**redirect**

boolean

### Responses

200OK

Returned if the request is successful when `redirect` is set to `false`.

206Partial Content

303See Other

400Bad Request

401Unauthorized

403Forbidden

404Not Found

416Requested Range Not Satisfiable

GET/rest/api/3/attachment/content/{id}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/attachment/content/{id}`); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.text());`

---

GET

## Get Jira attachment settings

Returns the attachment settings, that is, whether attachments are enabled and the maximum attachment size allowed.

Note that there are also [project permissions](https://confluence.atlassian.com/x/yodKLg) that restrict whether users can create and delete attachments.

This operation can be accessed anonymously.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** None.

**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-work`

**Granular** :`read:instance-configuration:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

This request has no parameters.

### Responses

200OK

Returned if the request is successful.

#### application/json

AttachmentSettings

Details of the instance's attachment settings.

Show child properties

401Unauthorized

GET/rest/api/3/attachment/meta

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/attachment/meta`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 ``{ "enabled": true, "uploadLimit": 1000000 }`

---

GET

## Get attachment thumbnail

Returns the thumbnail of an attachment.

To return the attachment contents, use [Get attachment content](/cloud/jira/platform/rest/v3/api-group-issue-attachments/#api-rest-api-3-attachment-content-id-get).

This operation can be accessed anonymously.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** For the issue containing the attachment:

  * _Browse projects_ [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
  * If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
  * If attachments are added in private comments, the comment-level restriction will be applied.


**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-work`

**Granular** :`read:attachment:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

#### Path parameters

**id**

string

Required

#### Query parameters

Expand all

**redirect**

boolean

**fallbackToDefault**

boolean

**width**

integer

**height**

integer

### Responses

200OK

Returned if the request is successful when `redirect` is set to `false`.

303See Other

400Bad Request

401Unauthorized

403Forbidden

404Not Found

GET/rest/api/3/attachment/thumbnail/{id}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/attachment/thumbnail/{id}`); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.text());`

---

GET

## Get attachment metadata

Returns the metadata for an attachment. Note that the attachment itself is not returned.

This operation can be accessed anonymously.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:**

  * _Browse projects_ [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
  * If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
  * If attachments are added in private comments, the comment-level restriction will be applied.


**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-work`

**Granular** :`read:attachment:jira`, `read:user:jira`, `read:application-role:jira`, `read:avatar:jira`, `read:group:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

#### Path parameters

**id**

string

Required

### Responses

200OK

Returned if the request is successful.

#### application/json

AttachmentMetadata

Metadata for an issue attachment.

Show child properties

401Unauthorized

403Forbidden

404Not Found

GET/rest/api/3/attachment/{id}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/attachment/{id}`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 ``{ "author": { "user_id": "5b10a2844c20165700ede21g", "accountType": "atlassian", "active": false, "avatarUrls": { "16x16": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=16&s=16", "24x24": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=24&s=24", "32x32": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=32&s=32", "48x48": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=48&s=48" }, "displayName": "Mia Krystof", "key": "", "name": "", "self": "https://your-domain.atlassian.net/rest/api/3/user?user_id=5b10a2844c20165700ede21g" }, "content": "https://your-domain.atlassian.net/jira/rest/api/3/attachment/content/10000", "created": "2022-10-06T07:32:47.000+0000", "filename": "picture.jpg", "id": 10000, "mimeType": "image/jpeg", "self": "https://your-domain.atlassian.net/rest/api/3/attachments/10000", "size": 23123, "thumbnail": "https://your-domain.atlassian.net/jira/rest/api/3/attachment/thumbnail/10000" }`

---

DEL

## Delete attachment

Deletes an attachment from an issue.

This operation can be accessed anonymously.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** For the project holding the issue containing the attachment:

  * _Delete own attachments_ [project permission](https://confluence.atlassian.com/x/yodKLg) to delete an attachment created by the calling user.
  * _Delete all attachments_ [project permission](https://confluence.atlassian.com/x/yodKLg) to delete an attachment created by any user.


**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`write:jira-work`

**Granular** :`delete:attachment:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `DELETE`

### Request

#### Path parameters

**id**

string

Required

### Responses

204No Content

Returned if the request is successful.

403Forbidden

404Not Found

DEL/rest/api/3/attachment/{id}

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/attachment/{id}`, { method: 'DELETE' }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.text());`

---

GET

## Get all metadata for an expanded attachmentExperimental

Returns the metadata for the contents of an attachment, if it is an archive, and metadata for the attachment itself. For example, if the attachment is a ZIP archive, then information about the files in the archive is returned and metadata for the ZIP archive. Currently, only the ZIP archive format is supported.

Use this operation to retrieve data that is presented to the user, as this operation returns the metadata for the attachment itself, such as the attachment's ID and name. Otherwise, use [ Get contents metadata for an expanded attachment](/cloud/jira/platform/rest/v3/api-group-issue-attachments/#api-rest-api-3-attachment-id-expand-raw-get), which only returns the metadata for the attachment's contents.

This operation can be accessed anonymously.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** For the issue containing the attachment:

  * _Browse projects_ [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
  * If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
  * If attachments are added in private comments, the comment-level restriction will be applied.


**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-work`

**Granular** :`read:attachment:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

#### Path parameters

**id**

string

Required

### Responses

200OK

Returned if the request is successful. If an empty list is returned in the response, the attachment is empty, corrupt, or not an archive.

#### application/json

AttachmentArchiveMetadataReadable

Metadata for an archive (for example a zip) and its contents.

Show child properties

401Unauthorized

403Forbidden

404Not Found

409Conflict

GET/rest/api/3/attachment/{id}/expand/human

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/attachment/{id}/expand/human`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 ``{ "entries": [ { "index": 0, "label": "MG00N067.JPG", "mediaType": "image/jpeg", "path": "MG00N067.JPG", "size": "119 kB" }, { "index": 1, "label": "Allegro from Duet in C Major.mp3", "mediaType": "audio/mpeg", "path": "Allegro from Duet in C Major.mp3", "size": "1.36 MB" }, { "index": 2, "label": "long/path/thanks/to/.../reach/the/leaf.txt", "mediaType": "text/plain", "path": "long/path/thanks/to/lots/of/subdirectories/inside/making/it/quite/hard/to/reach/the/leaf.txt", "size": "0.0 k" } ], "id": 7237823, "mediaType": "application/zip", "name": "images.zip", "totalEntryCount": 39 }`

---

GET

## Get contents metadata for an expanded attachmentExperimental

Returns the metadata for the contents of an attachment, if it is an archive. For example, if the attachment is a ZIP archive, then information about the files in the archive is returned. Currently, only the ZIP archive format is supported.

Use this operation if you are processing the data without presenting it to the user, as this operation only returns the metadata for the contents of the attachment. Otherwise, to retrieve data to present to the user, use [ Get all metadata for an expanded attachment](/cloud/jira/platform/rest/v3/api-group-issue-attachments/#api-rest-api-3-attachment-id-expand-human-get) which also returns the metadata for the attachment itself, such as the attachment's ID and name.

This operation can be accessed anonymously.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:** For the issue containing the attachment:

  * _Browse projects_ [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
  * If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
  * If attachments are added in private comments, the comment-level restriction will be applied.


**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`read:jira-work`

**Granular** :`read:attachment:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `READ`

### Request

#### Path parameters

**id**

string

Required

### Responses

200OK

Returned if the request is successful. If an empty list is returned in the response, the attachment is empty, corrupt, or not an archive.

#### application/json

AttachmentArchiveImpl

Show child properties

401Unauthorized

403Forbidden

404Not Found

409Conflict

GET/rest/api/3/attachment/{id}/expand/raw

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/attachment/{id}/expand/raw`, { headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 ``{ "entries": [ { "entryIndex": 0, "mediaType": "audio/mpeg", "name": "Allegro from Duet in C Major.mp3", "size": 1430174 }, { "entryIndex": 1, "mediaType": "text/rtf", "name": "lrm.rtf", "size": 331 } ], "totalEntryCount": 24 }`

---

POST

## Add attachment

Adds one or more attachments to an issue. Attachments are posted as multipart/form-data ([RFC 1867](https://www.ietf.org/rfc/rfc1867.txt)).

Note that:

  * The request must have a `X-Atlassian-Token: no-check` header, if not it is blocked. See [Special headers](/cloud/jira/platform/rest/v3/intro/#special-request-headers) for more information.
  * The name of the multipart/form-data parameter that contains the attachments must be `file`.


The following examples upload a file called _myfile.txt_ to the issue _TEST-123_ :

#### curl


    1
    2
    3
    4
    curl --location --request POST 'https://your-domain.atlassian.net/rest/api/3/issue/TEST-123/attachments'
     -u 'email@example.com:<api_token>'
     -H 'X-Atlassian-Token: no-check'
     --form 'file=@"myfile.txt"'


#### Node.js


    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    15
    16
    17
    18
    19
    20
    21
    22
    23
    24
    25
    26
    27
    28
    29
    30
    31
    32
    33
    34
    // This code sample uses the 'node-fetch' and 'form-data' libraries:
     // https://www.npmjs.com/package/node-fetch
     // https://www.npmjs.com/package/form-data
     const fetch = require('node-fetch');
     const FormData = require('form-data');
     const fs = require('fs');

     const filePath = 'myfile.txt';
     const form = new FormData();
     const stats = fs.statSync(filePath);
     const fileSizeInBytes = stats.size;
     const fileStream = fs.createReadStream(filePath);

     form.append('file', fileStream, {knownLength: fileSizeInBytes});

     fetch('https://your-domain.atlassian.net/rest/api/3/issue/TEST-123/attachments', {
         method: 'POST',
         body: form,
         headers: {
             'Authorization': `Basic ${Buffer.from(
                 'email@example.com:'
             ).toString('base64')}`,
             'Accept': 'application/json',
             'X-Atlassian-Token': 'no-check'
         }
     })
         .then(response => {
             console.log(
                 `Response: ${response.status} ${response.statusText}`
             );
             return response.text();
         })
         .then(text => console.log(text))
         .catch(err => console.error(err));


#### Java


    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    // This code sample uses the  'Unirest' library:
     // http://unirest.io/java.html
     HttpResponse response = Unirest.post("https://your-domain.atlassian.net/rest/api/2/issue/{issueIdOrKey}/attachments")
             .basicAuth("email@example.com", "")
             .header("Accept", "application/json")
             .header("X-Atlassian-Token", "no-check")
             .field("file", new File("myfile.txt"))
             .asJson();

             System.out.println(response.getBody());


#### Python


    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    15
    16
    17
    18
    19
    20
    21
    22
    23
    24
    25
    26
    # This code sample uses the 'requests' library:
     # http://docs.python-requests.org
     import requests
     from requests.auth import HTTPBasicAuth
     import json

     url = "https://your-domain.atlassian.net/rest/api/2/issue/{issueIdOrKey}/attachments"

     auth = HTTPBasicAuth("email@example.com", "")

     headers = {
        "Accept": "application/json",
        "X-Atlassian-Token": "no-check"
     }

     response = requests.request(
        "POST",
        url,
        headers = headers,
        auth = auth,
        files = {
             "file": ("myfile.txt", open("myfile.txt","rb"), "application-type")
        }
     )

     print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))


#### PHP


    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    15
    16
    17
    18
    19
    20
    // This code sample uses the 'Unirest' library:
     // http://unirest.io/php.html
     Unirest\Request::auth('email@example.com', '');

     $headers = array(
       'Accept' => 'application/json',
       'X-Atlassian-Token' => 'no-check'
     );

     $parameters = array(
       'file' => File::add('myfile.txt')
     );

     $response = Unirest\Request::post(
       'https://your-domain.atlassian.net/rest/api/2/issue/{issueIdOrKey}/attachments',
       $headers,
       $parameters
     );

     var_dump($response)


#### Forge


    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    15
    16
    17
    18
    19
    20
    // This sample uses Atlassian Forge and the `form-data` library.
     // https://developer.atlassian.com/platform/forge/
     // https://www.npmjs.com/package/form-data
     import api from "@forge/api";
     import FormData from "form-data";

     const form = new FormData();
     form.append('file', fileStream, {knownLength: fileSizeInBytes});

     const response = await api.asApp().requestJira('/rest/api/2/issue/{issueIdOrKey}/attachments', {
         method: 'POST',
         body: form,
         headers: {
             'Accept': 'application/json',
             'X-Atlassian-Token': 'no-check'
         }
     });

     console.log(`Response: ${response.status} ${response.statusText}`);
     console.log(await response.json());


Tip: Use a client library. Many client libraries have classes for handling multipart POST operations. For example, in Java, the Apache HTTP Components library provides a [MultiPartEntity](http://hc.apache.org/httpcomponents-client-ga/httpmime/apidocs/org/apache/http/entity/mime/MultipartEntity.html) class for multipart POST operations.

This operation can be accessed anonymously.

**[Permissions](/cloud/jira/platform/rest/v3/intro/#permissions) required:**

  * _Browse Projects_ and _Create attachments_ [ project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
  * If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.


**[Data Security Policy](/cloud/confluence/data-security-developer-guide)** : Not exempt from app access rules

##### Scopes

**[OAuth 2.0 scopes](/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) required:**

**Classic** RECOMMENDED:`write:jira-work`

**Granular** :`read:user:jira`, `write:attachment:jira`, `read:attachment:jira`, `read:avatar:jira`

**[Connect app scope](/cloud/jira/platform/scopes) required**:Â `WRITE`

### Request

#### Path parameters

**issueIdOrKey**

string

Required

#### Request bodymultipart/form-data

Expand all

array<MultipartFile>

**bytes**

array<string>

**contentType**

string

**empty**

boolean

**inputStream**

object

**name**

string

**originalFilename**

string

**resource**

Resource

**size**

integer

### Responses

200OK

Returned if the request is successful.

#### application/json

array<Attachment>

Show child properties

403Forbidden

404Not Found

413Request Entity Too Large

POST/rest/api/3/issue/{issueIdOrKey}/attachments

Forge

curl

Node.js

Java

Python

PHP

`1 2 3 4 5 6 7 8 9 10 11 12 13 ``// This sample uses Atlassian Forge // https://developer.atlassian.com/platform/forge/ import { requestJira } from "@forge/bridge"; const response = await requestJira(`/rest/api/3/issue/{issueIdOrKey}/attachments`, { method: 'POST', headers: { 'Accept': 'application/json' } }); console.log(`Response: ${response.status} ${response.statusText}`); console.log(await response.json());`

200Response

`1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 ``[ { "author": { "user_id": "5b10a2844c20165700ede21g", "active": true, "avatarUrls": { "16x16": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=16&s=16", "24x24": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=24&s=24", "32x32": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=32&s=32", "48x48": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=48&s=48" }, "displayName": "Mia Krystof", "emailAddress": "mia@example.com", "self": "https://your-domain.atlassian.net/rest/api/3/user?user_id=5b10a2844c20165700ede21g", "timeZone": "Australia/Sydney" }, "content": "https://your-domain.atlassian.net/rest/api/3/attachment/content/10000", "created": 1651316514000, "filename": "picture.jpg", "id": "10001", "mimeType": "image/jpeg", "self": "https://your-domain.atlassian.net/rest/api/3/attachments/10000", "size": 23123, "thumbnail": "https://your-domain.atlassian.net/rest/api/3/attachment/thumbnail/10000" }, { "author": { "user_id": "5b10a2844c20165700ede21g", "active": true, "avatarUrls": { "16x16": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=16&s=16", "24x24": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=24&s=24", "32x32": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=32&s=32", "48x48": "https://avatar-management--avatars.server-location.prod.public.atl-paas.net/initials/MK-5.png?size=48&s=48" }, "displayName": "Mia Krystof", "emailAddress": "mia@example.com", "self": "https://your-domain.atlassian.net/rest/api/3/user?user_id=5b10a2844c20165700ede21g", "timeZone": "Australia/Sydney" }, "content": "https://your-domain.atlassian.net/rest/api/3/attachment/content/10001", "created": 1658898511000, "filename": "dbeuglog.txt", "mimeType": "text/plain", "self": "https://your-domain.atlassian.net/rest/api/3/attachments/10001", "size": 2460 } ]`