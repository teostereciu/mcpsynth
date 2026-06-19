# REST API endpoints for outside collaborators

*Source: https://docs.github.com/en/rest/orgs/outside-collaborators*

---

# REST API endpoints for outside collaborators
Use the REST API to manage outside collaborators.

## List outside collaborators for an organization
List all users who are outside collaborators of an organization.

### Fine-grained access tokens for "List outside collaborators for an organization"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Members" organization permissions (read)

### Parameters for "List outside collaborators for an organization"

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
filterstringFilter the list of outside collaborators.2fa_disabledmeans that only outside collaborators withouttwo-factor authenticationenabled will be returned.2fa_insecuremeans that only outside collaborators withinsecure 2FA methodswill be returned.Default:allCan be one of:2fa_disabled,2fa_insecure,all
per_pageintegerThe number of results per page_number (max 100). For more information, see "Using pagination in the REST API."Default:30
pageintegerThe page_number number of the results to fetch. For more information, see "Using pagination in the REST API."Default:1
[/TABLE]
Filter the list of outside collaborators.2fa_disabledmeans that only outside collaborators withouttwo-factor authenticationenabled will be returned.2fa_insecuremeans that only outside collaborators withinsecure 2FA methodswill be returned.
Default:all
Can be one of:2fa_disabled,2fa_insecure,all

```
2fa_disabled
```

```
2fa_insecure
```
The number of results per page_number (max 100). For more information, see "Using pagination in the REST API."
Default:30
The page_number number of the results to fetch. For more information, see "Using pagination in the REST API."
Default:1

### HTTP response status codes for "List outside collaborators for an organization"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "List outside collaborators for an organization"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/orgs/ORG/outside_collaborators
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
]
```

## Convert an organization member to outside collaborator
When an organization member is converted to an outside collaborator, they'll only have access to the repositories that their current team membership allows. The user will no longer be a member of the organization. For more information, see "Converting an organization member to an outside collaborator". Converting an organization member to an outside collaborator may be restricted by enterprise administrators. For more information, see "Enforcing repository management policies in your enterprise."

### Fine-grained access tokens for "Convert an organization member to outside collaborator"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Members" organization permissions (write)

### Parameters for "Convert an organization member to outside collaborator"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
usernamestringRequiredThe handle for the GitHub user account.
[/TABLE]
The organization name. The name is not case sensitive.
The handle for the GitHub user account.

[TABLE]
Name, Type, Description
asyncbooleanWhen set totrue, the request will be performed asynchronously. Returns a 202 status code when the job is successfully queued.Default:false
[/TABLE]
When set totrue, the request will be performed asynchronously. Returns a 202 status code when the job is successfully queued.
Default:false

### HTTP response status codes for "Convert an organization member to outside collaborator"

[TABLE]
Status code | Description
202 | User is getting converted asynchronously
204 | User was converted
403 | Forbidden if user is the last owner of the organization, not a member of the organization, or if the enterprise enforces a policy for inviting outside collaborators. For more information, see "Enforcing repository management policies in your enterprise."
404 | Resource not found
[/TABLE]
User is getting converted asynchronously
User was converted
Forbidden if user is the last owner of the organization, not a member of the organization, or if the enterprise enforces a policy for inviting outside collaborators. For more information, see "Enforcing repository management policies in your enterprise."
Resource not found

### Code samples for "Convert an organization member to outside collaborator"

#### Request examples
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -X PUT \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/orgs/ORG/outside_collaborators/USERNAME \
  -d '{"async":true}'
```

#### User is getting converted asynchronously
- Example response
- Response schema

```
Status: 202
```

## Remove outside collaborator from an organization
Removing a user from this list will remove them from all the organization's repositories.

### Fine-grained access tokens for "Remove outside collaborator from an organization"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Members" organization permissions (write)

### Parameters for "Remove outside collaborator from an organization"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
usernamestringRequiredThe handle for the GitHub user account.
[/TABLE]
The organization name. The name is not case sensitive.
The handle for the GitHub user account.

### HTTP response status codes for "Remove outside collaborator from an organization"

[TABLE]
Status code | Description
204 | No Content
422 | Unprocessable Entity if user is a member of the organization
[/TABLE]
No Content
Unprocessable Entity if user is a member of the organization

### Code samples for "Remove outside collaborator from an organization"

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
  https://api.github.com/orgs/ORG/outside_collaborators/USERNAME
```

#### Response

```
Status: 204
```