# REST API endpoints for secret scanning push protection

*Source: https://docs.github.com/en/rest/secret-scanning/push-protection*

---

# REST API endpoints for secret scanning push protection
Use the REST API to manage secret scanning push protection.

## List organization pattern configurations
Lists the secret scanning pattern configurations for an organization.
Personal access tokens (classic) need theread:orgscope to use this endpoint.

### Fine-grained access tokens for "List organization pattern configurations"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Administration" organization permissions (read)

### Parameters for "List organization pattern configurations"

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

### HTTP response status codes for "List organization pattern configurations"

[TABLE]
Status code | Description
200 | OK
403 | Forbidden
404 | Resource not found
[/TABLE]
OK
Forbidden
Resource not found

### Code samples for "List organization pattern configurations"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/orgs/ORG/secret-scanning/pattern-configurations
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "pattern_config_version": "0ujsswThIGTUYm2K8FjOOfXtY1K",
  "provider_pattern_overrides": [
    {
      "token_type": "GITHUB_PERSONAL_ACCESS_TOKEN",
      "slug": "github_personal_access_token_legacy_v2",
      "display_name": "GitHub Personal Access Token (Legacy v2)",
      "alert_total": 15,
      "alert_total_percentage": 36,
      "false_positives": 2,
      "false_positive_rate": 13,
      "bypass_rate": 13,
      "default_setting": "enabled",
      "setting": "enabled",
      "enterprise_setting": "enabled"
    }
  ],
  "custom_pattern_overrides": [
    {
      "token_type": "cp_2",
      "custom_pattern_version": "0ujsswThIGTUYm2K8FjOOfXtY1K",
      "slug": "custom-api-key",
      "display_name": "Custom API Key",
      "alert_total": 15,
      "alert_total_percentage": 36,
      "false_positives": 3,
      "false_positive_rate": 20,
      "bypass_rate": 20,
      "default_setting": "disabled",
      "setting": "enabled"
    }
  ]
}
```

## Update organization pattern configurations
Updates the secret scanning pattern configurations for an organization.
Personal access tokens (classic) need thewrite:orgscope to use this endpoint.

### Fine-grained access tokens for "Update organization pattern configurations"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Administration" organization permissions (write)

### Parameters for "Update organization pattern configurations"

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
pattern_config_versionstring or nullThe version of the entity. This is used to confirm you're updating the current version of the entity and mitigate unintentionally overriding someone else's update.
provider_pattern_settingsarray of objectsPattern settings for provider patterns.
Properties ofprovider_pattern_settingsName, Type, Descriptiontoken_typestringThe ID of the pattern to configure.push_protection_settingstringPush protection setting to set for the pattern.Can be one of:not-set,disabled,enabled | Name, Type, Description | token_typestringThe ID of the pattern to configure. | push_protection_settingstringPush protection setting to set for the pattern.Can be one of:not-set,disabled,enabled
Name, Type, Description
token_typestringThe ID of the pattern to configure.
push_protection_settingstringPush protection setting to set for the pattern.Can be one of:not-set,disabled,enabled
custom_pattern_settingsarray of objectsPattern settings for custom patterns.
Properties ofcustom_pattern_settingsName, Type, Descriptiontoken_typestringThe ID of the pattern to configure.custom_pattern_versionstring or nullThe version of the entity. This is used to confirm you're updating the current version of the entity and mitigate unintentionally overriding someone else's update.push_protection_settingstringPush protection setting to set for the pattern.Can be one of:disabled,enabled | Name, Type, Description | token_typestringThe ID of the pattern to configure. | custom_pattern_versionstring or nullThe version of the entity. This is used to confirm you're updating the current version of the entity and mitigate unintentionally overriding someone else's update. | push_protection_settingstringPush protection setting to set for the pattern.Can be one of:disabled,enabled
Name, Type, Description
token_typestringThe ID of the pattern to configure.
custom_pattern_versionstring or nullThe version of the entity. This is used to confirm you're updating the current version of the entity and mitigate unintentionally overriding someone else's update.
push_protection_settingstringPush protection setting to set for the pattern.Can be one of:disabled,enabled
[/TABLE]

```
pattern_config_version
```
The version of the entity. This is used to confirm you're updating the current version of the entity and mitigate unintentionally overriding someone else's update.

```
provider_pattern_settings
```
Pattern settings for provider patterns.

```
provider_pattern_settings
```

[TABLE]
Name, Type, Description
token_typestringThe ID of the pattern to configure.
push_protection_settingstringPush protection setting to set for the pattern.Can be one of:not-set,disabled,enabled
[/TABLE]
The ID of the pattern to configure.

```
push_protection_setting
```
Push protection setting to set for the pattern.
Can be one of:not-set,disabled,enabled

```
custom_pattern_settings
```
Pattern settings for custom patterns.

```
custom_pattern_settings
```

[TABLE]
Name, Type, Description
token_typestringThe ID of the pattern to configure.
custom_pattern_versionstring or nullThe version of the entity. This is used to confirm you're updating the current version of the entity and mitigate unintentionally overriding someone else's update.
push_protection_settingstringPush protection setting to set for the pattern.Can be one of:disabled,enabled
[/TABLE]
The ID of the pattern to configure.

```
custom_pattern_version
```
The version of the entity. This is used to confirm you're updating the current version of the entity and mitigate unintentionally overriding someone else's update.

```
push_protection_setting
```
Push protection setting to set for the pattern.
Can be one of:disabled,enabled

### HTTP response status codes for "Update organization pattern configurations"

[TABLE]
Status code | Description
200 | OK
400 | Bad Request
403 | Forbidden
404 | Resource not found
409 | Conflict
422 | Validation failed, or the endpoint has been spammed.
[/TABLE]
OK
Bad Request
Forbidden
Resource not found
Conflict
Validation failed, or the endpoint has been spammed.

### Code samples for "Update organization pattern configurations"

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
  https://api.github.com/orgs/ORG/secret-scanning/pattern-configurations \
  -d '{"pattern_config_version":"0ujsswThIGTUYm2K8FjOOfXtY1K","provider_pattern_settings":[{"token_type":"GITHUB_PERSONAL_ACCESS_TOKEN","push_protection_setting":"enabled"}],"custom_pattern_settings":[{"token_type":"cp_2","custom_pattern_version":"0ujsswThIGTUYm2K8FjOOfXtY1K","push_protection_setting":"enabled"}]}'
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "pattern_config_version": "0ujsswThIGTUYm2K8FjOOfXtY1K"
}
```