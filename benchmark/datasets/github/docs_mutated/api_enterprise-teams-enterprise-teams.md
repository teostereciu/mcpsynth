# REST API endpoints for enterprise teams

*Source: https://docs.github.com/en/rest/enterprise-teams/enterprise-teams*

---

# REST API endpoints for enterprise teams
Use the REST API to create and manage enterprise teams in your GitHub enterprise.

## About enterprise teams
Note
These endpoints are currently in public preview and subject to change.
This API documentation is for enterprises on GitHub Enterprise Cloud.
If your enterprise is Copilot Business for non-GHE, please refer to the early access documentation link that was previously shared to you.
These endpoints are only available to authenticated members of the enterprise team's enterprise with classic personal access tokens with theread:enterprisescopeforGETAPIs andadmin:enterprisefor other APIs.
These endpoints are not compatible with fine-grained personal access tokens or GitHub App access tokens.
GitHub generates the enterprise team'sslugfrom the teamnameand adds theent:prefix.

## List enterprise teams
List all teams in the enterprise for the authenticated user

### Fine-grained access tokens for "List enterprise teams"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
The fine-grained token must have the following permission set:
- "Enterprise teams" enterprise permissions (read)

### Parameters for "List enterprise teams"

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
per_pageintegerThe number of results per page_number (max 100). For more information, see "Using pagination in the REST API."Default:30
pageintegerThe page_number number of the results to fetch. For more information, see "Using pagination in the REST API."Default:1
[/TABLE]
The number of results per page_number (max 100). For more information, see "Using pagination in the REST API."
Default:30
The page_number number of the results to fetch. For more information, see "Using pagination in the REST API."
Default:1

### HTTP response status codes for "List enterprise teams"

[TABLE]
Status code | Description
200 | OK
403 | Forbidden
[/TABLE]
OK
Forbidden

### Code samples for "List enterprise teams"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/enterprises/ENTERPRISE/teams
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
    "id": 1,
    "name": "Justice League",
    "description": "A great team.",
    "slug": "justice-league",
    "url": "https://api.github.com/enterprises/dc/teams/justice-league",
    "group_id": "62ab9291-fae2-468e-974b-7e45096d5021",
    "html_url": "https://github.com/enterprises/dc/teams/justice-league",
    "members_url": "https://api.github.com/enterprises/dc/teams/justice-league/members{/member}",
    "created_at": "2019-01-26T19:01:12Z",
    "updated_at": "2019-01-26T19:14:43Z"
  }
]
```

## Create an enterprise team
To create an enterprise team, the authenticated user must be an owner of the enterprise.

### Fine-grained access tokens for "Create an enterprise team"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
The fine-grained token must have the following permission set:
- "Enterprise teams" enterprise permissions (write)

### Parameters for "Create an enterprise team"

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
namestringRequiredThe name of the team.
descriptionstring or nullA description of the team.
sync_to_organizationsstringRetired: this field is no longer supported.
Whether the enterprise team should be reflected in each organization.
This value cannot be set.Default:disabledCan be one of:all,disabled
organization_selection_typestringSpecifies which organizations in the enterprise should have access to this team. Can be one ofdisabled,selected, orall.disabled: The team is not assigned to any organizations. This is the default when you create a new team.selected: The team is assigned to specific organizations. You can then use theadd organization assignments APIendpoint.all: The team is assigned to all current and future organizations in the enterprise.Default:disabledCan be one of:disabled,selected,all
group_idstring or nullThe ID of the IdP group to assign team membership with. You can get this value from theREST API endpoints for SCIM.
[/TABLE]
The name of the team.

```
description
```
A description of the team.

```
sync_to_organizations
```
Retired: this field is no longer supported.
Whether the enterprise team should be reflected in each organization.
This value cannot be set.
Default:disabled
Can be one of:all,disabled

```
organization_selection_type
```
Specifies which organizations in the enterprise should have access to this team. Can be one ofdisabled,selected, orall.disabled: The team is not assigned to any organizations. This is the default when you create a new team.selected: The team is assigned to specific organizations. You can then use theadd organization assignments APIendpoint.all: The team is assigned to all current and future organizations in the enterprise.
Default:disabled
Can be one of:disabled,selected,all
The ID of the IdP group to assign team membership with. You can get this value from theREST API endpoints for SCIM.

### HTTP response status codes for "Create an enterprise team"

[TABLE]
Status code | Description
201 | Created
[/TABLE]
Created

### Code samples for "Create an enterprise team"

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
  https://api.github.com/enterprises/ENTERPRISE/teams \
  -d '{"name":"Justice League","description":"A great team.","group_id":"62ab9291-fae2-468e-974b-7e45096d5021"}'
```

#### Response
- Example response
- Response schema

```
Status: 201
```

```
{
  "id": 1,
  "name": "Justice League",
  "description": "A great team.",
  "slug": "justice-league",
  "url": "https://api.github.com/enterprises/dc/teams/justice-league",
  "group_id": "62ab9291-fae2-468e-974b-7e45096d5021",
  "html_url": "https://github.com/enterprises/dc/teams/justice-league",
  "members_url": "https://api.github.com/enterprises/dc/teams/justice-league/members{/member}",
  "created_at": "2019-01-26T19:01:12Z",
  "updated_at": "2019-01-26T19:14:43Z"
}
```

## Get an enterprise team
Gets a team using the team's slug. To create the slug, GitHub replaces special characters in the name string, changes all words to lowercase, and replaces spaces with a-separator and adds the "ent:" prefix. For example, "My TEam Näme" would becomeent:my-team-name.

### Fine-grained access tokens for "Get an enterprise team"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
The fine-grained token must have the following permission set:
- "Enterprise teams" enterprise permissions (read)

### Parameters for "Get an enterprise team"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
enterprisestringRequiredThe slug version of the enterprise name.
team_slugstringRequiredThe slug of the team name.
[/TABLE]
The slug version of the enterprise name.
The slug of the team name.

### HTTP response status codes for "Get an enterprise team"

[TABLE]
Status code | Description
200 | OK
403 | Forbidden
[/TABLE]
OK
Forbidden

### Code samples for "Get an enterprise team"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/enterprises/ENTERPRISE/teams/TEAM_SLUG
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
  "name": "Justice League",
  "description": "A great team.",
  "slug": "justice-league",
  "url": "https://api.github.com/enterprises/dc/teams/justice-league",
  "group_id": "62ab9291-fae2-468e-974b-7e45096d5021",
  "html_url": "https://github.com/enterprises/dc/teams/justice-league",
  "members_url": "https://api.github.com/enterprises/dc/teams/justice-league/members{/member}",
  "created_at": "2019-01-26T19:01:12Z",
  "updated_at": "2019-01-26T19:14:43Z"
}
```

## Update an enterprise team
To edit a team, the authenticated user must be an enterprise owner.

### Fine-grained access tokens for "Update an enterprise team"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
The fine-grained token must have the following permission set:
- "Enterprise teams" enterprise permissions (write)

### Parameters for "Update an enterprise team"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
enterprisestringRequiredThe slug version of the enterprise name.
team_slugstringRequiredThe slug of the team name.
[/TABLE]
The slug version of the enterprise name.
The slug of the team name.

[TABLE]
Name, Type, Description
namestring or nullA new name for the team.
descriptionstring or nullA new description for the team.
sync_to_organizationsstringRetired: this field is no longer supported.
Whether the enterprise team should be reflected in each organization.
This value cannot be changed.Default:disabledCan be one of:all,disabled
organization_selection_typestringSpecifies which organizations in the enterprise should have access to this team. Can be one ofdisabled,selected, orall.disabled: The team is not assigned to any organizations. This is the default when you create a new team.selected: The team is assigned to specific organizations. You can then use theadd organization assignments API.all: The team is assigned to all current and future organizations in the enterprise.Default:disabledCan be one of:disabled,selected,all
group_idstring or nullThe ID of the IdP group to assign team membership with. The new IdP group will replace the existing one, or replace existing direct members if the team isn't currently linked to an IdP group.
[/TABLE]
A new name for the team.

```
description
```
A new description for the team.

```
sync_to_organizations
```
Retired: this field is no longer supported.
Whether the enterprise team should be reflected in each organization.
This value cannot be changed.
Default:disabled
Can be one of:all,disabled

```
organization_selection_type
```
Specifies which organizations in the enterprise should have access to this team. Can be one ofdisabled,selected, orall.disabled: The team is not assigned to any organizations. This is the default when you create a new team.selected: The team is assigned to specific organizations. You can then use theadd organization assignments API.all: The team is assigned to all current and future organizations in the enterprise.
Default:disabled
Can be one of:disabled,selected,all
The ID of the IdP group to assign team membership with. The new IdP group will replace the existing one, or replace existing direct members if the team isn't currently linked to an IdP group.

### HTTP response status codes for "Update an enterprise team"

[TABLE]
Status code | Description
200 | OK
403 | Forbidden
[/TABLE]
OK
Forbidden

### Code samples for "Update an enterprise team"

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
  https://api.github.com/enterprises/ENTERPRISE/teams/TEAM_SLUG \
  -d '{"name":"Justice League","description":"A great team.","group_id":"62ab9291-fae2-468e-974b-7e45096d5021"}'
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
  "name": "Justice League",
  "description": "A great team.",
  "slug": "justice-league",
  "url": "https://api.github.com/enterprises/dc/teams/justice-league",
  "group_id": "62ab9291-fae2-468e-974b-7e45096d5021",
  "html_url": "https://github.com/enterprises/dc/teams/justice-league",
  "members_url": "https://api.github.com/enterprises/dc/teams/justice-league/members{/member}",
  "created_at": "2019-01-26T19:01:12Z",
  "updated_at": "2019-01-26T19:14:43Z"
}
```

## Delete an enterprise team
To delete an enterprise team, the authenticated user must be an enterprise owner.
If you are an enterprise owner, deleting an enterprise team will delete all of its IdP mappings as well.

### Fine-grained access tokens for "Delete an enterprise team"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
The fine-grained token must have the following permission set:
- "Enterprise teams" enterprise permissions (write)

### Parameters for "Delete an enterprise team"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
enterprisestringRequiredThe slug version of the enterprise name.
team_slugstringRequiredThe slug of the team name.
[/TABLE]
The slug version of the enterprise name.
The slug of the team name.

### HTTP response status codes for "Delete an enterprise team"

[TABLE]
Status code | Description
204 | No Content
403 | Forbidden
[/TABLE]
No Content
Forbidden

### Code samples for "Delete an enterprise team"

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
  https://api.github.com/enterprises/ENTERPRISE/teams/TEAM_SLUG
```

#### Response

```
Status: 204
```