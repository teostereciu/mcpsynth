# REST API endpoints for custom properties

*Source: https://docs.github.com/en/rest/orgs/custom-properties*

---

# REST API endpoints for custom properties
Use the REST API to create and manage custom properties for an organization.

## About custom properties
You can use the REST API to create and manage custom properties for an organization. You can use custom properties to add metadata to repositories in your organization. For more information, seeManaging custom properties for repositories in your organization.

## Get all custom properties for an organization
Gets all custom properties defined for an organization.
Organization members can read these properties.

### Fine-grained access tokens for "Get all custom properties for an organization"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Custom properties" organization permissions (read)

### Parameters for "Get all custom properties for an organization"

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

### HTTP response status codes for "Get all custom properties for an organization"

[TABLE]
Status code | Description
200 | OK
403 | Forbidden
404 | Resource not found
[/TABLE]
OK
Forbidden
Resource not found

### Code samples for "Get all custom properties for an organization"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/orgs/ORG/properties/schema
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
    "url": "https://api.github.com/orgs/github/properties/schema/environment",
    "source_type": "organization",
    "value_type": "single_select",
    "required": true,
    "default_value": "production",
    "description": "Prod or dev environment",
    "allowed_values": [
      "production",
      "development"
    ],
    "values_editable_by": "org_actors",
    "require_explicit_values": true
  },
  {
    "property_name": "service",
    "url": "https://api.github.com/orgs/github/properties/schema/service",
    "source_type": "organization",
    "value_type": "string"
  },
  {
    "property_name": "team",
    "url": "https://api.github.com/orgs/github/properties/schema/team",
    "source_type": "organization",
    "value_type": "string",
    "description": "Team owning the repository"
  }
]
```

## Create or update custom properties for an organization
Creates new or updates existing custom properties defined for an organization in a batch.
If the property already exists, the existing property will be replaced with the new values.
Missing optional values will fall back to default values, previous values will be overwritten.
E.g. if a property exists withvalues_editable_by: org_and_repo_actorsand it's updated without specifyingvalues_editable_by, it will be updated to default valueorg_actors.
To use this endpoint, the authenticated user must be one of:
- An administrator for the organization.
- A user, or a user on a team, with the fine-grained permission ofcustom_properties_org_definitions_managerin the organization.

### Fine-grained access tokens for "Create or update custom properties for an organization"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Custom properties" organization permissions (admin)

### Parameters for "Create or update custom properties for an organization"

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
propertiesarray of objectsRequiredThe array of custom properties to create or update.
Properties ofpropertiesName, Type, Descriptionproperty_namestringRequiredThe name of the propertyurlstringThe URL that can be used to fetch, update, or delete info about this property via the API.source_typestringThe source type of the propertyCan be one of:organization,enterprisevalue_typestringRequiredThe type of the value for the propertyCan be one of:string,single_select,multi_select,true_false,urlrequiredbooleanWhether the property is required.default_valuenull or string or arrayDefault value of the propertydescriptionstring or nullShort description of the propertyallowed_valuesarray of strings or nullAn ordered list of the allowed values of the property.
The property can have up to 200 allowed values.values_editable_bystring or nullWho can edit the values of the propertyCan be one of:org_actors,org_and_repo_actors,nullrequire_explicit_valuesbooleanWhether setting properties values is mandatory | Name, Type, Description | property_namestringRequiredThe name of the property | urlstringThe URL that can be used to fetch, update, or delete info about this property via the API. | source_typestringThe source type of the propertyCan be one of:organization,enterprise | value_typestringRequiredThe type of the value for the propertyCan be one of:string,single_select,multi_select,true_false,url | requiredbooleanWhether the property is required. | default_valuenull or string or arrayDefault value of the property | descriptionstring or nullShort description of the property | allowed_valuesarray of strings or nullAn ordered list of the allowed values of the property.
The property can have up to 200 allowed values. | values_editable_bystring or nullWho can edit the values of the propertyCan be one of:org_actors,org_and_repo_actors,null | require_explicit_valuesbooleanWhether setting properties values is mandatory
Name, Type, Description
property_namestringRequiredThe name of the property
urlstringThe URL that can be used to fetch, update, or delete info about this property via the API.
source_typestringThe source type of the propertyCan be one of:organization,enterprise
value_typestringRequiredThe type of the value for the propertyCan be one of:string,single_select,multi_select,true_false,url
requiredbooleanWhether the property is required.
default_valuenull or string or arrayDefault value of the property
descriptionstring or nullShort description of the property
allowed_valuesarray of strings or nullAn ordered list of the allowed values of the property.
The property can have up to 200 allowed values.
values_editable_bystring or nullWho can edit the values of the propertyCan be one of:org_actors,org_and_repo_actors,null
require_explicit_valuesbooleanWhether setting properties values is mandatory
[/TABLE]
The array of custom properties to create or update.

[TABLE]
Name, Type, Description
property_namestringRequiredThe name of the property
urlstringThe URL that can be used to fetch, update, or delete info about this property via the API.
source_typestringThe source type of the propertyCan be one of:organization,enterprise
value_typestringRequiredThe type of the value for the propertyCan be one of:string,single_select,multi_select,true_false,url
requiredbooleanWhether the property is required.
default_valuenull or string or arrayDefault value of the property
descriptionstring or nullShort description of the property
allowed_valuesarray of strings or nullAn ordered list of the allowed values of the property.
The property can have up to 200 allowed values.
values_editable_bystring or nullWho can edit the values of the propertyCan be one of:org_actors,org_and_repo_actors,null
require_explicit_valuesbooleanWhether setting properties values is mandatory
[/TABLE]

```
property_name
```
The name of the property
The URL that can be used to fetch, update, or delete info about this property via the API.

```
source_type
```
The source type of the property
Can be one of:organization,enterprise

```
organization
```
The type of the value for the property
Can be one of:string,single_select,multi_select,true_false,url

```
single_select
```

```
multi_select
```
Whether the property is required.

```
default_value
```
Default value of the property

```
description
```
Short description of the property

```
allowed_values
```
An ordered list of the allowed values of the property.
The property can have up to 200 allowed values.

```
values_editable_by
```
Who can edit the values of the property
Can be one of:org_actors,org_and_repo_actors,null

```
org_and_repo_actors
```

```
require_explicit_values
```
Whether setting properties values is mandatory

### HTTP response status codes for "Create or update custom properties for an organization"

[TABLE]
Status code | Description
200 | OK
403 | Forbidden
404 | Resource not found
[/TABLE]
OK
Forbidden
Resource not found

### Code samples for "Create or update custom properties for an organization"

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
  https://api.github.com/orgs/ORG/properties/schema \
  -d '{"properties":[{"property_name":"environment","value_type":"single_select","required":true,"default_value":"production","description":"Prod or dev environment","allowed_values":["production","development"],"values_editable_by":"org_actors"},{"property_name":"service","value_type":"string"},{"property_name":"team","value_type":"string","description":"Team owning the repository"}]}'
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
    "url": "https://api.github.com/orgs/github/properties/schema/environment",
    "source_type": "organization",
    "value_type": "single_select",
    "required": true,
    "default_value": "production",
    "description": "Prod or dev environment",
    "allowed_values": [
      "production",
      "development"
    ],
    "values_editable_by": "org_actors",
    "require_explicit_values": true
  },
  {
    "property_name": "service",
    "url": "https://api.github.com/orgs/github/properties/schema/service",
    "source_type": "organization",
    "value_type": "string"
  },
  {
    "property_name": "team",
    "url": "https://api.github.com/orgs/github/properties/schema/team",
    "source_type": "organization",
    "value_type": "string",
    "description": "Team owning the repository"
  }
]
```

## Get a custom property for an organization
Gets a custom property that is defined for an organization.
Organization members can read these properties.

### Fine-grained access tokens for "Get a custom property for an organization"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Custom properties" organization permissions (read)

### Parameters for "Get a custom property for an organization"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
custom_property_namestringRequiredThe custom property name
[/TABLE]
The organization name. The name is not case sensitive.

```
custom_property_name
```
The custom property name

### HTTP response status codes for "Get a custom property for an organization"

[TABLE]
Status code | Description
200 | OK
403 | Forbidden
404 | Resource not found
[/TABLE]
OK
Forbidden
Resource not found

### Code samples for "Get a custom property for an organization"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/orgs/ORG/properties/schema/CUSTOM_PROPERTY_NAME
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "property_name": "environment",
  "url": "https://api.github.com/orgs/github/properties/schema/environment",
  "source_type": "organization",
  "value_type": "single_select",
  "required": true,
  "default_value": "production",
  "description": "Prod or dev environment",
  "allowed_values": [
    "production",
    "development"
  ]
}
```

## Create or update a custom property for an organization
Creates a new or updates an existing custom property that is defined for an organization.
To use this endpoint, the authenticated user must be one of:
- An administrator for the organization.
- A user, or a user on a team, with the fine-grained permission ofcustom_properties_org_definitions_managerin the organization.

### Fine-grained access tokens for "Create or update a custom property for an organization"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Custom properties" organization permissions (admin)

### Parameters for "Create or update a custom property for an organization"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
custom_property_namestringRequiredThe custom property name
[/TABLE]
The organization name. The name is not case sensitive.

```
custom_property_name
```
The custom property name

[TABLE]
Name, Type, Description
value_typestringRequiredThe type of the value for the propertyCan be one of:string,single_select,multi_select,true_false,url
requiredbooleanWhether the property is required.
default_valuenull or string or arrayDefault value of the property
descriptionstring or nullShort description of the property
allowed_valuesarray of strings or nullAn ordered list of the allowed values of the property.
The property can have up to 200 allowed values.
values_editable_bystring or nullWho can edit the values of the propertyCan be one of:org_actors,org_and_repo_actors,null
require_explicit_valuesbooleanWhether setting properties values is mandatory
[/TABLE]
The type of the value for the property
Can be one of:string,single_select,multi_select,true_false,url

```
single_select
```

```
multi_select
```
Whether the property is required.

```
default_value
```
Default value of the property

```
description
```
Short description of the property

```
allowed_values
```
An ordered list of the allowed values of the property.
The property can have up to 200 allowed values.

```
values_editable_by
```
Who can edit the values of the property
Can be one of:org_actors,org_and_repo_actors,null

```
org_and_repo_actors
```

```
require_explicit_values
```
Whether setting properties values is mandatory

### HTTP response status codes for "Create or update a custom property for an organization"

[TABLE]
Status code | Description
200 | OK
403 | Forbidden
404 | Resource not found
[/TABLE]
OK
Forbidden
Resource not found

### Code samples for "Create or update a custom property for an organization"

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
  https://api.github.com/orgs/ORG/properties/schema/CUSTOM_PROPERTY_NAME \
  -d '{"value_type":"single_select","required":true,"default_value":"production","description":"Prod or dev environment","allowed_values":["production","development"]}'
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "property_name": "environment",
  "url": "https://api.github.com/orgs/github/properties/schema/environment",
  "source_type": "organization",
  "value_type": "single_select",
  "required": true,
  "default_value": "production",
  "description": "Prod or dev environment",
  "allowed_values": [
    "production",
    "development"
  ]
}
```

## Remove a custom property for an organization
Removes a custom property that is defined for an organization.
To use this endpoint, the authenticated user must be one of:
- An administrator for the organization.
- A user, or a user on a team, with the fine-grained permission ofcustom_properties_org_definitions_managerin the organization.

### Fine-grained access tokens for "Remove a custom property for an organization"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Custom properties" organization permissions (admin)

### Parameters for "Remove a custom property for an organization"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
custom_property_namestringRequiredThe custom property name
[/TABLE]
The organization name. The name is not case sensitive.

```
custom_property_name
```
The custom property name

### HTTP response status codes for "Remove a custom property for an organization"

[TABLE]
Status code | Description
204 | A header with no content is returned.
403 | Forbidden
404 | Resource not found
[/TABLE]
A header with no content is returned.
Forbidden
Resource not found

### Code samples for "Remove a custom property for an organization"

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
  https://api.github.com/orgs/ORG/properties/schema/CUSTOM_PROPERTY_NAME
```

#### A header with no content is returned.

```
Status: 204
```

## List custom property values for organization repositories
Lists organization repositories with all of their custom property values.
Organization members can read these properties.

### Fine-grained access tokens for "List custom property values for organization repositories"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Custom properties" organization permissions (read)

### Parameters for "List custom property values for organization repositories"

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
repository_querystringFinds repositories in the organization with a query containing one or more search keywords and qualifiers. Qualifiers allow you to limit your search to specific areas of GitHub. The REST API supports the same qualifiers as the web interface for GitHub. To learn more about the format of the query, seeConstructing a search query. See "Searching for repositories" for a detailed list of qualifiers.
[/TABLE]
The number of results per page_number (max 100). For more information, see "Using pagination in the REST API."
Default:30
The page_number number of the results to fetch. For more information, see "Using pagination in the REST API."
Default:1

```
repository_query
```
Finds repositories in the organization with a query containing one or more search keywords and qualifiers. Qualifiers allow you to limit your search to specific areas of GitHub. The REST API supports the same qualifiers as the web interface for GitHub. To learn more about the format of the query, seeConstructing a search query. See "Searching for repositories" for a detailed list of qualifiers.

### HTTP response status codes for "List custom property values for organization repositories"

[TABLE]
Status code | Description
200 | OK
403 | Forbidden
404 | Resource not found
[/TABLE]
OK
Forbidden
Resource not found

### Code samples for "List custom property values for organization repositories"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/orgs/ORG/properties/values
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
    "repository_id": 1296269,
    "repository_name": "Hello-World",
    "repository_full_name": "octocat/Hello-World",
    "properties": [
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
  }
]
```

## Create or update custom property values for organization repositories
Create new or update existing custom property values for repositories in a batch that belong to an organization.
Each target repository will have its custom property values updated to match the values provided in the request.
A maximum of 30 repositories can be updated in a single request.
Using a value ofnullfor a custom property will remove or 'unset' the property value from the repository.
To use this endpoint, the authenticated user must be one of:
- An administrator for the organization.
- A user, or a user on a team, with the fine-grained permission ofcustom_properties_org_values_editorin the organization.

### Fine-grained access tokens for "Create or update custom property values for organization repositories"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Custom properties" organization permissions (write)

### Parameters for "Create or update custom property values for organization repositories"

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
repository_namesarray of stringsRequiredThe names of repositories that the custom property values will be applied to.
propertiesarray of objectsRequiredList of custom property names and associated values to apply to the repositories.
Properties ofpropertiesName, Type, Descriptionproperty_namestringRequiredThe name of the propertyvaluenull or string or arrayRequiredThe value assigned to the property | Name, Type, Description | property_namestringRequiredThe name of the property | valuenull or string or arrayRequiredThe value assigned to the property
Name, Type, Description
property_namestringRequiredThe name of the property
valuenull or string or arrayRequiredThe value assigned to the property
[/TABLE]

```
repository_names
```
The names of repositories that the custom property values will be applied to.
List of custom property names and associated values to apply to the repositories.

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

### HTTP response status codes for "Create or update custom property values for organization repositories"

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

### Code samples for "Create or update custom property values for organization repositories"

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
  https://api.github.com/orgs/ORG/properties/values \
  -d '{"repository_names":["Hello-World","octo-repo"],"properties":[{"property_name":"environment","value":"production"},{"property_name":"service","value":"web"},{"property_name":"team","value":"octocat"}]}'
```

#### No Content when custom property values are successfully created or updated

```
Status: 204
```