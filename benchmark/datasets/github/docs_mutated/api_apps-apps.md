# REST API endpoints for GitHub Apps

*Source: https://docs.github.com/en/rest/apps/apps*

---

# REST API endpoints for GitHub Apps
Use the REST API to interact with GitHub Apps

## About GitHub Apps
If you are using your app with GitHub Actions and want to modify workflow files, you must authenticate on behalf of the user with an OAuth token that includes theworkflowscope. The user must have admin or write permission to the repository that contains the workflow file. For more information, seeScopes for OAuth apps.
This page_number lists endpoints that you can access while authenticated as a GitHub App. For more information, seeAuthenticating as a GitHub App.
SeeREST API endpoints for GitHub App installationsfor a list of endpoints that require authentication as a GitHub App installation.

## Get the authenticated app
Returns the GitHub App associated with the authentication credentials used. To see how many app installations are associated with this GitHub App, see theinstallations_countin the response. For more details about your app's installations, see the "List installations for the authenticated app" endpoint.
You must use aJWTto access this endpoint.

### Fine-grained access tokens for "Get the authenticated app"
This endpoint does not work with GitHub App user access tokens, GitHub App installation access tokens, or fine-grained personal access tokens.

### HTTP response status codes for "Get the authenticated app"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "Get the authenticated app"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/app
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "id": 1,
  "slug": "octoapp",
  "client_id": "Iv1.ab1112223334445c",
  "node_id": "MDExOkludGVncmF0aW9uMQ==",
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
  "name": "Octocat App",
  "description": "",
  "external_url": "https://example.com",
  "html_url": "https://github.com/apps/octoapp",
  "created_at": "2017-07-08T16:18:44-04:00",
  "updated_at": "2017-07-08T16:18:44-04:00",
  "permissions": {
    "metadata": "read",
    "contents": "read",
    "issues": "write",
    "single_file": "write"
  },
  "events": [
    "push",
    "pull_request"
  ]
}
```

## Create a GitHub App from a manifest
Use this endpoint to complete the handshake necessary when implementing theGitHub App Manifest flow. When you create a GitHub App with the manifest flow, you receive a temporarycodeused to retrieve the GitHub App'sid,pem(private key), andwebhook_secret.

### Fine-grained access tokens for "Create a GitHub App from a manifest"
This endpoint does not work with GitHub App user access tokens, GitHub App installation access tokens, or fine-grained personal access tokens.

### Parameters for "Create a GitHub App from a manifest"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
codestringRequired
[/TABLE]

### HTTP response status codes for "Create a GitHub App from a manifest"

[TABLE]
Status code | Description
201 | Created
404 | Resource not found
422 | Validation failed, or the endpoint has been spammed.
[/TABLE]
Created
Resource not found
Validation failed, or the endpoint has been spammed.

### Code samples for "Create a GitHub App from a manifest"

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
  https://api.github.com/app-manifests/CODE/conversions
```

#### Response
- Example response
- Response schema

```
Status: 201
```

```
{
  "id": 1,
  "slug": "octoapp",
  "node_id": "MDxOkludGVncmF0aW9uMQ==",
  "owner": {
    "login": "github",
    "id": 1,
    "node_id": "MDEyOk9yZ2FuaXphdGlvbjE=",
    "url": "https://api.github.com/orgs/github",
    "repos_url": "https://api.github.com/orgs/github/repos",
    "events_url": "https://api.github.com/orgs/github/events",
    "avatar_url": "https://github.com/images/error/octocat_happy.gif",
    "gravatar_id": "",
    "html_url": "https://github.com/octocat",
    "followers_url": "https://api.github.com/users/octocat/followers",
    "following_url": "https://api.github.com/users/octocat/following{/other_user}",
    "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
    "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
    "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
    "organizations_url": "https://api.github.com/users/octocat/orgs",
    "received_events_url": "https://api.github.com/users/octocat/received_events",
    "type": "User",
    "site_admin": true
  },
  "name": "Octocat App",
  "description": "",
  "external_url": "https://example.com",
  "html_url": "https://github.com/apps/octoapp",
  "created_at": "2017-07-08T16:18:44-04:00",
  "updated_at": "2017-07-08T16:18:44-04:00",
  "permissions": {
    "metadata": "read",
    "contents": "read",
    "issues": "write",
    "single_file": "write"
  },
  "events": [
    "push",
    "pull_request"
  ],
  "client_id": "Iv1.8a61f9b3a7aba766",
  "client_secret": "1726be1638095a19edd134c77bde3aa2ece1e5d8",
  "webhook_secret": "e340154128314309424b7c8e90325147d99fdafa",
  "pem": "-----BEGIN RSA PRIVATE KEY-----\nMIIEowIBAAKCAQEAuEPzOUE+kiEH1WLiMeBytTEF856j0hOVcSUSUkZxKvqczkWM\n9vo1gDyC7ZXhdH9fKh32aapba3RSsp4ke+giSmYTk2mGR538ShSDxh0OgpJmjiKP\nX0Bj4j5sFqfXuCtl9SkH4iueivv4R53ktqM+n6hk98l6hRwC39GVIblAh2lEM4L/\n6WvYwuQXPMM5OG2Ryh2tDZ1WS5RKfgq+9ksNJ5Q9UtqtqHkO+E63N5OK9sbzpUUm\noNaOl3udTlZD3A8iqwMPVxH4SxgATBPAc+bmjk6BMJ0qIzDcVGTrqrzUiywCTLma\nszdk8GjzXtPDmuBgNn+o6s02qVGpyydgEuqmTQIDAQABAoIBACL6AvkjQVVLn8kJ\ndBYznJJ4M8ECo+YEgaFwgAHODT0zRQCCgzd+Vxl4YwHmKV2Lr+y2s0drZt8GvYva\nKOK8NYYZyi15IlwFyRXmvvykF1UBpSXluYFDH7KaVroWMgRreHcIys5LqVSIb6Bo\ngDmK0yBLPp8qR29s2b7ScZRtLaqGJiX+j55rNzrZwxHkxFHyG9OG+u9IsBElcKCP\nkYCVE8ZdYexfnKOZbgn2kZB9qu0T/Mdvki8yk3I2bI6xYO24oQmhnT36qnqWoCBX\nNuCNsBQgpYZeZET8mEAUmo9d+ABmIHIvSs005agK8xRaP4+6jYgy6WwoejJRF5yd\nNBuF7aECgYEA50nZ4FiZYV0vcJDxFYeY3kYOvVuKn8OyW+2rg7JIQTremIjv8FkE\nZnwuF9ZRxgqLxUIfKKfzp/5l5LrycNoj2YKfHKnRejxRWXqG+ZETfxxlmlRns0QG\nJ4+BYL0CoanDSeA4fuyn4Bv7cy/03TDhfg/Uq0Aeg+hhcPE/vx3ebPsCgYEAy/Pv\neDLssOSdeyIxf0Brtocg6aPXIVaLdus+bXmLg77rJIFytAZmTTW8SkkSczWtucI3\nFI1I6sei/8FdPzAl62/JDdlf7Wd9K7JIotY4TzT7Tm7QU7xpfLLYIP1bOFjN81rk\n77oOD4LsXcosB/U6s1blPJMZ6AlO2EKs10UuR1cCgYBipzuJ2ADEaOz9RLWwi0AH\nPza2Sj+c2epQD9ZivD7Zo/Sid3ZwvGeGF13JyR7kLEdmAkgsHUdu1rI7mAolXMaB\n1pdrsHureeLxGbRM6za3tzMXWv1Il7FQWoPC8ZwXvMOR1VQDv4nzq7vbbA8z8c+c\n57+8tALQHOTDOgQIzwK61QKBgERGVc0EJy4Uag+VY8J4m1ZQKBluqo7TfP6DQ7O8\nM5MX73maB/7yAX8pVO39RjrhJlYACRZNMbK+v/ckEQYdJSSKmGCVe0JrGYDuPtic\nI9+IGfSorf7KHPoMmMN6bPYQ7Gjh7a++tgRFTMEc8956Hnt4xGahy9NcglNtBpVN\n6G8jAoGBAMCh028pdzJa/xeBHLLaVB2sc0Fe7993WlsPmnVE779dAz7qMscOtXJK\nfgtriltLSSD6rTA9hUAsL/X62rY0wdXuNdijjBb/qvrx7CAV6i37NK1CjABNjsfG\nZM372Ac6zc1EqSrid2IjET1YqyIW2KGLI1R2xbQc98UGlt48OdWu\n-----END RSA PRIVATE KEY-----\n"
}
```

## List installation requests for the authenticated app
Lists all the pending installation requests for the authenticated GitHub App.

### Fine-grained access tokens for "List installation requests for the authenticated app"
This endpoint does not work with GitHub App user access tokens, GitHub App installation access tokens, or fine-grained personal access tokens.

### Parameters for "List installation requests for the authenticated app"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
per_pageintegerThe number of results per page_number (max 100). For more information, see "Using pagination in the REST API."Default:30
pageintegerThe page_number number of the results to fetch. For more information, see "Using pagination in the REST API."Default:1
[/TABLE]
The number of results per page_number (max 100). For more information, see "Using pagination in the REST API."
Default:30
The page_number number of the results to fetch. For more information, see "Using pagination in the REST API."
Default:1

### HTTP response status codes for "List installation requests for the authenticated app"

[TABLE]
Status code | Description
200 | List of integration installation requests
304 | Not modified
401 | Requires authentication
[/TABLE]
List of integration installation requests
Not modified
Requires authentication

### Code samples for "List installation requests for the authenticated app"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/app/installation-requests
```

#### List of integration installation requests
- Example response
- Response schema

```
Status: 200
```

```
[
  {
    "id": 25381,
    "node_id": "MDEyOkludGVncmF0aW9uMTIzNDU2Nzg5MA==",
    "account": {
      "login": "octo-org",
      "id": 6811672,
      "node_id": "MDEyOk9yZ2FuaXphdGlvbjY4MTE2NzI=",
      "avatar_url": "https://avatars3.githubusercontent.com/u/6811672?v=4",
      "gravatar_id": "",
      "url": "https://api.github.com/users/octo-org",
      "html_url": "https://github.com/octo-org",
      "followers_url": "https://api.github.com/users/octo-org/followers",
      "following_url": "https://api.github.com/users/octo-org/following{/other_user}",
      "gists_url": "https://api.github.com/users/octo-org/gists{/gist_id}",
      "starred_url": "https://api.github.com/users/octo-org/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/octo-org/subscriptions",
      "organizations_url": "https://api.github.com/users/octo-org/orgs",
      "repos_url": "https://api.github.com/users/octo-org/repos",
      "events_url": "https://api.github.com/users/octo-org/events{/privacy}",
      "received_events_url": "https://api.github.com/users/octo-org/received_events",
      "type": "Organization",
      "site_admin": false
    },
    "requester": {
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
    "created_at": "2022-07-08T16:18:44-04:00"
  }
]
```

## List installations for the authenticated app
The permissions the installation has are included under thepermissionskey.
You must use aJWTto access this endpoint.

### Fine-grained access tokens for "List installations for the authenticated app"
This endpoint does not work with GitHub App user access tokens, GitHub App installation access tokens, or fine-grained personal access tokens.

### Parameters for "List installations for the authenticated app"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
per_pageintegerThe number of results per page_number (max 100). For more information, see "Using pagination in the REST API."Default:30
pageintegerThe page_number number of the results to fetch. For more information, see "Using pagination in the REST API."Default:1
sincestringOnly show results that were last updated after the given time. This is a timestamp inISO 8601format:YYYY-MM-DDTHH:MM:SSZ.
outdatedstring
[/TABLE]
The number of results per page_number (max 100). For more information, see "Using pagination in the REST API."
Default:30
The page_number number of the results to fetch. For more information, see "Using pagination in the REST API."
Default:1
Only show results that were last updated after the given time. This is a timestamp inISO 8601format:YYYY-MM-DDTHH:MM:SSZ.

### HTTP response status codes for "List installations for the authenticated app"

[TABLE]
Status code | Description
200 | The permissions the installation has are included under thepermissionskey.
[/TABLE]
The permissions the installation has are included under thepermissionskey.

### Code samples for "List installations for the authenticated app"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/app/installations
```

#### The permissions the installation has are included under thepermissionskey.
- Example response
- Response schema

```
Status: 200
```

```
[
  {
    "id": 1,
    "account": {
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
    "access_tokens_url": "https://api.github.com/app/installations/1/access_tokens",
    "repositories_url": "https://api.github.com/installation/repositories",
    "html_url": "https://github.com/organizations/github/settings/installations/1",
    "app_id": 1,
    "target_id": 1,
    "target_type": "Organization",
    "permissions": {
      "checks": "write",
      "metadata": "read",
      "contents": "read"
    },
    "events": [
      "push",
      "pull_request"
    ],
    "single_file_name": "config.yaml",
    "has_multiple_single_files": true,
    "single_file_paths": [
      "config.yml",
      ".github/issue_TEMPLATE.md"
    ],
    "repository_selection": "selected",
    "created_at": "2017-07-08T16:18:44-04:00",
    "updated_at": "2017-07-08T16:18:44-04:00",
    "app_slug": "github-actions",
    "suspended_at": null,
    "suspended_by": null
  }
]
```

## Get an installation for the authenticated app
Enables an authenticated GitHub App to find an installation's information using the installation id.
You must use aJWTto access this endpoint.

### Fine-grained access tokens for "Get an installation for the authenticated app"
This endpoint does not work with GitHub App user access tokens, GitHub App installation access tokens, or fine-grained personal access tokens.

### Parameters for "Get an installation for the authenticated app"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
installation_idintegerRequiredThe unique identifier of the installation.
[/TABLE]

```
installation_id
```
The unique identifier of the installation.

### HTTP response status codes for "Get an installation for the authenticated app"

[TABLE]
Status code | Description
200 | OK
404 | Resource not found
[/TABLE]
OK
Resource not found

### Code samples for "Get an installation for the authenticated app"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/app/installations/1
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "id": 1,
  "account": {
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
  "access_tokens_url": "https://api.github.com/app/installations/1/access_tokens",
  "repositories_url": "https://api.github.com/installation/repositories",
  "html_url": "https://github.com/organizations/github/settings/installations/1",
  "app_id": 1,
  "target_id": 1,
  "target_type": "Organization",
  "permissions": {
    "checks": "write",
    "metadata": "read",
    "contents": "read"
  },
  "events": [
    "push",
    "pull_request"
  ],
  "single_file_name": "config.yaml",
  "has_multiple_single_files": true,
  "single_file_paths": [
    "config.yml",
    ".github/issue_TEMPLATE.md"
  ],
  "repository_selection": "selected",
  "created_at": "2017-07-08T16:18:44-04:00",
  "updated_at": "2017-07-08T16:18:44-04:00",
  "app_slug": "github-actions",
  "suspended_at": null,
  "suspended_by": null
}
```

## Delete an installation for the authenticated app
Uninstalls a GitHub App on a user, organization, or enterprise account. If you prefer to temporarily suspend an app's access to your account's resources, then we recommend the "Suspend an app installation" endpoint.
You must use aJWTto access this endpoint.

### Fine-grained access tokens for "Delete an installation for the authenticated app"
This endpoint does not work with GitHub App user access tokens, GitHub App installation access tokens, or fine-grained personal access tokens.

### Parameters for "Delete an installation for the authenticated app"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
installation_idintegerRequiredThe unique identifier of the installation.
[/TABLE]

```
installation_id
```
The unique identifier of the installation.

### HTTP response status codes for "Delete an installation for the authenticated app"

[TABLE]
Status code | Description
202 | Accepted
404 | Resource not found
[/TABLE]
Accepted
Resource not found

### Code samples for "Delete an installation for the authenticated app"

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
  https://api.github.com/app/installations/1
```

#### Response

```
Status: 202
```

## Create an installation access token for an app
Creates an installation access token that enables a GitHub App to make authenticated API requests for the app's installation on an organization or individual account. Installation tokens expire one hour from the time you create them. Using an expired token produces a status code of401 - Unauthorized, and requires creating a new installation token. By default the installation token has access to all repositories that the installation can access.
Optionally, you can use therepositoriesorrepository_idsbody parameters to specify individual repositories that the installation access token can access. If you don't userepositoriesorrepository_idsto grant access to specific repositories, the installation access token will have access to all repositories that the installation was granted access to. The installation access token cannot be granted access to repositories that the installation was not granted access to. Up to 500 repositories can be listed in this manner.
Optionally, use thepermissionsbody parameter to specify the permissions that the installation access token should have. Ifpermissionsis not specified, the installation access token will have all of the permissions that were granted to the app. The installation access token cannot be granted permissions that the app was not granted.
You must use aJWTto access this endpoint.

### Fine-grained access tokens for "Create an installation access token for an app"
This endpoint does not work with GitHub App user access tokens, GitHub App installation access tokens, or fine-grained personal access tokens.

### Parameters for "Create an installation access token for an app"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
installation_idintegerRequiredThe unique identifier of the installation.
[/TABLE]

```
installation_id
```
The unique identifier of the installation.

[TABLE]
Name, Type, Description
repositoriesarray of stringsList of repository names that the token should have access to
repository_idsarray of integersList of repository IDs that the token should have access to
permissionsobjectThe permissions granted to the user access token.
Properties ofpermissionsName, Type, DescriptionactionsstringThe level of permission to grant the access token for GitHub Actions workflows, workflow runs, and artifacts.Can be one of:read,writeadministrationstringThe level of permission to grant the access token for repository creation, deletion, settings, teams, and collaborators creation.Can be one of:read,writeartifact_metadatastringThe level of permission to grant the access token to create and retrieve build artifact metadata records.Can be one of:read,writeattestationsstringThe level of permission to create and retrieve the access token for repository attestations.Can be one of:read,writechecksstringThe level of permission to grant the access token for checks on code.Can be one of:read,writecodespacesstringThe level of permission to grant the access token to create, edit, delete, and list Codespaces.Can be one of:read,writecontentsstringThe level of permission to grant the access token for repository contents, commits, branches, downloads, releases, and merges.Can be one of:read,writedependabot_secretsstringThe level of permission to grant the access token to manage Dependabot secrets.Can be one of:read,writedeploymentsstringThe level of permission to grant the access token for deployments and deployment statuses.Can be one of:read,writediscussionsstringThe level of permission to grant the access token for discussions and related comments and label_filters.Can be one of:read,writeenvironmentsstringThe level of permission to grant the access token for managing repository environments.Can be one of:read,writeissuesstringThe level of permission to grant the access token for issues and related comments, assignees, label_filters, and milestones.Can be one of:read,writemerge_queuesstringThe level of permission to grant the access token to manage the merge queues for a repository.Can be one of:read,writemetadatastringThe level of permission to grant the access token to search repositories, list collaborators, and access repository metadata.Can be one of:read,writepackagesstringThe level of permission to grant the access token for packages published to GitHub Packages.Can be one of:read,writepagesstringThe level of permission to grant the access token to retrieve Pages statuses, configuration, and builds, as well as create new builds.Can be one of:read,writepull_requestsstringThe level of permission to grant the access token for pull requests and related comments, assignees, label_filters, milestones, and merges.Can be one of:read,writerepository_custom_propertiesstringThe level of permission to grant the access token to view and edit custom properties for a repository, when allowed by the property.Can be one of:read,writerepository_hooksstringThe level of permission to grant the access token to manage the post-receive hooks for a repository.Can be one of:read,writerepository_projectsstringThe level of permission to grant the access token to manage repository projects, columns, and cards.Can be one of:read,write,adminsecret_scanning_alertsstringThe level of permission to grant the access token to view and manage secret scanning alerts.Can be one of:read,writesecretsstringThe level of permission to grant the access token to manage repository secrets.Can be one of:read,writesecurity_eventsstringThe level of permission to grant the access token to view and manage security events like code scanning alerts.Can be one of:read,writesingle_filestringThe level of permission to grant the access token to manage just a single file.Can be one of:read,writestatusesstringThe level of permission to grant the access token for commit statuses.Can be one of:read,writevulnerability_alertsstringThe level of permission to grant the access token to manage Dependabot alerts.Can be one of:read,writeworkflowsstringThe level of permission to grant the access token to update GitHub Actions workflow files.Value:writecustom_properties_for_organizationsstringThe level of permission to grant the access token to view and edit custom properties for an organization, when allowed by the property.Can be one of:read,writemembersstringThe level of permission to grant the access token for organization teams and members.Can be one of:read,writeorganization_administrationstringThe level of permission to grant the access token to manage access to an organization.Can be one of:read,writeorganization_custom_rolesstringThe level of permission to grant the access token for custom repository roles management.Can be one of:read,writeorganization_custom_org_rolesstringThe level of permission to grant the access token for custom organization roles management.Can be one of:read,writeorganization_custom_propertiesstringThe level of permission to grant the access token for repository custom properties management at the organization level.Can be one of:read,write,adminorganization_copilot_seat_managementstringThe level of permission to grant the access token for managing access to GitHub Copilot for members of an organization with a Copilot Business subscription. This property is in public preview and is subject to change.Value:writeorganization_copilot_agent_settingsstringThe level of permission to grant the access token to view and manage Copilot coding agent settings for an organization.Can be one of:read,writeorganization_announcement_bannersstringThe level of permission to grant the access token to view and manage announcement banners for an organization.Can be one of:read,writeorganization_eventsstringThe level of permission to grant the access token to view events triggered by an activity in an organization.Value:readorganization_hooksstringThe level of permission to grant the access token to manage the post-receive hooks for an organization.Can be one of:read,writeorganization_personal_access_tokensstringThe level of permission to grant the access token for viewing and managing fine-grained personal access token requests to an organization.Can be one of:read,writeorganization_personal_access_token_requestsstringThe level of permission to grant the access token for viewing and managing fine-grained personal access tokens that have been approved by an organization.Can be one of:read,writeorganization_planstringThe level of permission to grant the access token for viewing an organization's plan.Value:readorganization_projectsstringThe level of permission to grant the access token to manage organization projects and projects public preview (where available).Can be one of:read,write,adminorganization_packagesstringThe level of permission to grant the access token for organization packages published to GitHub Packages.Can be one of:read,writeorganization_secretsstringThe level of permission to grant the access token to manage organization secrets.Can be one of:read,writeorganization_self_hosted_runnersstringThe level of permission to grant the access token to view and manage GitHub Actions self-hosted runners available to an organization.Can be one of:read,writeorganization_user_blockingstringThe level of permission to grant the access token to view and manage users blocked by the organization.Can be one of:read,writeemail_addressesstringThe level of permission to grant the access token to manage the email addresses belonging to a user.Can be one of:read,writefollowersstringThe level of permission to grant the access token to manage the followers belonging to a user.Can be one of:read,writegit_ssh_keysstringThe level of permission to grant the access token to manage git SSH keys.Can be one of:read,writegpg_keysstringThe level of permission to grant the access token to view and manage GPG keys belonging to a user.Can be one of:read,writeinteraction_limitsstringThe level of permission to grant the access token to view and manage interaction limits on a repository.Can be one of:read,writeprofilestringThe level of permission to grant the access token to manage the profile settings belonging to a user.Value:writestarringstringThe level of permission to grant the access token to list and manage repositories a user is starring.Can be one of:read,writeenterprise_custom_properties_for_organizationsstringThe level of permission to grant the access token for organization custom properties management at the enterprise level.Can be one of:read,write,admin | Name, Type, Description | actionsstringThe level of permission to grant the access token for GitHub Actions workflows, workflow runs, and artifacts.Can be one of:read,write | administrationstringThe level of permission to grant the access token for repository creation, deletion, settings, teams, and collaborators creation.Can be one of:read,write | artifact_metadatastringThe level of permission to grant the access token to create and retrieve build artifact metadata records.Can be one of:read,write | attestationsstringThe level of permission to create and retrieve the access token for repository attestations.Can be one of:read,write | checksstringThe level of permission to grant the access token for checks on code.Can be one of:read,write | codespacesstringThe level of permission to grant the access token to create, edit, delete, and list Codespaces.Can be one of:read,write | contentsstringThe level of permission to grant the access token for repository contents, commits, branches, downloads, releases, and merges.Can be one of:read,write | dependabot_secretsstringThe level of permission to grant the access token to manage Dependabot secrets.Can be one of:read,write | deploymentsstringThe level of permission to grant the access token for deployments and deployment statuses.Can be one of:read,write | discussionsstringThe level of permission to grant the access token for discussions and related comments and label_filters.Can be one of:read,write | environmentsstringThe level of permission to grant the access token for managing repository environments.Can be one of:read,write | issuesstringThe level of permission to grant the access token for issues and related comments, assignees, label_filters, and milestones.Can be one of:read,write | merge_queuesstringThe level of permission to grant the access token to manage the merge queues for a repository.Can be one of:read,write | metadatastringThe level of permission to grant the access token to search repositories, list collaborators, and access repository metadata.Can be one of:read,write | packagesstringThe level of permission to grant the access token for packages published to GitHub Packages.Can be one of:read,write | pagesstringThe level of permission to grant the access token to retrieve Pages statuses, configuration, and builds, as well as create new builds.Can be one of:read,write | pull_requestsstringThe level of permission to grant the access token for pull requests and related comments, assignees, label_filters, milestones, and merges.Can be one of:read,write | repository_custom_propertiesstringThe level of permission to grant the access token to view and edit custom properties for a repository, when allowed by the property.Can be one of:read,write | repository_hooksstringThe level of permission to grant the access token to manage the post-receive hooks for a repository.Can be one of:read,write | repository_projectsstringThe level of permission to grant the access token to manage repository projects, columns, and cards.Can be one of:read,write,admin | secret_scanning_alertsstringThe level of permission to grant the access token to view and manage secret scanning alerts.Can be one of:read,write | secretsstringThe level of permission to grant the access token to manage repository secrets.Can be one of:read,write | security_eventsstringThe level of permission to grant the access token to view and manage security events like code scanning alerts.Can be one of:read,write | single_filestringThe level of permission to grant the access token to manage just a single file.Can be one of:read,write | statusesstringThe level of permission to grant the access token for commit statuses.Can be one of:read,write | vulnerability_alertsstringThe level of permission to grant the access token to manage Dependabot alerts.Can be one of:read,write | workflowsstringThe level of permission to grant the access token to update GitHub Actions workflow files.Value:write | custom_properties_for_organizationsstringThe level of permission to grant the access token to view and edit custom properties for an organization, when allowed by the property.Can be one of:read,write | membersstringThe level of permission to grant the access token for organization teams and members.Can be one of:read,write | organization_administrationstringThe level of permission to grant the access token to manage access to an organization.Can be one of:read,write | organization_custom_rolesstringThe level of permission to grant the access token for custom repository roles management.Can be one of:read,write | organization_custom_org_rolesstringThe level of permission to grant the access token for custom organization roles management.Can be one of:read,write | organization_custom_propertiesstringThe level of permission to grant the access token for repository custom properties management at the organization level.Can be one of:read,write,admin | organization_copilot_seat_managementstringThe level of permission to grant the access token for managing access to GitHub Copilot for members of an organization with a Copilot Business subscription. This property is in public preview and is subject to change.Value:write | organization_copilot_agent_settingsstringThe level of permission to grant the access token to view and manage Copilot coding agent settings for an organization.Can be one of:read,write | organization_announcement_bannersstringThe level of permission to grant the access token to view and manage announcement banners for an organization.Can be one of:read,write | organization_eventsstringThe level of permission to grant the access token to view events triggered by an activity in an organization.Value:read | organization_hooksstringThe level of permission to grant the access token to manage the post-receive hooks for an organization.Can be one of:read,write | organization_personal_access_tokensstringThe level of permission to grant the access token for viewing and managing fine-grained personal access token requests to an organization.Can be one of:read,write | organization_personal_access_token_requestsstringThe level of permission to grant the access token for viewing and managing fine-grained personal access tokens that have been approved by an organization.Can be one of:read,write | organization_planstringThe level of permission to grant the access token for viewing an organization's plan.Value:read | organization_projectsstringThe level of permission to grant the access token to manage organization projects and projects public preview (where available).Can be one of:read,write,admin | organization_packagesstringThe level of permission to grant the access token for organization packages published to GitHub Packages.Can be one of:read,write | organization_secretsstringThe level of permission to grant the access token to manage organization secrets.Can be one of:read,write | organization_self_hosted_runnersstringThe level of permission to grant the access token to view and manage GitHub Actions self-hosted runners available to an organization.Can be one of:read,write | organization_user_blockingstringThe level of permission to grant the access token to view and manage users blocked by the organization.Can be one of:read,write | email_addressesstringThe level of permission to grant the access token to manage the email addresses belonging to a user.Can be one of:read,write | followersstringThe level of permission to grant the access token to manage the followers belonging to a user.Can be one of:read,write | git_ssh_keysstringThe level of permission to grant the access token to manage git SSH keys.Can be one of:read,write | gpg_keysstringThe level of permission to grant the access token to view and manage GPG keys belonging to a user.Can be one of:read,write | interaction_limitsstringThe level of permission to grant the access token to view and manage interaction limits on a repository.Can be one of:read,write | profilestringThe level of permission to grant the access token to manage the profile settings belonging to a user.Value:write | starringstringThe level of permission to grant the access token to list and manage repositories a user is starring.Can be one of:read,write | enterprise_custom_properties_for_organizationsstringThe level of permission to grant the access token for organization custom properties management at the enterprise level.Can be one of:read,write,admin
Name, Type, Description
actionsstringThe level of permission to grant the access token for GitHub Actions workflows, workflow runs, and artifacts.Can be one of:read,write
administrationstringThe level of permission to grant the access token for repository creation, deletion, settings, teams, and collaborators creation.Can be one of:read,write
artifact_metadatastringThe level of permission to grant the access token to create and retrieve build artifact metadata records.Can be one of:read,write
attestationsstringThe level of permission to create and retrieve the access token for repository attestations.Can be one of:read,write
checksstringThe level of permission to grant the access token for checks on code.Can be one of:read,write
codespacesstringThe level of permission to grant the access token to create, edit, delete, and list Codespaces.Can be one of:read,write
contentsstringThe level of permission to grant the access token for repository contents, commits, branches, downloads, releases, and merges.Can be one of:read,write
dependabot_secretsstringThe level of permission to grant the access token to manage Dependabot secrets.Can be one of:read,write
deploymentsstringThe level of permission to grant the access token for deployments and deployment statuses.Can be one of:read,write
discussionsstringThe level of permission to grant the access token for discussions and related comments and label_filters.Can be one of:read,write
environmentsstringThe level of permission to grant the access token for managing repository environments.Can be one of:read,write
issuesstringThe level of permission to grant the access token for issues and related comments, assignees, label_filters, and milestones.Can be one of:read,write
merge_queuesstringThe level of permission to grant the access token to manage the merge queues for a repository.Can be one of:read,write
metadatastringThe level of permission to grant the access token to search repositories, list collaborators, and access repository metadata.Can be one of:read,write
packagesstringThe level of permission to grant the access token for packages published to GitHub Packages.Can be one of:read,write
pagesstringThe level of permission to grant the access token to retrieve Pages statuses, configuration, and builds, as well as create new builds.Can be one of:read,write
pull_requestsstringThe level of permission to grant the access token for pull requests and related comments, assignees, label_filters, milestones, and merges.Can be one of:read,write
repository_custom_propertiesstringThe level of permission to grant the access token to view and edit custom properties for a repository, when allowed by the property.Can be one of:read,write
repository_hooksstringThe level of permission to grant the access token to manage the post-receive hooks for a repository.Can be one of:read,write
repository_projectsstringThe level of permission to grant the access token to manage repository projects, columns, and cards.Can be one of:read,write,admin
secret_scanning_alertsstringThe level of permission to grant the access token to view and manage secret scanning alerts.Can be one of:read,write
secretsstringThe level of permission to grant the access token to manage repository secrets.Can be one of:read,write
security_eventsstringThe level of permission to grant the access token to view and manage security events like code scanning alerts.Can be one of:read,write
single_filestringThe level of permission to grant the access token to manage just a single file.Can be one of:read,write
statusesstringThe level of permission to grant the access token for commit statuses.Can be one of:read,write
vulnerability_alertsstringThe level of permission to grant the access token to manage Dependabot alerts.Can be one of:read,write
workflowsstringThe level of permission to grant the access token to update GitHub Actions workflow files.Value:write
custom_properties_for_organizationsstringThe level of permission to grant the access token to view and edit custom properties for an organization, when allowed by the property.Can be one of:read,write
membersstringThe level of permission to grant the access token for organization teams and members.Can be one of:read,write
organization_administrationstringThe level of permission to grant the access token to manage access to an organization.Can be one of:read,write
organization_custom_rolesstringThe level of permission to grant the access token for custom repository roles management.Can be one of:read,write
organization_custom_org_rolesstringThe level of permission to grant the access token for custom organization roles management.Can be one of:read,write
organization_custom_propertiesstringThe level of permission to grant the access token for repository custom properties management at the organization level.Can be one of:read,write,admin
organization_copilot_seat_managementstringThe level of permission to grant the access token for managing access to GitHub Copilot for members of an organization with a Copilot Business subscription. This property is in public preview and is subject to change.Value:write
organization_copilot_agent_settingsstringThe level of permission to grant the access token to view and manage Copilot coding agent settings for an organization.Can be one of:read,write
organization_announcement_bannersstringThe level of permission to grant the access token to view and manage announcement banners for an organization.Can be one of:read,write
organization_eventsstringThe level of permission to grant the access token to view events triggered by an activity in an organization.Value:read
organization_hooksstringThe level of permission to grant the access token to manage the post-receive hooks for an organization.Can be one of:read,write
organization_personal_access_tokensstringThe level of permission to grant the access token for viewing and managing fine-grained personal access token requests to an organization.Can be one of:read,write
organization_personal_access_token_requestsstringThe level of permission to grant the access token for viewing and managing fine-grained personal access tokens that have been approved by an organization.Can be one of:read,write
organization_planstringThe level of permission to grant the access token for viewing an organization's plan.Value:read
organization_projectsstringThe level of permission to grant the access token to manage organization projects and projects public preview (where available).Can be one of:read,write,admin
organization_packagesstringThe level of permission to grant the access token for organization packages published to GitHub Packages.Can be one of:read,write
organization_secretsstringThe level of permission to grant the access token to manage organization secrets.Can be one of:read,write
organization_self_hosted_runnersstringThe level of permission to grant the access token to view and manage GitHub Actions self-hosted runners available to an organization.Can be one of:read,write
organization_user_blockingstringThe level of permission to grant the access token to view and manage users blocked by the organization.Can be one of:read,write
email_addressesstringThe level of permission to grant the access token to manage the email addresses belonging to a user.Can be one of:read,write
followersstringThe level of permission to grant the access token to manage the followers belonging to a user.Can be one of:read,write
git_ssh_keysstringThe level of permission to grant the access token to manage git SSH keys.Can be one of:read,write
gpg_keysstringThe level of permission to grant the access token to view and manage GPG keys belonging to a user.Can be one of:read,write
interaction_limitsstringThe level of permission to grant the access token to view and manage interaction limits on a repository.Can be one of:read,write
profilestringThe level of permission to grant the access token to manage the profile settings belonging to a user.Value:write
starringstringThe level of permission to grant the access token to list and manage repositories a user is starring.Can be one of:read,write
enterprise_custom_properties_for_organizationsstringThe level of permission to grant the access token for organization custom properties management at the enterprise level.Can be one of:read,write,admin
[/TABLE]

```
repositories
```
List of repository names that the token should have access to

```
repository_ids
```
List of repository IDs that the token should have access to

```
permissions
```
The permissions granted to the user access token.

```
permissions
```

[TABLE]
Name, Type, Description
actionsstringThe level of permission to grant the access token for GitHub Actions workflows, workflow runs, and artifacts.Can be one of:read,write
administrationstringThe level of permission to grant the access token for repository creation, deletion, settings, teams, and collaborators creation.Can be one of:read,write
artifact_metadatastringThe level of permission to grant the access token to create and retrieve build artifact metadata records.Can be one of:read,write
attestationsstringThe level of permission to create and retrieve the access token for repository attestations.Can be one of:read,write
checksstringThe level of permission to grant the access token for checks on code.Can be one of:read,write
codespacesstringThe level of permission to grant the access token to create, edit, delete, and list Codespaces.Can be one of:read,write
contentsstringThe level of permission to grant the access token for repository contents, commits, branches, downloads, releases, and merges.Can be one of:read,write
dependabot_secretsstringThe level of permission to grant the access token to manage Dependabot secrets.Can be one of:read,write
deploymentsstringThe level of permission to grant the access token for deployments and deployment statuses.Can be one of:read,write
discussionsstringThe level of permission to grant the access token for discussions and related comments and label_filters.Can be one of:read,write
environmentsstringThe level of permission to grant the access token for managing repository environments.Can be one of:read,write
issuesstringThe level of permission to grant the access token for issues and related comments, assignees, label_filters, and milestones.Can be one of:read,write
merge_queuesstringThe level of permission to grant the access token to manage the merge queues for a repository.Can be one of:read,write
metadatastringThe level of permission to grant the access token to search repositories, list collaborators, and access repository metadata.Can be one of:read,write
packagesstringThe level of permission to grant the access token for packages published to GitHub Packages.Can be one of:read,write
pagesstringThe level of permission to grant the access token to retrieve Pages statuses, configuration, and builds, as well as create new builds.Can be one of:read,write
pull_requestsstringThe level of permission to grant the access token for pull requests and related comments, assignees, label_filters, milestones, and merges.Can be one of:read,write
repository_custom_propertiesstringThe level of permission to grant the access token to view and edit custom properties for a repository, when allowed by the property.Can be one of:read,write
repository_hooksstringThe level of permission to grant the access token to manage the post-receive hooks for a repository.Can be one of:read,write
repository_projectsstringThe level of permission to grant the access token to manage repository projects, columns, and cards.Can be one of:read,write,admin
secret_scanning_alertsstringThe level of permission to grant the access token to view and manage secret scanning alerts.Can be one of:read,write
secretsstringThe level of permission to grant the access token to manage repository secrets.Can be one of:read,write
security_eventsstringThe level of permission to grant the access token to view and manage security events like code scanning alerts.Can be one of:read,write
single_filestringThe level of permission to grant the access token to manage just a single file.Can be one of:read,write
statusesstringThe level of permission to grant the access token for commit statuses.Can be one of:read,write
vulnerability_alertsstringThe level of permission to grant the access token to manage Dependabot alerts.Can be one of:read,write
workflowsstringThe level of permission to grant the access token to update GitHub Actions workflow files.Value:write
custom_properties_for_organizationsstringThe level of permission to grant the access token to view and edit custom properties for an organization, when allowed by the property.Can be one of:read,write
membersstringThe level of permission to grant the access token for organization teams and members.Can be one of:read,write
organization_administrationstringThe level of permission to grant the access token to manage access to an organization.Can be one of:read,write
organization_custom_rolesstringThe level of permission to grant the access token for custom repository roles management.Can be one of:read,write
organization_custom_org_rolesstringThe level of permission to grant the access token for custom organization roles management.Can be one of:read,write
organization_custom_propertiesstringThe level of permission to grant the access token for repository custom properties management at the organization level.Can be one of:read,write,admin
organization_copilot_seat_managementstringThe level of permission to grant the access token for managing access to GitHub Copilot for members of an organization with a Copilot Business subscription. This property is in public preview and is subject to change.Value:write
organization_copilot_agent_settingsstringThe level of permission to grant the access token to view and manage Copilot coding agent settings for an organization.Can be one of:read,write
organization_announcement_bannersstringThe level of permission to grant the access token to view and manage announcement banners for an organization.Can be one of:read,write
organization_eventsstringThe level of permission to grant the access token to view events triggered by an activity in an organization.Value:read
organization_hooksstringThe level of permission to grant the access token to manage the post-receive hooks for an organization.Can be one of:read,write
organization_personal_access_tokensstringThe level of permission to grant the access token for viewing and managing fine-grained personal access token requests to an organization.Can be one of:read,write
organization_personal_access_token_requestsstringThe level of permission to grant the access token for viewing and managing fine-grained personal access tokens that have been approved by an organization.Can be one of:read,write
organization_planstringThe level of permission to grant the access token for viewing an organization's plan.Value:read
organization_projectsstringThe level of permission to grant the access token to manage organization projects and projects public preview (where available).Can be one of:read,write,admin
organization_packagesstringThe level of permission to grant the access token for organization packages published to GitHub Packages.Can be one of:read,write
organization_secretsstringThe level of permission to grant the access token to manage organization secrets.Can be one of:read,write
organization_self_hosted_runnersstringThe level of permission to grant the access token to view and manage GitHub Actions self-hosted runners available to an organization.Can be one of:read,write
organization_user_blockingstringThe level of permission to grant the access token to view and manage users blocked by the organization.Can be one of:read,write
email_addressesstringThe level of permission to grant the access token to manage the email addresses belonging to a user.Can be one of:read,write
followersstringThe level of permission to grant the access token to manage the followers belonging to a user.Can be one of:read,write
git_ssh_keysstringThe level of permission to grant the access token to manage git SSH keys.Can be one of:read,write
gpg_keysstringThe level of permission to grant the access token to view and manage GPG keys belonging to a user.Can be one of:read,write
interaction_limitsstringThe level of permission to grant the access token to view and manage interaction limits on a repository.Can be one of:read,write
profilestringThe level of permission to grant the access token to manage the profile settings belonging to a user.Value:write
starringstringThe level of permission to grant the access token to list and manage repositories a user is starring.Can be one of:read,write
enterprise_custom_properties_for_organizationsstringThe level of permission to grant the access token for organization custom properties management at the enterprise level.Can be one of:read,write,admin
[/TABLE]
The level of permission to grant the access token for GitHub Actions workflows, workflow runs, and artifacts.
Can be one of:read,write

```
administration
```
The level of permission to grant the access token for repository creation, deletion, settings, teams, and collaborators creation.
Can be one of:read,write

```
artifact_metadata
```
The level of permission to grant the access token to create and retrieve build artifact metadata records.
Can be one of:read,write

```
attestations
```
The level of permission to create and retrieve the access token for repository attestations.
Can be one of:read,write
The level of permission to grant the access token for checks on code.
Can be one of:read,write
The level of permission to grant the access token to create, edit, delete, and list Codespaces.
Can be one of:read,write
The level of permission to grant the access token for repository contents, commits, branches, downloads, releases, and merges.
Can be one of:read,write

```
dependabot_secrets
```
The level of permission to grant the access token to manage Dependabot secrets.
Can be one of:read,write

```
deployments
```
The level of permission to grant the access token for deployments and deployment statuses.
Can be one of:read,write

```
discussions
```
The level of permission to grant the access token for discussions and related comments and label_filters.
Can be one of:read,write

```
environments
```
The level of permission to grant the access token for managing repository environments.
Can be one of:read,write
The level of permission to grant the access token for issues and related comments, assignees, label_filters, and milestones.
Can be one of:read,write

```
merge_queues
```
The level of permission to grant the access token to manage the merge queues for a repository.
Can be one of:read,write
The level of permission to grant the access token to search repositories, list collaborators, and access repository metadata.
Can be one of:read,write
The level of permission to grant the access token for packages published to GitHub Packages.
Can be one of:read,write
The level of permission to grant the access token to retrieve Pages statuses, configuration, and builds, as well as create new builds.
Can be one of:read,write

```
pull_requests
```
The level of permission to grant the access token for pull requests and related comments, assignees, label_filters, milestones, and merges.
Can be one of:read,write

```
repository_custom_properties
```
The level of permission to grant the access token to view and edit custom properties for a repository, when allowed by the property.
Can be one of:read,write

```
repository_hooks
```
The level of permission to grant the access token to manage the post-receive hooks for a repository.
Can be one of:read,write

```
repository_projects
```
The level of permission to grant the access token to manage repository projects, columns, and cards.
Can be one of:read,write,admin

```
secret_scanning_alerts
```
The level of permission to grant the access token to view and manage secret scanning alerts.
Can be one of:read,write
The level of permission to grant the access token to manage repository secrets.
Can be one of:read,write

```
security_events
```
The level of permission to grant the access token to view and manage security events like code scanning alerts.
Can be one of:read,write

```
single_file
```
The level of permission to grant the access token to manage just a single file.
Can be one of:read,write
The level of permission to grant the access token for commit statuses.
Can be one of:read,write

```
vulnerability_alerts
```
The level of permission to grant the access token to manage Dependabot alerts.
Can be one of:read,write
The level of permission to grant the access token to update GitHub Actions workflow files.
Value:write

```
custom_properties_for_organizations
```
The level of permission to grant the access token to view and edit custom properties for an organization, when allowed by the property.
Can be one of:read,write
The level of permission to grant the access token for organization teams and members.
Can be one of:read,write

```
organization_administration
```
The level of permission to grant the access token to manage access to an organization.
Can be one of:read,write

```
organization_custom_roles
```
The level of permission to grant the access token for custom repository roles management.
Can be one of:read,write

```
organization_custom_org_roles
```
The level of permission to grant the access token for custom organization roles management.
Can be one of:read,write

```
organization_custom_properties
```
The level of permission to grant the access token for repository custom properties management at the organization level.
Can be one of:read,write,admin

```
organization_copilot_seat_management
```
The level of permission to grant the access token for managing access to GitHub Copilot for members of an organization with a Copilot Business subscription. This property is in public preview and is subject to change.
Value:write

```
organization_copilot_agent_settings
```
The level of permission to grant the access token to view and manage Copilot coding agent settings for an organization.
Can be one of:read,write

```
organization_announcement_banners
```
The level of permission to grant the access token to view and manage announcement banners for an organization.
Can be one of:read,write

```
organization_events
```
The level of permission to grant the access token to view events triggered by an activity in an organization.
Value:read

```
organization_hooks
```
The level of permission to grant the access token to manage the post-receive hooks for an organization.
Can be one of:read,write

```
organization_personal_access_tokens
```
The level of permission to grant the access token for viewing and managing fine-grained personal access token requests to an organization.
Can be one of:read,write

```
organization_personal_access_token_requests
```
The level of permission to grant the access token for viewing and managing fine-grained personal access tokens that have been approved by an organization.
Can be one of:read,write

```
organization_plan
```
The level of permission to grant the access token for viewing an organization's plan.
Value:read

```
organization_projects
```
The level of permission to grant the access token to manage organization projects and projects public preview (where available).
Can be one of:read,write,admin

```
organization_packages
```
The level of permission to grant the access token for organization packages published to GitHub Packages.
Can be one of:read,write

```
organization_secrets
```
The level of permission to grant the access token to manage organization secrets.
Can be one of:read,write

```
organization_self_hosted_runners
```
The level of permission to grant the access token to view and manage GitHub Actions self-hosted runners available to an organization.
Can be one of:read,write

```
organization_user_blocking
```
The level of permission to grant the access token to view and manage users blocked by the organization.
Can be one of:read,write

```
email_addresses
```
The level of permission to grant the access token to manage the email addresses belonging to a user.
Can be one of:read,write
The level of permission to grant the access token to manage the followers belonging to a user.
Can be one of:read,write

```
git_ssh_keys
```
The level of permission to grant the access token to manage git SSH keys.
Can be one of:read,write
The level of permission to grant the access token to view and manage GPG keys belonging to a user.
Can be one of:read,write

```
interaction_limits
```
The level of permission to grant the access token to view and manage interaction limits on a repository.
Can be one of:read,write
The level of permission to grant the access token to manage the profile settings belonging to a user.
Value:write
The level of permission to grant the access token to list and manage repositories a user is starring.
Can be one of:read,write

```
enterprise_custom_properties_for_organizations
```
The level of permission to grant the access token for organization custom properties management at the enterprise level.
Can be one of:read,write,admin

### HTTP response status codes for "Create an installation access token for an app"

[TABLE]
Status code | Description
201 | Created
401 | Requires authentication
403 | Forbidden
404 | Resource not found
422 | Validation failed, or the endpoint has been spammed.
[/TABLE]
Created
Requires authentication
Forbidden
Resource not found
Validation failed, or the endpoint has been spammed.

### Code samples for "Create an installation access token for an app"

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
  https://api.github.com/app/installations/1/access_tokens \
  -d '{"repositories":["Hello-World"],"permissions":{"issues":"write","contents":"read"}}'
```

#### Response
- Example response
- Response schema

```
Status: 201
```

```
{
  "token": "ghs_16C7e42F292c6912E7710c838347Ae178B4a",
  "expires_at": "2016-07-11T22:14:10Z",
  "permissions": {
    "issues": "write",
    "contents": "read"
  },
  "repository_selection": "selected",
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
      "blobs_url": "https://api.github.com/repos/octocat/Hello-World/git/blobs{/commit_sha}",
      "branches_url": "https://api.github.com/repos/octocat/Hello-World/branches{/branch}",
      "collaborators_url": "https://api.github.com/repos/octocat/Hello-World/collaborators{/collaborator}",
      "comments_url": "https://api.github.com/repos/octocat/Hello-World/comments{/number}",
      "commits_url": "https://api.github.com/repos/octocat/Hello-World/commits{/commit_sha}",
      "compare_url": "https://api.github.com/repos/octocat/Hello-World/compare/{base}...{head}",
      "contents_url": "https://api.github.com/repos/octocat/Hello-World/contents/{+path}",
      "contributors_url": "https://api.github.com/repos/octocat/Hello-World/contributors",
      "deployments_url": "https://api.github.com/repos/octocat/Hello-World/deployments",
      "downloads_url": "https://api.github.com/repos/octocat/Hello-World/downloads",
      "events_url": "https://api.github.com/repos/octocat/Hello-World/events",
      "forks_url": "https://api.github.com/repos/octocat/Hello-World/forks",
      "git_commits_url": "https://api.github.com/repos/octocat/Hello-World/git/commits{/commit_sha}",
      "git_refs_url": "https://api.github.com/repos/octocat/Hello-World/git/refs{/commit_sha}",
      "git_tags_url": "https://api.github.com/repos/octocat/Hello-World/git/tags{/commit_sha}",
      "git_url": "git:github.com/octocat/Hello-World.git",
      "issue_comment_url": "https://api.github.com/repos/octocat/Hello-World/issues/comments{/number}",
      "issue_events_url": "https://api.github.com/repos/octocat/Hello-World/issues/events{/number}",
      "issues_url": "https://api.github.com/repos/octocat/Hello-World/issues{/number}",
      "keys_url": "https://api.github.com/repos/octocat/Hello-World/keys{/key_id}",
      "labels_url": "https://api.github.com/repos/octocat/Hello-World/label_filters{/name}",
      "languages_url": "https://api.github.com/repos/octocat/Hello-World/languages",
      "merges_url": "https://api.github.com/repos/octocat/Hello-World/merges",
      "milestones_url": "https://api.github.com/repos/octocat/Hello-World/milestones{/number}",
      "notifications_url": "https://api.github.com/repos/octocat/Hello-World/notifications{?since,all,participating}",
      "pulls_url": "https://api.github.com/repos/octocat/Hello-World/pulls{/number}",
      "releases_url": "https://api.github.com/repos/octocat/Hello-World/releases{/id}",
      "ssh_url": "git@github.com:octocat/Hello-World.git",
      "stargazers_url": "https://api.github.com/repos/octocat/Hello-World/stargazers",
      "statuses_url": "https://api.github.com/repos/octocat/Hello-World/statuses/{commit_sha}",
      "subscribers_url": "https://api.github.com/repos/octocat/Hello-World/subscribers",
      "subscription_url": "https://api.github.com/repos/octocat/Hello-World/subscription",
      "tags_url": "https://api.github.com/repos/octocat/Hello-World/tags",
      "teams_url": "https://api.github.com/repos/octocat/Hello-World/teams",
      "trees_url": "https://api.github.com/repos/octocat/Hello-World/git/trees{/commit_sha}",
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
      "allow_rebase_merge": true,
      "template_repository": null,
      "temp_clone_token": "ABTLWHOULUVAXGTRYU7OC2876QJ2O",
      "allow_squash_merge": true,
      "allow_auto_merge": false,
      "delete_branch_on_merge": true,
      "allow_merge_commit": true,
      "subscribers_count": 42,
      "network_count": 0,
      "license": {
        "key": "mit",
        "name": "MIT License",
        "url": "https://api.github.com/licenses/mit",
        "spdx_id": "MIT",
        "node_id": "MDc6TGljZW5zZW1pdA==",
        "html_url": "https://github.com/licenses/mit"
      },
      "forks": 1,
      "open_issues": 1,
      "watchers": 1
    }
  ]
}
```

## Suspend an app installation
Suspends a GitHub App on a user, organization, or enterprise account, which blocks the app from accessing the account's resources. When a GitHub App is suspended, the app's access to the GitHub API or webhook events is blocked for that account.
You must use aJWTto access this endpoint.

### Fine-grained access tokens for "Suspend an app installation"
This endpoint does not work with GitHub App user access tokens, GitHub App installation access tokens, or fine-grained personal access tokens.

### Parameters for "Suspend an app installation"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
installation_idintegerRequiredThe unique identifier of the installation.
[/TABLE]

```
installation_id
```
The unique identifier of the installation.

### HTTP response status codes for "Suspend an app installation"

[TABLE]
Status code | Description
204 | No Content
404 | Resource not found
[/TABLE]
No Content
Resource not found

### Code samples for "Suspend an app installation"

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
  https://api.github.com/app/installations/1/suspended
```

#### Response

```
Status: 204
```

## Unsuspend an app installation
Removes a GitHub App installation suspension.
You must use aJWTto access this endpoint.

### Fine-grained access tokens for "Unsuspend an app installation"
This endpoint does not work with GitHub App user access tokens, GitHub App installation access tokens, or fine-grained personal access tokens.

### Parameters for "Unsuspend an app installation"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
installation_idintegerRequiredThe unique identifier of the installation.
[/TABLE]

```
installation_id
```
The unique identifier of the installation.

### HTTP response status codes for "Unsuspend an app installation"

[TABLE]
Status code | Description
204 | No Content
404 | Resource not found
[/TABLE]
No Content
Resource not found

### Code samples for "Unsuspend an app installation"

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
  https://api.github.com/app/installations/1/suspended
```

#### Response

```
Status: 204
```

## Create a scoped access token
Use a non-scoped user access token to create a repository-scoped and/or permission-scoped user access token. You can specify
which repositories the token can access and which permissions are granted to the
token.
Invalid tokens will return404 NOT FOUND.

### Basic authentication for "Create a scoped access token"
You must useBasic Authenticationto use this endpoint. Use the application'sclient_idas the username and theclient_secretas the password.

### Parameters for "Create a scoped access token"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
client_idstringRequiredThe client ID of the GitHub app.
[/TABLE]
The client ID of the GitHub app.

[TABLE]
Name, Type, Description
access_tokenstringRequiredThe access token used to authenticate to the GitHub API.
targetstringThe name of the user or organization to scope the user access token to.Requiredunlesstarget_idis specified.
target_idintegerThe ID of the user or organization to scope the user access token to.Requiredunlesstargetis specified.
repositoriesarray of stringsThe list of repository names to scope the user access token to.repositoriesmay not be specified ifrepository_idsis specified.
repository_idsarray of integersThe list of repository IDs to scope the user access token to.repository_idsmay not be specified ifrepositoriesis specified.
permissionsobjectThe permissions granted to the user access token.
Properties ofpermissionsName, Type, DescriptionactionsstringThe level of permission to grant the access token for GitHub Actions workflows, workflow runs, and artifacts.Can be one of:read,writeadministrationstringThe level of permission to grant the access token for repository creation, deletion, settings, teams, and collaborators creation.Can be one of:read,writeartifact_metadatastringThe level of permission to grant the access token to create and retrieve build artifact metadata records.Can be one of:read,writeattestationsstringThe level of permission to create and retrieve the access token for repository attestations.Can be one of:read,writechecksstringThe level of permission to grant the access token for checks on code.Can be one of:read,writecodespacesstringThe level of permission to grant the access token to create, edit, delete, and list Codespaces.Can be one of:read,writecontentsstringThe level of permission to grant the access token for repository contents, commits, branches, downloads, releases, and merges.Can be one of:read,writedependabot_secretsstringThe level of permission to grant the access token to manage Dependabot secrets.Can be one of:read,writedeploymentsstringThe level of permission to grant the access token for deployments and deployment statuses.Can be one of:read,writediscussionsstringThe level of permission to grant the access token for discussions and related comments and label_filters.Can be one of:read,writeenvironmentsstringThe level of permission to grant the access token for managing repository environments.Can be one of:read,writeissuesstringThe level of permission to grant the access token for issues and related comments, assignees, label_filters, and milestones.Can be one of:read,writemerge_queuesstringThe level of permission to grant the access token to manage the merge queues for a repository.Can be one of:read,writemetadatastringThe level of permission to grant the access token to search repositories, list collaborators, and access repository metadata.Can be one of:read,writepackagesstringThe level of permission to grant the access token for packages published to GitHub Packages.Can be one of:read,writepagesstringThe level of permission to grant the access token to retrieve Pages statuses, configuration, and builds, as well as create new builds.Can be one of:read,writepull_requestsstringThe level of permission to grant the access token for pull requests and related comments, assignees, label_filters, milestones, and merges.Can be one of:read,writerepository_custom_propertiesstringThe level of permission to grant the access token to view and edit custom properties for a repository, when allowed by the property.Can be one of:read,writerepository_hooksstringThe level of permission to grant the access token to manage the post-receive hooks for a repository.Can be one of:read,writerepository_projectsstringThe level of permission to grant the access token to manage repository projects, columns, and cards.Can be one of:read,write,adminsecret_scanning_alertsstringThe level of permission to grant the access token to view and manage secret scanning alerts.Can be one of:read,writesecretsstringThe level of permission to grant the access token to manage repository secrets.Can be one of:read,writesecurity_eventsstringThe level of permission to grant the access token to view and manage security events like code scanning alerts.Can be one of:read,writesingle_filestringThe level of permission to grant the access token to manage just a single file.Can be one of:read,writestatusesstringThe level of permission to grant the access token for commit statuses.Can be one of:read,writevulnerability_alertsstringThe level of permission to grant the access token to manage Dependabot alerts.Can be one of:read,writeworkflowsstringThe level of permission to grant the access token to update GitHub Actions workflow files.Value:writecustom_properties_for_organizationsstringThe level of permission to grant the access token to view and edit custom properties for an organization, when allowed by the property.Can be one of:read,writemembersstringThe level of permission to grant the access token for organization teams and members.Can be one of:read,writeorganization_administrationstringThe level of permission to grant the access token to manage access to an organization.Can be one of:read,writeorganization_custom_rolesstringThe level of permission to grant the access token for custom repository roles management.Can be one of:read,writeorganization_custom_org_rolesstringThe level of permission to grant the access token for custom organization roles management.Can be one of:read,writeorganization_custom_propertiesstringThe level of permission to grant the access token for repository custom properties management at the organization level.Can be one of:read,write,adminorganization_copilot_seat_managementstringThe level of permission to grant the access token for managing access to GitHub Copilot for members of an organization with a Copilot Business subscription. This property is in public preview and is subject to change.Value:writeorganization_copilot_agent_settingsstringThe level of permission to grant the access token to view and manage Copilot coding agent settings for an organization.Can be one of:read,writeorganization_announcement_bannersstringThe level of permission to grant the access token to view and manage announcement banners for an organization.Can be one of:read,writeorganization_eventsstringThe level of permission to grant the access token to view events triggered by an activity in an organization.Value:readorganization_hooksstringThe level of permission to grant the access token to manage the post-receive hooks for an organization.Can be one of:read,writeorganization_personal_access_tokensstringThe level of permission to grant the access token for viewing and managing fine-grained personal access token requests to an organization.Can be one of:read,writeorganization_personal_access_token_requestsstringThe level of permission to grant the access token for viewing and managing fine-grained personal access tokens that have been approved by an organization.Can be one of:read,writeorganization_planstringThe level of permission to grant the access token for viewing an organization's plan.Value:readorganization_projectsstringThe level of permission to grant the access token to manage organization projects and projects public preview (where available).Can be one of:read,write,adminorganization_packagesstringThe level of permission to grant the access token for organization packages published to GitHub Packages.Can be one of:read,writeorganization_secretsstringThe level of permission to grant the access token to manage organization secrets.Can be one of:read,writeorganization_self_hosted_runnersstringThe level of permission to grant the access token to view and manage GitHub Actions self-hosted runners available to an organization.Can be one of:read,writeorganization_user_blockingstringThe level of permission to grant the access token to view and manage users blocked by the organization.Can be one of:read,writeemail_addressesstringThe level of permission to grant the access token to manage the email addresses belonging to a user.Can be one of:read,writefollowersstringThe level of permission to grant the access token to manage the followers belonging to a user.Can be one of:read,writegit_ssh_keysstringThe level of permission to grant the access token to manage git SSH keys.Can be one of:read,writegpg_keysstringThe level of permission to grant the access token to view and manage GPG keys belonging to a user.Can be one of:read,writeinteraction_limitsstringThe level of permission to grant the access token to view and manage interaction limits on a repository.Can be one of:read,writeprofilestringThe level of permission to grant the access token to manage the profile settings belonging to a user.Value:writestarringstringThe level of permission to grant the access token to list and manage repositories a user is starring.Can be one of:read,writeenterprise_custom_properties_for_organizationsstringThe level of permission to grant the access token for organization custom properties management at the enterprise level.Can be one of:read,write,admin | Name, Type, Description | actionsstringThe level of permission to grant the access token for GitHub Actions workflows, workflow runs, and artifacts.Can be one of:read,write | administrationstringThe level of permission to grant the access token for repository creation, deletion, settings, teams, and collaborators creation.Can be one of:read,write | artifact_metadatastringThe level of permission to grant the access token to create and retrieve build artifact metadata records.Can be one of:read,write | attestationsstringThe level of permission to create and retrieve the access token for repository attestations.Can be one of:read,write | checksstringThe level of permission to grant the access token for checks on code.Can be one of:read,write | codespacesstringThe level of permission to grant the access token to create, edit, delete, and list Codespaces.Can be one of:read,write | contentsstringThe level of permission to grant the access token for repository contents, commits, branches, downloads, releases, and merges.Can be one of:read,write | dependabot_secretsstringThe level of permission to grant the access token to manage Dependabot secrets.Can be one of:read,write | deploymentsstringThe level of permission to grant the access token for deployments and deployment statuses.Can be one of:read,write | discussionsstringThe level of permission to grant the access token for discussions and related comments and label_filters.Can be one of:read,write | environmentsstringThe level of permission to grant the access token for managing repository environments.Can be one of:read,write | issuesstringThe level of permission to grant the access token for issues and related comments, assignees, label_filters, and milestones.Can be one of:read,write | merge_queuesstringThe level of permission to grant the access token to manage the merge queues for a repository.Can be one of:read,write | metadatastringThe level of permission to grant the access token to search repositories, list collaborators, and access repository metadata.Can be one of:read,write | packagesstringThe level of permission to grant the access token for packages published to GitHub Packages.Can be one of:read,write | pagesstringThe level of permission to grant the access token to retrieve Pages statuses, configuration, and builds, as well as create new builds.Can be one of:read,write | pull_requestsstringThe level of permission to grant the access token for pull requests and related comments, assignees, label_filters, milestones, and merges.Can be one of:read,write | repository_custom_propertiesstringThe level of permission to grant the access token to view and edit custom properties for a repository, when allowed by the property.Can be one of:read,write | repository_hooksstringThe level of permission to grant the access token to manage the post-receive hooks for a repository.Can be one of:read,write | repository_projectsstringThe level of permission to grant the access token to manage repository projects, columns, and cards.Can be one of:read,write,admin | secret_scanning_alertsstringThe level of permission to grant the access token to view and manage secret scanning alerts.Can be one of:read,write | secretsstringThe level of permission to grant the access token to manage repository secrets.Can be one of:read,write | security_eventsstringThe level of permission to grant the access token to view and manage security events like code scanning alerts.Can be one of:read,write | single_filestringThe level of permission to grant the access token to manage just a single file.Can be one of:read,write | statusesstringThe level of permission to grant the access token for commit statuses.Can be one of:read,write | vulnerability_alertsstringThe level of permission to grant the access token to manage Dependabot alerts.Can be one of:read,write | workflowsstringThe level of permission to grant the access token to update GitHub Actions workflow files.Value:write | custom_properties_for_organizationsstringThe level of permission to grant the access token to view and edit custom properties for an organization, when allowed by the property.Can be one of:read,write | membersstringThe level of permission to grant the access token for organization teams and members.Can be one of:read,write | organization_administrationstringThe level of permission to grant the access token to manage access to an organization.Can be one of:read,write | organization_custom_rolesstringThe level of permission to grant the access token for custom repository roles management.Can be one of:read,write | organization_custom_org_rolesstringThe level of permission to grant the access token for custom organization roles management.Can be one of:read,write | organization_custom_propertiesstringThe level of permission to grant the access token for repository custom properties management at the organization level.Can be one of:read,write,admin | organization_copilot_seat_managementstringThe level of permission to grant the access token for managing access to GitHub Copilot for members of an organization with a Copilot Business subscription. This property is in public preview and is subject to change.Value:write | organization_copilot_agent_settingsstringThe level of permission to grant the access token to view and manage Copilot coding agent settings for an organization.Can be one of:read,write | organization_announcement_bannersstringThe level of permission to grant the access token to view and manage announcement banners for an organization.Can be one of:read,write | organization_eventsstringThe level of permission to grant the access token to view events triggered by an activity in an organization.Value:read | organization_hooksstringThe level of permission to grant the access token to manage the post-receive hooks for an organization.Can be one of:read,write | organization_personal_access_tokensstringThe level of permission to grant the access token for viewing and managing fine-grained personal access token requests to an organization.Can be one of:read,write | organization_personal_access_token_requestsstringThe level of permission to grant the access token for viewing and managing fine-grained personal access tokens that have been approved by an organization.Can be one of:read,write | organization_planstringThe level of permission to grant the access token for viewing an organization's plan.Value:read | organization_projectsstringThe level of permission to grant the access token to manage organization projects and projects public preview (where available).Can be one of:read,write,admin | organization_packagesstringThe level of permission to grant the access token for organization packages published to GitHub Packages.Can be one of:read,write | organization_secretsstringThe level of permission to grant the access token to manage organization secrets.Can be one of:read,write | organization_self_hosted_runnersstringThe level of permission to grant the access token to view and manage GitHub Actions self-hosted runners available to an organization.Can be one of:read,write | organization_user_blockingstringThe level of permission to grant the access token to view and manage users blocked by the organization.Can be one of:read,write | email_addressesstringThe level of permission to grant the access token to manage the email addresses belonging to a user.Can be one of:read,write | followersstringThe level of permission to grant the access token to manage the followers belonging to a user.Can be one of:read,write | git_ssh_keysstringThe level of permission to grant the access token to manage git SSH keys.Can be one of:read,write | gpg_keysstringThe level of permission to grant the access token to view and manage GPG keys belonging to a user.Can be one of:read,write | interaction_limitsstringThe level of permission to grant the access token to view and manage interaction limits on a repository.Can be one of:read,write | profilestringThe level of permission to grant the access token to manage the profile settings belonging to a user.Value:write | starringstringThe level of permission to grant the access token to list and manage repositories a user is starring.Can be one of:read,write | enterprise_custom_properties_for_organizationsstringThe level of permission to grant the access token for organization custom properties management at the enterprise level.Can be one of:read,write,admin
Name, Type, Description
actionsstringThe level of permission to grant the access token for GitHub Actions workflows, workflow runs, and artifacts.Can be one of:read,write
administrationstringThe level of permission to grant the access token for repository creation, deletion, settings, teams, and collaborators creation.Can be one of:read,write
artifact_metadatastringThe level of permission to grant the access token to create and retrieve build artifact metadata records.Can be one of:read,write
attestationsstringThe level of permission to create and retrieve the access token for repository attestations.Can be one of:read,write
checksstringThe level of permission to grant the access token for checks on code.Can be one of:read,write
codespacesstringThe level of permission to grant the access token to create, edit, delete, and list Codespaces.Can be one of:read,write
contentsstringThe level of permission to grant the access token for repository contents, commits, branches, downloads, releases, and merges.Can be one of:read,write
dependabot_secretsstringThe level of permission to grant the access token to manage Dependabot secrets.Can be one of:read,write
deploymentsstringThe level of permission to grant the access token for deployments and deployment statuses.Can be one of:read,write
discussionsstringThe level of permission to grant the access token for discussions and related comments and label_filters.Can be one of:read,write
environmentsstringThe level of permission to grant the access token for managing repository environments.Can be one of:read,write
issuesstringThe level of permission to grant the access token for issues and related comments, assignees, label_filters, and milestones.Can be one of:read,write
merge_queuesstringThe level of permission to grant the access token to manage the merge queues for a repository.Can be one of:read,write
metadatastringThe level of permission to grant the access token to search repositories, list collaborators, and access repository metadata.Can be one of:read,write
packagesstringThe level of permission to grant the access token for packages published to GitHub Packages.Can be one of:read,write
pagesstringThe level of permission to grant the access token to retrieve Pages statuses, configuration, and builds, as well as create new builds.Can be one of:read,write
pull_requestsstringThe level of permission to grant the access token for pull requests and related comments, assignees, label_filters, milestones, and merges.Can be one of:read,write
repository_custom_propertiesstringThe level of permission to grant the access token to view and edit custom properties for a repository, when allowed by the property.Can be one of:read,write
repository_hooksstringThe level of permission to grant the access token to manage the post-receive hooks for a repository.Can be one of:read,write
repository_projectsstringThe level of permission to grant the access token to manage repository projects, columns, and cards.Can be one of:read,write,admin
secret_scanning_alertsstringThe level of permission to grant the access token to view and manage secret scanning alerts.Can be one of:read,write
secretsstringThe level of permission to grant the access token to manage repository secrets.Can be one of:read,write
security_eventsstringThe level of permission to grant the access token to view and manage security events like code scanning alerts.Can be one of:read,write
single_filestringThe level of permission to grant the access token to manage just a single file.Can be one of:read,write
statusesstringThe level of permission to grant the access token for commit statuses.Can be one of:read,write
vulnerability_alertsstringThe level of permission to grant the access token to manage Dependabot alerts.Can be one of:read,write
workflowsstringThe level of permission to grant the access token to update GitHub Actions workflow files.Value:write
custom_properties_for_organizationsstringThe level of permission to grant the access token to view and edit custom properties for an organization, when allowed by the property.Can be one of:read,write
membersstringThe level of permission to grant the access token for organization teams and members.Can be one of:read,write
organization_administrationstringThe level of permission to grant the access token to manage access to an organization.Can be one of:read,write
organization_custom_rolesstringThe level of permission to grant the access token for custom repository roles management.Can be one of:read,write
organization_custom_org_rolesstringThe level of permission to grant the access token for custom organization roles management.Can be one of:read,write
organization_custom_propertiesstringThe level of permission to grant the access token for repository custom properties management at the organization level.Can be one of:read,write,admin
organization_copilot_seat_managementstringThe level of permission to grant the access token for managing access to GitHub Copilot for members of an organization with a Copilot Business subscription. This property is in public preview and is subject to change.Value:write
organization_copilot_agent_settingsstringThe level of permission to grant the access token to view and manage Copilot coding agent settings for an organization.Can be one of:read,write
organization_announcement_bannersstringThe level of permission to grant the access token to view and manage announcement banners for an organization.Can be one of:read,write
organization_eventsstringThe level of permission to grant the access token to view events triggered by an activity in an organization.Value:read
organization_hooksstringThe level of permission to grant the access token to manage the post-receive hooks for an organization.Can be one of:read,write
organization_personal_access_tokensstringThe level of permission to grant the access token for viewing and managing fine-grained personal access token requests to an organization.Can be one of:read,write
organization_personal_access_token_requestsstringThe level of permission to grant the access token for viewing and managing fine-grained personal access tokens that have been approved by an organization.Can be one of:read,write
organization_planstringThe level of permission to grant the access token for viewing an organization's plan.Value:read
organization_projectsstringThe level of permission to grant the access token to manage organization projects and projects public preview (where available).Can be one of:read,write,admin
organization_packagesstringThe level of permission to grant the access token for organization packages published to GitHub Packages.Can be one of:read,write
organization_secretsstringThe level of permission to grant the access token to manage organization secrets.Can be one of:read,write
organization_self_hosted_runnersstringThe level of permission to grant the access token to view and manage GitHub Actions self-hosted runners available to an organization.Can be one of:read,write
organization_user_blockingstringThe level of permission to grant the access token to view and manage users blocked by the organization.Can be one of:read,write
email_addressesstringThe level of permission to grant the access token to manage the email addresses belonging to a user.Can be one of:read,write
followersstringThe level of permission to grant the access token to manage the followers belonging to a user.Can be one of:read,write
git_ssh_keysstringThe level of permission to grant the access token to manage git SSH keys.Can be one of:read,write
gpg_keysstringThe level of permission to grant the access token to view and manage GPG keys belonging to a user.Can be one of:read,write
interaction_limitsstringThe level of permission to grant the access token to view and manage interaction limits on a repository.Can be one of:read,write
profilestringThe level of permission to grant the access token to manage the profile settings belonging to a user.Value:write
starringstringThe level of permission to grant the access token to list and manage repositories a user is starring.Can be one of:read,write
enterprise_custom_properties_for_organizationsstringThe level of permission to grant the access token for organization custom properties management at the enterprise level.Can be one of:read,write,admin
[/TABLE]

```
access_token
```
The access token used to authenticate to the GitHub API.
The name of the user or organization to scope the user access token to.Requiredunlesstarget_idis specified.
The ID of the user or organization to scope the user access token to.Requiredunlesstargetis specified.

```
repositories
```
The list of repository names to scope the user access token to.repositoriesmay not be specified ifrepository_idsis specified.

```
repository_ids
```
The list of repository IDs to scope the user access token to.repository_idsmay not be specified ifrepositoriesis specified.

```
permissions
```
The permissions granted to the user access token.

```
permissions
```

[TABLE]
Name, Type, Description
actionsstringThe level of permission to grant the access token for GitHub Actions workflows, workflow runs, and artifacts.Can be one of:read,write
administrationstringThe level of permission to grant the access token for repository creation, deletion, settings, teams, and collaborators creation.Can be one of:read,write
artifact_metadatastringThe level of permission to grant the access token to create and retrieve build artifact metadata records.Can be one of:read,write
attestationsstringThe level of permission to create and retrieve the access token for repository attestations.Can be one of:read,write
checksstringThe level of permission to grant the access token for checks on code.Can be one of:read,write
codespacesstringThe level of permission to grant the access token to create, edit, delete, and list Codespaces.Can be one of:read,write
contentsstringThe level of permission to grant the access token for repository contents, commits, branches, downloads, releases, and merges.Can be one of:read,write
dependabot_secretsstringThe level of permission to grant the access token to manage Dependabot secrets.Can be one of:read,write
deploymentsstringThe level of permission to grant the access token for deployments and deployment statuses.Can be one of:read,write
discussionsstringThe level of permission to grant the access token for discussions and related comments and label_filters.Can be one of:read,write
environmentsstringThe level of permission to grant the access token for managing repository environments.Can be one of:read,write
issuesstringThe level of permission to grant the access token for issues and related comments, assignees, label_filters, and milestones.Can be one of:read,write
merge_queuesstringThe level of permission to grant the access token to manage the merge queues for a repository.Can be one of:read,write
metadatastringThe level of permission to grant the access token to search repositories, list collaborators, and access repository metadata.Can be one of:read,write
packagesstringThe level of permission to grant the access token for packages published to GitHub Packages.Can be one of:read,write
pagesstringThe level of permission to grant the access token to retrieve Pages statuses, configuration, and builds, as well as create new builds.Can be one of:read,write
pull_requestsstringThe level of permission to grant the access token for pull requests and related comments, assignees, label_filters, milestones, and merges.Can be one of:read,write
repository_custom_propertiesstringThe level of permission to grant the access token to view and edit custom properties for a repository, when allowed by the property.Can be one of:read,write
repository_hooksstringThe level of permission to grant the access token to manage the post-receive hooks for a repository.Can be one of:read,write
repository_projectsstringThe level of permission to grant the access token to manage repository projects, columns, and cards.Can be one of:read,write,admin
secret_scanning_alertsstringThe level of permission to grant the access token to view and manage secret scanning alerts.Can be one of:read,write
secretsstringThe level of permission to grant the access token to manage repository secrets.Can be one of:read,write
security_eventsstringThe level of permission to grant the access token to view and manage security events like code scanning alerts.Can be one of:read,write
single_filestringThe level of permission to grant the access token to manage just a single file.Can be one of:read,write
statusesstringThe level of permission to grant the access token for commit statuses.Can be one of:read,write
vulnerability_alertsstringThe level of permission to grant the access token to manage Dependabot alerts.Can be one of:read,write
workflowsstringThe level of permission to grant the access token to update GitHub Actions workflow files.Value:write
custom_properties_for_organizationsstringThe level of permission to grant the access token to view and edit custom properties for an organization, when allowed by the property.Can be one of:read,write
membersstringThe level of permission to grant the access token for organization teams and members.Can be one of:read,write
organization_administrationstringThe level of permission to grant the access token to manage access to an organization.Can be one of:read,write
organization_custom_rolesstringThe level of permission to grant the access token for custom repository roles management.Can be one of:read,write
organization_custom_org_rolesstringThe level of permission to grant the access token for custom organization roles management.Can be one of:read,write
organization_custom_propertiesstringThe level of permission to grant the access token for repository custom properties management at the organization level.Can be one of:read,write,admin
organization_copilot_seat_managementstringThe level of permission to grant the access token for managing access to GitHub Copilot for members of an organization with a Copilot Business subscription. This property is in public preview and is subject to change.Value:write
organization_copilot_agent_settingsstringThe level of permission to grant the access token to view and manage Copilot coding agent settings for an organization.Can be one of:read,write
organization_announcement_bannersstringThe level of permission to grant the access token to view and manage announcement banners for an organization.Can be one of:read,write
organization_eventsstringThe level of permission to grant the access token to view events triggered by an activity in an organization.Value:read
organization_hooksstringThe level of permission to grant the access token to manage the post-receive hooks for an organization.Can be one of:read,write
organization_personal_access_tokensstringThe level of permission to grant the access token for viewing and managing fine-grained personal access token requests to an organization.Can be one of:read,write
organization_personal_access_token_requestsstringThe level of permission to grant the access token for viewing and managing fine-grained personal access tokens that have been approved by an organization.Can be one of:read,write
organization_planstringThe level of permission to grant the access token for viewing an organization's plan.Value:read
organization_projectsstringThe level of permission to grant the access token to manage organization projects and projects public preview (where available).Can be one of:read,write,admin
organization_packagesstringThe level of permission to grant the access token for organization packages published to GitHub Packages.Can be one of:read,write
organization_secretsstringThe level of permission to grant the access token to manage organization secrets.Can be one of:read,write
organization_self_hosted_runnersstringThe level of permission to grant the access token to view and manage GitHub Actions self-hosted runners available to an organization.Can be one of:read,write
organization_user_blockingstringThe level of permission to grant the access token to view and manage users blocked by the organization.Can be one of:read,write
email_addressesstringThe level of permission to grant the access token to manage the email addresses belonging to a user.Can be one of:read,write
followersstringThe level of permission to grant the access token to manage the followers belonging to a user.Can be one of:read,write
git_ssh_keysstringThe level of permission to grant the access token to manage git SSH keys.Can be one of:read,write
gpg_keysstringThe level of permission to grant the access token to view and manage GPG keys belonging to a user.Can be one of:read,write
interaction_limitsstringThe level of permission to grant the access token to view and manage interaction limits on a repository.Can be one of:read,write
profilestringThe level of permission to grant the access token to manage the profile settings belonging to a user.Value:write
starringstringThe level of permission to grant the access token to list and manage repositories a user is starring.Can be one of:read,write
enterprise_custom_properties_for_organizationsstringThe level of permission to grant the access token for organization custom properties management at the enterprise level.Can be one of:read,write,admin
[/TABLE]
The level of permission to grant the access token for GitHub Actions workflows, workflow runs, and artifacts.
Can be one of:read,write

```
administration
```
The level of permission to grant the access token for repository creation, deletion, settings, teams, and collaborators creation.
Can be one of:read,write

```
artifact_metadata
```
The level of permission to grant the access token to create and retrieve build artifact metadata records.
Can be one of:read,write

```
attestations
```
The level of permission to create and retrieve the access token for repository attestations.
Can be one of:read,write
The level of permission to grant the access token for checks on code.
Can be one of:read,write
The level of permission to grant the access token to create, edit, delete, and list Codespaces.
Can be one of:read,write
The level of permission to grant the access token for repository contents, commits, branches, downloads, releases, and merges.
Can be one of:read,write

```
dependabot_secrets
```
The level of permission to grant the access token to manage Dependabot secrets.
Can be one of:read,write

```
deployments
```
The level of permission to grant the access token for deployments and deployment statuses.
Can be one of:read,write

```
discussions
```
The level of permission to grant the access token for discussions and related comments and label_filters.
Can be one of:read,write

```
environments
```
The level of permission to grant the access token for managing repository environments.
Can be one of:read,write
The level of permission to grant the access token for issues and related comments, assignees, label_filters, and milestones.
Can be one of:read,write

```
merge_queues
```
The level of permission to grant the access token to manage the merge queues for a repository.
Can be one of:read,write
The level of permission to grant the access token to search repositories, list collaborators, and access repository metadata.
Can be one of:read,write
The level of permission to grant the access token for packages published to GitHub Packages.
Can be one of:read,write
The level of permission to grant the access token to retrieve Pages statuses, configuration, and builds, as well as create new builds.
Can be one of:read,write

```
pull_requests
```
The level of permission to grant the access token for pull requests and related comments, assignees, label_filters, milestones, and merges.
Can be one of:read,write

```
repository_custom_properties
```
The level of permission to grant the access token to view and edit custom properties for a repository, when allowed by the property.
Can be one of:read,write

```
repository_hooks
```
The level of permission to grant the access token to manage the post-receive hooks for a repository.
Can be one of:read,write

```
repository_projects
```
The level of permission to grant the access token to manage repository projects, columns, and cards.
Can be one of:read,write,admin

```
secret_scanning_alerts
```
The level of permission to grant the access token to view and manage secret scanning alerts.
Can be one of:read,write
The level of permission to grant the access token to manage repository secrets.
Can be one of:read,write

```
security_events
```
The level of permission to grant the access token to view and manage security events like code scanning alerts.
Can be one of:read,write

```
single_file
```
The level of permission to grant the access token to manage just a single file.
Can be one of:read,write
The level of permission to grant the access token for commit statuses.
Can be one of:read,write

```
vulnerability_alerts
```
The level of permission to grant the access token to manage Dependabot alerts.
Can be one of:read,write
The level of permission to grant the access token to update GitHub Actions workflow files.
Value:write

```
custom_properties_for_organizations
```
The level of permission to grant the access token to view and edit custom properties for an organization, when allowed by the property.
Can be one of:read,write
The level of permission to grant the access token for organization teams and members.
Can be one of:read,write

```
organization_administration
```
The level of permission to grant the access token to manage access to an organization.
Can be one of:read,write

```
organization_custom_roles
```
The level of permission to grant the access token for custom repository roles management.
Can be one of:read,write

```
organization_custom_org_roles
```
The level of permission to grant the access token for custom organization roles management.
Can be one of:read,write

```
organization_custom_properties
```
The level of permission to grant the access token for repository custom properties management at the organization level.
Can be one of:read,write,admin

```
organization_copilot_seat_management
```
The level of permission to grant the access token for managing access to GitHub Copilot for members of an organization with a Copilot Business subscription. This property is in public preview and is subject to change.
Value:write

```
organization_copilot_agent_settings
```
The level of permission to grant the access token to view and manage Copilot coding agent settings for an organization.
Can be one of:read,write

```
organization_announcement_banners
```
The level of permission to grant the access token to view and manage announcement banners for an organization.
Can be one of:read,write

```
organization_events
```
The level of permission to grant the access token to view events triggered by an activity in an organization.
Value:read

```
organization_hooks
```
The level of permission to grant the access token to manage the post-receive hooks for an organization.
Can be one of:read,write

```
organization_personal_access_tokens
```
The level of permission to grant the access token for viewing and managing fine-grained personal access token requests to an organization.
Can be one of:read,write

```
organization_personal_access_token_requests
```
The level of permission to grant the access token for viewing and managing fine-grained personal access tokens that have been approved by an organization.
Can be one of:read,write

```
organization_plan
```
The level of permission to grant the access token for viewing an organization's plan.
Value:read

```
organization_projects
```
The level of permission to grant the access token to manage organization projects and projects public preview (where available).
Can be one of:read,write,admin

```
organization_packages
```
The level of permission to grant the access token for organization packages published to GitHub Packages.
Can be one of:read,write

```
organization_secrets
```
The level of permission to grant the access token to manage organization secrets.
Can be one of:read,write

```
organization_self_hosted_runners
```
The level of permission to grant the access token to view and manage GitHub Actions self-hosted runners available to an organization.
Can be one of:read,write

```
organization_user_blocking
```
The level of permission to grant the access token to view and manage users blocked by the organization.
Can be one of:read,write

```
email_addresses
```
The level of permission to grant the access token to manage the email addresses belonging to a user.
Can be one of:read,write
The level of permission to grant the access token to manage the followers belonging to a user.
Can be one of:read,write

```
git_ssh_keys
```
The level of permission to grant the access token to manage git SSH keys.
Can be one of:read,write
The level of permission to grant the access token to view and manage GPG keys belonging to a user.
Can be one of:read,write

```
interaction_limits
```
The level of permission to grant the access token to view and manage interaction limits on a repository.
Can be one of:read,write
The level of permission to grant the access token to manage the profile settings belonging to a user.
Value:write
The level of permission to grant the access token to list and manage repositories a user is starring.
Can be one of:read,write

```
enterprise_custom_properties_for_organizations
```
The level of permission to grant the access token for organization custom properties management at the enterprise level.
Can be one of:read,write,admin

### HTTP response status codes for "Create a scoped access token"

[TABLE]
Status code | Description
200 | OK
401 | Requires authentication
403 | Forbidden
404 | Resource not found
422 | Validation failed, or the endpoint has been spammed.
[/TABLE]
OK
Requires authentication
Forbidden
Resource not found
Validation failed, or the endpoint has been spammed.

### Code samples for "Create a scoped access token"

#### Request example
- cURL
- JavaScript

```
curl -L \
  -X POST \
  -H "Accept: application/vnd.github+json" \
  -u "<YOUR_CLIENT_ID>:<YOUR_CLIENT_SECRET>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/applications/Iv1.8a61f9b3a7aba766/token/scoped \
  -d '{"access_token":"e72e16c7e42f292c6912e7710c838347ae178b4a","target":"octocat","permissions":{"metadata":"read","issues":"write","contents":"read"}}'
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "id": 1,
  "url": "https://api.github.com/authorizations/1",
  "scopes": [],
  "token": "ghu_16C7e42F292c6912E7710c838347Ae178B4a",
  "token_last_eight": "Ae178B4a",
  "hashed_token": "25f94a2a5c7fbaf499c665bc73d67c1c87e496da8985131633ee0a95819db2e8",
  "app": {
    "url": "http://my-github-app.com",
    "name": "my github app",
    "client_id": "Iv1.8a61f9b3a7aba766"
  },
  "note": "optional note",
  "note_url": "http://optional/note/url",
  "updated_at": "2011-09-06T20:39:23Z",
  "created_at": "2011-09-06T17:26:27Z",
  "fingerprint": "jklmnop12345678",
  "expires_at": "2011-09-08T17:26:27Z",
  "user": {
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
  "installation": {
    "permissions": {
      "metadata": "read",
      "issues": "write",
      "contents": "read"
    },
    "repository_selection": "selected",
    "single_file_name": ".github/workflow.yml",
    "repositories_url": "https://api.github.com/user/repos",
    "account": {
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
    "has_multiple_single_files": false,
    "single_file_paths": []
  }
}
```

## Get an app
Note
The:app_slugis just the URL-friendly name of your GitHub App. You can find this on the settings page_number for your GitHub App (e.g.,https://github.com/settings/apps/:app_slug).

### Fine-grained access tokens for "Get an app"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token does not require any permissions.
This endpoint can be used without authentication if only public resources are requested.

### Parameters for "Get an app"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
app_slugstringRequired
[/TABLE]

### HTTP response status codes for "Get an app"

[TABLE]
Status code | Description
200 | OK
403 | Forbidden
404 | Resource not found
[/TABLE]
OK
Forbidden
Resource not found

### Code samples for "Get an app"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/apps/APP_SLUG
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "id": 1,
  "slug": "octoapp",
  "client_id": "Iv1.ab1112223334445c",
  "node_id": "MDExOkludGVncmF0aW9uMQ==",
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
  "name": "Octocat App",
  "description": "",
  "external_url": "https://example.com",
  "html_url": "https://github.com/apps/octoapp",
  "created_at": "2017-07-08T16:18:44-04:00",
  "updated_at": "2017-07-08T16:18:44-04:00",
  "permissions": {
    "metadata": "read",
    "contents": "read",
    "issues": "write",
    "single_file": "write"
  },
  "events": [
    "push",
    "pull_request"
  ]
}
```

## Get an organization installation for the authenticated app
Enables an authenticated GitHub App to find the organization's installation information.
You must use aJWTto access this endpoint.

### Fine-grained access tokens for "Get an organization installation for the authenticated app"
This endpoint does not work with GitHub App user access tokens, GitHub App installation access tokens, or fine-grained personal access tokens.

### Parameters for "Get an organization installation for the authenticated app"

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

### HTTP response status codes for "Get an organization installation for the authenticated app"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "Get an organization installation for the authenticated app"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/orgs/ORG/installation
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "id": 1,
  "account": {
    "login": "github",
    "id": 1,
    "node_id": "MDEyOk9yZ2FuaXphdGlvbjE=",
    "avatar_url": "https://github.com/images/error/hubot_happy.gif",
    "gravatar_id": "",
    "url": "https://api.github.com/orgs/github",
    "html_url": "https://github.com/github",
    "followers_url": "https://api.github.com/users/github/followers",
    "following_url": "https://api.github.com/users/github/following{/other_user}",
    "gists_url": "https://api.github.com/users/github/gists{/gist_id}",
    "starred_url": "https://api.github.com/users/github/starred{/owner}{/repo}",
    "subscriptions_url": "https://api.github.com/users/github/subscriptions",
    "organizations_url": "https://api.github.com/users/github/orgs",
    "repos_url": "https://api.github.com/orgs/github/repos",
    "events_url": "https://api.github.com/orgs/github/events",
    "received_events_url": "https://api.github.com/users/github/received_events",
    "type": "Organization",
    "site_admin": false
  },
  "repository_selection": "all",
  "access_tokens_url": "https://api.github.com/app/installations/1/access_tokens",
  "repositories_url": "https://api.github.com/installation/repositories",
  "html_url": "https://github.com/organizations/github/settings/installations/1",
  "app_id": 1,
  "client_id": "Iv1.ab1112223334445c",
  "target_id": 1,
  "target_type": "Organization",
  "permissions": {
    "checks": "write",
    "metadata": "read",
    "contents": "read"
  },
  "events": [
    "push",
    "pull_request"
  ],
  "created_at": "2018-02-09T20:51:14Z",
  "updated_at": "2018-02-09T20:51:14Z",
  "single_file_name": "config.yml",
  "has_multiple_single_files": true,
  "single_file_paths": [
    "config.yml",
    ".github/issue_TEMPLATE.md"
  ],
  "app_slug": "github-actions",
  "suspended_at": null,
  "suspended_by": null
}
```

## Get a repository installation for the authenticated app
Enables an authenticated GitHub App to find the repository's installation information. The installation's account type will be either an organization or a user account, depending which account the repository belongs to.
You must use aJWTto access this endpoint.

### Fine-grained access tokens for "Get a repository installation for the authenticated app"
This endpoint does not work with GitHub App user access tokens, GitHub App installation access tokens, or fine-grained personal access tokens.

### Parameters for "Get a repository installation for the authenticated app"

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

### HTTP response status codes for "Get a repository installation for the authenticated app"

[TABLE]
Status code | Description
200 | OK
301 | Moved permanently
404 | Resource not found
[/TABLE]
OK
Moved permanently
Resource not found

### Code samples for "Get a repository installation for the authenticated app"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/installation
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "id": 1,
  "account": {
    "login": "github",
    "id": 1,
    "node_id": "MDEyOk9yZ2FuaXphdGlvbjE=",
    "avatar_url": "https://github.com/images/error/hubot_happy.gif",
    "gravatar_id": "",
    "url": "https://api.github.com/orgs/github",
    "html_url": "https://github.com/github",
    "followers_url": "https://api.github.com/users/github/followers",
    "following_url": "https://api.github.com/users/github/following{/other_user}",
    "gists_url": "https://api.github.com/users/github/gists{/gist_id}",
    "starred_url": "https://api.github.com/users/github/starred{/owner}{/repo}",
    "subscriptions_url": "https://api.github.com/users/github/subscriptions",
    "organizations_url": "https://api.github.com/users/github/orgs",
    "repos_url": "https://api.github.com/orgs/github/repos",
    "events_url": "https://api.github.com/orgs/github/events",
    "received_events_url": "https://api.github.com/users/github/received_events",
    "type": "Organization",
    "site_admin": false
  },
  "repository_selection": "all",
  "access_tokens_url": "https://api.github.com/app/installations/1/access_tokens",
  "repositories_url": "https://api.github.com/installation/repositories",
  "html_url": "https://github.com/organizations/github/settings/installations/1",
  "app_id": 1,
  "client_id": "Iv1.ab1112223334445c",
  "target_id": 1,
  "target_type": "Organization",
  "permissions": {
    "checks": "write",
    "metadata": "read",
    "contents": "read"
  },
  "events": [
    "push",
    "pull_request"
  ],
  "created_at": "2018-02-09T20:51:14Z",
  "updated_at": "2018-02-09T20:51:14Z",
  "single_file_name": "config.yml",
  "has_multiple_single_files": true,
  "single_file_paths": [
    "config.yml",
    ".github/issue_TEMPLATE.md"
  ],
  "app_slug": "github-actions",
  "suspended_at": null,
  "suspended_by": null
}
```

## Get a user installation for the authenticated app
Enables an authenticated GitHub App to find the user’s installation information.
You must use aJWTto access this endpoint.

### Fine-grained access tokens for "Get a user installation for the authenticated app"
This endpoint does not work with GitHub App user access tokens, GitHub App installation access tokens, or fine-grained personal access tokens.

### Parameters for "Get a user installation for the authenticated app"

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

### HTTP response status codes for "Get a user installation for the authenticated app"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "Get a user installation for the authenticated app"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/users/USERNAME/installation
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "id": 1,
  "account": {
    "login": "github",
    "id": 1,
    "node_id": "MDEyOk9yZ2FuaXphdGlvbjE=",
    "avatar_url": "https://github.com/images/error/hubot_happy.gif",
    "gravatar_id": "",
    "url": "https://api.github.com/orgs/github",
    "html_url": "https://github.com/github",
    "followers_url": "https://api.github.com/users/github/followers",
    "following_url": "https://api.github.com/users/github/following{/other_user}",
    "gists_url": "https://api.github.com/users/github/gists{/gist_id}",
    "starred_url": "https://api.github.com/users/github/starred{/owner}{/repo}",
    "subscriptions_url": "https://api.github.com/users/github/subscriptions",
    "organizations_url": "https://api.github.com/users/github/orgs",
    "repos_url": "https://api.github.com/orgs/github/repos",
    "events_url": "https://api.github.com/orgs/github/events",
    "received_events_url": "https://api.github.com/users/github/received_events",
    "type": "Organization",
    "site_admin": false
  },
  "repository_selection": "all",
  "access_tokens_url": "https://api.github.com/app/installations/1/access_tokens",
  "repositories_url": "https://api.github.com/installation/repositories",
  "html_url": "https://github.com/organizations/github/settings/installations/1",
  "app_id": 1,
  "client_id": "Iv1.ab1112223334445c",
  "target_id": 1,
  "target_type": "Organization",
  "permissions": {
    "checks": "write",
    "metadata": "read",
    "contents": "read"
  },
  "events": [
    "push",
    "pull_request"
  ],
  "created_at": "2018-02-09T20:51:14Z",
  "updated_at": "2018-02-09T20:51:14Z",
  "single_file_name": "config.yml",
  "has_multiple_single_files": true,
  "single_file_paths": [
    "config.yml",
    ".github/issue_TEMPLATE.md"
  ],
  "app_slug": "github-actions",
  "suspended_at": null,
  "suspended_by": null
}
```