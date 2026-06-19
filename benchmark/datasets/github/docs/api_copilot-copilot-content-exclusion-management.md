# REST API endpoints for Copilot content exclusion management

*Source: https://docs.github.com/en/rest/copilot/copilot-content-exclusion-management*

---

# REST API endpoints for Copilot content exclusion management
Use the REST API to manage Copilot content exclusion rules.

## Get Copilot content exclusion rules for an organization
Note
This endpoint is in public preview and is subject to change.
Gets information about an organization's Copilot content exclusion path rules.
To configure these settings, go to the organization's settings on GitHub.
For more information, see "Excluding content from GitHub Copilot."
Organization owners can view details about Copilot content exclusion rules for the organization.
OAuth app tokens and personal access tokens (classic) need either thecopilotorread:orgscopes to use this endpoint.
Caution
- At this time, the API does not support comments. This endpoint will not return any comments in the existing rules.
- At this time, the API does not support duplicate keys. If your content exclusion configuration contains duplicate keys, the API will return only the last occurrence of that key. For example, if duplicate entries are present, only the final value will be included in the response.

### Fine-grained access tokens for "Get Copilot content exclusion rules for an organization"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Copilot content exclusion" organization permissions (read)

### Parameters for "Get Copilot content exclusion rules for an organization"

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

### HTTP response status codes for "Get Copilot content exclusion rules for an organization"

[TABLE]
Status code | Description
200 | OK
401 | Requires authentication
403 | Forbidden
404 | Resource not found
500 | Internal Error
[/TABLE]
OK
Requires authentication
Forbidden
Resource not found
Internal Error

### Code samples for "Get Copilot content exclusion rules for an organization"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/orgs/ORG/copilot/content_exclusion
```

#### OK
- Example response
- Response schema

```
Status: 200
```

```
{
  "octo-repo": [
    "/src/some-dir/kernel.rs"
  ]
}
```

## Set Copilot content exclusion rules for an organization
Note
This endpoint is in public preview and is subject to change.
Sets Copilot content exclusion path rules for an organization.
To configure these settings, go to the organization's settings on GitHub.
For more information, see "Excluding content from GitHub Copilot."
Organization owners can set Copilot content exclusion rules for the organization.
OAuth app tokens and personal access tokens (classic) need thecopilotscope to use this endpoint.
Caution
- At this time, the API does not support comments. When using this endpoint, any existing comments in your rules will be deleted.
- At this time, the API does not support duplicate keys. If you submit content exclusions through the API with duplicate keys, only the last occurrence will be saved. Earlier entries with the same key will be overwritten.

### Fine-grained access tokens for "Set Copilot content exclusion rules for an organization"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Copilot content exclusion" organization permissions (write)

### Parameters for "Set Copilot content exclusion rules for an organization"

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

### HTTP response status codes for "Set Copilot content exclusion rules for an organization"

[TABLE]
Status code | Description
200 | Success
401 | Requires authentication
403 | Forbidden
404 | Resource not found
413 | Payload Too Large
422 | Validation failed, or the endpoint has been spammed.
500 | Internal Error
[/TABLE]
Success
Requires authentication
Forbidden
Resource not found
Payload Too Large
Validation failed, or the endpoint has been spammed.
Internal Error

### Code samples for "Set Copilot content exclusion rules for an organization"

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
  https://api.github.com/orgs/ORG/copilot/content_exclusion \
  -d '{"octo-repo":["/src/some-dir/kernel.rs"]}'
```

#### Success
- Example response
- Response schema

```
Status: 200
```

```
{
  "message": "Content exclusion rules updated successfully."
}
```