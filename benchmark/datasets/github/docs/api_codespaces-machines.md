# REST API endpoints for Codespaces machines

*Source: https://docs.github.com/en/rest/codespaces/machines*

---

# REST API endpoints for Codespaces machines
Use the REST API to manage availability of machine types for a codespace.

## About Codespaces machines
You can determine which machine types are available to create a codespace, either on a given repository or as an authenticated user. For more information, seeChanging the machine type for your codespace.
You can also use this information when changing the machine of an existing codespace by updating itsmachineproperty. The machine update will take place the next time the codespace is restarted. For more information, seeChanging the machine type for your codespace.

## List available machine types for a repository
List the machine types available for a given repository based on its configuration.
OAuth app tokens and personal access tokens (classic) need thecodespacescope to use this endpoint.

### Fine-grained access tokens for "List available machine types for a repository"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Codespaces metadata" repository permissions (read)

### Parameters for "List available machine types for a repository"

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
locationstringThe location to check for available machines. Assigned by IP if not provided.
client_ipstringIP for location auto-detection when proxying a request
refstringThe branch or commit to check for prebuild availability and devcontainer restrictions.
[/TABLE]
The location to check for available machines. Assigned by IP if not provided.
IP for location auto-detection when proxying a request
The branch or commit to check for prebuild availability and devcontainer restrictions.

### HTTP response status codes for "List available machine types for a repository"

[TABLE]
Status code | Description
200 | OK
304 | Not modified
401 | Requires authentication
403 | Forbidden
404 | Resource not found
500 | Internal Error
[/TABLE]
OK
Not modified
Requires authentication
Forbidden
Resource not found
Internal Error

### Code samples for "List available machine types for a repository"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/codespaces/machines
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
  "machines": [
    {
      "name": "standardLinux",
      "display_name": "4 cores, 16 GB RAM, 64 GB storage",
      "operating_system": "linux",
      "storage_in_bytes": 68719476736,
      "memory_in_bytes": 17179869184,
      "cpus": 4
    },
    {
      "name": "premiumLinux",
      "display_name": "8 cores, 32 GB RAM, 64 GB storage",
      "operating_system": "linux",
      "storage_in_bytes": 68719476736,
      "memory_in_bytes": 34359738368,
      "cpus": 8
    }
  ]
}
```

## List machine types for a codespace
List the machine types a codespace can transition to use.
OAuth app tokens and personal access tokens (classic) need thecodespacescope to use this endpoint.

### Fine-grained access tokens for "List machine types for a codespace"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Codespaces metadata" repository permissions (read)

### Parameters for "List machine types for a codespace"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
codespace_namestringRequiredThe name of the codespace.
[/TABLE]

```
codespace_name
```
The name of the codespace.

### HTTP response status codes for "List machine types for a codespace"

[TABLE]
Status code | Description
200 | OK
304 | Not modified
401 | Requires authentication
403 | Forbidden
404 | Resource not found
500 | Internal Error
[/TABLE]
OK
Not modified
Requires authentication
Forbidden
Resource not found
Internal Error

### Code samples for "List machine types for a codespace"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/user/codespaces/CODESPACE_NAME/machines
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
  "machines": [
    {
      "name": "standardLinux",
      "display_name": "4 cores, 16 GB RAM, 64 GB storage",
      "operating_system": "linux",
      "storage_in_bytes": 68719476736,
      "memory_in_bytes": 17179869184,
      "cpus": 4
    },
    {
      "name": "premiumLinux",
      "display_name": "8 cores, 32 GB RAM, 64 GB storage",
      "operating_system": "linux",
      "storage_in_bytes": 68719476736,
      "memory_in_bytes": 34359738368,
      "cpus": 8
    }
  ]
}
```