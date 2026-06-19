# REST API endpoints for self-hosted runner groups

*Source: https://docs.github.com/en/rest/actions/self-hosted-runner-groups*

---

# REST API endpoints for self-hosted runner groups
Use the REST API to interact with self-hosted runner groups for GitHub Actions.

## About self-hosted runner groups in GitHub Actions
You can use the REST API to manage groups of self-hosted runners in GitHub Actions. For more information, seeManaging access to self-hosted runners using groups.
These endpoints are available for authenticated users, OAuth apps, and GitHub Apps. Access tokens requirereposcopefor private repositories andpublic_reposcopefor public repositories. GitHub Apps must have theadministrationpermission for repositories or theorganization_self_hosted_runnerspermission for organizations. Authenticated users must have admin access to repositories or organizations, or themanage_runners:enterprisescope for enterprises to use these endpoints.

```
public_repo
```

## List self-hosted runner groups for an organization
Lists all self-hosted runner groups configured in an organization and inherited from an enterprise.
OAuth app tokens and personal access tokens (classic) need theadmin:orgscope to use this endpoint.

### Fine-grained access tokens for "List self-hosted runner groups for an organization"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Self-hosted runners" organization permissions (read)

### Parameters for "List self-hosted runner groups for an organization"

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
per_pageintegerThe number of results per page (max 100). For more information, see "Using pagination in the REST API."Default:30
pageintegerThe page number of the results to fetch. For more information, see "Using pagination in the REST API."Default:1
visible_to_repositorystringOnly return runner groups that are allowed to be used by this repository.
[/TABLE]
The number of results per page (max 100). For more information, see "Using pagination in the REST API."
Default:30
The page number of the results to fetch. For more information, see "Using pagination in the REST API."
Default:1

```
visible_to_repository
```
Only return runner groups that are allowed to be used by this repository.

### HTTP response status codes for "List self-hosted runner groups for an organization"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "List self-hosted runner groups for an organization"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/orgs/ORG/actions/runner-groups
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
  "runner_groups": [
    {
      "id": 1,
      "name": "Default",
      "visibility": "all",
      "default": true,
      "runners_url": "https://api.github.com/orgs/octo-org/actions/runner_groups/1/runners",
      "inherited": false,
      "allows_public_repositories": true,
      "restricted_to_workflows": false,
      "selected_workflows": [],
      "workflow_restrictions_read_only": false
    },
    {
      "id": 2,
      "name": "octo-runner-group",
      "visibility": "selected",
      "default": false,
      "selected_repositories_url": "https://api.github.com/orgs/octo-org/actions/runner_groups/2/repositories",
      "runners_url": "https://api.github.com/orgs/octo-org/actions/runner_groups/2/runners",
      "inherited": true,
      "allows_public_repositories": true,
      "restricted_to_workflows": true,
      "selected_workflows": [
        "octo-org/octo-repo/.github/workflows/deploy.yaml@refs/heads/main"
      ],
      "workflow_restrictions_read_only": true
    },
    {
      "id": 3,
      "name": "expensive-hardware",
      "visibility": "private",
      "default": false,
      "runners_url": "https://api.github.com/orgs/octo-org/actions/runner_groups/3/runners",
      "inherited": false,
      "allows_public_repositories": true,
      "restricted_to_workflows": false,
      "selected_workflows": [
        "octo-org/octo-repo/.github/workflows/deploy.yaml@refs/heads/main"
      ],
      "workflow_restrictions_read_only": false
    }
  ]
}
```

## Create a self-hosted runner group for an organization
Creates a new self-hosted runner group for an organization.
OAuth tokens and personal access tokens (classic) need theadmin:orgscope to use this endpoint.

### Fine-grained access tokens for "Create a self-hosted runner group for an organization"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Self-hosted runners" organization permissions (write)

### Parameters for "Create a self-hosted runner group for an organization"

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
namestringRequiredName of the runner group.
visibilitystringVisibility of a runner group. You can select all repositories, select individual repositories, or limit access to private repositories.Default:allCan be one of:selected,all,private
selected_repository_idsarray of integersList of repository IDs that can access the runner group.
runnersarray of integersList of runner IDs to add to the runner group.
allows_public_repositoriesbooleanWhether the runner group can be used bypublicrepositories.Default:false
restricted_to_workflowsbooleanIftrue, the runner group will be restricted to running only the workflows specified in theselected_workflowsarray.Default:false
selected_workflowsarray of stringsList of workflows the runner group should be allowed to run. This setting will be ignored unlessrestricted_to_workflowsis set totrue.
network_configuration_idstringThe identifier of a hosted compute network configuration.
[/TABLE]
Name of the runner group.
Visibility of a runner group. You can select all repositories, select individual repositories, or limit access to private repositories.
Default:all
Can be one of:selected,all,private

```
selected_repository_ids
```
List of repository IDs that can access the runner group.
List of runner IDs to add to the runner group.

```
allows_public_repositories
```
Whether the runner group can be used bypublicrepositories.
Default:false

```
restricted_to_workflows
```
Iftrue, the runner group will be restricted to running only the workflows specified in theselected_workflowsarray.
Default:false

```
selected_workflows
```
List of workflows the runner group should be allowed to run. This setting will be ignored unlessrestricted_to_workflowsis set totrue.

```
network_configuration_id
```
The identifier of a hosted compute network configuration.

### HTTP response status codes for "Create a self-hosted runner group for an organization"

[TABLE]
Status code | Description
201 | Created
[/TABLE]
Created

### Code samples for "Create a self-hosted runner group for an organization"

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
  https://api.github.com/orgs/ORG/actions/runner-groups \
  -d '{"name":"Expensive hardware runners","visibility":"selected","selected_repository_ids":[32,91],"runners":[9,2]}'
```

#### Response
- Example response
- Response schema

```
Status: 201
```

```
{
  "id": 2,
  "name": "octo-runner-group",
  "visibility": "selected",
  "default": false,
  "selected_repositories_url": "https://api.github.com/orgs/octo-org/actions/runner-groups/2/repositories",
  "runners_url": "https://api.github.com/orgs/octo-org/actions/runner_groups/2/runners",
  "hosted_runners_url": "https://api.github.com/orgs/octo-org/actions/runner_groups/2/hosted-runners",
  "network_configuration_id": "EC486D5D793175D7E3B29C27318D5C1AAE49A7833FC85F2E82C3D2C54AC7D3BA",
  "inherited": false,
  "allows_public_repositories": true,
  "restricted_to_workflows": true,
  "selected_workflows": [
    "octo-org/octo-repo/.github/workflows/deploy.yaml@refs/heads/main"
  ],
  "workflow_restrictions_read_only": false
}
```

## Get a self-hosted runner group for an organization
Gets a specific self-hosted runner group for an organization.
OAuth app tokens and personal access tokens (classic) need theadmin:orgscope to use this endpoint.

### Fine-grained access tokens for "Get a self-hosted runner group for an organization"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Self-hosted runners" organization permissions (read)

### Parameters for "Get a self-hosted runner group for an organization"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
runner_group_idintegerRequiredUnique identifier of the self-hosted runner group.
[/TABLE]
The organization name. The name is not case sensitive.

```
runner_group_id
```
Unique identifier of the self-hosted runner group.

### HTTP response status codes for "Get a self-hosted runner group for an organization"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "Get a self-hosted runner group for an organization"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/orgs/ORG/actions/runner-groups/RUNNER_GROUP_ID
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "id": 2,
  "name": "octo-runner-group",
  "visibility": "selected",
  "default": false,
  "selected_repositories_url": "https://api.github.com/orgs/octo-org/actions/runner_groups/2/repositories",
  "runners_url": "https://api.github.com/orgs/octo-org/actions/runner_groups/2/runners",
  "hosted_runners_url": "https://api.github.com/orgs/octo-org/actions/runner_groups/2/hosted-runners",
  "network_configuration_id": "EC486D5D793175D7E3B29C27318D5C1AAE49A7833FC85F2E82C3D2C54AC7D3BA",
  "inherited": false,
  "allows_public_repositories": true,
  "restricted_to_workflows": true,
  "selected_workflows": [
    "octo-org/octo-repo/.github/workflows/deploy.yaml@refs/heads/main"
  ],
  "workflow_restrictions_read_only": false
}
```

## Update a self-hosted runner group for an organization
Updates thenameandvisibilityof a self-hosted runner group in an organization.
OAuth app tokens and personal access tokens (classic) need theadmin:orgscope to use this endpoint.

### Fine-grained access tokens for "Update a self-hosted runner group for an organization"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Self-hosted runners" organization permissions (write)

### Parameters for "Update a self-hosted runner group for an organization"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
runner_group_idintegerRequiredUnique identifier of the self-hosted runner group.
[/TABLE]
The organization name. The name is not case sensitive.

```
runner_group_id
```
Unique identifier of the self-hosted runner group.

[TABLE]
Name, Type, Description
namestringRequiredName of the runner group.
visibilitystringVisibility of a runner group. You can select all repositories, select individual repositories, or all private repositories.Can be one of:selected,all,private
allows_public_repositoriesbooleanWhether the runner group can be used bypublicrepositories.Default:false
restricted_to_workflowsbooleanIftrue, the runner group will be restricted to running only the workflows specified in theselected_workflowsarray.Default:false
selected_workflowsarray of stringsList of workflows the runner group should be allowed to run. This setting will be ignored unlessrestricted_to_workflowsis set totrue.
network_configuration_idstring or nullThe identifier of a hosted compute network configuration.
[/TABLE]
Name of the runner group.
Visibility of a runner group. You can select all repositories, select individual repositories, or all private repositories.
Can be one of:selected,all,private

```
allows_public_repositories
```
Whether the runner group can be used bypublicrepositories.
Default:false

```
restricted_to_workflows
```
Iftrue, the runner group will be restricted to running only the workflows specified in theselected_workflowsarray.
Default:false

```
selected_workflows
```
List of workflows the runner group should be allowed to run. This setting will be ignored unlessrestricted_to_workflowsis set totrue.

```
network_configuration_id
```
The identifier of a hosted compute network configuration.

### HTTP response status codes for "Update a self-hosted runner group for an organization"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "Update a self-hosted runner group for an organization"

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
  https://api.github.com/orgs/ORG/actions/runner-groups/RUNNER_GROUP_ID \
  -d '{"name":"Expensive hardware runners","visibility":"selected"}'
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "id": 2,
  "name": "octo-runner-group",
  "visibility": "selected",
  "default": false,
  "selected_repositories_url": "https://api.github.com/orgs/octo-org/actions/runner-groups/2/repositories",
  "runners_url": "https://api.github.com/orgs/octo-org/actions/runner_groups/2/runners",
  "hosted_runners_url": "https://api.github.com/orgs/octo-org/actions/runner_groups/2/hosted-runners",
  "network_configuration_id": "EC486D5D793175D7E3B29C27318D5C1AAE49A7833FC85F2E82C3D2C54AC7D3BA",
  "inherited": false,
  "allows_public_repositories": true,
  "restricted_to_workflows": true,
  "selected_workflows": [
    "octo-org/octo-repo/.github/workflows/deploy.yaml@refs/heads/main"
  ],
  "workflow_restrictions_read_only": false
}
```

## Delete a self-hosted runner group from an organization
Deletes a self-hosted runner group for an organization.
OAuth tokens and personal access tokens (classic) need theadmin:orgscope to use this endpoint.

### Fine-grained access tokens for "Delete a self-hosted runner group from an organization"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Self-hosted runners" organization permissions (write)

### Parameters for "Delete a self-hosted runner group from an organization"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
runner_group_idintegerRequiredUnique identifier of the self-hosted runner group.
[/TABLE]
The organization name. The name is not case sensitive.

```
runner_group_id
```
Unique identifier of the self-hosted runner group.

### HTTP response status codes for "Delete a self-hosted runner group from an organization"

[TABLE]
Status code | Description
204 | No Content
[/TABLE]
No Content

### Code samples for "Delete a self-hosted runner group from an organization"

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
  https://api.github.com/orgs/ORG/actions/runner-groups/RUNNER_GROUP_ID
```

#### Response

```
Status: 204
```

## List GitHub-hosted runners in a group for an organization
Lists the GitHub-hosted runners in an organization group.
OAuth app tokens and personal access tokens (classic) need theadmin:orgscope to use this endpoint.

### Fine-grained access tokens for "List GitHub-hosted runners in a group for an organization"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Self-hosted runners" organization permissions (read)

### Parameters for "List GitHub-hosted runners in a group for an organization"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
runner_group_idintegerRequiredUnique identifier of the self-hosted runner group.
[/TABLE]
The organization name. The name is not case sensitive.

```
runner_group_id
```
Unique identifier of the self-hosted runner group.

[TABLE]
Name, Type, Description
per_pageintegerThe number of results per page (max 100). For more information, see "Using pagination in the REST API."Default:30
pageintegerThe page number of the results to fetch. For more information, see "Using pagination in the REST API."Default:1
[/TABLE]
The number of results per page (max 100). For more information, see "Using pagination in the REST API."
Default:30
The page number of the results to fetch. For more information, see "Using pagination in the REST API."
Default:1

### HTTP response status codes for "List GitHub-hosted runners in a group for an organization"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "List GitHub-hosted runners in a group for an organization"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/orgs/ORG/actions/runner-groups/RUNNER_GROUP_ID/hosted-runners
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
      "id": 5,
      "name": "My hosted ubuntu runner",
      "runner_group_id": 2,
      "platform": "linux-x64",
      "image": {
        "id": "ubuntu-20.04",
        "size": 86
      },
      "machine_size_details": {
        "id": "4-core",
        "cpu_cores": 4,
        "memory_gb": 16,
        "storage_gb": 150
      },
      "status": "Ready",
      "maximum_runners": 10,
      "public_ip_enabled": true,
      "public_ips": [
        {
          "enabled": true,
          "prefix": "20.80.208.150",
          "length": 31
        }
      ],
      "last_active_on": "2022-10-09T23:39:01Z"
    },
    {
      "id": 7,
      "name": "My hosted Windows runner",
      "runner_group_id": 2,
      "platform": "win-x64",
      "image": {
        "id": "windows-latest",
        "size": 256
      },
      "machine_size_details": {
        "id": "8-core",
        "cpu_cores": 8,
        "memory_gb": 32,
        "storage_gb": 300
      },
      "status": "Ready",
      "maximum_runners": 20,
      "public_ip_enabled": false,
      "public_ips": [],
      "last_active_on": "2023-04-26T15:23:37Z"
    }
  ]
}
```

## List repository access to a self-hosted runner group in an organization
Lists the repositories with access to a self-hosted runner group configured in an organization.
OAuth app tokens and personal access tokens (classic) need theadmin:orgscope to use this endpoint.

### Fine-grained access tokens for "List repository access to a self-hosted runner group in an organization"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Self-hosted runners" organization permissions (read)

### Parameters for "List repository access to a self-hosted runner group in an organization"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
runner_group_idintegerRequiredUnique identifier of the self-hosted runner group.
[/TABLE]
The organization name. The name is not case sensitive.

```
runner_group_id
```
Unique identifier of the self-hosted runner group.

[TABLE]
Name, Type, Description
pageintegerThe page number of the results to fetch. For more information, see "Using pagination in the REST API."Default:1
per_pageintegerThe number of results per page (max 100). For more information, see "Using pagination in the REST API."Default:30
[/TABLE]
The page number of the results to fetch. For more information, see "Using pagination in the REST API."
Default:1
The number of results per page (max 100). For more information, see "Using pagination in the REST API."
Default:30

### HTTP response status codes for "List repository access to a self-hosted runner group in an organization"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "List repository access to a self-hosted runner group in an organization"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/orgs/ORG/actions/runner-groups/RUNNER_GROUP_ID/repositories
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "total_count": 1,
  "repositories": [
    {
      "id": 1296269,
      "node_id": "MDEwOlJlcG9zaXRvcnkxMjk2MjY5",
      "name": "Hello-World",
      "full_name": "octocat/Hello-World",
      "owner": {
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
      "private": false,
      "html_url": "https://github.com/octocat/Hello-World",
      "description": "This your first repo!",
      "fork": false,
      "url": "https://api.github.com/repos/octocat/Hello-World",
      "archive_url": "https://api.github.com/repos/octocat/Hello-World/{archive_format}{/ref}",
      "assignees_url": "https://api.github.com/repos/octocat/Hello-World/assignees{/user}",
      "blobs_url": "https://api.github.com/repos/octocat/Hello-World/git/blobs{/sha}",
      "branches_url": "https://api.github.com/repos/octocat/Hello-World/branches{/branch}",
      "collaborators_url": "https://api.github.com/repos/octocat/Hello-World/collaborators{/collaborator}",
      "comments_url": "https://api.github.com/repos/octocat/Hello-World/comments{/number}",
      "commits_url": "https://api.github.com/repos/octocat/Hello-World/commits{/sha}",
      "compare_url": "https://api.github.com/repos/octocat/Hello-World/compare/{base}...{head}",
      "contents_url": "https://api.github.com/repos/octocat/Hello-World/contents/{+path}",
      "contributors_url": "https://api.github.com/repos/octocat/Hello-World/contributors",
      "deployments_url": "https://api.github.com/repos/octocat/Hello-World/deployments",
      "downloads_url": "https://api.github.com/repos/octocat/Hello-World/downloads",
      "events_url": "https://api.github.com/repos/octocat/Hello-World/events",
      "forks_url": "https://api.github.com/repos/octocat/Hello-World/forks",
      "git_commits_url": "https://api.github.com/repos/octocat/Hello-World/git/commits{/sha}",
      "git_refs_url": "https://api.github.com/repos/octocat/Hello-World/git/refs{/sha}",
      "git_tags_url": "https://api.github.com/repos/octocat/Hello-World/git/tags{/sha}",
      "git_url": "git:github.com/octocat/Hello-World.git",
      "issue_comment_url": "https://api.github.com/repos/octocat/Hello-World/issues/comments{/number}",
      "issue_events_url": "https://api.github.com/repos/octocat/Hello-World/issues/events{/number}",
      "issues_url": "https://api.github.com/repos/octocat/Hello-World/issues{/number}",
      "keys_url": "https://api.github.com/repos/octocat/Hello-World/keys{/key_id}",
      "labels_url": "https://api.github.com/repos/octocat/Hello-World/labels{/name}",
      "languages_url": "https://api.github.com/repos/octocat/Hello-World/languages",
      "merges_url": "https://api.github.com/repos/octocat/Hello-World/merges",
      "milestones_url": "https://api.github.com/repos/octocat/Hello-World/milestones{/number}",
      "notifications_url": "https://api.github.com/repos/octocat/Hello-World/notifications{?since,all,participating}",
      "pulls_url": "https://api.github.com/repos/octocat/Hello-World/pulls{/number}",
      "releases_url": "https://api.github.com/repos/octocat/Hello-World/releases{/id}",
      "ssh_url": "git@github.com:octocat/Hello-World.git",
      "stargazers_url": "https://api.github.com/repos/octocat/Hello-World/stargazers",
      "statuses_url": "https://api.github.com/repos/octocat/Hello-World/statuses/{sha}",
      "subscribers_url": "https://api.github.com/repos/octocat/Hello-World/subscribers",
      "subscription_url": "https://api.github.com/repos/octocat/Hello-World/subscription",
      "tags_url": "https://api.github.com/repos/octocat/Hello-World/tags",
      "teams_url": "https://api.github.com/repos/octocat/Hello-World/teams",
      "trees_url": "https://api.github.com/repos/octocat/Hello-World/git/trees{/sha}",
      "clone_url": "https://github.com/octocat/Hello-World.git",
      "mirror_url": "git:git.example.com/octocat/Hello-World",
      "hooks_url": "https://api.github.com/repos/octocat/Hello-World/hooks",
      "svn_url": "https://svn.github.com/octocat/Hello-World",
      "homepage": "https://github.com",
      "language": null,
      "forks_count": 9,
      "stargazers_count": 80,
      "watchers_count": 80,
      "size": 108,
      "default_branch": "master",
      "open_issues_count": 0,
      "is_template": true,
      "topics": [
        "octocat",
        "atom",
        "electron",
        "api"
      ],
      "has_issues": true,
      "has_projects": true,
      "has_wiki": true,
      "has_pages": false,
      "has_downloads": true,
      "archived": false,
      "disabled": false,
      "visibility": "public",
      "pushed_at": "2011-01-26T19:06:43Z",
      "created_at": "2011-01-26T19:01:12Z",
      "updated_at": "2011-01-26T19:14:43Z",
      "permissions": {
        "admin": false,
        "push": false,
        "pull": true
      },
      "template_repository": {
        "id": 1296269,
        "node_id": "MDEwOlJlcG9zaXRvcnkxMjk2MjY5",
        "name": "Hello-World",
        "full_name": "octocat/Hello-World",
        "owner": {
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
        "private": false,
        "html_url": "https://github.com/octocat/Hello-World",
        "description": "This your first repo!",
        "fork": false,
        "url": "https://api.github.com/repos/octocat/Hello-World",
        "archive_url": "https://api.github.com/repos/octocat/Hello-World/{archive_format}{/ref}",
        "assignees_url": "https://api.github.com/repos/octocat/Hello-World/assignees{/user}",
        "blobs_url": "https://api.github.com/repos/octocat/Hello-World/git/blobs{/sha}",
        "branches_url": "https://api.github.com/repos/octocat/Hello-World/branches{/branch}",
        "collaborators_url": "https://api.github.com/repos/octocat/Hello-World/collaborators{/collaborator}",
        "comments_url": "https://api.github.com/repos/octocat/Hello-World/comments{/number}",
        "commits_url": "https://api.github.com/repos/octocat/Hello-World/commits{/sha}",
        "compare_url": "https://api.github.com/repos/octocat/Hello-World/compare/{base}...{head}",
        "contents_url": "https://api.github.com/repos/octocat/Hello-World/contents/{+path}",
        "contributors_url": "https://api.github.com/repos/octocat/Hello-World/contributors",
        "deployments_url": "https://api.github.com/repos/octocat/Hello-World/deployments",
        "downloads_url": "https://api.github.com/repos/octocat/Hello-World/downloads",
        "events_url": "https://api.github.com/repos/octocat/Hello-World/events",
        "forks_url": "https://api.github.com/repos/octocat/Hello-World/forks",
        "git_commits_url": "https://api.github.com/repos/octocat/Hello-World/git/commits{/sha}",
        "git_refs_url": "https://api.github.com/repos/octocat/Hello-World/git/refs{/sha}",
        "git_tags_url": "https://api.github.com/repos/octocat/Hello-World/git/tags{/sha}",
        "git_url": "git:github.com/octocat/Hello-World.git",
        "issue_comment_url": "https://api.github.com/repos/octocat/Hello-World/issues/comments{/number}",
        "issue_events_url": "https://api.github.com/repos/octocat/Hello-World/issues/events{/number}",
        "issues_url": "https://api.github.com/repos/octocat/Hello-World/issues{/number}",
        "keys_url": "https://api.github.com/repos/octocat/Hello-World/keys{/key_id}",
        "labels_url": "https://api.github.com/repos/octocat/Hello-World/labels{/name}",
        "languages_url": "https://api.github.com/repos/octocat/Hello-World/languages",
        "merges_url": "https://api.github.com/repos/octocat/Hello-World/merges",
        "milestones_url": "https://api.github.com/repos/octocat/Hello-World/milestones{/number}",
        "notifications_url": "https://api.github.com/repos/octocat/Hello-World/notifications{?since,all,participating}",
        "pulls_url": "https://api.github.com/repos/octocat/Hello-World/pulls{/number}",
        "releases_url": "https://api.github.com/repos/octocat/Hello-World/releases{/id}",
        "ssh_url": "git@github.com:octocat/Hello-World.git",
        "stargazers_url": "https://api.github.com/repos/octocat/Hello-World/stargazers",
        "statuses_url": "https://api.github.com/repos/octocat/Hello-World/statuses/{sha}",
        "subscribers_url": "https://api.github.com/repos/octocat/Hello-World/subscribers",
        "subscription_url": "https://api.github.com/repos/octocat/Hello-World/subscription",
        "tags_url": "https://api.github.com/repos/octocat/Hello-World/tags",
        "teams_url": "https://api.github.com/repos/octocat/Hello-World/teams",
        "trees_url": "https://api.github.com/repos/octocat/Hello-World/git/trees{/sha}",
        "clone_url": "https://github.com/octocat/Hello-World.git",
        "mirror_url": "git:git.example.com/octocat/Hello-World",
        "hooks_url": "https://api.github.com/repos/octocat/Hello-World/hooks",
        "svn_url": "https://svn.github.com/octocat/Hello-World",
        "homepage": "https://github.com",
        "organization": null,
        "language": null,
        "forks": 9,
        "forks_count": 9,
        "stargazers_count": 80,
        "watchers_count": 80,
        "watchers": 80,
        "size": 108,
        "default_branch": "master",
        "open_issues": 0,
        "open_issues_count": 0,
        "is_template": true,
        "license": {
          "key": "mit",
          "name": "MIT License",
          "url": "https://api.github.com/licenses/mit",
          "spdx_id": "MIT",
          "node_id": "MDc6TGljZW5zZW1pdA==",
          "html_url": "https://api.github.com/licenses/mit"
        },
        "topics": [
          "octocat",
          "atom",
          "electron",
          "api"
        ],
        "has_issues": true,
        "has_projects": true,
        "has_wiki": true,
        "has_pages": false,
        "has_downloads": true,
        "archived": false,
        "disabled": false,
        "visibility": "public",
        "pushed_at": "2011-01-26T19:06:43Z",
        "created_at": "2011-01-26T19:01:12Z",
        "updated_at": "2011-01-26T19:14:43Z",
        "permissions": {
          "admin": false,
          "push": false,
          "pull": true
        },
        "allow_rebase_merge": true,
        "template_repository": null,
        "temp_clone_token": "ABTLWHOULUVAXGTRYU7OC2876QJ2O",
        "allow_squash_merge": true,
        "allow_auto_merge": false,
        "delete_branch_on_merge": true,
        "allow_merge_commit": true,
        "subscribers_count": 42,
        "network_count": 0
      },
      "temp_clone_token": "ABTLWHOULUVAXGTRYU7OC2876QJ2O",
      "delete_branch_on_merge": true,
      "subscribers_count": 42,
      "network_count": 0,
      "license": {
        "key": "mit",
        "name": "MIT License",
        "url": "https://api.github.com/licenses/mit",
        "spdx_id": "MIT",
        "node_id": "MDc6TGljZW5zZW1pdA=="
      },
      "forks": 1,
      "open_issues": 1,
      "watchers": 1
    }
  ]
}
```

## Set repository access for a self-hosted runner group in an organization
Replaces the list of repositories that have access to a self-hosted runner group configured in an organization.
OAuth app tokens and personal access tokens (classic) need theadmin:orgscope to use this endpoint.

### Fine-grained access tokens for "Set repository access for a self-hosted runner group in an organization"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Self-hosted runners" organization permissions (write)

### Parameters for "Set repository access for a self-hosted runner group in an organization"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
runner_group_idintegerRequiredUnique identifier of the self-hosted runner group.
[/TABLE]
The organization name. The name is not case sensitive.

```
runner_group_id
```
Unique identifier of the self-hosted runner group.

[TABLE]
Name, Type, Description
selected_repository_idsarray of integersRequiredList of repository IDs that can access the runner group.
[/TABLE]

```
selected_repository_ids
```
List of repository IDs that can access the runner group.

### HTTP response status codes for "Set repository access for a self-hosted runner group in an organization"

[TABLE]
Status code | Description
204 | No Content
[/TABLE]
No Content

### Code samples for "Set repository access for a self-hosted runner group in an organization"

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
  https://api.github.com/orgs/ORG/actions/runner-groups/RUNNER_GROUP_ID/repositories \
  -d '{"selected_repository_ids":[32,91]}'
```

#### Response

```
Status: 204
```

## Add repository access to a self-hosted runner group in an organization
Adds a repository to the list of repositories that can access a self-hosted runner group. The runner group must havevisibilityset toselected. For more information, see "Create a self-hosted runner group for an organization."
OAuth tokens and personal access tokens (classic) need theadmin:orgscope to use this endpoint.

### Fine-grained access tokens for "Add repository access to a self-hosted runner group in an organization"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Self-hosted runners" organization permissions (write)and"Metadata" repository permissions (read)

### Parameters for "Add repository access to a self-hosted runner group in an organization"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
runner_group_idintegerRequiredUnique identifier of the self-hosted runner group.
repository_idintegerRequiredThe unique identifier of the repository.
[/TABLE]
The organization name. The name is not case sensitive.

```
runner_group_id
```
Unique identifier of the self-hosted runner group.

```
repository_id
```
The unique identifier of the repository.

### HTTP response status codes for "Add repository access to a self-hosted runner group in an organization"

[TABLE]
Status code | Description
204 | No Content
[/TABLE]
No Content

### Code samples for "Add repository access to a self-hosted runner group in an organization"

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
  https://api.github.com/orgs/ORG/actions/runner-groups/RUNNER_GROUP_ID/repositories/REPOSITORY_ID
```

#### Response

```
Status: 204
```

## Remove repository access to a self-hosted runner group in an organization
Removes a repository from the list of selected repositories that can access a self-hosted runner group. The runner group must havevisibilityset toselected. For more information, see "Create a self-hosted runner group for an organization."
OAuth app tokens and personal access tokens (classic) need theadmin:orgscope to use this endpoint.

### Fine-grained access tokens for "Remove repository access to a self-hosted runner group in an organization"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Self-hosted runners" organization permissions (write)and"Metadata" repository permissions (read)

### Parameters for "Remove repository access to a self-hosted runner group in an organization"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
runner_group_idintegerRequiredUnique identifier of the self-hosted runner group.
repository_idintegerRequiredThe unique identifier of the repository.
[/TABLE]
The organization name. The name is not case sensitive.

```
runner_group_id
```
Unique identifier of the self-hosted runner group.

```
repository_id
```
The unique identifier of the repository.

### HTTP response status codes for "Remove repository access to a self-hosted runner group in an organization"

[TABLE]
Status code | Description
204 | No Content
[/TABLE]
No Content

### Code samples for "Remove repository access to a self-hosted runner group in an organization"

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
  https://api.github.com/orgs/ORG/actions/runner-groups/RUNNER_GROUP_ID/repositories/REPOSITORY_ID
```

#### Response

```
Status: 204
```

## List self-hosted runners in a group for an organization
Lists self-hosted runners that are in a specific organization group.
OAuth app tokens and personal access tokens (classic) need theadmin:orgscope to use this endpoint.

### Fine-grained access tokens for "List self-hosted runners in a group for an organization"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Self-hosted runners" organization permissions (read)

### Parameters for "List self-hosted runners in a group for an organization"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
runner_group_idintegerRequiredUnique identifier of the self-hosted runner group.
[/TABLE]
The organization name. The name is not case sensitive.

```
runner_group_id
```
Unique identifier of the self-hosted runner group.

[TABLE]
Name, Type, Description
per_pageintegerThe number of results per page (max 100). For more information, see "Using pagination in the REST API."Default:30
pageintegerThe page number of the results to fetch. For more information, see "Using pagination in the REST API."Default:1
[/TABLE]
The number of results per page (max 100). For more information, see "Using pagination in the REST API."
Default:30
The page number of the results to fetch. For more information, see "Using pagination in the REST API."
Default:1

### HTTP response status codes for "List self-hosted runners in a group for an organization"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "List self-hosted runners in a group for an organization"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/orgs/ORG/actions/runner-groups/RUNNER_GROUP_ID/runners
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

## Set self-hosted runners in a group for an organization
Replaces the list of self-hosted runners that are part of an organization runner group.
OAuth app tokens and personal access tokens (classic) need theadmin:orgscope to use this endpoint.

### Fine-grained access tokens for "Set self-hosted runners in a group for an organization"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Self-hosted runners" organization permissions (write)

### Parameters for "Set self-hosted runners in a group for an organization"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
runner_group_idintegerRequiredUnique identifier of the self-hosted runner group.
[/TABLE]
The organization name. The name is not case sensitive.

```
runner_group_id
```
Unique identifier of the self-hosted runner group.

[TABLE]
Name, Type, Description
runnersarray of integersRequiredList of runner IDs to add to the runner group.
[/TABLE]
List of runner IDs to add to the runner group.

### HTTP response status codes for "Set self-hosted runners in a group for an organization"

[TABLE]
Status code | Description
204 | No Content
[/TABLE]
No Content

### Code samples for "Set self-hosted runners in a group for an organization"

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
  https://api.github.com/orgs/ORG/actions/runner-groups/RUNNER_GROUP_ID/runners \
  -d '{"runners":[9,2]}'
```

#### Response

```
Status: 204
```

## Add a self-hosted runner to a group for an organization
Adds a self-hosted runner to a runner group configured in an organization.
OAuth tokens and personal access tokens (classic) need theadmin:orgscope to use this endpoint.

### Fine-grained access tokens for "Add a self-hosted runner to a group for an organization"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Self-hosted runners" organization permissions (write)

### Parameters for "Add a self-hosted runner to a group for an organization"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
runner_group_idintegerRequiredUnique identifier of the self-hosted runner group.
runner_idintegerRequiredUnique identifier of the self-hosted runner.
[/TABLE]
The organization name. The name is not case sensitive.

```
runner_group_id
```
Unique identifier of the self-hosted runner group.
Unique identifier of the self-hosted runner.

### HTTP response status codes for "Add a self-hosted runner to a group for an organization"

[TABLE]
Status code | Description
204 | No Content
[/TABLE]
No Content

### Code samples for "Add a self-hosted runner to a group for an organization"

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
  https://api.github.com/orgs/ORG/actions/runner-groups/RUNNER_GROUP_ID/runners/RUNNER_ID
```

#### Response

```
Status: 204
```

## Remove a self-hosted runner from a group for an organization
Removes a self-hosted runner from a group configured in an organization. The runner is then returned to the default group.
OAuth app tokens and personal access tokens (classic) need theadmin:orgscope to use this endpoint.

### Fine-grained access tokens for "Remove a self-hosted runner from a group for an organization"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Self-hosted runners" organization permissions (write)

### Parameters for "Remove a self-hosted runner from a group for an organization"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
runner_group_idintegerRequiredUnique identifier of the self-hosted runner group.
runner_idintegerRequiredUnique identifier of the self-hosted runner.
[/TABLE]
The organization name. The name is not case sensitive.

```
runner_group_id
```
Unique identifier of the self-hosted runner group.
Unique identifier of the self-hosted runner.

### HTTP response status codes for "Remove a self-hosted runner from a group for an organization"

[TABLE]
Status code | Description
204 | No Content
[/TABLE]
No Content

### Code samples for "Remove a self-hosted runner from a group for an organization"

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
  https://api.github.com/orgs/ORG/actions/runner-groups/RUNNER_GROUP_ID/runners/RUNNER_ID
```

#### Response

```
Status: 204
```