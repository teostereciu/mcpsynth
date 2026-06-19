# REST API endpoints for GitHub Actions cache

*Source: https://docs.github.com/en/rest/actions/cache*

---

# REST API endpoints for GitHub Actions cache
Use the REST API to interact with the cache for repositories in GitHub Actions.

## About the cache in GitHub Actions
You can use the REST API to query and manage the cache for repositories in GitHub Actions. You can also install a GitHub CLI extension to manage your caches from the command line. For more information, seeDependency caching reference.

## Get GitHub Actions cache retention limit for an enterprise
Gets GitHub Actions cache retention limit for an enterprise. All organizations and repositories under this
enterprise may not set a higher cache retention limit.
OAuth tokens and personal access tokens (classic) need theadmin:enterprisescope to use this endpoint.

### Fine-grained access tokens for "Get GitHub Actions cache retention limit for an enterprise"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
The fine-grained token must have the following permission set:
- "Enterprise administration" enterprise permissions (write)

### Parameters for "Get GitHub Actions cache retention limit for an enterprise"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
enterprisestringRequiredThe slug version of the enterprise name.
[/TABLE]
The slug version of the enterprise name.

### HTTP response status codes for "Get GitHub Actions cache retention limit for an enterprise"

[TABLE]
Status code | Description
200 | OK
403 | Forbidden
404 | Resource not found
[/TABLE]
OK
Forbidden
Resource not found

### Code samples for "Get GitHub Actions cache retention limit for an enterprise"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/enterprises/ENTERPRISE/actions/cache/retention-limit
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "max_cache_retention_days": 80
}
```

## Set GitHub Actions cache retention limit for an enterprise
Sets GitHub Actions cache retention limit for an enterprise. All organizations and repositories under this
enterprise may not set a higher cache retention limit.
OAuth tokens and personal access tokens (classic) need theadmin:enterprisescope to use this endpoint.

### Fine-grained access tokens for "Set GitHub Actions cache retention limit for an enterprise"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
The fine-grained token must have the following permission set:
- "Enterprise administration" enterprise permissions (write)

### Parameters for "Set GitHub Actions cache retention limit for an enterprise"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
enterprisestringRequiredThe slug version of the enterprise name.
[/TABLE]
The slug version of the enterprise name.

[TABLE]
Name, Type, Description
max_cache_retention_daysintegerFor repositories & organizations in an enterprise, the maximum duration, in days, for which caches in a repository may be retained.
[/TABLE]

```
max_cache_retention_days
```
For repositories & organizations in an enterprise, the maximum duration, in days, for which caches in a repository may be retained.

### HTTP response status codes for "Set GitHub Actions cache retention limit for an enterprise"

[TABLE]
Status code | Description
204 | No Content
400 | Bad Request
403 | Forbidden
404 | Resource not found
[/TABLE]
No Content
Bad Request
Forbidden
Resource not found

### Code samples for "Set GitHub Actions cache retention limit for an enterprise"

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
  https://api.github.com/enterprises/ENTERPRISE/actions/cache/retention-limit \
  -d '{"max_cache_retention_days":80}'
```

#### Response

```
Status: 204
```

## Get GitHub Actions cache storage limit for an enterprise
Gets GitHub Actions cache storage limit for an enterprise. All organizations and repositories under this
enterprise may not set a higher cache storage limit.
OAuth tokens and personal access tokens (classic) need theadmin:enterprisescope to use this endpoint.

### Fine-grained access tokens for "Get GitHub Actions cache storage limit for an enterprise"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
The fine-grained token must have the following permission set:
- "Enterprise administration" enterprise permissions (write)

### Parameters for "Get GitHub Actions cache storage limit for an enterprise"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
enterprisestringRequiredThe slug version of the enterprise name.
[/TABLE]
The slug version of the enterprise name.

### HTTP response status codes for "Get GitHub Actions cache storage limit for an enterprise"

[TABLE]
Status code | Description
200 | OK
403 | Forbidden
404 | Resource not found
[/TABLE]
OK
Forbidden
Resource not found

### Code samples for "Get GitHub Actions cache storage limit for an enterprise"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/enterprises/ENTERPRISE/actions/cache/storage-limit
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "max_cache_size_gb": 150
}
```

## Set GitHub Actions cache storage limit for an enterprise
Sets GitHub Actions cache storage limit for an enterprise. All organizations and repositories under this
enterprise may not set a higher cache storage limit.
OAuth tokens and personal access tokens (classic) need theadmin:enterprisescope to use this endpoint.

### Fine-grained access tokens for "Set GitHub Actions cache storage limit for an enterprise"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
The fine-grained token must have the following permission set:
- "Enterprise administration" enterprise permissions (write)

### Parameters for "Set GitHub Actions cache storage limit for an enterprise"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
enterprisestringRequiredThe slug version of the enterprise name.
[/TABLE]
The slug version of the enterprise name.

[TABLE]
Name, Type, Description
max_cache_size_gbintegerFor repositories & organizations in an enterprise, the maximum size limit for the sum of all caches in a repository, in gigabytes.
[/TABLE]

```
max_cache_size_gb
```
For repositories & organizations in an enterprise, the maximum size limit for the sum of all caches in a repository, in gigabytes.

### HTTP response status codes for "Set GitHub Actions cache storage limit for an enterprise"

[TABLE]
Status code | Description
204 | No Content
400 | Bad Request
403 | Forbidden
404 | Resource not found
[/TABLE]
No Content
Bad Request
Forbidden
Resource not found

### Code samples for "Set GitHub Actions cache storage limit for an enterprise"

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
  https://api.github.com/enterprises/ENTERPRISE/actions/cache/storage-limit \
  -d '{"max_cache_size_gb":150}'
```

#### Response

```
Status: 204
```

## Get GitHub Actions cache retention limit for an organization
Gets GitHub Actions cache retention limit for an organization. All repositories under this
organization may not set a higher cache retention limit.
OAuth tokens and personal access tokens (classic) need theadmin:organizationscope to use this endpoint.

### Fine-grained access tokens for "Get GitHub Actions cache retention limit for an organization"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Administration" organization permissions (read)

### Parameters for "Get GitHub Actions cache retention limit for an organization"

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

### HTTP response status codes for "Get GitHub Actions cache retention limit for an organization"

[TABLE]
Status code | Description
200 | OK
403 | Forbidden
404 | Resource not found
[/TABLE]
OK
Forbidden
Resource not found

### Code samples for "Get GitHub Actions cache retention limit for an organization"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/organizations/ORG/actions/cache/retention-limit
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "max_cache_retention_days": 80
}
```

## Set GitHub Actions cache retention limit for an organization
Sets GitHub Actions cache retention limit for an organization. All repositories under this
organization may not set a higher cache retention limit.
OAuth tokens and personal access tokens (classic) need theadmin:organizationscope to use this endpoint.

### Fine-grained access tokens for "Set GitHub Actions cache retention limit for an organization"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Administration" organization permissions (write)

### Parameters for "Set GitHub Actions cache retention limit for an organization"

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
max_cache_retention_daysintegerFor repositories in this organization, the maximum duration, in days, for which caches in a repository may be retained.
[/TABLE]

```
max_cache_retention_days
```
For repositories in this organization, the maximum duration, in days, for which caches in a repository may be retained.

### HTTP response status codes for "Set GitHub Actions cache retention limit for an organization"

[TABLE]
Status code | Description
204 | No Content
400 | Bad Request
403 | Forbidden
404 | Resource not found
[/TABLE]
No Content
Bad Request
Forbidden
Resource not found

### Code samples for "Set GitHub Actions cache retention limit for an organization"

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
  https://api.github.com/organizations/ORG/actions/cache/retention-limit \
  -d '{"max_cache_retention_days":80}'
```

#### Response

```
Status: 204
```

## Get GitHub Actions cache storage limit for an organization
Gets GitHub Actions cache storage limit for an organization. All repositories under this
organization may not set a higher cache storage limit.
OAuth tokens and personal access tokens (classic) need theadmin:organizationscope to use this endpoint.

### Fine-grained access tokens for "Get GitHub Actions cache storage limit for an organization"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Administration" organization permissions (read)

### Parameters for "Get GitHub Actions cache storage limit for an organization"

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

### HTTP response status codes for "Get GitHub Actions cache storage limit for an organization"

[TABLE]
Status code | Description
200 | OK
403 | Forbidden
404 | Resource not found
[/TABLE]
OK
Forbidden
Resource not found

### Code samples for "Get GitHub Actions cache storage limit for an organization"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/organizations/ORG/actions/cache/storage-limit
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "max_cache_size_gb": 150
}
```

## Set GitHub Actions cache storage limit for an organization
Sets GitHub Actions cache storage limit for an organization. All organizations and repositories under this
organization may not set a higher cache storage limit.
OAuth tokens and personal access tokens (classic) need theadmin:organizationscope to use this endpoint.

### Fine-grained access tokens for "Set GitHub Actions cache storage limit for an organization"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Administration" organization permissions (write)

### Parameters for "Set GitHub Actions cache storage limit for an organization"

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
max_cache_size_gbintegerFor repositories in the organization, the maximum size limit for the sum of all caches in a repository, in gigabytes.
[/TABLE]

```
max_cache_size_gb
```
For repositories in the organization, the maximum size limit for the sum of all caches in a repository, in gigabytes.

### HTTP response status codes for "Set GitHub Actions cache storage limit for an organization"

[TABLE]
Status code | Description
204 | No Content
400 | Bad Request
403 | Forbidden
404 | Resource not found
[/TABLE]
No Content
Bad Request
Forbidden
Resource not found

### Code samples for "Set GitHub Actions cache storage limit for an organization"

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
  https://api.github.com/organizations/ORG/actions/cache/storage-limit \
  -d '{"max_cache_size_gb":150}'
```

#### Response

```
Status: 204
```

## Get GitHub Actions cache usage for an organization
Gets the total GitHub Actions cache usage for an organization.
The data fetched using this API is refreshed approximately every 5 minutes, so values returned from this endpoint may take at least 5 minutes to get updated.
OAuth tokens and personal access tokens (classic) need theread:orgscope to use this endpoint.

### Fine-grained access tokens for "Get GitHub Actions cache usage for an organization"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Administration" organization permissions (read)

### Parameters for "Get GitHub Actions cache usage for an organization"

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

### HTTP response status codes for "Get GitHub Actions cache usage for an organization"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "Get GitHub Actions cache usage for an organization"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/orgs/ORG/actions/cache/usage
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "total_active_caches_size_in_bytes": 3344284,
  "total_active_caches_count": 5
}
```

## List repositories with GitHub Actions cache usage for an organization
Lists repositories and their GitHub Actions cache usage for an organization.
The data fetched using this API is refreshed approximately every 5 minutes, so values returned from this endpoint may take at least 5 minutes to get updated.
OAuth tokens and personal access tokens (classic) need theread:orgscope to use this endpoint.

### Fine-grained access tokens for "List repositories with GitHub Actions cache usage for an organization"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Administration" organization permissions (read)

### Parameters for "List repositories with GitHub Actions cache usage for an organization"

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
per_pageintegerThe number of results per page_number (max 100). For more information, see "Using pagination in the REST API."Default:30
pageintegerThe page_number number of the results to fetch. For more information, see "Using pagination in the REST API."Default:1
[/TABLE]
The number of results per page_number (max 100). For more information, see "Using pagination in the REST API."
Default:30
The page_number number of the results to fetch. For more information, see "Using pagination in the REST API."
Default:1

### HTTP response status codes for "List repositories with GitHub Actions cache usage for an organization"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "List repositories with GitHub Actions cache usage for an organization"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/orgs/ORG/actions/cache/usage-by-repository
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
  "repository_cache_usages": [
    {
      "full_name": "octo-org/Hello-World",
      "active_caches_size_in_bytes": 2322142,
      "active_caches_count": 3
    },
    {
      "full_name": "octo-org/server",
      "active_caches_size_in_bytes": 1022142,
      "active_caches_count": 2
    }
  ]
}
```

## Get GitHub Actions cache retention limit for a repository
Gets GitHub Actions cache retention limit for a repository. This determines how long caches will be retained for, if
not manually removed or evicted due to size constraints.
OAuth tokens and personal access tokens (classic) need theadmin:repositoryscope to use this endpoint.

### Fine-grained access tokens for "Get GitHub Actions cache retention limit for a repository"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Administration" repository permissions (read)

### Parameters for "Get GitHub Actions cache retention limit for a repository"

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

### HTTP response status codes for "Get GitHub Actions cache retention limit for a repository"

[TABLE]
Status code | Description
200 | OK
403 | Forbidden
404 | Resource not found
[/TABLE]
OK
Forbidden
Resource not found

### Code samples for "Get GitHub Actions cache retention limit for a repository"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/actions/cache/retention-limit
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "max_cache_retention_days": 80
}
```

## Set GitHub Actions cache retention limit for a repository
Sets GitHub Actions cache retention limit for a repository. This determines how long caches will be retained for, if
not manually removed or evicted due to size constraints.
OAuth tokens and personal access tokens (classic) need theadmin:repositoryscope to use this endpoint.

### Fine-grained access tokens for "Set GitHub Actions cache retention limit for a repository"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Administration" repository permissions (write)

### Parameters for "Set GitHub Actions cache retention limit for a repository"

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
max_cache_retention_daysintegerThe maximum number of days to keep caches in this repository.
[/TABLE]

```
max_cache_retention_days
```
The maximum number of days to keep caches in this repository.

### HTTP response status codes for "Set GitHub Actions cache retention limit for a repository"

[TABLE]
Status code | Description
204 | No Content
400 | Bad Request
403 | Forbidden
404 | Resource not found
[/TABLE]
No Content
Bad Request
Forbidden
Resource not found

### Code samples for "Set GitHub Actions cache retention limit for a repository"

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
  https://api.github.com/repos/OWNER/REPO/actions/cache/retention-limit \
  -d '{"max_cache_retention_days":80}'
```

#### Response

```
Status: 204
```

## Get GitHub Actions cache storage limit for a repository
Gets GitHub Actions cache storage limit for a repository. This determines the maximum size of caches that can be
stored before eviction occurs.
OAuth tokens and personal access tokens (classic) need theadmin:repositoryscope to use this endpoint.

### Fine-grained access tokens for "Get GitHub Actions cache storage limit for a repository"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Actions" repository permissions (read)

### Parameters for "Get GitHub Actions cache storage limit for a repository"

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

### HTTP response status codes for "Get GitHub Actions cache storage limit for a repository"

[TABLE]
Status code | Description
200 | OK
403 | Forbidden
404 | Resource not found
[/TABLE]
OK
Forbidden
Resource not found

### Code samples for "Get GitHub Actions cache storage limit for a repository"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/actions/cache/storage-limit
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "max_cache_size_gb": 150
}
```

## Set GitHub Actions cache storage limit for a repository
Sets GitHub Actions cache storage limit for a repository. This determines the maximum size of caches that can be
stored before eviction occurs.
OAuth tokens and personal access tokens (classic) need theadmin:repositoryscope to use this endpoint.

### Fine-grained access tokens for "Set GitHub Actions cache storage limit for a repository"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Administration" repository permissions (write)

### Parameters for "Set GitHub Actions cache storage limit for a repository"

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
max_cache_size_gbintegerThe maximum total cache size for this repository, in gigabytes.
[/TABLE]

```
max_cache_size_gb
```
The maximum total cache size for this repository, in gigabytes.

### HTTP response status codes for "Set GitHub Actions cache storage limit for a repository"

[TABLE]
Status code | Description
204 | No Content
400 | Bad Request
403 | Forbidden
404 | Resource not found
[/TABLE]
No Content
Bad Request
Forbidden
Resource not found

### Code samples for "Set GitHub Actions cache storage limit for a repository"

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
  https://api.github.com/repos/OWNER/REPO/actions/cache/storage-limit \
  -d '{"max_cache_size_gb":150}'
```

#### Response

```
Status: 204
```

## Get GitHub Actions cache usage for a repository
Gets GitHub Actions cache usage for a repository.
The data fetched using this API is refreshed approximately every 5 minutes, so values returned from this endpoint may take at least 5 minutes to get updated.
Anyone with read access to the repository can use this endpoint.
If the repository is private, OAuth tokens and personal access tokens (classic) need thereposcope to use this endpoint.

### Fine-grained access tokens for "Get GitHub Actions cache usage for a repository"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Actions" repository permissions (read)
This endpoint can be used without authentication or the aforementioned permissions if only public resources are requested.

### Parameters for "Get GitHub Actions cache usage for a repository"

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

### HTTP response status codes for "Get GitHub Actions cache usage for a repository"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "Get GitHub Actions cache usage for a repository"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/actions/cache/usage
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "full_name": "octo-org/Hello-World",
  "active_caches_size_in_bytes": 2322142,
  "active_caches_count": 3
}
```

## List GitHub Actions caches for a repository
Lists the GitHub Actions caches for a repository.
OAuth tokens and personal access tokens (classic) need thereposcope to use this endpoint.

### Fine-grained access tokens for "List GitHub Actions caches for a repository"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Actions" repository permissions (read)
This endpoint can be used without authentication or the aforementioned permissions if only public resources are requested.

### Parameters for "List GitHub Actions caches for a repository"

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
refstringThe full Git reference for narrowing down the cache. Thereffor a branch should be formatted asrefs/heads/<branch name>. To reference a pull request userefs/pull/<number>/merge.
keystringAn explicit key or prefix for identifying the cache
sortstringThe property to sort the results by.created_atmeans when the cache was created.last_accessed_atmeans when the cache was last accessed.size_in_bytesis the size of the cache in bytes.Default:last_accessed_atCan be one of:created_at,last_accessed_at,size_in_bytes
directionstringThe direction to sort the results by.Default:descCan be one of:asc,desc
[/TABLE]
The number of results per page_number (max 100). For more information, see "Using pagination in the REST API."
Default:30
The page_number number of the results to fetch. For more information, see "Using pagination in the REST API."
Default:1
The full Git reference for narrowing down the cache. Thereffor a branch should be formatted asrefs/heads/<branch name>. To reference a pull request userefs/pull/<number>/merge.
An explicit key or prefix for identifying the cache
The property to sort the results by.created_atmeans when the cache was created.last_accessed_atmeans when the cache was last accessed.size_in_bytesis the size of the cache in bytes.
Default:last_accessed_at
Can be one of:created_at,last_accessed_at,size_in_bytes

```
last_accessed_at
```

```
size_in_bytes
```
The direction to sort the results by.
Default:desc
Can be one of:asc,desc

### HTTP response status codes for "List GitHub Actions caches for a repository"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "List GitHub Actions caches for a repository"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/actions/caches
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
  "actions_caches": [
    {
      "id": 505,
      "ref": "refs/heads/main",
      "key": "Linux-node-958aff96db2d75d67787d1e634ae70b659de937b",
      "version": "73885106f58cc52a7df9ec4d4a5622a5614813162cb516c759a30af6bf56e6f0",
      "last_accessed_at": "2019-01-24T22:45:36.000Z",
      "created_at": "2019-01-24T22:45:36.000Z",
      "size_in_bytes": 1024
    }
  ]
}
```

## Delete GitHub Actions caches for a repository (using a cache key)
Deletes one or more GitHub Actions caches for a repository, using a complete cache key. By default, all caches that match the provided key are deleted, but you can optionally provide a Git ref to restrict deletions to caches that match both the provided key and the Git ref.
OAuth tokens and personal access tokens (classic) need thereposcope to use this endpoint.

### Fine-grained access tokens for "Delete GitHub Actions caches for a repository (using a cache key)"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Actions" repository permissions (write)

### Parameters for "Delete GitHub Actions caches for a repository (using a cache key)"

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
keystringRequiredA key for identifying the cache.
refstringThe full Git reference for narrowing down the cache. Thereffor a branch should be formatted asrefs/heads/<branch name>. To reference a pull request userefs/pull/<number>/merge.
[/TABLE]
A key for identifying the cache.
The full Git reference for narrowing down the cache. Thereffor a branch should be formatted asrefs/heads/<branch name>. To reference a pull request userefs/pull/<number>/merge.

### HTTP response status codes for "Delete GitHub Actions caches for a repository (using a cache key)"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "Delete GitHub Actions caches for a repository (using a cache key)"

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
  "https://api.github.com/repos/OWNER/REPO/actions/caches?key=Linux-node-958aff96db2d75d67787d1e634ae70b659de937b"
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
  "actions_caches": [
    {
      "id": 505,
      "ref": "refs/heads/main",
      "key": "Linux-node-958aff96db2d75d67787d1e634ae70b659de937b",
      "version": "73885106f58cc52a7df9ec4d4a5622a5614813162cb516c759a30af6bf56e6f0",
      "last_accessed_at": "2019-01-24T22:45:36.000Z",
      "created_at": "2019-01-24T22:45:36.000Z",
      "size_in_bytes": 1024
    }
  ]
}
```

## Delete a GitHub Actions cache for a repository (using a cache ID)
Deletes a GitHub Actions cache for a repository, using a cache ID.
OAuth tokens and personal access tokens (classic) need thereposcope to use this endpoint.

### Fine-grained access tokens for "Delete a GitHub Actions cache for a repository (using a cache ID)"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Actions" repository permissions (write)

### Parameters for "Delete a GitHub Actions cache for a repository (using a cache ID)"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
cache_idintegerRequiredThe unique identifier of the GitHub Actions cache.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.
The unique identifier of the GitHub Actions cache.

### HTTP response status codes for "Delete a GitHub Actions cache for a repository (using a cache ID)"

[TABLE]
Status code | Description
204 | No Content
[/TABLE]
No Content

### Code samples for "Delete a GitHub Actions cache for a repository (using a cache ID)"

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
  https://api.github.com/repos/OWNER/REPO/actions/caches/CACHE_ID
```

#### Response

```
Status: 204
```