# REST API endpoints for deployment environments

*Source: https://docs.github.com/en/rest/deployments/environments*

---

# REST API endpoints for deployment environments
Use the REST API to create, configure, and delete deployment environments.

## About deployment environments
For more information about environments, seeManaging environments for deployment. To manage environment secrets, seeREST API endpoints for GitHub Actions Secrets.
Environments, environment secrets, and deployment protection rules are available in public repositories for all current GitHub plans. They are not available on legacy plans, such as Bronze, Silver, or Gold. For access to environments, environment secrets, and deployment branches in private or internal repositories, you must use GitHub Pro, GitHub Team, or GitHub Enterprise. If you are on a GitHub Free, GitHub Pro, or GitHub Team plan, other deployment protection rules, such as a wait timer or required reviewers, are only available for public repositories.

## List environments
Lists the environments for a repository.
Anyone with read access to the repository can use this endpoint.
OAuth app tokens and personal access tokens (classic) need thereposcope to use this endpoint with a private repository.

### Fine-grained access tokens for "List environments"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Actions" repository permissions (read)
This endpoint can be used without authentication or the aforementioned permissions if only public resources are requested.

### Parameters for "List environments"

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
per_pageintegerThe number of results per page_number (max 100). For more information, see "Using pagination in the REST API."Default:30
pageintegerThe page_number number of the results to fetch. For more information, see "Using pagination in the REST API."Default:1
[/TABLE]
The number of results per page_number (max 100). For more information, see "Using pagination in the REST API."
Default:30
The page_number number of the results to fetch. For more information, see "Using pagination in the REST API."
Default:1

### HTTP response status codes for "List environments"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "List environments"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/environments
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
  "environments": [
    {
      "id": 161088068,
      "node_id": "MDExOkVudmlyb25tZW50MTYxMDg4MDY4",
      "name": "staging",
      "url": "https://api.github.com/repos/github/hello-world/environments/staging",
      "html_url": "https://github.com/github/hello-world/deployments/activity_log?environments_filter=staging",
      "created_at": "2020-11-23T22:00:40Z",
      "updated_at": "2020-11-23T22:00:40Z",
      "protection_rules": [
        {
          "id": 3736,
          "node_id": "MDQ6R2F0ZTM3MzY=",
          "type": "wait_timer",
          "wait_timer": 30
        },
        {
          "id": 3755,
          "node_id": "MDQ6R2F0ZTM3NTU=",
          "prevent_self_review": false,
          "type": "required_reviewers",
          "reviewers": [
            {
              "type": "User",
              "reviewer": {
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
              }
            },
            {
              "type": "Team",
              "reviewer": {
                "id": 1,
                "node_id": "MDQ6VGVhbTE=",
                "url": "https://api.github.com/teams/1",
                "html_url": "https://github.com/orgs/github/teams/justice-league",
                "name": "Justice League",
                "slug": "justice-league",
                "description": "A great team.",
                "privacy": "closed",
                "notification_setting": "notifications_enabled",
                "permission": "admin",
                "members_url": "https://api.github.com/teams/1/members{/member}",
                "repositories_url": "https://api.github.com/teams/1/repos",
                "parent": null
              }
            }
          ]
        },
        {
          "id": 3756,
          "node_id": "MDQ6R2F0ZTM3NTY=",
          "type": "branch_policy"
        }
      ],
      "deployment_branch_policy": {
        "protected_branches": false,
        "custom_branch_policies": true
      }
    }
  ]
}
```

## Get an environment
Note
To get information about name patterns that branches must match in order to deploy to this environment, see "Get a deployment branch policy."
Anyone with read access to the repository can use this endpoint.
OAuth app tokens and personal access tokens (classic) need thereposcope to use this endpoint with a private repository.

### Fine-grained access tokens for "Get an environment"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Actions" repository permissions (read)
This endpoint can be used without authentication or the aforementioned permissions if only public resources are requested.

### Parameters for "Get an environment"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
environment_namestringRequiredThe name of the environment. The name must be URL encoded. For example, any slashes in the name must be replaced with%2F.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.

```
environment_name
```
The name of the environment. The name must be URL encoded. For example, any slashes in the name must be replaced with%2F.

### HTTP response status codes for "Get an environment"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "Get an environment"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/environments/ENVIRONMENT_NAME
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "id": 161088068,
  "node_id": "MDExOkVudmlyb25tZW50MTYxMDg4MDY4",
  "name": "staging",
  "url": "https://api.github.com/repos/github/hello-world/environments/staging",
  "html_url": "https://github.com/github/hello-world/deployments/activity_log?environments_filter=staging",
  "created_at": "2020-11-23T22:00:40Z",
  "updated_at": "2020-11-23T22:00:40Z",
  "protection_rules": [
    {
      "id": 3736,
      "node_id": "MDQ6R2F0ZTM3MzY=",
      "type": "wait_timer",
      "wait_timer": 30
    },
    {
      "id": 3755,
      "node_id": "MDQ6R2F0ZTM3NTU=",
      "prevent_self_review": false,
      "type": "required_reviewers",
      "reviewers": [
        {
          "type": "User",
          "reviewer": {
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
          }
        },
        {
          "type": "Team",
          "reviewer": {
            "id": 1,
            "node_id": "MDQ6VGVhbTE=",
            "url": "https://api.github.com/teams/1",
            "html_url": "https://github.com/orgs/github/teams/justice-league",
            "name": "Justice League",
            "slug": "justice-league",
            "description": "A great team.",
            "privacy": "closed",
            "notification_setting": "notifications_enabled",
            "permission": "admin",
            "members_url": "https://api.github.com/teams/1/members{/member}",
            "repositories_url": "https://api.github.com/teams/1/repos",
            "parent": null
          }
        }
      ]
    },
    {
      "id": 3756,
      "node_id": "MDQ6R2F0ZTM3NTY=",
      "type": "branch_policy"
    }
  ],
  "deployment_branch_policy": {
    "protected_branches": false,
    "custom_branch_policies": true
  }
}
```

## Create or update an environment
Create or update an environment with protection rules, such as required reviewers. For more information about environment protection rules, see "Environments."
Note
To create or update name patterns that branches must match in order to deploy to this environment, see "Deployment branch policies."
Note
To create or update secrets for an environment, see "GitHub Actions secrets."
OAuth app tokens and personal access tokens (classic) need thereposcope to use this endpoint.

### Fine-grained access tokens for "Create or update an environment"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Administration" repository permissions (write)

### Parameters for "Create or update an environment"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
environment_namestringRequiredThe name of the environment. The name must be URL encoded. For example, any slashes in the name must be replaced with%2F.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.

```
environment_name
```
The name of the environment. The name must be URL encoded. For example, any slashes in the name must be replaced with%2F.

[TABLE]
Name, Type, Description
wait_timerintegerThe amount of time to delay a job after the job is initially triggered. The time (in minutes) must be an integer between 0 and 43,200 (30 days).
prevent_self_reviewbooleanWhether or not a user who created the job is prevented from approving their own job.
reviewersarray of objects or nullThe people or teams that may review jobs that reference the environment. You can list up to six users or teams as reviewers. The reviewers must have at least read access to the repository. Only one of the required reviewers needs to approve the job for it to proceed.
Properties ofreviewersName, Type, DescriptiontypestringThe type of reviewer.Can be one of:User,TeamidintegerThe id of the user or team who can review the deployment | Name, Type, Description | typestringThe type of reviewer.Can be one of:User,Team | idintegerThe id of the user or team who can review the deployment
Name, Type, Description
typestringThe type of reviewer.Can be one of:User,Team
idintegerThe id of the user or team who can review the deployment
deployment_branch_policyobject or nullThe type of deployment branch policy for this environment. To allow all branches to deploy, set tonull.
Properties ofdeployment_branch_policyName, Type, Descriptionprotected_branchesbooleanRequiredWhether only branches with branch protection rules can deploy to this environment. Ifprotected_branchesistrue,custom_branch_policiesmust befalse; ifprotected_branchesisfalse,custom_branch_policiesmust betrue.custom_branch_policiesbooleanRequiredWhether only branches that match the specified name patterns can deploy to this environment.  Ifcustom_branch_policiesistrue,protected_branchesmust befalse; ifcustom_branch_policiesisfalse,protected_branchesmust betrue. | Name, Type, Description | protected_branchesbooleanRequiredWhether only branches with branch protection rules can deploy to this environment. Ifprotected_branchesistrue,custom_branch_policiesmust befalse; ifprotected_branchesisfalse,custom_branch_policiesmust betrue. | custom_branch_policiesbooleanRequiredWhether only branches that match the specified name patterns can deploy to this environment.  Ifcustom_branch_policiesistrue,protected_branchesmust befalse; ifcustom_branch_policiesisfalse,protected_branchesmust betrue.
Name, Type, Description
protected_branchesbooleanRequiredWhether only branches with branch protection rules can deploy to this environment. Ifprotected_branchesistrue,custom_branch_policiesmust befalse; ifprotected_branchesisfalse,custom_branch_policiesmust betrue.
custom_branch_policiesbooleanRequiredWhether only branches that match the specified name patterns can deploy to this environment.  Ifcustom_branch_policiesistrue,protected_branchesmust befalse; ifcustom_branch_policiesisfalse,protected_branchesmust betrue.
[/TABLE]
The amount of time to delay a job after the job is initially triggered. The time (in minutes) must be an integer between 0 and 43,200 (30 days).

```
prevent_self_review
```
Whether or not a user who created the job is prevented from approving their own job.
The people or teams that may review jobs that reference the environment. You can list up to six users or teams as reviewers. The reviewers must have at least read access to the repository. Only one of the required reviewers needs to approve the job for it to proceed.

[TABLE]
Name, Type, Description
typestringThe type of reviewer.Can be one of:User,Team
idintegerThe id of the user or team who can review the deployment
[/TABLE]
The type of reviewer.
Can be one of:User,Team
The id of the user or team who can review the deployment

```
deployment_branch_policy
```
The type of deployment branch policy for this environment. To allow all branches to deploy, set tonull.

```
deployment_branch_policy
```

[TABLE]
Name, Type, Description
protected_branchesbooleanRequiredWhether only branches with branch protection rules can deploy to this environment. Ifprotected_branchesistrue,custom_branch_policiesmust befalse; ifprotected_branchesisfalse,custom_branch_policiesmust betrue.
custom_branch_policiesbooleanRequiredWhether only branches that match the specified name patterns can deploy to this environment.  Ifcustom_branch_policiesistrue,protected_branchesmust befalse; ifcustom_branch_policiesisfalse,protected_branchesmust betrue.
[/TABLE]

```
protected_branches
```
Whether only branches with branch protection rules can deploy to this environment. Ifprotected_branchesistrue,custom_branch_policiesmust befalse; ifprotected_branchesisfalse,custom_branch_policiesmust betrue.

```
custom_branch_policies
```
Whether only branches that match the specified name patterns can deploy to this environment.  Ifcustom_branch_policiesistrue,protected_branchesmust befalse; ifcustom_branch_policiesisfalse,protected_branchesmust betrue.

### HTTP response status codes for "Create or update an environment"

[TABLE]
Status code | Description
200 | OK
422 | Validation error when the environment name is invalid or whenprotected_branchesandcustom_branch_policiesindeployment_branch_policyare set to the same value
[/TABLE]
OK
Validation error when the environment name is invalid or whenprotected_branchesandcustom_branch_policiesindeployment_branch_policyare set to the same value

### Code samples for "Create or update an environment"

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
  https://api.github.com/repos/OWNER/REPO/environments/ENVIRONMENT_NAME \
  -d '{"wait_timer":30,"prevent_self_review":false,"reviewers":[{"type":"User","id":1},{"type":"Team","id":1}],"deployment_branch_policy":{"protected_branches":false,"custom_branch_policies":true}}'
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "id": 161088068,
  "node_id": "MDExOkVudmlyb25tZW50MTYxMDg4MDY4",
  "name": "staging",
  "url": "https://api.github.com/repos/github/hello-world/environments/staging",
  "html_url": "https://github.com/github/hello-world/deployments/activity_log?environments_filter=staging",
  "created_at": "2020-11-23T22:00:40Z",
  "updated_at": "2020-11-23T22:00:40Z",
  "protection_rules": [
    {
      "id": 3736,
      "node_id": "MDQ6R2F0ZTM3MzY=",
      "type": "wait_timer",
      "wait_timer": 30
    },
    {
      "id": 3755,
      "node_id": "MDQ6R2F0ZTM3NTU=",
      "prevent_self_review": false,
      "type": "required_reviewers",
      "reviewers": [
        {
          "type": "User",
          "reviewer": {
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
          }
        },
        {
          "type": "Team",
          "reviewer": {
            "id": 1,
            "node_id": "MDQ6VGVhbTE=",
            "url": "https://api.github.com/teams/1",
            "html_url": "https://github.com/orgs/github/teams/justice-league",
            "name": "Justice League",
            "slug": "justice-league",
            "description": "A great team.",
            "privacy": "closed",
            "notification_setting": "notifications_enabled",
            "permission": "admin",
            "members_url": "https://api.github.com/teams/1/members{/member}",
            "repositories_url": "https://api.github.com/teams/1/repos",
            "parent": null
          }
        }
      ]
    },
    {
      "id": 3756,
      "node_id": "MDQ6R2F0ZTM3NTY=",
      "type": "branch_policy"
    }
  ],
  "deployment_branch_policy": {
    "protected_branches": false,
    "custom_branch_policies": true
  }
}
```

## Delete an environment
OAuth app tokens and personal access tokens (classic) need thereposcope to use this endpoint.

### Fine-grained access tokens for "Delete an environment"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Administration" repository permissions (write)

### Parameters for "Delete an environment"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
environment_namestringRequiredThe name of the environment. The name must be URL encoded. For example, any slashes in the name must be replaced with%2F.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.

```
environment_name
```
The name of the environment. The name must be URL encoded. For example, any slashes in the name must be replaced with%2F.

### HTTP response status codes for "Delete an environment"

[TABLE]
Status code | Description
204 | Default response
[/TABLE]
Default response

### Code samples for "Delete an environment"

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
  https://api.github.com/repos/OWNER/REPO/environments/ENVIRONMENT_NAME
```

#### Default response

```
Status: 204
```