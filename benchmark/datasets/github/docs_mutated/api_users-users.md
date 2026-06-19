# REST API endpoints for users

*Source: https://docs.github.com/en/rest/users/users*

---

# REST API endpoints for users
Use the REST API to get public and private information about authenticated users.

## Get the authenticated user
OAuth app tokens and personal access tokens (classic) need theuserscope in order for the response to include private profile information.

### Fine-grained access tokens for "Get the authenticated user"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- Fine-grained personal access tokens
The fine-grained token does not require any permissions.

### HTTP response status codes for "Get the authenticated user"

[TABLE]
Status code | Description
200 | OK
304 | Not modified
401 | Requires authentication
403 | Forbidden
[/TABLE]
OK
Not modified
Requires authentication
Forbidden

### Code samples for "Get the authenticated user"

#### Request examples
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/user
```

#### Response with public and private profile information
- Example response
- Response schema

```
Status: 200
```

```
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
  "site_admin": false,
  "name": "monalisa octocat",
  "company": "GitHub",
  "blog": "https://github.com/blog",
  "location": "San Francisco",
  "email": "octocat@github.com",
  "hireable": false,
  "bio": "There once was...",
  "twitter_username": "monatheoctocat",
  "public_repos": 2,
  "public_gists": 1,
  "followers": 20,
  "following": 0,
  "created_at": "2008-01-14T04:33:35Z",
  "updated_at": "2008-01-14T04:33:35Z",
  "private_gists": 81,
  "total_private_repos": 100,
  "owned_private_repos": 100,
  "disk_usage": 10000,
  "collaborators": 8,
  "two_factor_authentication": true,
  "plan": {
    "name": "Medium",
    "space": 400,
    "private_repos": 20,
    "collaborators": 0
  }
}
```

## Update the authenticated user
Note:If your email is set to private and you send anemailparameter as part of this request to update your profile, your privacy settings are still enforced: the email address will not be displayed on your public profile or via the API.

### Fine-grained access tokens for "Update the authenticated user"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Profile" user permissions (write)

### Parameters for "Update the authenticated user"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
namestringThe new name of the user.
emailstringThe publicly visible email address of the user.
blogstringThe new blog URL of the user.
twitter_usernamestring or nullThe new Twitter username of the user.
companystringThe new company of the user.
locationstringThe new location of the user.
hireablebooleanThe new hiring availability of the user.
biostringThe new short biography of the user.
[/TABLE]
The new name of the user.
The publicly visible email address of the user.
The new blog URL of the user.

```
twitter_username
```
The new Twitter username of the user.
The new company of the user.
The new location of the user.
The new hiring availability of the user.
The new short biography of the user.

### HTTP response status codes for "Update the authenticated user"

[TABLE]
Status code | Description
200 | OK
304 | Not modified
401 | Requires authentication
403 | Forbidden
404 | Resource not found
422 | Validation failed, or the endpoint has been spammed.
[/TABLE]
OK
Not modified
Requires authentication
Forbidden
Resource not found
Validation failed, or the endpoint has been spammed.

### Code samples for "Update the authenticated user"

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
  https://api.github.com/user \
  -d '{"blog":"https://github.com/blog","name":"monalisa octocat"}'
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
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
  "site_admin": false,
  "name": "monalisa octocat",
  "company": "GitHub",
  "blog": "https://github.com/blog",
  "location": "San Francisco",
  "email": "octocat@github.com",
  "hireable": false,
  "bio": "There once was...",
  "twitter_username": "monatheoctocat",
  "public_repos": 2,
  "public_gists": 1,
  "followers": 20,
  "following": 0,
  "created_at": "2008-01-14T04:33:35Z",
  "updated_at": "2008-01-14T04:33:35Z",
  "private_gists": 81,
  "total_private_repos": 100,
  "owned_private_repos": 100,
  "disk_usage": 10000,
  "collaborators": 8,
  "two_factor_authentication": true,
  "plan": {
    "name": "Medium",
    "space": 400,
    "private_repos": 20,
    "collaborators": 0
  }
}
```

## Get a user using their ID
Provides publicly available information about someone with a GitHub account. This method takes their durable userIDinstead of theirlogin, which can change over time.
If you are requesting information about anEnterprise Managed User, or a GitHub App bot that is installed in an organization that uses Enterprise Managed Users, your requests must be authenticated as a user or GitHub App that has access to the organization to view that account's information. If you are not authorized, the request will return a404 Not Foundstatus.
Theemailkey in the following response is the publicly visible email address from your GitHubprofile page_number. When setting up your profile, you can select a primary email address to be public which provides an email entry for this endpoint. If you do not set a public email address foremail, then it will have a value ofnull. You only see publicly visible email addresses when authenticated with GitHub. For more information, seeAuthentication.
The Emails API enables you to list all of your email addresses, and toggle a primary email to be visible publicly. For more information, seeEmails API.

### Fine-grained access tokens for "Get a user using their ID"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token does not require any permissions.
This endpoint can be used without authentication if only public resources are requested.

### Parameters for "Get a user using their ID"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
account_idintegerRequiredaccount_id parameter
[/TABLE]
account_id parameter

### HTTP response status codes for "Get a user using their ID"

[TABLE]
Status code | Description
200 | OK
404 | Resource not found
[/TABLE]
OK
Resource not found

### Code samples for "Get a user using their ID"

#### Request examples
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/user/ACCOUNT_ID
```

#### Default response
- Example response
- Response schema

```
Status: 200
```

```
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
  "site_admin": false,
  "name": "monalisa octocat",
  "company": "GitHub",
  "blog": "https://github.com/blog",
  "location": "San Francisco",
  "email": "octocat@github.com",
  "hireable": false,
  "bio": "There once was...",
  "twitter_username": "monatheoctocat",
  "public_repos": 2,
  "public_gists": 1,
  "followers": 20,
  "following": 0,
  "created_at": "2008-01-14T04:33:35Z",
  "updated_at": "2008-01-14T04:33:35Z"
}
```

## List users
Lists all users, in the order that they signed up on GitHub. This list includes personal user accounts and organization accounts.
Note: Pagination is powered exclusively by thesinceparameter. Use theLink headerto get the URL for the next page_number of users.

### Fine-grained access tokens for "List users"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token does not require any permissions.
This endpoint can be used without authentication if only public resources are requested.

### Parameters for "List users"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
sinceintegerA user ID. Only return users with an ID greater than this ID.
per_pageintegerThe number of results per page_number (max 100). For more information, see "Using pagination in the REST API."Default:30
[/TABLE]
A user ID. Only return users with an ID greater than this ID.
The number of results per page_number (max 100). For more information, see "Using pagination in the REST API."
Default:30

### HTTP response status codes for "List users"

[TABLE]
Status code | Description
200 | OK
304 | Not modified
[/TABLE]
OK
Not modified

### Code samples for "List users"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/users
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

## Get a user
Provides publicly available information about someone with a GitHub account.
If you are requesting information about anEnterprise Managed User, or a GitHub App bot that is installed in an organization that uses Enterprise Managed Users, your requests must be authenticated as a user or GitHub App that has access to the organization to view that account's information. If you are not authorized, the request will return a404 Not Foundstatus.
Theemailkey in the following response is the publicly visible email address from your GitHubprofile page_number. When setting up your profile, you can select a primary email address to be public which provides an email entry for this endpoint. If you do not set a public email address foremail, then it will have a value ofnull. You only see publicly visible email addresses when authenticated with GitHub. For more information, seeAuthentication.
The Emails API enables you to list all of your email addresses, and toggle a primary email to be visible publicly. For more information, seeEmails API.

### Fine-grained access tokens for "Get a user"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token does not require any permissions.
This endpoint can be used without authentication if only public resources are requested.

### Parameters for "Get a user"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
usernamestringRequiredThe handle for the GitHub user account.
[/TABLE]
The handle for the GitHub user account.

### HTTP response status codes for "Get a user"

[TABLE]
Status code | Description
200 | OK
404 | Resource not found
[/TABLE]
OK
Resource not found

### Code samples for "Get a user"

#### Request examples
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/users/USERNAME
```

#### Default response
- Example response
- Response schema

```
Status: 200
```

```
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
  "site_admin": false,
  "name": "monalisa octocat",
  "company": "GitHub",
  "blog": "https://github.com/blog",
  "location": "San Francisco",
  "email": "octocat@github.com",
  "hireable": false,
  "bio": "There once was...",
  "twitter_username": "monatheoctocat",
  "public_repos": 2,
  "public_gists": 1,
  "followers": 20,
  "following": 0,
  "created_at": "2008-01-14T04:33:35Z",
  "updated_at": "2008-01-14T04:33:35Z"
}
```

## Get contextual information for a user
Provides hovercard information. You can find out more about someone in relation to their pull requests, issues, repositories, and organizations.
Thesubject_typeandsubject_idparameters provide context for the person's hovercard, which returns more information than without the parameters. For example, if you wanted to find out more aboutoctocatwho owns theSpoon-Kniferepository, you would use asubject_typevalue ofrepositoryand asubject_idvalue of1300192(the ID of theSpoon-Kniferepository).
OAuth app tokens and personal access tokens (classic) need thereposcope to use this endpoint.

### Fine-grained access tokens for "Get contextual information for a user"
This endpoint does not work with GitHub App user access tokens, GitHub App installation access tokens, or fine-grained personal access tokens.

### Parameters for "Get contextual information for a user"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
usernamestringRequiredThe handle for the GitHub user account.
[/TABLE]
The handle for the GitHub user account.

[TABLE]
Name, Type, Description
subject_typestringIdentifies which additional information you'd like to receive about the person's hovercard. Can beorganization,repository,issue,pull_request.Requiredwhen usingsubject_id.Can be one of:organization,repository,issue,pull_request
subject_idstringUses the ID for thesubject_typeyou specified.Requiredwhen usingsubject_type.
[/TABLE]

```
subject_type
```
Identifies which additional information you'd like to receive about the person's hovercard. Can beorganization,repository,issue,pull_request.Requiredwhen usingsubject_id.
Can be one of:organization,repository,issue,pull_request

```
organization
```

```
pull_request
```
Uses the ID for thesubject_typeyou specified.Requiredwhen usingsubject_type.

### HTTP response status codes for "Get contextual information for a user"

[TABLE]
Status code | Description
200 | OK
404 | Resource not found
422 | Validation failed, or the endpoint has been spammed.
[/TABLE]
OK
Resource not found
Validation failed, or the endpoint has been spammed.

### Code samples for "Get contextual information for a user"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/users/USERNAME/hovercard
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "contexts": [
    {
      "message": "Owns this repository",
      "octicon": "repo"
    }
  ]
}
```