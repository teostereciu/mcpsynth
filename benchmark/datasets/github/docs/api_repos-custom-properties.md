# REST API endpoints for custom properties

*Source: https://docs.github.com/en/rest/repos/custom-properties*

---

# REST API endpoints for custom properties
Use the REST API to list the custom properties assigned to a repository by the organization.

## About custom properties
You can use the REST API to view the custom properties that were assigned to a repository by the organization that owns the repository. For more information, seeManaging custom properties for repositories in your organization. For more information about the REST API endpoints to manage custom properties, seeREST API endpoints for custom properties.

## Get all custom property values for a repository
Gets all custom property values that are set for a repository.
Users with read access to the repository can use this endpoint.

### Fine-grained access tokens for "Get all custom property values for a repository"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Metadata" repository permissions (read)
This endpoint can be used without authentication or the aforementioned permissions if only public resources are requested.

### Parameters for "Get all custom property values for a repository"

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

### HTTP response status codes for "Get all custom property values for a repository"

[TABLE]
Status code | Description
200 | OK
403 | Forbidden
404 | Resource not found
[/TABLE]
OK
Forbidden
Resource not found

### Code samples for "Get all custom property values for a repository"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/properties/values
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
    "property_name": "environment",
    "value": "production"
  },
  {
    "property_name": "service",
    "value": "web"
  },
  {
    "property_name": "team",
    "value": "octocat"
  }
]
```

## Create or update custom property values for a repository
Create new or update existing custom property values for a repository.
Using a value ofnullfor a custom property will remove or 'unset' the property value from the repository.
Repository admins and other users with the repository-level "edit custom property values" fine-grained permission can use this endpoint.

### Fine-grained access tokens for "Create or update custom property values for a repository"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Custom properties" repository permissions (write)

### Parameters for "Create or update custom property values for a repository"

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
propertiesarray of objectsRequiredA list of custom property names and associated values to apply to the repositories.
Properties ofpropertiesName, Type, Descriptionproperty_namestringRequiredThe name of the propertyvaluenull or string or arrayRequiredThe value assigned to the property | Name, Type, Description | property_namestringRequiredThe name of the property | valuenull or string or arrayRequiredThe value assigned to the property
Name, Type, Description
property_namestringRequiredThe name of the property
valuenull or string or arrayRequiredThe value assigned to the property
[/TABLE]
A list of custom property names and associated values to apply to the repositories.

[TABLE]
Name, Type, Description
property_namestringRequiredThe name of the property
valuenull or string or arrayRequiredThe value assigned to the property
[/TABLE]

```
property_name
```
The name of the property
The value assigned to the property

### HTTP response status codes for "Create or update custom property values for a repository"

[TABLE]
Status code | Description
204 | No Content when custom property values are successfully created or updated
403 | Forbidden
404 | Resource not found
422 | Validation failed, or the endpoint has been spammed.
[/TABLE]
No Content when custom property values are successfully created or updated
Forbidden
Resource not found
Validation failed, or the endpoint has been spammed.

### Code samples for "Create or update custom property values for a repository"

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
  https://api.github.com/repos/OWNER/REPO/properties/values \
  -d '{"properties":[{"property_name":"environment","value":"production"},{"property_name":"service","value":"web"},{"property_name":"team","value":"octocat"}]}'
```

#### No Content when custom property values are successfully created or updated

```
Status: 204
```