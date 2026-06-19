# Billing usage

*Source: https://docs.github.com/en/rest/billing/usage*

---

# Billing usage
Use the REST API to get billing usage information.
The endpoints on this page return usage that is billed to the account associated with the endpoint. For help deciding which level of usage to report on, seeAutomating usage reporting with the REST API.
- User endpoints return Copilot usage that is billed directly to an individual user’s personal account. These endpoints are only applicable if the user has purchased their own Copilot plan.
- If a user’s Copilot license is managed and billed through an organization or enterprise, their usage is not included in user-level endpoints. In that case, you must use the organization- or enterprise-level endpoints instead.
To view enterprise-level endpoints, select the dropdown menu at the top of the page and switch from Free, Pro, & Team to GitHub Enterprise Cloud.

## Get billing premium request usage report for an organization
Gets a report of premium request usage for an organization. To use this endpoint, you must be an administrator of an organization within an enterprise or an organization account.
Note:Only data from the past 24 months is accessible via this endpoint.

### Fine-grained access tokens for "Get billing premium request usage report for an organization"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Administration" organization permissions (read)

### Parameters for "Get billing premium request usage report for an organization"

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
yearintegerIf specified, only return results for a single year. The value ofyearis an integer with four digits representing a year. For example,2025. Default value is the current year.
monthintegerIf specified, only return results for a single month. The value ofmonthis an integer between1and12. Default value is the current month. If no year is specified the defaultyearis used.
dayintegerIf specified, only return results for a single day. The value ofdayis an integer between1and31. If noyearormonthis specified, the defaultyearandmonthare used.
userstringThe user name to query usage for. The name is not case sensitive.
modelstringThe model name to query usage for. The name is not case sensitive.
productstringThe product name to query usage for. The name is not case sensitive.
[/TABLE]
If specified, only return results for a single year. The value ofyearis an integer with four digits representing a year. For example,2025. Default value is the current year.
If specified, only return results for a single month. The value ofmonthis an integer between1and12. Default value is the current month. If no year is specified the defaultyearis used.
If specified, only return results for a single day. The value ofdayis an integer between1and31. If noyearormonthis specified, the defaultyearandmonthare used.
The user name to query usage for. The name is not case sensitive.
The model name to query usage for. The name is not case sensitive.
The product name to query usage for. The name is not case sensitive.

### HTTP response status codes for "Get billing premium request usage report for an organization"

[TABLE]
Status code | Description
200 | Response when getting a billing premium request usage report
400 | Bad Request
403 | Forbidden
404 | Resource not found
500 | Internal Error
503 | Service unavailable
[/TABLE]
Response when getting a billing premium request usage report
Bad Request
Forbidden
Resource not found
Internal Error
Service unavailable

### Code samples for "Get billing premium request usage report for an organization"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/organizations/ORG/settings/billing/premium_request/usage
```

#### Response when getting a billing premium request usage report
- Example response
- Response schema

```
Status: 200
```

```
{
  "timePeriod": {
    "year": 2025
  },
  "organization": "GitHub",
  "usageItems": [
    {
      "product": "Copilot",
      "sku": "Copilot Premium Request",
      "model": "GPT-5",
      "unitType": "requests",
      "pricePerUnit": 0.04,
      "grossQuantity": 100,
      "grossAmount": 4,
      "discountQuantity": 0,
      "discountAmount": 0,
      "netQuantity": 100,
      "netAmount": 4
    }
  ]
}
```

## Get billing usage report for an organization
Gets a report of the total usage for an organization. To use this endpoint, you must be an administrator of an organization within an enterprise or an organization account.
Note:This endpoint is only available to organizations with access to the enhanced billing platform. For more information, see "About the enhanced billing platform."

### Fine-grained access tokens for "Get billing usage report for an organization"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Administration" organization permissions (read)

### Parameters for "Get billing usage report for an organization"

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
yearintegerIf specified, only return results for a single year. The value ofyearis an integer with four digits representing a year. For example,2025. Default value is the current year.
monthintegerIf specified, only return results for a single month. The value ofmonthis an integer between1and12. If no year is specified the defaultyearis used.
dayintegerIf specified, only return results for a single day. The value ofdayis an integer between1and31. If noyearormonthis specified, the defaultyearandmonthare used.
[/TABLE]
If specified, only return results for a single year. The value ofyearis an integer with four digits representing a year. For example,2025. Default value is the current year.
If specified, only return results for a single month. The value ofmonthis an integer between1and12. If no year is specified the defaultyearis used.
If specified, only return results for a single day. The value ofdayis an integer between1and31. If noyearormonthis specified, the defaultyearandmonthare used.

### HTTP response status codes for "Get billing usage report for an organization"

[TABLE]
Status code | Description
200 | Billing usage report response for an organization
400 | Bad Request
403 | Forbidden
500 | Internal Error
503 | Service unavailable
[/TABLE]
Billing usage report response for an organization
Bad Request
Forbidden
Internal Error
Service unavailable

### Code samples for "Get billing usage report for an organization"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/organizations/ORG/settings/billing/usage
```

#### Billing usage report response for an organization
- Example response
- Response schema

```
Status: 200
```

```
{
  "usageItems": [
    {
      "date": "2023-08-01",
      "product": "Actions",
      "sku": "Actions Linux",
      "quantity": 100,
      "unitType": "minutes",
      "pricePerUnit": 0.008,
      "grossAmount": 0.8,
      "discountAmount": 0,
      "netAmount": 0.8,
      "organizationName": "GitHub",
      "repositoryName": "github/example"
    }
  ]
}
```

## Get billing usage summary for an organization
Note
This endpoint is in public preview and is subject to change.
Gets a summary report of usage for an organization. To use this endpoint, you must be an administrator of an organization within an enterprise or an organization account.
Note:Only data from the past 24 months is accessible via this endpoint.

### Fine-grained access tokens for "Get billing usage summary for an organization"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Administration" organization permissions (read)

### Parameters for "Get billing usage summary for an organization"

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
yearintegerIf specified, only return results for a single year. The value ofyearis an integer with four digits representing a year. For example,2025. Default value is the current year.
monthintegerIf specified, only return results for a single month. The value ofmonthis an integer between1and12. Default value is the current month. If no year is specified the defaultyearis used.
dayintegerIf specified, only return results for a single day. The value ofdayis an integer between1and31. If noyearormonthis specified, the defaultyearandmonthare used.
repositorystringThe repository name to query for usage in the format owner/repository.
productstringThe product name to query usage for. The name is not case sensitive.
skustringThe SKU to query for usage.
[/TABLE]
If specified, only return results for a single year. The value ofyearis an integer with four digits representing a year. For example,2025. Default value is the current year.
If specified, only return results for a single month. The value ofmonthis an integer between1and12. Default value is the current month. If no year is specified the defaultyearis used.
If specified, only return results for a single day. The value ofdayis an integer between1and31. If noyearormonthis specified, the defaultyearandmonthare used.
The repository name to query for usage in the format owner/repository.
The product name to query usage for. The name is not case sensitive.
The SKU to query for usage.

### HTTP response status codes for "Get billing usage summary for an organization"

[TABLE]
Status code | Description
200 | Response when getting a billing usage summary
400 | Bad Request
403 | Forbidden
500 | Internal Error
503 | Service unavailable
[/TABLE]
Response when getting a billing usage summary
Bad Request
Forbidden
Internal Error
Service unavailable

### Code samples for "Get billing usage summary for an organization"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/organizations/ORG/settings/billing/usage/summary
```

#### Response when getting a billing usage summary
- Example response
- Response schema

```
Status: 200
```

```
{
  "timePeriod": {
    "year": 2025
  },
  "organization": "GitHub",
  "usageItems": [
    {
      "product": "Actions",
      "sku": "actions_linux",
      "unitType": "minutes",
      "pricePerUnit": 0.008,
      "grossQuantity": 1000,
      "grossAmount": 8,
      "discountQuantity": 0,
      "discountAmount": 0,
      "netQuantity": 1000,
      "netAmount": 8
    }
  ]
}
```

## Get billing premium request usage report for a user
Gets a report of premium request usage for a user.
Note:Only data from the past 24 months is accessible via this endpoint.

### Fine-grained access tokens for "Get billing premium request usage report for a user"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Plan" user permissions (read)

### Parameters for "Get billing premium request usage report for a user"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
usernamestringRequiredThe handle for the GitHub user account.
[/TABLE]
The handle for the GitHub user account.

[TABLE]
Name, Type, Description
yearintegerIf specified, only return results for a single year. The value ofyearis an integer with four digits representing a year. For example,2025. Default value is the current year.
monthintegerIf specified, only return results for a single month. The value ofmonthis an integer between1and12. Default value is the current month. If no year is specified the defaultyearis used.
dayintegerIf specified, only return results for a single day. The value ofdayis an integer between1and31. If noyearormonthis specified, the defaultyearandmonthare used.
modelstringThe model name to query usage for. The name is not case sensitive.
productstringThe product name to query usage for. The name is not case sensitive.
[/TABLE]
If specified, only return results for a single year. The value ofyearis an integer with four digits representing a year. For example,2025. Default value is the current year.
If specified, only return results for a single month. The value ofmonthis an integer between1and12. Default value is the current month. If no year is specified the defaultyearis used.
If specified, only return results for a single day. The value ofdayis an integer between1and31. If noyearormonthis specified, the defaultyearandmonthare used.
The model name to query usage for. The name is not case sensitive.
The product name to query usage for. The name is not case sensitive.

### HTTP response status codes for "Get billing premium request usage report for a user"

[TABLE]
Status code | Description
200 | Response when getting a billing premium request usage report
400 | Bad Request
403 | Forbidden
404 | Resource not found
500 | Internal Error
503 | Service unavailable
[/TABLE]
Response when getting a billing premium request usage report
Bad Request
Forbidden
Resource not found
Internal Error
Service unavailable

### Code samples for "Get billing premium request usage report for a user"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/users/USERNAME/settings/billing/premium_request/usage
```

#### Response when getting a billing premium request usage report
- Example response
- Response schema

```
Status: 200
```

```
{
  "timePeriod": {
    "year": 2025
  },
  "user": "monalisa",
  "usageItems": [
    {
      "product": "Copilot",
      "sku": "Copilot Premium Request",
      "model": "GPT-5",
      "unitType": "requests",
      "pricePerUnit": 0.04,
      "grossQuantity": 100,
      "grossAmount": 4,
      "discountQuantity": 0,
      "discountAmount": 0,
      "netQuantity": 100,
      "netAmount": 4
    }
  ]
}
```

## Get billing usage report for a user
Gets a report of the total usage for a user.
Note:This endpoint is only available to users with access to the enhanced billing platform.

### Fine-grained access tokens for "Get billing usage report for a user"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Plan" user permissions (read)

### Parameters for "Get billing usage report for a user"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
usernamestringRequiredThe handle for the GitHub user account.
[/TABLE]
The handle for the GitHub user account.

[TABLE]
Name, Type, Description
yearintegerIf specified, only return results for a single year. The value ofyearis an integer with four digits representing a year. For example,2025. Default value is the current year.
monthintegerIf specified, only return results for a single month. The value ofmonthis an integer between1and12. If no year is specified the defaultyearis used.
dayintegerIf specified, only return results for a single day. The value ofdayis an integer between1and31. If noyearormonthis specified, the defaultyearandmonthare used.
[/TABLE]
If specified, only return results for a single year. The value ofyearis an integer with four digits representing a year. For example,2025. Default value is the current year.
If specified, only return results for a single month. The value ofmonthis an integer between1and12. If no year is specified the defaultyearis used.
If specified, only return results for a single day. The value ofdayis an integer between1and31. If noyearormonthis specified, the defaultyearandmonthare used.

### HTTP response status codes for "Get billing usage report for a user"

[TABLE]
Status code | Description
200 | Response when getting a billing usage report
400 | Bad Request
403 | Forbidden
500 | Internal Error
503 | Service unavailable
[/TABLE]
Response when getting a billing usage report
Bad Request
Forbidden
Internal Error
Service unavailable

### Code samples for "Get billing usage report for a user"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/users/USERNAME/settings/billing/usage
```

#### Response when getting a billing usage report
- Example response
- Response schema

```
Status: 200
```

```
{
  "usageItems": [
    {
      "date": "2023-08-01",
      "product": "Actions",
      "sku": "Actions Linux",
      "quantity": 100,
      "unitType": "minutes",
      "pricePerUnit": 0.008,
      "grossAmount": 0.8,
      "discountAmount": 0,
      "netAmount": 0.8,
      "repositoryName": "user/example"
    }
  ]
}
```

## Get billing usage summary for a user
Note
This endpoint is in public preview and is subject to change.
Gets a summary report of usage for a user.
Note:Only data from the past 24 months is accessible via this endpoint.

### Fine-grained access tokens for "Get billing usage summary for a user"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Plan" user permissions (read)

### Parameters for "Get billing usage summary for a user"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
usernamestringRequiredThe handle for the GitHub user account.
[/TABLE]
The handle for the GitHub user account.

[TABLE]
Name, Type, Description
yearintegerIf specified, only return results for a single year. The value ofyearis an integer with four digits representing a year. For example,2025. Default value is the current year.
monthintegerIf specified, only return results for a single month. The value ofmonthis an integer between1and12. Default value is the current month. If no year is specified the defaultyearis used.
dayintegerIf specified, only return results for a single day. The value ofdayis an integer between1and31. If noyearormonthis specified, the defaultyearandmonthare used.
repositorystringThe repository name to query for usage in the format owner/repository.
productstringThe product name to query usage for. The name is not case sensitive.
skustringThe SKU to query for usage.
[/TABLE]
If specified, only return results for a single year. The value ofyearis an integer with four digits representing a year. For example,2025. Default value is the current year.
If specified, only return results for a single month. The value ofmonthis an integer between1and12. Default value is the current month. If no year is specified the defaultyearis used.
If specified, only return results for a single day. The value ofdayis an integer between1and31. If noyearormonthis specified, the defaultyearandmonthare used.
The repository name to query for usage in the format owner/repository.
The product name to query usage for. The name is not case sensitive.
The SKU to query for usage.

### HTTP response status codes for "Get billing usage summary for a user"

[TABLE]
Status code | Description
200 | Response when getting a billing usage summary
400 | Bad Request
403 | Forbidden
404 | Resource not found
500 | Internal Error
503 | Service unavailable
[/TABLE]
Response when getting a billing usage summary
Bad Request
Forbidden
Resource not found
Internal Error
Service unavailable

### Code samples for "Get billing usage summary for a user"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/users/USERNAME/settings/billing/usage/summary
```

#### Response when getting a billing usage summary
- Example response
- Response schema

```
Status: 200
```

```
{
  "timePeriod": {
    "year": 2025
  },
  "user": "monalisa",
  "usageItems": [
    {
      "product": "Actions",
      "sku": "actions_linux",
      "unitType": "minutes",
      "pricePerUnit": 0.008,
      "grossQuantity": 1000,
      "grossAmount": 8,
      "discountQuantity": 0,
      "discountAmount": 0,
      "netQuantity": 1000,
      "netAmount": 8
    }
  ]
}
```