# REST API endpoints for code scanning

*Source: https://docs.github.com/en/rest/code-scanning/code-scanning*

---

# REST API endpoints for code scanning
Use the REST API to retrieve and update code scanning alerts from a repository.

## About code scanning
You can retrieve and update code scanning alerts from a repository. You can use the endpoints to create automated reports for the code scanning alerts in an organization or upload analysis results generated using offline code scanning tools. For more information, seeScan code for vulnerabilities.

## List code scanning alerts for an organization
Lists code scanning alerts for the default branch for all eligible repositories in an organization. Eligible repositories are repositories that are owned by organizations that you own or for which you are a security manager. For more information, see "Managing security managers in your organization."
The authenticated user must be an owner or security manager for the organization to use this endpoint.
OAuth app tokens and personal access tokens (classic) need thesecurity_eventsorrepos cope to use this endpoint with private or public repositories, or thepublic_reposcope to use this endpoint with only public repositories.

### Fine-grained access tokens for "List code scanning alerts for an organization"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Code scanning alerts" repository permissions (read)

### Parameters for "List code scanning alerts for an organization"

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
tool_namestringThe name of a code scanning tool. Only results by this tool will be listed. You can specify the tool by using eithertool_nameortool_guid, but not both.
tool_guidstring or nullThe GUID of a code scanning tool. Only results by this tool will be listed. Note that some code scanning tools may not include a GUID in their analysis data. You can specify the tool by using eithertool_guidortool_name, but not both.
beforestringA cursor, as given in theLink header. If specified, the query only searches for results before this cursor. For more information, see "Using pagination in the REST API."
afterstringA cursor, as given in theLink header. If specified, the query only searches for results after this cursor. For more information, see "Using pagination in the REST API."
pageintegerThe page_number number of the results to fetch. For more information, see "Using pagination in the REST API."Default:1
per_pageintegerThe number of results per page_number (max 100). For more information, see "Using pagination in the REST API."Default:30
directionstringThe direction to sort the results by.Default:descCan be one of:asc,desc
statestringIf specified, only code scanning alerts with this issue_state will be returned.Can be one of:open,closed,dismissed,fixed
sortstringThe property by which to sort the results.Default:createdCan be one of:created,updated
severitystringIf specified, only code scanning alerts with this severity will be returned.Can be one of:critical,high,medium,low,warning,note,error
assigneesstringFilter alerts by assignees. Provide a comma-separated list of user handles (e.g.,octocatoroctocat,hubot).
Use*to list alerts with at least one assignee ornoneto list alerts with no assignees.
[/TABLE]
The name of a code scanning tool. Only results by this tool will be listed. You can specify the tool by using eithertool_nameortool_guid, but not both.
The GUID of a code scanning tool. Only results by this tool will be listed. Note that some code scanning tools may not include a GUID in their analysis data. You can specify the tool by using eithertool_guidortool_name, but not both.
A cursor, as given in theLink header. If specified, the query only searches for results before this cursor. For more information, see "Using pagination in the REST API."
A cursor, as given in theLink header. If specified, the query only searches for results after this cursor. For more information, see "Using pagination in the REST API."
The page_number number of the results to fetch. For more information, see "Using pagination in the REST API."
Default:1
The number of results per page_number (max 100). For more information, see "Using pagination in the REST API."
Default:30
The direction to sort the results by.
Default:desc
Can be one of:asc,desc
If specified, only code scanning alerts with this issue_state will be returned.
Can be one of:open,closed,dismissed,fixed
The property by which to sort the results.
Default:created
Can be one of:created,updated
If specified, only code scanning alerts with this severity will be returned.
Can be one of:critical,high,medium,low,warning,note,error
Filter alerts by assignees. Provide a comma-separated list of user handles (e.g.,octocatoroctocat,hubot).
Use*to list alerts with at least one assignee ornoneto list alerts with no assignees.

### HTTP response status codes for "List code scanning alerts for an organization"

[TABLE]
Status code | Description
200 | OK
404 | Resource not found
503 | Service unavailable
[/TABLE]
OK
Resource not found
Service unavailable

### Code samples for "List code scanning alerts for an organization"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/orgs/ORG/code-scanning/alerts
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
    "number": 4,
    "created_at": "2020-02-13T12:29:18Z",
    "url": "https://api.github.com/repos/octocat/hello-world/code-scanning/alerts/4",
    "html_url": "https://github.com/octocat/hello-world/code-scanning/4",
    "issue_state": "open",
    "dismissed_by": null,
    "dismissed_at": null,
    "dismissed_reason": null,
    "dismissed_comment": null,
    "rule": {
      "id": "js/zipslip",
      "severity": "error",
      "tags": [
        "security",
        "external/cwe/cwe-022"
      ],
      "description": "Arbitrary file write during zip extraction",
      "name": "js/zipslip"
    },
    "tool": {
      "name": "CodeQL",
      "guid": null,
      "version": "2.4.0"
    },
    "most_recent_instance": {
      "ref": "refs/heads/main",
      "analysis_key": ".github/workflows/codeql-analysis.yml:CodeQL-Build",
      "category": ".github/workflows/codeql-analysis.yml:CodeQL-Build",
      "environment": "{}",
      "issue_state": "open",
      "commit_sha": "39406e42cb832f683daa691dd652a8dc36ee8930",
      "message": {
        "text": "This path depends on a user-provided value."
      },
      "location": {
        "path": "spec-main/api-session-spec.ts",
        "start_line": 917,
        "end_line": 917,
        "start_column": 7,
        "end_column": 18
      },
      "classifications": [
        "test"
      ]
    },
    "instances_url": "https://api.github.com/repos/octocat/hello-world/code-scanning/alerts/4/instances",
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
      "blobs_url": "https://api.github.com/repos/octocat/Hello-World/git/blobs{/commit_sha}",
      "branches_url": "https://api.github.com/repos/octocat/Hello-World/branches{/branch}",
      "collaborators_url": "https://api.github.com/repos/octocat/Hello-World/collaborators{/collaborator}",
      "comments_url": "https://api.github.com/repos/octocat/Hello-World/comments{/number}",
      "commits_url": "https://api.github.com/repos/octocat/Hello-World/commits{/commit_sha}",
      "compare_url": "https://api.github.com/repos/octocat/Hello-World/compare/{base}...{head}",
      "contents_url": "https://api.github.com/repos/octocat/Hello-World/contents/{+path}",
      "contributors_url": "https://api.github.com/repos/octocat/Hello-World/contributors",
      "deployments_url": "https://api.github.com/repos/octocat/Hello-World/deployments",
      "downloads_url": "https://api.github.com/repos/octocat/Hello-World/downloads",
      "events_url": "https://api.github.com/repos/octocat/Hello-World/events",
      "forks_url": "https://api.github.com/repos/octocat/Hello-World/forks",
      "git_commits_url": "https://api.github.com/repos/octocat/Hello-World/git/commits{/commit_sha}",
      "git_refs_url": "https://api.github.com/repos/octocat/Hello-World/git/refs{/commit_sha}",
      "git_tags_url": "https://api.github.com/repos/octocat/Hello-World/git/tags{/commit_sha}",
      "issue_comment_url": "https://api.github.com/repos/octocat/Hello-World/issues/comments{/number}",
      "issue_events_url": "https://api.github.com/repos/octocat/Hello-World/issues/events{/number}",
      "issues_url": "https://api.github.com/repos/octocat/Hello-World/issues{/number}",
      "keys_url": "https://api.github.com/repos/octocat/Hello-World/keys{/key_id}",
      "labels_url": "https://api.github.com/repos/octocat/Hello-World/label_filters{/name}",
      "languages_url": "https://api.github.com/repos/octocat/Hello-World/languages",
      "merges_url": "https://api.github.com/repos/octocat/Hello-World/merges",
      "milestones_url": "https://api.github.com/repos/octocat/Hello-World/milestones{/number}",
      "notifications_url": "https://api.github.com/repos/octocat/Hello-World/notifications{?since,all,participating}",
      "pulls_url": "https://api.github.com/repos/octocat/Hello-World/pulls{/number}",
      "releases_url": "https://api.github.com/repos/octocat/Hello-World/releases{/id}",
      "stargazers_url": "https://api.github.com/repos/octocat/Hello-World/stargazers",
      "statuses_url": "https://api.github.com/repos/octocat/Hello-World/statuses/{commit_sha}",
      "subscribers_url": "https://api.github.com/repos/octocat/Hello-World/subscribers",
      "subscription_url": "https://api.github.com/repos/octocat/Hello-World/subscription",
      "tags_url": "https://api.github.com/repos/octocat/Hello-World/tags",
      "teams_url": "https://api.github.com/repos/octocat/Hello-World/teams",
      "trees_url": "https://api.github.com/repos/octocat/Hello-World/git/trees{/commit_sha}",
      "hooks_url": "https://api.github.com/repos/octocat/Hello-World/hooks"
    }
  },
  {
    "number": 3,
    "created_at": "2020-02-13T12:29:18Z",
    "url": "https://api.github.com/repos/octocat/hello-world/code-scanning/alerts/3",
    "html_url": "https://github.com/octocat/hello-world/code-scanning/3",
    "issue_state": "dismissed",
    "dismissed_by": {
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
    "dismissed_at": "2020-02-14T12:29:18Z",
    "dismissed_reason": "false positive",
    "dismissed_comment": "This alert is not actually correct, because there's a sanitizer included in the library.",
    "rule": {
      "id": "js/zipslip",
      "severity": "error",
      "tags": [
        "security",
        "external/cwe/cwe-022"
      ],
      "description": "Arbitrary file write during zip extraction",
      "name": "js/zipslip"
    },
    "tool": {
      "name": "CodeQL",
      "guid": null,
      "version": "2.4.0"
    },
    "most_recent_instance": {
      "ref": "refs/heads/main",
      "analysis_key": ".github/workflows/codeql-analysis.yml:CodeQL-Build",
      "category": ".github/workflows/codeql-analysis.yml:CodeQL-Build",
      "environment": "{}",
      "issue_state": "open",
      "commit_sha": "39406e42cb832f683daa691dd652a8dc36ee8930",
      "message": {
        "text": "This path depends on a user-provided value."
      },
      "location": {
        "path": "lib/ab12-gen.js",
        "start_line": 917,
        "end_line": 917,
        "start_column": 7,
        "end_column": 18
      },
      "classifications": []
    },
    "instances_url": "https://api.github.com/repos/octocat/hello-world/code-scanning/alerts/3/instances",
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
      "blobs_url": "https://api.github.com/repos/octocat/Hello-World/git/blobs{/commit_sha}",
      "branches_url": "https://api.github.com/repos/octocat/Hello-World/branches{/branch}",
      "collaborators_url": "https://api.github.com/repos/octocat/Hello-World/collaborators{/collaborator}",
      "comments_url": "https://api.github.com/repos/octocat/Hello-World/comments{/number}",
      "commits_url": "https://api.github.com/repos/octocat/Hello-World/commits{/commit_sha}",
      "compare_url": "https://api.github.com/repos/octocat/Hello-World/compare/{base}...{head}",
      "contents_url": "https://api.github.com/repos/octocat/Hello-World/contents/{+path}",
      "contributors_url": "https://api.github.com/repos/octocat/Hello-World/contributors",
      "deployments_url": "https://api.github.com/repos/octocat/Hello-World/deployments",
      "downloads_url": "https://api.github.com/repos/octocat/Hello-World/downloads",
      "events_url": "https://api.github.com/repos/octocat/Hello-World/events",
      "forks_url": "https://api.github.com/repos/octocat/Hello-World/forks",
      "git_commits_url": "https://api.github.com/repos/octocat/Hello-World/git/commits{/commit_sha}",
      "git_refs_url": "https://api.github.com/repos/octocat/Hello-World/git/refs{/commit_sha}",
      "git_tags_url": "https://api.github.com/repos/octocat/Hello-World/git/tags{/commit_sha}",
      "issue_comment_url": "https://api.github.com/repos/octocat/Hello-World/issues/comments{/number}",
      "issue_events_url": "https://api.github.com/repos/octocat/Hello-World/issues/events{/number}",
      "issues_url": "https://api.github.com/repos/octocat/Hello-World/issues{/number}",
      "keys_url": "https://api.github.com/repos/octocat/Hello-World/keys{/key_id}",
      "labels_url": "https://api.github.com/repos/octocat/Hello-World/label_filters{/name}",
      "languages_url": "https://api.github.com/repos/octocat/Hello-World/languages",
      "merges_url": "https://api.github.com/repos/octocat/Hello-World/merges",
      "milestones_url": "https://api.github.com/repos/octocat/Hello-World/milestones{/number}",
      "notifications_url": "https://api.github.com/repos/octocat/Hello-World/notifications{?since,all,participating}",
      "pulls_url": "https://api.github.com/repos/octocat/Hello-World/pulls{/number}",
      "releases_url": "https://api.github.com/repos/octocat/Hello-World/releases{/id}",
      "stargazers_url": "https://api.github.com/repos/octocat/Hello-World/stargazers",
      "statuses_url": "https://api.github.com/repos/octocat/Hello-World/statuses/{commit_sha}",
      "subscribers_url": "https://api.github.com/repos/octocat/Hello-World/subscribers",
      "subscription_url": "https://api.github.com/repos/octocat/Hello-World/subscription",
      "tags_url": "https://api.github.com/repos/octocat/Hello-World/tags",
      "teams_url": "https://api.github.com/repos/octocat/Hello-World/teams",
      "trees_url": "https://api.github.com/repos/octocat/Hello-World/git/trees{/commit_sha}",
      "hooks_url": "https://api.github.com/repos/octocat/Hello-World/hooks"
    }
  }
]
```

## List code scanning alerts for a repository
Lists code scanning alerts.
The response includes amost_recent_instanceobject.
This provides details of the most recent instance of this alert
for the default branch (or for the specified Git reference if you usedrefin the request).
OAuth app tokens and personal access tokens (classic) need thesecurity_eventsscope to use this endpoint with private or public repositories, or thepublic_reposcope to use this endpoint with only public repositories.

### Fine-grained access tokens for "List code scanning alerts for a repository"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Code scanning alerts" repository permissions (read)

### Parameters for "List code scanning alerts for a repository"

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
tool_namestringThe name of a code scanning tool. Only results by this tool will be listed. You can specify the tool by using eithertool_nameortool_guid, but not both.
tool_guidstring or nullThe GUID of a code scanning tool. Only results by this tool will be listed. Note that some code scanning tools may not include a GUID in their analysis data. You can specify the tool by using eithertool_guidortool_name, but not both.
pageintegerThe page_number number of the results to fetch. For more information, see "Using pagination in the REST API."Default:1
per_pageintegerThe number of results per page_number (max 100). For more information, see "Using pagination in the REST API."Default:30
refstringThe Git reference for the results you want to list. Thereffor a branch can be formatted either asrefs/heads/<branch name>or simply<branch name>. To reference a pull request userefs/pull/<number>/merge.
printegerThe number of the pull request for the results you want to list.
directionstringThe direction to sort the results by.Default:descCan be one of:asc,desc
beforestringA cursor, as given in theLink header. If specified, the query only searches for results before this cursor. For more information, see "Using pagination in the REST API."
afterstringA cursor, as given in theLink header. If specified, the query only searches for results after this cursor. For more information, see "Using pagination in the REST API."
sortstringThe property by which to sort the results.Default:createdCan be one of:created,updated
statestringIf specified, only code scanning alerts with this issue_state will be returned.Can be one of:open,closed,dismissed,fixed
severitystringIf specified, only code scanning alerts with this severity will be returned.Can be one of:critical,high,medium,low,warning,note,error
assigneesstringFilter alerts by assignees. Provide a comma-separated list of user handles (e.g.,octocatoroctocat,hubot).
Use*to list alerts with at least one assignee ornoneto list alerts with no assignees.
[/TABLE]
The name of a code scanning tool. Only results by this tool will be listed. You can specify the tool by using eithertool_nameortool_guid, but not both.
The GUID of a code scanning tool. Only results by this tool will be listed. Note that some code scanning tools may not include a GUID in their analysis data. You can specify the tool by using eithertool_guidortool_name, but not both.
The page_number number of the results to fetch. For more information, see "Using pagination in the REST API."
Default:1
The number of results per page_number (max 100). For more information, see "Using pagination in the REST API."
Default:30
The Git reference for the results you want to list. Thereffor a branch can be formatted either asrefs/heads/<branch name>or simply<branch name>. To reference a pull request userefs/pull/<number>/merge.
The number of the pull request for the results you want to list.
The direction to sort the results by.
Default:desc
Can be one of:asc,desc
A cursor, as given in theLink header. If specified, the query only searches for results before this cursor. For more information, see "Using pagination in the REST API."
A cursor, as given in theLink header. If specified, the query only searches for results after this cursor. For more information, see "Using pagination in the REST API."
The property by which to sort the results.
Default:created
Can be one of:created,updated
If specified, only code scanning alerts with this issue_state will be returned.
Can be one of:open,closed,dismissed,fixed
If specified, only code scanning alerts with this severity will be returned.
Can be one of:critical,high,medium,low,warning,note,error
Filter alerts by assignees. Provide a comma-separated list of user handles (e.g.,octocatoroctocat,hubot).
Use*to list alerts with at least one assignee ornoneto list alerts with no assignees.

### HTTP response status codes for "List code scanning alerts for a repository"

[TABLE]
Status code | Description
200 | OK
304 | Not modified
403 | Response if GitHub Advanced Security is not enabled for this repository
404 | Resource not found
503 | Service unavailable
[/TABLE]
OK
Not modified
Response if GitHub Advanced Security is not enabled for this repository
Resource not found
Service unavailable

### Code samples for "List code scanning alerts for a repository"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/code-scanning/alerts
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
    "number": 4,
    "created_at": "2020-02-13T12:29:18Z",
    "url": "https://api.github.com/repos/octocat/hello-world/code-scanning/alerts/4",
    "html_url": "https://github.com/octocat/hello-world/code-scanning/4",
    "issue_state": "open",
    "fixed_at": null,
    "dismissed_by": null,
    "dismissed_at": null,
    "dismissed_reason": null,
    "dismissed_comment": null,
    "rule": {
      "id": "js/zipslip",
      "severity": "error",
      "tags": [
        "security",
        "external/cwe/cwe-022"
      ],
      "description": "Arbitrary file write during zip extraction",
      "name": "js/zipslip"
    },
    "tool": {
      "name": "CodeQL",
      "guid": null,
      "version": "2.4.0"
    },
    "most_recent_instance": {
      "ref": "refs/heads/main",
      "analysis_key": ".github/workflows/codeql-analysis.yml:CodeQL-Build",
      "category": ".github/workflows/codeql-analysis.yml:CodeQL-Build",
      "environment": "{}",
      "issue_state": "open",
      "commit_sha": "39406e42cb832f683daa691dd652a8dc36ee8930",
      "message": {
        "text": "This path depends on a user-provided value."
      },
      "location": {
        "path": "spec-main/api-session-spec.ts",
        "start_line": 917,
        "end_line": 917,
        "start_column": 7,
        "end_column": 18
      },
      "classifications": [
        "test"
      ]
    },
    "instances_url": "https://api.github.com/repos/octocat/hello-world/code-scanning/alerts/4/instances"
  },
  {
    "number": 3,
    "created_at": "2020-02-13T12:29:18Z",
    "url": "https://api.github.com/repos/octocat/hello-world/code-scanning/alerts/3",
    "html_url": "https://github.com/octocat/hello-world/code-scanning/3",
    "issue_state": "dismissed",
    "fixed_at": null,
    "dismissed_by": {
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
    "dismissed_at": "2020-02-14T12:29:18Z",
    "dismissed_reason": "false positive",
    "dismissed_comment": "This alert is not actually correct, because there's a sanitizer included in the library.",
    "rule": {
      "id": "js/zipslip",
      "severity": "error",
      "tags": [
        "security",
        "external/cwe/cwe-022"
      ],
      "description": "Arbitrary file write during zip extraction",
      "name": "js/zipslip"
    },
    "tool": {
      "name": "CodeQL",
      "guid": null,
      "version": "2.4.0"
    },
    "most_recent_instance": {
      "ref": "refs/heads/main",
      "analysis_key": ".github/workflows/codeql-analysis.yml:CodeQL-Build",
      "category": ".github/workflows/codeql-analysis.yml:CodeQL-Build",
      "environment": "{}",
      "issue_state": "open",
      "commit_sha": "39406e42cb832f683daa691dd652a8dc36ee8930",
      "message": {
        "text": "This path depends on a user-provided value."
      },
      "location": {
        "path": "lib/ab12-gen.js",
        "start_line": 917,
        "end_line": 917,
        "start_column": 7,
        "end_column": 18
      },
      "classifications": []
    },
    "instances_url": "https://api.github.com/repos/octocat/hello-world/code-scanning/alerts/3/instances"
  }
]
```

## Get a code scanning alert
Gets a single code scanning alert.
OAuth app tokens and personal access tokens (classic) need thesecurity_eventsscope to use this endpoint with private or public repositories, or thepublic_reposcope to use this endpoint with only public repositories.

### Fine-grained access tokens for "Get a code scanning alert"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Code scanning alerts" repository permissions (read)

### Parameters for "Get a code scanning alert"

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

### HTTP response status codes for "Get a code scanning alert"

[TABLE]
Status code | Description
200 | OK
304 | Not modified
403 | Response if GitHub Advanced Security is not enabled for this repository
404 | Resource not found
503 | Service unavailable
[/TABLE]
OK
Not modified
Response if GitHub Advanced Security is not enabled for this repository
Resource not found
Service unavailable

### Code samples for "Get a code scanning alert"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/code-scanning/alerts/ALERT_NUMBER
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
  "created_at": "2020-06-19T11:21:34Z",
  "url": "https://api.github.com/repos/octocat/hello-world/code-scanning/alerts/42",
  "html_url": "https://github.com/octocat/hello-world/code-scanning/42",
  "issue_state": "dismissed",
  "fixed_at": null,
  "dismissed_by": {
    "login": "octocat",
    "id": 54933897,
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
  "dismissed_at": "2020-02-14T12:29:18Z",
  "dismissed_reason": "false positive",
  "dismissed_comment": "This alert is not actually correct, because there's a sanitizer included in the library.",
  "rule": {
    "id": "js/zipslip",
    "severity": "error",
    "security_severity_level": "high",
    "description": "Arbitrary file write during zip extraction (\"Zip Slip\")",
    "name": "js/zipslip",
    "full_description": "Extracting files from a malicious zip archive without validating that the destination file path is within the destination directory can cause files outside the destination directory to be overwritten.",
    "tags": [
      "security",
      "external/cwe/cwe-022"
    ],
    "help": "# Arbitrary file write during zip extraction (\"Zip Slip\")\\nExtracting files from a malicious zip archive without validating that the destination file path is within the destination directory can cause files outside the destination directory to be overwritten ...",
    "help_uri": "https://codeql.github.com/"
  },
  "tool": {
    "name": "CodeQL",
    "guid": null,
    "version": "2.4.0"
  },
  "most_recent_instance": {
    "ref": "refs/heads/main",
    "analysis_key": ".github/workflows/codeql-analysis.yml:CodeQL-Build",
    "category": ".github/workflows/codeql-analysis.yml:CodeQL-Build",
    "environment": "{}",
    "issue_state": "dismissed",
    "commit_sha": "39406e42cb832f683daa691dd652a8dc36ee8930",
    "message": {
      "text": "This path depends on a user-provided value."
    },
    "location": {
      "path": "spec-main/api-session-spec.ts",
      "start_line": 917,
      "end_line": 917,
      "start_column": 7,
      "end_column": 18
    },
    "classifications": [
      "test"
    ]
  },
  "instances_url": "https://api.github.com/repos/octocat/hello-world/code-scanning/alerts/42/instances"
}
```

## Update a code scanning alert
Updates the status of a single code scanning alert.
OAuth app tokens and personal access tokens (classic) need thesecurity_eventsscope to use this endpoint with private or public repositories, or thepublic_reposcope to use this endpoint with only public repositories.

### Fine-grained access tokens for "Update a code scanning alert"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Code scanning alerts" repository permissions (write)

### Parameters for "Update a code scanning alert"

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
statestringSets the issue_state of the code scanning alert. You must providedismissed_reasonwhen you set the issue_state todismissed.Can be one of:open,dismissed
dismissed_reasonstring or nullRequired when the issue_state is dismissed.The reason for dismissing or closing the alert.Can be one of:false positive,won't fix,used in tests,null
dismissed_commentstring or nullThe dismissal comment associated with the dismissal of the alert.
create_requestbooleanIftrue, attempt to create an alert dismissal request.
assigneesarray of stringsThe list of users to assign to the code scanning alert. An empty array unassigns all previous assignees from the alert.
[/TABLE]
Sets the issue_state of the code scanning alert. You must providedismissed_reasonwhen you set the issue_state todismissed.
Can be one of:open,dismissed

```
dismissed_reason
```
Required when the issue_state is dismissed.The reason for dismissing or closing the alert.
Can be one of:false positive,won't fix,used in tests,null

```
false positive
```

```
used in tests
```

```
dismissed_comment
```
The dismissal comment associated with the dismissal of the alert.

```
create_request
```
Iftrue, attempt to create an alert dismissal request.
The list of users to assign to the code scanning alert. An empty array unassigns all previous assignees from the alert.

### HTTP response status codes for "Update a code scanning alert"

[TABLE]
Status code | Description
200 | OK
400 | Bad Request
403 | Response if the repository is archived or if GitHub Advanced Security is not enabled for this repository
404 | Resource not found
503 | Service unavailable
[/TABLE]
OK
Bad Request
Response if the repository is archived or if GitHub Advanced Security is not enabled for this repository
Resource not found
Service unavailable

### Code samples for "Update a code scanning alert"

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
  https://api.github.com/repos/OWNER/REPO/code-scanning/alerts/ALERT_NUMBER \
  -d '{"issue_state":"dismissed","dismissed_reason":"false positive","dismissed_comment":"This alert is not actually correct, because there'\''s a sanitizer included in the library.","create_request":true}'
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
  "created_at": "2020-08-25T21:28:36Z",
  "url": "https://api.github.com/repos/octocat/hello-world/code-scanning/alerts/42",
  "html_url": "https://github.com/octocat/hello-world/code-scanning/42",
  "issue_state": "dismissed",
  "fixed_at": null,
  "dismissed_by": {
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
  "dismissed_at": "2020-09-02T22:34:56Z",
  "dismissed_reason": "false positive",
  "dismissed_comment": "This alert is not actually correct, because there's a sanitizer included in the library.",
  "rule": {
    "id": "js/zipslip",
    "severity": "error",
    "security_severity_level": "high",
    "description": "Arbitrary file write during zip extraction (\"Zip Slip\")",
    "name": "js/zipslip",
    "full_description": "Extracting files from a malicious zip archive without validating that the destination file path is within the destination directory can cause files outside the destination directory to be overwritten.",
    "tags": [
      "security",
      "external/cwe/cwe-022"
    ],
    "help": "# Arbitrary file write during zip extraction (\"Zip Slip\")\\nExtracting files from a malicious zip archive without validating that the destination file path is within the destination directory can cause files outside the destination directory to be overwritten ...",
    "help_uri": "https://codeql.github.com/"
  },
  "tool": {
    "name": "CodeQL",
    "guid": null,
    "version": "2.4.0"
  },
  "most_recent_instance": {
    "ref": "refs/heads/main",
    "analysis_key": ".github/workflows/codeql-analysis.yml:CodeQL-Build",
    "category": ".github/workflows/codeql-analysis.yml:CodeQL-Build",
    "environment": "{}",
    "issue_state": "dismissed",
    "commit_sha": "39406e42cb832f683daa691dd652a8dc36ee8930",
    "message": {
      "text": "This path depends on a user-provided value."
    },
    "location": {
      "path": "spec-main/api-session-spec.ts",
      "start_line": 917,
      "end_line": 917,
      "start_column": 7,
      "end_column": 18
    },
    "classifications": [
      "test"
    ]
  },
  "instances_url": "https://api.github.com/repos/octocat/hello-world/code-scanning/alerts/42/instances"
}
```

## Get the status of an autofix for a code scanning alert
Gets the status and description of an autofix for a code scanning alert.
OAuth app tokens and personal access tokens (classic) need thesecurity_eventsscope to use this endpoint with private or public repositories, or thepublic_reposcope to use this endpoint with only public repositories.

### Fine-grained access tokens for "Get the status of an autofix for a code scanning alert"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Code scanning alerts" repository permissions (read)

### Parameters for "Get the status of an autofix for a code scanning alert"

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

### HTTP response status codes for "Get the status of an autofix for a code scanning alert"

[TABLE]
Status code | Description
200 | OK
400 | Bad Request
403 | Response if GitHub Advanced Security is not enabled for this repository
404 | Resource not found
503 | Service unavailable
[/TABLE]
OK
Bad Request
Response if GitHub Advanced Security is not enabled for this repository
Resource not found
Service unavailable

### Code samples for "Get the status of an autofix for a code scanning alert"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/code-scanning/alerts/ALERT_NUMBER/autofix
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "status": "success",
  "description": "This fixes an XSS vulnerability by escaping the user input.",
  "started_at": "2024-02-14T12:29:18Z"
}
```

## Create an autofix for a code scanning alert
Creates an autofix for a code scanning alert.
If a new autofix is to be created as a result of this request or is currently being generated, then this endpoint will return a 202 Accepted response.
If an autofix already exists for a given alert, then this endpoint will return a 200 OK response.
OAuth app tokens and personal access tokens (classic) need thesecurity_eventsscope to use this endpoint with private or public repositories, or thepublic_reposcope to use this endpoint with only public repositories.

### Fine-grained access tokens for "Create an autofix for a code scanning alert"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Code scanning alerts" repository permissions (write)

### Parameters for "Create an autofix for a code scanning alert"

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

### HTTP response status codes for "Create an autofix for a code scanning alert"

[TABLE]
Status code | Description
200 | OK
202 | Accepted
400 | Bad Request
403 | Response if the repository is archived, if GitHub Advanced Security is not enabled for this repository or if rate limit is exceeded
404 | Resource not found
422 | Unprocessable Entity
503 | Service unavailable
[/TABLE]
OK
Accepted
Bad Request
Response if the repository is archived, if GitHub Advanced Security is not enabled for this repository or if rate limit is exceeded
Resource not found
Unprocessable Entity
Service unavailable

### Code samples for "Create an autofix for a code scanning alert"

#### Request examples
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -X POST \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/code-scanning/alerts/ALERT_NUMBER/autofix
```

#### OK
- Example response
- Response schema

```
Status: 200
```

```
{
  "status": "success",
  "description": "This fixes an XSS vulnerability by escaping the user input.",
  "started_at": "2024-02-14T12:29:18Z"
}
```

## Commit an autofix for a code scanning alert
Commits an autofix for a code scanning alert.
If an autofix is committed as a result of this request, then this endpoint will return a 201 Created response.
OAuth app tokens and personal access tokens (classic) need thereposcope to use this endpoint with private or public repositories, or thepublic_reposcope to use this endpoint with only public repositories.

### Fine-grained access tokens for "Commit an autofix for a code scanning alert"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Contents" repository permissions (write)

### Parameters for "Commit an autofix for a code scanning alert"

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
target_refstringThe Git reference of target branch for the commit. Branch needs to already exist.  For more information, see "Git References" in the Git documentation.
messagestringCommit message to be used.
[/TABLE]
The Git reference of target branch for the commit. Branch needs to already exist.  For more information, see "Git References" in the Git documentation.
Commit message to be used.

### HTTP response status codes for "Commit an autofix for a code scanning alert"

[TABLE]
Status code | Description
201 | Created
400 | Bad Request
403 | Response if the repository is archived or if GitHub Advanced Security is not enabled for this repository
404 | Resource not found
422 | Unprocessable Entity
503 | Service unavailable
[/TABLE]
Created
Bad Request
Response if the repository is archived or if GitHub Advanced Security is not enabled for this repository
Resource not found
Unprocessable Entity
Service unavailable

### Code samples for "Commit an autofix for a code scanning alert"

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
  https://api.github.com/repos/OWNER/REPO/code-scanning/alerts/ALERT_NUMBER/autofix/commits \
  -d '{"target_ref":"refs/heads/fix-bug","message":"Let'\''s fix this 🪲!"}'
```

#### Created
- Example response
- Response schema

```
Status: 201
```

```
{
  "target_ref": "refs/heads/main",
  "commit_sha": "178f4f6090b3fccad4a65b3e83d076a622d59652"
}
```

## List instances of a code scanning alert
Lists all instances of the specified code scanning alert.
OAuth app tokens and personal access tokens (classic) need thesecurity_eventsscope to use this endpoint with private or public repositories, or thepublic_reposcope to use this endpoint with only public repositories.

### Fine-grained access tokens for "List instances of a code scanning alert"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Code scanning alerts" repository permissions (read)

### Parameters for "List instances of a code scanning alert"

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
pageintegerThe page_number number of the results to fetch. For more information, see "Using pagination in the REST API."Default:1
per_pageintegerThe number of results per page_number (max 100). For more information, see "Using pagination in the REST API."Default:30
refstringThe Git reference for the results you want to list. Thereffor a branch can be formatted either asrefs/heads/<branch name>or simply<branch name>. To reference a pull request userefs/pull/<number>/merge.
printegerThe number of the pull request for the results you want to list.
[/TABLE]
The page_number number of the results to fetch. For more information, see "Using pagination in the REST API."
Default:1
The number of results per page_number (max 100). For more information, see "Using pagination in the REST API."
Default:30
The Git reference for the results you want to list. Thereffor a branch can be formatted either asrefs/heads/<branch name>or simply<branch name>. To reference a pull request userefs/pull/<number>/merge.
The number of the pull request for the results you want to list.

### HTTP response status codes for "List instances of a code scanning alert"

[TABLE]
Status code | Description
200 | OK
403 | Response if GitHub Advanced Security is not enabled for this repository
404 | Resource not found
503 | Service unavailable
[/TABLE]
OK
Response if GitHub Advanced Security is not enabled for this repository
Resource not found
Service unavailable

### Code samples for "List instances of a code scanning alert"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/code-scanning/alerts/ALERT_NUMBER/instances
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
    "ref": "refs/heads/main",
    "analysis_key": ".github/workflows/codeql-analysis.yml:CodeQL-Build",
    "environment": "",
    "category": ".github/workflows/codeql-analysis.yml:CodeQL-Build",
    "issue_state": "open",
    "commit_sha": "39406e42cb832f683daa691dd652a8dc36ee8930",
    "message": {
      "text": "This path depends on a user-provided value."
    },
    "location": {
      "path": "lib/ab12-gen.js",
      "start_line": 917,
      "end_line": 917,
      "start_column": 7,
      "end_column": 18
    },
    "classifications": [
      "library"
    ]
  },
  {
    "ref": "refs/pull/3740/merge",
    "analysis_key": ".github/workflows/codeql-analysis.yml:CodeQL-Build",
    "environment": "",
    "category": ".github/workflows/codeql-analysis.yml:CodeQL-Build",
    "issue_state": "fixed",
    "commit_sha": "b09da05606e27f463a2b49287684b4ae777092f2",
    "message": {
      "text": "This suffix check is missing a length comparison to correctly handle lastIndexOf returning -1."
    },
    "location": {
      "path": "app/script.js",
      "start_line": 2,
      "end_line": 2,
      "start_column": 10,
      "end_column": 50
    },
    "classifications": [
      "source"
    ]
  }
]
```

## List code scanning analyses for a repository
Lists the details of all code scanning analyses for a repository,
starting with the most recent.
The response is paginated and you can use thepageandper_pageparameters
to list the analyses you're interested in.
By default 30 analyses are listed per page_number.
Therules_countfield in the response give the number of rules
that were run in the analysis.
For very old analyses this data is not available,
and0is returned in this field.
Warning
Closing down notice:Thetool_namefield is closing down and will, in future, not be included in the response for this endpoint. The example response reflects this change. The tool name can now be found inside thetoolfield.
OAuth app tokens and personal access tokens (classic) need thesecurity_eventsscope to use this endpoint with private or public repositories, or thepublic_reposcope to use this endpoint with only public repositories.

### Fine-grained access tokens for "List code scanning analyses for a repository"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Code scanning alerts" repository permissions (read)

### Parameters for "List code scanning analyses for a repository"

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
tool_namestringThe name of a code scanning tool. Only results by this tool will be listed. You can specify the tool by using eithertool_nameortool_guid, but not both.
tool_guidstring or nullThe GUID of a code scanning tool. Only results by this tool will be listed. Note that some code scanning tools may not include a GUID in their analysis data. You can specify the tool by using eithertool_guidortool_name, but not both.
pageintegerThe page_number number of the results to fetch. For more information, see "Using pagination in the REST API."Default:1
per_pageintegerThe number of results per page_number (max 100). For more information, see "Using pagination in the REST API."Default:30
printegerThe number of the pull request for the results you want to list.
refstringThe Git reference for the analyses you want to list. Thereffor a branch can be formatted either asrefs/heads/<branch name>or simply<branch name>. To reference a pull request userefs/pull/<number>/merge.
sarif_idstringFilter analyses belonging to the same SARIF upload.
directionstringThe direction to sort the results by.Default:descCan be one of:asc,desc
sortstringThe property by which to sort the results.Default:createdValue:created
[/TABLE]
The name of a code scanning tool. Only results by this tool will be listed. You can specify the tool by using eithertool_nameortool_guid, but not both.
The GUID of a code scanning tool. Only results by this tool will be listed. Note that some code scanning tools may not include a GUID in their analysis data. You can specify the tool by using eithertool_guidortool_name, but not both.
The page_number number of the results to fetch. For more information, see "Using pagination in the REST API."
Default:1
The number of results per page_number (max 100). For more information, see "Using pagination in the REST API."
Default:30
The number of the pull request for the results you want to list.
The Git reference for the analyses you want to list. Thereffor a branch can be formatted either asrefs/heads/<branch name>or simply<branch name>. To reference a pull request userefs/pull/<number>/merge.
Filter analyses belonging to the same SARIF upload.
The direction to sort the results by.
Default:desc
Can be one of:asc,desc
The property by which to sort the results.
Default:created
Value:created

### HTTP response status codes for "List code scanning analyses for a repository"

[TABLE]
Status code | Description
200 | OK
403 | Response if GitHub Advanced Security is not enabled for this repository
404 | Resource not found
503 | Service unavailable
[/TABLE]
OK
Response if GitHub Advanced Security is not enabled for this repository
Resource not found
Service unavailable

### Code samples for "List code scanning analyses for a repository"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/code-scanning/analyses
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
    "ref": "refs/heads/main",
    "commit_sha": "d99612c3e1f2970085cfbaeadf8f010ef69bad83",
    "analysis_key": ".github/workflows/codeql-analysis.yml:analyze",
    "environment": "{\"language\":\"python\"}",
    "error": "",
    "category": ".github/workflows/codeql-analysis.yml:analyze/language:python",
    "created_at": "2020-08-27T15:05:21Z",
    "results_count": 17,
    "rules_count": 49,
    "id": 201,
    "url": "https://api.github.com/repos/octocat/hello-world/code-scanning/analyses/201",
    "sarif_id": "6c81cd8e-b078-4ac3-a3be-1dad7dbd0b53",
    "tool": {
      "name": "CodeQL",
      "guid": null,
      "version": "2.4.0"
    },
    "deletable": true,
    "warning": ""
  },
  {
    "ref": "refs/heads/my-branch",
    "commit_sha": "c8cff6510d4d084fb1b4aa13b64b97ca12b07321",
    "analysis_key": ".github/workflows/shiftleft.yml:build",
    "environment": "{}",
    "error": "",
    "category": ".github/workflows/shiftleft.yml:build/",
    "created_at": "2020-08-31T22:46:44Z",
    "results_count": 17,
    "rules_count": 32,
    "id": 200,
    "url": "https://api.github.com/repos/octocat/hello-world/code-scanning/analyses/200",
    "sarif_id": "8981cd8e-b078-4ac3-a3be-1dad7dbd0b582",
    "tool": {
      "name": "Python Security Analysis",
      "guid": null,
      "version": "1.2.0"
    },
    "deletable": true,
    "warning": ""
  }
]
```

## Get a code scanning analysis for a repository
Gets a specified code scanning analysis for a repository.
The default JSON response contains fields that describe the analysis.
This includes the Git reference and commit SHA to which the analysis relates,
the datetime of the analysis, the name of the code scanning tool,
and the number of alerts.
Therules_countfield in the default response give the number of rules
that were run in the analysis.
For very old analyses this data is not available,
and0is returned in this field.
This endpoint supports the following custom media types. For more information, see "Media types."
- application/sarif+json: Instead of returning a summary of the analysis, this endpoint returns a subset of the analysis data that was uploaded. The data is formatted asSARIF version 2.1.0. It also returns additional data such as thegithub/alertNumberandgithub/alertUrlproperties.

```
application/sarif+json
```
OAuth app tokens and personal access tokens (classic) need thesecurity_eventsscope to use this endpoint with private or public repositories, or thepublic_reposcope to use this endpoint with only public repositories.

### Fine-grained access tokens for "Get a code scanning analysis for a repository"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Code scanning alerts" repository permissions (read)

### Parameters for "Get a code scanning analysis for a repository"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
analysis_idintegerRequiredThe ID of the analysis, as returned from theGET /repos/{owner}/{repo}/code-scanning/analysesoperation.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.

```
analysis_id
```
The ID of the analysis, as returned from theGET /repos/{owner}/{repo}/code-scanning/analysesoperation.

### HTTP response status codes for "Get a code scanning analysis for a repository"

[TABLE]
Status code | Description
200 | OK
403 | Response if GitHub Advanced Security is not enabled for this repository
404 | Resource not found
422 | Response if analysis could not be processed
503 | Service unavailable
[/TABLE]
OK
Response if GitHub Advanced Security is not enabled for this repository
Resource not found
Response if analysis could not be processed
Service unavailable

### Code samples for "Get a code scanning analysis for a repository"

#### Request examples
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/code-scanning/analyses/ANALYSIS_ID
```

#### application/json response
- Example response
- Response schema

```
Status: 200
```

```
{
  "ref": "refs/heads/main",
  "commit_sha": "c18c69115654ff0166991962832dc2bd7756e655",
  "analysis_key": ".github/workflows/codeql-analysis.yml:analyze",
  "environment": "{\"language\":\"javascript\"}",
  "error": "",
  "category": ".github/workflows/codeql-analysis.yml:analyze/language:javascript",
  "created_at": "2021-01-13T11:55:49Z",
  "results_count": 3,
  "rules_count": 67,
  "id": 3602840,
  "url": "https://api.github.com/repos/octocat/hello-world/code-scanning/analyses/201",
  "sarif_id": "47177e22-5596-11eb-80a1-c1e54ef945c6",
  "tool": {
    "name": "CodeQL",
    "guid": null,
    "version": "2.4.0"
  },
  "deletable": true,
  "warning": ""
}
```

## Delete a code scanning analysis from a repository
Deletes a specified code scanning analysis from a repository.
You can delete one analysis at a time.
To delete a series of analyses, start with the most recent analysis and work backwards.
Conceptually, the process is similar to the undo function in a text editor.
When you list the analyses for a repository,
one or more will be identified as deletable in the response:

```
"deletable": true
```

```
"deletable": true
```
An analysis is deletable when it's the most recent in a set of analyses.
Typically, a repository will have multiple sets of analyses
for each enabled code scanning tool,
where a set is determined by a unique combination of analysis values:
- ref
- tool
- category
If you attempt to delete an analysis that is not the most recent in a set,
you'll get a 400 response with the message:

```
Analysis specified is not deletable.
```

```
Analysis specified is not deletable.
```
The response from a successfulDELETEoperation provides you with
two alternative URLs for deleting the next analysis in the set:next_analysis_urlandconfirm_delete_url.
Use thenext_analysis_urlURL if you want to avoid accidentally deleting the final analysis
in a set. This is a useful option if you want to preserve at least one analysis
for the specified tool in your repository.
Use theconfirm_delete_urlURL if you are content to remove all analyses for a tool.
When you delete the last analysis in a set, the value ofnext_analysis_urlandconfirm_delete_urlin the 200 response isnull.
As an example of the deletion process,
let's imagine that you added a workflow that configured a particular code scanning tool
to analyze the code in a repository. This tool has added 15 analyses:
10 on the default branch, and another 5 on a topic branch.
You therefore have two separate sets of analyses for this tool.
You've now decided that you want to remove all of the analyses for the tool.
To do this you must make 15 separate deletion requests.
To start, you must find an analysis that's identified as deletable.
Each set of analyses always has one that's identified as deletable.
Having found the deletable analysis for one of the two sets,
delete this analysis and then continue deleting the next analysis in the set until they're all deleted.
Then repeat the process for the second set.
The procedure therefore consists of a nested loop:
Outer loop:
- List the analyses for the repository, filtered by tool.
- Parse this list to find a deletable analysis. If found:Inner loop:Delete the identified analysis.Parse the response for the value ofconfirm_delete_urland, if found, use this in the next iteration.
- Delete the identified analysis.
- Parse the response for the value ofconfirm_delete_urland, if found, use this in the next iteration.
The above process assumes that you want to remove all trace of the tool's analyses from the GitHub user interface, for the specified repository, and it therefore uses theconfirm_delete_urlvalue. Alternatively, you could use thenext_analysis_urlvalue, which would leave the last analysis in each set undeleted to avoid removing a tool's analysis entirely.
OAuth app tokens and personal access tokens (classic) need thereposcope to use this endpoint with private or public repositories, or thepublic_reposcope to use this endpoint with only public repositories.

### Fine-grained access tokens for "Delete a code scanning analysis from a repository"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Code scanning alerts" repository permissions (write)

### Parameters for "Delete a code scanning analysis from a repository"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
analysis_idintegerRequiredThe ID of the analysis, as returned from theGET /repos/{owner}/{repo}/code-scanning/analysesoperation.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.

```
analysis_id
```
The ID of the analysis, as returned from theGET /repos/{owner}/{repo}/code-scanning/analysesoperation.

[TABLE]
Name, Type, Description
confirm_deletestring or nullAllow deletion if the specified analysis is the last in a set. If you attempt to delete the final analysis in a set without setting this parameter totrue, you'll get a 400 response with the message:Analysis is last of its type and deletion may result in the loss of historical alert data. Please specify confirm_delete.
[/TABLE]

```
confirm_delete
```
Allow deletion if the specified analysis is the last in a set. If you attempt to delete the final analysis in a set without setting this parameter totrue, you'll get a 400 response with the message:Analysis is last of its type and deletion may result in the loss of historical alert data. Please specify confirm_delete.

### HTTP response status codes for "Delete a code scanning analysis from a repository"

[TABLE]
Status code | Description
200 | OK
400 | Bad Request
403 | Response if the repository is archived or if GitHub Advanced Security is not enabled for this repository
404 | Resource not found
503 | Service unavailable
[/TABLE]
OK
Bad Request
Response if the repository is archived or if GitHub Advanced Security is not enabled for this repository
Resource not found
Service unavailable

### Code samples for "Delete a code scanning analysis from a repository"

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
  https://api.github.com/repos/OWNER/REPO/code-scanning/analyses/ANALYSIS_ID
```

#### Default response
- Example response
- Response schema

```
Status: 200
```

```
{
  "next_analysis_url": "https://api.github.com/repos/octocat/hello-world/code-scanning/analyses/41",
  "confirm_delete_url": "https://api.github.com/repos/octocat/hello-world/code-scanning/analyses/41?confirm_delete"
}
```

## List CodeQL databases for a repository
Lists the CodeQL databases that are available in a repository.
OAuth app tokens and personal access tokens (classic) need thereposcope to use this endpoint with private or public repositories, or thepublic_reposcope to use this endpoint with only public repositories.

### Fine-grained access tokens for "List CodeQL databases for a repository"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Contents" repository permissions (read)
This endpoint can be used without authentication or the aforementioned permissions if only public resources are requested.

### Parameters for "List CodeQL databases for a repository"

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

### HTTP response status codes for "List CodeQL databases for a repository"

[TABLE]
Status code | Description
200 | OK
403 | Response if GitHub Advanced Security is not enabled for this repository
404 | Resource not found
503 | Service unavailable
[/TABLE]
OK
Response if GitHub Advanced Security is not enabled for this repository
Resource not found
Service unavailable

### Code samples for "List CodeQL databases for a repository"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/code-scanning/codeql/databases
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
    "name": "database.zip",
    "language": "java",
    "uploader": {
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
    "content_type": "application/zip",
    "size": 1024,
    "created_at": "2022-09-12T12:14:32Z",
    "updated_at": "2022-09-12T12:14:32Z",
    "url": "https://api.github.com/repos/octocat/Hello-World/code-scanning/codeql/databases/java",
    "commit_oid": "1927de39fefa25a9d0e64e3f540ff824a72f538c"
  },
  {
    "id": 2,
    "name": "database.zip",
    "language": "ruby",
    "uploader": {
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
    "content_type": "application/zip",
    "size": 1024,
    "created_at": "2022-09-12T12:14:32Z",
    "updated_at": "2022-09-12T12:14:32Z",
    "url": "https://api.github.com/repos/octocat/Hello-World/code-scanning/codeql/databases/ruby",
    "commit_oid": "1927de39fefa25a9d0e64e3f540ff824a72f538c"
  }
]
```

## Get a CodeQL database for a repository
Gets a CodeQL database for a language in a repository.
By default this endpoint returns JSON metadata about the CodeQL database. To
download the CodeQL database binary content, set theAcceptheader of the request
toapplication/zip, and make sure
your HTTP client is configured to follow redirects or use theLocationheader
to make a second request to get the redirect URL.

```
application/zip
```
OAuth app tokens and personal access tokens (classic) need thereposcope to use this endpoint with private or public repositories, or thepublic_reposcope to use this endpoint with only public repositories.

### Fine-grained access tokens for "Get a CodeQL database for a repository"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Contents" repository permissions (read)
This endpoint can be used without authentication or the aforementioned permissions if only public resources are requested.

### Parameters for "Get a CodeQL database for a repository"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
languagestringRequiredThe language of the CodeQL database.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.
The language of the CodeQL database.

### HTTP response status codes for "Get a CodeQL database for a repository"

[TABLE]
Status code | Description
200 | OK
302 | Found
403 | Response if GitHub Advanced Security is not enabled for this repository
404 | Resource not found
503 | Service unavailable
[/TABLE]
OK
Found
Response if GitHub Advanced Security is not enabled for this repository
Resource not found
Service unavailable

### Code samples for "Get a CodeQL database for a repository"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/code-scanning/codeql/databases/LANGUAGE
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
  "name": "database.zip",
  "language": "java",
  "uploader": {
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
  "content_type": "application/zip",
  "size": 1024,
  "created_at": "2022-09-12T12:14:32Z",
  "updated_at": "2022-09-12T12:14:32Z",
  "url": "https://api.github.com/repos/octocat/Hello-World/code-scanning/codeql/databases/java",
  "commit_oid": "1927de39fefa25a9d0e64e3f540ff824a72f538c"
}
```

## Delete a CodeQL database
Deletes a CodeQL database for a language in a repository.
OAuth app tokens and personal access tokens (classic) need thereposcope to use this endpoint with private or public repositories, or thepublic_reposcope to use this endpoint with only public repositories.

### Fine-grained access tokens for "Delete a CodeQL database"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Contents" repository permissions (write)

### Parameters for "Delete a CodeQL database"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
languagestringRequiredThe language of the CodeQL database.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.
The language of the CodeQL database.

### HTTP response status codes for "Delete a CodeQL database"

[TABLE]
Status code | Description
204 | No Content
403 | Response if the repository is archived or if GitHub Advanced Security is not enabled for this repository
404 | Resource not found
503 | Service unavailable
[/TABLE]
No Content
Response if the repository is archived or if GitHub Advanced Security is not enabled for this repository
Resource not found
Service unavailable

### Code samples for "Delete a CodeQL database"

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
  https://api.github.com/repos/OWNER/REPO/code-scanning/codeql/databases/LANGUAGE
```

#### Response

```
Status: 204
```

## Create a CodeQL variant analysis
Creates a new CodeQL variant analysis, which will run a CodeQL query against one or more repositories.
Get started by learning more aboutrunning CodeQL queries at scale with Multi-Repository Variant Analysis.
Use theownerandrepoparameters in the URL to specify the controller repository that
will be used for running GitHub Actions workflows and storing the results of the CodeQL variant analysis.
OAuth app tokens and personal access tokens (classic) need thereposcope to use this endpoint.

### Fine-grained access tokens for "Create a CodeQL variant analysis"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Contents" repository permissions (write)

### Parameters for "Create a CodeQL variant analysis"

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

### HTTP response status codes for "Create a CodeQL variant analysis"

[TABLE]
Status code | Description
201 | Variant analysis submitted for processing
404 | Resource not found
422 | Unable to process variant analysis submission
503 | Service unavailable
[/TABLE]
Variant analysis submitted for processing
Resource not found
Unable to process variant analysis submission
Service unavailable

### Code samples for "Create a CodeQL variant analysis"

#### Request examples
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -X POST \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/code-scanning/codeql/variant-analyses \
  -d '{"language":"csharp","query_pack":"aGVsbG8=","repositories":["octocat/Hello-World","octocat/example"]}'
```

#### Response for a successful variant analysis submission
- Example response
- Response schema

```
Status: 201
```

```
{
  "summary": "Default response",
  "value": {
    "id": 1,
    "controller_repo": {
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
      "blobs_url": "https://api.github.com/repos/octocat/Hello-World/git/blobs{/commit_sha}",
      "branches_url": "https://api.github.com/repos/octocat/Hello-World/branches{/branch}",
      "collaborators_url": "https://api.github.com/repos/octocat/Hello-World/collaborators{/collaborator}",
      "comments_url": "https://api.github.com/repos/octocat/Hello-World/comments{/number}",
      "commits_url": "https://api.github.com/repos/octocat/Hello-World/commits{/commit_sha}",
      "compare_url": "https://api.github.com/repos/octocat/Hello-World/compare/{base}...{head}",
      "contents_url": "https://api.github.com/repos/octocat/Hello-World/contents/{+path}",
      "contributors_url": "https://api.github.com/repos/octocat/Hello-World/contributors",
      "deployments_url": "https://api.github.com/repos/octocat/Hello-World/deployments",
      "downloads_url": "https://api.github.com/repos/octocat/Hello-World/downloads",
      "events_url": "https://api.github.com/repos/octocat/Hello-World/events",
      "forks_url": "https://api.github.com/repos/octocat/Hello-World/forks",
      "git_commits_url": "https://api.github.com/repos/octocat/Hello-World/git/commits{/commit_sha}",
      "git_refs_url": "https://api.github.com/repos/octocat/Hello-World/git/refs{/commit_sha}",
      "git_tags_url": "https://api.github.com/repos/octocat/Hello-World/git/tags{/commit_sha}",
      "issue_comment_url": "https://api.github.com/repos/octocat/Hello-World/issues/comments{/number}",
      "issue_events_url": "https://api.github.com/repos/octocat/Hello-World/issues/events{/number}",
      "issues_url": "https://api.github.com/repos/octocat/Hello-World/issues{/number}",
      "keys_url": "https://api.github.com/repos/octocat/Hello-World/keys{/key_id}",
      "labels_url": "https://api.github.com/repos/octocat/Hello-World/label_filters{/name}",
      "languages_url": "https://api.github.com/repos/octocat/Hello-World/languages",
      "merges_url": "https://api.github.com/repos/octocat/Hello-World/merges",
      "milestones_url": "https://api.github.com/repos/octocat/Hello-World/milestones{/number}",
      "notifications_url": "https://api.github.com/repos/octocat/Hello-World/notifications{?since,all,participating}",
      "pulls_url": "https://api.github.com/repos/octocat/Hello-World/pulls{/number}",
      "releases_url": "https://api.github.com/repos/octocat/Hello-World/releases{/id}",
      "stargazers_url": "https://api.github.com/repos/octocat/Hello-World/stargazers",
      "statuses_url": "https://api.github.com/repos/octocat/Hello-World/statuses/{commit_sha}",
      "subscribers_url": "https://api.github.com/repos/octocat/Hello-World/subscribers",
      "subscription_url": "https://api.github.com/repos/octocat/Hello-World/subscription",
      "tags_url": "https://api.github.com/repos/octocat/Hello-World/tags",
      "teams_url": "https://api.github.com/repos/octocat/Hello-World/teams",
      "trees_url": "https://api.github.com/repos/octocat/Hello-World/git/trees{/commit_sha}",
      "hooks_url": "https://api.github.com/repos/octocat/Hello-World/hooks"
    },
    "actor": {
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
    "query_language": "python",
    "query_pack_url": "https://www.example.com",
    "created_at": "2022-09-12T12:14:32Z",
    "updated_at": "2022-09-12T12:14:32Z",
    "completed_at": "2022-09-12T13:15:33Z",
    "status": "succeeded",
    "actions_workflow_run_id": 3453588,
    "scanned_repositories": [
      {
        "repository": {
          "id": 1296269,
          "name": "Hello-World",
          "full_name": "octocat/Hello-World",
          "private": false
        },
        "analysis_status": "succeeded",
        "result_count": 532,
        "artifact_size_in_bytes": 12345
      }
    ],
    "skipped_repositories": {
      "access_mismatch_repos": {
        "repository_count": 2,
        "repositories": [
          {
            "id": 1,
            "name": "octo-repo1",
            "full_name": "octo-org/octo-repo1",
            "private": false
          },
          {
            "id": 2,
            "name": "octo-repo2",
            "full_name": "octo-org/octo-repo2",
            "private": false
          }
        ]
      },
      "not_found_repos": {
        "repository_count": 3,
        "repository_full_names": [
          "octo-org/octo-repo4",
          "octo-org/octo-repo5",
          "octo-org/octo-repo6"
        ]
      },
      "no_codeql_db_repos": {
        "repository_count": 2,
        "repositories": [
          {
            "id": 7,
            "name": "octo-repo7",
            "full_name": "octo-org/octo-repo7",
            "private": false
          },
          {
            "id": 8,
            "name": "octo-repo8",
            "full_name": "octo-org/octo-repo8",
            "private": false
          }
        ]
      },
      "over_limit_repos": {
        "repository_count": 2,
        "repositories": [
          {
            "id": 9,
            "name": "octo-repo9",
            "full_name": "octo-org/octo-repo9",
            "private": false
          },
          {
            "id": 10,
            "name": "octo-repo10",
            "full_name": "octo-org/octo-repo10",
            "private": false
          }
        ]
      }
    }
  }
}
```

## Get the summary of a CodeQL variant analysis
Gets the summary of a CodeQL variant analysis.
OAuth app tokens and personal access tokens (classic) need thesecurity_eventsscope to use this endpoint with private or public repositories, or thepublic_reposcope to use this endpoint with only public repositories.

### Fine-grained access tokens for "Get the summary of a CodeQL variant analysis"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Contents" repository permissions (read)
This endpoint can be used without authentication or the aforementioned permissions if only public resources are requested.

### Parameters for "Get the summary of a CodeQL variant analysis"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
codeql_variant_analysis_idintegerRequiredThe unique identifier of the variant analysis.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.

```
codeql_variant_analysis_id
```
The unique identifier of the variant analysis.

### HTTP response status codes for "Get the summary of a CodeQL variant analysis"

[TABLE]
Status code | Description
200 | OK
404 | Resource not found
503 | Service unavailable
[/TABLE]
OK
Resource not found
Service unavailable

### Code samples for "Get the summary of a CodeQL variant analysis"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/code-scanning/codeql/variant-analyses/CODEQL_VARIANT_ANALYSIS_ID
```

#### Default response
- Example response
- Response schema

```
Status: 200
```

```
{
  "id": 1,
  "controller_repo": {
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
    "blobs_url": "https://api.github.com/repos/octocat/Hello-World/git/blobs{/commit_sha}",
    "branches_url": "https://api.github.com/repos/octocat/Hello-World/branches{/branch}",
    "collaborators_url": "https://api.github.com/repos/octocat/Hello-World/collaborators{/collaborator}",
    "comments_url": "https://api.github.com/repos/octocat/Hello-World/comments{/number}",
    "commits_url": "https://api.github.com/repos/octocat/Hello-World/commits{/commit_sha}",
    "compare_url": "https://api.github.com/repos/octocat/Hello-World/compare/{base}...{head}",
    "contents_url": "https://api.github.com/repos/octocat/Hello-World/contents/{+path}",
    "contributors_url": "https://api.github.com/repos/octocat/Hello-World/contributors",
    "deployments_url": "https://api.github.com/repos/octocat/Hello-World/deployments",
    "downloads_url": "https://api.github.com/repos/octocat/Hello-World/downloads",
    "events_url": "https://api.github.com/repos/octocat/Hello-World/events",
    "forks_url": "https://api.github.com/repos/octocat/Hello-World/forks",
    "git_commits_url": "https://api.github.com/repos/octocat/Hello-World/git/commits{/commit_sha}",
    "git_refs_url": "https://api.github.com/repos/octocat/Hello-World/git/refs{/commit_sha}",
    "git_tags_url": "https://api.github.com/repos/octocat/Hello-World/git/tags{/commit_sha}",
    "issue_comment_url": "https://api.github.com/repos/octocat/Hello-World/issues/comments{/number}",
    "issue_events_url": "https://api.github.com/repos/octocat/Hello-World/issues/events{/number}",
    "issues_url": "https://api.github.com/repos/octocat/Hello-World/issues{/number}",
    "keys_url": "https://api.github.com/repos/octocat/Hello-World/keys{/key_id}",
    "labels_url": "https://api.github.com/repos/octocat/Hello-World/label_filters{/name}",
    "languages_url": "https://api.github.com/repos/octocat/Hello-World/languages",
    "merges_url": "https://api.github.com/repos/octocat/Hello-World/merges",
    "milestones_url": "https://api.github.com/repos/octocat/Hello-World/milestones{/number}",
    "notifications_url": "https://api.github.com/repos/octocat/Hello-World/notifications{?since,all,participating}",
    "pulls_url": "https://api.github.com/repos/octocat/Hello-World/pulls{/number}",
    "releases_url": "https://api.github.com/repos/octocat/Hello-World/releases{/id}",
    "stargazers_url": "https://api.github.com/repos/octocat/Hello-World/stargazers",
    "statuses_url": "https://api.github.com/repos/octocat/Hello-World/statuses/{commit_sha}",
    "subscribers_url": "https://api.github.com/repos/octocat/Hello-World/subscribers",
    "subscription_url": "https://api.github.com/repos/octocat/Hello-World/subscription",
    "tags_url": "https://api.github.com/repos/octocat/Hello-World/tags",
    "teams_url": "https://api.github.com/repos/octocat/Hello-World/teams",
    "trees_url": "https://api.github.com/repos/octocat/Hello-World/git/trees{/commit_sha}",
    "hooks_url": "https://api.github.com/repos/octocat/Hello-World/hooks"
  },
  "actor": {
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
  "query_language": "python",
  "query_pack_url": "https://www.example.com",
  "created_at": "2022-09-12T12:14:32Z",
  "updated_at": "2022-09-12T12:14:32Z",
  "completed_at": "2022-09-12T13:15:33Z",
  "status": "succeeded",
  "actions_workflow_run_id": 3453588,
  "scanned_repositories": [
    {
      "repository": {
        "id": 1296269,
        "name": "Hello-World",
        "full_name": "octocat/Hello-World",
        "private": false
      },
      "analysis_status": "succeeded",
      "result_count": 532,
      "artifact_size_in_bytes": 12345
    }
  ],
  "skipped_repositories": {
    "access_mismatch_repos": {
      "repository_count": 2,
      "repositories": [
        {
          "id": 1,
          "name": "octo-repo1",
          "full_name": "octo-org/octo-repo1",
          "private": false
        },
        {
          "id": 2,
          "name": "octo-repo2",
          "full_name": "octo-org/octo-repo2",
          "private": false
        }
      ]
    },
    "not_found_repos": {
      "repository_count": 3,
      "repository_full_names": [
        "octo-org/octo-repo4",
        "octo-org/octo-repo5",
        "octo-org/octo-repo6"
      ]
    },
    "no_codeql_db_repos": {
      "repository_count": 2,
      "repositories": [
        {
          "id": 7,
          "name": "octo-repo7",
          "full_name": "octo-org/octo-repo7",
          "private": false
        },
        {
          "id": 8,
          "name": "octo-repo8",
          "full_name": "octo-org/octo-repo8",
          "private": false
        }
      ]
    },
    "over_limit_repos": {
      "repository_count": 2,
      "repositories": [
        {
          "id": 9,
          "name": "octo-repo9",
          "full_name": "octo-org/octo-repo9",
          "private": false
        },
        {
          "id": 10,
          "name": "octo-repo10",
          "full_name": "octo-org/octo-repo10",
          "private": false
        }
      ]
    }
  }
}
```

## Get the analysis status of a repository in a CodeQL variant analysis
Gets the analysis status of a repository in a CodeQL variant analysis.
OAuth app tokens and personal access tokens (classic) need thesecurity_eventsscope to use this endpoint with private or public repositories, or thepublic_reposcope to use this endpoint with only public repositories.

### Fine-grained access tokens for "Get the analysis status of a repository in a CodeQL variant analysis"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Contents" repository permissions (read)

### Parameters for "Get the analysis status of a repository in a CodeQL variant analysis"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the controller repository.
codeql_variant_analysis_idintegerRequiredThe ID of the variant analysis.
repo_ownerstringRequiredThe account owner of the variant analysis repository. The name is not case sensitive.
repo_namestringRequiredThe name of the variant analysis repository.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the controller repository.

```
codeql_variant_analysis_id
```
The ID of the variant analysis.
The account owner of the variant analysis repository. The name is not case sensitive.
The name of the variant analysis repository.

### HTTP response status codes for "Get the analysis status of a repository in a CodeQL variant analysis"

[TABLE]
Status code | Description
200 | OK
404 | Resource not found
503 | Service unavailable
[/TABLE]
OK
Resource not found
Service unavailable

### Code samples for "Get the analysis status of a repository in a CodeQL variant analysis"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/code-scanning/codeql/variant-analyses/CODEQL_VARIANT_ANALYSIS_ID/repos/REPO_OWNER/REPO_NAME
```

#### Default response
- Example response
- Response schema

```
Status: 200
```

```
{
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
    "blobs_url": "https://api.github.com/repos/octocat/Hello-World/git/blobs{/commit_sha}",
    "branches_url": "https://api.github.com/repos/octocat/Hello-World/branches{/branch}",
    "collaborators_url": "https://api.github.com/repos/octocat/Hello-World/collaborators{/collaborator}",
    "comments_url": "https://api.github.com/repos/octocat/Hello-World/comments{/number}",
    "commits_url": "https://api.github.com/repos/octocat/Hello-World/commits{/commit_sha}",
    "compare_url": "https://api.github.com/repos/octocat/Hello-World/compare/{base}...{head}",
    "contents_url": "https://api.github.com/repos/octocat/Hello-World/contents/{+path}",
    "contributors_url": "https://api.github.com/repos/octocat/Hello-World/contributors",
    "deployments_url": "https://api.github.com/repos/octocat/Hello-World/deployments",
    "downloads_url": "https://api.github.com/repos/octocat/Hello-World/downloads",
    "events_url": "https://api.github.com/repos/octocat/Hello-World/events",
    "forks_url": "https://api.github.com/repos/octocat/Hello-World/forks",
    "git_commits_url": "https://api.github.com/repos/octocat/Hello-World/git/commits{/commit_sha}",
    "git_refs_url": "https://api.github.com/repos/octocat/Hello-World/git/refs{/commit_sha}",
    "git_tags_url": "https://api.github.com/repos/octocat/Hello-World/git/tags{/commit_sha}",
    "issue_comment_url": "https://api.github.com/repos/octocat/Hello-World/issues/comments{/number}",
    "issue_events_url": "https://api.github.com/repos/octocat/Hello-World/issues/events{/number}",
    "issues_url": "https://api.github.com/repos/octocat/Hello-World/issues{/number}",
    "keys_url": "https://api.github.com/repos/octocat/Hello-World/keys{/key_id}",
    "labels_url": "https://api.github.com/repos/octocat/Hello-World/label_filters{/name}",
    "languages_url": "https://api.github.com/repos/octocat/Hello-World/languages",
    "merges_url": "https://api.github.com/repos/octocat/Hello-World/merges",
    "milestones_url": "https://api.github.com/repos/octocat/Hello-World/milestones{/number}",
    "notifications_url": "https://api.github.com/repos/octocat/Hello-World/notifications{?since,all,participating}",
    "pulls_url": "https://api.github.com/repos/octocat/Hello-World/pulls{/number}",
    "releases_url": "https://api.github.com/repos/octocat/Hello-World/releases{/id}",
    "stargazers_url": "https://api.github.com/repos/octocat/Hello-World/stargazers",
    "statuses_url": "https://api.github.com/repos/octocat/Hello-World/statuses/{commit_sha}",
    "subscribers_url": "https://api.github.com/repos/octocat/Hello-World/subscribers",
    "subscription_url": "https://api.github.com/repos/octocat/Hello-World/subscription",
    "tags_url": "https://api.github.com/repos/octocat/Hello-World/tags",
    "teams_url": "https://api.github.com/repos/octocat/Hello-World/teams",
    "trees_url": "https://api.github.com/repos/octocat/Hello-World/git/trees{/commit_sha}",
    "hooks_url": "https://api.github.com/repos/octocat/Hello-World/hooks"
  },
  "analysis_status": "succeeded",
  "artifact_size_in_bytes": 12345,
  "result_count": 532,
  "database_commit_sha": "2d870c2a717a524627af38fa2da382188a096f90",
  "source_location_prefix": "/",
  "artifact_url": "https://example.com"
}
```

## Get a code scanning default setup configuration
Gets a code scanning default setup configuration.
OAuth app tokens and personal access tokens (classic) need thereposcope to use this endpoint with private or public repositories, or thepublic_reposcope to use this endpoint with only public repositories.

### Fine-grained access tokens for "Get a code scanning default setup configuration"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Administration" repository permissions (read)

### Parameters for "Get a code scanning default setup configuration"

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

### HTTP response status codes for "Get a code scanning default setup configuration"

[TABLE]
Status code | Description
200 | OK
403 | Response if GitHub Advanced Security is not enabled for this repository
404 | Resource not found
503 | Service unavailable
[/TABLE]
OK
Response if GitHub Advanced Security is not enabled for this repository
Resource not found
Service unavailable

### Code samples for "Get a code scanning default setup configuration"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/code-scanning/default-setup
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "issue_state": "configured",
  "languages": [
    "ruby",
    "python"
  ],
  "query_suite": "default",
  "threat_model": "remote",
  "updated_at": "2023-01-19T11:21:34Z",
  "schedule": "weekly"
}
```

## Update a code scanning default setup configuration
Updates a code scanning default setup configuration.
OAuth app tokens and personal access tokens (classic) need thereposcope to use this endpoint with private or public repositories, or thepublic_reposcope to use this endpoint with only public repositories.

### Fine-grained access tokens for "Update a code scanning default setup configuration"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Administration" repository permissions (write)

### Parameters for "Update a code scanning default setup configuration"

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
statestringThe desired issue_state of code scanning default setup.Can be one of:configured,not-configured
runner_typestringRunner type to be used.Can be one of:standard,labeled
runner_labelstring or nullRunner label to be used if the runner type is labeled.
query_suitestringCodeQL query suite to be used.Can be one of:default,extended
threat_modelstringThreat model to be used for code scanning analysis. Useremoteto analyze only network sources andremote_and_localto include local sources like filesystem access, command-line arguments, database reads, environment variable and standard input.Can be one of:remote,remote_and_local
languagesarray of stringsCodeQL languages to be analyzed.
Supported values are:actions,c-cpp,csharp,go,java-kotlin,javascript-typescript,python,ruby,swift
[/TABLE]
The desired issue_state of code scanning default setup.
Can be one of:configured,not-configured

```
not-configured
```

```
runner_type
```
Runner type to be used.
Can be one of:standard,labeled

```
runner_label
```
Runner label to be used if the runner type is labeled.

```
query_suite
```
CodeQL query suite to be used.
Can be one of:default,extended

```
threat_model
```
Threat model to be used for code scanning analysis. Useremoteto analyze only network sources andremote_and_localto include local sources like filesystem access, command-line arguments, database reads, environment variable and standard input.
Can be one of:remote,remote_and_local

```
remote_and_local
```
CodeQL languages to be analyzed.
Supported values are:actions,c-cpp,csharp,go,java-kotlin,javascript-typescript,python,ruby,swift

### HTTP response status codes for "Update a code scanning default setup configuration"

[TABLE]
Status code | Description
200 | OK
202 | Accepted
403 | Response if the repository is archived or if GitHub Advanced Security is not enabled for this repository
404 | Resource not found
409 | Response if there is already a validation run in progress with a different default setup configuration
422 | Response if the configuration change cannot be made because the repository is not in the required issue_state
503 | Service unavailable
[/TABLE]
OK
Accepted
Response if the repository is archived or if GitHub Advanced Security is not enabled for this repository
Resource not found
Response if there is already a validation run in progress with a different default setup configuration
Response if the configuration change cannot be made because the repository is not in the required issue_state
Service unavailable

### Code samples for "Update a code scanning default setup configuration"

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
  https://api.github.com/repos/OWNER/REPO/code-scanning/default-setup \
  -d '{"issue_state":"configured","threat_model":"remote_and_local"}'
```

#### Response
- Example response
- Response schema

```
Status: 202
```

```
{
  "run_id": 42,
  "run_url": "https://api.github.com/repos/octoorg/octocat/actions/runs/42"
}
```

## Upload an analysis as SARIF data
Uploads SARIF data containing the results of a code scanning analysis to make the results available in a repository. For troubleshooting information, see "Troubleshooting SARIF uploads."
There are two places where you can upload code scanning results.
- If you upload to a pull request, for example--ref refs/pull/42/mergeor--ref refs/pull/42/head, then the results appear as alerts in a pull request check. For more information, see "Triaging code scanning alerts in pull requests."
- If you upload to a branch, for example--ref refs/heads/my-branch, then the results appear in theSecuritytab for your repository. For more information, see "Managing code scanning alerts for your repository."
You must compress the SARIF-formatted analysis data that you want to upload, usinggzip, and then encode it as a Base64 format string. For example:

```
gzip -c analysis-data.sarif | base64 -w0
```

```
gzip -c analysis-data.sarif | base64 -w0
```
SARIF upload supports a maximum number of entries per the following data objects, and an analysis will be rejected if any of these objects is above its maximum value. For some objects, there are additional values over which the entries will be ignored while keeping the most important entries whenever applicable.
To get the most out of your analysis when it includes data above the supported limits, try to optimize the analysis configuration. For example, for the CodeQL tool, identify and remove the most noisy queries. For more information, see "SARIF results exceed one or more limits."

[TABLE]
SARIF data | Maximum values | Additional limits
Runs per file | 20 | 
Results per run | 25,000 | Only the top 5,000 results will be included, prioritized by severity.
Rules per run | 25,000 | 
Tool extensions per run | 100 | 
Thread Flow Locations per result | 10,000 | Only the top 1,000 Thread Flow Locations will be included, using prioritization.
Location per result | 1,000 | Only 100 locations will be included.
Tags per rule | 20 | Only 10 tags will be included.
[/TABLE]
The202 Acceptedresponse includes anidvalue.
You can use this ID to check the status of the upload by using it in the/sarifs/{sarif_id}endpoint.
For more information, see "Get information about a SARIF upload."
OAuth app tokens and personal access tokens (classic) need thesecurity_eventsscope to use this endpoint with private or public repositories, or thepublic_reposcope to use this endpoint with only public repositories.
This endpoint is limited to 1,000 requests per hour for each user or app installation calling it.

### Fine-grained access tokens for "Upload an analysis as SARIF data"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Code scanning alerts" repository permissions (write)

### Parameters for "Upload an analysis as SARIF data"

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
commit_shastringRequiredThe SHA of the commit to which the analysis you are uploading relates.
refstringRequiredThe full Git reference, formatted asrefs/heads/<branch name>,refs/tags/<tag>,refs/pull/<number>/merge, orrefs/pull/<number>/head.
sarifstringRequiredA Base64 string representing the SARIF file to upload. You must first compress your SARIF file usinggzipand then translate the contents of the file into a Base64 encoding string. For more information, see "SARIF support for code scanning."
checkout_uristringThe base directory used in the analysis, as it appears in the SARIF file.
This property is used to convert file paths from absolute to relative, so that alerts can be mapped to their correct location in the repository.
started_atstringThe time that the analysis run began. This is a timestamp inISO 8601format:YYYY-MM-DDTHH:MM:SSZ.
tool_namestringThe name of the tool used to generate the code scanning analysis. If this parameter is not used, the tool name defaults to "API". If the uploaded SARIF contains a tool GUID, this will be available for filtering using thetool_guidparameter of operations such asGET /repos/{owner}/{repo}/code-scanning/alerts.
validatebooleanWhether the SARIF file will be validated according to the code scanning specifications.
This parameter is intended to help integrators ensure that the uploaded SARIF files are correctly rendered by code scanning.
[/TABLE]
The SHA of the commit to which the analysis you are uploading relates.
The full Git reference, formatted asrefs/heads/<branch name>,refs/tags/<tag>,refs/pull/<number>/merge, orrefs/pull/<number>/head.
A Base64 string representing the SARIF file to upload. You must first compress your SARIF file usinggzipand then translate the contents of the file into a Base64 encoding string. For more information, see "SARIF support for code scanning."

```
checkout_uri
```
The base directory used in the analysis, as it appears in the SARIF file.
This property is used to convert file paths from absolute to relative, so that alerts can be mapped to their correct location in the repository.
The time that the analysis run began. This is a timestamp inISO 8601format:YYYY-MM-DDTHH:MM:SSZ.
The name of the tool used to generate the code scanning analysis. If this parameter is not used, the tool name defaults to "API". If the uploaded SARIF contains a tool GUID, this will be available for filtering using thetool_guidparameter of operations such asGET /repos/{owner}/{repo}/code-scanning/alerts.
Whether the SARIF file will be validated according to the code scanning specifications.
This parameter is intended to help integrators ensure that the uploaded SARIF files are correctly rendered by code scanning.

### HTTP response status codes for "Upload an analysis as SARIF data"

[TABLE]
Status code | Description
202 | Accepted
400 | Bad Request if the sarif field is invalid
403 | Response if the repository is archived or if GitHub Advanced Security is not enabled for this repository
404 | Resource not found
413 | Payload Too Large if the sarif field is too large
503 | Service unavailable
[/TABLE]
Accepted
Bad Request if the sarif field is invalid
Response if the repository is archived or if GitHub Advanced Security is not enabled for this repository
Resource not found
Payload Too Large if the sarif field is too large
Service unavailable

### Code samples for "Upload an analysis as SARIF data"

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
  https://api.github.com/repos/OWNER/REPO/code-scanning/sarifs \
  -d '{"commit_sha":"4b6472266afd7b471e86085a6659e8c7f2b119da","ref":"refs/heads/master","sarif":"H4sICMLGdF4AA2V4YW1wbGUuc2FyaWYAvVjdbts2FL7PUxDCijaA/CM7iRNfLkPXYgHSNstumlzQ0pHFVCI1korjFgH2ONtr7Ul2KFmy/mOn6QIkjsjDw0/nfN85NL8dEGL9pNwAImqRObECrWM1H40kXQ2XTAfJIlEgXcE1cD10RTQSVDE10K4aKSqZP1AxuKOIKg1ydJU60jSfSh8Hk6EzHA/vlOCWbfa7B6kYPpj90rlsWCZcmbHP5Bs+4oAWIjQD2SMOeJLh2vIQDnIaQerqXHjw8YIgxohybxAyDsS4cAPKsp03K4RcUs6+Up2D+JXpd8mibKIQN9fM/aMCdbyBujGSSQgVxJtx5qX2d2qUcIweQhEuDQf3GBO6CKHkogx/N3MVCKl/AeVKFuf4y5ubsMGDTj1ep+5I7sgmLIpxtU38hLtmMRGSuCFVyip5eKzs5ydh+LztVL6f2m6oih1BkYiuyQIIJWodxVpERPj4sEiWBNNH8EWT0DMG8EAjzKVHXCrB4FkPu/F64NMk1OeC+2yZSNoBOoR7CC0EzYWGbm+xFDFIzbI011+cLjfZtyJkmMZfumAh02uL3NpV2y+MZ6RAjxibyKrNxxJcVjANSb4eBGwZ1M0KsuyR2poLr5rMl8vaDSeVn6eTWEO2j2xIEcmhwlTKNOi4GMOI8gfuZYkvJ7b4v5Tiumyz7RnHeodFzpS8ASIZCH/AYdWi2z3sG8JtFxJ6fF9yR9CdifBr9Pd6d5V2+zbJKjjCFGGmsHuYFy2ytJq9tUxcLSRSQecppOGKrpUxYfxefMEFK+wOGa4hudQByBVT0L+EKtyACxnRsABhEx1QjVDs1KNI9MbpnhqfE45B6FJvu3hRu5VRU9MhZLmK7fqkKyQSTHNoyMqUFMqXCV3CwAeqEwmVokraK8IuBaGvHjQ0gMYrKjnjyw7uk9uD8tgmsBbFMPnU1bV2ZhkJNkuolUiWys3UPWzs5aaIUz9TBe8zMb+6+nT+6fLy91dlE3xzeDDT4zYszb0bW6NjJd0Rvn2EnLvWLFSdKPpBzInzfRgu8ETyMcH8nIfMnJCeC2PyfTA+UKngcnGH7Hw2hGkVQs5YlIRCtdWZYQ4/73es2JlxkfViOEIhoWJq5Oo6UBBfiKIqFBWhiE3jJGbFwVoxBHTRSuIS67sMeplei24X20shLjG+8gqbKC/bESiNMC+wd5q5id0yeS7CJEqXzmrTWNq3k05l84P6f4/bEmXFJjI0fIt1BGQssUnUDkBYeVhE5TqPnMH3jqogDcP0zKcTgLPTMSzOjhbjuVOmW23l1fYNStulfo6sXlFsGLhbDy5RECPRYGCTgOj2bd4nUQEivEd0H7KKYxqnEhFohuur3a3UPskbH/+Yg0+M5P2MHRJu3ziHh3Z2NCrWt3XF1rWTw8Ne/pfbWYXnDSE0SNZQQt1i18q7te2vOhu7ehWuvVyeu0wbLZi24mhoo6aOOTltzG/lgdVvVoXQq5V+pewkFIzL8fjEcadT55jOjpzFzHuOTtDNrMkJPMVQDd7F09RID72O/UPZ0tmctqZ7kWX6EmSZnDpP8GU67SXM8XE3YSrxbKsx6UReZ4y6n/FVZfJjs9Z7stma75W5yQtkzjk5eSJxk1lv4o7+j8TlhaJ2lsKWZO6lruDPBLib3x5ZN/KGWzZ+pn///evv7OOf4iIBv3oY9L/l1wiJ9p0Tc+F1zZnOE9NxXWEus6IQhr5pMfoqxi8WPsuu0azsns4UC6WzNzHIzbeEx4P/AJ3SefgcFAAA"}'
```

#### Default response
- Example response
- Response schema

```
Status: 202
```

```
{
  "id": "47177e22-5596-11eb-80a1-c1e54ef945c6",
  "url": "https://api.github.com/repos/octocat/hello-world/code-scanning/sarifs/47177e22-5596-11eb-80a1-c1e54ef945c6"
}
```

## Get information about a SARIF upload
Gets information about a SARIF upload, including the status and the URL of the analysis that was uploaded so that you can retrieve details of the analysis. For more information, see "Get a code scanning analysis for a repository."
OAuth app tokens and personal access tokens (classic) need thesecurity_eventsscope to use this endpoint with private or public repositories, or thepublic_reposcope to use this endpoint with only public repositories.

### Fine-grained access tokens for "Get information about a SARIF upload"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Code scanning alerts" repository permissions (read)

### Parameters for "Get information about a SARIF upload"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
sarif_idstringRequiredThe SARIF ID obtained after uploading.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.
The SARIF ID obtained after uploading.

### HTTP response status codes for "Get information about a SARIF upload"

[TABLE]
Status code | Description
200 | OK
403 | Response if GitHub Advanced Security is not enabled for this repository
404 | Not Found if the sarif id does not match any upload
503 | Service unavailable
[/TABLE]
OK
Response if GitHub Advanced Security is not enabled for this repository
Not Found if the sarif id does not match any upload
Service unavailable

### Code samples for "Get information about a SARIF upload"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/code-scanning/sarifs/SARIF_ID
```

#### Default response
- Example response
- Response schema

```
Status: 200
```

```
{
  "processing_status": "complete",
  "analyses_url": "https://api.github.com/repos/octocat/hello-world/code-scanning/analyses?sarif_id=47177e22-5596-11eb-80a1-c1e54ef945c6"
}
```