# REST API endpoints for check suites

*Source: https://docs.github.com/en/rest/checks/suites*

---

# REST API endpoints for check suites
Use the REST API to manage check suites.
Note
Write permission for the REST API to interact with checks is only available to GitHub Apps. OAuth apps and authenticated users can view check runs and check suites, but they are not able to create them. If you aren't building a GitHub App, you might be interested in using the REST API to interact withcommit statuses.
Note
A GitHub App usually only receives onecheck_suiteevent per commit SHA, even if you push the commit SHA to more than one branch. To find out when a commit SHA is pushed to a branch, you can subscribe to branchcreateevents.

```
check_suite
```

## Create a check suite
Creates a check suite manually. By default, check suites are automatically created when you create acheck run. You only need to use this endpoint for manually creating check suites when you've disabled automatic creation using "Update repository preferences for check suites".
Note
The Checks API only looks for pushes in the repository where the check suite or check run were created. Pushes to a branch in a forked repository are not detected and return an emptypull_requestsarray and anullvalue forhead_branch.
OAuth apps and personal access tokens (classic) cannot use this endpoint.

### Fine-grained access tokens for "Create a check suite"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Checks" repository permissions (write)

### Parameters for "Create a check suite"

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
head_shastringRequiredThe commit_sha of the head commit.
[/TABLE]
The commit_sha of the head commit.

### HTTP response status codes for "Create a check suite"

[TABLE]
Status code | Description
200 | Response when the suite already exists
201 | Response when the suite was created
[/TABLE]
Response when the suite already exists
Response when the suite was created

### Code samples for "Create a check suite"

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
  https://api.github.com/repos/OWNER/REPO/check-suites \
  -d '{"head_sha":"d6fde92930d4715a2b49857d24b940956b26d2d3"}'
```

#### Response when the suite already exists
- Example response
- Response schema

```
Status: 200
```

```
{
  "id": 5,
  "node_id": "MDEwOkNoZWNrU3VpdGU1",
  "head_branch": "master",
  "head_sha": "d6fde92930d4715a2b49857d24b940956b26d2d3",
  "status": "completed",
  "conclusion": "neutral",
  "url": "https://api.github.com/repos/github/hello-world/check-suites/5",
  "before": "146e867f55c26428e5f9fade55a9bbf5e95a7912",
  "after": "d6fde92930d4715a2b49857d24b940956b26d2d3",
  "pull_requests": [],
  "created_at": "2017-07-08T16:18:44-04:00",
  "updated_at": "2017-07-08T16:18:44-04:00",
  "app": {
    "id": 1,
    "slug": "octoapp",
    "node_id": "MDExOkludGVncmF0aW9uMQ==",
    "owner": {
      "login": "github",
      "id": 1,
      "node_id": "MDEyOk9yZ2FuaXphdGlvbjE=",
      "url": "https://api.github.com/orgs/github",
      "repos_url": "https://api.github.com/orgs/github/repos",
      "events_url": "https://api.github.com/orgs/github/events",
      "avatar_url": "https://github.com/images/error/octocat_happy.gif",
      "gravatar_id": "",
      "html_url": "https://github.com/octocat",
      "followers_url": "https://api.github.com/users/octocat/followers",
      "following_url": "https://api.github.com/users/octocat/following{/other_user}",
      "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
      "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
      "organizations_url": "https://api.github.com/users/octocat/orgs",
      "received_events_url": "https://api.github.com/users/octocat/received_events",
      "type": "User",
      "site_admin": true
    },
    "name": "Octocat App",
    "description": "",
    "external_url": "https://example.com",
    "html_url": "https://github.com/apps/octoapp",
    "created_at": "2017-07-08T16:18:44-04:00",
    "updated_at": "2017-07-08T16:18:44-04:00",
    "permissions": {
      "metadata": "read",
      "contents": "read",
      "issues": "write",
      "single_file": "write"
    },
    "events": [
      "push",
      "pull_request"
    ]
  },
  "repository": {
    "id": 1296269,
    "node_id": "MDEwOlJlcG9zaXRvcnkxMjk2MjY5",
    "name": "Hello-World",
    "full_name": "octocat/Hello-World",
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
      "admin": false,
      "push": false,
      "pull": true
    },
    "temp_clone_token": "ABTLWHOULUVAXGTRYU7OC2876QJ2O",
    "delete_branch_on_merge": true,
    "subscribers_count": 42,
    "network_count": 0
  },
  "head_commit": {
    "id": "7fd1a60b01f91b314f59955a4e4d4e80d8edf11d",
    "tree_id": "7fd1a60b01f91b314f59955a4e4d4e80d8edf11d",
    "message": "Merge pull request #6 from Spaceghost/patch-1\n\nNew line at end of file.",
    "timestamp": "2016-10-10T00:00:00Z",
    "author": {
      "name": "The Octocat",
      "email": "octocat@nowhere.com"
    },
    "committer": {
      "name": "The Octocat",
      "email": "octocat@nowhere.com"
    }
  },
  "latest_check_runs_count": 1,
  "check_runs_url": "https://api.github.com/repos/octocat/Hello-World/check-suites/5/check-runs"
}
```

## Update repository preferences for check suites
Changes the default automatic flow when creating check suites. By default, a check suite is automatically created each time code is pushed to a repository. When you disable the automatic creation of check suites, you can manuallyCreate a check suite.
You must have admin permissions in the repository to set preferences for check suites.

### Fine-grained access tokens for "Update repository preferences for check suites"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Checks" repository permissions (write)

### Parameters for "Update repository preferences for check suites"

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
auto_trigger_checksarray of objectsEnables or disables automatic creation of CheckSuite events upon pushes to the repository. Enabled by default.
Properties ofauto_trigger_checksName, Type, Descriptionapp_idintegerRequiredTheidof the GitHub App.settingbooleanRequiredSet totrueto enable automatic creation of CheckSuite events upon pushes to the repository, orfalseto disable them.Default:true | Name, Type, Description | app_idintegerRequiredTheidof the GitHub App. | settingbooleanRequiredSet totrueto enable automatic creation of CheckSuite events upon pushes to the repository, orfalseto disable them.Default:true
Name, Type, Description
app_idintegerRequiredTheidof the GitHub App.
settingbooleanRequiredSet totrueto enable automatic creation of CheckSuite events upon pushes to the repository, orfalseto disable them.Default:true
[/TABLE]

```
auto_trigger_checks
```
Enables or disables automatic creation of CheckSuite events upon pushes to the repository. Enabled by default.

```
auto_trigger_checks
```

[TABLE]
Name, Type, Description
app_idintegerRequiredTheidof the GitHub App.
settingbooleanRequiredSet totrueto enable automatic creation of CheckSuite events upon pushes to the repository, orfalseto disable them.Default:true
[/TABLE]
Theidof the GitHub App.
Set totrueto enable automatic creation of CheckSuite events upon pushes to the repository, orfalseto disable them.
Default:true

### HTTP response status codes for "Update repository preferences for check suites"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "Update repository preferences for check suites"

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
  https://api.github.com/repos/OWNER/REPO/check-suites/preferences \
  -d '{"auto_trigger_checks":[{"app_id":4,"setting":false}]}'
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "preferences": {
    "auto_trigger_checks": [
      {
        "app_id": 2,
        "setting": true
      },
      {
        "app_id": 4,
        "setting": false
      }
    ]
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
    "language": null,
    "forks_count": 9,
    "stargazers_count": 80,
    "watchers_count": 80,
    "size": 108,
    "default_branch": "master",
    "open_issues_count": 0,
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
      "admin": false,
      "push": false,
      "pull": true
    },
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
    }
  }
}
```

## Get a check suite
Gets a single check suite using itsid.
Note
The Checks API only looks for pushes in the repository where the check suite or check run were created. Pushes to a branch in a forked repository are not detected and return an emptypull_requestsarray and anullvalue forhead_branch.
OAuth app tokens and personal access tokens (classic) need thereposcope to use this endpoint on a private repository.

### Fine-grained access tokens for "Get a check suite"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Checks" repository permissions (read)
This endpoint can be used without authentication or the aforementioned permissions if only public resources are requested.

### Parameters for "Get a check suite"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
check_suite_idintegerRequiredThe unique identifier of the check suite.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.

```
check_suite_id
```
The unique identifier of the check suite.

### HTTP response status codes for "Get a check suite"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "Get a check suite"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/check-suites/CHECK_SUITE_ID
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "id": 5,
  "node_id": "MDEwOkNoZWNrU3VpdGU1",
  "head_branch": "master",
  "head_sha": "d6fde92930d4715a2b49857d24b940956b26d2d3",
  "status": "completed",
  "conclusion": "neutral",
  "url": "https://api.github.com/repos/github/hello-world/check-suites/5",
  "before": "146e867f55c26428e5f9fade55a9bbf5e95a7912",
  "after": "d6fde92930d4715a2b49857d24b940956b26d2d3",
  "pull_requests": [],
  "created_at": "2017-07-08T16:18:44-04:00",
  "updated_at": "2017-07-08T16:18:44-04:00",
  "app": {
    "id": 1,
    "slug": "octoapp",
    "node_id": "MDExOkludGVncmF0aW9uMQ==",
    "owner": {
      "login": "github",
      "id": 1,
      "node_id": "MDEyOk9yZ2FuaXphdGlvbjE=",
      "url": "https://api.github.com/orgs/github",
      "repos_url": "https://api.github.com/orgs/github/repos",
      "events_url": "https://api.github.com/orgs/github/events",
      "avatar_url": "https://github.com/images/error/octocat_happy.gif",
      "gravatar_id": "",
      "html_url": "https://github.com/octocat",
      "followers_url": "https://api.github.com/users/octocat/followers",
      "following_url": "https://api.github.com/users/octocat/following{/other_user}",
      "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
      "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
      "organizations_url": "https://api.github.com/users/octocat/orgs",
      "received_events_url": "https://api.github.com/users/octocat/received_events",
      "type": "User",
      "site_admin": true
    },
    "name": "Octocat App",
    "description": "",
    "external_url": "https://example.com",
    "html_url": "https://github.com/apps/octoapp",
    "created_at": "2017-07-08T16:18:44-04:00",
    "updated_at": "2017-07-08T16:18:44-04:00",
    "permissions": {
      "metadata": "read",
      "contents": "read",
      "issues": "write",
      "single_file": "write"
    },
    "events": [
      "push",
      "pull_request"
    ]
  },
  "repository": {
    "id": 1296269,
    "node_id": "MDEwOlJlcG9zaXRvcnkxMjk2MjY5",
    "name": "Hello-World",
    "full_name": "octocat/Hello-World",
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
      "admin": false,
      "push": false,
      "pull": true
    },
    "temp_clone_token": "ABTLWHOULUVAXGTRYU7OC2876QJ2O",
    "delete_branch_on_merge": true,
    "subscribers_count": 42,
    "network_count": 0
  },
  "head_commit": {
    "id": "7fd1a60b01f91b314f59955a4e4d4e80d8edf11d",
    "tree_id": "7fd1a60b01f91b314f59955a4e4d4e80d8edf11d",
    "message": "Merge pull request #6 from Spaceghost/patch-1\n\nNew line at end of file.",
    "timestamp": "2016-10-10T00:00:00Z",
    "author": {
      "name": "The Octocat",
      "email": "octocat@nowhere.com"
    },
    "committer": {
      "name": "The Octocat",
      "email": "octocat@nowhere.com"
    }
  },
  "latest_check_runs_count": 1,
  "check_runs_url": "https://api.github.com/repos/octocat/Hello-World/check-suites/5/check-runs"
}
```

## Rerequest a check suite
Triggers GitHub to rerequest an existing check suite, without pushing new code to a repository. This endpoint will trigger thecheck_suitewebhookevent with the actionrerequested. When a check suite isrerequested, itsstatusis reset toqueuedand theconclusionis cleared.

```
check_suite
```

### Fine-grained access tokens for "Rerequest a check suite"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Checks" repository permissions (write)

### Parameters for "Rerequest a check suite"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
check_suite_idintegerRequiredThe unique identifier of the check suite.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.

```
check_suite_id
```
The unique identifier of the check suite.

### HTTP response status codes for "Rerequest a check suite"

[TABLE]
Status code | Description
201 | Created
[/TABLE]
Created

### Code samples for "Rerequest a check suite"

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
  https://api.github.com/repos/OWNER/REPO/check-suites/CHECK_SUITE_ID/rerequest
```

#### Response
- Example response
- Response schema

```
Status: 201
```

## List check suites for a Git reference
Lists check suites for a commitref. Therefcan be a SHA, branch name, or a tag name.
Note
The endpoints to manage checks only look for pushes in the repository where the check suite or check run were created. Pushes to a branch in a forked repository are not detected and return an emptypull_requestsarray and anullvalue forhead_branch.
OAuth app tokens and personal access tokens (classic) need thereposcope to use this endpoint on a private repository.

### Fine-grained access tokens for "List check suites for a Git reference"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Checks" repository permissions (read)
This endpoint can be used without authentication or the aforementioned permissions if only public resources are requested.

### Parameters for "List check suites for a Git reference"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
refstringRequiredThe commit reference. Can be a commit SHA, branch name (heads/BRANCH_NAME), or tag name (tags/TAG_NAME). For more information, see "Git References" in the Git documentation.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.
The commit reference. Can be a commit SHA, branch name (heads/BRANCH_NAME), or tag name (tags/TAG_NAME). For more information, see "Git References" in the Git documentation.

[TABLE]
Name, Type, Description
app_idintegerFilters check suites by GitHub Appid.
check_namestringReturns check runs with the specifiedname.
per_pageintegerThe number of results per page_number (max 100). For more information, see "Using pagination in the REST API."Default:30
pageintegerThe page_number number of the results to fetch. For more information, see "Using pagination in the REST API."Default:1
[/TABLE]
Filters check suites by GitHub Appid.
Returns check runs with the specifiedname.
The number of results per page_number (max 100). For more information, see "Using pagination in the REST API."
Default:30
The page_number number of the results to fetch. For more information, see "Using pagination in the REST API."
Default:1

### HTTP response status codes for "List check suites for a Git reference"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "List check suites for a Git reference"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/commits/REF/check-suites
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "total_count": 1,
  "check_suites": [
    {
      "id": 5,
      "node_id": "MDEwOkNoZWNrU3VpdGU1",
      "head_branch": "master",
      "head_sha": "d6fde92930d4715a2b49857d24b940956b26d2d3",
      "status": "completed",
      "conclusion": "neutral",
      "url": "https://api.github.com/repos/github/hello-world/check-suites/5",
      "before": "146e867f55c26428e5f9fade55a9bbf5e95a7912",
      "after": "d6fde92930d4715a2b49857d24b940956b26d2d3",
      "pull_requests": [],
      "app": {
        "id": 1,
        "slug": "octoapp",
        "node_id": "MDExOkludGVncmF0aW9uMQ==",
        "owner": {
          "login": "github",
          "id": 1,
          "node_id": "MDEyOk9yZ2FuaXphdGlvbjE=",
          "url": "https://api.github.com/orgs/github",
          "repos_url": "https://api.github.com/orgs/github/repos",
          "events_url": "https://api.github.com/orgs/github/events",
          "avatar_url": "https://github.com/images/error/octocat_happy.gif",
          "gravatar_id": "",
          "html_url": "https://github.com/octocat",
          "followers_url": "https://api.github.com/users/octocat/followers",
          "following_url": "https://api.github.com/users/octocat/following{/other_user}",
          "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
          "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
          "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
          "organizations_url": "https://api.github.com/users/octocat/orgs",
          "received_events_url": "https://api.github.com/users/octocat/received_events",
          "type": "User",
          "site_admin": true
        },
        "name": "Octocat App",
        "description": "",
        "external_url": "https://example.com",
        "html_url": "https://github.com/apps/octoapp",
        "created_at": "2017-07-08T16:18:44-04:00",
        "updated_at": "2017-07-08T16:18:44-04:00",
        "permissions": {
          "metadata": "read",
          "contents": "read",
          "issues": "write",
          "single_file": "write"
        },
        "events": [
          "push",
          "pull_request"
        ]
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
        "temp_clone_token": "ABTLWHOULUVAXGTRYU7OC2876QJ2O",
        "delete_branch_on_merge": true,
        "subscribers_count": 42,
        "network_count": 0
      },
      "created_at": "2011-01-26T19:01:12Z",
      "updated_at": "2011-01-26T19:14:43Z",
      "head_commit": {
        "id": "7fd1a60b01f91b314f59955a4e4d4e80d8edf11d",
        "tree_id": "7fd1a60b01f91b314f59955a4e4d4e80d8edf11d",
        "message": "Merge pull request #6 from Spaceghost/patch-1\n\nNew line at end of file.",
        "timestamp": "2016-10-10T00:00:00Z",
        "author": {
          "name": "The Octocat",
          "email": "octocat@nowhere.com"
        },
        "committer": {
          "name": "The Octocat",
          "email": "octocat@nowhere.com"
        }
      },
      "latest_check_runs_count": 1,
      "check_runs_url": "https://api.github.com/repos/octocat/Hello-World/check-suites/5/check-runs"
    }
  ]
}
```