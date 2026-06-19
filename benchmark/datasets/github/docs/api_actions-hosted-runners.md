# GitHub-hosted runners

*Source: https://docs.github.com/en/rest/actions/hosted-runners*

---

# GitHub-hosted runners
Use the REST API to interact with GitHub-hosted runners in GitHub Actions.

## List GitHub-hosted runners for an organization
Lists all GitHub-hosted runners configured in an organization.
OAuth app tokens and personal access tokens (classic) need themanage_runner:orgscope to use this endpoint.

### Fine-grained access tokens for "List GitHub-hosted runners for an organization"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Administration" organization permissions (read)

### Parameters for "List GitHub-hosted runners for an organization"

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
per_pageintegerThe number of results per page (max 100). For more information, see "Using pagination in the REST API."Default:30
pageintegerThe page number of the results to fetch. For more information, see "Using pagination in the REST API."Default:1
[/TABLE]
The number of results per page (max 100). For more information, see "Using pagination in the REST API."
Default:30
The page number of the results to fetch. For more information, see "Using pagination in the REST API."
Default:1

### HTTP response status codes for "List GitHub-hosted runners for an organization"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "List GitHub-hosted runners for an organization"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/orgs/ORG/actions/hosted-runners
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
  "runners": [
    {
      "id": 5,
      "name": "My hosted ubuntu runner",
      "runner_group_id": 2,
      "platform": "linux-x64",
      "image": {
        "id": "ubuntu-20.04",
        "size": 86
      },
      "machine_size_details": {
        "id": "4-core",
        "cpu_cores": 4,
        "memory_gb": 16,
        "storage_gb": 150
      },
      "status": "Ready",
      "maximum_runners": 10,
      "public_ip_enabled": true,
      "public_ips": [
        {
          "enabled": true,
          "prefix": "20.80.208.150",
          "length": 31
        }
      ],
      "last_active_on": "2022-10-09T23:39:01Z"
    },
    {
      "id": 7,
      "name": "My hosted Windows runner",
      "runner_group_id": 2,
      "platform": "win-x64",
      "image": {
        "id": "windows-latest",
        "size": 256
      },
      "machine_size_details": {
        "id": "8-core",
        "cpu_cores": 8,
        "memory_gb": 32,
        "storage_gb": 300
      },
      "status": "Ready",
      "maximum_runners": 20,
      "public_ip_enabled": false,
      "public_ips": [],
      "last_active_on": "2023-04-26T15:23:37Z"
    }
  ]
}
```

## Create a GitHub-hosted runner for an organization
Creates a GitHub-hosted runner for an organization.
OAuth tokens and personal access tokens (classic) need themanage_runners:orgscope to use this endpoint.

### Fine-grained access tokens for "Create a GitHub-hosted runner for an organization"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Administration" organization permissions (write)

### Parameters for "Create a GitHub-hosted runner for an organization"

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
namestringRequiredName of the runner. Must be between 1 and 64 characters and may only contain upper and lowercase letters a-z, numbers 0-9, '.', '-', and '_'.
imageobjectRequiredThe image of runner. To list all available images, useGET /actions/hosted-runners/images/github-ownedorGET /actions/hosted-runners/images/partner.
Properties ofimageName, Type, DescriptionidstringThe unique identifier of the runner image.sourcestringThe source of the runner image.Can be one of:github,partner,customversionstring or nullThe version of the runner image to deploy. This is relevant only for runners using custom images. | Name, Type, Description | idstringThe unique identifier of the runner image. | sourcestringThe source of the runner image.Can be one of:github,partner,custom | versionstring or nullThe version of the runner image to deploy. This is relevant only for runners using custom images.
Name, Type, Description
idstringThe unique identifier of the runner image.
sourcestringThe source of the runner image.Can be one of:github,partner,custom
versionstring or nullThe version of the runner image to deploy. This is relevant only for runners using custom images.
sizestringRequiredThe machine size of the runner. To list available sizes, useGET actions/hosted-runners/machine-sizes
runner_group_idintegerRequiredThe existing runner group to add this runner to.
maximum_runnersintegerThe maximum amount of runners to scale up to. Runners will not auto-scale above this number. Use this setting to limit your cost.
enable_static_ipbooleanWhether this runner should be created with a static public IP. Note limit on account. To list limits on account, useGET actions/hosted-runners/limits
image_genbooleanWhether this runner should be used to generate custom images.Default:false
[/TABLE]
Name of the runner. Must be between 1 and 64 characters and may only contain upper and lowercase letters a-z, numbers 0-9, '.', '-', and '_'.
The image of runner. To list all available images, useGET /actions/hosted-runners/images/github-ownedorGET /actions/hosted-runners/images/partner.

[TABLE]
Name, Type, Description
idstringThe unique identifier of the runner image.
sourcestringThe source of the runner image.Can be one of:github,partner,custom
versionstring or nullThe version of the runner image to deploy. This is relevant only for runners using custom images.
[/TABLE]
The unique identifier of the runner image.
The source of the runner image.
Can be one of:github,partner,custom
The version of the runner image to deploy. This is relevant only for runners using custom images.
The machine size of the runner. To list available sizes, useGET actions/hosted-runners/machine-sizes

```
runner_group_id
```
The existing runner group to add this runner to.

```
maximum_runners
```
The maximum amount of runners to scale up to. Runners will not auto-scale above this number. Use this setting to limit your cost.

```
enable_static_ip
```
Whether this runner should be created with a static public IP. Note limit on account. To list limits on account, useGET actions/hosted-runners/limits
Whether this runner should be used to generate custom images.
Default:false

### HTTP response status codes for "Create a GitHub-hosted runner for an organization"

[TABLE]
Status code | Description
201 | Created
[/TABLE]
Created

### Code samples for "Create a GitHub-hosted runner for an organization"

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
  https://api.github.com/orgs/ORG/actions/hosted-runners \
  -d '{"name":"My Hosted runner","image":{"id":"ubuntu-latest","source":"github"},"runner_group_id":1,"size":"4-core","maximum_runners":50,"enable_static_ip":false}'
```

#### Response
- Example response
- Response schema

```
Status: 201
```

```
{
  "id": 5,
  "name": "My hosted ubuntu runner",
  "runner_group_id": 2,
  "platform": "linux-x64",
  "image": {
    "id": "ubuntu-20.04",
    "size": 86
  },
  "machine_size_details": {
    "id": "4-core",
    "cpu_cores": 4,
    "memory_gb": 16,
    "storage_gb": 150
  },
  "status": "Ready",
  "maximum_runners": 10,
  "public_ip_enabled": true,
  "public_ips": [
    {
      "enabled": true,
      "prefix": "20.80.208.150",
      "length": 31
    }
  ],
  "last_active_on": "2022-10-09T23:39:01Z"
}
```

## List custom images for an organization
List custom images for an organization.
OAuth tokens and personal access tokens (classic) need themanage_runners:orgscope to use this endpoint.

### Fine-grained access tokens for "List custom images for an organization"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Hosted runner custom images" organization permissions (read)

### Parameters for "List custom images for an organization"

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

### HTTP response status codes for "List custom images for an organization"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "List custom images for an organization"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/orgs/ORG/actions/hosted-runners/images/custom
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
  "image_versions": [
    {
      "version": "1.1.0",
      "size_gb": 75,
      "state": "Ready",
      "created_on": "2024-11-09T23:39:01Z"
    },
    {
      "version": "1.0.0",
      "size_gb": 75,
      "state": "Ready",
      "created_on": "2024-11-08T20:39:01Z"
    }
  ]
}
```

## Get a custom image definition for GitHub Actions Hosted Runners
Get a custom image definition for GitHub Actions Hosted Runners.
OAuth tokens and personal access tokens (classic) need themanage_runners:orgscope to use this endpoint.

### Fine-grained access tokens for "Get a custom image definition for GitHub Actions Hosted Runners"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Hosted runner custom images" organization permissions (read)

### Parameters for "Get a custom image definition for GitHub Actions Hosted Runners"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
image_definition_idintegerRequiredImage definition ID of custom image
[/TABLE]
The organization name. The name is not case sensitive.

```
image_definition_id
```
Image definition ID of custom image

### HTTP response status codes for "Get a custom image definition for GitHub Actions Hosted Runners"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "Get a custom image definition for GitHub Actions Hosted Runners"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/orgs/ORG/actions/hosted-runners/images/custom/IMAGE_DEFINITION_ID
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
  "platform": "linux-x64",
  "name": "CustomImage",
  "source": "custom",
  "versions_count": 4,
  "total_versions_size": 200,
  "latest_version": "1.3.0",
  "state": "Ready"
}
```

## Delete a custom image from the organization
Delete a custom image from the organization.
OAuth tokens and personal access tokens (classic) need themanage_runners:orgscope to use this endpoint.

### Fine-grained access tokens for "Delete a custom image from the organization"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Hosted runner custom images" organization permissions (write)

### Parameters for "Delete a custom image from the organization"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
image_definition_idintegerRequiredImage definition ID of custom image
[/TABLE]
The organization name. The name is not case sensitive.

```
image_definition_id
```
Image definition ID of custom image

### HTTP response status codes for "Delete a custom image from the organization"

[TABLE]
Status code | Description
204 | No Content
[/TABLE]
No Content

### Code samples for "Delete a custom image from the organization"

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
  https://api.github.com/orgs/ORG/actions/hosted-runners/images/custom/IMAGE_DEFINITION_ID
```

#### Response

```
Status: 204
```

## List image versions of a custom image for an organization
List image versions of a custom image for an organization.
OAuth tokens and personal access tokens (classic) need themanage_runners:orgscope to use this endpoint.

### Fine-grained access tokens for "List image versions of a custom image for an organization"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Hosted runner custom images" organization permissions (read)

### Parameters for "List image versions of a custom image for an organization"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
image_definition_idintegerRequiredImage definition ID of custom image
orgstringRequiredThe organization name. The name is not case sensitive.
[/TABLE]

```
image_definition_id
```
Image definition ID of custom image
The organization name. The name is not case sensitive.

### HTTP response status codes for "List image versions of a custom image for an organization"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "List image versions of a custom image for an organization"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/orgs/ORG/actions/hosted-runners/images/custom/IMAGE_DEFINITION_ID/versions
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
  "image_versions": [
    {
      "version": "1.1.0",
      "size_gb": 75,
      "state": "Ready",
      "created_on": "2024-11-09T23:39:01Z"
    },
    {
      "version": "1.0.0",
      "size_gb": 75,
      "state": "Ready",
      "created_on": "2024-11-08T20:39:01Z"
    }
  ]
}
```

## Get an image version of a custom image for GitHub Actions Hosted Runners
Get an image version of a custom image for GitHub Actions Hosted Runners.
OAuth tokens and personal access tokens (classic) need themanage_runners:orgscope to use this endpoint.

### Fine-grained access tokens for "Get an image version of a custom image for GitHub Actions Hosted Runners"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Hosted runner custom images" organization permissions (read)

### Parameters for "Get an image version of a custom image for GitHub Actions Hosted Runners"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
image_definition_idintegerRequiredImage definition ID of custom image
versionstringRequiredVersion of a custom image
[/TABLE]
The organization name. The name is not case sensitive.

```
image_definition_id
```
Image definition ID of custom image
Version of a custom image

### HTTP response status codes for "Get an image version of a custom image for GitHub Actions Hosted Runners"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "Get an image version of a custom image for GitHub Actions Hosted Runners"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/orgs/ORG/actions/hosted-runners/images/custom/IMAGE_DEFINITION_ID/versions/VERSION
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "version": "1.0.0",
  "size_gb": 75,
  "state": "Ready",
  "created_on": "2024-11-08T20:39:01Z"
}
```

## Delete an image version of custom image from the organization
Delete an image version of custom image from the organization.
OAuth tokens and personal access tokens (classic) need themanage_runners:orgscope to use this endpoint.

### Fine-grained access tokens for "Delete an image version of custom image from the organization"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Hosted runner custom images" organization permissions (write)

### Parameters for "Delete an image version of custom image from the organization"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
image_definition_idintegerRequiredImage definition ID of custom image
versionstringRequiredVersion of a custom image
[/TABLE]
The organization name. The name is not case sensitive.

```
image_definition_id
```
Image definition ID of custom image
Version of a custom image

### HTTP response status codes for "Delete an image version of custom image from the organization"

[TABLE]
Status code | Description
204 | No Content
[/TABLE]
No Content

### Code samples for "Delete an image version of custom image from the organization"

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
  https://api.github.com/orgs/ORG/actions/hosted-runners/images/custom/IMAGE_DEFINITION_ID/versions/VERSION
```

#### Response

```
Status: 204
```

## Get GitHub-owned images for GitHub-hosted runners in an organization
Get the list of GitHub-owned images available for GitHub-hosted runners for an organization.

### Fine-grained access tokens for "Get GitHub-owned images for GitHub-hosted runners in an organization"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Administration" organization permissions (read)

### Parameters for "Get GitHub-owned images for GitHub-hosted runners in an organization"

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

### HTTP response status codes for "Get GitHub-owned images for GitHub-hosted runners in an organization"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "Get GitHub-owned images for GitHub-hosted runners in an organization"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/orgs/ORG/actions/hosted-runners/images/github-owned
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "id": "ubuntu-20.04",
  "platform": "linux-x64",
  "size_gb": 86,
  "display_name": "20.04",
  "source": "github"
}
```

## Get partner images for GitHub-hosted runners in an organization
Get the list of partner images available for GitHub-hosted runners for an organization.

### Fine-grained access tokens for "Get partner images for GitHub-hosted runners in an organization"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Administration" organization permissions (read)

### Parameters for "Get partner images for GitHub-hosted runners in an organization"

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

### HTTP response status codes for "Get partner images for GitHub-hosted runners in an organization"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "Get partner images for GitHub-hosted runners in an organization"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/orgs/ORG/actions/hosted-runners/images/partner
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "id": "ubuntu-20.04",
  "platform": "linux-x64",
  "size_gb": 86,
  "display_name": "20.04",
  "source": "github"
}
```

## Get limits on GitHub-hosted runners for an organization
Get the GitHub-hosted runners limits for an organization.

### Fine-grained access tokens for "Get limits on GitHub-hosted runners for an organization"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Administration" organization permissions (read)

### Parameters for "Get limits on GitHub-hosted runners for an organization"

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

### HTTP response status codes for "Get limits on GitHub-hosted runners for an organization"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "Get limits on GitHub-hosted runners for an organization"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/orgs/ORG/actions/hosted-runners/limits
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "public_ips": {
    "current_usage": 17,
    "maximum": 50
  }
}
```

## Get GitHub-hosted runners machine specs for an organization
Get the list of machine specs available for GitHub-hosted runners for an organization.

### Fine-grained access tokens for "Get GitHub-hosted runners machine specs for an organization"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Administration" organization permissions (read)

### Parameters for "Get GitHub-hosted runners machine specs for an organization"

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

### HTTP response status codes for "Get GitHub-hosted runners machine specs for an organization"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "Get GitHub-hosted runners machine specs for an organization"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/orgs/ORG/actions/hosted-runners/machine-sizes
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "id": "4-core",
  "cpu_cores": 4,
  "memory_gb": 16,
  "storage_gb": 150
}
```

## Get platforms for GitHub-hosted runners in an organization
Get the list of platforms available for GitHub-hosted runners for an organization.

### Fine-grained access tokens for "Get platforms for GitHub-hosted runners in an organization"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Administration" organization permissions (read)

### Parameters for "Get platforms for GitHub-hosted runners in an organization"

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

### HTTP response status codes for "Get platforms for GitHub-hosted runners in an organization"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "Get platforms for GitHub-hosted runners in an organization"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/orgs/ORG/actions/hosted-runners/platforms
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
  "platforms": [
    "linux-x64",
    "win-x64"
  ]
}
```

## Get a GitHub-hosted runner for an organization
Gets a GitHub-hosted runner configured in an organization.
OAuth app tokens and personal access tokens (classic) need themanage_runners:orgscope to use this endpoint.

### Fine-grained access tokens for "Get a GitHub-hosted runner for an organization"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Administration" organization permissions (read)

### Parameters for "Get a GitHub-hosted runner for an organization"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
hosted_runner_idintegerRequiredUnique identifier of the GitHub-hosted runner.
[/TABLE]
The organization name. The name is not case sensitive.

```
hosted_runner_id
```
Unique identifier of the GitHub-hosted runner.

### HTTP response status codes for "Get a GitHub-hosted runner for an organization"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "Get a GitHub-hosted runner for an organization"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/orgs/ORG/actions/hosted-runners/HOSTED_RUNNER_ID
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "id": 5,
  "name": "My hosted ubuntu runner",
  "runner_group_id": 2,
  "platform": "linux-x64",
  "image": {
    "id": "ubuntu-20.04",
    "size": 86
  },
  "machine_size_details": {
    "id": "4-core",
    "cpu_cores": 4,
    "memory_gb": 16,
    "storage_gb": 150
  },
  "status": "Ready",
  "maximum_runners": 10,
  "public_ip_enabled": true,
  "public_ips": [
    {
      "enabled": true,
      "prefix": "20.80.208.150",
      "length": 31
    }
  ],
  "last_active_on": "2022-10-09T23:39:01Z"
}
```

## Update a GitHub-hosted runner for an organization
Updates a GitHub-hosted runner for an organization.
OAuth app tokens and personal access tokens (classic) need themanage_runners:orgscope to use this endpoint.

### Fine-grained access tokens for "Update a GitHub-hosted runner for an organization"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Administration" organization permissions (write)

### Parameters for "Update a GitHub-hosted runner for an organization"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
hosted_runner_idintegerRequiredUnique identifier of the GitHub-hosted runner.
[/TABLE]
The organization name. The name is not case sensitive.

```
hosted_runner_id
```
Unique identifier of the GitHub-hosted runner.

[TABLE]
Name, Type, Description
namestringName of the runner. Must be between 1 and 64 characters and may only contain upper and lowercase letters a-z, numbers 0-9, '.', '-', and '_'.
runner_group_idintegerThe existing runner group to add this runner to.
maximum_runnersintegerThe maximum amount of runners to scale up to. Runners will not auto-scale above this number. Use this setting to limit your cost.
enable_static_ipbooleanWhether this runner should be updated with a static public IP. Note limit on account. To list limits on account, useGET actions/hosted-runners/limits
sizestringThe machine size of the runner. To list available sizes, useGET actions/hosted-runners/machine-sizes
image_idstringThe unique identifier of the runner image. To list available images, useGET /actions/hosted-runners/images/github-owned,GET /actions/hosted-runners/images/partner, orGET /actions/hosted-runners/images/custom.
image_versionstring or nullThe version of the runner image to deploy. This is relevant only for runners using custom images.
[/TABLE]
Name of the runner. Must be between 1 and 64 characters and may only contain upper and lowercase letters a-z, numbers 0-9, '.', '-', and '_'.

```
runner_group_id
```
The existing runner group to add this runner to.

```
maximum_runners
```
The maximum amount of runners to scale up to. Runners will not auto-scale above this number. Use this setting to limit your cost.

```
enable_static_ip
```
Whether this runner should be updated with a static public IP. Note limit on account. To list limits on account, useGET actions/hosted-runners/limits
The machine size of the runner. To list available sizes, useGET actions/hosted-runners/machine-sizes
The unique identifier of the runner image. To list available images, useGET /actions/hosted-runners/images/github-owned,GET /actions/hosted-runners/images/partner, orGET /actions/hosted-runners/images/custom.

```
image_version
```
The version of the runner image to deploy. This is relevant only for runners using custom images.

### HTTP response status codes for "Update a GitHub-hosted runner for an organization"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "Update a GitHub-hosted runner for an organization"

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
  https://api.github.com/orgs/ORG/actions/hosted-runners/HOSTED_RUNNER_ID \
  -d '{"name":"My larger runner","runner_group_id":1,"maximum_runners":50,"enable_static_ip":false}'
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "id": 5,
  "name": "My hosted ubuntu runner",
  "runner_group_id": 2,
  "platform": "linux-x64",
  "image": {
    "id": "ubuntu-20.04",
    "size": 86
  },
  "machine_size_details": {
    "id": "4-core",
    "cpu_cores": 4,
    "memory_gb": 16,
    "storage_gb": 150
  },
  "status": "Ready",
  "maximum_runners": 10,
  "public_ip_enabled": true,
  "public_ips": [
    {
      "enabled": true,
      "prefix": "20.80.208.150",
      "length": 31
    }
  ],
  "last_active_on": "2022-10-09T23:39:01Z"
}
```

## Delete a GitHub-hosted runner for an organization
Deletes a GitHub-hosted runner for an organization.

### Fine-grained access tokens for "Delete a GitHub-hosted runner for an organization"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Administration" organization permissions (write)

### Parameters for "Delete a GitHub-hosted runner for an organization"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
hosted_runner_idintegerRequiredUnique identifier of the GitHub-hosted runner.
[/TABLE]
The organization name. The name is not case sensitive.

```
hosted_runner_id
```
Unique identifier of the GitHub-hosted runner.

### HTTP response status codes for "Delete a GitHub-hosted runner for an organization"

[TABLE]
Status code | Description
202 | Accepted
[/TABLE]
Accepted

### Code samples for "Delete a GitHub-hosted runner for an organization"

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
  https://api.github.com/orgs/ORG/actions/hosted-runners/HOSTED_RUNNER_ID
```

#### Response
- Example response
- Response schema

```
Status: 202
```

```
{
  "id": 5,
  "name": "My hosted ubuntu runner",
  "runner_group_id": 2,
  "platform": "linux-x64",
  "image": {
    "id": "ubuntu-20.04",
    "size": 86
  },
  "machine_size_details": {
    "id": "4-core",
    "cpu_cores": 4,
    "memory_gb": 16,
    "storage_gb": 150
  },
  "status": "Ready",
  "maximum_runners": 10,
  "public_ip_enabled": true,
  "public_ips": [
    {
      "enabled": true,
      "prefix": "20.80.208.150",
      "length": 31
    }
  ],
  "last_active_on": "2022-10-09T23:39:01Z"
}
```