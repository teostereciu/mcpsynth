# REST API endpoints for self-hosted runners

*Source: https://docs.github.com/en/rest/actions/self-hosted-runners*

---

# REST API endpoints for self-hosted runners
Use the REST API to interact with self-hosted runners in GitHub Actions.

## About self-hosted runners in GitHub Actions
You can use the REST API to register, view, and delete self-hosted runners in GitHub Actions. Self-hosted runners allow you to host your own runners and customize the environment used to run jobs in your GitHub Actions workflows. For more information, seeManaging self-hosted runners.

## List self-hosted runners for an organization
Lists all self-hosted runners configured in an organization.
Authenticated users must have admin access to the organization to use this endpoint.
OAuth app tokens and personal access tokens (classic) need theadmin:orgscope to use this endpoint. If the repository is private, thereposcope is also required.

### Fine-grained access tokens for "List self-hosted runners for an organization"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Self-hosted runners" organization permissions (read)

### Parameters for "List self-hosted runners for an organization"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
[/TABLE]
The organization name. The name is not case sensitive.

[TABLE]
Name, Type, Description
namestringThe name of a self-hosted runner.
per_pageintegerThe number of results per page (max 100). For more information, see "Using pagination in the REST API."Default:30
pageintegerThe page number of the results to fetch. For more information, see "Using pagination in the REST API."Default:1
[/TABLE]
The name of a self-hosted runner.
The number of results per page (max 100). For more information, see "Using pagination in the REST API."
Default:30
The page number of the results to fetch. For more information, see "Using pagination in the REST API."
Default:1

### HTTP response status codes for "List self-hosted runners for an organization"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "List self-hosted runners for an organization"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/orgs/ORG/actions/runners
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
  "runners": [
    {
      "id": 23,
      "name": "linux_runner",
      "os": "linux",
      "status": "online",
      "busy": true,
      "ephemeral": false,
      "labels": [
        {
          "id": 5,
          "name": "self-hosted",
          "type": "read-only"
        },
        {
          "id": 7,
          "name": "X64",
          "type": "read-only"
        },
        {
          "id": 11,
          "name": "Linux",
          "type": "read-only"
        }
      ]
    },
    {
      "id": 24,
      "name": "mac_runner",
      "os": "macos",
      "status": "offline",
      "busy": false,
      "ephemeral": false,
      "labels": [
        {
          "id": 5,
          "name": "self-hosted",
          "type": "read-only"
        },
        {
          "id": 7,
          "name": "X64",
          "type": "read-only"
        },
        {
          "id": 20,
          "name": "macOS",
          "type": "read-only"
        },
        {
          "id": 21,
          "name": "no-gpu",
          "type": "custom"
        }
      ]
    }
  ]
}
```

## List runner applications for an organization
Lists binaries for the runner application that you can download and run.
Authenticated users must have admin access to the organization to use this endpoint.
OAuth app tokens and personal access tokens (classic) need theadmin:orgscope to use this endpoint.  If the repository is private, thereposcope is also required.

### Fine-grained access tokens for "List runner applications for an organization"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Self-hosted runners" organization permissions (read)

### Parameters for "List runner applications for an organization"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
[/TABLE]
The organization name. The name is not case sensitive.

### HTTP response status codes for "List runner applications for an organization"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "List runner applications for an organization"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/orgs/ORG/actions/runners/downloads
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
    "os": "osx",
    "architecture": "x64",
    "download_url": "https://github.com/actions/runner/releases/download/v2.164.0/actions-runner-osx-x64-2.164.0.tar.gz",
    "filename": "actions-runner-osx-x64-2.164.0.tar.gz"
  },
  {
    "os": "linux",
    "architecture": "x64",
    "download_url": "https://github.com/actions/runner/releases/download/v2.164.0/actions-runner-linux-x64-2.164.0.tar.gz",
    "filename": "actions-runner-linux-x64-2.164.0.tar.gz"
  },
  {
    "os": "linux",
    "architecture": "arm",
    "download_url": "https://github.com/actions/runner/releases/download/v2.164.0/actions-runner-linux-arm-2.164.0.tar.gz",
    "filename": "actions-runner-linux-arm-2.164.0.tar.gz"
  },
  {
    "os": "win",
    "architecture": "x64",
    "download_url": "https://github.com/actions/runner/releases/download/v2.164.0/actions-runner-win-x64-2.164.0.zip",
    "filename": "actions-runner-win-x64-2.164.0.zip"
  },
  {
    "os": "linux",
    "architecture": "arm64",
    "download_url": "https://github.com/actions/runner/releases/download/v2.164.0/actions-runner-linux-arm64-2.164.0.tar.gz",
    "filename": "actions-runner-linux-arm64-2.164.0.tar.gz"
  }
]
```

## Create configuration for a just-in-time runner for an organization
Generates a configuration that can be passed to the runner application at startup.
The authenticated user must have admin access to the organization.
OAuth tokens and personal access tokens (classic) need theadmin:orgscope to use this endpoint. If the repository is private, OAuth tokens and personal access tokens (classic) need thereposcope to use this endpoint.

### Fine-grained access tokens for "Create configuration for a just-in-time runner for an organization"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Self-hosted runners" organization permissions (write)

### Parameters for "Create configuration for a just-in-time runner for an organization"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
[/TABLE]
The organization name. The name is not case sensitive.

[TABLE]
Name, Type, Description
namestringRequiredThe name of the new runner.
runner_group_idintegerRequiredThe ID of the runner group to register the runner to.
labelsarray of stringsRequiredThe names of the custom labels to add to the runner.Minimum items: 1.Maximum items: 100.
work_folderstringThe working directory to be used for job execution, relative to the runner install directory.Default:_work
[/TABLE]
The name of the new runner.

```
runner_group_id
```
The ID of the runner group to register the runner to.
The names of the custom labels to add to the runner.Minimum items: 1.Maximum items: 100.

```
work_folder
```
The working directory to be used for job execution, relative to the runner install directory.
Default:_work

### HTTP response status codes for "Create configuration for a just-in-time runner for an organization"

[TABLE]
Status code | Description
201 | Created
404 | Resource not found
409 | Conflict
422 | Validation failed, or the endpoint has been spammed.
[/TABLE]
Created
Resource not found
Conflict
Validation failed, or the endpoint has been spammed.

### Code samples for "Create configuration for a just-in-time runner for an organization"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -X POST \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/orgs/ORG/actions/runners/generate-jitconfig \
  -d '{"name":"New runner","runner_group_id":1,"labels":["self-hosted","X64","macOS","no-gpu"],"work_folder":"_work"}'
```

#### Response
- Example response
- Response schema

```
Status: 201
```

```
{
  "runner": {
    "id": 23,
    "name": "New runner",
    "os": "unknown",
    "status": "offline",
    "busy": false,
    "labels": [
      {
        "id": 5,
        "name": "self-hosted",
        "type": "read-only"
      },
      {
        "id": 7,
        "name": "X64",
        "type": "read-only"
      },
      {
        "id": 20,
        "name": "macOS",
        "type": "read-only"
      },
      {
        "id": 21,
        "name": "no-gpu",
        "type": "custom"
      }
    ]
  },
  "encoded_jit_config": "abc123"
}
```

## Create a registration token for an organization
Returns a token that you can pass to theconfigscript. The token expires after one hour.
For example, you can replaceTOKENin the following example with the registration token provided by this endpoint to configure your self-hosted runner:

```
./config.sh --url https://github.com/octo-org --token TOKEN
```

```
./config.sh --url https://github.com/octo-org --token TOKEN
```
Authenticated users must have admin access to the organization to use this endpoint.
OAuth tokens and personal access tokens (classic) need theadmin:orgscope to use this endpoint. If the repository is private, OAuth tokens and personal access tokens (classic) need thereposcope to use this endpoint.

### Fine-grained access tokens for "Create a registration token for an organization"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Self-hosted runners" organization permissions (write)

### Parameters for "Create a registration token for an organization"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
[/TABLE]
The organization name. The name is not case sensitive.

### HTTP response status codes for "Create a registration token for an organization"

[TABLE]
Status code | Description
201 | Created
[/TABLE]
Created

### Code samples for "Create a registration token for an organization"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -X POST \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/orgs/ORG/actions/runners/registration-token
```

#### Response
- Example response
- Response schema

```
Status: 201
```

```
{
  "token": "LLBF3JGZDX3P5PMEXLND6TS6FCWO6",
  "expires_at": "2020-01-22T12:13:35.123-08:00"
}
```

## Create a remove token for an organization
Returns a token that you can pass to theconfigscript to remove a self-hosted runner from an organization. The token expires after one hour.
For example, you can replaceTOKENin the following example with the registration token provided by this endpoint to remove your self-hosted runner from an organization:

```
./config.sh remove --token TOKEN
```

```
./config.sh remove --token TOKEN
```
Authenticated users must have admin access to the organization to use this endpoint.
OAuth tokens and personal access tokens (classic) need theadmin:orgscope to use this endpoint. If the repository is private, OAuth tokens and personal access tokens (classic) need thereposcope to use this endpoint.

### Fine-grained access tokens for "Create a remove token for an organization"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Self-hosted runners" organization permissions (write)

### Parameters for "Create a remove token for an organization"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
[/TABLE]
The organization name. The name is not case sensitive.

### HTTP response status codes for "Create a remove token for an organization"

[TABLE]
Status code | Description
201 | Created
[/TABLE]
Created

### Code samples for "Create a remove token for an organization"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -X POST \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/orgs/ORG/actions/runners/remove-token
```

#### Response
- Example response
- Response schema

```
Status: 201
```

```
{
  "token": "AABF3JGZDX3P5PMEXLND6TS6FCWO6",
  "expires_at": "2020-01-29T12:13:35.123-08:00"
}
```

## Get a self-hosted runner for an organization
Gets a specific self-hosted runner configured in an organization.
Authenticated users must have admin access to the organization to use this endpoint.
OAuth app tokens and personal access tokens (classic) need theadmin:orgscope to use this endpoint. If the repository is private, thereposcope is also required.

### Fine-grained access tokens for "Get a self-hosted runner for an organization"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Self-hosted runners" organization permissions (read)

### Parameters for "Get a self-hosted runner for an organization"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
runner_idintegerRequiredUnique identifier of the self-hosted runner.
[/TABLE]
The organization name. The name is not case sensitive.
Unique identifier of the self-hosted runner.

### HTTP response status codes for "Get a self-hosted runner for an organization"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "Get a self-hosted runner for an organization"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/orgs/ORG/actions/runners/RUNNER_ID
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "id": 23,
  "name": "MBP",
  "os": "macos",
  "status": "online",
  "busy": true,
  "ephemeral": false,
  "labels": [
    {
      "id": 5,
      "name": "self-hosted",
      "type": "read-only"
    },
    {
      "id": 7,
      "name": "X64",
      "type": "read-only"
    },
    {
      "id": 20,
      "name": "macOS",
      "type": "read-only"
    },
    {
      "id": 21,
      "name": "no-gpu",
      "type": "custom"
    }
  ]
}
```

## Delete a self-hosted runner from an organization
Forces the removal of a self-hosted runner from an organization. You can use this endpoint to completely remove the runner when the machine you were using no longer exists.
Authenticated users must have admin access to the organization to use this endpoint.
OAuth tokens and personal access tokens (classic) need theadmin:orgscope to use this endpoint. If the repository is private, OAuth tokens and personal access tokens (classic) need thereposcope to use this endpoint.

### Fine-grained access tokens for "Delete a self-hosted runner from an organization"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Self-hosted runners" organization permissions (write)

### Parameters for "Delete a self-hosted runner from an organization"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
runner_idintegerRequiredUnique identifier of the self-hosted runner.
[/TABLE]
The organization name. The name is not case sensitive.
Unique identifier of the self-hosted runner.

### HTTP response status codes for "Delete a self-hosted runner from an organization"

[TABLE]
Status code | Description
204 | No Content
422 | Validation failed, or the endpoint has been spammed.
[/TABLE]
No Content
Validation failed, or the endpoint has been spammed.

### Code samples for "Delete a self-hosted runner from an organization"

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
  https://api.github.com/orgs/ORG/actions/runners/RUNNER_ID
```

#### Response

```
Status: 204
```

## List labels for a self-hosted runner for an organization
Lists all labels for a self-hosted runner configured in an organization.
Authenticated users must have admin access to the organization to use this endpoint.
OAuth app tokens and personal access tokens (classic) need theadmin:orgscope to use this endpoint. If the repository is private, thereposcope is also required.

### Fine-grained access tokens for "List labels for a self-hosted runner for an organization"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Self-hosted runners" organization permissions (read)

### Parameters for "List labels for a self-hosted runner for an organization"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
runner_idintegerRequiredUnique identifier of the self-hosted runner.
[/TABLE]
The organization name. The name is not case sensitive.
Unique identifier of the self-hosted runner.

### HTTP response status codes for "List labels for a self-hosted runner for an organization"

[TABLE]
Status code | Description
200 | OK
404 | Resource not found
[/TABLE]
OK
Resource not found

### Code samples for "List labels for a self-hosted runner for an organization"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/orgs/ORG/actions/runners/RUNNER_ID/labels
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "total_count": 4,
  "labels": [
    {
      "id": 5,
      "name": "self-hosted",
      "type": "read-only"
    },
    {
      "id": 7,
      "name": "X64",
      "type": "read-only"
    },
    {
      "id": 20,
      "name": "macOS",
      "type": "read-only"
    },
    {
      "id": 21,
      "name": "no-gpu",
      "type": "custom"
    }
  ]
}
```

## Add custom labels to a self-hosted runner for an organization
Adds custom labels to a self-hosted runner configured in an organization.
Authenticated users must have admin access to the organization to use this endpoint.
OAuth tokens and personal access tokens (classic) need theadmin:orgscope to use this endpoint.

### Fine-grained access tokens for "Add custom labels to a self-hosted runner for an organization"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Self-hosted runners" organization permissions (write)

### Parameters for "Add custom labels to a self-hosted runner for an organization"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
runner_idintegerRequiredUnique identifier of the self-hosted runner.
[/TABLE]
The organization name. The name is not case sensitive.
Unique identifier of the self-hosted runner.

[TABLE]
Name, Type, Description
labelsarray of stringsRequiredThe names of the custom labels to add to the runner.
[/TABLE]
The names of the custom labels to add to the runner.

### HTTP response status codes for "Add custom labels to a self-hosted runner for an organization"

[TABLE]
Status code | Description
200 | OK
404 | Resource not found
422 | Validation failed, or the endpoint has been spammed.
[/TABLE]
OK
Resource not found
Validation failed, or the endpoint has been spammed.

### Code samples for "Add custom labels to a self-hosted runner for an organization"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -X POST \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/orgs/ORG/actions/runners/RUNNER_ID/labels \
  -d '{"labels":["gpu","accelerated"]}'
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "total_count": 4,
  "labels": [
    {
      "id": 5,
      "name": "self-hosted",
      "type": "read-only"
    },
    {
      "id": 7,
      "name": "X64",
      "type": "read-only"
    },
    {
      "id": 20,
      "name": "macOS",
      "type": "read-only"
    },
    {
      "id": 21,
      "name": "no-gpu",
      "type": "custom"
    }
  ]
}
```

## Set custom labels for a self-hosted runner for an organization
Remove all previous custom labels and set the new custom labels for a specific
self-hosted runner configured in an organization.
Authenticated users must have admin access to the organization to use this endpoint.
OAuth app tokens and personal access tokens (classic) need theadmin:orgscope to use this endpoint. If the repository is private, thereposcope is also required.

### Fine-grained access tokens for "Set custom labels for a self-hosted runner for an organization"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Self-hosted runners" organization permissions (write)

### Parameters for "Set custom labels for a self-hosted runner for an organization"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
runner_idintegerRequiredUnique identifier of the self-hosted runner.
[/TABLE]
The organization name. The name is not case sensitive.
Unique identifier of the self-hosted runner.

[TABLE]
Name, Type, Description
labelsarray of stringsRequiredThe names of the custom labels to set for the runner. You can pass an empty array to remove all custom labels.
[/TABLE]
The names of the custom labels to set for the runner. You can pass an empty array to remove all custom labels.

### HTTP response status codes for "Set custom labels for a self-hosted runner for an organization"

[TABLE]
Status code | Description
200 | OK
404 | Resource not found
422 | Validation failed, or the endpoint has been spammed.
[/TABLE]
OK
Resource not found
Validation failed, or the endpoint has been spammed.

### Code samples for "Set custom labels for a self-hosted runner for an organization"

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
  https://api.github.com/orgs/ORG/actions/runners/RUNNER_ID/labels \
  -d '{"labels":["gpu","accelerated"]}'
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "total_count": 4,
  "labels": [
    {
      "id": 5,
      "name": "self-hosted",
      "type": "read-only"
    },
    {
      "id": 7,
      "name": "X64",
      "type": "read-only"
    },
    {
      "id": 20,
      "name": "macOS",
      "type": "read-only"
    },
    {
      "id": 21,
      "name": "no-gpu",
      "type": "custom"
    }
  ]
}
```

## Remove all custom labels from a self-hosted runner for an organization
Remove all custom labels from a self-hosted runner configured in an
organization. Returns the remaining read-only labels from the runner.
Authenticated users must have admin access to the organization to use this endpoint.
OAuth app tokens and personal access tokens (classic) need theadmin:orgscope to use this endpoint. If the repository is private, thereposcope is also required.

### Fine-grained access tokens for "Remove all custom labels from a self-hosted runner for an organization"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Self-hosted runners" organization permissions (write)

### Parameters for "Remove all custom labels from a self-hosted runner for an organization"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
runner_idintegerRequiredUnique identifier of the self-hosted runner.
[/TABLE]
The organization name. The name is not case sensitive.
Unique identifier of the self-hosted runner.

### HTTP response status codes for "Remove all custom labels from a self-hosted runner for an organization"

[TABLE]
Status code | Description
200 | OK
404 | Resource not found
[/TABLE]
OK
Resource not found

### Code samples for "Remove all custom labels from a self-hosted runner for an organization"

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
  https://api.github.com/orgs/ORG/actions/runners/RUNNER_ID/labels
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "total_count": 3,
  "labels": [
    {
      "id": 5,
      "name": "self-hosted",
      "type": "read-only"
    },
    {
      "id": 7,
      "name": "X64",
      "type": "read-only"
    },
    {
      "id": 20,
      "name": "macOS",
      "type": "read-only"
    }
  ]
}
```

## Remove a custom label from a self-hosted runner for an organization
Remove a custom label from a self-hosted runner configured
in an organization. Returns the remaining labels from the runner.
This endpoint returns a404 Not Foundstatus if the custom label is not
present on the runner.
Authenticated users must have admin access to the organization to use this endpoint.
OAuth app tokens and personal access tokens (classic) need theadmin:orgscope to use this endpoint. If the repository is private, thereposcope is also required.

### Fine-grained access tokens for "Remove a custom label from a self-hosted runner for an organization"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Self-hosted runners" organization permissions (write)

### Parameters for "Remove a custom label from a self-hosted runner for an organization"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
runner_idintegerRequiredUnique identifier of the self-hosted runner.
namestringRequiredThe name of a self-hosted runner's custom label.
[/TABLE]
The organization name. The name is not case sensitive.
Unique identifier of the self-hosted runner.
The name of a self-hosted runner's custom label.

### HTTP response status codes for "Remove a custom label from a self-hosted runner for an organization"

[TABLE]
Status code | Description
200 | OK
404 | Resource not found
422 | Validation failed, or the endpoint has been spammed.
[/TABLE]
OK
Resource not found
Validation failed, or the endpoint has been spammed.

### Code samples for "Remove a custom label from a self-hosted runner for an organization"

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
  https://api.github.com/orgs/ORG/actions/runners/RUNNER_ID/labels/NAME
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "total_count": 4,
  "labels": [
    {
      "id": 5,
      "name": "self-hosted",
      "type": "read-only"
    },
    {
      "id": 7,
      "name": "X64",
      "type": "read-only"
    },
    {
      "id": 20,
      "name": "macOS",
      "type": "read-only"
    },
    {
      "id": 21,
      "name": "no-gpu",
      "type": "custom"
    }
  ]
}
```

## List self-hosted runners for a repository
Lists all self-hosted runners configured in a repository.
Authenticated users must have admin access to the repository to use this endpoint.
OAuth app tokens and personal access tokens (classic) need thereposcope to use this endpoint.

### Fine-grained access tokens for "List self-hosted runners for a repository"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Administration" repository permissions (read)

### Parameters for "List self-hosted runners for a repository"

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
namestringThe name of a self-hosted runner.
per_pageintegerThe number of results per page (max 100). For more information, see "Using pagination in the REST API."Default:30
pageintegerThe page number of the results to fetch. For more information, see "Using pagination in the REST API."Default:1
[/TABLE]
The name of a self-hosted runner.
The number of results per page (max 100). For more information, see "Using pagination in the REST API."
Default:30
The page number of the results to fetch. For more information, see "Using pagination in the REST API."
Default:1

### HTTP response status codes for "List self-hosted runners for a repository"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "List self-hosted runners for a repository"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/actions/runners
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
  "runners": [
    {
      "id": 23,
      "name": "linux_runner",
      "os": "linux",
      "status": "online",
      "busy": true,
      "ephemeral": false,
      "labels": [
        {
          "id": 5,
          "name": "self-hosted",
          "type": "read-only"
        },
        {
          "id": 7,
          "name": "X64",
          "type": "read-only"
        },
        {
          "id": 11,
          "name": "Linux",
          "type": "read-only"
        }
      ]
    },
    {
      "id": 24,
      "name": "mac_runner",
      "os": "macos",
      "status": "offline",
      "busy": false,
      "ephemeral": false,
      "labels": [
        {
          "id": 5,
          "name": "self-hosted",
          "type": "read-only"
        },
        {
          "id": 7,
          "name": "X64",
          "type": "read-only"
        },
        {
          "id": 20,
          "name": "macOS",
          "type": "read-only"
        },
        {
          "id": 21,
          "name": "no-gpu",
          "type": "custom"
        }
      ]
    }
  ]
}
```

## List runner applications for a repository
Lists binaries for the runner application that you can download and run.
Authenticated users must have admin access to the repository to use this endpoint.
OAuth app tokens and personal access tokens (classic) need thereposcope to use this endpoint.

### Fine-grained access tokens for "List runner applications for a repository"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Administration" repository permissions (read)

### Parameters for "List runner applications for a repository"

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

### HTTP response status codes for "List runner applications for a repository"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "List runner applications for a repository"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/actions/runners/downloads
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
    "os": "osx",
    "architecture": "x64",
    "download_url": "https://github.com/actions/runner/releases/download/v2.164.0/actions-runner-osx-x64-2.164.0.tar.gz",
    "filename": "actions-runner-osx-x64-2.164.0.tar.gz"
  },
  {
    "os": "linux",
    "architecture": "x64",
    "download_url": "https://github.com/actions/runner/releases/download/v2.164.0/actions-runner-linux-x64-2.164.0.tar.gz",
    "filename": "actions-runner-linux-x64-2.164.0.tar.gz"
  },
  {
    "os": "linux",
    "architecture": "arm",
    "download_url": "https://github.com/actions/runner/releases/download/v2.164.0/actions-runner-linux-arm-2.164.0.tar.gz",
    "filename": "actions-runner-linux-arm-2.164.0.tar.gz"
  },
  {
    "os": "win",
    "architecture": "x64",
    "download_url": "https://github.com/actions/runner/releases/download/v2.164.0/actions-runner-win-x64-2.164.0.zip",
    "filename": "actions-runner-win-x64-2.164.0.zip"
  },
  {
    "os": "linux",
    "architecture": "arm64",
    "download_url": "https://github.com/actions/runner/releases/download/v2.164.0/actions-runner-linux-arm64-2.164.0.tar.gz",
    "filename": "actions-runner-linux-arm64-2.164.0.tar.gz"
  }
]
```

## Create configuration for a just-in-time runner for a repository
Generates a configuration that can be passed to the runner application at startup.
The authenticated user must have admin access to the repository.
OAuth tokens and personal access tokens (classic) need thereposcope to use this endpoint.

### Fine-grained access tokens for "Create configuration for a just-in-time runner for a repository"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Administration" repository permissions (write)

### Parameters for "Create configuration for a just-in-time runner for a repository"

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
namestringRequiredThe name of the new runner.
runner_group_idintegerRequiredThe ID of the runner group to register the runner to.
labelsarray of stringsRequiredThe names of the custom labels to add to the runner.Minimum items: 1.Maximum items: 100.
work_folderstringThe working directory to be used for job execution, relative to the runner install directory.Default:_work
[/TABLE]
The name of the new runner.

```
runner_group_id
```
The ID of the runner group to register the runner to.
The names of the custom labels to add to the runner.Minimum items: 1.Maximum items: 100.

```
work_folder
```
The working directory to be used for job execution, relative to the runner install directory.
Default:_work

### HTTP response status codes for "Create configuration for a just-in-time runner for a repository"

[TABLE]
Status code | Description
201 | Created
404 | Resource not found
409 | Conflict
422 | Validation failed, or the endpoint has been spammed.
[/TABLE]
Created
Resource not found
Conflict
Validation failed, or the endpoint has been spammed.

### Code samples for "Create configuration for a just-in-time runner for a repository"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -X POST \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/actions/runners/generate-jitconfig \
  -d '{"name":"New runner","runner_group_id":1,"labels":["self-hosted","X64","macOS","no-gpu"],"work_folder":"_work"}'
```

#### Response
- Example response
- Response schema

```
Status: 201
```

```
{
  "runner": {
    "id": 23,
    "name": "New runner",
    "os": "unknown",
    "status": "offline",
    "busy": false,
    "labels": [
      {
        "id": 5,
        "name": "self-hosted",
        "type": "read-only"
      },
      {
        "id": 7,
        "name": "X64",
        "type": "read-only"
      },
      {
        "id": 20,
        "name": "macOS",
        "type": "read-only"
      },
      {
        "id": 21,
        "name": "no-gpu",
        "type": "custom"
      }
    ]
  },
  "encoded_jit_config": "abc123"
}
```

## Create a registration token for a repository
Returns a token that you can pass to theconfigscript. The token expires after one hour.
For example, you can replaceTOKENin the following example with the registration token provided by this endpoint to configure your self-hosted runner:

```
./config.sh --url https://github.com/octo-org --token TOKEN
```

```
./config.sh --url https://github.com/octo-org --token TOKEN
```
Authenticated users must have admin access to the repository to use this endpoint.
OAuth tokens and personal access tokens (classic) need thereposcope to use this endpoint.

### Fine-grained access tokens for "Create a registration token for a repository"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Administration" repository permissions (write)

### Parameters for "Create a registration token for a repository"

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

### HTTP response status codes for "Create a registration token for a repository"

[TABLE]
Status code | Description
201 | Created
[/TABLE]
Created

### Code samples for "Create a registration token for a repository"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -X POST \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/actions/runners/registration-token
```

#### Response
- Example response
- Response schema

```
Status: 201
```

```
{
  "token": "LLBF3JGZDX3P5PMEXLND6TS6FCWO6",
  "expires_at": "2020-01-22T12:13:35.123-08:00"
}
```

## Create a remove token for a repository
Returns a token that you can pass to theconfigscript to remove a self-hosted runner from an repository. The token expires after one hour.
For example, you can replaceTOKENin the following example with the registration token provided by this endpoint to remove your self-hosted runner from an organization:

```
./config.sh remove --token TOKEN
```

```
./config.sh remove --token TOKEN
```
Authenticated users must have admin access to the repository to use this endpoint.
OAuth tokens and personal access tokens (classic) need thereposcope to use this endpoint.

### Fine-grained access tokens for "Create a remove token for a repository"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Administration" repository permissions (write)

### Parameters for "Create a remove token for a repository"

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

### HTTP response status codes for "Create a remove token for a repository"

[TABLE]
Status code | Description
201 | Created
[/TABLE]
Created

### Code samples for "Create a remove token for a repository"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -X POST \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/actions/runners/remove-token
```

#### Response
- Example response
- Response schema

```
Status: 201
```

```
{
  "token": "AABF3JGZDX3P5PMEXLND6TS6FCWO6",
  "expires_at": "2020-01-29T12:13:35.123-08:00"
}
```

## Get a self-hosted runner for a repository
Gets a specific self-hosted runner configured in a repository.
Authenticated users must have admin access to the repository to use this endpoint.
OAuth app tokens and personal access tokens (classic) need thereposcope to use this endpoint.

### Fine-grained access tokens for "Get a self-hosted runner for a repository"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Administration" repository permissions (read)

### Parameters for "Get a self-hosted runner for a repository"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
runner_idintegerRequiredUnique identifier of the self-hosted runner.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.
Unique identifier of the self-hosted runner.

### HTTP response status codes for "Get a self-hosted runner for a repository"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "Get a self-hosted runner for a repository"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/actions/runners/RUNNER_ID
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "id": 23,
  "name": "MBP",
  "os": "macos",
  "status": "online",
  "busy": true,
  "ephemeral": false,
  "labels": [
    {
      "id": 5,
      "name": "self-hosted",
      "type": "read-only"
    },
    {
      "id": 7,
      "name": "X64",
      "type": "read-only"
    },
    {
      "id": 20,
      "name": "macOS",
      "type": "read-only"
    },
    {
      "id": 21,
      "name": "no-gpu",
      "type": "custom"
    }
  ]
}
```

## Delete a self-hosted runner from a repository
Forces the removal of a self-hosted runner from a repository. You can use this endpoint to completely remove the runner when the machine you were using no longer exists.
Authenticated users must have admin access to the repository to use this endpoint.
OAuth tokens and personal access tokens (classic) need thereposcope to use this endpoint.

### Fine-grained access tokens for "Delete a self-hosted runner from a repository"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Administration" repository permissions (write)

### Parameters for "Delete a self-hosted runner from a repository"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
runner_idintegerRequiredUnique identifier of the self-hosted runner.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.
Unique identifier of the self-hosted runner.

### HTTP response status codes for "Delete a self-hosted runner from a repository"

[TABLE]
Status code | Description
204 | No Content
422 | Validation failed, or the endpoint has been spammed.
[/TABLE]
No Content
Validation failed, or the endpoint has been spammed.

### Code samples for "Delete a self-hosted runner from a repository"

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
  https://api.github.com/repos/OWNER/REPO/actions/runners/RUNNER_ID
```

#### Response

```
Status: 204
```

## List labels for a self-hosted runner for a repository
Lists all labels for a self-hosted runner configured in a repository.
Authenticated users must have admin access to the repository to use this endpoint.
OAuth app tokens and personal access tokens (classic) need thereposcope to use this endpoint.

### Fine-grained access tokens for "List labels for a self-hosted runner for a repository"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Administration" repository permissions (read)

### Parameters for "List labels for a self-hosted runner for a repository"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
runner_idintegerRequiredUnique identifier of the self-hosted runner.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.
Unique identifier of the self-hosted runner.

### HTTP response status codes for "List labels for a self-hosted runner for a repository"

[TABLE]
Status code | Description
200 | OK
404 | Resource not found
[/TABLE]
OK
Resource not found

### Code samples for "List labels for a self-hosted runner for a repository"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/actions/runners/RUNNER_ID/labels
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "total_count": 4,
  "labels": [
    {
      "id": 5,
      "name": "self-hosted",
      "type": "read-only"
    },
    {
      "id": 7,
      "name": "X64",
      "type": "read-only"
    },
    {
      "id": 20,
      "name": "macOS",
      "type": "read-only"
    },
    {
      "id": 21,
      "name": "no-gpu",
      "type": "custom"
    }
  ]
}
```

## Add custom labels to a self-hosted runner for a repository
Adds custom labels to a self-hosted runner configured in a repository.
Authenticated users must have admin access to the organization to use this endpoint.
OAuth tokens and personal access tokens (classic) need thereposcope to use this endpoint.

### Fine-grained access tokens for "Add custom labels to a self-hosted runner for a repository"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Administration" repository permissions (write)

### Parameters for "Add custom labels to a self-hosted runner for a repository"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
runner_idintegerRequiredUnique identifier of the self-hosted runner.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.
Unique identifier of the self-hosted runner.

[TABLE]
Name, Type, Description
labelsarray of stringsRequiredThe names of the custom labels to add to the runner.
[/TABLE]
The names of the custom labels to add to the runner.

### HTTP response status codes for "Add custom labels to a self-hosted runner for a repository"

[TABLE]
Status code | Description
200 | OK
404 | Resource not found
422 | Validation failed, or the endpoint has been spammed.
[/TABLE]
OK
Resource not found
Validation failed, or the endpoint has been spammed.

### Code samples for "Add custom labels to a self-hosted runner for a repository"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -X POST \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/actions/runners/RUNNER_ID/labels \
  -d '{"labels":["gpu","accelerated"]}'
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "total_count": 4,
  "labels": [
    {
      "id": 5,
      "name": "self-hosted",
      "type": "read-only"
    },
    {
      "id": 7,
      "name": "X64",
      "type": "read-only"
    },
    {
      "id": 20,
      "name": "macOS",
      "type": "read-only"
    },
    {
      "id": 21,
      "name": "no-gpu",
      "type": "custom"
    }
  ]
}
```

## Set custom labels for a self-hosted runner for a repository
Remove all previous custom labels and set the new custom labels for a specific
self-hosted runner configured in a repository.
Authenticated users must have admin access to the repository to use this endpoint.
OAuth app tokens and personal access tokens (classic) need thereposcope to use this endpoint.

### Fine-grained access tokens for "Set custom labels for a self-hosted runner for a repository"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Administration" repository permissions (write)

### Parameters for "Set custom labels for a self-hosted runner for a repository"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
runner_idintegerRequiredUnique identifier of the self-hosted runner.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.
Unique identifier of the self-hosted runner.

[TABLE]
Name, Type, Description
labelsarray of stringsRequiredThe names of the custom labels to set for the runner. You can pass an empty array to remove all custom labels.
[/TABLE]
The names of the custom labels to set for the runner. You can pass an empty array to remove all custom labels.

### HTTP response status codes for "Set custom labels for a self-hosted runner for a repository"

[TABLE]
Status code | Description
200 | OK
404 | Resource not found
422 | Validation failed, or the endpoint has been spammed.
[/TABLE]
OK
Resource not found
Validation failed, or the endpoint has been spammed.

### Code samples for "Set custom labels for a self-hosted runner for a repository"

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
  https://api.github.com/repos/OWNER/REPO/actions/runners/RUNNER_ID/labels \
  -d '{"labels":["gpu","accelerated"]}'
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "total_count": 4,
  "labels": [
    {
      "id": 5,
      "name": "self-hosted",
      "type": "read-only"
    },
    {
      "id": 7,
      "name": "X64",
      "type": "read-only"
    },
    {
      "id": 20,
      "name": "macOS",
      "type": "read-only"
    },
    {
      "id": 21,
      "name": "no-gpu",
      "type": "custom"
    }
  ]
}
```

## Remove all custom labels from a self-hosted runner for a repository
Remove all custom labels from a self-hosted runner configured in a
repository. Returns the remaining read-only labels from the runner.
Authenticated users must have admin access to the repository to use this endpoint.
OAuth app tokens and personal access tokens (classic) need thereposcope to use this endpoint.

### Fine-grained access tokens for "Remove all custom labels from a self-hosted runner for a repository"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Administration" repository permissions (write)

### Parameters for "Remove all custom labels from a self-hosted runner for a repository"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
runner_idintegerRequiredUnique identifier of the self-hosted runner.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.
Unique identifier of the self-hosted runner.

### HTTP response status codes for "Remove all custom labels from a self-hosted runner for a repository"

[TABLE]
Status code | Description
200 | OK
404 | Resource not found
[/TABLE]
OK
Resource not found

### Code samples for "Remove all custom labels from a self-hosted runner for a repository"

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
  https://api.github.com/repos/OWNER/REPO/actions/runners/RUNNER_ID/labels
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "total_count": 3,
  "labels": [
    {
      "id": 5,
      "name": "self-hosted",
      "type": "read-only"
    },
    {
      "id": 7,
      "name": "X64",
      "type": "read-only"
    },
    {
      "id": 20,
      "name": "macOS",
      "type": "read-only"
    }
  ]
}
```

## Remove a custom label from a self-hosted runner for a repository
Remove a custom label from a self-hosted runner configured
in a repository. Returns the remaining labels from the runner.
This endpoint returns a404 Not Foundstatus if the custom label is not
present on the runner.
Authenticated users must have admin access to the repository to use this endpoint.
OAuth app tokens and personal access tokens (classic) need thereposcope to use this endpoint.

### Fine-grained access tokens for "Remove a custom label from a self-hosted runner for a repository"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Administration" repository permissions (write)

### Parameters for "Remove a custom label from a self-hosted runner for a repository"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
runner_idintegerRequiredUnique identifier of the self-hosted runner.
namestringRequiredThe name of a self-hosted runner's custom label.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.
Unique identifier of the self-hosted runner.
The name of a self-hosted runner's custom label.

### HTTP response status codes for "Remove a custom label from a self-hosted runner for a repository"

[TABLE]
Status code | Description
200 | OK
404 | Resource not found
422 | Validation failed, or the endpoint has been spammed.
[/TABLE]
OK
Resource not found
Validation failed, or the endpoint has been spammed.

### Code samples for "Remove a custom label from a self-hosted runner for a repository"

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
  https://api.github.com/repos/OWNER/REPO/actions/runners/RUNNER_ID/labels/NAME
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "total_count": 4,
  "labels": [
    {
      "id": 5,
      "name": "self-hosted",
      "type": "read-only"
    },
    {
      "id": 7,
      "name": "X64",
      "type": "read-only"
    },
    {
      "id": 20,
      "name": "macOS",
      "type": "read-only"
    },
    {
      "id": 21,
      "name": "no-gpu",
      "type": "custom"
    }
  ]
}
```