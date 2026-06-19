# Budgets

*Source: https://docs.github.com/en/rest/billing/budgets*

---

# Budgets
Use the REST API to get budget information.

## Get all budgets for an organization
Note
This endpoint is in public preview and is subject to change.
Gets all budgets for an organization. The authenticated user must be an organization admin or billing manager.
Each page returns up to 10 budgets.

### Fine-grained access tokens for "Get all budgets for an organization"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Administration" organization permissions (read)

### Parameters for "Get all budgets for an organization"

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
pageintegerThe page number of the results to fetch.Default:1
per_pageintegerThe number of results per page (max 10).Default:10
scopestringFilter budgets by scope type.Can be one of:enterprise,organization,repository,cost_center
[/TABLE]
The page number of the results to fetch.
Default:1
The number of results per page (max 10).
Default:10
Filter budgets by scope type.
Can be one of:enterprise,organization,repository,cost_center

```
organization
```

```
cost_center
```

### HTTP response status codes for "Get all budgets for an organization"

[TABLE]
Status code | Description
200 | Response when getting all budgets
403 | Forbidden
404 | Resource not found
500 | Internal Error
[/TABLE]
Response when getting all budgets
Forbidden
Resource not found
Internal Error

### Code samples for "Get all budgets for an organization"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/organizations/ORG/settings/billing/budgets
```

#### Response when getting all budgets
- Example response
- Response schema

```
Status: 200
```

```
{
  "budgets": [
    {
      "id": "2066deda-923f-43f9-88d2-62395a28c0cdd",
      "budget_type": "ProductPricing",
      "budget_product_skus": [
        "actions"
      ],
      "budget_scope": "enterprise",
      "budget_amount": 1000,
      "prevent_further_usage": true,
      "budget_alerting": {
        "will_alert": true,
        "alert_recipients": [
          "enterprise-admin",
          "billing-manager"
        ]
      }
    },
    {
      "id": "f47ac10b-58cc-4372-a567-0e02b2c3d479",
      "budget_type": "SkuPricing",
      "budget_product_skus": [
        "actions_linux"
      ],
      "budget_scope": "organization",
      "budget_amount": 500,
      "prevent_further_usage": false,
      "budget_alerting": {
        "will_alert": true,
        "alert_recipients": [
          "org-owner"
        ]
      }
    },
    {
      "id": "6ba7b810-9dad-11d1-80b4-00c04fd430c8",
      "budget_type": "ProductPricing",
      "budget_product_skus": [
        "packages"
      ],
      "budget_scope": "cost_center",
      "budget_amount": 250,
      "prevent_further_usage": true,
      "budget_alerting": {
        "will_alert": false,
        "alert_recipients": []
      }
    }
  ],
  "has_next_page": false,
  "total_count": 3
}
```

## Get a budget by ID for an organization
Note
This endpoint is in public preview and is subject to change.
Gets a budget by ID. The authenticated user must be an organization admin or billing manager.

### Fine-grained access tokens for "Get a budget by ID for an organization"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Administration" organization permissions (read)

### Parameters for "Get a budget by ID for an organization"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
budget_idstringRequiredThe ID corresponding to the budget.
[/TABLE]
The organization name. The name is not case sensitive.
The ID corresponding to the budget.

### HTTP response status codes for "Get a budget by ID for an organization"

[TABLE]
Status code | Description
200 | Response when updating a budget
400 | Bad Request
403 | Forbidden
404 | Resource not found
500 | Internal Error
503 | Service unavailable
[/TABLE]
Response when updating a budget
Bad Request
Forbidden
Resource not found
Internal Error
Service unavailable

### Code samples for "Get a budget by ID for an organization"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/organizations/ORG/settings/billing/budgets/BUDGET_ID
```

#### Response when updating a budget
- Example response
- Response schema

```
Status: 200
```

```
{
  "id": "2066deda-923f-43f9-88d2-62395a28c0cdd",
  "budget_type": "ProductPricing",
  "budget_product_sku": "actions_linux",
  "budget_scope": "repository",
  "budget_entity_name": "example-repo-name",
  "budget_amount": 0,
  "prevent_further_usage": true,
  "budget_alerting": {
    "will_alert": true,
    "alert_recipients": [
      "mona",
      "lisa"
    ]
  }
}
```

## Update a budget for an organization
Note
This endpoint is in public preview and is subject to change.
Updates an existing budget for an organization. The authenticated user must be an organization admin or billing manager.

### Fine-grained access tokens for "Update a budget for an organization"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Administration" organization permissions (write)

### Parameters for "Update a budget for an organization"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
budget_idstringRequiredThe ID corresponding to the budget.
[/TABLE]
The organization name. The name is not case sensitive.
The ID corresponding to the budget.

[TABLE]
Name, Type, Description
budget_amountintegerThe budget amount in whole dollars. For license-based products, this represents the number of licenses.
prevent_further_usagebooleanWhether to prevent additional spending once the budget is exceeded
budget_alertingobject
Properties ofbudget_alertingName, Type, Descriptionwill_alertbooleanWhether alerts are enabled for this budgetalert_recipientsarray of stringsArray of user login names who will receive alerts | Name, Type, Description | will_alertbooleanWhether alerts are enabled for this budget | alert_recipientsarray of stringsArray of user login names who will receive alerts
Name, Type, Description
will_alertbooleanWhether alerts are enabled for this budget
alert_recipientsarray of stringsArray of user login names who will receive alerts
budget_scopestringThe scope of the budgetCan be one of:enterprise,organization,repository,cost_center
budget_entity_namestringThe name of the entity to apply the budget to
budget_typestringThe type of pricing for the budget
budget_product_skustringA single product or SKU that will be covered in the budget
[/TABLE]

```
budget_amount
```
The budget amount in whole dollars. For license-based products, this represents the number of licenses.

```
prevent_further_usage
```
Whether to prevent additional spending once the budget is exceeded

```
budget_alerting
```

```
budget_alerting
```

[TABLE]
Name, Type, Description
will_alertbooleanWhether alerts are enabled for this budget
alert_recipientsarray of stringsArray of user login names who will receive alerts
[/TABLE]
Whether alerts are enabled for this budget

```
alert_recipients
```
Array of user login names who will receive alerts

```
budget_scope
```
The scope of the budget
Can be one of:enterprise,organization,repository,cost_center

```
organization
```

```
cost_center
```

```
budget_entity_name
```
The name of the entity to apply the budget to

```
budget_type
```
The type of pricing for the budget

```
budget_product_sku
```
A single product or SKU that will be covered in the budget

### HTTP response status codes for "Update a budget for an organization"

[TABLE]
Status code | Description
200 | Budget updated successfully
400 | Bad Request
401 | Requires authentication
403 | Forbidden
404 | Budget not found or feature not enabled
422 | Validation failed, or the endpoint has been spammed.
500 | Internal server error
[/TABLE]
Budget updated successfully
Bad Request
Requires authentication
Forbidden
Budget not found or feature not enabled
Validation failed, or the endpoint has been spammed.
Internal server error

### Code samples for "Update a budget for an organization"

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
  https://api.github.com/organizations/ORG/settings/billing/budgets/BUDGET_ID \
  -d '{"prevent_further_usage":false,"budget_amount":10,"budget_alerting":{"will_alert":false,"alert_recipients":[]}}'
```

#### Budget updated successfully
- Example response
- Response schema

```
Status: 200
```

```
{
  "message": "Budget successfully updated.",
  "budget": {
    "id": "2066deda-923f-43f9-88d2-62395a28c0cdd",
    "budget_type": "ProductPricing",
    "budget_product_sku": "actions_linux",
    "budget_scope": "repository",
    "budget_entity_name": "org-name/example-repo-name",
    "budget_amount": 0,
    "prevent_further_usage": true,
    "budget_alerting": {
      "will_alert": true,
      "alert_recipients": [
        "mona",
        "lisa"
      ]
    }
  }
}
```

## Delete a budget for an organization
Note
This endpoint is in public preview and is subject to change.
Deletes a budget by ID for an organization. The authenticated user must be an organization admin or billing manager.

### Fine-grained access tokens for "Delete a budget for an organization"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Administration" organization permissions (write)

### Parameters for "Delete a budget for an organization"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
budget_idstringRequiredThe ID corresponding to the budget.
[/TABLE]
The organization name. The name is not case sensitive.
The ID corresponding to the budget.

### HTTP response status codes for "Delete a budget for an organization"

[TABLE]
Status code | Description
200 | Response when deleting a budget
400 | Bad Request
403 | Forbidden
404 | Resource not found
500 | Internal Error
503 | Service unavailable
[/TABLE]
Response when deleting a budget
Bad Request
Forbidden
Resource not found
Internal Error
Service unavailable

### Code samples for "Delete a budget for an organization"

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
  https://api.github.com/organizations/ORG/settings/billing/budgets/BUDGET_ID
```

#### Response when deleting a budget
- Example response
- Response schema

```
Status: 200
```

```
{
  "message": "Budget successfully deleted.",
  "budget_id": "2c1feb79-3947-4dc8-a16e-80cbd732cc0b"
}
```