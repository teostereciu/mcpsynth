# REST API endpoints for workflows

*Source: https://docs.github.com/en/rest/actions/workflows*

---

# REST API endpoints for workflows
Use the REST API to interact with workflows in GitHub Actions.

## About workflows in GitHub Actions
You can use the REST API to view workflows for a repository in GitHub Actions. Workflows automate your software development life cycle with a wide range of tools and services. For more information, seeWorkflowsin the GitHub Actions documentation.

## List repository workflows
Lists the workflows in a repository.
Anyone with read access to the repository can use this endpoint.
OAuth app tokens and personal access tokens (classic) need thereposcope to use this endpoint with a private repository.

### Fine-grained access tokens for "List repository workflows"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Actions" repository permissions (read)
This endpoint can be used without authentication or the aforementioned permissions if only public resources are requested.

### Parameters for "List repository workflows"

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
[/TABLE]
The number of results per page (max 100). For more information, see "Using pagination in the REST API."
Default:30
The page number of the results to fetch. For more information, see "Using pagination in the REST API."
Default:1

### HTTP response status codes for "List repository workflows"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "List repository workflows"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/actions/workflows
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
  "workflows": [
    {
      "id": 161335,
      "node_id": "MDg6V29ya2Zsb3cxNjEzMzU=",
      "name": "CI",
      "path": ".github/workflows/blank.yaml",
      "state": "active",
      "created_at": "2020-01-08T23:48:37.000-08:00",
      "updated_at": "2020-01-08T23:50:21.000-08:00",
      "url": "https://api.github.com/repos/octo-org/octo-repo/actions/workflows/161335",
      "html_url": "https://github.com/octo-org/octo-repo/blob/master/.github/workflows/161335",
      "badge_url": "https://github.com/octo-org/octo-repo/workflows/CI/badge.svg"
    },
    {
      "id": 269289,
      "node_id": "MDE4OldvcmtmbG93IFNlY29uZGFyeTI2OTI4OQ==",
      "name": "Linter",
      "path": ".github/workflows/linter.yaml",
      "state": "active",
      "created_at": "2020-01-08T23:48:37.000-08:00",
      "updated_at": "2020-01-08T23:50:21.000-08:00",
      "url": "https://api.github.com/repos/octo-org/octo-repo/actions/workflows/269289",
      "html_url": "https://github.com/octo-org/octo-repo/blob/master/.github/workflows/269289",
      "badge_url": "https://github.com/octo-org/octo-repo/workflows/Linter/badge.svg"
    }
  ]
}
```

## Get a workflow
Gets a specific workflow. You can replaceworkflow_idwith the workflow
file name. For example, you could usemain.yaml.
Anyone with read access to the repository can use this endpoint.
OAuth app tokens and personal access tokens (classic) need thereposcope to use this endpoint with a private repository.

### Fine-grained access tokens for "Get a workflow"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Actions" repository permissions (read)
This endpoint can be used without authentication or the aforementioned permissions if only public resources are requested.

### Parameters for "Get a workflow"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
workflow_idRequiredThe ID of the workflow. You can also pass the workflow file name as a string.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.

```
workflow_id
```
The ID of the workflow. You can also pass the workflow file name as a string.

### HTTP response status codes for "Get a workflow"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "Get a workflow"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/actions/workflows/WORKFLOW_ID
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "id": 161335,
  "node_id": "MDg6V29ya2Zsb3cxNjEzMzU=",
  "name": "CI",
  "path": ".github/workflows/blank.yaml",
  "state": "active",
  "created_at": "2020-01-08T23:48:37.000-08:00",
  "updated_at": "2020-01-08T23:50:21.000-08:00",
  "url": "https://api.github.com/repos/octo-org/octo-repo/actions/workflows/161335",
  "html_url": "https://github.com/octo-org/octo-repo/blob/master/.github/workflows/161335",
  "badge_url": "https://github.com/octo-org/octo-repo/workflows/CI/badge.svg"
}
```

## Disable a workflow
Disables a workflow and sets thestateof the workflow todisabled_manually. You can replaceworkflow_idwith the workflow file name. For example, you could usemain.yaml.
OAuth tokens and personal access tokens (classic) need thereposcope to use this endpoint.

### Fine-grained access tokens for "Disable a workflow"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Actions" repository permissions (write)

### Parameters for "Disable a workflow"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
workflow_idRequiredThe ID of the workflow. You can also pass the workflow file name as a string.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.

```
workflow_id
```
The ID of the workflow. You can also pass the workflow file name as a string.

### HTTP response status codes for "Disable a workflow"

[TABLE]
Status code | Description
204 | No Content
[/TABLE]
No Content

### Code samples for "Disable a workflow"

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
  https://api.github.com/repos/OWNER/REPO/actions/workflows/WORKFLOW_ID/disable
```

#### Response

```
Status: 204
```

## Create a workflow dispatch event
You can use this endpoint to manually trigger a GitHub Actions workflow run. You can replaceworkflow_idwith the workflow file name. For example, you could usemain.yaml.
You must configure your GitHub Actions workflow to run when theworkflow_dispatchwebhookevent occurs. Theinputsare configured in the workflow file. For more information about how to configure theworkflow_dispatchevent in the workflow file, see "Events that trigger workflows."

```
workflow_dispatch
```
OAuth tokens and personal access tokens (classic) need thereposcope to use this endpoint.

### Fine-grained access tokens for "Create a workflow dispatch event"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Actions" repository permissions (write)

### Parameters for "Create a workflow dispatch event"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
workflow_idRequiredThe ID of the workflow. You can also pass the workflow file name as a string.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.

```
workflow_id
```
The ID of the workflow. You can also pass the workflow file name as a string.

[TABLE]
Name, Type, Description
refstringRequiredThe git reference for the workflow. The reference can be a branch or tag name.
inputsobjectInput keys and values configured in the workflow file. The maximum number of properties is 25. Any default properties configured in the workflow file will be used wheninputsare omitted.
[/TABLE]
The git reference for the workflow. The reference can be a branch or tag name.
Input keys and values configured in the workflow file. The maximum number of properties is 25. Any default properties configured in the workflow file will be used wheninputsare omitted.

### HTTP response status codes for "Create a workflow dispatch event"

[TABLE]
Status code | Description
200 | Response including the workflow run ID and URLs whenreturn_run_detailsparameter istrue.
[/TABLE]
Response including the workflow run ID and URLs whenreturn_run_detailsparameter istrue.

### Code samples for "Create a workflow dispatch event"

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
  https://api.github.com/repos/OWNER/REPO/actions/workflows/WORKFLOW_ID/dispatches \
  -d '{"ref":"topic-branch","inputs":{"name":"Mona the Octocat","home":"San Francisco, CA"}}'
```

#### Response including the workflow run ID and URLs whenreturn_run_detailsparameter istrue.
- Example response
- Response schema

```
Status: 200
```

```
{
  "workflow_run_id": 1,
  "run_url": "https://api.github.com/repos/octo-org/octo-repo/actions/runs/1",
  "html_url": "https://github.com/octo-org/octo-repo/actions/runs/1"
}
```

## Enable a workflow
Enables a workflow and sets thestateof the workflow toactive. You can replaceworkflow_idwith the workflow file name. For example, you could usemain.yaml.
OAuth tokens and personal access tokens (classic) need thereposcope to use this endpoint.

### Fine-grained access tokens for "Enable a workflow"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Actions" repository permissions (write)

### Parameters for "Enable a workflow"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
workflow_idRequiredThe ID of the workflow. You can also pass the workflow file name as a string.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.

```
workflow_id
```
The ID of the workflow. You can also pass the workflow file name as a string.

### HTTP response status codes for "Enable a workflow"

[TABLE]
Status code | Description
204 | No Content
[/TABLE]
No Content

### Code samples for "Enable a workflow"

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
  https://api.github.com/repos/OWNER/REPO/actions/workflows/WORKFLOW_ID/enable
```

#### Response

```
Status: 204
```

## Get workflow usage
Warning
This endpoint is in the process of closing down. Refer to "Actions Get workflow usage and Get workflow run usage endpoints closing down" for more information.
Gets the number of billable minutes used by a specific workflow during the current billing cycle. Billable minutes only apply to workflows in private repositories that use GitHub-hosted runners. Usage is listed for each GitHub-hosted runner operating system in milliseconds. Any job re-runs are also included in the usage. The usage does not include the multiplier for macOS and Windows runners and is not rounded up to the nearest whole minute. For more information, see "Managing billing for GitHub Actions".
You can replaceworkflow_idwith the workflow file name. For example, you could usemain.yaml.
Anyone with read access to the repository can use this endpoint.
OAuth app tokens and personal access tokens (classic) need thereposcope to use this endpoint with a private repository.

### Fine-grained access tokens for "Get workflow usage"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Actions" repository permissions (read)
This endpoint can be used without authentication or the aforementioned permissions if only public resources are requested.

### Parameters for "Get workflow usage"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
workflow_idRequiredThe ID of the workflow. You can also pass the workflow file name as a string.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.

```
workflow_id
```
The ID of the workflow. You can also pass the workflow file name as a string.

### HTTP response status codes for "Get workflow usage"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "Get workflow usage"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/actions/workflows/WORKFLOW_ID/timing
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "billable": {
    "UBUNTU": {
      "total_ms": 180000
    },
    "MACOS": {
      "total_ms": 240000
    },
    "WINDOWS": {
      "total_ms": 300000
    }
  }
}
```