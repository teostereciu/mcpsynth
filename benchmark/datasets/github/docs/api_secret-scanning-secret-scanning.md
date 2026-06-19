# REST API endpoints for secret scanning

*Source: https://docs.github.com/en/rest/secret-scanning/secret-scanning*

---

# REST API endpoints for secret scanning
Use the REST API to retrieve and update secret alerts from a repository.

## About secret scanning
You can use the API to:
- Enable or disable secret scanning and push protection for a repository. For more information, seeREST API endpoints for repositoriesand expand the "Properties of thesecurity_and_analysisobject" section.
- Retrieve and update secret scanning alerts from a repository. For further details, see the sections below.
For more information about secret scanning, seeAbout secret scanning.

## List secret scanning alerts for an organization
Lists secret scanning alerts for eligible repositories in an organization, from newest to oldest.
The authenticated user must be an administrator or security manager for the organization to use this endpoint.
OAuth app tokens and personal access tokens (classic) need therepoorsecurity_eventsscope to use this endpoint. If this endpoint is only used with public repositories, the token can use thepublic_reposcope instead.

### Fine-grained access tokens for "List secret scanning alerts for an organization"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Secret scanning alerts" repository permissions (read)

### Parameters for "List secret scanning alerts for an organization"

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
statestringSet toopenorresolvedto only list secret scanning alerts in a specific state.Can be one of:open,resolved
secret_typestringA comma-separated list of secret types to return. All default secret patterns are returned. To return generic patterns, pass the token name(s) in the parameter. See "Supported secret scanning patterns" for a complete list of secret types.
resolutionstringA comma-separated list of resolutions. Only secret scanning alerts with one of these resolutions are listed. Valid resolutions arefalse_positive,wont_fix,revoked,pattern_edited,pattern_deletedorused_in_tests.
assigneestringFilters alerts by assignee. Use*to get all assigned alerts,noneto get all unassigned alerts, or a GitHub username to get alerts assigned to a specific user.
sortstringThe property to sort the results by.createdmeans when the alert was created.updatedmeans when the alert was updated or resolved.Default:createdCan be one of:created,updated
directionstringThe direction to sort the results by.Default:descCan be one of:asc,desc
pageintegerThe page number of the results to fetch. For more information, see "Using pagination in the REST API."Default:1
per_pageintegerThe number of results per page (max 100). For more information, see "Using pagination in the REST API."Default:30
beforestringA cursor, as given in theLink header. If specified, the query only searches for events before this cursor. To receive an initial cursor on your first request, include an empty "before" query string.
afterstringA cursor, as given in theLink header. If specified, the query only searches for events after this cursor.  To receive an initial cursor on your first request, include an empty "after" query string.
validitystringA comma-separated list of validities that, when present, will return alerts that match the validities in this list. Valid options areactive,inactive, andunknown.
is_publicly_leakedbooleanA boolean value representing whether or not to filter alerts by the publicly-leaked tag being present.Default:false
is_multi_repobooleanA boolean value representing whether or not to filter alerts by the multi-repo tag being present.Default:false
hide_secretbooleanA boolean value representing whether or not to hide literal secrets in the results.Default:false
[/TABLE]
Set toopenorresolvedto only list secret scanning alerts in a specific state.
Can be one of:open,resolved

```
secret_type
```
A comma-separated list of secret types to return. All default secret patterns are returned. To return generic patterns, pass the token name(s) in the parameter. See "Supported secret scanning patterns" for a complete list of secret types.
A comma-separated list of resolutions. Only secret scanning alerts with one of these resolutions are listed. Valid resolutions arefalse_positive,wont_fix,revoked,pattern_edited,pattern_deletedorused_in_tests.
Filters alerts by assignee. Use*to get all assigned alerts,noneto get all unassigned alerts, or a GitHub username to get alerts assigned to a specific user.
The property to sort the results by.createdmeans when the alert was created.updatedmeans when the alert was updated or resolved.
Default:created
Can be one of:created,updated
The direction to sort the results by.
Default:desc
Can be one of:asc,desc
The page number of the results to fetch. For more information, see "Using pagination in the REST API."
Default:1
The number of results per page (max 100). For more information, see "Using pagination in the REST API."
Default:30
A cursor, as given in theLink header. If specified, the query only searches for events before this cursor. To receive an initial cursor on your first request, include an empty "before" query string.
A cursor, as given in theLink header. If specified, the query only searches for events after this cursor.  To receive an initial cursor on your first request, include an empty "after" query string.
A comma-separated list of validities that, when present, will return alerts that match the validities in this list. Valid options areactive,inactive, andunknown.

```
is_publicly_leaked
```
A boolean value representing whether or not to filter alerts by the publicly-leaked tag being present.
Default:false

```
is_multi_repo
```
A boolean value representing whether or not to filter alerts by the multi-repo tag being present.
Default:false

```
hide_secret
```
A boolean value representing whether or not to hide literal secrets in the results.
Default:false

### HTTP response status codes for "List secret scanning alerts for an organization"

[TABLE]
Status code | Description
200 | OK
404 | Resource not found
503 | Service unavailable
[/TABLE]
OK
Resource not found
Service unavailable

### Code samples for "List secret scanning alerts for an organization"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/orgs/ORG/secret-scanning/alerts
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
    "number": 2,
    "created_at": "2020-11-06T18:48:51Z",
    "url": "https://api.github.com/repos/owner/private-repo/secret-scanning/alerts/2",
    "html_url": "https://github.com/owner/private-repo/security/secret-scanning/2",
    "locations_url": "https://api.github.com/repos/owner/private-repo/secret-scanning/alerts/2/locations",
    "state": "resolved",
    "resolution": "false_positive",
    "resolved_at": "2020-11-07T02:47:13Z",
    "resolved_by": {
      "login": "monalisa",
      "id": 2,
      "node_id": "MDQ6VXNlcjI=",
      "avatar_url": "https://alambic.github.com/avatars/u/2?",
      "gravatar_id": "",
      "url": "https://api.github.com/users/monalisa",
      "html_url": "https://github.com/monalisa",
      "followers_url": "https://api.github.com/users/monalisa/followers",
      "following_url": "https://api.github.com/users/monalisa/following{/other_user}",
      "gists_url": "https://api.github.com/users/monalisa/gists{/gist_id}",
      "starred_url": "https://api.github.com/users/monalisa/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/monalisa/subscriptions",
      "organizations_url": "https://api.github.com/users/monalisa/orgs",
      "repos_url": "https://api.github.com/users/monalisa/repos",
      "events_url": "https://api.github.com/users/monalisa/events{/privacy}",
      "received_events_url": "https://api.github.com/users/monalisa/received_events",
      "type": "User",
      "site_admin": true
    },
    "secret_type": "adafruit_io_key",
    "secret_type_display_name": "Adafruit IO Key",
    "secret": "aio_XXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "repository": {
      "id": 1296269,
      "node_id": "MDEwOlJlcG9zaXRvcnkxMjk2MjY5",
      "name": "Hello-World",
      "full_name": "octocat/Hello-World",
      "owner": {
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
      },
      "private": false,
      "html_url": "https://github.com/octocat/Hello-World",
      "description": "This your first repo!",
      "fork": false,
      "url": "https://api.github.com/repos/octocat/Hello-World",
      "archive_url": "https://api.github.com/repos/octocat/Hello-World/{archive_format}{/ref}",
      "assignees_url": "https://api.github.com/repos/octocat/Hello-World/assignees{/user}",
      "blobs_url": "https://api.github.com/repos/octocat/Hello-World/git/blobs{/sha}",
      "branches_url": "https://api.github.com/repos/octocat/Hello-World/branches{/branch}",
      "collaborators_url": "https://api.github.com/repos/octocat/Hello-World/collaborators{/collaborator}",
      "comments_url": "https://api.github.com/repos/octocat/Hello-World/comments{/number}",
      "commits_url": "https://api.github.com/repos/octocat/Hello-World/commits{/sha}",
      "compare_url": "https://api.github.com/repos/octocat/Hello-World/compare/{base}...{head}",
      "contents_url": "https://api.github.com/repos/octocat/Hello-World/contents/{+path}",
      "contributors_url": "https://api.github.com/repos/octocat/Hello-World/contributors",
      "deployments_url": "https://api.github.com/repos/octocat/Hello-World/deployments",
      "downloads_url": "https://api.github.com/repos/octocat/Hello-World/downloads",
      "events_url": "https://api.github.com/repos/octocat/Hello-World/events",
      "forks_url": "https://api.github.com/repos/octocat/Hello-World/forks",
      "git_commits_url": "https://api.github.com/repos/octocat/Hello-World/git/commits{/sha}",
      "git_refs_url": "https://api.github.com/repos/octocat/Hello-World/git/refs{/sha}",
      "git_tags_url": "https://api.github.com/repos/octocat/Hello-World/git/tags{/sha}",
      "issue_comment_url": "https://api.github.com/repos/octocat/Hello-World/issues/comments{/number}",
      "issue_events_url": "https://api.github.com/repos/octocat/Hello-World/issues/events{/number}",
      "issues_url": "https://api.github.com/repos/octocat/Hello-World/issues{/number}",
      "keys_url": "https://api.github.com/repos/octocat/Hello-World/keys{/key_id}",
      "labels_url": "https://api.github.com/repos/octocat/Hello-World/labels{/name}",
      "languages_url": "https://api.github.com/repos/octocat/Hello-World/languages",
      "merges_url": "https://api.github.com/repos/octocat/Hello-World/merges",
      "milestones_url": "https://api.github.com/repos/octocat/Hello-World/milestones{/number}",
      "notifications_url": "https://api.github.com/repos/octocat/Hello-World/notifications{?since,all,participating}",
      "pulls_url": "https://api.github.com/repos/octocat/Hello-World/pulls{/number}",
      "releases_url": "https://api.github.com/repos/octocat/Hello-World/releases{/id}",
      "stargazers_url": "https://api.github.com/repos/octocat/Hello-World/stargazers",
      "statuses_url": "https://api.github.com/repos/octocat/Hello-World/statuses/{sha}",
      "subscribers_url": "https://api.github.com/repos/octocat/Hello-World/subscribers",
      "subscription_url": "https://api.github.com/repos/octocat/Hello-World/subscription",
      "tags_url": "https://api.github.com/repos/octocat/Hello-World/tags",
      "teams_url": "https://api.github.com/repos/octocat/Hello-World/teams",
      "trees_url": "https://api.github.com/repos/octocat/Hello-World/git/trees{/sha}",
      "hooks_url": "https://api.github.com/repos/octocat/Hello-World/hooks"
    },
    "push_protection_bypassed_by": {
      "login": "monalisa",
      "id": 2,
      "node_id": "MDQ6VXNlcjI=",
      "avatar_url": "https://alambic.github.com/avatars/u/2?",
      "gravatar_id": "",
      "url": "https://api.github.com/users/monalisa",
      "html_url": "https://github.com/monalisa",
      "followers_url": "https://api.github.com/users/monalisa/followers",
      "following_url": "https://api.github.com/users/monalisa/following{/other_user}",
      "gists_url": "https://api.github.com/users/monalisa/gists{/gist_id}",
      "starred_url": "https://api.github.com/users/monalisa/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/monalisa/subscriptions",
      "organizations_url": "https://api.github.com/users/monalisa/orgs",
      "repos_url": "https://api.github.com/users/monalisa/repos",
      "events_url": "https://api.github.com/users/monalisa/events{/privacy}",
      "received_events_url": "https://api.github.com/users/monalisa/received_events",
      "type": "User",
      "site_admin": true
    },
    "push_protection_bypassed": true,
    "push_protection_bypassed_at": "2020-11-06T21:48:51Z",
    "push_protection_bypass_request_reviewer": {
      "login": "octocat",
      "id": 3,
      "node_id": "MDQ6VXNlcjI=",
      "avatar_url": "https://alambic.github.com/avatars/u/3?",
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
      "site_admin": true
    },
    "push_protection_bypass_request_reviewer_comment": "Example response",
    "push_protection_bypass_request_comment": "Example comment",
    "push_protection_bypass_request_html_url": "https://github.com/owner/repo/secret_scanning_exemptions/1",
    "resolution_comment": "Example comment",
    "validity": "active",
    "publicly_leaked": false,
    "multi_repo": false,
    "is_base64_encoded": false,
    "first_location_detected": {
      "path": "/example/secrets.txt",
      "start_line": 1,
      "end_line": 1,
      "start_column": 1,
      "end_column": 64,
      "blob_sha": "af5626b4a114abcb82d63db7c8082c3c4756e51b",
      "blob_url": "https://api.github.com/repos/octocat/hello-world/git/blobs/af5626b4a114abcb82d63db7c8082c3c4756e51b",
      "commit_sha": "f14d7debf9775f957cf4f1e8176da0786431f72b",
      "commit_url": "https://api.github.com/repos/octocat/hello-world/git/commits/f14d7debf9775f957cf4f1e8176da0786431f72b"
    },
    "has_more_locations": true,
    "assigned_to": {
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
  }
]
```

## List secret scanning alerts for a repository
Lists secret scanning alerts for an eligible repository, from newest to oldest.
The authenticated user must be an administrator for the repository or for the organization that owns the repository to use this endpoint.
OAuth app tokens and personal access tokens (classic) need therepoorsecurity_eventsscope to use this endpoint. If this endpoint is only used with public repositories, the token can use thepublic_reposcope instead.

### Fine-grained access tokens for "List secret scanning alerts for a repository"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Secret scanning alerts" repository permissions (read)

### Parameters for "List secret scanning alerts for a repository"

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
statestringSet toopenorresolvedto only list secret scanning alerts in a specific state.Can be one of:open,resolved
secret_typestringA comma-separated list of secret types to return. All default secret patterns are returned. To return generic patterns, pass the token name(s) in the parameter. See "Supported secret scanning patterns" for a complete list of secret types.
resolutionstringA comma-separated list of resolutions. Only secret scanning alerts with one of these resolutions are listed. Valid resolutions arefalse_positive,wont_fix,revoked,pattern_edited,pattern_deletedorused_in_tests.
assigneestringFilters alerts by assignee. Use*to get all assigned alerts,noneto get all unassigned alerts, or a GitHub username to get alerts assigned to a specific user.
sortstringThe property to sort the results by.createdmeans when the alert was created.updatedmeans when the alert was updated or resolved.Default:createdCan be one of:created,updated
directionstringThe direction to sort the results by.Default:descCan be one of:asc,desc
pageintegerThe page number of the results to fetch. For more information, see "Using pagination in the REST API."Default:1
per_pageintegerThe number of results per page (max 100). For more information, see "Using pagination in the REST API."Default:30
beforestringA cursor, as given in theLink header. If specified, the query only searches for events before this cursor. To receive an initial cursor on your first request, include an empty "before" query string.
afterstringA cursor, as given in theLink header. If specified, the query only searches for events after this cursor.  To receive an initial cursor on your first request, include an empty "after" query string.
validitystringA comma-separated list of validities that, when present, will return alerts that match the validities in this list. Valid options areactive,inactive, andunknown.
is_publicly_leakedbooleanA boolean value representing whether or not to filter alerts by the publicly-leaked tag being present.Default:false
is_multi_repobooleanA boolean value representing whether or not to filter alerts by the multi-repo tag being present.Default:false
hide_secretbooleanA boolean value representing whether or not to hide literal secrets in the results.Default:false
[/TABLE]
Set toopenorresolvedto only list secret scanning alerts in a specific state.
Can be one of:open,resolved

```
secret_type
```
A comma-separated list of secret types to return. All default secret patterns are returned. To return generic patterns, pass the token name(s) in the parameter. See "Supported secret scanning patterns" for a complete list of secret types.
A comma-separated list of resolutions. Only secret scanning alerts with one of these resolutions are listed. Valid resolutions arefalse_positive,wont_fix,revoked,pattern_edited,pattern_deletedorused_in_tests.
Filters alerts by assignee. Use*to get all assigned alerts,noneto get all unassigned alerts, or a GitHub username to get alerts assigned to a specific user.
The property to sort the results by.createdmeans when the alert was created.updatedmeans when the alert was updated or resolved.
Default:created
Can be one of:created,updated
The direction to sort the results by.
Default:desc
Can be one of:asc,desc
The page number of the results to fetch. For more information, see "Using pagination in the REST API."
Default:1
The number of results per page (max 100). For more information, see "Using pagination in the REST API."
Default:30
A cursor, as given in theLink header. If specified, the query only searches for events before this cursor. To receive an initial cursor on your first request, include an empty "before" query string.
A cursor, as given in theLink header. If specified, the query only searches for events after this cursor.  To receive an initial cursor on your first request, include an empty "after" query string.
A comma-separated list of validities that, when present, will return alerts that match the validities in this list. Valid options areactive,inactive, andunknown.

```
is_publicly_leaked
```
A boolean value representing whether or not to filter alerts by the publicly-leaked tag being present.
Default:false

```
is_multi_repo
```
A boolean value representing whether or not to filter alerts by the multi-repo tag being present.
Default:false

```
hide_secret
```
A boolean value representing whether or not to hide literal secrets in the results.
Default:false

### HTTP response status codes for "List secret scanning alerts for a repository"

[TABLE]
Status code | Description
200 | OK
404 | Repository is public or secret scanning is disabled for the repository
503 | Service unavailable
[/TABLE]
OK
Repository is public or secret scanning is disabled for the repository
Service unavailable

### Code samples for "List secret scanning alerts for a repository"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/secret-scanning/alerts
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
    "number": 2,
    "created_at": "2020-11-06T18:48:51Z",
    "url": "https://api.github.com/repos/owner/private-repo/secret-scanning/alerts/2",
    "html_url": "https://github.com/owner/private-repo/security/secret-scanning/2",
    "locations_url": "https://api.github.com/repos/owner/private-repo/secret-scanning/alerts/2/locations",
    "state": "resolved",
    "resolution": "false_positive",
    "resolved_at": "2020-11-07T02:47:13Z",
    "resolved_by": {
      "login": "monalisa",
      "id": 2,
      "node_id": "MDQ6VXNlcjI=",
      "avatar_url": "https://alambic.github.com/avatars/u/2?",
      "gravatar_id": "",
      "url": "https://api.github.com/users/monalisa",
      "html_url": "https://github.com/monalisa",
      "followers_url": "https://api.github.com/users/monalisa/followers",
      "following_url": "https://api.github.com/users/monalisa/following{/other_user}",
      "gists_url": "https://api.github.com/users/monalisa/gists{/gist_id}",
      "starred_url": "https://api.github.com/users/monalisa/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/monalisa/subscriptions",
      "organizations_url": "https://api.github.com/users/monalisa/orgs",
      "repos_url": "https://api.github.com/users/monalisa/repos",
      "events_url": "https://api.github.com/users/monalisa/events{/privacy}",
      "received_events_url": "https://api.github.com/users/monalisa/received_events",
      "type": "User",
      "site_admin": true
    },
    "secret_type": "adafruit_io_key",
    "secret_type_display_name": "Adafruit IO Key",
    "secret": "aio_XXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "push_protection_bypassed_by": {
      "login": "monalisa",
      "id": 2,
      "node_id": "MDQ6VXNlcjI=",
      "avatar_url": "https://alambic.github.com/avatars/u/2?",
      "gravatar_id": "",
      "url": "https://api.github.com/users/monalisa",
      "html_url": "https://github.com/monalisa",
      "followers_url": "https://api.github.com/users/monalisa/followers",
      "following_url": "https://api.github.com/users/monalisa/following{/other_user}",
      "gists_url": "https://api.github.com/users/monalisa/gists{/gist_id}",
      "starred_url": "https://api.github.com/users/monalisa/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/monalisa/subscriptions",
      "organizations_url": "https://api.github.com/users/monalisa/orgs",
      "repos_url": "https://api.github.com/users/monalisa/repos",
      "events_url": "https://api.github.com/users/monalisa/events{/privacy}",
      "received_events_url": "https://api.github.com/users/monalisa/received_events",
      "type": "User",
      "site_admin": true
    },
    "push_protection_bypassed": true,
    "push_protection_bypassed_at": "2020-11-06T21:48:51Z",
    "push_protection_bypass_request_reviewer": {
      "login": "octocat",
      "id": 3,
      "node_id": "MDQ6VXNlcjI=",
      "avatar_url": "https://alambic.github.com/avatars/u/3?",
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
      "site_admin": true
    },
    "push_protection_bypass_request_reviewer_comment": "Example response",
    "push_protection_bypass_request_comment": "Example comment",
    "push_protection_bypass_request_html_url": "https://github.com/owner/repo/secret_scanning_exemptions/1",
    "resolution_comment": "Example comment",
    "validity": "inactive",
    "publicly_leaked": false,
    "multi_repo": false,
    "is_base64_encoded": false,
    "first_location_detected": {
      "path": "/example/secrets.txt",
      "start_line": 1,
      "end_line": 1,
      "start_column": 1,
      "end_column": 64,
      "blob_sha": "af5626b4a114abcb82d63db7c8082c3c4756e51b",
      "blob_url": "https://api.github.com/repos/octocat/hello-world/git/blobs/af5626b4a114abcb82d63db7c8082c3c4756e51b",
      "commit_sha": "f14d7debf9775f957cf4f1e8176da0786431f72b",
      "commit_url": "https://api.github.com/repos/octocat/hello-world/git/commits/f14d7debf9775f957cf4f1e8176da0786431f72b"
    },
    "has_more_locations": true,
    "assigned_to": {
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
  }
]
```

## Get a secret scanning alert
Gets a single secret scanning alert detected in an eligible repository.
The authenticated user must be an administrator for the repository or for the organization that owns the repository to use this endpoint.
OAuth app tokens and personal access tokens (classic) need therepoorsecurity_eventsscope to use this endpoint. If this endpoint is only used with public repositories, the token can use thepublic_reposcope instead.

### Fine-grained access tokens for "Get a secret scanning alert"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Secret scanning alerts" repository permissions (read)

### Parameters for "Get a secret scanning alert"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
alert_numberintegerRequiredThe number that identifies an alert. You can find this at the end of the URL for a code scanning alert within GitHub, and in thenumberfield in the response from theGET /repos/{owner}/{repo}/code-scanning/alertsoperation.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.

```
alert_number
```
The number that identifies an alert. You can find this at the end of the URL for a code scanning alert within GitHub, and in thenumberfield in the response from theGET /repos/{owner}/{repo}/code-scanning/alertsoperation.

[TABLE]
Name, Type, Description
hide_secretbooleanA boolean value representing whether or not to hide literal secrets in the results.Default:false
[/TABLE]

```
hide_secret
```
A boolean value representing whether or not to hide literal secrets in the results.
Default:false

### HTTP response status codes for "Get a secret scanning alert"

[TABLE]
Status code | Description
200 | OK
304 | Not modified
404 | Repository is public, or secret scanning is disabled for the repository, or the resource is not found
503 | Service unavailable
[/TABLE]
OK
Not modified
Repository is public, or secret scanning is disabled for the repository, or the resource is not found
Service unavailable

### Code samples for "Get a secret scanning alert"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/secret-scanning/alerts/ALERT_NUMBER
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "number": 42,
  "created_at": "2020-11-06T18:18:30Z",
  "url": "https://api.github.com/repos/owner/private-repo/secret-scanning/alerts/42",
  "html_url": "https://github.com/owner/private-repo/security/secret-scanning/42",
  "locations_url": "https://api.github.com/repos/owner/private-repo/secret-scanning/alerts/42/locations",
  "state": "open",
  "resolution": null,
  "resolved_at": null,
  "resolved_by": null,
  "secret_type": "mailchimp_api_key",
  "secret_type_display_name": "Mailchimp API Key",
  "secret": "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-us2",
  "push_protection_bypassed_by": null,
  "push_protection_bypassed": false,
  "push_protection_bypassed_at": null,
  "push_protection_bypass_request_reviewer": null,
  "push_protection_bypass_request_reviewer_comment": null,
  "push_protection_bypass_request_comment": null,
  "push_protection_bypass_request_html_url": null,
  "resolution_comment": null,
  "validity": "unknown",
  "publicly_leaked": false,
  "multi_repo": false
}
```

## Update a secret scanning alert
Updates the status of a secret scanning alert in an eligible repository.
You can also use this endpoint to assign or unassign an alert to a user who has write access to the repository.
The authenticated user must be an administrator for the repository or for the organization that owns the repository to use this endpoint.
OAuth app tokens and personal access tokens (classic) need therepoorsecurity_eventsscope to use this endpoint. If this endpoint is only used with public repositories, the token can use thepublic_reposcope instead.

### Fine-grained access tokens for "Update a secret scanning alert"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Secret scanning alerts" repository permissions (write)

### Parameters for "Update a secret scanning alert"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
alert_numberintegerRequiredThe number that identifies an alert. You can find this at the end of the URL for a code scanning alert within GitHub, and in thenumberfield in the response from theGET /repos/{owner}/{repo}/code-scanning/alertsoperation.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.

```
alert_number
```
The number that identifies an alert. You can find this at the end of the URL for a code scanning alert within GitHub, and in thenumberfield in the response from theGET /repos/{owner}/{repo}/code-scanning/alertsoperation.

[TABLE]
Name, Type, Description
statestringSets the state of the secret scanning alert. You must provideresolutionwhen you set the state toresolved.Can be one of:open,resolved
resolutionstring or nullRequired when thestateisresolved.The reason for resolving the alert.Can be one of:false_positive,wont_fix,revoked,used_in_tests,null
resolution_commentstring or nullAn optional comment when closing or reopening an alert. Cannot be updated or deleted.
assigneestring or nullThe username of the user to assign to the alert. Set tonullto unassign the alert.
[/TABLE]
Sets the state of the secret scanning alert. You must provideresolutionwhen you set the state toresolved.
Can be one of:open,resolved
Required when thestateisresolved.The reason for resolving the alert.
Can be one of:false_positive,wont_fix,revoked,used_in_tests,null

```
false_positive
```

```
used_in_tests
```

```
resolution_comment
```
An optional comment when closing or reopening an alert. Cannot be updated or deleted.
The username of the user to assign to the alert. Set tonullto unassign the alert.

### HTTP response status codes for "Update a secret scanning alert"

[TABLE]
Status code | Description
200 | OK
400 | Bad request, resolution comment is invalid or the resolution was not changed.
404 | Repository is public, or secret scanning is disabled for the repository, or the resource is not found
422 | State does not match the resolution or resolution comment, or assignee does not have write access to the repository
503 | Service unavailable
[/TABLE]
OK
Bad request, resolution comment is invalid or the resolution was not changed.
Repository is public, or secret scanning is disabled for the repository, or the resource is not found
State does not match the resolution or resolution comment, or assignee does not have write access to the repository
Service unavailable

### Code samples for "Update a secret scanning alert"

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
  https://api.github.com/repos/OWNER/REPO/secret-scanning/alerts/ALERT_NUMBER \
  -d '{"state":"resolved","resolution":"false_positive"}'
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "number": 42,
  "created_at": "2020-11-06T18:18:30Z",
  "url": "https://api.github.com/repos/owner/private-repo/secret-scanning/alerts/42",
  "html_url": "https://github.com/owner/private-repo/security/secret-scanning/42",
  "locations_url": "https://api.github.com/repos/owner/private-repo/secret-scanning/alerts/42/locations",
  "state": "resolved",
  "resolution": "used_in_tests",
  "resolved_at": "2020-11-16T22:42:07Z",
  "resolved_by": {
    "login": "monalisa",
    "id": 2,
    "node_id": "MDQ6VXNlcjI=",
    "avatar_url": "https://alambic.github.com/avatars/u/2?",
    "gravatar_id": "",
    "url": "https://api.github.com/users/monalisa",
    "html_url": "https://github.com/monalisa",
    "followers_url": "https://api.github.com/users/monalisa/followers",
    "following_url": "https://api.github.com/users/monalisa/following{/other_user}",
    "gists_url": "https://api.github.com/users/monalisa/gists{/gist_id}",
    "starred_url": "https://api.github.com/users/monalisa/starred{/owner}{/repo}",
    "subscriptions_url": "https://api.github.com/users/monalisa/subscriptions",
    "organizations_url": "https://api.github.com/users/monalisa/orgs",
    "repos_url": "https://api.github.com/users/monalisa/repos",
    "events_url": "https://api.github.com/users/monalisa/events{/privacy}",
    "received_events_url": "https://api.github.com/users/monalisa/received_events",
    "type": "User",
    "site_admin": true
  },
  "secret_type": "mailchimp_api_key",
  "secret_type_display_name": "Mailchimp API Key",
  "secret": "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-us2",
  "push_protection_bypassed": false,
  "push_protection_bypassed_by": null,
  "push_protection_bypassed_at": null,
  "push_protection_bypass_request_reviewer": null,
  "push_protection_bypass_request_reviewer_comment": null,
  "push_protection_bypass_request_comment": null,
  "push_protection_bypass_request_html_url": null,
  "resolution_comment": "Example comment",
  "validity": "unknown",
  "publicly_leaked": false,
  "multi_repo": false,
  "assigned_to": {
    "login": "octocat",
    "id": 1,
    "node_id": "MDQ6VXNlcjE=",
    "avatar_url": "https://alambic.github.com/avatars/u/1?",
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
}
```

## List locations for a secret scanning alert
Lists all locations for a given secret scanning alert for an eligible repository.
The authenticated user must be an administrator for the repository or for the organization that owns the repository to use this endpoint.
OAuth app tokens and personal access tokens (classic) need therepoorsecurity_eventsscope to use this endpoint. If this endpoint is only used with public repositories, the token can use thepublic_reposcope instead.

### Fine-grained access tokens for "List locations for a secret scanning alert"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Secret scanning alerts" repository permissions (read)

### Parameters for "List locations for a secret scanning alert"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
alert_numberintegerRequiredThe number that identifies an alert. You can find this at the end of the URL for a code scanning alert within GitHub, and in thenumberfield in the response from theGET /repos/{owner}/{repo}/code-scanning/alertsoperation.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.

```
alert_number
```
The number that identifies an alert. You can find this at the end of the URL for a code scanning alert within GitHub, and in thenumberfield in the response from theGET /repos/{owner}/{repo}/code-scanning/alertsoperation.

[TABLE]
Name, Type, Description
pageintegerThe page number of the results to fetch. For more information, see "Using pagination in the REST API."Default:1
per_pageintegerThe number of results per page (max 100). For more information, see "Using pagination in the REST API."Default:30
[/TABLE]
The page number of the results to fetch. For more information, see "Using pagination in the REST API."
Default:1
The number of results per page (max 100). For more information, see "Using pagination in the REST API."
Default:30

### HTTP response status codes for "List locations for a secret scanning alert"

[TABLE]
Status code | Description
200 | OK
404 | Repository is public, or secret scanning is disabled for the repository, or the resource is not found
503 | Service unavailable
[/TABLE]
OK
Repository is public, or secret scanning is disabled for the repository, or the resource is not found
Service unavailable

### Code samples for "List locations for a secret scanning alert"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/secret-scanning/alerts/ALERT_NUMBER/locations
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
    "type": "commit",
    "details": {
      "path": "/example/secrets.txt",
      "start_line": 1,
      "end_line": 1,
      "start_column": 1,
      "end_column": 64,
      "blob_sha": "af5626b4a114abcb82d63db7c8082c3c4756e51b",
      "blob_url": "https://api.github.com/repos/octocat/hello-world/git/blobs/af5626b4a114abcb82d63db7c8082c3c4756e51b",
      "commit_sha": "f14d7debf9775f957cf4f1e8176da0786431f72b",
      "commit_url": "https://api.github.com/repos/octocat/hello-world/git/commits/f14d7debf9775f957cf4f1e8176da0786431f72b"
    }
  },
  {
    "type": "wiki_commit",
    "details": {
      "path": "/example/Home.md",
      "start_line": 1,
      "end_line": 1,
      "start_column": 1,
      "end_column": 64,
      "blob_sha": "af5626b4a114abcb82d63db7c8082c3c4756e51b",
      "page_url": "https://github.com/octocat/Hello-World/wiki/Home/302c0b7e200761c9dd9b57e57db540ee0b4293a5",
      "commit_sha": "302c0b7e200761c9dd9b57e57db540ee0b4293a5",
      "commit_url": "https://github.com/octocat/Hello-World/wiki/_compare/302c0b7e200761c9dd9b57e57db540ee0b4293a5"
    }
  },
  {
    "type": "issue_title",
    "details": {
      "issue_title_url": "https://api.github.com/repos/octocat/Hello-World/issues/1347"
    }
  },
  {
    "type": "issue_body",
    "details": {
      "issue_body_url": "https://api.github.com/repos/octocat/Hello-World/issues/1347"
    }
  },
  {
    "type": "issue_comment",
    "details": {
      "issue_comment_url": "https://api.github.com/repos/octocat/Hello-World/issues/comments/1081119451"
    }
  },
  {
    "type": "discussion_title",
    "details": {
      "discussion_title_url": "https://github.com/community/community/discussions/39082"
    }
  },
  {
    "type": "discussion_body",
    "details": {
      "discussion_body_url": "https://github.com/community/community/discussions/39082#discussion-4566270"
    }
  },
  {
    "type": "discussion_comment",
    "details": {
      "discussion_comment_url": "https://github.com/community/community/discussions/39082#discussioncomment-4158232"
    }
  },
  {
    "type": "pull_request_title",
    "details": {
      "pull_request_title_url": "https://api.github.com/repos/octocat/Hello-World/pulls/2846"
    }
  },
  {
    "type": "pull_request_body",
    "details": {
      "pull_request_body_url": "https://api.github.com/repos/octocat/Hello-World/pulls/2846"
    }
  },
  {
    "type": "pull_request_comment",
    "details": {
      "pull_request_comment_url": "https://api.github.com/repos/octocat/Hello-World/issues/comments/1825855898"
    }
  },
  {
    "type": "pull_request_review",
    "details": {
      "pull_request_review_url": "https://api.github.com/repos/octocat/Hello-World/pulls/2846/reviews/80"
    }
  },
  {
    "type": "pull_request_review_comment",
    "details": {
      "pull_request_review_comment_url": "https://api.github.com/repos/octocat/Hello-World/pulls/comments/12"
    }
  }
]
```

## Create a push protection bypass
Creates a bypass for a previously push protected secret.
The authenticated user must be the original author of the committed secret.
OAuth app tokens and personal access tokens (classic) need thereposcope to use this endpoint.

### Fine-grained access tokens for "Create a push protection bypass"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Contents" repository permissions (write)

### Parameters for "Create a push protection bypass"

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
reasonstringRequiredThe reason for bypassing push protection.Can be one of:false_positive,used_in_tests,will_fix_later
placeholder_idstringRequiredThe ID of the push protection bypass placeholder. This value is returned on any push protected routes.
[/TABLE]
The reason for bypassing push protection.
Can be one of:false_positive,used_in_tests,will_fix_later

```
false_positive
```

```
used_in_tests
```

```
will_fix_later
```

```
placeholder_id
```
The ID of the push protection bypass placeholder. This value is returned on any push protected routes.

### HTTP response status codes for "Create a push protection bypass"

[TABLE]
Status code | Description
200 | OK
403 | User does not have enough permissions to perform this action.
404 | Placeholder ID not found, or push protection is disabled on this repository.
422 | Bad request, input data missing or incorrect.
503 | Service unavailable
[/TABLE]
OK
User does not have enough permissions to perform this action.
Placeholder ID not found, or push protection is disabled on this repository.
Bad request, input data missing or incorrect.
Service unavailable

### Code samples for "Create a push protection bypass"

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
  https://api.github.com/repos/OWNER/REPO/secret-scanning/push-protection-bypasses \
  -d '{"reason":"will_fix_later","placeholder_id":"2k4dM4tseyC5lPIsjl5emX9sPNk"}'
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "reason": "will_fix_later",
  "expire_at": "2020-11-06T18:18:30Z",
  "token_type": "mailchimp_api_key"
}
```

## Get secret scanning scan history for a repository
Lists the latest default incremental and backfill scans by type for a repository. Scans from Copilot Secret Scanning are not included.
Note
This endpoint requiresGitHub Advanced Security."
OAuth app tokens and personal access tokens (classic) need therepoorsecurity_eventsscope to use this endpoint. If this endpoint is only used with public repositories, the token can use thepublic_reposcope instead.

### Fine-grained access tokens for "Get secret scanning scan history for a repository"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Secret scanning alerts" repository permissions (read)

### Parameters for "Get secret scanning scan history for a repository"

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

### HTTP response status codes for "Get secret scanning scan history for a repository"

[TABLE]
Status code | Description
200 | OK
404 | Repository does not have GitHub Advanced Security or secret scanning enabled
503 | Service unavailable
[/TABLE]
OK
Repository does not have GitHub Advanced Security or secret scanning enabled
Service unavailable

### Code samples for "Get secret scanning scan history for a repository"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/secret-scanning/scan-history
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "incremental_scans": [
    {
      "type": "git",
      "status": "completed",
      "completed_at": "2024-10-07T02:47:00Z"
    }
  ],
  "backfill_scans": [
    {
      "type": "git",
      "status": "completed",
      "started_at": "2024-10-07T02:47:00Z",
      "completed_at": "2024-10-07T02:50:00Z"
    },
    {
      "type": "issue",
      "status": "completed",
      "started_at": "2024-10-07T02:47:00Z",
      "completed_at": "2024-10-07T02:49:00Z"
    },
    {
      "type": "discussion",
      "status": "completed",
      "started_at": "2024-10-07T02:47:00Z",
      "completed_at": "2024-10-07T02:48:00Z"
    }
  ],
  "pattern_update_scans": [
    {
      "type": "discussion",
      "status": "in_progress",
      "started_at": "2024-10-07T02:47:00Z",
      "completed_at": "2024-10-07T02:51:00Z"
    }
  ],
  "custom_pattern_backfill_scans": [
    {
      "type": "git",
      "status": "completed",
      "started_at": "2024-10-07T02:47:00Z",
      "completed_at": "2024-10-07T02:55:00Z",
      "pattern_slug": "my-custom-pattern",
      "pattern_scope": "enterprise"
    },
    {
      "type": "git",
      "status": "completed",
      "started_at": "2024-10-07T02:47:00Z",
      "completed_at": "2024-10-07T02:55:00Z",
      "pattern_slug": "my-custom-pattern",
      "pattern_scope": "organization"
    }
  ]
}
```