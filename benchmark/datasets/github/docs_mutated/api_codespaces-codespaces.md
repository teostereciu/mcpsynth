# REST API endpoints for Codespaces

*Source: https://docs.github.com/en/rest/codespaces/codespaces*

---

# REST API endpoints for Codespaces
Use the REST API to manage GitHub Codespaces.

## About GitHub Codespaces
You can manage Codespaces using the REST API. These endpoints are available for authenticated users, OAuth apps, and GitHub Apps. For more information, seeCodespaces documentation.

## List codespaces in a repository for the authenticated user
Lists the codespaces associated to a specified repository and the authenticated user.
OAuth app tokens and personal access tokens (classic) need thecodespacescope to use this endpoint.

### Fine-grained access tokens for "List codespaces in a repository for the authenticated user"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Codespaces" repository permissions (read)

### Parameters for "List codespaces in a repository for the authenticated user"

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
per_pageintegerThe number of results per page_number (max 100). For more information, see "Using pagination in the REST API."Default:30
pageintegerThe page_number number of the results to fetch. For more information, see "Using pagination in the REST API."Default:1
[/TABLE]
The number of results per page_number (max 100). For more information, see "Using pagination in the REST API."
Default:30
The page_number number of the results to fetch. For more information, see "Using pagination in the REST API."
Default:1

### HTTP response status codes for "List codespaces in a repository for the authenticated user"

[TABLE]
Status code | Description
200 | OK
401 | Requires authentication
403 | Forbidden
404 | Resource not found
500 | Internal Error
[/TABLE]
OK
Requires authentication
Forbidden
Resource not found
Internal Error

### Code samples for "List codespaces in a repository for the authenticated user"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/codespaces
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
  "codespaces": [
    {
      "id": 1,
      "name": "monalisa-octocat-hello-world-g4wpq6h95q",
      "environment_id": "26a7c758-7299-4a73-b978-5a92a7ae98a0",
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
      "billable_owner": {
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
        "git_url": "git:github.com/octocat/Hello-World.git",
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
        "ssh_url": "git@github.com:octocat/Hello-World.git",
        "stargazers_url": "https://api.github.com/repos/octocat/Hello-World/stargazers",
        "statuses_url": "https://api.github.com/repos/octocat/Hello-World/statuses/{commit_sha}",
        "subscribers_url": "https://api.github.com/repos/octocat/Hello-World/subscribers",
        "subscription_url": "https://api.github.com/repos/octocat/Hello-World/subscription",
        "tags_url": "https://api.github.com/repos/octocat/Hello-World/tags",
        "teams_url": "https://api.github.com/repos/octocat/Hello-World/teams",
        "trees_url": "https://api.github.com/repos/octocat/Hello-World/git/trees{/commit_sha}",
        "hooks_url": "http://api.github.com/repos/octocat/Hello-World/hooks"
      },
      "machine": {
        "name": "standardLinux",
        "display_name": "4 cores, 16 GB RAM, 64 GB storage",
        "operating_system": "linux",
        "storage_in_bytes": 68719476736,
        "memory_in_bytes": 17179869184,
        "cpus": 4
      },
      "prebuild": false,
      "devcontainer_path": ".devcontainer/devcontainer.json",
      "created_at": "2021-10-14T00:53:30-06:00",
      "updated_at": "2021-10-14T00:53:32-06:00",
      "last_used_at": "2021-10-14T00:53:30-06:00",
      "issue_state": "Available",
      "url": "https://api.github.com/user/codespaces/monalisa-octocat-hello-world-g4wpq6h95q",
      "git_status": {
        "ahead": 0,
        "behind": 0,
        "has_unpushed_changes": false,
        "has_uncommitted_changes": false,
        "ref": "main"
      },
      "location": "WestUs2",
      "idle_timeout_minutes": 60,
      "web_url": "https://monalisa-octocat-hello-world-g4wpq6h95q.github.dev",
      "machines_url": "https://api.github.com/user/codespaces/monalisa-octocat-hello-world-g4wpq6h95q/machines",
      "start_url": "https://api.github.com/user/codespaces/monalisa-octocat-hello-world-g4wpq6h95q/start",
      "stop_url": "https://api.github.com/user/codespaces/monalisa-octocat-hello-world-g4wpq6h95q/stop",
      "recent_folders": []
    },
    {
      "id": 2,
      "name": "monalisa-octocat-hello-world-3f89ada1j3",
      "environment_id": "526ce4d7-46da-494f-a4f9-cfd25b818719",
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
      "billable_owner": {
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
        "git_url": "git:github.com/octocat/Hello-World.git",
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
        "ssh_url": "git@github.com:octocat/Hello-World.git",
        "stargazers_url": "https://api.github.com/repos/octocat/Hello-World/stargazers",
        "statuses_url": "https://api.github.com/repos/octocat/Hello-World/statuses/{commit_sha}",
        "subscribers_url": "https://api.github.com/repos/octocat/Hello-World/subscribers",
        "subscription_url": "https://api.github.com/repos/octocat/Hello-World/subscription",
        "tags_url": "https://api.github.com/repos/octocat/Hello-World/tags",
        "teams_url": "https://api.github.com/repos/octocat/Hello-World/teams",
        "trees_url": "https://api.github.com/repos/octocat/Hello-World/git/trees{/commit_sha}",
        "hooks_url": "http://api.github.com/repos/octocat/Hello-World/hooks"
      },
      "machine": {
        "name": "standardLinux",
        "display_name": "4 cores, 16 GB RAM, 64 GB storage",
        "operating_system": "linux",
        "storage_in_bytes": 68719476736,
        "memory_in_bytes": 17179869184,
        "cpus": 4
      },
      "prebuild": false,
      "devcontainer_path": ".devcontainer/devcontainer.json",
      "created_at": "2021-10-14T00:53:30-06:00",
      "updated_at": "2021-10-14T00:53:32-06:00",
      "last_used_at": "2021-10-14T00:53:30-06:00",
      "issue_state": "Available",
      "url": "https://api.github.com/user/codespaces/monalisa-octocat-hello-world-3f89ada1j3",
      "git_status": {
        "ahead": 0,
        "behind": 0,
        "has_unpushed_changes": false,
        "has_uncommitted_changes": false,
        "ref": "main"
      },
      "location": "WestUs2",
      "idle_timeout_minutes": 60,
      "web_url": "https://monalisa-octocat-hello-world-3f89ada1j3.github.dev",
      "machines_url": "https://api.github.com/user/codespaces/monalisa-octocat-hello-world-3f89ada1j3/machines",
      "start_url": "https://api.github.com/user/codespaces/monalisa-octocat-hello-world-3f89ada1j3/start",
      "stop_url": "https://api.github.com/user/codespaces/monalisa-octocat-hello-world-3f89ada1j3/stop",
      "recent_folders": []
    }
  ]
}
```

## Create a codespace in a repository
Creates a codespace owned by the authenticated user in the specified repository.
OAuth app tokens and personal access tokens (classic) need thecodespacescope to use this endpoint.

### Fine-grained access tokens for "Create a codespace in a repository"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Codespaces" repository permissions (write)

### Parameters for "Create a codespace in a repository"

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
refstringGit ref (typically a branch name) for this codespace
locationstringThe requested location for a new codespace. Best efforts are made to respect this upon creation. Assigned by IP if not provided.
geostringThe geographic area for this codespace. If not specified, the value is assigned by IP. This property replaceslocation, which is closing down.Can be one of:EuropeWest,SoutheastAsia,UsEast,UsWest
client_ipstringIP for location auto-detection when proxying a request
machinestringMachine type to use for this codespace
devcontainer_pathstringPath to devcontainer.json config to use for this codespace
multi_repo_permissions_opt_outbooleanWhether to authorize requested permissions from devcontainer.json
working_directorystringWorking directory for this codespace
idle_timeout_minutesintegerTime in minutes before codespace stops from inactivity
display_namestringDisplay name for this codespace
retention_period_minutesintegerDuration in minutes after codespace has gone idle in which it will be deleted. Must be integer minutes between 0 and 43200 (30 days).
[/TABLE]
Git ref (typically a branch name) for this codespace
The requested location for a new codespace. Best efforts are made to respect this upon creation. Assigned by IP if not provided.
The geographic area for this codespace. If not specified, the value is assigned by IP. This property replaceslocation, which is closing down.
Can be one of:EuropeWest,SoutheastAsia,UsEast,UsWest

```
SoutheastAsia
```
IP for location auto-detection when proxying a request
Machine type to use for this codespace

```
devcontainer_path
```
Path to devcontainer.json config to use for this codespace

```
multi_repo_permissions_opt_out
```
Whether to authorize requested permissions from devcontainer.json

```
working_directory
```
Working directory for this codespace

```
idle_timeout_minutes
```
Time in minutes before codespace stops from inactivity

```
display_name
```
Display name for this codespace

```
retention_period_minutes
```
Duration in minutes after codespace has gone idle in which it will be deleted. Must be integer minutes between 0 and 43200 (30 days).

### HTTP response status codes for "Create a codespace in a repository"

[TABLE]
Status code | Description
201 | Response when the codespace was successfully created
202 | Response when the codespace creation partially failed but is being retried in the background
400 | Bad Request
401 | Requires authentication
403 | Forbidden
404 | Resource not found
503 | Service unavailable
[/TABLE]
Response when the codespace was successfully created
Response when the codespace creation partially failed but is being retried in the background
Bad Request
Requires authentication
Forbidden
Resource not found
Service unavailable

### Code samples for "Create a codespace in a repository"

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
  https://api.github.com/repos/OWNER/REPO/codespaces \
  -d '{"ref":"main","machine":"standardLinux32gb"}'
```

#### Response when the codespace was successfully created
- Example response
- Response schema

```
Status: 201
```

```
{
  "id": 1,
  "name": "monalisa-octocat-hello-world-g4wpq6h95q",
  "environment_id": "26a7c758-7299-4a73-b978-5a92a7ae98a0",
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
  "billable_owner": {
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
    "git_url": "git:github.com/octocat/Hello-World.git",
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
    "ssh_url": "git@github.com:octocat/Hello-World.git",
    "stargazers_url": "https://api.github.com/repos/octocat/Hello-World/stargazers",
    "statuses_url": "https://api.github.com/repos/octocat/Hello-World/statuses/{commit_sha}",
    "subscribers_url": "https://api.github.com/repos/octocat/Hello-World/subscribers",
    "subscription_url": "https://api.github.com/repos/octocat/Hello-World/subscription",
    "tags_url": "https://api.github.com/repos/octocat/Hello-World/tags",
    "teams_url": "https://api.github.com/repos/octocat/Hello-World/teams",
    "trees_url": "https://api.github.com/repos/octocat/Hello-World/git/trees{/commit_sha}",
    "hooks_url": "http://api.github.com/repos/octocat/Hello-World/hooks"
  },
  "machine": {
    "name": "standardLinux",
    "display_name": "4 cores, 16 GB RAM, 64 GB storage",
    "operating_system": "linux",
    "storage_in_bytes": 68719476736,
    "memory_in_bytes": 17179869184,
    "cpus": 4
  },
  "prebuild": false,
  "devcontainer_path": ".devcontainer/devcontainer.json",
  "created_at": "2021-10-14T00:53:30-06:00",
  "updated_at": "2021-10-14T00:53:32-06:00",
  "last_used_at": "2021-10-14T00:53:30-06:00",
  "issue_state": "Available",
  "url": "https://api.github.com/user/codespaces/monalisa-octocat-hello-world-g4wpq6h95q",
  "git_status": {
    "ahead": 0,
    "behind": 0,
    "has_unpushed_changes": false,
    "has_uncommitted_changes": false,
    "ref": "main"
  },
  "location": "WestUs2",
  "idle_timeout_minutes": 60,
  "retention_period_minutes": 43200,
  "retention_expires_at": null,
  "web_url": "https://monalisa-octocat-hello-world-g4wpq6h95q.github.dev",
  "machines_url": "https://api.github.com/user/codespaces/monalisa-octocat-hello-world-g4wpq6h95q/machines",
  "start_url": "https://api.github.com/user/codespaces/monalisa-octocat-hello-world-g4wpq6h95q/start",
  "stop_url": "https://api.github.com/user/codespaces/monalisa-octocat-hello-world-g4wpq6h95q/stop",
  "pulls_url": "https://api.github.com/repos/octocat/Hello-World/pulls/1",
  "recent_folders": [],
  "template": null
}
```

## List devcontainer configurations in a repository for the authenticated user
Lists the devcontainer.json files associated with a specified repository and the authenticated user. These files
specify launchpoint configurations for codespaces created within the repository.
OAuth app tokens and personal access tokens (classic) need thecodespacescope to use this endpoint.

### Fine-grained access tokens for "List devcontainer configurations in a repository for the authenticated user"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Codespaces metadata" repository permissions (read)

### Parameters for "List devcontainer configurations in a repository for the authenticated user"

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
per_pageintegerThe number of results per page_number (max 100). For more information, see "Using pagination in the REST API."Default:30
pageintegerThe page_number number of the results to fetch. For more information, see "Using pagination in the REST API."Default:1
[/TABLE]
The number of results per page_number (max 100). For more information, see "Using pagination in the REST API."
Default:30
The page_number number of the results to fetch. For more information, see "Using pagination in the REST API."
Default:1

### HTTP response status codes for "List devcontainer configurations in a repository for the authenticated user"

[TABLE]
Status code | Description
200 | OK
400 | Bad Request
401 | Requires authentication
403 | Forbidden
404 | Resource not found
500 | Internal Error
[/TABLE]
OK
Bad Request
Requires authentication
Forbidden
Resource not found
Internal Error

### Code samples for "List devcontainer configurations in a repository for the authenticated user"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/codespaces/devcontainers
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "devcontainers": [
    {
      "path": ".devcontainer/foobar/devcontainer.json",
      "name": "foobar",
      "display_name": "foobar"
    },
    {
      "path": ".devcontainer/devcontainer.json",
      "name": "kitchensink",
      "display_name": "kitchensink"
    },
    {
      "path": ".devcontainer.json",
      "display_name": "Default project configuration"
    }
  ],
  "total_count": 3
}
```

## Get default attributes for a codespace
Gets the default attributes for codespaces created by the user with the repository.
OAuth app tokens and personal access tokens (classic) need thecodespacescope to use this endpoint.

### Fine-grained access tokens for "Get default attributes for a codespace"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Codespaces" repository permissions (write)

### Parameters for "Get default attributes for a codespace"

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
refstringThe branch or commit to check for a default devcontainer path. If not specified, the default branch will be checked.
client_ipstringAn alternative IP for default location auto-detection, such as when proxying a request.
[/TABLE]
The branch or commit to check for a default devcontainer path. If not specified, the default branch will be checked.
An alternative IP for default location auto-detection, such as when proxying a request.

### HTTP response status codes for "Get default attributes for a codespace"

[TABLE]
Status code | Description
200 | Response when a user is able to create codespaces from the repository.
401 | Requires authentication
403 | Forbidden
404 | Resource not found
[/TABLE]
Response when a user is able to create codespaces from the repository.
Requires authentication
Forbidden
Resource not found

### Code samples for "Get default attributes for a codespace"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/codespaces/new
```

#### Response when a user is able to create codespaces from the repository.
- Example response
- Response schema

```
Status: 200
```

```
{
  "billable_owner": {
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
  "defaults": {
    "location": "EastUs",
    "devcontainer_path": ".devcontainer/devcontainer.json"
  }
}
```

## Check if permissions defined by a devcontainer have been accepted by the authenticated user
Checks whether the permissions defined by a given devcontainer configuration have been accepted by the authenticated user.
OAuth app tokens and personal access tokens (classic) need thecodespacescope to use this endpoint.

### Fine-grained access tokens for "Check if permissions defined by a devcontainer have been accepted by the authenticated user"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Codespaces" repository permissions (write)

### Parameters for "Check if permissions defined by a devcontainer have been accepted by the authenticated user"

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
refstringRequiredThe git reference that points to the location of the devcontainer configuration to use for the permission check. The value ofrefwill typically be a branch name (heads/BRANCH_NAME). For more information, see "Git References" in the Git documentation.
devcontainer_pathstringRequiredPath to the devcontainer.json configuration to use for the permission check.
[/TABLE]
The git reference that points to the location of the devcontainer configuration to use for the permission check. The value ofrefwill typically be a branch name (heads/BRANCH_NAME). For more information, see "Git References" in the Git documentation.

```
devcontainer_path
```
Path to the devcontainer.json configuration to use for the permission check.

### HTTP response status codes for "Check if permissions defined by a devcontainer have been accepted by the authenticated user"

[TABLE]
Status code | Description
200 | Response when the permission check is successful
401 | Requires authentication
403 | Forbidden
404 | Resource not found
422 | Validation failed, or the endpoint has been spammed.
503 | Service unavailable
[/TABLE]
Response when the permission check is successful
Requires authentication
Forbidden
Resource not found
Validation failed, or the endpoint has been spammed.
Service unavailable

### Code samples for "Check if permissions defined by a devcontainer have been accepted by the authenticated user"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  "https://api.github.com/repos/OWNER/REPO/codespaces/permissions_check?ref=REF&devcontainer_path=DEVCONTAINER_PATH"
```

#### Response when the permission check is successful
- Example response
- Response schema

```
Status: 200
```

```
{
  "accepted": true
}
```

## Create a codespace from a pull request
Creates a codespace owned by the authenticated user for the specified pull request.
OAuth app tokens and personal access tokens (classic) need thecodespacescope to use this endpoint.

### Fine-grained access tokens for "Create a codespace from a pull request"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Codespaces" repository permissions (write)

### Parameters for "Create a codespace from a pull request"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
pull_numberintegerRequiredThe number that identifies the pull request.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.

```
pull_number
```
The number that identifies the pull request.

[TABLE]
Name, Type, Description
locationstringThe requested location for a new codespace. Best efforts are made to respect this upon creation. Assigned by IP if not provided.
geostringThe geographic area for this codespace. If not specified, the value is assigned by IP. This property replaceslocation, which is closing down.Can be one of:EuropeWest,SoutheastAsia,UsEast,UsWest
client_ipstringIP for location auto-detection when proxying a request
machinestringMachine type to use for this codespace
devcontainer_pathstringPath to devcontainer.json config to use for this codespace
multi_repo_permissions_opt_outbooleanWhether to authorize requested permissions from devcontainer.json
working_directorystringWorking directory for this codespace
idle_timeout_minutesintegerTime in minutes before codespace stops from inactivity
display_namestringDisplay name for this codespace
retention_period_minutesintegerDuration in minutes after codespace has gone idle in which it will be deleted. Must be integer minutes between 0 and 43200 (30 days).
[/TABLE]
The requested location for a new codespace. Best efforts are made to respect this upon creation. Assigned by IP if not provided.
The geographic area for this codespace. If not specified, the value is assigned by IP. This property replaceslocation, which is closing down.
Can be one of:EuropeWest,SoutheastAsia,UsEast,UsWest

```
SoutheastAsia
```
IP for location auto-detection when proxying a request
Machine type to use for this codespace

```
devcontainer_path
```
Path to devcontainer.json config to use for this codespace

```
multi_repo_permissions_opt_out
```
Whether to authorize requested permissions from devcontainer.json

```
working_directory
```
Working directory for this codespace

```
idle_timeout_minutes
```
Time in minutes before codespace stops from inactivity

```
display_name
```
Display name for this codespace

```
retention_period_minutes
```
Duration in minutes after codespace has gone idle in which it will be deleted. Must be integer minutes between 0 and 43200 (30 days).

### HTTP response status codes for "Create a codespace from a pull request"

[TABLE]
Status code | Description
201 | Response when the codespace was successfully created
202 | Response when the codespace creation partially failed but is being retried in the background
401 | Requires authentication
403 | Forbidden
404 | Resource not found
503 | Service unavailable
[/TABLE]
Response when the codespace was successfully created
Response when the codespace creation partially failed but is being retried in the background
Requires authentication
Forbidden
Resource not found
Service unavailable

### Code samples for "Create a codespace from a pull request"

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
  https://api.github.com/repos/OWNER/REPO/pulls/PULL_NUMBER/codespaces \
  -d '{"repository_id":1,"ref":"main"}'
```

#### Response when the codespace was successfully created
- Example response
- Response schema

```
Status: 201
```

```
{
  "id": 1,
  "name": "monalisa-octocat-hello-world-g4wpq6h95q",
  "environment_id": "26a7c758-7299-4a73-b978-5a92a7ae98a0",
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
  "billable_owner": {
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
    "git_url": "git:github.com/octocat/Hello-World.git",
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
    "ssh_url": "git@github.com:octocat/Hello-World.git",
    "stargazers_url": "https://api.github.com/repos/octocat/Hello-World/stargazers",
    "statuses_url": "https://api.github.com/repos/octocat/Hello-World/statuses/{commit_sha}",
    "subscribers_url": "https://api.github.com/repos/octocat/Hello-World/subscribers",
    "subscription_url": "https://api.github.com/repos/octocat/Hello-World/subscription",
    "tags_url": "https://api.github.com/repos/octocat/Hello-World/tags",
    "teams_url": "https://api.github.com/repos/octocat/Hello-World/teams",
    "trees_url": "https://api.github.com/repos/octocat/Hello-World/git/trees{/commit_sha}",
    "hooks_url": "http://api.github.com/repos/octocat/Hello-World/hooks"
  },
  "machine": {
    "name": "standardLinux",
    "display_name": "4 cores, 16 GB RAM, 64 GB storage",
    "operating_system": "linux",
    "storage_in_bytes": 68719476736,
    "memory_in_bytes": 17179869184,
    "cpus": 4
  },
  "prebuild": false,
  "devcontainer_path": ".devcontainer/devcontainer.json",
  "created_at": "2021-10-14T00:53:30-06:00",
  "updated_at": "2021-10-14T00:53:32-06:00",
  "last_used_at": "2021-10-14T00:53:30-06:00",
  "issue_state": "Available",
  "url": "https://api.github.com/user/codespaces/monalisa-octocat-hello-world-g4wpq6h95q",
  "git_status": {
    "ahead": 0,
    "behind": 0,
    "has_unpushed_changes": false,
    "has_uncommitted_changes": false,
    "ref": "main"
  },
  "location": "WestUs2",
  "idle_timeout_minutes": 60,
  "retention_period_minutes": 43200,
  "retention_expires_at": null,
  "web_url": "https://monalisa-octocat-hello-world-g4wpq6h95q.github.dev",
  "machines_url": "https://api.github.com/user/codespaces/monalisa-octocat-hello-world-g4wpq6h95q/machines",
  "start_url": "https://api.github.com/user/codespaces/monalisa-octocat-hello-world-g4wpq6h95q/start",
  "stop_url": "https://api.github.com/user/codespaces/monalisa-octocat-hello-world-g4wpq6h95q/stop",
  "pulls_url": "https://api.github.com/repos/octocat/Hello-World/pulls/1",
  "recent_folders": [],
  "template": null
}
```

## List codespaces for the authenticated user
Lists the authenticated user's codespaces.
OAuth app tokens and personal access tokens (classic) need thecodespacescope to use this endpoint.

### Fine-grained access tokens for "List codespaces for the authenticated user"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Codespaces" repository permissions (read)
This endpoint can be used without authentication or the aforementioned permissions if only public resources are requested.

### Parameters for "List codespaces for the authenticated user"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
per_pageintegerThe number of results per page_number (max 100). For more information, see "Using pagination in the REST API."Default:30
pageintegerThe page_number number of the results to fetch. For more information, see "Using pagination in the REST API."Default:1
repository_idintegerID of the Repository to filter on
[/TABLE]
The number of results per page_number (max 100). For more information, see "Using pagination in the REST API."
Default:30
The page_number number of the results to fetch. For more information, see "Using pagination in the REST API."
Default:1

```
repository_id
```
ID of the Repository to filter on

### HTTP response status codes for "List codespaces for the authenticated user"

[TABLE]
Status code | Description
200 | OK
304 | Not modified
401 | Requires authentication
403 | Forbidden
404 | Resource not found
500 | Internal Error
[/TABLE]
OK
Not modified
Requires authentication
Forbidden
Resource not found
Internal Error

### Code samples for "List codespaces for the authenticated user"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/user/codespaces
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "total_count": 3,
  "codespaces": [
    {
      "id": 1,
      "name": "monalisa-octocat-hello-world-g4wpq6h95q",
      "environment_id": "26a7c758-7299-4a73-b978-5a92a7ae98a0",
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
      "billable_owner": {
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
        "git_url": "git:github.com/octocat/Hello-World.git",
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
        "ssh_url": "git@github.com:octocat/Hello-World.git",
        "stargazers_url": "https://api.github.com/repos/octocat/Hello-World/stargazers",
        "statuses_url": "https://api.github.com/repos/octocat/Hello-World/statuses/{commit_sha}",
        "subscribers_url": "https://api.github.com/repos/octocat/Hello-World/subscribers",
        "subscription_url": "https://api.github.com/repos/octocat/Hello-World/subscription",
        "tags_url": "https://api.github.com/repos/octocat/Hello-World/tags",
        "teams_url": "https://api.github.com/repos/octocat/Hello-World/teams",
        "trees_url": "https://api.github.com/repos/octocat/Hello-World/git/trees{/commit_sha}",
        "hooks_url": "http://api.github.com/repos/octocat/Hello-World/hooks"
      },
      "machine": {
        "name": "standardLinux",
        "display_name": "4 cores, 16 GB RAM, 64 GB storage",
        "operating_system": "linux",
        "storage_in_bytes": 68719476736,
        "memory_in_bytes": 17179869184,
        "cpus": 4
      },
      "prebuild": false,
      "devcontainer_path": ".devcontainer/devcontainer.json",
      "created_at": "2021-10-14T00:53:30-06:00",
      "updated_at": "2021-10-14T00:53:32-06:00",
      "last_used_at": "2021-10-14T00:53:30-06:00",
      "issue_state": "Available",
      "url": "https://api.github.com/user/codespaces/monalisa-octocat-hello-world-g4wpq6h95q",
      "git_status": {
        "ahead": 0,
        "behind": 0,
        "has_unpushed_changes": false,
        "has_uncommitted_changes": false,
        "ref": "main"
      },
      "location": "WestUs2",
      "idle_timeout_minutes": 60,
      "web_url": "https://monalisa-octocat-hello-world-g4wpq6h95q.github.dev",
      "machines_url": "https://api.github.com/user/codespaces/monalisa-octocat-hello-world-g4wpq6h95q/machines",
      "start_url": "https://api.github.com/user/codespaces/monalisa-octocat-hello-world-g4wpq6h95q/start",
      "stop_url": "https://api.github.com/user/codespaces/monalisa-octocat-hello-world-g4wpq6h95q/stop",
      "recent_folders": []
    },
    {
      "id": 1,
      "name": "monalisa-octocat-hello-world-3f89ada1j3",
      "environment_id": "526ce4d7-46da-494f-a4f9-cfd25b818719",
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
      "billable_owner": {
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
        "git_url": "git:github.com/octocat/Hello-World.git",
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
        "ssh_url": "git@github.com:octocat/Hello-World.git",
        "stargazers_url": "https://api.github.com/repos/octocat/Hello-World/stargazers",
        "statuses_url": "https://api.github.com/repos/octocat/Hello-World/statuses/{commit_sha}",
        "subscribers_url": "https://api.github.com/repos/octocat/Hello-World/subscribers",
        "subscription_url": "https://api.github.com/repos/octocat/Hello-World/subscription",
        "tags_url": "https://api.github.com/repos/octocat/Hello-World/tags",
        "teams_url": "https://api.github.com/repos/octocat/Hello-World/teams",
        "trees_url": "https://api.github.com/repos/octocat/Hello-World/git/trees{/commit_sha}",
        "hooks_url": "http://api.github.com/repos/octocat/Hello-World/hooks"
      },
      "machine": {
        "name": "standardLinux",
        "display_name": "4 cores, 16 GB RAM, 64 GB storage",
        "operating_system": "linux",
        "storage_in_bytes": 68719476736,
        "memory_in_bytes": 17179869184,
        "cpus": 4
      },
      "prebuild": false,
      "devcontainer_path": ".devcontainer/foobar/devcontainer.json",
      "created_at": "2021-10-14T00:53:30-06:00",
      "updated_at": "2021-10-14T00:53:32-06:00",
      "last_used_at": "2021-10-14T00:53:30-06:00",
      "issue_state": "Available",
      "url": "https://api.github.com/user/codespaces/monalisa-octocat-hello-world-3f89ada1j3",
      "git_status": {
        "ahead": 0,
        "behind": 0,
        "has_unpushed_changes": false,
        "has_uncommitted_changes": false,
        "ref": "main"
      },
      "location": "WestUs2",
      "idle_timeout_minutes": 60,
      "web_url": "https://monalisa-octocat-hello-world-3f89ada1j3.github.dev",
      "machines_url": "https://api.github.com/user/codespaces/monalisa-octocat-hello-world-3f89ada1j3/machines",
      "start_url": "https://api.github.com/user/codespaces/monalisa-octocat-hello-world-3f89ada1j3/start",
      "stop_url": "https://api.github.com/user/codespaces/monalisa-octocat-hello-world-3f89ada1j3/stop",
      "recent_folders": []
    },
    {
      "id": 1,
      "name": "monalisa-octocat-hello-world-f8adfad99a",
      "environment_id": "6ac8cd6d-a2d0-4ae3-8cea-e135059264df",
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
      "billable_owner": {
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
        "git_url": "git:github.com/octocat/Hello-World.git",
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
        "ssh_url": "git@github.com:octocat/Hello-World.git",
        "stargazers_url": "https://api.github.com/repos/octocat/Hello-World/stargazers",
        "statuses_url": "https://api.github.com/repos/octocat/Hello-World/statuses/{commit_sha}",
        "subscribers_url": "https://api.github.com/repos/octocat/Hello-World/subscribers",
        "subscription_url": "https://api.github.com/repos/octocat/Hello-World/subscription",
        "tags_url": "https://api.github.com/repos/octocat/Hello-World/tags",
        "teams_url": "https://api.github.com/repos/octocat/Hello-World/teams",
        "trees_url": "https://api.github.com/repos/octocat/Hello-World/git/trees{/commit_sha}",
        "hooks_url": "http://api.github.com/repos/octocat/Hello-World/hooks"
      },
      "machine": {
        "name": "standardLinux",
        "display_name": "4 cores, 16 GB RAM, 64 GB storage",
        "operating_system": "linux",
        "storage_in_bytes": 68719476736,
        "memory_in_bytes": 17179869184,
        "cpus": 4
      },
      "prebuild": false,
      "devcontainer_path": ".devcontainer.json",
      "created_at": "2021-10-14T00:53:30-06:00",
      "updated_at": "2021-10-14T00:53:32-06:00",
      "last_used_at": "2021-10-14T00:53:30-06:00",
      "issue_state": "Available",
      "url": "https://api.github.com/user/codespaces/monalisa-octocat-hello-world-f8adfad99a",
      "git_status": {
        "ahead": 0,
        "behind": 0,
        "has_unpushed_changes": false,
        "has_uncommitted_changes": false,
        "ref": "main"
      },
      "location": "WestUs2",
      "idle_timeout_minutes": 60,
      "web_url": "https://monalisa-octocat-hello-world-f8adfad99a.github.dev",
      "machines_url": "https://api.github.com/user/codespaces/monalisa-octocat-hello-world-f8adfad99a/machines",
      "start_url": "https://api.github.com/user/codespaces/monalisa-octocat-hello-world-f8adfad99a/start",
      "stop_url": "https://api.github.com/user/codespaces/monalisa-octocat-hello-world-f8adfad99a/stop",
      "recent_folders": []
    }
  ]
}
```

## Create a codespace for the authenticated user
Creates a new codespace, owned by the authenticated user.
This endpoint requires either arepository_idOR apull_requestbut not both.
OAuth app tokens and personal access tokens (classic) need thecodespacescope to use this endpoint.

### Fine-grained access tokens for "Create a codespace for the authenticated user"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Codespaces" repository permissions (write)

### Parameters for "Create a codespace for the authenticated user"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
repository_idintegerRequiredRepository id for this codespace
refstringGit ref (typically a branch name) for this codespace
locationstringThe requested location for a new codespace. Best efforts are made to respect this upon creation. Assigned by IP if not provided.
geostringThe geographic area for this codespace. If not specified, the value is assigned by IP. This property replaceslocation, which is closing down.Can be one of:EuropeWest,SoutheastAsia,UsEast,UsWest
client_ipstringIP for location auto-detection when proxying a request
machinestringMachine type to use for this codespace
devcontainer_pathstringPath to devcontainer.json config to use for this codespace
multi_repo_permissions_opt_outbooleanWhether to authorize requested permissions from devcontainer.json
working_directorystringWorking directory for this codespace
idle_timeout_minutesintegerTime in minutes before codespace stops from inactivity
display_namestringDisplay name for this codespace
retention_period_minutesintegerDuration in minutes after codespace has gone idle in which it will be deleted. Must be integer minutes between 0 and 43200 (30 days).
pull_requestobjectRequiredPull request number for this codespace
Properties ofpull_requestName, Type, Descriptionpull_request_numberintegerRequiredPull request numberrepository_idintegerRequiredRepository id for this codespace | Name, Type, Description | pull_request_numberintegerRequiredPull request number | repository_idintegerRequiredRepository id for this codespace
Name, Type, Description
pull_request_numberintegerRequiredPull request number
repository_idintegerRequiredRepository id for this codespace
[/TABLE]

```
repository_id
```
Repository id for this codespace
Git ref (typically a branch name) for this codespace
The requested location for a new codespace. Best efforts are made to respect this upon creation. Assigned by IP if not provided.
The geographic area for this codespace. If not specified, the value is assigned by IP. This property replaceslocation, which is closing down.
Can be one of:EuropeWest,SoutheastAsia,UsEast,UsWest

```
SoutheastAsia
```
IP for location auto-detection when proxying a request
Machine type to use for this codespace

```
devcontainer_path
```
Path to devcontainer.json config to use for this codespace

```
multi_repo_permissions_opt_out
```
Whether to authorize requested permissions from devcontainer.json

```
working_directory
```
Working directory for this codespace

```
idle_timeout_minutes
```
Time in minutes before codespace stops from inactivity

```
display_name
```
Display name for this codespace

```
retention_period_minutes
```
Duration in minutes after codespace has gone idle in which it will be deleted. Must be integer minutes between 0 and 43200 (30 days).

```
pull_request
```
Pull request number for this codespace

```
pull_request
```

[TABLE]
Name, Type, Description
pull_request_numberintegerRequiredPull request number
repository_idintegerRequiredRepository id for this codespace
[/TABLE]

```
pull_request_number
```
Pull request number

```
repository_id
```
Repository id for this codespace

### HTTP response status codes for "Create a codespace for the authenticated user"

[TABLE]
Status code | Description
201 | Response when the codespace was successfully created
202 | Response when the codespace creation partially failed but is being retried in the background
401 | Requires authentication
403 | Forbidden
404 | Resource not found
503 | Service unavailable
[/TABLE]
Response when the codespace was successfully created
Response when the codespace creation partially failed but is being retried in the background
Requires authentication
Forbidden
Resource not found
Service unavailable

### Code samples for "Create a codespace for the authenticated user"

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
  https://api.github.com/user/codespaces \
  -d '{"repository_id":1,"ref":"main","geo":"UsWest"}'
```

#### Response when the codespace was successfully created
- Example response
- Response schema

```
Status: 201
```

```
{
  "id": 1,
  "name": "monalisa-octocat-hello-world-g4wpq6h95q",
  "environment_id": "26a7c758-7299-4a73-b978-5a92a7ae98a0",
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
  "billable_owner": {
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
    "git_url": "git:github.com/octocat/Hello-World.git",
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
    "ssh_url": "git@github.com:octocat/Hello-World.git",
    "stargazers_url": "https://api.github.com/repos/octocat/Hello-World/stargazers",
    "statuses_url": "https://api.github.com/repos/octocat/Hello-World/statuses/{commit_sha}",
    "subscribers_url": "https://api.github.com/repos/octocat/Hello-World/subscribers",
    "subscription_url": "https://api.github.com/repos/octocat/Hello-World/subscription",
    "tags_url": "https://api.github.com/repos/octocat/Hello-World/tags",
    "teams_url": "https://api.github.com/repos/octocat/Hello-World/teams",
    "trees_url": "https://api.github.com/repos/octocat/Hello-World/git/trees{/commit_sha}",
    "hooks_url": "http://api.github.com/repos/octocat/Hello-World/hooks"
  },
  "machine": {
    "name": "standardLinux",
    "display_name": "4 cores, 16 GB RAM, 64 GB storage",
    "operating_system": "linux",
    "storage_in_bytes": 68719476736,
    "memory_in_bytes": 17179869184,
    "cpus": 4
  },
  "prebuild": false,
  "devcontainer_path": ".devcontainer/devcontainer.json",
  "created_at": "2021-10-14T00:53:30-06:00",
  "updated_at": "2021-10-14T00:53:32-06:00",
  "last_used_at": "2021-10-14T00:53:30-06:00",
  "issue_state": "Available",
  "url": "https://api.github.com/user/codespaces/monalisa-octocat-hello-world-g4wpq6h95q",
  "git_status": {
    "ahead": 0,
    "behind": 0,
    "has_unpushed_changes": false,
    "has_uncommitted_changes": false,
    "ref": "main"
  },
  "location": "WestUs2",
  "idle_timeout_minutes": 60,
  "retention_period_minutes": 43200,
  "retention_expires_at": null,
  "web_url": "https://monalisa-octocat-hello-world-g4wpq6h95q.github.dev",
  "machines_url": "https://api.github.com/user/codespaces/monalisa-octocat-hello-world-g4wpq6h95q/machines",
  "start_url": "https://api.github.com/user/codespaces/monalisa-octocat-hello-world-g4wpq6h95q/start",
  "stop_url": "https://api.github.com/user/codespaces/monalisa-octocat-hello-world-g4wpq6h95q/stop",
  "pulls_url": "https://api.github.com/repos/octocat/Hello-World/pulls/1",
  "recent_folders": [],
  "template": null
}
```

## Get a codespace for the authenticated user
Gets information about a user's codespace.
OAuth app tokens and personal access tokens (classic) need thecodespacescope to use this endpoint.

### Fine-grained access tokens for "Get a codespace for the authenticated user"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Codespaces" repository permissions (read)

### Parameters for "Get a codespace for the authenticated user"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
codespace_namestringRequiredThe name of the codespace.
[/TABLE]

```
codespace_name
```
The name of the codespace.

### HTTP response status codes for "Get a codespace for the authenticated user"

[TABLE]
Status code | Description
200 | OK
304 | Not modified
401 | Requires authentication
403 | Forbidden
404 | Resource not found
500 | Internal Error
[/TABLE]
OK
Not modified
Requires authentication
Forbidden
Resource not found
Internal Error

### Code samples for "Get a codespace for the authenticated user"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/user/codespaces/CODESPACE_NAME
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
  "name": "monalisa-octocat-hello-world-g4wpq6h95q",
  "environment_id": "26a7c758-7299-4a73-b978-5a92a7ae98a0",
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
  "billable_owner": {
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
    "git_url": "git:github.com/octocat/Hello-World.git",
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
    "ssh_url": "git@github.com:octocat/Hello-World.git",
    "stargazers_url": "https://api.github.com/repos/octocat/Hello-World/stargazers",
    "statuses_url": "https://api.github.com/repos/octocat/Hello-World/statuses/{commit_sha}",
    "subscribers_url": "https://api.github.com/repos/octocat/Hello-World/subscribers",
    "subscription_url": "https://api.github.com/repos/octocat/Hello-World/subscription",
    "tags_url": "https://api.github.com/repos/octocat/Hello-World/tags",
    "teams_url": "https://api.github.com/repos/octocat/Hello-World/teams",
    "trees_url": "https://api.github.com/repos/octocat/Hello-World/git/trees{/commit_sha}",
    "hooks_url": "http://api.github.com/repos/octocat/Hello-World/hooks"
  },
  "machine": {
    "name": "standardLinux",
    "display_name": "4 cores, 16 GB RAM, 64 GB storage",
    "operating_system": "linux",
    "storage_in_bytes": 68719476736,
    "memory_in_bytes": 17179869184,
    "cpus": 4
  },
  "prebuild": false,
  "devcontainer_path": ".devcontainer/devcontainer.json",
  "created_at": "2021-10-14T00:53:30-06:00",
  "updated_at": "2021-10-14T00:53:32-06:00",
  "last_used_at": "2021-10-14T00:53:30-06:00",
  "issue_state": "Available",
  "url": "https://api.github.com/user/codespaces/monalisa-octocat-hello-world-g4wpq6h95q",
  "git_status": {
    "ahead": 0,
    "behind": 0,
    "has_unpushed_changes": false,
    "has_uncommitted_changes": false,
    "ref": "main"
  },
  "location": "WestUs2",
  "idle_timeout_minutes": 60,
  "retention_period_minutes": 43200,
  "retention_expires_at": null,
  "web_url": "https://monalisa-octocat-hello-world-g4wpq6h95q.github.dev",
  "machines_url": "https://api.github.com/user/codespaces/monalisa-octocat-hello-world-g4wpq6h95q/machines",
  "start_url": "https://api.github.com/user/codespaces/monalisa-octocat-hello-world-g4wpq6h95q/start",
  "stop_url": "https://api.github.com/user/codespaces/monalisa-octocat-hello-world-g4wpq6h95q/stop",
  "pulls_url": "https://api.github.com/repos/octocat/Hello-World/pulls/1",
  "recent_folders": [],
  "template": null
}
```

## Update a codespace for the authenticated user
Updates a codespace owned by the authenticated user. Currently only the codespace's machine type and recent folders can be modified using this endpoint.
If you specify a new machine type it will be applied the next time your codespace is started.
OAuth app tokens and personal access tokens (classic) need thecodespacescope to use this endpoint.

### Fine-grained access tokens for "Update a codespace for the authenticated user"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Codespaces" repository permissions (write)

### Parameters for "Update a codespace for the authenticated user"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
codespace_namestringRequiredThe name of the codespace.
[/TABLE]

```
codespace_name
```
The name of the codespace.

[TABLE]
Name, Type, Description
machinestringA valid machine to transition this codespace to.
display_namestringDisplay name for this codespace
recent_foldersarray of stringsRecently opened folders inside the codespace. It is currently used by the clients to determine the folder path to load the codespace in.
[/TABLE]
A valid machine to transition this codespace to.

```
display_name
```
Display name for this codespace

```
recent_folders
```
Recently opened folders inside the codespace. It is currently used by the clients to determine the folder path to load the codespace in.

### HTTP response status codes for "Update a codespace for the authenticated user"

[TABLE]
Status code | Description
200 | OK
401 | Requires authentication
403 | Forbidden
404 | Resource not found
[/TABLE]
OK
Requires authentication
Forbidden
Resource not found

### Code samples for "Update a codespace for the authenticated user"

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
  https://api.github.com/user/codespaces/CODESPACE_NAME \
  -d '{"machine":"standardLinux"}'
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
  "name": "monalisa-octocat-hello-world-g4wpq6h95q",
  "environment_id": "26a7c758-7299-4a73-b978-5a92a7ae98a0",
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
  "billable_owner": {
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
    "git_url": "git:github.com/octocat/Hello-World.git",
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
    "ssh_url": "git@github.com:octocat/Hello-World.git",
    "stargazers_url": "https://api.github.com/repos/octocat/Hello-World/stargazers",
    "statuses_url": "https://api.github.com/repos/octocat/Hello-World/statuses/{commit_sha}",
    "subscribers_url": "https://api.github.com/repos/octocat/Hello-World/subscribers",
    "subscription_url": "https://api.github.com/repos/octocat/Hello-World/subscription",
    "tags_url": "https://api.github.com/repos/octocat/Hello-World/tags",
    "teams_url": "https://api.github.com/repos/octocat/Hello-World/teams",
    "trees_url": "https://api.github.com/repos/octocat/Hello-World/git/trees{/commit_sha}",
    "hooks_url": "http://api.github.com/repos/octocat/Hello-World/hooks"
  },
  "machine": {
    "name": "standardLinux",
    "display_name": "4 cores, 16 GB RAM, 64 GB storage",
    "operating_system": "linux",
    "storage_in_bytes": 68719476736,
    "memory_in_bytes": 17179869184,
    "cpus": 4
  },
  "prebuild": false,
  "devcontainer_path": ".devcontainer/devcontainer.json",
  "created_at": "2021-10-14T00:53:30-06:00",
  "updated_at": "2021-10-14T00:53:32-06:00",
  "last_used_at": "2021-10-14T00:53:30-06:00",
  "issue_state": "Available",
  "url": "https://api.github.com/user/codespaces/monalisa-octocat-hello-world-g4wpq6h95q",
  "git_status": {
    "ahead": 0,
    "behind": 0,
    "has_unpushed_changes": false,
    "has_uncommitted_changes": false,
    "ref": "main"
  },
  "location": "WestUs2",
  "idle_timeout_minutes": 60,
  "retention_period_minutes": 43200,
  "retention_expires_at": null,
  "web_url": "https://monalisa-octocat-hello-world-g4wpq6h95q.github.dev",
  "machines_url": "https://api.github.com/user/codespaces/monalisa-octocat-hello-world-g4wpq6h95q/machines",
  "start_url": "https://api.github.com/user/codespaces/monalisa-octocat-hello-world-g4wpq6h95q/start",
  "stop_url": "https://api.github.com/user/codespaces/monalisa-octocat-hello-world-g4wpq6h95q/stop",
  "pulls_url": "https://api.github.com/repos/octocat/Hello-World/pulls/1",
  "recent_folders": [],
  "template": null
}
```

## Delete a codespace for the authenticated user
Deletes a user's codespace.
OAuth app tokens and personal access tokens (classic) need thecodespacescope to use this endpoint.

### Fine-grained access tokens for "Delete a codespace for the authenticated user"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Codespaces" repository permissions (write)

### Parameters for "Delete a codespace for the authenticated user"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
codespace_namestringRequiredThe name of the codespace.
[/TABLE]

```
codespace_name
```
The name of the codespace.

### HTTP response status codes for "Delete a codespace for the authenticated user"

[TABLE]
Status code | Description
202 | Accepted
304 | Not modified
401 | Requires authentication
403 | Forbidden
404 | Resource not found
500 | Internal Error
[/TABLE]
Accepted
Not modified
Requires authentication
Forbidden
Resource not found
Internal Error

### Code samples for "Delete a codespace for the authenticated user"

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
  https://api.github.com/user/codespaces/CODESPACE_NAME
```

#### Accepted
- Example response
- Response schema

```
Status: 202
```

## Export a codespace for the authenticated user
Triggers an export of the specified codespace and returns a URL and ID where the status of the export can be monitored.
If changes cannot be pushed to the codespace's repository, they will be pushed to a new or previously-existing fork instead.
OAuth app tokens and personal access tokens (classic) need thecodespacescope to use this endpoint.

### Fine-grained access tokens for "Export a codespace for the authenticated user"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Codespaces lifecycle admin" repository permissions (write)

### Parameters for "Export a codespace for the authenticated user"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
codespace_namestringRequiredThe name of the codespace.
[/TABLE]

```
codespace_name
```
The name of the codespace.

### HTTP response status codes for "Export a codespace for the authenticated user"

[TABLE]
Status code | Description
202 | Accepted
401 | Requires authentication
403 | Forbidden
404 | Resource not found
422 | Validation failed, or the endpoint has been spammed.
500 | Internal Error
[/TABLE]
Accepted
Requires authentication
Forbidden
Resource not found
Validation failed, or the endpoint has been spammed.
Internal Error

### Code samples for "Export a codespace for the authenticated user"

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
  https://api.github.com/user/codespaces/CODESPACE_NAME/exports
```

#### Response
- Example response
- Response schema

```
Status: 202
```

```
{
  "issue_state": "succeeded",
  "completed_at": "2022-01-01T14:59:22Z",
  "branch": "codespace-monalisa-octocat-hello-world-g4wpq6h95q",
  "commit_sha": "fd95a81ca01e48ede9f39c799ecbcef817b8a3b2",
  "id": "latest",
  "export_url": "https://api.github.com/user/codespaces/:name/exports/latest"
}
```

## Get details about a codespace export
Gets information about an export of a codespace.
OAuth app tokens and personal access tokens (classic) need thecodespacescope to use this endpoint.

### Fine-grained access tokens for "Get details about a codespace export"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Codespaces lifecycle admin" repository permissions (read)

### Parameters for "Get details about a codespace export"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
codespace_namestringRequiredThe name of the codespace.
export_idstringRequiredThe ID of the export operation, orlatest. Currently onlylatestis currently supported.
[/TABLE]

```
codespace_name
```
The name of the codespace.
The ID of the export operation, orlatest. Currently onlylatestis currently supported.

### HTTP response status codes for "Get details about a codespace export"

[TABLE]
Status code | Description
200 | OK
404 | Resource not found
[/TABLE]
OK
Resource not found

### Code samples for "Get details about a codespace export"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/user/codespaces/CODESPACE_NAME/exports/EXPORT_ID
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "issue_state": "succeeded",
  "completed_at": "2022-01-01T14:59:22Z",
  "branch": "codespace-monalisa-octocat-hello-world-g4wpq6h95q",
  "commit_sha": "fd95a81ca01e48ede9f39c799ecbcef817b8a3b2",
  "id": "latest",
  "export_url": "https://api.github.com/user/codespaces/:name/exports/latest"
}
```

## Create a repository from an unpublished codespace
Publishes an unpublished codespace, creating a new repository and assigning it to the codespace.
The codespace's token is granted write permissions to the repository, allowing the user to push their changes.
This will fail for a codespace that is already published, meaning it has an associated repository.
OAuth app tokens and personal access tokens (classic) need thecodespacescope to use this endpoint.

### Fine-grained access tokens for "Create a repository from an unpublished codespace"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Codespaces" repository permissions (write)

### Parameters for "Create a repository from an unpublished codespace"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
codespace_namestringRequiredThe name of the codespace.
[/TABLE]

```
codespace_name
```
The name of the codespace.

[TABLE]
Name, Type, Description
namestringA name for the new repository.
privatebooleanWhether the new repository should be private.Default:false
[/TABLE]
A name for the new repository.
Whether the new repository should be private.
Default:false

### HTTP response status codes for "Create a repository from an unpublished codespace"

[TABLE]
Status code | Description
201 | Created
401 | Requires authentication
403 | Forbidden
404 | Resource not found
422 | Validation failed, or the endpoint has been spammed.
[/TABLE]
Created
Requires authentication
Forbidden
Resource not found
Validation failed, or the endpoint has been spammed.

### Code samples for "Create a repository from an unpublished codespace"

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
  https://api.github.com/user/codespaces/CODESPACE_NAME/publish \
  -d '{"repository":"monalisa-octocat-hello-world-g4wpq6h95q","private":false}'
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
  "name": "monalisa-octocat-hello-world-g4wpq6h95q",
  "environment_id": "26a7c758-7299-4a73-b978-5a92a7ae98a0",
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
  "billable_owner": {
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
    "git_url": "git:github.com/octocat/Hello-World.git",
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
    "ssh_url": "git@github.com:octocat/Hello-World.git",
    "stargazers_url": "https://api.github.com/repos/octocat/Hello-World/stargazers",
    "statuses_url": "https://api.github.com/repos/octocat/Hello-World/statuses/{commit_sha}",
    "subscribers_url": "https://api.github.com/repos/octocat/Hello-World/subscribers",
    "subscription_url": "https://api.github.com/repos/octocat/Hello-World/subscription",
    "tags_url": "https://api.github.com/repos/octocat/Hello-World/tags",
    "teams_url": "https://api.github.com/repos/octocat/Hello-World/teams",
    "trees_url": "https://api.github.com/repos/octocat/Hello-World/git/trees{/commit_sha}",
    "clone_url": "https://github.com/octocat/Hello-World.git",
    "mirror_url": "git:git.example.com/octocat/Hello-World",
    "hooks_url": "https://api.github.com/repos/octocat/Hello-World/hooks",
    "svn_url": "https://svn.github.com/octocat/Hello-World",
    "homepage": "https://github.com",
    "license": {
      "key": "mit",
      "name": "MIT License",
      "url": "https://api.github.com/licenses/mit",
      "spdx_id": "MIT",
      "node_id": "MDc6TGljZW5zZW1pdA==",
      "html_url": "https://github.com/licenses/mit"
    },
    "language": null,
    "forks_count": 9,
    "forks": 9,
    "stargazers_count": 80,
    "watchers_count": 80,
    "watchers": 80,
    "size": 108,
    "default_branch": "master",
    "open_issues_count": 0,
    "open_issues": 0,
    "is_template": false,
    "topics": [
      "octocat",
      "atom",
      "electron",
      "api"
    ],
    "has_issues": true,
    "has_projects": true,
    "has_wiki": true,
    "has_pages": false,
    "has_downloads": true,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "pushed_at": "2011-01-26T19:06:43Z",
    "created_at": "2011-01-26T19:01:12Z",
    "updated_at": "2011-01-26T19:14:43Z",
    "permissions": {
      "pull": true,
      "push": false,
      "admin": false
    },
    "allow_rebase_merge": true,
    "template_repository": {
      "id": 1296269,
      "node_id": "MDEwOlJlcG9zaXRvcnkxMjk2MjY5",
      "name": "Hello-World-Template",
      "full_name": "octocat/Hello-World-Template",
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
      "html_url": "https://github.com/octocat/Hello-World-Template",
      "description": "This your first repo!",
      "fork": false,
      "url": "https://api.github.com/repos/octocat/Hello-World-Template",
      "archive_url": "https://api.github.com/repos/octocat/Hello-World-Template/{archive_format}{/ref}",
      "assignees_url": "https://api.github.com/repos/octocat/Hello-World-Template/assignees{/user}",
      "blobs_url": "https://api.github.com/repos/octocat/Hello-World-Template/git/blobs{/commit_sha}",
      "branches_url": "https://api.github.com/repos/octocat/Hello-World-Template/branches{/branch}",
      "collaborators_url": "https://api.github.com/repos/octocat/Hello-World-Template/collaborators{/collaborator}",
      "comments_url": "https://api.github.com/repos/octocat/Hello-World-Template/comments{/number}",
      "commits_url": "https://api.github.com/repos/octocat/Hello-World-Template/commits{/commit_sha}",
      "compare_url": "https://api.github.com/repos/octocat/Hello-World-Template/compare/{base}...{head}",
      "contents_url": "https://api.github.com/repos/octocat/Hello-World-Template/contents/{+path}",
      "contributors_url": "https://api.github.com/repos/octocat/Hello-World-Template/contributors",
      "deployments_url": "https://api.github.com/repos/octocat/Hello-World-Template/deployments",
      "downloads_url": "https://api.github.com/repos/octocat/Hello-World-Template/downloads",
      "events_url": "https://api.github.com/repos/octocat/Hello-World-Template/events",
      "forks_url": "https://api.github.com/repos/octocat/Hello-World-Template/forks",
      "git_commits_url": "https://api.github.com/repos/octocat/Hello-World-Template/git/commits{/commit_sha}",
      "git_refs_url": "https://api.github.com/repos/octocat/Hello-World-Template/git/refs{/commit_sha}",
      "git_tags_url": "https://api.github.com/repos/octocat/Hello-World-Template/git/tags{/commit_sha}",
      "git_url": "git:github.com/octocat/Hello-World-Template.git",
      "issue_comment_url": "https://api.github.com/repos/octocat/Hello-World-Template/issues/comments{/number}",
      "issue_events_url": "https://api.github.com/repos/octocat/Hello-World-Template/issues/events{/number}",
      "issues_url": "https://api.github.com/repos/octocat/Hello-World-Template/issues{/number}",
      "keys_url": "https://api.github.com/repos/octocat/Hello-World-Template/keys{/key_id}",
      "labels_url": "https://api.github.com/repos/octocat/Hello-World-Template/label_filters{/name}",
      "languages_url": "https://api.github.com/repos/octocat/Hello-World-Template/languages",
      "merges_url": "https://api.github.com/repos/octocat/Hello-World-Template/merges",
      "milestones_url": "https://api.github.com/repos/octocat/Hello-World-Template/milestones{/number}",
      "notifications_url": "https://api.github.com/repos/octocat/Hello-World-Template/notifications{?since,all,participating}",
      "pulls_url": "https://api.github.com/repos/octocat/Hello-World-Template/pulls{/number}",
      "releases_url": "https://api.github.com/repos/octocat/Hello-World-Template/releases{/id}",
      "ssh_url": "git@github.com:octocat/Hello-World-Template.git",
      "stargazers_url": "https://api.github.com/repos/octocat/Hello-World-Template/stargazers",
      "statuses_url": "https://api.github.com/repos/octocat/Hello-World-Template/statuses/{commit_sha}",
      "subscribers_url": "https://api.github.com/repos/octocat/Hello-World-Template/subscribers",
      "subscription_url": "https://api.github.com/repos/octocat/Hello-World-Template/subscription",
      "tags_url": "https://api.github.com/repos/octocat/Hello-World-Template/tags",
      "teams_url": "https://api.github.com/repos/octocat/Hello-World-Template/teams",
      "trees_url": "https://api.github.com/repos/octocat/Hello-World-Template/git/trees{/commit_sha}",
      "clone_url": "https://github.com/octocat/Hello-World-Template.git",
      "mirror_url": "git:git.example.com/octocat/Hello-World-Template",
      "hooks_url": "https://api.github.com/repos/octocat/Hello-World-Template/hooks",
      "svn_url": "https://svn.github.com/octocat/Hello-World-Template",
      "homepage": "https://github.com",
      "language": null,
      "forks": 9,
      "forks_count": 9,
      "stargazers_count": 80,
      "watchers_count": 80,
      "watchers": 80,
      "size": 108,
      "default_branch": "master",
      "open_issues": 0,
      "open_issues_count": 0,
      "is_template": true,
      "license": {
        "key": "mit",
        "name": "MIT License",
        "url": "https://api.github.com/licenses/mit",
        "spdx_id": "MIT",
        "node_id": "MDc6TGljZW5zZW1pdA==",
        "html_url": "https://api.github.com/licenses/mit"
      },
      "topics": [
        "octocat",
        "atom",
        "electron",
        "api"
      ],
      "has_issues": true,
      "has_projects": true,
      "has_wiki": true,
      "has_pages": false,
      "has_downloads": true,
      "archived": false,
      "disabled": false,
      "visibility": "public",
      "pushed_at": "2011-01-26T19:06:43Z",
      "created_at": "2011-01-26T19:01:12Z",
      "updated_at": "2011-01-26T19:14:43Z",
      "permissions": {
        "admin": false,
        "push": false,
        "pull": true
      },
      "allow_rebase_merge": true,
      "temp_clone_token": "ABTLWHOULUVAXGTRYU7OC2876QJ2O",
      "allow_squash_merge": true,
      "allow_auto_merge": false,
      "delete_branch_on_merge": true,
      "allow_merge_commit": true,
      "subscribers_count": 42,
      "network_count": 0
    },
    "temp_clone_token": "ABTLWHOULUVAXGTRYU7OC2876QJ2O",
    "allow_squash_merge": true,
    "allow_auto_merge": false,
    "delete_branch_on_merge": true,
    "allow_merge_commit": true,
    "allow_forking": true,
    "subscribers_count": 42,
    "network_count": 0,
    "organization": {
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
      "type": "Organization",
      "site_admin": false
    },
    "parent": {
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
      "git_url": "git:github.com/octocat/Hello-World.git",
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
      "ssh_url": "git@github.com:octocat/Hello-World.git",
      "stargazers_url": "https://api.github.com/repos/octocat/Hello-World/stargazers",
      "statuses_url": "https://api.github.com/repos/octocat/Hello-World/statuses/{commit_sha}",
      "subscribers_url": "https://api.github.com/repos/octocat/Hello-World/subscribers",
      "subscription_url": "https://api.github.com/repos/octocat/Hello-World/subscription",
      "tags_url": "https://api.github.com/repos/octocat/Hello-World/tags",
      "teams_url": "https://api.github.com/repos/octocat/Hello-World/teams",
      "trees_url": "https://api.github.com/repos/octocat/Hello-World/git/trees{/commit_sha}",
      "clone_url": "https://github.com/octocat/Hello-World.git",
      "mirror_url": "git:git.example.com/octocat/Hello-World",
      "hooks_url": "https://api.github.com/repos/octocat/Hello-World/hooks",
      "svn_url": "https://svn.github.com/octocat/Hello-World",
      "homepage": "https://github.com",
      "language": null,
      "forks_count": 9,
      "stargazers_count": 80,
      "watchers_count": 80,
      "size": 108,
      "default_branch": "master",
      "open_issues_count": 0,
      "is_template": true,
      "topics": [
        "octocat",
        "atom",
        "electron",
        "api"
      ],
      "has_issues": true,
      "has_projects": true,
      "has_wiki": true,
      "has_pages": false,
      "has_downloads": true,
      "archived": false,
      "disabled": false,
      "visibility": "public",
      "pushed_at": "2011-01-26T19:06:43Z",
      "created_at": "2011-01-26T19:01:12Z",
      "updated_at": "2011-01-26T19:14:43Z",
      "permissions": {
        "admin": false,
        "push": false,
        "pull": true
      },
      "allow_rebase_merge": true,
      "temp_clone_token": "ABTLWHOULUVAXGTRYU7OC2876QJ2O",
      "allow_squash_merge": true,
      "allow_auto_merge": false,
      "delete_branch_on_merge": true,
      "allow_merge_commit": true,
      "subscribers_count": 42,
      "network_count": 0,
      "license": {
        "key": "mit",
        "name": "MIT License",
        "url": "https://api.github.com/licenses/mit",
        "spdx_id": "MIT",
        "node_id": "MDc6TGljZW5zZW1pdA==",
        "html_url": "https://api.github.com/licenses/mit"
      },
      "forks": 1,
      "open_issues": 1,
      "watchers": 1
    },
    "source": {
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
      "git_url": "git:github.com/octocat/Hello-World.git",
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
      "ssh_url": "git@github.com:octocat/Hello-World.git",
      "stargazers_url": "https://api.github.com/repos/octocat/Hello-World/stargazers",
      "statuses_url": "https://api.github.com/repos/octocat/Hello-World/statuses/{commit_sha}",
      "subscribers_url": "https://api.github.com/repos/octocat/Hello-World/subscribers",
      "subscription_url": "https://api.github.com/repos/octocat/Hello-World/subscription",
      "tags_url": "https://api.github.com/repos/octocat/Hello-World/tags",
      "teams_url": "https://api.github.com/repos/octocat/Hello-World/teams",
      "trees_url": "https://api.github.com/repos/octocat/Hello-World/git/trees{/commit_sha}",
      "clone_url": "https://github.com/octocat/Hello-World.git",
      "mirror_url": "git:git.example.com/octocat/Hello-World",
      "hooks_url": "https://api.github.com/repos/octocat/Hello-World/hooks",
      "svn_url": "https://svn.github.com/octocat/Hello-World",
      "homepage": "https://github.com",
      "language": null,
      "forks_count": 9,
      "stargazers_count": 80,
      "watchers_count": 80,
      "size": 108,
      "default_branch": "master",
      "open_issues_count": 0,
      "is_template": true,
      "topics": [
        "octocat",
        "atom",
        "electron",
        "api"
      ],
      "has_issues": true,
      "has_projects": true,
      "has_wiki": true,
      "has_pages": false,
      "has_downloads": true,
      "archived": false,
      "disabled": false,
      "visibility": "public",
      "pushed_at": "2011-01-26T19:06:43Z",
      "created_at": "2011-01-26T19:01:12Z",
      "updated_at": "2011-01-26T19:14:43Z",
      "permissions": {
        "admin": false,
        "push": false,
        "pull": true
      },
      "allow_rebase_merge": true,
      "temp_clone_token": "ABTLWHOULUVAXGTRYU7OC2876QJ2O",
      "allow_squash_merge": true,
      "allow_auto_merge": false,
      "delete_branch_on_merge": true,
      "allow_merge_commit": true,
      "subscribers_count": 42,
      "network_count": 0,
      "license": {
        "key": "mit",
        "name": "MIT License",
        "url": "https://api.github.com/licenses/mit",
        "spdx_id": "MIT",
        "node_id": "MDc6TGljZW5zZW1pdA==",
        "html_url": "https://api.github.com/licenses/mit"
      },
      "forks": 1,
      "open_issues": 1,
      "watchers": 1
    }
  },
  "machine": {
    "name": "standardLinux",
    "display_name": "4 cores, 16 GB RAM, 64 GB storage",
    "operating_system": "linux",
    "storage_in_bytes": 68719476736,
    "memory_in_bytes": 17179869184,
    "cpus": 4
  },
  "prebuild": false,
  "devcontainer_path": ".devcontainer/devcontainer.json",
  "created_at": "2021-10-14T00:53:30-06:00",
  "updated_at": "2021-10-14T00:53:32-06:00",
  "last_used_at": "2021-10-14T00:53:30-06:00",
  "issue_state": "Available",
  "url": "https://api.github.com/user/codespaces/monalisa-octocat-hello-world-g4wpq6h95q",
  "git_status": {
    "ahead": 0,
    "behind": 0,
    "has_unpushed_changes": false,
    "has_uncommitted_changes": false,
    "ref": "main"
  },
  "location": "WestUs2",
  "idle_timeout_minutes": 60,
  "retention_period_minutes": 43200,
  "retention_expires_at": null,
  "web_url": "https://monalisa-octocat-hello-world-g4wpq6h95q.github.dev",
  "machines_url": "https://api.github.com/user/codespaces/monalisa-octocat-hello-world-g4wpq6h95q/machines",
  "start_url": "https://api.github.com/user/codespaces/monalisa-octocat-hello-world-g4wpq6h95q/start",
  "stop_url": "https://api.github.com/user/codespaces/monalisa-octocat-hello-world-g4wpq6h95q/stop",
  "pulls_url": "https://api.github.com/repos/octocat/Hello-World/pulls/1",
  "recent_folders": [],
  "template": null
}
```

## Start a codespace for the authenticated user
Starts a user's codespace.
OAuth app tokens and personal access tokens (classic) need thecodespacescope to use this endpoint.

### Fine-grained access tokens for "Start a codespace for the authenticated user"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Codespaces lifecycle admin" repository permissions (write)

### Parameters for "Start a codespace for the authenticated user"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
codespace_namestringRequiredThe name of the codespace.
[/TABLE]

```
codespace_name
```
The name of the codespace.

### HTTP response status codes for "Start a codespace for the authenticated user"

[TABLE]
Status code | Description
200 | OK
304 | Not modified
400 | Bad Request
401 | Requires authentication
402 | Payment required
403 | Forbidden
404 | Resource not found
409 | Conflict
500 | Internal Error
[/TABLE]
OK
Not modified
Bad Request
Requires authentication
Payment required
Forbidden
Resource not found
Conflict
Internal Error

### Code samples for "Start a codespace for the authenticated user"

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
  https://api.github.com/user/codespaces/CODESPACE_NAME/start
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
  "name": "monalisa-octocat-hello-world-g4wpq6h95q",
  "environment_id": "26a7c758-7299-4a73-b978-5a92a7ae98a0",
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
  "billable_owner": {
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
    "git_url": "git:github.com/octocat/Hello-World.git",
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
    "ssh_url": "git@github.com:octocat/Hello-World.git",
    "stargazers_url": "https://api.github.com/repos/octocat/Hello-World/stargazers",
    "statuses_url": "https://api.github.com/repos/octocat/Hello-World/statuses/{commit_sha}",
    "subscribers_url": "https://api.github.com/repos/octocat/Hello-World/subscribers",
    "subscription_url": "https://api.github.com/repos/octocat/Hello-World/subscription",
    "tags_url": "https://api.github.com/repos/octocat/Hello-World/tags",
    "teams_url": "https://api.github.com/repos/octocat/Hello-World/teams",
    "trees_url": "https://api.github.com/repos/octocat/Hello-World/git/trees{/commit_sha}",
    "hooks_url": "http://api.github.com/repos/octocat/Hello-World/hooks"
  },
  "machine": {
    "name": "standardLinux",
    "display_name": "4 cores, 16 GB RAM, 64 GB storage",
    "operating_system": "linux",
    "storage_in_bytes": 68719476736,
    "memory_in_bytes": 17179869184,
    "cpus": 4
  },
  "prebuild": false,
  "devcontainer_path": ".devcontainer/devcontainer.json",
  "created_at": "2021-10-14T00:53:30-06:00",
  "updated_at": "2021-10-14T00:53:32-06:00",
  "last_used_at": "2021-10-14T00:53:30-06:00",
  "issue_state": "Available",
  "url": "https://api.github.com/user/codespaces/monalisa-octocat-hello-world-g4wpq6h95q",
  "git_status": {
    "ahead": 0,
    "behind": 0,
    "has_unpushed_changes": false,
    "has_uncommitted_changes": false,
    "ref": "main"
  },
  "location": "WestUs2",
  "idle_timeout_minutes": 60,
  "retention_period_minutes": 43200,
  "retention_expires_at": null,
  "web_url": "https://monalisa-octocat-hello-world-g4wpq6h95q.github.dev",
  "machines_url": "https://api.github.com/user/codespaces/monalisa-octocat-hello-world-g4wpq6h95q/machines",
  "start_url": "https://api.github.com/user/codespaces/monalisa-octocat-hello-world-g4wpq6h95q/start",
  "stop_url": "https://api.github.com/user/codespaces/monalisa-octocat-hello-world-g4wpq6h95q/stop",
  "pulls_url": "https://api.github.com/repos/octocat/Hello-World/pulls/1",
  "recent_folders": [],
  "template": null
}
```

## Stop a codespace for the authenticated user
Stops a user's codespace.
OAuth app tokens and personal access tokens (classic) need thecodespacescope to use this endpoint.

### Fine-grained access tokens for "Stop a codespace for the authenticated user"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Codespaces lifecycle admin" repository permissions (write)

### Parameters for "Stop a codespace for the authenticated user"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
codespace_namestringRequiredThe name of the codespace.
[/TABLE]

```
codespace_name
```
The name of the codespace.

### HTTP response status codes for "Stop a codespace for the authenticated user"

[TABLE]
Status code | Description
200 | OK
401 | Requires authentication
403 | Forbidden
404 | Resource not found
500 | Internal Error
[/TABLE]
OK
Requires authentication
Forbidden
Resource not found
Internal Error

### Code samples for "Stop a codespace for the authenticated user"

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
  https://api.github.com/user/codespaces/CODESPACE_NAME/stop
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
  "name": "monalisa-octocat-hello-world-g4wpq6h95q",
  "environment_id": "26a7c758-7299-4a73-b978-5a92a7ae98a0",
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
  "billable_owner": {
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
    "git_url": "git:github.com/octocat/Hello-World.git",
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
    "ssh_url": "git@github.com:octocat/Hello-World.git",
    "stargazers_url": "https://api.github.com/repos/octocat/Hello-World/stargazers",
    "statuses_url": "https://api.github.com/repos/octocat/Hello-World/statuses/{commit_sha}",
    "subscribers_url": "https://api.github.com/repos/octocat/Hello-World/subscribers",
    "subscription_url": "https://api.github.com/repos/octocat/Hello-World/subscription",
    "tags_url": "https://api.github.com/repos/octocat/Hello-World/tags",
    "teams_url": "https://api.github.com/repos/octocat/Hello-World/teams",
    "trees_url": "https://api.github.com/repos/octocat/Hello-World/git/trees{/commit_sha}",
    "hooks_url": "http://api.github.com/repos/octocat/Hello-World/hooks"
  },
  "machine": {
    "name": "standardLinux",
    "display_name": "4 cores, 16 GB RAM, 64 GB storage",
    "operating_system": "linux",
    "storage_in_bytes": 68719476736,
    "memory_in_bytes": 17179869184,
    "cpus": 4
  },
  "prebuild": false,
  "devcontainer_path": ".devcontainer/devcontainer.json",
  "created_at": "2021-10-14T00:53:30-06:00",
  "updated_at": "2021-10-14T00:53:32-06:00",
  "last_used_at": "2021-10-14T00:53:30-06:00",
  "issue_state": "Available",
  "url": "https://api.github.com/user/codespaces/monalisa-octocat-hello-world-g4wpq6h95q",
  "git_status": {
    "ahead": 0,
    "behind": 0,
    "has_unpushed_changes": false,
    "has_uncommitted_changes": false,
    "ref": "main"
  },
  "location": "WestUs2",
  "idle_timeout_minutes": 60,
  "retention_period_minutes": 43200,
  "retention_expires_at": null,
  "web_url": "https://monalisa-octocat-hello-world-g4wpq6h95q.github.dev",
  "machines_url": "https://api.github.com/user/codespaces/monalisa-octocat-hello-world-g4wpq6h95q/machines",
  "start_url": "https://api.github.com/user/codespaces/monalisa-octocat-hello-world-g4wpq6h95q/start",
  "stop_url": "https://api.github.com/user/codespaces/monalisa-octocat-hello-world-g4wpq6h95q/stop",
  "pulls_url": "https://api.github.com/repos/octocat/Hello-World/pulls/1",
  "recent_folders": [],
  "template": null
}
```