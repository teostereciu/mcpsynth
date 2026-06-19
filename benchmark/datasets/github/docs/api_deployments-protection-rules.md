# REST API endpoints for protection rules

*Source: https://docs.github.com/en/rest/deployments/protection-rules*

---

# REST API endpoints for protection rules
Use the REST API to create, configure, and delete deployment protection rules.

## Get all deployment protection rules for an environment
Gets all custom deployment protection rules that are enabled for an environment. Anyone with read access to the repository can use this endpoint. For more information about environments, see "Using environments for deployment."
For more information about the app that is providing this custom deployment rule, see thedocumentation for theGET /apps/{app_slug}endpoint.

```
GET /apps/{app_slug}
```
OAuth app tokens and personal access tokens (classic) need thereposcope to use this endpoint with a private repository.

### Fine-grained access tokens for "Get all deployment protection rules for an environment"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Actions" repository permissions (read)
This endpoint can be used without authentication or the aforementioned permissions if only public resources are requested.

### Parameters for "Get all deployment protection rules for an environment"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
environment_namestringRequiredThe name of the environment. The name must be URL encoded. For example, any slashes in the name must be replaced with%2F.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
[/TABLE]

```
environment_name
```
The name of the environment. The name must be URL encoded. For example, any slashes in the name must be replaced with%2F.
The name of the repository without the.gitextension. The name is not case sensitive.
The account owner of the repository. The name is not case sensitive.

### HTTP response status codes for "Get all deployment protection rules for an environment"

[TABLE]
Status code | Description
200 | List of deployment protection rules
[/TABLE]
List of deployment protection rules

### Code samples for "Get all deployment protection rules for an environment"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/environments/ENVIRONMENT_NAME/deployment_protection_rules
```

#### List of deployment protection rules
- Example response
- Response schema

```
Status: 200
```

```
{
  "total_count": 2,
  "custom_deployment_protection_rules": [
    {
      "id": 3,
      "node_id": "IEH37kRlcGxveW1lbnRTdGF0ddiv",
      "enabled": true,
      "app": {
        "id": 1,
        "node_id": "GHT58kRlcGxveW1lbnRTdTY!bbcy",
        "slug": "a-custom-app",
        "integration_url": "https://api.github.com/apps/a-custom-app"
      }
    },
    {
      "id": 4,
      "node_id": "MDE2OkRlcGxveW1lbnRTdHJ41128",
      "enabled": true,
      "app": {
        "id": 1,
        "node_id": "UHVE67RlcGxveW1lbnRTdTY!jfeuy",
        "slug": "another-custom-app",
        "integration_url": "https://api.github.com/apps/another-custom-app"
      }
    }
  ]
}
```

## Create a custom deployment protection rule on an environment
Enable a custom deployment protection rule for an environment.
The authenticated user must have admin or owner permissions to the repository to use this endpoint.
For more information about the app that is providing this custom deployment rule, see thedocumentation for theGET /apps/{app_slug}endpoint, as well as theguide to creating custom deployment protection rules.

```
GET /apps/{app_slug}
```
OAuth app tokens and personal access tokens (classic) need thereposcope to use this endpoint.

### Fine-grained access tokens for "Create a custom deployment protection rule on an environment"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Administration" repository permissions (write)

### Parameters for "Create a custom deployment protection rule on an environment"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
environment_namestringRequiredThe name of the environment. The name must be URL encoded. For example, any slashes in the name must be replaced with%2F.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
[/TABLE]

```
environment_name
```
The name of the environment. The name must be URL encoded. For example, any slashes in the name must be replaced with%2F.
The name of the repository without the.gitextension. The name is not case sensitive.
The account owner of the repository. The name is not case sensitive.

[TABLE]
Name, Type, Description
integration_idintegerThe ID of the custom app that will be enabled on the environment.
[/TABLE]

```
integration_id
```
The ID of the custom app that will be enabled on the environment.

### HTTP response status codes for "Create a custom deployment protection rule on an environment"

[TABLE]
Status code | Description
201 | The enabled custom deployment protection rule
[/TABLE]
The enabled custom deployment protection rule

### Code samples for "Create a custom deployment protection rule on an environment"

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
  https://api.github.com/repos/OWNER/REPO/environments/ENVIRONMENT_NAME/deployment_protection_rules \
  -d '{"integration_id":5}'
```

#### The enabled custom deployment protection rule
- Example response
- Response schema

```
Status: 201
```

```
{
  "id": 3,
  "node_id": "IEH37kRlcGxveW1lbnRTdGF0ddiv",
  "enabled": true,
  "app": {
    "id": 1,
    "node_id": "GHT58kRlcGxveW1lbnRTdTY!bbcy",
    "slug": "a-custom-app",
    "integration_url": "https://api.github.com/apps/a-custom-app"
  }
}
```

## List custom deployment rule integrations available for an environment
Gets all custom deployment protection rule integrations that are available for an environment.
The authenticated user must have admin or owner permissions to the repository to use this endpoint.
For more information about environments, see "Using environments for deployment."
For more information about the app that is providing this custom deployment rule, see "GET an app".
OAuth app tokens and personal access tokens (classic) need thereposcope to use this endpoint with a private repository.

### Fine-grained access tokens for "List custom deployment rule integrations available for an environment"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Administration" repository permissions (read)

### Parameters for "List custom deployment rule integrations available for an environment"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
environment_namestringRequiredThe name of the environment. The name must be URL encoded. For example, any slashes in the name must be replaced with%2F.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
[/TABLE]

```
environment_name
```
The name of the environment. The name must be URL encoded. For example, any slashes in the name must be replaced with%2F.
The name of the repository without the.gitextension. The name is not case sensitive.
The account owner of the repository. The name is not case sensitive.

[TABLE]
Name, Type, Description
pageintegerThe page number of the results to fetch. For more information, see "Using pagination in the REST API."Default:1
per_pageintegerThe number of results per page (max 100). For more information, see "Using pagination in the REST API."Default:30
[/TABLE]
The page number of the results to fetch. For more information, see "Using pagination in the REST API."
Default:1
The number of results per page (max 100). For more information, see "Using pagination in the REST API."
Default:30

### HTTP response status codes for "List custom deployment rule integrations available for an environment"

[TABLE]
Status code | Description
200 | A list of custom deployment rule integrations available for this environment.
[/TABLE]
A list of custom deployment rule integrations available for this environment.

### Code samples for "List custom deployment rule integrations available for an environment"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/environments/ENVIRONMENT_NAME/deployment_protection_rules/apps
```

#### A list of custom deployment rule integrations available for this environment.
- Example response
- Response schema

```
Status: 200
```

```
[
  {
    "total_count": 2
  },
  {
    "available_custom_deployment_protection_rule_integrations": [
      {
        "id": 1,
        "node_id": "GHT58kRlcGxveW1lbnRTdTY!bbcy",
        "slug": "a-custom-app",
        "integration_url": "https://api.github.com/apps/a-custom-app"
      },
      {
        "id": 2,
        "node_id": "UHVE67RlcGxveW1lbnRTdTY!jfeuy",
        "slug": "another-custom-app",
        "integration_url": "https://api.github.com/apps/another-custom-app"
      }
    ]
  }
]
```

## Get a custom deployment protection rule
Gets an enabled custom deployment protection rule for an environment. Anyone with read access to the repository can use this endpoint. For more information about environments, see "Using environments for deployment."
For more information about the app that is providing this custom deployment rule, seeGET /apps/{app_slug}.

```
GET /apps/{app_slug}
```
OAuth app tokens and personal access tokens (classic) need thereposcope to use this endpoint with a private repository.

### Fine-grained access tokens for "Get a custom deployment protection rule"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Actions" repository permissions (read)
This endpoint can be used without authentication or the aforementioned permissions if only public resources are requested.

### Parameters for "Get a custom deployment protection rule"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
environment_namestringRequiredThe name of the environment. The name must be URL encoded. For example, any slashes in the name must be replaced with%2F.
protection_rule_idintegerRequiredThe unique identifier of the protection rule.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.

```
environment_name
```
The name of the environment. The name must be URL encoded. For example, any slashes in the name must be replaced with%2F.

```
protection_rule_id
```
The unique identifier of the protection rule.

### HTTP response status codes for "Get a custom deployment protection rule"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "Get a custom deployment protection rule"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/environments/ENVIRONMENT_NAME/deployment_protection_rules/PROTECTION_RULE_ID
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "id": 3,
  "node_id": "IEH37kRlcGxveW1lbnRTdGF0ddiv",
  "enabled": true,
  "app": {
    "id": 1,
    "node_id": "GHT58kRlcGxveW1lbnRTdTY!bbcy",
    "slug": "a-custom-app",
    "integration_url": "https://api.github.com/apps/a-custom-app"
  }
}
```

## Disable a custom protection rule for an environment
Disables a custom deployment protection rule for an environment.
The authenticated user must have admin or owner permissions to the repository to use this endpoint.
OAuth app tokens and personal access tokens (classic) need thereposcope to use this endpoint.

### Fine-grained access tokens for "Disable a custom protection rule for an environment"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Administration" repository permissions (write)

### Parameters for "Disable a custom protection rule for an environment"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
environment_namestringRequiredThe name of the environment. The name must be URL encoded. For example, any slashes in the name must be replaced with%2F.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
protection_rule_idintegerRequiredThe unique identifier of the protection rule.
[/TABLE]

```
environment_name
```
The name of the environment. The name must be URL encoded. For example, any slashes in the name must be replaced with%2F.
The name of the repository without the.gitextension. The name is not case sensitive.
The account owner of the repository. The name is not case sensitive.

```
protection_rule_id
```
The unique identifier of the protection rule.

### HTTP response status codes for "Disable a custom protection rule for an environment"

[TABLE]
Status code | Description
204 | No Content
[/TABLE]
No Content

### Code samples for "Disable a custom protection rule for an environment"

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
  https://api.github.com/repos/OWNER/REPO/environments/ENVIRONMENT_NAME/deployment_protection_rules/PROTECTION_RULE_ID
```

#### Response

```
Status: 204
```