# REST API endpoints for deployment statuses

*Source: https://docs.github.com/en/rest/deployments/statuses*

---

# REST API endpoints for deployment statuses
Use the REST API to manage deployment statuses.

## List deployment statuses
Users with pull access can view deployment statuses for a deployment:

### Fine-grained access tokens for "List deployment statuses"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Deployments" repository permissions (read)
This endpoint can be used without authentication or the aforementioned permissions if only public resources are requested.

### Parameters for "List deployment statuses"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
deployment_idintegerRequireddeployment_id parameter
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.

```
deployment_id
```
deployment_id parameter

[TABLE]
Name, Type, Description
per_pageintegerThe number of results per page (max 100). For more information, see "Using pagination in the REST API."Default:30
pageintegerThe page number of the results to fetch. For more information, see "Using pagination in the REST API."Default:1
[/TABLE]
The number of results per page (max 100). For more information, see "Using pagination in the REST API."
Default:30
The page number of the results to fetch. For more information, see "Using pagination in the REST API."
Default:1

### HTTP response status codes for "List deployment statuses"

[TABLE]
Status code | Description
200 | OK
404 | Resource not found
[/TABLE]
OK
Resource not found

### Code samples for "List deployment statuses"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/deployments/DEPLOYMENT_ID/statuses
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
    "url": "https://api.github.com/repos/octocat/example/deployments/42/statuses/1",
    "id": 1,
    "node_id": "MDE2OkRlcGxveW1lbnRTdGF0dXMx",
    "state": "success",
    "creator": {
      "login": "octocat",
      "id": 1,
      "node_id": "MDQ6VXNlcjE=",
      "avatar_url": "https://github.com/images/error/octocat_happy.gif",
      "gravatar_id": "",
      "url": "https://api.github.com/users/octocat",
      "html_url": "https://github.com/octocat",
      "followers_url": "https://api.github.com/users/octocat/followers",
      "following_url": "https://api.github.com/users/octocat/following{/other_user}",
      "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
      "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
      "organizations_url": "https://api.github.com/users/octocat/orgs",
      "repos_url": "https://api.github.com/users/octocat/repos",
      "events_url": "https://api.github.com/users/octocat/events{/privacy}",
      "received_events_url": "https://api.github.com/users/octocat/received_events",
      "type": "User",
      "site_admin": false
    },
    "description": "Deployment finished successfully.",
    "environment": "production",
    "target_url": "https://example.com/deployment/42/output",
    "created_at": "2012-07-20T01:19:13Z",
    "updated_at": "2012-07-20T01:19:13Z",
    "deployment_url": "https://api.github.com/repos/octocat/example/deployments/42",
    "repository_url": "https://api.github.com/repos/octocat/example",
    "environment_url": "https://test-branch.lab.acme.com",
    "log_url": "https://example.com/deployment/42/output"
  }
]
```

## Create a deployment status
Users withpushaccess can create deployment statuses for a given deployment.
OAuth app tokens and personal access tokens (classic) need therepo_deploymentscope to use this endpoint.

### Fine-grained access tokens for "Create a deployment status"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Deployments" repository permissions (write)

### Parameters for "Create a deployment status"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
deployment_idintegerRequireddeployment_id parameter
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.

```
deployment_id
```
deployment_id parameter

[TABLE]
Name, Type, Description
statestringRequiredThe state of the status. When you set a transient deployment toinactive, the deployment will be shown asdestroyedin GitHub.Can be one of:error,failure,inactive,in_progress,queued,pending,success
target_urlstringThe target URL to associate with this status. This URL should contain output to keep the user updated while the task is running or serve as historical information for what happened in the deployment.NoteIt's recommended to use thelog_urlparameter, which replacestarget_url.Default:""
log_urlstringThe full URL of the deployment's output. This parameter replacestarget_url. We will continue to accepttarget_urlto support legacy uses, but we recommend replacingtarget_urlwithlog_url. Settinglog_urlwill automatically settarget_urlto the same value. Default:""Default:""
descriptionstringA short description of the status. The maximum description length is 140 characters.Default:""
environmentstringName for the target deployment environment, which can be changed when setting a deploy status. For example,production,staging, orqa. If not defined, the environment of the previous status on the deployment will be used, if it exists. Otherwise, the environment of the deployment will be used.
environment_urlstringSets the URL for accessing your environment. Default:""Default:""
auto_inactivebooleanAdds a newinactivestatus to all prior non-transient, non-production environment deployments with the same repository andenvironmentname as the created status's deployment. Aninactivestatus is only added to deployments that had asuccessstate. Default:true
[/TABLE]
The state of the status. When you set a transient deployment toinactive, the deployment will be shown asdestroyedin GitHub.
Can be one of:error,failure,inactive,in_progress,queued,pending,success

```
in_progress
```
The target URL to associate with this status. This URL should contain output to keep the user updated while the task is running or serve as historical information for what happened in the deployment.
Note
It's recommended to use thelog_urlparameter, which replacestarget_url.
Default:""
The full URL of the deployment's output. This parameter replacestarget_url. We will continue to accepttarget_urlto support legacy uses, but we recommend replacingtarget_urlwithlog_url. Settinglog_urlwill automatically settarget_urlto the same value. Default:""
Default:""

```
description
```
A short description of the status. The maximum description length is 140 characters.
Default:""

```
environment
```
Name for the target deployment environment, which can be changed when setting a deploy status. For example,production,staging, orqa. If not defined, the environment of the previous status on the deployment will be used, if it exists. Otherwise, the environment of the deployment will be used.

```
environment_url
```
Sets the URL for accessing your environment. Default:""
Default:""

```
auto_inactive
```
Adds a newinactivestatus to all prior non-transient, non-production environment deployments with the same repository andenvironmentname as the created status's deployment. Aninactivestatus is only added to deployments that had asuccessstate. Default:true

### HTTP response status codes for "Create a deployment status"

[TABLE]
Status code | Description
201 | Created
422 | Validation failed, or the endpoint has been spammed.
[/TABLE]
Created
Validation failed, or the endpoint has been spammed.

### Code samples for "Create a deployment status"

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
  https://api.github.com/repos/OWNER/REPO/deployments/DEPLOYMENT_ID/statuses \
  -d '{"environment":"production","state":"success","log_url":"https://example.com/deployment/42/output","description":"Deployment finished successfully."}'
```

#### Response
- Example response
- Response schema

```
Status: 201
```

```
{
  "url": "https://api.github.com/repos/octocat/example/deployments/42/statuses/1",
  "id": 1,
  "node_id": "MDE2OkRlcGxveW1lbnRTdGF0dXMx",
  "state": "success",
  "creator": {
    "login": "octocat",
    "id": 1,
    "node_id": "MDQ6VXNlcjE=",
    "avatar_url": "https://github.com/images/error/octocat_happy.gif",
    "gravatar_id": "",
    "url": "https://api.github.com/users/octocat",
    "html_url": "https://github.com/octocat",
    "followers_url": "https://api.github.com/users/octocat/followers",
    "following_url": "https://api.github.com/users/octocat/following{/other_user}",
    "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
    "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
    "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
    "organizations_url": "https://api.github.com/users/octocat/orgs",
    "repos_url": "https://api.github.com/users/octocat/repos",
    "events_url": "https://api.github.com/users/octocat/events{/privacy}",
    "received_events_url": "https://api.github.com/users/octocat/received_events",
    "type": "User",
    "site_admin": false
  },
  "description": "Deployment finished successfully.",
  "environment": "production",
  "target_url": "https://example.com/deployment/42/output",
  "created_at": "2012-07-20T01:19:13Z",
  "updated_at": "2012-07-20T01:19:13Z",
  "deployment_url": "https://api.github.com/repos/octocat/example/deployments/42",
  "repository_url": "https://api.github.com/repos/octocat/example",
  "environment_url": "https://test-branch.lab.acme.com",
  "log_url": "https://example.com/deployment/42/output"
}
```

## Get a deployment status
Users with pull access can view a deployment status for a deployment:

### Fine-grained access tokens for "Get a deployment status"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Deployments" repository permissions (read)
This endpoint can be used without authentication or the aforementioned permissions if only public resources are requested.

### Parameters for "Get a deployment status"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
deployment_idintegerRequireddeployment_id parameter
status_idintegerRequired
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.

```
deployment_id
```
deployment_id parameter

### HTTP response status codes for "Get a deployment status"

[TABLE]
Status code | Description
200 | OK
404 | Resource not found
[/TABLE]
OK
Resource not found

### Code samples for "Get a deployment status"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/deployments/DEPLOYMENT_ID/statuses/STATUS_ID
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "url": "https://api.github.com/repos/octocat/example/deployments/42/statuses/1",
  "id": 1,
  "node_id": "MDE2OkRlcGxveW1lbnRTdGF0dXMx",
  "state": "success",
  "creator": {
    "login": "octocat",
    "id": 1,
    "node_id": "MDQ6VXNlcjE=",
    "avatar_url": "https://github.com/images/error/octocat_happy.gif",
    "gravatar_id": "",
    "url": "https://api.github.com/users/octocat",
    "html_url": "https://github.com/octocat",
    "followers_url": "https://api.github.com/users/octocat/followers",
    "following_url": "https://api.github.com/users/octocat/following{/other_user}",
    "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
    "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
    "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
    "organizations_url": "https://api.github.com/users/octocat/orgs",
    "repos_url": "https://api.github.com/users/octocat/repos",
    "events_url": "https://api.github.com/users/octocat/events{/privacy}",
    "received_events_url": "https://api.github.com/users/octocat/received_events",
    "type": "User",
    "site_admin": false
  },
  "description": "Deployment finished successfully.",
  "environment": "production",
  "target_url": "https://example.com/deployment/42/output",
  "created_at": "2012-07-20T01:19:13Z",
  "updated_at": "2012-07-20T01:19:13Z",
  "deployment_url": "https://api.github.com/repos/octocat/example/deployments/42",
  "repository_url": "https://api.github.com/repos/octocat/example",
  "environment_url": "https://test-branch.lab.acme.com",
  "log_url": "https://example.com/deployment/42/output"
}
```