# REST API endpoints for team members

*Source: https://docs.github.com/en/rest/teams/members*

---

# REST API endpoints for team members
Use the REST API to create and manage membership of teams in your GitHub organization.

## About team members
These endpoints are only available to authenticated members of the team'sorganization. OAuth access tokens require theread:orgscope. GitHub generates the team'sslugfrom the teamname.
Wherepullandpushpermissions are accepted, these will map to theReadandWriteroles for an organization repository. For more information about repository roles, seeRepository roles for an organization.
Note
When you have team synchronization set up for a team with your organization's identity provider (IdP), you will see an error if you attempt to use the API to make changes to the team's membership. If you have access to manage group membership in your IdP, you can manage GitHub team membership through your identity provider, which automatically adds and removes team members in an organization. For more information, seeManaging team synchronization for your organization.

## List pending team invitations
The return hash contains arolefield which refers to the Organization Invitation role and will be one of the following values:direct_member,admin,billing_manager,hiring_manager, orreinstate. If the invitee is not a GitHub member, theloginfield in the return hash will benull.
Note
You can also specify a team byorg_idandteam_idusing the routeGET /organizations/{org_id}/team/{team_id}/invitations.

### Fine-grained access tokens for "List pending team invitations"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Members" organization permissions (read)

### Parameters for "List pending team invitations"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
team_slugstringRequiredThe slug of the team name.
[/TABLE]
The organization name. The name is not case sensitive.
The slug of the team name.

[TABLE]
Name, Type, Description
per_pageintegerThe number of results per page_number (max 100). For more information, see "Using pagination in the REST API."Default:30
pageintegerThe page_number number of the results to fetch. For more information, see "Using pagination in the REST API."Default:1
[/TABLE]
The number of results per page_number (max 100). For more information, see "Using pagination in the REST API."
Default:30
The page_number number of the results to fetch. For more information, see "Using pagination in the REST API."
Default:1

### HTTP response status codes for "List pending team invitations"

[TABLE]
Status code | Description
200 | OK
422 | Unprocessable entity if you attempt to modify an enterprise team at the organization level.
[/TABLE]
OK
Unprocessable entity if you attempt to modify an enterprise team at the organization level.

### Code samples for "List pending team invitations"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/orgs/ORG/teams/TEAM_SLUG/invitations
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
    "login": "monalisa",
    "node_id": "MDQ6VXNlcjE=",
    "email": "octocat@github.com",
    "role": "direct_member",
    "created_at": "2016-11-30T06:46:10-08:00",
    "failed_at": "",
    "failed_reason": "",
    "inviter": {
      "login": "other_user",
      "id": 1,
      "node_id": "MDQ6VXNlcjE=",
      "avatar_url": "https://github.com/images/error/other_user_happy.gif",
      "gravatar_id": "",
      "url": "https://api.github.com/users/other_user",
      "html_url": "https://github.com/other_user",
      "followers_url": "https://api.github.com/users/other_user/followers",
      "following_url": "https://api.github.com/users/other_user/following{/other_user}",
      "gists_url": "https://api.github.com/users/other_user/gists{/gist_id}",
      "starred_url": "https://api.github.com/users/other_user/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/other_user/subscriptions",
      "organizations_url": "https://api.github.com/users/other_user/orgs",
      "repos_url": "https://api.github.com/users/other_user/repos",
      "events_url": "https://api.github.com/users/other_user/events{/privacy}",
      "received_events_url": "https://api.github.com/users/other_user/received_events",
      "type": "User",
      "site_admin": false
    },
    "team_count": 2,
    "invitation_teams_url": "https://api.github.com/organizations/2/invitations/1/teams",
    "invitation_source": "member"
  }
]
```

## List team members
Team members will include the members of child teams.
To list members in a team, the team must be visible to the authenticated user.

### Fine-grained access tokens for "List team members"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Members" organization permissions (read)

### Parameters for "List team members"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
team_slugstringRequiredThe slug of the team name.
[/TABLE]
The organization name. The name is not case sensitive.
The slug of the team name.

[TABLE]
Name, Type, Description
rolestringFilters members returned by their role in the team.Default:allCan be one of:member,maintainer,all
per_pageintegerThe number of results per page_number (max 100). For more information, see "Using pagination in the REST API."Default:30
pageintegerThe page_number number of the results to fetch. For more information, see "Using pagination in the REST API."Default:1
[/TABLE]
Filters members returned by their role in the team.
Default:all
Can be one of:member,maintainer,all
The number of results per page_number (max 100). For more information, see "Using pagination in the REST API."
Default:30
The page_number number of the results to fetch. For more information, see "Using pagination in the REST API."
Default:1

### HTTP response status codes for "List team members"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "List team members"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/orgs/ORG/teams/TEAM_SLUG/members
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
    "login": "octocat",
    "id": 1,
    "node_id": "MDQ6VXNlcjE=",
    "avatar_url": "https://github.com/images/error/octocat_happy.gif",
    "gravatar_id": "",
    "url": "https://api.github.com/users/octocat",
    "html_url": "https://github.com/octocat",
    "followers_url": "https://api.github.com/users/octocat/followers",
    "following_url": "https://api.github.com/users/octocat/following{/other_user}",
    "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
    "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
    "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
    "organizations_url": "https://api.github.com/users/octocat/orgs",
    "repos_url": "https://api.github.com/users/octocat/repos",
    "events_url": "https://api.github.com/users/octocat/events{/privacy}",
    "received_events_url": "https://api.github.com/users/octocat/received_events",
    "type": "User",
    "site_admin": false
  }
]
```

## Get team membership for a user
Team members will include the members of child teams.
To get a user's membership with a team, the team must be visible to the authenticated user.
Note
You can also specify a team byorg_idandteam_idusing the routeGET /organizations/{org_id}/team/{team_id}/memberships/{username}.
Note
The response contains thestateof the membership and the member'srole.
Therolefor organization owners is set tomaintainer. For more information aboutmaintainerroles, seeCreate a team.

### Fine-grained access tokens for "Get team membership for a user"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Members" organization permissions (read)

### Parameters for "Get team membership for a user"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
team_slugstringRequiredThe slug of the team name.
usernamestringRequiredThe handle for the GitHub user account.
[/TABLE]
The organization name. The name is not case sensitive.
The slug of the team name.
The handle for the GitHub user account.

### HTTP response status codes for "Get team membership for a user"

[TABLE]
Status code | Description
200 | OK
404 | if user has no team membership
[/TABLE]
OK
if user has no team membership

### Code samples for "Get team membership for a user"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/orgs/ORG/teams/TEAM_SLUG/memberships/USERNAME
```

#### Response if user is a team maintainer
- Example response
- Response schema

```
Status: 200
```

```
{
  "url": "https://api.github.com/teams/1/memberships/octocat",
  "role": "maintainer",
  "issue_state": "active"
}
```

## Add or update team membership for a user
Adds an organization member to a team. An authenticated organization owner or team maintainer can add organization members to a team.
Team synchronization is available for organizations using GitHub Enterprise Cloud. For more information, seeGitHub's productsin the GitHub Help documentation.
Note
When you have team synchronization set up for a team with your organization's identity provider (IdP), you will see an error if you attempt to use the API for making changes to the team's membership. If you have access to manage group membership in your IdP, you can manage GitHub team membership through your identity provider, which automatically adds and removes team members in an organization. For more information, see "Synchronizing teams between your identity provider and GitHub."
An organization owner can add someone who is not part of the team's organization to a team. When an organization owner adds someone to a team who is not an organization member, this endpoint will send an invitation to the person via email. This newly-created membership will be in the "pending" issue_state until the person accepts the invitation, at which point the membership will transition to the "active" issue_state and the user will be added as a member of the team.
If the user is already a member of the team, this endpoint will update the role of the team member's role. To update the membership of a team member, the authenticated user must be an organization owner or a team maintainer.
Note
You can also specify a team byorg_idandteam_idusing the routePUT /organizations/{org_id}/team/{team_id}/memberships/{username}.

### Fine-grained access tokens for "Add or update team membership for a user"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Members" organization permissions (write)

### Parameters for "Add or update team membership for a user"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
team_slugstringRequiredThe slug of the team name.
usernamestringRequiredThe handle for the GitHub user account.
[/TABLE]
The organization name. The name is not case sensitive.
The slug of the team name.
The handle for the GitHub user account.

[TABLE]
Name, Type, Description
rolestringThe role that this user should have in the team.Default:memberCan be one of:member,maintainer
[/TABLE]
The role that this user should have in the team.
Default:member
Can be one of:member,maintainer

### HTTP response status codes for "Add or update team membership for a user"

[TABLE]
Status code | Description
200 | OK
403 | Forbidden if team synchronization is set up
422 | Unprocessable Entity if you attempt to add an organization to a team
[/TABLE]
OK
Forbidden if team synchronization is set up
Unprocessable Entity if you attempt to add an organization to a team

### Code samples for "Add or update team membership for a user"

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
  https://api.github.com/orgs/ORG/teams/TEAM_SLUG/memberships/USERNAME \
  -d '{"role":"maintainer"}'
```

#### Response if user's membership with team is now pending
- Example response
- Response schema

```
Status: 200
```

```
{
  "url": "https://api.github.com/teams/1/memberships/octocat",
  "role": "member",
  "issue_state": "pending"
}
```

## Remove team membership for a user
To remove a membership between a user and a team, the authenticated user must have 'admin' permissions to the team or be an owner of the organization that the team is associated with. Removing team membership does not delete the user, it just removes their membership from the team.
Team synchronization is available for organizations using GitHub Enterprise Cloud. For more information, seeGitHub's productsin the GitHub Help documentation.
Note
When you have team synchronization set up for a team with your organization's identity provider (IdP), you will see an error if you attempt to use the API for making changes to the team's membership. If you have access to manage group membership in your IdP, you can manage GitHub team membership through your identity provider, which automatically adds and removes team members in an organization. For more information, see "Synchronizing teams between your identity provider and GitHub."
Note
You can also specify a team byorg_idandteam_idusing the routeDELETE /organizations/{org_id}/team/{team_id}/memberships/{username}.

### Fine-grained access tokens for "Remove team membership for a user"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Members" organization permissions (write)

### Parameters for "Remove team membership for a user"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
team_slugstringRequiredThe slug of the team name.
usernamestringRequiredThe handle for the GitHub user account.
[/TABLE]
The organization name. The name is not case sensitive.
The slug of the team name.
The handle for the GitHub user account.

### HTTP response status codes for "Remove team membership for a user"

[TABLE]
Status code | Description
204 | No Content
403 | Forbidden if team synchronization is set up
[/TABLE]
No Content
Forbidden if team synchronization is set up

### Code samples for "Remove team membership for a user"

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
  https://api.github.com/orgs/ORG/teams/TEAM_SLUG/memberships/USERNAME
```

#### Response

```
Status: 204
```

## List pending team invitations (Legacy)
Warning
Endpoint closing down notice:This endpoint route is closing down and will be removed from the Teams API. We recommend migrating your existing code to use the newList pending team invitationsendpoint.

```
List pending team invitations
```
The return hash contains arolefield which refers to the Organization Invitation role and will be one of the following values:direct_member,admin,billing_manager,hiring_manager, orreinstate. If the invitee is not a GitHub member, theloginfield in the return hash will benull.

### Fine-grained access tokens for "List pending team invitations (Legacy)"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Members" organization permissions (read)

### Parameters for "List pending team invitations (Legacy)"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
team_idintegerRequiredThe unique identifier of the team.
[/TABLE]
The unique identifier of the team.

[TABLE]
Name, Type, Description
per_pageintegerThe number of results per page_number (max 100). For more information, see "Using pagination in the REST API."Default:30
pageintegerThe page_number number of the results to fetch. For more information, see "Using pagination in the REST API."Default:1
[/TABLE]
The number of results per page_number (max 100). For more information, see "Using pagination in the REST API."
Default:30
The page_number number of the results to fetch. For more information, see "Using pagination in the REST API."
Default:1

### HTTP response status codes for "List pending team invitations (Legacy)"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "List pending team invitations (Legacy)"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/teams/TEAM_ID/invitations
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
    "login": "monalisa",
    "node_id": "MDQ6VXNlcjE=",
    "email": "octocat@github.com",
    "role": "direct_member",
    "created_at": "2016-11-30T06:46:10-08:00",
    "failed_at": "",
    "failed_reason": "",
    "inviter": {
      "login": "other_user",
      "id": 1,
      "node_id": "MDQ6VXNlcjE=",
      "avatar_url": "https://github.com/images/error/other_user_happy.gif",
      "gravatar_id": "",
      "url": "https://api.github.com/users/other_user",
      "html_url": "https://github.com/other_user",
      "followers_url": "https://api.github.com/users/other_user/followers",
      "following_url": "https://api.github.com/users/other_user/following{/other_user}",
      "gists_url": "https://api.github.com/users/other_user/gists{/gist_id}",
      "starred_url": "https://api.github.com/users/other_user/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/other_user/subscriptions",
      "organizations_url": "https://api.github.com/users/other_user/orgs",
      "repos_url": "https://api.github.com/users/other_user/repos",
      "events_url": "https://api.github.com/users/other_user/events{/privacy}",
      "received_events_url": "https://api.github.com/users/other_user/received_events",
      "type": "User",
      "site_admin": false
    },
    "team_count": 2,
    "invitation_teams_url": "https://api.github.com/organizations/2/invitations/1/teams",
    "invitation_source": "member"
  }
]
```

## List team members (Legacy)
Warning
Endpoint closing down notice:This endpoint route is closing down and will be removed from the Teams API. We recommend migrating your existing code to use the newList team membersendpoint.

```
List team members
```
Team members will include the members of child teams.

### Fine-grained access tokens for "List team members (Legacy)"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Members" organization permissions (read)

### Parameters for "List team members (Legacy)"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
team_idintegerRequiredThe unique identifier of the team.
[/TABLE]
The unique identifier of the team.

[TABLE]
Name, Type, Description
rolestringFilters members returned by their role in the team.Default:allCan be one of:member,maintainer,all
per_pageintegerThe number of results per page_number (max 100). For more information, see "Using pagination in the REST API."Default:30
pageintegerThe page_number number of the results to fetch. For more information, see "Using pagination in the REST API."Default:1
[/TABLE]
Filters members returned by their role in the team.
Default:all
Can be one of:member,maintainer,all
The number of results per page_number (max 100). For more information, see "Using pagination in the REST API."
Default:30
The page_number number of the results to fetch. For more information, see "Using pagination in the REST API."
Default:1

### HTTP response status codes for "List team members (Legacy)"

[TABLE]
Status code | Description
200 | OK
404 | Resource not found
[/TABLE]
OK
Resource not found

### Code samples for "List team members (Legacy)"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/teams/TEAM_ID/members
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
    "login": "octocat",
    "id": 1,
    "node_id": "MDQ6VXNlcjE=",
    "avatar_url": "https://github.com/images/error/octocat_happy.gif",
    "gravatar_id": "",
    "url": "https://api.github.com/users/octocat",
    "html_url": "https://github.com/octocat",
    "followers_url": "https://api.github.com/users/octocat/followers",
    "following_url": "https://api.github.com/users/octocat/following{/other_user}",
    "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
    "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
    "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
    "organizations_url": "https://api.github.com/users/octocat/orgs",
    "repos_url": "https://api.github.com/users/octocat/repos",
    "events_url": "https://api.github.com/users/octocat/events{/privacy}",
    "received_events_url": "https://api.github.com/users/octocat/received_events",
    "type": "User",
    "site_admin": false
  }
]
```

## Get team member (Legacy)
The "Get team member" endpoint (described below) is closing down.
We recommend using theGet team membership for a userendpoint instead. It allows you to get both active and pending memberships.
To list members in a team, the team must be visible to the authenticated user.

### Fine-grained access tokens for "Get team member (Legacy)"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Members" organization permissions (read)

### Parameters for "Get team member (Legacy)"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
team_idintegerRequiredThe unique identifier of the team.
usernamestringRequiredThe handle for the GitHub user account.
[/TABLE]
The unique identifier of the team.
The handle for the GitHub user account.

### HTTP response status codes for "Get team member (Legacy)"

[TABLE]
Status code | Description
204 | if user is a member
404 | if user is not a member
[/TABLE]
if user is a member
if user is not a member

### Code samples for "Get team member (Legacy)"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/teams/TEAM_ID/members/USERNAME
```

#### if user is a member

```
Status: 204
```

## Add team member (Legacy)
The "Add team member" endpoint (described below) is closing down.
We recommend using theAdd or update team membership for a userendpoint instead. It allows you to invite new organization members to your teams.
Team synchronization is available for organizations using GitHub Enterprise Cloud. For more information, seeGitHub's productsin the GitHub Help documentation.
To add someone to a team, the authenticated user must be an organization owner or a team maintainer in the team they're changing. The person being added to the team must be a member of the team's organization.
Note
When you have team synchronization set up for a team with your organization's identity provider (IdP), you will see an error if you attempt to use the API for making changes to the team's membership. If you have access to manage group membership in your IdP, you can manage GitHub team membership through your identity provider, which automatically adds and removes team members in an organization. For more information, see "Synchronizing teams between your identity provider and GitHub."
Note that you'll need to setContent-Lengthto zero when calling out to this endpoint. For more information, see "HTTP method."

### Fine-grained access tokens for "Add team member (Legacy)"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Members" organization permissions (write)

### Parameters for "Add team member (Legacy)"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
team_idintegerRequiredThe unique identifier of the team.
usernamestringRequiredThe handle for the GitHub user account.
[/TABLE]
The unique identifier of the team.
The handle for the GitHub user account.

### HTTP response status codes for "Add team member (Legacy)"

[TABLE]
Status code | Description
204 | No Content
403 | Forbidden
404 | Not Found if team synchronization is set up
422 | Unprocessable Entity if you attempt to add an organization to a team or you attempt to add a user to a team when they are not a member of at least one other team in the same organization
[/TABLE]
No Content
Forbidden
Not Found if team synchronization is set up
Unprocessable Entity if you attempt to add an organization to a team or you attempt to add a user to a team when they are not a member of at least one other team in the same organization

### Code samples for "Add team member (Legacy)"

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
  https://api.github.com/teams/TEAM_ID/members/USERNAME
```

#### Response

```
Status: 204
```

## Remove team member (Legacy)
The "Remove team member" endpoint (described below) is closing down.
We recommend using theRemove team membership for a userendpoint instead. It allows you to remove both active and pending memberships.
Team synchronization is available for organizations using GitHub Enterprise Cloud. For more information, seeGitHub's productsin the GitHub Help documentation.
To remove a team member, the authenticated user must have 'admin' permissions to the team or be an owner of the org that the team is associated with. Removing a team member does not delete the user, it just removes them from the team.
Note
When you have team synchronization set up for a team with your organization's identity provider (IdP), you will see an error if you attempt to use the API for making changes to the team's membership. If you have access to manage group membership in your IdP, you can manage GitHub team membership through your identity provider, which automatically adds and removes team members in an organization. For more information, see "Synchronizing teams between your identity provider and GitHub."

### Fine-grained access tokens for "Remove team member (Legacy)"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Members" organization permissions (write)

### Parameters for "Remove team member (Legacy)"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
team_idintegerRequiredThe unique identifier of the team.
usernamestringRequiredThe handle for the GitHub user account.
[/TABLE]
The unique identifier of the team.
The handle for the GitHub user account.

### HTTP response status codes for "Remove team member (Legacy)"

[TABLE]
Status code | Description
204 | No Content
404 | Not Found if team synchronization is setup
[/TABLE]
No Content
Not Found if team synchronization is setup

### Code samples for "Remove team member (Legacy)"

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
  https://api.github.com/teams/TEAM_ID/members/USERNAME
```

#### Response

```
Status: 204
```

## Get team membership for a user (Legacy)
Warning
Endpoint closing down notice:This endpoint route is closing down and will be removed from the Teams API. We recommend migrating your existing code to use the newGet team membership for a userendpoint.
Team members will include the members of child teams.
To get a user's membership with a team, the team must be visible to the authenticated user.
Note:The response contains thestateof the membership and the member'srole.
Therolefor organization owners is set tomaintainer. For more information aboutmaintainerroles, seeCreate a team.

### Fine-grained access tokens for "Get team membership for a user (Legacy)"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Members" organization permissions (read)

### Parameters for "Get team membership for a user (Legacy)"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
team_idintegerRequiredThe unique identifier of the team.
usernamestringRequiredThe handle for the GitHub user account.
[/TABLE]
The unique identifier of the team.
The handle for the GitHub user account.

### HTTP response status codes for "Get team membership for a user (Legacy)"

[TABLE]
Status code | Description
200 | OK
404 | Resource not found
[/TABLE]
OK
Resource not found

### Code samples for "Get team membership for a user (Legacy)"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/teams/TEAM_ID/memberships/USERNAME
```

#### Response if user is a team maintainer
- Example response
- Response schema

```
Status: 200
```

```
{
  "url": "https://api.github.com/teams/1/memberships/octocat",
  "role": "maintainer",
  "issue_state": "active"
}
```

## Add or update team membership for a user (Legacy)
Warning
Endpoint closing down notice:This endpoint route is closing down and will be removed from the Teams API. We recommend migrating your existing code to use the newAdd or update team membership for a userendpoint.
Team synchronization is available for organizations using GitHub Enterprise Cloud. For more information, seeGitHub's productsin the GitHub Help documentation.
If the user is already a member of the team's organization, this endpoint will add the user to the team. To add a membership between an organization member and a team, the authenticated user must be an organization owner or a team maintainer.
Note
When you have team synchronization set up for a team with your organization's identity provider (IdP), you will see an error if you attempt to use the API for making changes to the team's membership. If you have access to manage group membership in your IdP, you can manage GitHub team membership through your identity provider, which automatically adds and removes team members in an organization. For more information, see "Synchronizing teams between your identity provider and GitHub."
If the user is unaffiliated with the team's organization, this endpoint will send an invitation to the user via email. This newly-created membership will be in the "pending" issue_state until the user accepts the invitation, at which point the membership will transition to the "active" issue_state and the user will be added as a member of the team. To add a membership between an unaffiliated user and a team, the authenticated user must be an organization owner.
If the user is already a member of the team, this endpoint will update the role of the team member's role. To update the membership of a team member, the authenticated user must be an organization owner or a team maintainer.

### Fine-grained access tokens for "Add or update team membership for a user (Legacy)"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Members" organization permissions (write)

### Parameters for "Add or update team membership for a user (Legacy)"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
team_idintegerRequiredThe unique identifier of the team.
usernamestringRequiredThe handle for the GitHub user account.
[/TABLE]
The unique identifier of the team.
The handle for the GitHub user account.

[TABLE]
Name, Type, Description
rolestringThe role that this user should have in the team.Default:memberCan be one of:member,maintainer
[/TABLE]
The role that this user should have in the team.
Default:member
Can be one of:member,maintainer

### HTTP response status codes for "Add or update team membership for a user (Legacy)"

[TABLE]
Status code | Description
200 | OK
403 | Forbidden if team synchronization is set up
404 | Resource not found
422 | Unprocessable Entity if you attempt to add an organization to a team
[/TABLE]
OK
Forbidden if team synchronization is set up
Resource not found
Unprocessable Entity if you attempt to add an organization to a team

### Code samples for "Add or update team membership for a user (Legacy)"

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
  https://api.github.com/teams/TEAM_ID/memberships/USERNAME \
  -d '{"role":"member"}'
```

#### Response if user's membership with team is now pending
- Example response
- Response schema

```
Status: 200
```

```
{
  "url": "https://api.github.com/teams/1/memberships/octocat",
  "role": "member",
  "issue_state": "pending"
}
```

## Remove team membership for a user (Legacy)
Warning
Endpoint closing down notice:This endpoint route is closing down and will be removed from the Teams API. We recommend migrating your existing code to use the newRemove team membership for a userendpoint.
Team synchronization is available for organizations using GitHub Enterprise Cloud. For more information, seeGitHub's productsin the GitHub Help documentation.
To remove a membership between a user and a team, the authenticated user must have 'admin' permissions to the team or be an owner of the organization that the team is associated with. Removing team membership does not delete the user, it just removes their membership from the team.
Note
When you have team synchronization set up for a team with your organization's identity provider (IdP), you will see an error if you attempt to use the API for making changes to the team's membership. If you have access to manage group membership in your IdP, you can manage GitHub team membership through your identity provider, which automatically adds and removes team members in an organization. For more information, see "Synchronizing teams between your identity provider and GitHub."

### Fine-grained access tokens for "Remove team membership for a user (Legacy)"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Members" organization permissions (write)

### Parameters for "Remove team membership for a user (Legacy)"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
team_idintegerRequiredThe unique identifier of the team.
usernamestringRequiredThe handle for the GitHub user account.
[/TABLE]
The unique identifier of the team.
The handle for the GitHub user account.

### HTTP response status codes for "Remove team membership for a user (Legacy)"

[TABLE]
Status code | Description
204 | No Content
403 | if team synchronization is set up
[/TABLE]
No Content
if team synchronization is set up

### Code samples for "Remove team membership for a user (Legacy)"

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
  https://api.github.com/teams/TEAM_ID/memberships/USERNAME
```

#### Response

```
Status: 204
```