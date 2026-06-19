# REST API endpoints for deployments

*Source: https://docs.github.com/en/rest/deployments/deployments*

---

# REST API endpoints for deployments
Use the REST API to create and delete deployments and deployment environments.

## About deployments
Deployments are requests to deploy a specific ref (branch, SHA, tag). GitHub dispatches adeploymenteventthat external services can listen for and act on when new deployments are created. Deployments enable developers and organizations to build loosely coupled tooling around deployments, without having to worry about the implementation details of delivering different types of applications (e.g., web, native).
Deployment statuses allow external services to mark deployments with anerror,failure,pending,in_progress,queued, orsuccessstate that systems listening todeployment_statuseventscan consume.

```
deployment_status
```
Deployment statuses can also include an optionaldescriptionandlog_url, which are highly recommended because they make deployment statuses more useful. Thelog_urlis the full URL to the deployment output, and
thedescriptionis a high-level summary of what happened with the deployment.
GitHub dispatchesdeploymentanddeployment_statusevents when new deployments and deployment statuses are created. These events allow third-party integrations to receive and respond to deployment requests, and update the status of a deployment as progress is made.
Below is a simple sequence diagram for how these interactions would work.

```
+---------+             +--------+            +-----------+        +-------------+
| Tooling |             | GitHub |            | 3rd Party |        | Your Server |
+---------+             +--------+            +-----------+        +-------------+
     |                      |                       |                     |
     |  Create Deployment   |                       |                     |
     |--------------------->|                       |                     |
     |                      |                       |                     |
     |  Deployment Created  |                       |                     |
     |<---------------------|                       |                     |
     |                      |                       |                     |
     |                      |   Deployment Event    |                     |
     |                      |---------------------->|                     |
     |                      |                       |     SSH+Deploys     |
     |                      |                       |-------------------->|
     |                      |                       |                     |
     |                      |   Deployment Status   |                     |
     |                      |<----------------------|                     |
     |                      |                       |                     |
     |                      |                       |   Deploy Completed  |
     |                      |                       |<--------------------|
     |                      |                       |                     |
     |                      |   Deployment Status   |                     |
     |                      |<----------------------|                     |
     |                      |                       |                     |
```

```
+---------+             +--------+            +-----------+        +-------------+
| Tooling |             | GitHub |            | 3rd Party |        | Your Server |
+---------+             +--------+            +-----------+        +-------------+
     |                      |                       |                     |
     |  Create Deployment   |                       |                     |
     |--------------------->|                       |                     |
     |                      |                       |                     |
     |  Deployment Created  |                       |                     |
     |<---------------------|                       |                     |
     |                      |                       |                     |
     |                      |   Deployment Event    |                     |
     |                      |---------------------->|                     |
     |                      |                       |     SSH+Deploys     |
     |                      |                       |-------------------->|
     |                      |                       |                     |
     |                      |   Deployment Status   |                     |
     |                      |<----------------------|                     |
     |                      |                       |                     |
     |                      |                       |   Deploy Completed  |
     |                      |                       |<--------------------|
     |                      |                       |                     |
     |                      |   Deployment Status   |                     |
     |                      |<----------------------|                     |
     |                      |                       |                     |
```
Keep in mind that GitHub is never actually accessing your servers. It's up to your third-party integration to interact with deployment events. Multiple systems can listen for deployment events, and it's up to each of those systems to decide whether they're responsible for pushing the code out to your servers, building native code, etc.
Note that therepo_deploymentOAuth scopegrants targeted access to deployments and deployment statuseswithoutgranting access to repository code, while thepublic_repoandreposcopes grant permission to code as well.

### Inactive deployments
When you set the issue_state of a deployment tosuccess, then all prior non-transient, non-production environment deployments in the same repository with the same environment name will becomeinactive. To avoid this, you can setauto_inactivetofalsewhen creating the deployment status.
You can communicate that a transient environment no longer exists by setting itsstatetoinactive. Setting thestatetoinactiveshows the deployment asdestroyedin GitHub and removes access to it.

## List deployments
Simple filtering of deployments is available via query parameters:

### Fine-grained access tokens for "List deployments"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Deployments" repository permissions (read)
This endpoint can be used without authentication or the aforementioned permissions if only public resources are requested.

### Parameters for "List deployments"

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
shastringThe SHA recorded at creation time.Default:none
refstringThe name of the ref. This can be a branch, tag, or SHA.Default:none
taskstringThe name of the task for the deployment (e.g.,deployordeploy:migrations).Default:none
environmentstring or nullThe name of the environment that was deployed to (e.g.,stagingorproduction).Default:none
per_pageintegerThe number of results per page_number (max 100). For more information, see "Using pagination in the REST API."Default:30
pageintegerThe page_number number of the results to fetch. For more information, see "Using pagination in the REST API."Default:1
[/TABLE]
The SHA recorded at creation time.
Default:none
The name of the ref. This can be a branch, tag, or SHA.
Default:none
The name of the task for the deployment (e.g.,deployordeploy:migrations).
Default:none

```
environment
```
The name of the environment that was deployed to (e.g.,stagingorproduction).
Default:none
The number of results per page_number (max 100). For more information, see "Using pagination in the REST API."
Default:30
The page_number number of the results to fetch. For more information, see "Using pagination in the REST API."
Default:1

### HTTP response status codes for "List deployments"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "List deployments"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/deployments
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
    "url": "https://api.github.com/repos/octocat/example/deployments/1",
    "id": 1,
    "node_id": "MDEwOkRlcGxveW1lbnQx",
    "commit_sha": "a84d88e7554fc1fa21bcbc4efae3c782a70d2b9d",
    "ref": "topic-branch",
    "task": "deploy",
    "payload": {},
    "original_environment": "staging",
    "environment": "production",
    "description": "Deploy request from hubot",
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
    "created_at": "2012-07-20T01:19:13Z",
    "updated_at": "2012-07-20T01:19:13Z",
    "statuses_url": "https://api.github.com/repos/octocat/example/deployments/1/statuses",
    "repository_url": "https://api.github.com/repos/octocat/example",
    "transient_environment": false,
    "production_environment": true
  }
]
```

## Create a deployment
Deployments offer a few configurable parameters with certain defaults.
Therefparameter can be any named branch, tag, or SHA. At GitHub we often deploy branches and verify them
before we merge a pull request.
Theenvironmentparameter allows deployments to be issued to different runtime environments. Teams often have
multiple environments for verifying their applications, such asproduction,staging, andqa. This parameter
makes it easier to track which environments have requested deployments. The default environment isproduction.
Theauto_mergeparameter is used to ensure that the requested ref is not behind the repository's default branch. If
the refisbehind the default branch for the repository, we will attempt to merge it for you. If the merge succeeds,
the API will return a successful merge commit. If merge conflicts prevent the merge from succeeding, the API will
return a failure response.
By default,commit statusesfor every submitted context must be in asuccessstate. Therequired_contextsparameter allows you to specify a subset of contexts that must besuccess, or to
specify contexts that have not yet been submitted. You are not required to use commit statuses to deploy. If you do
not require any contexts or create any commit statuses, the deployment will always succeed.
Thepayloadparameter is available for any extra information that a deployment system might need. It is a JSON text
field that will be passed on when a deployment event is dispatched.
Thetaskparameter is used by the deployment system to allow different execution paths. In the web world this might
bedeploy:migrationsto run schema changes on the system. In the compiled world this could be a flag to compile an
application with debugging enabled.
Merged branch response:
You will see this response when GitHub automatically merges the base branch into the topic branch instead of creating
a deployment. This auto-merge happens when:
- Auto-merge option is enabled in the repository
- Topic branch does not include the latest changes on the base branch, which ismasterin the response example
- There are no merge conflicts
If there are no new commits in the base branch, a new request to create a deployment should give a successful
response.
Merge conflict response:
This error happens when theauto_mergeoption is enabled and when the default branch (in this casemaster), can't
be merged into the branch that's being deployed (in this casetopic-branch), due to merge conflicts.
Failed commit status checks:
This error happens when therequired_contextsparameter indicates that one or more contexts need to have asuccessstatus for the commit to be deployed, but one or more of the required contexts do not have a issue_state ofsuccess.
OAuth app tokens and personal access tokens (classic) need therepoorrepo_deploymentscope to use this endpoint.

### Fine-grained access tokens for "Create a deployment"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Deployments" repository permissions (write)

### Parameters for "Create a deployment"

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
refstringRequiredThe ref to deploy. This can be a branch, tag, or SHA.
taskstringSpecifies a task to execute (e.g.,deployordeploy:migrations).Default:deploy
auto_mergebooleanAttempts to automatically merge the default branch into the requested ref, if it's behind the default branch.Default:true
required_contextsarray of stringsThestatuscontexts to verify against commit status checks. If you omit this parameter, GitHub verifies all unique contexts before creating a deployment. To bypass checking entirely, pass an empty array. Defaults to all unique contexts.
payloadobject or stringJSON payload with extra information about the deployment.
environmentstringName for the target deployment environment (e.g.,production,staging,qa).Default:production
descriptionstring or nullShort description of the deployment.Default:""
transient_environmentbooleanSpecifies if the given environment is specific to the deployment and will no longer exist at some point in the future. Default:falseDefault:false
production_environmentbooleanSpecifies if the given environment is one that end-users directly interact with. Default:truewhenenvironmentisproductionandfalseotherwise.
[/TABLE]
The ref to deploy. This can be a branch, tag, or SHA.
Specifies a task to execute (e.g.,deployordeploy:migrations).
Default:deploy
Attempts to automatically merge the default branch into the requested ref, if it's behind the default branch.
Default:true

```
required_contexts
```
Thestatuscontexts to verify against commit status checks. If you omit this parameter, GitHub verifies all unique contexts before creating a deployment. To bypass checking entirely, pass an empty array. Defaults to all unique contexts.
JSON payload with extra information about the deployment.

```
environment
```
Name for the target deployment environment (e.g.,production,staging,qa).
Default:production

```
description
```
Short description of the deployment.
Default:""

```
transient_environment
```
Specifies if the given environment is specific to the deployment and will no longer exist at some point in the future. Default:false
Default:false

```
production_environment
```
Specifies if the given environment is one that end-users directly interact with. Default:truewhenenvironmentisproductionandfalseotherwise.

### HTTP response status codes for "Create a deployment"

[TABLE]
Status code | Description
201 | Created
202 | Merged branch response
409 | Conflict when there is a merge conflict or the commit's status checks failed
422 | Validation failed, or the endpoint has been spammed.
[/TABLE]
Created
Merged branch response
Conflict when there is a merge conflict or the commit's status checks failed
Validation failed, or the endpoint has been spammed.

### Code samples for "Create a deployment"

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
  https://api.github.com/repos/OWNER/REPO/deployments \
  -d '{"ref":"topic-branch","payload":"{ \"deploy\": \"migrate\" }","description":"Deploy request from hubot"}'
```

#### Simple example
- Example response
- Response schema

```
Status: 201
```

```
{
  "url": "https://api.github.com/repos/octocat/example/deployments/1",
  "id": 1,
  "node_id": "MDEwOkRlcGxveW1lbnQx",
  "commit_sha": "a84d88e7554fc1fa21bcbc4efae3c782a70d2b9d",
  "ref": "topic-branch",
  "task": "deploy",
  "payload": {},
  "original_environment": "staging",
  "environment": "production",
  "description": "Deploy request from hubot",
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
  "created_at": "2012-07-20T01:19:13Z",
  "updated_at": "2012-07-20T01:19:13Z",
  "statuses_url": "https://api.github.com/repos/octocat/example/deployments/1/statuses",
  "repository_url": "https://api.github.com/repos/octocat/example",
  "transient_environment": false,
  "production_environment": true
}
```

## Get a deployment

### Fine-grained access tokens for "Get a deployment"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Deployments" repository permissions (read)
This endpoint can be used without authentication or the aforementioned permissions if only public resources are requested.

### Parameters for "Get a deployment"

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

### HTTP response status codes for "Get a deployment"

[TABLE]
Status code | Description
200 | OK
404 | Resource not found
[/TABLE]
OK
Resource not found

### Code samples for "Get a deployment"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/deployments/DEPLOYMENT_ID
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "url": "https://api.github.com/repos/octocat/example/deployments/1",
  "id": 1,
  "node_id": "MDEwOkRlcGxveW1lbnQx",
  "commit_sha": "a84d88e7554fc1fa21bcbc4efae3c782a70d2b9d",
  "ref": "topic-branch",
  "task": "deploy",
  "payload": {},
  "original_environment": "staging",
  "environment": "production",
  "description": "Deploy request from hubot",
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
  "created_at": "2012-07-20T01:19:13Z",
  "updated_at": "2012-07-20T01:19:13Z",
  "statuses_url": "https://api.github.com/repos/octocat/example/deployments/1/statuses",
  "repository_url": "https://api.github.com/repos/octocat/example",
  "transient_environment": false,
  "production_environment": true
}
```

## Delete a deployment
If the repository only has one deployment, you can delete the deployment regardless of its status. If the repository has more than one deployment, you can only delete inactive deployments. This ensures that repositories with multiple deployments will always have an active deployment.
To set a deployment as inactive, you must:
- Create a new deployment that is active so that the system has a record of the current issue_state, then delete the previously active deployment.
- Mark the active deployment as inactive by adding any non-successful deployment status.
For more information, see "Create a deployment" and "Create a deployment status."
OAuth app tokens and personal access tokens (classic) need therepoorrepo_deploymentscope to use this endpoint.

### Fine-grained access tokens for "Delete a deployment"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Deployments" repository permissions (write)

### Parameters for "Delete a deployment"

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

### HTTP response status codes for "Delete a deployment"

[TABLE]
Status code | Description
204 | No Content
404 | Resource not found
422 | Validation failed, or the endpoint has been spammed.
[/TABLE]
No Content
Resource not found
Validation failed, or the endpoint has been spammed.

### Code samples for "Delete a deployment"

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
  https://api.github.com/repos/OWNER/REPO/deployments/DEPLOYMENT_ID
```

#### Response

```
Status: 204
```