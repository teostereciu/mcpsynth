# REST API endpoints for repository interactions

*Source: https://docs.github.com/en/rest/interactions/repos*

---

# REST API endpoints for repository interactions
Use the REST API to temporarily restrict which type of user can comment, open issues, or create pull requests in a public repository.

## Who can use this feature?
People with owner or admin access to temporarily restrict which type of user can comment, open issues, or create pull requests in a public repository.

## About repository interactions
People with owner or admin access can use the REST API to temporarily restrict which type of user can comment, open issues, or create pull requests in a public repository. When restrictions are enabled, only the specified type of GitHub user will be able to participate in interactions. Restrictions automatically expire after a defined duration. Here's more about the types of GitHub users:
- Existing users:When you limit interactions toexisting_users, new users with accounts less than 24 hours old who have not previously contributed and are not collaborators will be temporarily restricted in the repository.
- Contributors only:When you limit interactions tocontributors_only, users who have not previously contributed and are not collaborators will be temporarily restricted in the repository.
- Collaborators only:When you limit interactions tocollaborators_only, users who are not collaborators will be temporarily restricted in the repository.
If an interaction limit is enabled for the user or organization that owns the repository, the limit cannot be changed for the individual repository. Instead, use theUserorOrganizationinteractions endpoints to change the interaction limit.

## Get interaction restrictions for a repository
Shows which type of GitHub user can interact with this repository and when the restriction expires. If there are no restrictions, you will see an empty response.

### Fine-grained access tokens for "Get interaction restrictions for a repository"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Administration" repository permissions (read)

### Parameters for "Get interaction restrictions for a repository"

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

### HTTP response status codes for "Get interaction restrictions for a repository"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "Get interaction restrictions for a repository"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/interaction-limits
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "limit": "collaborators_only",
  "origin": "repository",
  "expires_at": "2018-08-17T04:18:39Z"
}
```

## Set interaction restrictions for a repository
Temporarily restricts interactions to a certain type of GitHub user within the given repository. You must have owner or admin access to set these restrictions. If an interaction limit is set for the user or organization that owns this repository, you will receive a409 Conflictresponse and will not be able to use this endpoint to change the interaction limit for a single repository.

### Fine-grained access tokens for "Set interaction restrictions for a repository"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Administration" repository permissions (write)

### Parameters for "Set interaction restrictions for a repository"

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
limitstringRequiredThe type of GitHub user that can comment, open issues, or create pull requests while the interaction limit is in effect.Can be one of:existing_users,contributors_only,collaborators_only
expirystringThe duration of the interaction restriction. Default:one_day.Can be one of:one_day,three_days,one_week,one_month,six_months
[/TABLE]
The type of GitHub user that can comment, open issues, or create pull requests while the interaction limit is in effect.
Can be one of:existing_users,contributors_only,collaborators_only

```
existing_users
```

```
contributors_only
```

```
collaborators_only
```
The duration of the interaction restriction. Default:one_day.
Can be one of:one_day,three_days,one_week,one_month,six_months

### HTTP response status codes for "Set interaction restrictions for a repository"

[TABLE]
Status code | Description
200 | OK
409 | Conflict
[/TABLE]
OK
Conflict

### Code samples for "Set interaction restrictions for a repository"

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
  https://api.github.com/repos/OWNER/REPO/interaction-limits \
  -d '{"limit":"collaborators_only","expiry":"one_day"}'
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "limit": "collaborators_only",
  "origin": "repository",
  "expires_at": "2018-08-17T04:18:39Z"
}
```

## Remove interaction restrictions for a repository
Removes all interaction restrictions from the given repository. You must have owner or admin access to remove restrictions. If the interaction limit is set for the user or organization that owns this repository, you will receive a409 Conflictresponse and will not be able to use this endpoint to change the interaction limit for a single repository.

### Fine-grained access tokens for "Remove interaction restrictions for a repository"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Administration" repository permissions (write)

### Parameters for "Remove interaction restrictions for a repository"

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

### HTTP response status codes for "Remove interaction restrictions for a repository"

[TABLE]
Status code | Description
204 | No Content
409 | Conflict
[/TABLE]
No Content
Conflict

### Code samples for "Remove interaction restrictions for a repository"

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
  https://api.github.com/repos/OWNER/REPO/interaction-limits
```

#### Response

```
Status: 204
```