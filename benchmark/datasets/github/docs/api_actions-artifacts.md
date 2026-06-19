# REST API endpoints for GitHub Actions artifacts

*Source: https://docs.github.com/en/rest/actions/artifacts*

---

# REST API endpoints for GitHub Actions artifacts
Use the REST API to interact with artifacts in GitHub Actions.

## About artifacts in GitHub Actions
You can use the REST API to download, delete, and retrieve information about workflow artifacts in GitHub Actions. Artifacts enable you to share data between jobs in a workflow and store data once that workflow has completed. For more information, seeStore and share data with workflow artifacts.

## List artifacts for a repository
Lists all artifacts for a repository.
Anyone with read access to the repository can use this endpoint.
OAuth app tokens and personal access tokens (classic) need thereposcope to use this endpoint with a private repository.

### Fine-grained access tokens for "List artifacts for a repository"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Actions" repository permissions (read)
This endpoint can be used without authentication or the aforementioned permissions if only public resources are requested.

### Parameters for "List artifacts for a repository"

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
per_pageintegerThe number of results per page (max 100). For more information, see "Using pagination in the REST API."Default:30
pageintegerThe page number of the results to fetch. For more information, see "Using pagination in the REST API."Default:1
namestringThe name field of an artifact. When specified, only artifacts with this name will be returned.
[/TABLE]
The number of results per page (max 100). For more information, see "Using pagination in the REST API."
Default:30
The page number of the results to fetch. For more information, see "Using pagination in the REST API."
Default:1
The name field of an artifact. When specified, only artifacts with this name will be returned.

### HTTP response status codes for "List artifacts for a repository"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "List artifacts for a repository"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/actions/artifacts
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "total_count": 2,
  "artifacts": [
    {
      "id": 11,
      "node_id": "MDg6QXJ0aWZhY3QxMQ==",
      "name": "Rails",
      "size_in_bytes": 556,
      "url": "https://api.github.com/repos/octo-org/octo-docs/actions/artifacts/11",
      "archive_download_url": "https://api.github.com/repos/octo-org/octo-docs/actions/artifacts/11/zip",
      "expired": false,
      "created_at": "2020-01-10T14:59:22Z",
      "expires_at": "2020-03-21T14:59:22Z",
      "updated_at": "2020-02-21T14:59:22Z",
      "digest": "sha256:cfc3236bdad15b5898bca8408945c9e19e1917da8704adc20eaa618444290a8c",
      "workflow_run": {
        "id": 2332938,
        "repository_id": 1296269,
        "head_repository_id": 1296269,
        "head_branch": "main",
        "head_sha": "328faa0536e6fef19753d9d91dc96a9931694ce3"
      }
    },
    {
      "id": 13,
      "node_id": "MDg6QXJ0aWZhY3QxMw==",
      "name": "Test output",
      "size_in_bytes": 453,
      "url": "https://api.github.com/repos/octo-org/octo-docs/actions/artifacts/13",
      "archive_download_url": "https://api.github.com/repos/octo-org/octo-docs/actions/artifacts/13/zip",
      "expired": false,
      "created_at": "2020-01-10T14:59:22Z",
      "expires_at": "2020-03-21T14:59:22Z",
      "updated_at": "2020-02-21T14:59:22Z",
      "digest": "sha256:cfc3236bdad15b5898bca8408945c9e19e1917da8704adc20eaa618444290a8c",
      "workflow_run": {
        "id": 2332942,
        "repository_id": 1296269,
        "head_repository_id": 1296269,
        "head_branch": "main",
        "head_sha": "178f4f6090b3fccad4a65b3e83d076a622d59652"
      }
    }
  ]
}
```

## Get an artifact
Gets a specific artifact for a workflow run.
Anyone with read access to the repository can use this endpoint.
If the repository is private, OAuth tokens and personal access tokens (classic) need thereposcope to use this endpoint.

### Fine-grained access tokens for "Get an artifact"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Actions" repository permissions (read)
This endpoint can be used without authentication or the aforementioned permissions if only public resources are requested.

### Parameters for "Get an artifact"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
artifact_idintegerRequiredThe unique identifier of the artifact.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.

```
artifact_id
```
The unique identifier of the artifact.

### HTTP response status codes for "Get an artifact"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "Get an artifact"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/actions/artifacts/ARTIFACT_ID
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "id": 11,
  "node_id": "MDg6QXJ0aWZhY3QxMQ==",
  "name": "Rails",
  "size_in_bytes": 556,
  "url": "https://api.github.com/repos/octo-org/octo-docs/actions/artifacts/11",
  "archive_download_url": "https://api.github.com/repos/octo-org/octo-docs/actions/artifacts/11/zip",
  "expired": false,
  "created_at": "2020-01-10T14:59:22Z",
  "expires_at": "2020-01-21T14:59:22Z",
  "updated_at": "2020-01-21T14:59:22Z",
  "digest": "sha256:cfc3236bdad15b5898bca8408945c9e19e1917da8704adc20eaa618444290a8c",
  "workflow_run": {
    "id": 2332938,
    "repository_id": 1296269,
    "head_repository_id": 1296269,
    "head_branch": "main",
    "head_sha": "328faa0536e6fef19753d9d91dc96a9931694ce3"
  }
}
```

## Delete an artifact
Deletes an artifact for a workflow run.
OAuth tokens and personal access tokens (classic) need thereposcope to use this endpoint.

### Fine-grained access tokens for "Delete an artifact"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Actions" repository permissions (write)

### Parameters for "Delete an artifact"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
artifact_idintegerRequiredThe unique identifier of the artifact.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.

```
artifact_id
```
The unique identifier of the artifact.

### HTTP response status codes for "Delete an artifact"

[TABLE]
Status code | Description
204 | No Content
[/TABLE]
No Content

### Code samples for "Delete an artifact"

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
  https://api.github.com/repos/OWNER/REPO/actions/artifacts/ARTIFACT_ID
```

#### Response

```
Status: 204
```

## Download an artifact
Gets a redirect URL to download an archive for a repository. This URL expires after 1 minute. Look forLocation:in
the response header to find the URL for the download. The:archive_formatmust bezip.
OAuth tokens and personal access tokens (classic) need thereposcope to use this endpoint.

### Fine-grained access tokens for "Download an artifact"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Actions" repository permissions (read)

### Parameters for "Download an artifact"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
artifact_idintegerRequiredThe unique identifier of the artifact.
archive_formatstringRequired
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.

```
artifact_id
```
The unique identifier of the artifact.

```
archive_format
```

### HTTP response status codes for "Download an artifact"

[TABLE]
Status code | Description
302 | Found
410 | Gone
[/TABLE]
Found
Gone

### Code samples for "Download an artifact"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/actions/artifacts/ARTIFACT_ID/ARCHIVE_FORMAT
```

#### Response

```
Status: 302
```

## List workflow run artifacts
Lists artifacts for a workflow run.
Anyone with read access to the repository can use this endpoint.
OAuth app tokens and personal access tokens (classic) need thereposcope to use this endpoint with a private repository.

### Fine-grained access tokens for "List workflow run artifacts"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Actions" repository permissions (read)
This endpoint can be used without authentication or the aforementioned permissions if only public resources are requested.

### Parameters for "List workflow run artifacts"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
run_idintegerRequiredThe unique identifier of the workflow run.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.
The unique identifier of the workflow run.

[TABLE]
Name, Type, Description
per_pageintegerThe number of results per page (max 100). For more information, see "Using pagination in the REST API."Default:30
pageintegerThe page number of the results to fetch. For more information, see "Using pagination in the REST API."Default:1
namestringThe name field of an artifact. When specified, only artifacts with this name will be returned.
directionstringThe direction to sort the results by.Default:descCan be one of:asc,desc
[/TABLE]
The number of results per page (max 100). For more information, see "Using pagination in the REST API."
Default:30
The page number of the results to fetch. For more information, see "Using pagination in the REST API."
Default:1
The name field of an artifact. When specified, only artifacts with this name will be returned.
The direction to sort the results by.
Default:desc
Can be one of:asc,desc

### HTTP response status codes for "List workflow run artifacts"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "List workflow run artifacts"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/actions/runs/RUN_ID/artifacts
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "total_count": 2,
  "artifacts": [
    {
      "id": 11,
      "node_id": "MDg6QXJ0aWZhY3QxMQ==",
      "name": "Rails",
      "size_in_bytes": 556,
      "url": "https://api.github.com/repos/octo-org/octo-docs/actions/artifacts/11",
      "archive_download_url": "https://api.github.com/repos/octo-org/octo-docs/actions/artifacts/11/zip",
      "expired": false,
      "created_at": "2020-01-10T14:59:22Z",
      "expires_at": "2020-03-21T14:59:22Z",
      "updated_at": "2020-02-21T14:59:22Z",
      "digest": "sha256:cfc3236bdad15b5898bca8408945c9e19e1917da8704adc20eaa618444290a8c",
      "workflow_run": {
        "id": 2332938,
        "repository_id": 1296269,
        "head_repository_id": 1296269,
        "head_branch": "main",
        "head_sha": "328faa0536e6fef19753d9d91dc96a9931694ce3"
      }
    },
    {
      "id": 13,
      "node_id": "MDg6QXJ0aWZhY3QxMw==",
      "name": "Test output",
      "size_in_bytes": 453,
      "url": "https://api.github.com/repos/octo-org/octo-docs/actions/artifacts/13",
      "archive_download_url": "https://api.github.com/repos/octo-org/octo-docs/actions/artifacts/13/zip",
      "expired": false,
      "created_at": "2020-01-10T14:59:22Z",
      "expires_at": "2020-03-21T14:59:22Z",
      "updated_at": "2020-02-21T14:59:22Z",
      "digest": "sha256:cfc3236bdad15b5898bca8408945c9e19e1917da8704adc20eaa618444290a8c",
      "workflow_run": {
        "id": 2332942,
        "repository_id": 1296269,
        "head_repository_id": 1296269,
        "head_branch": "main",
        "head_sha": "178f4f6090b3fccad4a65b3e83d076a622d59652"
      }
    }
  ]
}
```