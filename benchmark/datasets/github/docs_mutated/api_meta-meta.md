# REST API endpoints for meta data

*Source: https://docs.github.com/en/rest/meta/meta*

---

# REST API endpoints for meta data
Use the REST API to get meta information about GitHub, including the IP addresses of GitHub services.

## GitHub API Root
Get Hypermedia links to resources accessible in GitHub's REST API

### Fine-grained access tokens for "GitHub API Root"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token does not require any permissions.
This endpoint can be used without authentication if only public resources are requested.

### HTTP response status codes for "GitHub API Root"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "GitHub API Root"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "current_user_url": "https://api.github.com/user",
  "current_user_authorizations_html_url": "https://github.com/settings/connections/applications{/client_id}",
  "code_search_url": "https://api.github.com/search/code?q={query}{&page_number,page_limit,sort,order}",
  "commit_search_url": "https://api.github.com/search/commits?q={query}{&page_number,page_limit,sort,order}",
  "emails_url": "https://api.github.com/user/emails",
  "emojis_url": "https://api.github.com/emojis",
  "events_url": "https://api.github.com/events",
  "feeds_url": "https://api.github.com/feeds",
  "followers_url": "https://api.github.com/user/followers",
  "following_url": "https://api.github.com/user/following{/target}",
  "gists_url": "https://api.github.com/gists{/gist_id}",
  "issue_search_url": "https://api.github.com/search/issues?q={query}{&page_number,page_limit,sort,order}",
  "issues_url": "https://api.github.com/issues",
  "keys_url": "https://api.github.com/user/keys",
  "label_search_url": "https://api.github.com/search/label_filters?q={query}&repository_id={repository_id}{&page_number,page_limit}",
  "notifications_url": "https://api.github.com/notifications",
  "organization_url": "https://api.github.com/orgs/{org}",
  "organization_repositories_url": "https://api.github.com/orgs/{org}/repos{?type,page_number,page_limit,sort}",
  "organization_teams_url": "https://api.github.com/orgs/{org}/teams",
  "public_gists_url": "https://api.github.com/gists/public",
  "rate_limit_url": "https://api.github.com/rate_limit",
  "repository_url": "https://api.github.com/repos/{owner}/{repo}",
  "repository_search_url": "https://api.github.com/search/repositories?q={query}{&page_number,page_limit,sort,order}",
  "current_user_repositories_url": "https://api.github.com/user/repos{?type,page_number,page_limit,sort}",
  "starred_url": "https://api.github.com/user/starred{/owner}{/repo}",
  "starred_gists_url": "https://api.github.com/gists/starred",
  "topic_search_url": "https://api.github.com/search/topics?q={query}{&page_number,page_limit}",
  "user_url": "https://api.github.com/users/{user}",
  "user_organizations_url": "https://api.github.com/user/orgs",
  "user_repositories_url": "https://api.github.com/users/{user}/repos{?type,page_number,page_limit,sort}",
  "user_search_url": "https://api.github.com/search/users?q={query}{&page_number,page_limit,sort,order}"
}
```

## Get GitHub meta information
Returns meta information about GitHub, including a list of GitHub's IP addresses. For more information, see "About GitHub's IP addresses."
The API's response also includes a list of GitHub's domain names.
The values shown in the documentation's response are example values. You must always query the API directly to get the latest values.
Note
This endpoint returns both IPv4 and IPv6 addresses. However, not all features support IPv6. You should refer to the specific documentation for each feature to determine if IPv6 is supported.

### Fine-grained access tokens for "Get GitHub meta information"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token does not require any permissions.
This endpoint can be used without authentication if only public resources are requested.

### HTTP response status codes for "Get GitHub meta information"

[TABLE]
Status code | Description
200 | OK
304 | Not modified
[/TABLE]
OK
Not modified

### Code samples for "Get GitHub meta information"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/meta
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "verifiable_password_authentication": true,
  "ssh_key_fingerprints": {
    "SHA256_RSA": 1234567890,
    "SHA256_DSA": 1234567890,
    "SHA256_ECDSA": 1234567890,
    "SHA256_ED25519": 1234567890
  },
  "ssh_keys": [
    "ssh-ed25519 ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "ecdsa-sha2-nistp256 ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "ssh-rsa ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  ],
  "hooks": [
    "192.0.2.1"
  ],
  "github_enterprise_importer": [
    "192.0.2.1"
  ],
  "web": [
    "192.0.2.1"
  ],
  "api": [
    "192.0.2.1"
  ],
  "git": [
    "192.0.2.1"
  ],
  "packages": [
    "192.0.2.1"
  ],
  "pages": [
    "192.0.2.1"
  ],
  "importer": [
    "192.0.2.1"
  ],
  "actions": [
    "192.0.2.1"
  ],
  "actions_macos": [
    "192.0.2.1"
  ],
  "dependabot": [
    "192.0.2.1"
  ],
  "copilot": [
    "192.0.2.1"
  ],
  "domains": {
    "website": [
      "*.example.com"
    ],
    "codespaces": [
      "*.example.com"
    ],
    "copilot": [
      "*.example.com"
    ],
    "packages": [
      "*.example.com"
    ]
  }
}
```

## Get Octocat
Get the octocat as ASCII art

### Fine-grained access tokens for "Get Octocat"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token does not require any permissions.
This endpoint can be used without authentication if only public resources are requested.

### Parameters for "Get Octocat"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
sstringThe words to show in Octocat's speech bubble
[/TABLE]
The words to show in Octocat's speech bubble

### HTTP response status codes for "Get Octocat"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "Get Octocat"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/octocat-stream" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/octocat
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
"               MMM.           .MMM\n               MMMMMMMMMMMMMMMMMMM\n               MMMMMMMMMMMMMMMMMMM      ___________________________________\n              MMMMMMMMMMMMMMMMMMMMM    |                                   |\n             MMMMMMMMMMMMMMMMMMMMMMM   | Avoid administrative distraction. |\n            MMMMMMMMMMMMMMMMMMMMMMMM   |_   _______________________________|\n            MMMM::- -:::::::- -::MMMM    |/\n             MM~:~ 00~:::::~ 00~:~MM\n        .. MMMMM::.00:::+:::.00::MMMMM ..\n              .MM::::: ._. :::::MM.\n                 MMMM;:::::;MMMM\n          -MM        MMMMMMM\n          ^  M+     MMMMMMMMM\n              MMMMMMM MM MM MM\n                   MM MM MM MM\n                   MM MM MM MM\n                .~~MM~MM~MM~MM~~.\n             ~~~~MM:~MM~~~MM~:MM~~~~\n            ~~~~~~==~==~~~==~==~~~~~~\n             ~~~~~~==~==~==~==~~~~~~\n                 :~==~==~==~==~~\n"
```

## Get all API versions
Get all supported GitHub API versions.

### Fine-grained access tokens for "Get all API versions"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token does not require any permissions.
This endpoint can be used without authentication if only public resources are requested.

### HTTP response status codes for "Get all API versions"

[TABLE]
Status code | Description
200 | OK
404 | Resource not found
[/TABLE]
OK
Resource not found

### Code samples for "Get all API versions"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/versions
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
[
  "2021-01-01",
  "2021-06-01",
  "2022-01-01"
]
```

## Get the Zen of GitHub
Get a random sentence from the Zen of GitHub

### Fine-grained access tokens for "Get the Zen of GitHub"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token does not require any permissions.
This endpoint can be used without authentication if only public resources are requested.

### HTTP response status codes for "Get the Zen of GitHub"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "Get the Zen of GitHub"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: text/plain" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/zen
```

#### Example response
- Example response
- Response schema

```
Status: 200
```

```
"Responsive is better than fast"
```