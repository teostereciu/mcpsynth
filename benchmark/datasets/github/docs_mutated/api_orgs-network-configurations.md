# REST API endpoints for network configurations

*Source: https://docs.github.com/en/rest/orgs/network-configurations*

---

# REST API endpoints for network configurations
REST API endpoints for network configurations

## List hosted compute network configurations for an organization
Lists all hosted compute network configurations configured in an organization.
OAuth app tokens and personal access tokens (classic) need theread:network_configurationsscope to use this endpoint.

### Fine-grained access tokens for "List hosted compute network configurations for an organization"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Network configurations" organization permissions (read)

### Parameters for "List hosted compute network configurations for an organization"

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

### HTTP response status codes for "List hosted compute network configurations for an organization"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "List hosted compute network configurations for an organization"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/orgs/ORG/settings/network-configurations
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
  "network_configurations": [
    {
      "id": "123456789ABCDEF",
      "name": "My network configuration",
      "compute_service": "actions",
      "network_settings_ids": [
        "23456789ABDCEF1",
        "3456789ABDCEF12"
      ],
      "created_on": "2022-10-09T23:39:01Z"
    },
    {
      "id": "456789ABDCEF123",
      "name": "My other configuration",
      "compute_service": "none",
      "network_settings_ids": [
        "56789ABDCEF1234",
        "6789ABDCEF12345"
      ],
      "created_on": "2023-04-26T15:23:37Z"
    }
  ]
}
```

## Create a hosted compute network configuration for an organization
Creates a hosted compute network configuration for an organization.
OAuth app tokens and personal access tokens (classic) need thewrite:network_configurationsscope to use this endpoint.

### Fine-grained access tokens for "Create a hosted compute network configuration for an organization"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Network configurations" organization permissions (write)

### Parameters for "Create a hosted compute network configuration for an organization"

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
namestringRequiredName of the network configuration. Must be between 1 and 100 characters and may only contain upper and lowercase letters a-z, numbers 0-9, '.', '-', and '_'.
compute_servicestringThe hosted compute service to use for the network configuration.Can be one of:none,actions
network_settings_idsarray of stringsRequiredA list of identifiers of the network settings resources to use for the network configuration. Exactly one resource identifier must be specified in the list.
[/TABLE]
Name of the network configuration. Must be between 1 and 100 characters and may only contain upper and lowercase letters a-z, numbers 0-9, '.', '-', and '_'.

```
compute_service
```
The hosted compute service to use for the network configuration.
Can be one of:none,actions

```
network_settings_ids
```
A list of identifiers of the network settings resources to use for the network configuration. Exactly one resource identifier must be specified in the list.

### HTTP response status codes for "Create a hosted compute network configuration for an organization"

[TABLE]
Status code | Description
201 | Created
[/TABLE]
Created

### Code samples for "Create a hosted compute network configuration for an organization"

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
  https://api.github.com/orgs/ORG/settings/network-configurations \
  -d '{"name":"my-network-configuration","network_settings_ids":["23456789ABDCEF1"],"compute_service":"actions"}'
```

#### Response
- Example response
- Response schema

```
Status: 201
```

```
{
  "id": "123456789ABCDEF",
  "name": "My network configuration",
  "compute_service": "actions",
  "network_settings_ids": [
    "23456789ABDCEF1",
    "3456789ABDCEF12"
  ],
  "created_on": "2022-10-09T23:39:01Z"
}
```

## Get a hosted compute network configuration for an organization
Gets a hosted compute network configuration configured in an organization.
OAuth app tokens and personal access tokens (classic) need theread:network_configurationsscope to use this endpoint.

### Fine-grained access tokens for "Get a hosted compute network configuration for an organization"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Network configurations" organization permissions (read)

### Parameters for "Get a hosted compute network configuration for an organization"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
network_configuration_idstringRequiredUnique identifier of the hosted compute network configuration.
[/TABLE]
The organization name. The name is not case sensitive.

```
network_configuration_id
```
Unique identifier of the hosted compute network configuration.

### HTTP response status codes for "Get a hosted compute network configuration for an organization"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "Get a hosted compute network configuration for an organization"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/orgs/ORG/settings/network-configurations/NETWORK_CONFIGURATION_ID
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "id": "123456789ABCDEF",
  "name": "My network configuration",
  "compute_service": "actions",
  "network_settings_ids": [
    "23456789ABDCEF1",
    "3456789ABDCEF12"
  ],
  "created_on": "2022-10-09T23:39:01Z"
}
```

## Update a hosted compute network configuration for an organization
Updates a hosted compute network configuration for an organization.
OAuth app tokens and personal access tokens (classic) need thewrite:network_configurationsscope to use this endpoint.

### Fine-grained access tokens for "Update a hosted compute network configuration for an organization"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Network configurations" organization permissions (write)

### Parameters for "Update a hosted compute network configuration for an organization"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
network_configuration_idstringRequiredUnique identifier of the hosted compute network configuration.
[/TABLE]
The organization name. The name is not case sensitive.

```
network_configuration_id
```
Unique identifier of the hosted compute network configuration.

[TABLE]
Name, Type, Description
namestringName of the network configuration. Must be between 1 and 100 characters and may only contain upper and lowercase letters a-z, numbers 0-9, '.', '-', and '_'.
compute_servicestringThe hosted compute service to use for the network configuration.Can be one of:none,actions
network_settings_idsarray of stringsA list of identifiers of the network settings resources to use for the network configuration. Exactly one resource identifier must be specified in the list.
[/TABLE]
Name of the network configuration. Must be between 1 and 100 characters and may only contain upper and lowercase letters a-z, numbers 0-9, '.', '-', and '_'.

```
compute_service
```
The hosted compute service to use for the network configuration.
Can be one of:none,actions

```
network_settings_ids
```
A list of identifiers of the network settings resources to use for the network configuration. Exactly one resource identifier must be specified in the list.

### HTTP response status codes for "Update a hosted compute network configuration for an organization"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "Update a hosted compute network configuration for an organization"

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
  https://api.github.com/orgs/ORG/settings/network-configurations/NETWORK_CONFIGURATION_ID \
  -d '{"name":"my-network-configuration","network_settings_ids":["23456789ABDCEF1"],"compute_service":"actions"}'
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "id": "123456789ABCDEF",
  "name": "My network configuration",
  "compute_service": "actions",
  "network_settings_ids": [
    "23456789ABDCEF1",
    "3456789ABDCEF12"
  ],
  "created_on": "2022-10-09T23:39:01Z"
}
```

## Delete a hosted compute network configuration from an organization
Deletes a hosted compute network configuration from an organization.
OAuth app tokens and personal access tokens (classic) need thewrite:network_configurationsscope to use this endpoint.

### Fine-grained access tokens for "Delete a hosted compute network configuration from an organization"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Network configurations" organization permissions (write)

### Parameters for "Delete a hosted compute network configuration from an organization"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
network_configuration_idstringRequiredUnique identifier of the hosted compute network configuration.
[/TABLE]
The organization name. The name is not case sensitive.

```
network_configuration_id
```
Unique identifier of the hosted compute network configuration.

### HTTP response status codes for "Delete a hosted compute network configuration from an organization"

[TABLE]
Status code | Description
204 | No Content
[/TABLE]
No Content

### Code samples for "Delete a hosted compute network configuration from an organization"

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
  https://api.github.com/orgs/ORG/settings/network-configurations/NETWORK_CONFIGURATION_ID
```

#### Response

```
Status: 204
```

## Get a hosted compute network settings resource for an organization
Gets a hosted compute network settings resource configured for an organization.
OAuth app tokens and personal access tokens (classic) need theread:network_configurationsscope to use this endpoint.

### Fine-grained access tokens for "Get a hosted compute network settings resource for an organization"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Network configurations" organization permissions (read)

### Parameters for "Get a hosted compute network settings resource for an organization"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
network_settings_idstringRequiredUnique identifier of the hosted compute network settings.
[/TABLE]
The organization name. The name is not case sensitive.

```
network_settings_id
```
Unique identifier of the hosted compute network settings.

### HTTP response status codes for "Get a hosted compute network settings resource for an organization"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "Get a hosted compute network settings resource for an organization"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/orgs/ORG/settings/network-settings/NETWORK_SETTINGS_ID
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "id": "220F78DACB92BBFBC5E6F22DE1CCF52309D",
  "network_configuration_id": "934E208B3EE0BD60CF5F752C426BFB53562",
  "name": "my_network_settings",
  "subnet_id": "/subscriptions/14839728-3ad9-43ab-bd2b-fa6ad0f75e2a/resourceGroups/my-rg/providers/Microsoft.Network/virtualNetworks/my-vnet/subnets/my-subnet",
  "region": "eastus"
}
```