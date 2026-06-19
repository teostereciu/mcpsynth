# REST API endpoints for GitHub Actions OIDC

*Source: https://docs.github.com/en/rest/actions/oidc*

---

# REST API endpoints for GitHub Actions OIDC
Use the REST API to interact with JWTs for OIDC subject claims in GitHub Actions.

## About GitHub Actions OIDC
You can use the REST API to query and manage a customization template for an OpenID Connect (OIDC) subject claim. For more information, seeOpenID Connect.

## List OIDC custom property inclusions for an enterprise
Lists the repository custom properties that are included in the OIDC token for repository actions in an enterprise.
OAuth app tokens and personal access tokens (classic) need theadmin:enterprisescope to use this endpoint.

### Fine-grained access tokens for "List OIDC custom property inclusions for an enterprise"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
The fine-grained token must have the following permission set:
- "Enterprise administration" enterprise permissions (read)

### Parameters for "List OIDC custom property inclusions for an enterprise"

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

### HTTP response status codes for "List OIDC custom property inclusions for an enterprise"

[TABLE]
Status code | Description
200 | A JSON array of OIDC custom property inclusions
403 | Forbidden
404 | Resource not found
[/TABLE]
A JSON array of OIDC custom property inclusions
Forbidden
Resource not found

### Code samples for "List OIDC custom property inclusions for an enterprise"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/enterprises/ENTERPRISE/actions/oidc/customization/properties/repo
```

#### A JSON array of OIDC custom property inclusions
- Example response
- Response schema

```
Status: 200
```

```
[
  {
    "custom_property_name": "environment",
    "inclusion_source": "enterprise"
  },
  {
    "custom_property_name": "team",
    "inclusion_source": "enterprise"
  }
]
```

## Create an OIDC custom property inclusion for an enterprise
Adds a repository custom property to be included in the OIDC token for repository actions in an enterprise.
OAuth app tokens and personal access tokens (classic) need theadmin:enterprisescope to use this endpoint.

### Fine-grained access tokens for "Create an OIDC custom property inclusion for an enterprise"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
The fine-grained token must have the following permission set:
- "Enterprise administration" enterprise permissions (write)

### Parameters for "Create an OIDC custom property inclusion for an enterprise"

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
custom_property_namestringRequiredThe name of the custom property to include in the OIDC token
[/TABLE]

```
custom_property_name
```
The name of the custom property to include in the OIDC token

### HTTP response status codes for "Create an OIDC custom property inclusion for an enterprise"

[TABLE]
Status code | Description
201 | OIDC custom property inclusion created
400 | Invalid input
403 | Forbidden
422 | Property inclusion already exists
[/TABLE]
OIDC custom property inclusion created
Invalid input
Forbidden
Property inclusion already exists

### Code samples for "Create an OIDC custom property inclusion for an enterprise"

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
  https://api.github.com/enterprises/ENTERPRISE/actions/oidc/customization/properties/repo \
  -d '{"custom_property_name":"environment"}'
```

#### OIDC custom property inclusion created
- Example response
- Response schema

```
Status: 201
```

```
{
  "custom_property_name": "environment"
}
```

## Delete an OIDC custom property inclusion for an enterprise
Removes a repository custom property from being included in the OIDC token for repository actions in an enterprise.
OAuth app tokens and personal access tokens (classic) need theadmin:enterprisescope to use this endpoint.

### Fine-grained access tokens for "Delete an OIDC custom property inclusion for an enterprise"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
The fine-grained token must have the following permission set:
- "Enterprise administration" enterprise permissions (write)

### Parameters for "Delete an OIDC custom property inclusion for an enterprise"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
enterprisestringRequiredThe slug version of the enterprise name.
custom_property_namestringRequiredThe name of the custom property to remove from OIDC token inclusion
[/TABLE]
The slug version of the enterprise name.

```
custom_property_name
```
The name of the custom property to remove from OIDC token inclusion

### HTTP response status codes for "Delete an OIDC custom property inclusion for an enterprise"

[TABLE]
Status code | Description
204 | OIDC custom property inclusion deleted
400 | Invalid input
403 | Forbidden
404 | Property inclusion not found
[/TABLE]
OIDC custom property inclusion deleted
Invalid input
Forbidden
Property inclusion not found

### Code samples for "Delete an OIDC custom property inclusion for an enterprise"

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
  https://api.github.com/enterprises/ENTERPRISE/actions/oidc/customization/properties/repo/CUSTOM_PROPERTY_NAME
```

#### OIDC custom property inclusion deleted

```
Status: 204
```

## List OIDC custom property inclusions for an organization
Lists the repository custom properties that are included in the OIDC token for repository actions in an organization.
OAuth app tokens and personal access tokens (classic) need theread:orgscope to use this endpoint.

### Fine-grained access tokens for "List OIDC custom property inclusions for an organization"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Administration" organization permissions (read)

### Parameters for "List OIDC custom property inclusions for an organization"

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

### HTTP response status codes for "List OIDC custom property inclusions for an organization"

[TABLE]
Status code | Description
200 | A JSON array of OIDC custom property inclusions
403 | Forbidden
404 | Resource not found
[/TABLE]
A JSON array of OIDC custom property inclusions
Forbidden
Resource not found

### Code samples for "List OIDC custom property inclusions for an organization"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/orgs/ORG/actions/oidc/customization/properties/repo
```

#### A JSON array of OIDC custom property inclusions
- Example response
- Response schema

```
Status: 200
```

```
[
  {
    "property_name": "environment"
  },
  {
    "property_name": "team"
  }
]
```

## Create an OIDC custom property inclusion for an organization
Adds a repository custom property to be included in the OIDC token for repository actions in an organization.
OAuth app tokens and personal access tokens (classic) need theadmin:orgscope to use this endpoint.

### Fine-grained access tokens for "Create an OIDC custom property inclusion for an organization"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Administration" organization permissions (write)

### Parameters for "Create an OIDC custom property inclusion for an organization"

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
custom_property_namestringRequiredThe name of the custom property to include in the OIDC token
[/TABLE]

```
custom_property_name
```
The name of the custom property to include in the OIDC token

### HTTP response status codes for "Create an OIDC custom property inclusion for an organization"

[TABLE]
Status code | Description
201 | OIDC custom property inclusion created
400 | Invalid input
403 | Forbidden
422 | Property inclusion already exists
[/TABLE]
OIDC custom property inclusion created
Invalid input
Forbidden
Property inclusion already exists

### Code samples for "Create an OIDC custom property inclusion for an organization"

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
  https://api.github.com/orgs/ORG/actions/oidc/customization/properties/repo \
  -d '{"custom_property_name":"environment"}'
```

#### OIDC custom property inclusion created
- Example response
- Response schema

```
Status: 201
```

```
{
  "custom_property_name": "environment"
}
```

## Delete an OIDC custom property inclusion for an organization
Removes a repository custom property from being included in the OIDC token for repository actions in an organization.
OAuth app tokens and personal access tokens (classic) need theadmin:orgscope to use this endpoint.

### Fine-grained access tokens for "Delete an OIDC custom property inclusion for an organization"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Administration" organization permissions (write)

### Parameters for "Delete an OIDC custom property inclusion for an organization"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
custom_property_namestringRequiredThe name of the custom property to remove from OIDC token inclusion
[/TABLE]
The organization name. The name is not case sensitive.

```
custom_property_name
```
The name of the custom property to remove from OIDC token inclusion

### HTTP response status codes for "Delete an OIDC custom property inclusion for an organization"

[TABLE]
Status code | Description
204 | OIDC custom property inclusion deleted
400 | Invalid input
403 | Forbidden
404 | Property inclusion not found
[/TABLE]
OIDC custom property inclusion deleted
Invalid input
Forbidden
Property inclusion not found

### Code samples for "Delete an OIDC custom property inclusion for an organization"

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
  https://api.github.com/orgs/ORG/actions/oidc/customization/properties/repo/CUSTOM_PROPERTY_NAME
```

#### OIDC custom property inclusion deleted

```
Status: 204
```

## Get the customization template for an OIDC subject claim for an organization
Gets the customization template for an OpenID Connect (OIDC) subject claim.
OAuth app tokens and personal access tokens (classic) need theread:orgscope to use this endpoint.

### Fine-grained access tokens for "Get the customization template for an OIDC subject claim for an organization"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Administration" organization permissions (read)

### Parameters for "Get the customization template for an OIDC subject claim for an organization"

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

### HTTP response status codes for "Get the customization template for an OIDC subject claim for an organization"

[TABLE]
Status code | Description
200 | A JSON serialized template for OIDC subject claim customization
[/TABLE]
A JSON serialized template for OIDC subject claim customization

### Code samples for "Get the customization template for an OIDC subject claim for an organization"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/orgs/ORG/actions/oidc/customization/sub
```

#### A JSON serialized template for OIDC subject claim customization
- Example response
- Response schema

```
Status: 200
```

```
{
  "include_claim_keys": [
    "repo",
    "context"
  ]
}
```

## Set the customization template for an OIDC subject claim for an organization
Creates or updates the customization template for an OpenID Connect (OIDC) subject claim.
OAuth app tokens and personal access tokens (classic) need thewrite:orgscope to use this endpoint.

### Fine-grained access tokens for "Set the customization template for an OIDC subject claim for an organization"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Administration" organization permissions (write)

### Parameters for "Set the customization template for an OIDC subject claim for an organization"

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
include_claim_keysarray of stringsRequiredArray of unique strings. Each claim key can only contain alphanumeric characters and underscores.
[/TABLE]

```
include_claim_keys
```
Array of unique strings. Each claim key can only contain alphanumeric characters and underscores.

### HTTP response status codes for "Set the customization template for an OIDC subject claim for an organization"

[TABLE]
Status code | Description
201 | Empty response
403 | Forbidden
404 | Resource not found
[/TABLE]
Empty response
Forbidden
Resource not found

### Code samples for "Set the customization template for an OIDC subject claim for an organization"

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
  https://api.github.com/orgs/ORG/actions/oidc/customization/sub \
  -d '{"include_claim_keys":["repo","context"]}'
```

#### Empty response
- Example response
- Response schema

```
Status: 201
```

## Get the customization template for an OIDC subject claim for a repository
Gets the customization template for an OpenID Connect (OIDC) subject claim.
OAuth tokens and personal access tokens (classic) need thereposcope to use this endpoint.

### Fine-grained access tokens for "Get the customization template for an OIDC subject claim for a repository"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Actions" repository permissions (read)
This endpoint can be used without authentication or the aforementioned permissions if only public resources are requested.

### Parameters for "Get the customization template for an OIDC subject claim for a repository"

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

### HTTP response status codes for "Get the customization template for an OIDC subject claim for a repository"

[TABLE]
Status code | Description
200 | Status response
400 | Bad Request
404 | Resource not found
[/TABLE]
Status response
Bad Request
Resource not found

### Code samples for "Get the customization template for an OIDC subject claim for a repository"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/actions/oidc/customization/sub
```

#### Status response
- Example response
- Response schema

```
Status: 200
```

```
{
  "use_default": false,
  "include_claim_keys": [
    "repo",
    "context"
  ]
}
```

## Set the customization template for an OIDC subject claim for a repository
Sets the customization template andopt-inoropt-outflag for an OpenID Connect (OIDC) subject claim for a repository.
OAuth app tokens and personal access tokens (classic) need thereposcope to use this endpoint.

### Fine-grained access tokens for "Set the customization template for an OIDC subject claim for a repository"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Actions" repository permissions (write)

### Parameters for "Set the customization template for an OIDC subject claim for a repository"

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
use_defaultbooleanRequiredWhether to use the default template or not. Iftrue, theinclude_claim_keysfield is ignored.
include_claim_keysarray of stringsArray of unique strings. Each claim key can only contain alphanumeric characters and underscores.
[/TABLE]

```
use_default
```
Whether to use the default template or not. Iftrue, theinclude_claim_keysfield is ignored.

```
include_claim_keys
```
Array of unique strings. Each claim key can only contain alphanumeric characters and underscores.

### HTTP response status codes for "Set the customization template for an OIDC subject claim for a repository"

[TABLE]
Status code | Description
201 | Empty response
400 | Bad Request
404 | Resource not found
422 | Validation failed, or the endpoint has been spammed.
[/TABLE]
Empty response
Bad Request
Resource not found
Validation failed, or the endpoint has been spammed.

### Code samples for "Set the customization template for an OIDC subject claim for a repository"

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
  https://api.github.com/repos/OWNER/REPO/actions/oidc/customization/sub \
  -d '{"use_default":false,"include_claim_keys":["repo","context"]}'
```

#### Empty response
- Example response
- Response schema

```
Status: 201
```