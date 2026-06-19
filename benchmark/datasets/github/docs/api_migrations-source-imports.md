# REST API endpoints for source imports

*Source: https://docs.github.com/en/rest/migrations/source-imports*

---

# REST API endpoints for source imports
Use the REST API to start an import from a Git source repository.

## About source imports
Warning
Due to very low levels of usage and available alternatives, the Source Imports API has been retired. For more details and alternatives, see thechangelog.
You can use these endpoints to start an import from a Git repository hosted with another service. This is the same functionality as the GitHub Importer. For more information, seeImporting a repository with GitHub Importer. A typical source import would start the import and then (optionally) update the authors and/or update the preference for using Git LFS if large files exist in the import. You can also create a webhook that listens for theRepositoryImportEventto find out the status of the import.

```
RepositoryImportEvent
```
Note
These endpoints only support authentication using a personal access token (classic). For more information, seeManaging your personal access tokens.
The following diagram provides a more detailed example:

```
+---------+                     +--------+                              +---------------------+
| Tooling |                     | GitHub |                              | Original Repository |
+---------+                     +--------+                              +---------------------+
     |                              |                                              |
     |  Start import                |                                              |
     |----------------------------->|                                              |
     |                              |                                              |
     |                              |  Download source data                        |
     |                              |--------------------------------------------->|
     |                              |                        Begin streaming data  |
     |                              |<---------------------------------------------|
     |                              |                                              |
     |  Get import progress         |                                              |
     |----------------------------->|                                              |
     |       "status": "importing"  |                                              |
     |<-----------------------------|                                              |
     |                              |                                              |
     |  Get commit authors          |                                              |
     |----------------------------->|                                              |
     |                              |                                              |
     |  Map a commit author         |                                              |
     |----------------------------->|                                              |
     |                              |                                              |
     |                              |                                              |
     |                              |                       Finish streaming data  |
     |                              |<---------------------------------------------|
     |                              |                                              |
     |                              |  Rewrite commits with mapped authors         |
     |                              |------+                                       |
     |                              |      |                                       |
     |                              |<-----+                                       |
     |                              |                                              |
     |                              |  Update repository on GitHub                 |
     |                              |------+                                       |
     |                              |      |                                       |
     |                              |<-----+                                       |
     |                              |                                              |
     |  Map a commit author         |                                              |
     |----------------------------->|                                              |
     |                              |  Rewrite commits with mapped authors         |
     |                              |------+                                       |
     |                              |      |                                       |
     |                              |<-----+                                       |
     |                              |                                              |
     |                              |  Update repository on GitHub                 |
     |                              |------+                                       |
     |                              |      |                                       |
     |                              |<-----+                                       |
     |                              |                                              |
     |  Get large files             |                                              |
     |----------------------------->|                                              |
     |                              |                                              |
     |  opt_in to Git LFS           |                                              |
     |----------------------------->|                                              |
     |                              |  Rewrite commits for large files             |
     |                              |------+                                       |
     |                              |      |                                       |
     |                              |<-----+                                       |
     |                              |                                              |
     |                              |  Update repository on GitHub                 |
     |                              |------+                                       |
     |                              |      |                                       |
     |                              |<-----+                                       |
     |                              |                                              |
     |  Get import progress         |                                              |
     |----------------------------->|                                              |
     |        "status": "complete"  |                                              |
     |<-----------------------------|                                              |
     |                              |                                              |
     |                              |                                              |
```

```
+---------+                     +--------+                              +---------------------+
| Tooling |                     | GitHub |                              | Original Repository |
+---------+                     +--------+                              +---------------------+
     |                              |                                              |
     |  Start import                |                                              |
     |----------------------------->|                                              |
     |                              |                                              |
     |                              |  Download source data                        |
     |                              |--------------------------------------------->|
     |                              |                        Begin streaming data  |
     |                              |<---------------------------------------------|
     |                              |                                              |
     |  Get import progress         |                                              |
     |----------------------------->|                                              |
     |       "status": "importing"  |                                              |
     |<-----------------------------|                                              |
     |                              |                                              |
     |  Get commit authors          |                                              |
     |----------------------------->|                                              |
     |                              |                                              |
     |  Map a commit author         |                                              |
     |----------------------------->|                                              |
     |                              |                                              |
     |                              |                                              |
     |                              |                       Finish streaming data  |
     |                              |<---------------------------------------------|
     |                              |                                              |
     |                              |  Rewrite commits with mapped authors         |
     |                              |------+                                       |
     |                              |      |                                       |
     |                              |<-----+                                       |
     |                              |                                              |
     |                              |  Update repository on GitHub                 |
     |                              |------+                                       |
     |                              |      |                                       |
     |                              |<-----+                                       |
     |                              |                                              |
     |  Map a commit author         |                                              |
     |----------------------------->|                                              |
     |                              |  Rewrite commits with mapped authors         |
     |                              |------+                                       |
     |                              |      |                                       |
     |                              |<-----+                                       |
     |                              |                                              |
     |                              |  Update repository on GitHub                 |
     |                              |------+                                       |
     |                              |      |                                       |
     |                              |<-----+                                       |
     |                              |                                              |
     |  Get large files             |                                              |
     |----------------------------->|                                              |
     |                              |                                              |
     |  opt_in to Git LFS           |                                              |
     |----------------------------->|                                              |
     |                              |  Rewrite commits for large files             |
     |                              |------+                                       |
     |                              |      |                                       |
     |                              |<-----+                                       |
     |                              |                                              |
     |                              |  Update repository on GitHub                 |
     |                              |------+                                       |
     |                              |      |                                       |
     |                              |<-----+                                       |
     |                              |                                              |
     |  Get import progress         |                                              |
     |----------------------------->|                                              |
     |        "status": "complete"  |                                              |
     |<-----------------------------|                                              |
     |                              |                                              |
     |                              |                                              |
```

## Get an import status
View the progress of an import.
Warning
Endpoint closing down notice:Due to very low levels of usage and available alternatives, this endpoint is closing down and will no longer be available from 00:00 UTC on April 12, 2024. For more details and alternatives, see thechangelog.
Import status
This section includes details about the possible values of thestatusfield of the Import Progress response.
An import that does not have errors will progress through these steps:
- detecting- the "detection" step of the import is in progress because the request did not include avcsparameter. The import is identifying the type of source control present at the URL.
- importing- the "raw" step of the import is in progress. This is where commit data is fetched from the original repository. The import progress response will includecommit_count(the total number of raw commits that will be imported) andpercent(0 - 100, the current progress through the import).
- mapping- the "rewrite" step of the import is in progress. This is where SVN branches are converted to Git branches, and where author updates are applied. The import progress response does not include progress information.
- pushing- the "push" step of the import is in progress. This is where the importer updates the repository on GitHub. The import progress response will includepush_percent, which is the percent value reported bygit pushwhen it is "Writing objects".
- complete- the import is complete, and the repository is ready on GitHub.
If there are problems, you will see one of these in thestatusfield:
- auth_failed- the import requires authentication in order to connect to the original repository. To update authentication for the import, please see theUpdate an importsection.
- error- the import encountered an error. The import progress response will include thefailed_stepand an error message. ContactGitHub Supportfor more information.
- detection_needs_auth- the importer requires authentication for the originating repository to continue detection. To update authentication for the import, please see theUpdate an importsection.
- detection_found_nothing- the importer didn't recognize any source control at the URL. To resolve,Cancel the importandretrywith the correct URL.
- detection_found_multiple- the importer found several projects or repositories at the provided URL. When this is the case, the Import Progress response will also include aproject_choicesfield with the possible project choices as values. To update project choice, please see theUpdate an importsection.
The project_choices field
When multiple projects are found at the provided URL, the response hash will include aproject_choicesfield, the value of which is an array of hashes each representing a project choice. The exact key/value pairs of the project hashes will differ depending on the version control type.
Git LFS related fields
This section includes details about Git LFS related fields that may be present in the Import Progress response.
- use_lfs- describes whether the import has been opted in or out of using Git LFS. The value can beopt_in,opt_out, orundecidedif no action has been taken.
- has_large_files- the boolean value describing whether files larger than 100MB were found during theimportingstep.
- large_files_size- the total size in gigabytes of files larger than 100MB found in the originating repository.
- large_files_count- the total number of files larger than 100MB found in the originating repository. To see a list of these files, make a "Get Large Files" request.

### Fine-grained access tokens for "Get an import status"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Contents" repository permissions (read)

### Parameters for "Get an import status"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.

### HTTP response status codes for "Get an import status"

[TABLE]
Status code | Description
200 | OK
404 | Resource not found
503 | Unavailable due to service under maintenance.
[/TABLE]
OK
Resource not found
Unavailable due to service under maintenance.

### Code samples for "Get an import status"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/import
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "vcs": "subversion",
  "use_lfs": true,
  "vcs_url": "http://svn.mycompany.com/svn/myproject",
  "status": "complete",
  "status_text": "Done",
  "has_large_files": true,
  "large_files_size": 132331036,
  "large_files_count": 1,
  "authors_count": 4,
  "url": "https://api.github.com/repos/octocat/socm/import",
  "html_url": "https://import.github.com/octocat/socm/import",
  "authors_url": "https://api.github.com/repos/octocat/socm/import/authors",
  "repository_url": "https://api.github.com/repos/octocat/socm"
}
```

## Start an import
Start a source import to a GitHub repository using GitHub Importer.
Importing into a GitHub repository with GitHub Actions enabled is not supported and will
return a status422 Unprocessable Entityresponse.
Warning
Endpoint closing down notice:Due to very low levels of usage and available alternatives, this endpoint is closing down and will no longer be available from 00:00 UTC on April 12, 2024. For more details and alternatives, see thechangelog.

### Fine-grained access tokens for "Start an import"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Contents" repository permissions (write)

### Parameters for "Start an import"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.

[TABLE]
Name, Type, Description
vcs_urlstringRequiredThe URL of the originating repository.
vcsstringThe originating VCS type. Without this parameter, the import job will take additional time to detect the VCS type before beginning the import. This detection step will be reflected in the response.Can be one of:subversion,git,mercurial,tfvc
vcs_usernamestringIf authentication is required, the username to provide tovcs_url.
vcs_passwordstringIf authentication is required, the password to provide tovcs_url.
tfvc_projectstringFor a tfvc import, the name of the project that is being imported.
[/TABLE]
The URL of the originating repository.
The originating VCS type. Without this parameter, the import job will take additional time to detect the VCS type before beginning the import. This detection step will be reflected in the response.
Can be one of:subversion,git,mercurial,tfvc

```
vcs_username
```
If authentication is required, the username to provide tovcs_url.

```
vcs_password
```
If authentication is required, the password to provide tovcs_url.

```
tfvc_project
```
For a tfvc import, the name of the project that is being imported.

### HTTP response status codes for "Start an import"

[TABLE]
Status code | Description
201 | Created
404 | Resource not found
422 | Validation failed, or the endpoint has been spammed.
503 | Unavailable due to service under maintenance.
[/TABLE]
Created
Resource not found
Validation failed, or the endpoint has been spammed.
Unavailable due to service under maintenance.

### Code samples for "Start an import"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -X PUT \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/import \
  -d '{"vcs":"subversion","vcs_url":"http://svn.mycompany.com/svn/myproject","vcs_username":"octocat","vcs_password":"secret"}'
```

#### Response
- Example response
- Response schema

```
Status: 201
```

```
{
  "vcs": "subversion",
  "use_lfs": true,
  "vcs_url": "http://svn.mycompany.com/svn/myproject",
  "status": "importing",
  "status_text": "Importing...",
  "has_large_files": false,
  "large_files_size": 0,
  "large_files_count": 0,
  "authors_count": 0,
  "commit_count": 1042,
  "url": "https://api.github.com/repos/octocat/socm/import",
  "html_url": "https://import.github.com/octocat/socm/import",
  "authors_url": "https://api.github.com/repos/octocat/socm/import/authors",
  "repository_url": "https://api.github.com/repos/octocat/socm"
}
```

## Update an import
An import can be updated with credentials or a project choice by passing in the appropriate parameters in this API
request. If no parameters are provided, the import will be restarted.
Some servers (e.g. TFS servers) can have several projects at a single URL. In those cases the import progress will
have the statusdetection_found_multipleand the Import Progress response will include aproject_choicesarray.
You can select the project to import by providing one of the objects in theproject_choicesarray in the update request.
Warning
Endpoint closing down notice:Due to very low levels of usage and available alternatives, this endpoint is closing down and will no longer be available from 00:00 UTC on April 12, 2024. For more details and alternatives, see thechangelog.

### Fine-grained access tokens for "Update an import"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Contents" repository permissions (write)

### Parameters for "Update an import"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.

[TABLE]
Name, Type, Description
vcs_usernamestringThe username to provide to the originating repository.
vcs_passwordstringThe password to provide to the originating repository.
vcsstringThe type of version control system you are migrating from.Can be one of:subversion,tfvc,git,mercurial
tfvc_projectstringFor a tfvc import, the name of the project that is being imported.
[/TABLE]

```
vcs_username
```
The username to provide to the originating repository.

```
vcs_password
```
The password to provide to the originating repository.
The type of version control system you are migrating from.
Can be one of:subversion,tfvc,git,mercurial

```
tfvc_project
```
For a tfvc import, the name of the project that is being imported.

### HTTP response status codes for "Update an import"

[TABLE]
Status code | Description
200 | OK
503 | Unavailable due to service under maintenance.
[/TABLE]
OK
Unavailable due to service under maintenance.

### Code samples for "Update an import"

#### Request examples
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -X PATCH \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/import \
  -d '{"vcs_username":"octocat","vcs_password":"secret"}'
```

#### Example 1
- Example response
- Response schema

```
Status: 200
```

```
{
  "vcs": "subversion",
  "use_lfs": true,
  "vcs_url": "http://svn.mycompany.com/svn/myproject",
  "status": "detecting",
  "url": "https://api.github.com/repos/octocat/socm/import",
  "html_url": "https://import.github.com/octocat/socm/import",
  "authors_url": "https://api.github.com/repos/octocat/socm/import/authors",
  "repository_url": "https://api.github.com/repos/octocat/socm"
}
```

## Cancel an import
Stop an import for a repository.
Warning
Endpoint closing down notice:Due to very low levels of usage and available alternatives, this endpoint is closing down and will no longer be available from 00:00 UTC on April 12, 2024. For more details and alternatives, see thechangelog.

### Fine-grained access tokens for "Cancel an import"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Contents" repository permissions (write)

### Parameters for "Cancel an import"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.

### HTTP response status codes for "Cancel an import"

[TABLE]
Status code | Description
204 | No Content
503 | Unavailable due to service under maintenance.
[/TABLE]
No Content
Unavailable due to service under maintenance.

### Code samples for "Cancel an import"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -X DELETE \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/import
```

#### Response

```
Status: 204
```

## Get commit authors
Each type of source control system represents authors in a different way. For example, a Git commit author has a display name and an email address, but a Subversion commit author just has a username. The GitHub Importer will make the author information valid, but the author might not be correct. For example, it will change the bare Subversion usernamehubotinto something likehubot <hubot@12341234-abab-fefe-8787-fedcba987654>.
This endpoint and theMap a commit authorendpoint allow you to provide correct Git author information.
Warning
Endpoint closing down notice:Due to very low levels of usage and available alternatives, this endpoint is closing down and will no longer be available from 00:00 UTC on April 12, 2024. For more details and alternatives, see thechangelog.

### Fine-grained access tokens for "Get commit authors"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Contents" repository permissions (read)

### Parameters for "Get commit authors"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.

[TABLE]
Name, Type, Description
sinceintegerA user ID. Only return users with an ID greater than this ID.
[/TABLE]
A user ID. Only return users with an ID greater than this ID.

### HTTP response status codes for "Get commit authors"

[TABLE]
Status code | Description
200 | OK
404 | Resource not found
503 | Unavailable due to service under maintenance.
[/TABLE]
OK
Resource not found
Unavailable due to service under maintenance.

### Code samples for "Get commit authors"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/import/authors
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
[
  {
    "id": 2268557,
    "remote_id": "nobody@fc7da526-431c-80fe-3c8c-c148ff18d7ef",
    "remote_name": "nobody",
    "email": "hubot@github.com",
    "name": "Hubot",
    "url": "https://api.github.com/repos/octocat/socm/import/authors/2268557",
    "import_url": "https://api.github.com/repos/octocat/socm/import"
  },
  {
    "id": 2268558,
    "remote_id": "svner@fc7da526-431c-80fe-3c8c-c148ff18d7ef",
    "remote_name": "svner",
    "email": "svner@fc7da526-431c-80fe-3c8c-c148ff18d7ef",
    "name": "svner",
    "url": "https://api.github.com/repos/octocat/socm/import/authors/2268558",
    "import_url": "https://api.github.com/repos/octocat/socm/import"
  },
  {
    "id": 2268559,
    "remote_id": "svner@example.com@fc7da526-431c-80fe-3c8c-c148ff18d7ef",
    "remote_name": "svner@example.com",
    "email": "svner@example.com@fc7da526-431c-80fe-3c8c-c148ff18d7ef",
    "name": "svner@example.com",
    "url": "https://api.github.com/repos/octocat/socm/import/authors/2268559",
    "import_url": "https://api.github.com/repos/octocat/socm/import"
  }
]
```

## Map a commit author
Update an author's identity for the import. Your application can continue updating authors any time before you push
new commits to the repository.
Warning
Endpoint closing down notice:Due to very low levels of usage and available alternatives, this endpoint is closing down and will no longer be available from 00:00 UTC on April 12, 2024. For more details and alternatives, see thechangelog.

### Fine-grained access tokens for "Map a commit author"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Contents" repository permissions (write)

### Parameters for "Map a commit author"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
author_idintegerRequired
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.

[TABLE]
Name, Type, Description
emailstringThe new Git author email.
namestringThe new Git author name.
[/TABLE]
The new Git author email.
The new Git author name.

### HTTP response status codes for "Map a commit author"

[TABLE]
Status code | Description
200 | OK
404 | Resource not found
422 | Validation failed, or the endpoint has been spammed.
503 | Unavailable due to service under maintenance.
[/TABLE]
OK
Resource not found
Validation failed, or the endpoint has been spammed.
Unavailable due to service under maintenance.

### Code samples for "Map a commit author"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -X PATCH \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/import/authors/AUTHOR_ID \
  -d '{"email":"hubot@github.com","name":"Hubot the Robot"}'
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "id": 2268557,
  "remote_id": "nobody@fc7da526-431c-80fe-3c8c-c148ff18d7ef",
  "remote_name": "nobody",
  "email": "hubot@github.com",
  "name": "Hubot",
  "url": "https://api.github.com/repos/octocat/socm/import/authors/2268557",
  "import_url": "https://api.github.com/repos/octocat/socm/import"
}
```

## Get large files
List files larger than 100MB found during the import
Warning
Endpoint closing down notice:Due to very low levels of usage and available alternatives, this endpoint is closing down and will no longer be available from 00:00 UTC on April 12, 2024. For more details and alternatives, see thechangelog.

### Fine-grained access tokens for "Get large files"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Contents" repository permissions (read)

### Parameters for "Get large files"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.

### HTTP response status codes for "Get large files"

[TABLE]
Status code | Description
200 | OK
503 | Unavailable due to service under maintenance.
[/TABLE]
OK
Unavailable due to service under maintenance.

### Code samples for "Get large files"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/import/large_files
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
[
  {
    "ref_name": "refs/heads/master",
    "path": "foo/bar/1",
    "oid": "d3d9446802a44259755d38e6d163e820",
    "size": 10485760
  },
  {
    "ref_name": "refs/heads/master",
    "path": "foo/bar/2",
    "oid": "6512bd43d9caa6e02c990b0a82652dca",
    "size": 11534336
  },
  {
    "ref_name": "refs/heads/master",
    "path": "foo/bar/3",
    "oid": "c20ad4d76fe97759aa27a0c99bff6710",
    "size": 12582912
  }
]
```

## Update Git LFS preference
You can import repositories from Subversion, Mercurial, and TFS that include files larger than 100MB. This ability
is powered byGit LFS.
You can learn more about our LFS feature and working with large fileson our help
site.
Warning
Endpoint closing down notice:Due to very low levels of usage and available alternatives, this endpoint is closing down and will no longer be available from 00:00 UTC on April 12, 2024. For more details and alternatives, see thechangelog.

### Fine-grained access tokens for "Update Git LFS preference"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Contents" repository permissions (write)

### Parameters for "Update Git LFS preference"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.

[TABLE]
Name, Type, Description
use_lfsstringRequiredWhether to store large files during the import.opt_inmeans large files will be stored using Git LFS.opt_outmeans large files will be removed during the import.Can be one of:opt_in,opt_out
[/TABLE]
Whether to store large files during the import.opt_inmeans large files will be stored using Git LFS.opt_outmeans large files will be removed during the import.
Can be one of:opt_in,opt_out

### HTTP response status codes for "Update Git LFS preference"

[TABLE]
Status code | Description
200 | OK
422 | Validation failed, or the endpoint has been spammed.
503 | Unavailable due to service under maintenance.
[/TABLE]
OK
Validation failed, or the endpoint has been spammed.
Unavailable due to service under maintenance.

### Code samples for "Update Git LFS preference"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -X PATCH \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/import/lfs \
  -d '{"use_lfs":"opt_in"}'
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "vcs": "subversion",
  "use_lfs": true,
  "vcs_url": "http://svn.mycompany.com/svn/myproject",
  "status": "complete",
  "status_text": "Done",
  "has_large_files": true,
  "large_files_size": 132331036,
  "large_files_count": 1,
  "authors_count": 4,
  "url": "https://api.github.com/repos/octocat/socm/import",
  "html_url": "https://import.github.com/octocat/socm/import",
  "authors_url": "https://api.github.com/repos/octocat/socm/import/authors",
  "repository_url": "https://api.github.com/repos/octocat/socm"
}
```