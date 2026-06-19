# REST API endpoints for repository autolinks

*Source: https://docs.github.com/en/rest/repos/autolinks*

---

# REST API endpoints for repository autolinks
Use the REST API to add autolinks to external resources.

## About repository autolinks
To help streamline your workflow, you can use the REST API to add autolinks to external resources like JIRA issues and Zendesk tickets. For more information, seeConfiguring autolinks to reference external resources.
GitHub Apps require repository administration permissions with read or write access to use these endpoints.

## Get all autolinks of a repository
Gets all autolinks that are configured for a repository.
Information about autolinks are only available to repository administrators.

### Fine-grained access tokens for "Get all autolinks of a repository"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Administration" repository permissions (read)

### Parameters for "Get all autolinks of a repository"

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

### HTTP response status codes for "Get all autolinks of a repository"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "Get all autolinks of a repository"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/autolinks
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
    "id": 1,
    "key_prefix": "TICKET-",
    "url_template": "https://example.com/TICKET?query=<num>",
    "is_alphanumeric": true
  }
]
```

## Create an autolink reference for a repository
Users with admin access to the repository can create an autolink.

### Fine-grained access tokens for "Create an autolink reference for a repository"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Administration" repository permissions (write)

### Parameters for "Create an autolink reference for a repository"

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
key_prefixstringRequiredThis prefix appended by certain characters will generate a link any time it is found in an issue, pull request, or commit.
url_templatestringRequiredThe URL must contain<num>for the reference number.<num>matches different characters depending on the value ofis_alphanumeric.
is_alphanumericbooleanWhether this autolink reference matches alphanumeric characters. If true, the<num>parameter of theurl_templatematches alphanumeric charactersA-Z(case insensitive),0-9, and-. If false, this autolink reference only matches numeric characters.Default:true
[/TABLE]
This prefix appended by certain characters will generate a link any time it is found in an issue, pull request, or commit.

```
url_template
```
The URL must contain<num>for the reference number.<num>matches different characters depending on the value ofis_alphanumeric.

```
is_alphanumeric
```
Whether this autolink reference matches alphanumeric characters. If true, the<num>parameter of theurl_templatematches alphanumeric charactersA-Z(case insensitive),0-9, and-. If false, this autolink reference only matches numeric characters.
Default:true

### HTTP response status codes for "Create an autolink reference for a repository"

[TABLE]
Status code | Description
201 | Created
422 | Validation failed, or the endpoint has been spammed.
[/TABLE]
Created
Validation failed, or the endpoint has been spammed.

### Code samples for "Create an autolink reference for a repository"

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
  https://api.github.com/repos/OWNER/REPO/autolinks \
  -d '{"key_prefix":"TICKET-","url_template":"https://example.com/TICKET?query=<num>","is_alphanumeric":true}'
```

#### response
- Example response
- Response schema

```
Status: 201
```

```
{
  "id": 1,
  "key_prefix": "TICKET-",
  "url_template": "https://example.com/TICKET?query=<num>",
  "is_alphanumeric": true
}
```

## Get an autolink reference of a repository
This returns a single autolink reference by ID that was configured for the given repository.
Information about autolinks are only available to repository administrators.

### Fine-grained access tokens for "Get an autolink reference of a repository"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Administration" repository permissions (read)

### Parameters for "Get an autolink reference of a repository"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
autolink_idintegerRequiredThe unique identifier of the autolink.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.

```
autolink_id
```
The unique identifier of the autolink.

### HTTP response status codes for "Get an autolink reference of a repository"

[TABLE]
Status code | Description
200 | OK
404 | Resource not found
[/TABLE]
OK
Resource not found

### Code samples for "Get an autolink reference of a repository"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/autolinks/AUTOLINK_ID
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
  "key_prefix": "TICKET-",
  "url_template": "https://example.com/TICKET?query=<num>",
  "is_alphanumeric": true
}
```

## Delete an autolink reference from a repository
This deletes a single autolink reference by ID that was configured for the given repository.
Information about autolinks are only available to repository administrators.

### Fine-grained access tokens for "Delete an autolink reference from a repository"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Administration" repository permissions (write)

### Parameters for "Delete an autolink reference from a repository"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
autolink_idintegerRequiredThe unique identifier of the autolink.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.

```
autolink_id
```
The unique identifier of the autolink.

### HTTP response status codes for "Delete an autolink reference from a repository"

[TABLE]
Status code | Description
204 | No Content
404 | Resource not found
[/TABLE]
No Content
Resource not found

### Code samples for "Delete an autolink reference from a repository"

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
  https://api.github.com/repos/OWNER/REPO/autolinks/AUTOLINK_ID
```

#### Response

```
Status: 204
```