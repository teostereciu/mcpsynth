# REST API endpoints for user interactions

*Source: https://docs.github.com/en/rest/interactions/user*

---

# REST API endpoints for user interactions
Use the REST API to temporarily restrict which type of user can comment, open issues, or create pull requests in your public repositories.

## About user interactions
You can use the REST API to temporarily restrict which type of user can comment, open issues, or create pull requests on your public repositories. When restrictions are enabled, only the specified type of GitHub user will be able to participate in interactions. Restrictions automatically expire after a defined duration. Here's more about the types of GitHub users:
- Existing users:When you limit interactions toexisting_users, new users with accounts less than 24 hours old who have not previously contributed and are not collaborators will be temporarily restricted from interacting with your repositories.
- Contributors only:When you limit interactions tocontributors_only, users who have not previously contributed and are not collaborators will be temporarily restricted from interacting with your repositories.
- Collaborators only:When you limit interactions tocollaborators_only, users who are not collaborators will be temporarily restricted from interacting with your repositories.
Setting the interaction limit at the user level will overwrite any interaction limits that are set for individual repositories owned by the user. To set different interaction limits for individual repositories owned by the user, use theRepositoryinteractions endpoints instead.

## Get interaction restrictions for your public repositories
Shows which type of GitHub user can interact with your public repositories and when the restriction expires.

### Fine-grained access tokens for "Get interaction restrictions for your public repositories"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Interaction limits" user permissions (read)

### HTTP response status codes for "Get interaction restrictions for your public repositories"

[TABLE]
Status code | Description
200 | Default response
204 | Response when there are no restrictions
[/TABLE]
Default response
Response when there are no restrictions

### Code samples for "Get interaction restrictions for your public repositories"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/user/interaction-limits
```

#### Default response
- Example response
- Response schema

```
Status: 200
```

```
{
  "limit": "collaborators_only",
  "origin": "organization",
  "expires_at": "2018-08-17T04:18:39Z"
}
```

## Set interaction restrictions for your public repositories
Temporarily restricts which type of GitHub user can interact with your public repositories. Setting the interaction limit at the user level will overwrite any interaction limits that are set for individual repositories owned by the user.

### Fine-grained access tokens for "Set interaction restrictions for your public repositories"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Interaction limits" user permissions (write)

### Parameters for "Set interaction restrictions for your public repositories"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

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

### HTTP response status codes for "Set interaction restrictions for your public repositories"

[TABLE]
Status code | Description
200 | OK
422 | Validation failed, or the endpoint has been spammed.
[/TABLE]
OK
Validation failed, or the endpoint has been spammed.

### Code samples for "Set interaction restrictions for your public repositories"

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
  https://api.github.com/user/interaction-limits \
  -d '{"limit":"collaborators_only","expiry":"one_month"}'
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
  "origin": "user",
  "expires_at": "2018-08-17T04:18:39Z"
}
```

## Remove interaction restrictions from your public repositories
Removes any interaction restrictions from your public repositories.

### Fine-grained access tokens for "Remove interaction restrictions from your public repositories"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Interaction limits" user permissions (write)

### HTTP response status codes for "Remove interaction restrictions from your public repositories"

[TABLE]
Status code | Description
204 | No Content
[/TABLE]
No Content

### Code samples for "Remove interaction restrictions from your public repositories"

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
  https://api.github.com/user/interaction-limits
```

#### Response

```
Status: 204
```