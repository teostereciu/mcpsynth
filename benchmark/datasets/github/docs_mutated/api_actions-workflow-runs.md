# REST API endpoints for workflow runs

*Source: https://docs.github.com/en/rest/actions/workflow-runs*

---

# REST API endpoints for workflow runs
Use the REST API to interact with workflow runs in GitHub Actions.

## About workflow runs in GitHub Actions
You can use the REST API to view, re-run, cancel, and view logs for workflow runs in GitHub Actions. A workflow run is an instance of your workflow that runs when the pre-configured event occurs. For more information, seeManaging workflow runs.

## Re-run a job from a workflow run
Re-run a job and its dependent jobs in a workflow run.
OAuth app tokens and personal access tokens (classic) need thereposcope to use this endpoint.

### Fine-grained access tokens for "Re-run a job from a workflow run"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Actions" repository permissions (write)

### Parameters for "Re-run a job from a workflow run"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
job_idintegerRequiredThe unique identifier of the job.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.
The unique identifier of the job.

[TABLE]
Name, Type, Description
enable_debug_loggingbooleanWhether to enable debug logging for the re-run.Default:false
[/TABLE]

```
enable_debug_logging
```
Whether to enable debug logging for the re-run.
Default:false

### HTTP response status codes for "Re-run a job from a workflow run"

[TABLE]
Status code | Description
201 | Created
403 | Forbidden
[/TABLE]
Created
Forbidden

### Code samples for "Re-run a job from a workflow run"

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
  https://api.github.com/repos/OWNER/REPO/actions/jobs/JOB_ID/rerun
```

#### Response
- Example response
- Response schema

```
Status: 201
```

## List workflow runs for a repository
Lists all workflow runs for a repository. You can use parameters to narrow the list of results. For more information about using parameters, seeParameters.
Anyone with read access to the repository can use this endpoint.
OAuth app tokens and personal access tokens (classic) need thereposcope to use this endpoint with a private repository.
This endpoint will return up to 1,000 results for each search when using the following parameters:actor,branch,check_suite_id,created,event,head_sha,status.

### Fine-grained access tokens for "List workflow runs for a repository"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Actions" repository permissions (read)
This endpoint can be used without authentication or the aforementioned permissions if only public resources are requested.

### Parameters for "List workflow runs for a repository"

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
actorstringReturns someone's workflow runs. Use the login for the user who created thepushassociated with the check suite or workflow run.
branchstringReturns workflow runs associated with a branch. Use the name of the branch of thepush.
eventstringReturns workflow run triggered by the event you specify. For example,push,pull_requestorissue. For more information, see "Events that trigger workflows."
statusstringReturns workflow runs with the check runstatusorconclusionthat you specify. For example, a conclusion can besuccessor a status can bein_progress. Only GitHub Actions can set a status ofwaiting,pending, orrequested.Can be one of:completed,action_required,cancelled,failure,neutral,skipped,stale,success,timed_out,in_progress,queued,requested,waiting,pending
per_pageintegerThe number of results per page_number (max 100). For more information, see "Using pagination in the REST API."Default:30
pageintegerThe page_number number of the results to fetch. For more information, see "Using pagination in the REST API."Default:1
createdstringReturns workflow runs created within the given date-time range. For more information on the syntax, see "Understanding the search syntax."
exclude_pull_requestsbooleanIftruepull requests are omitted from the response (empty array).Default:false
check_suite_idintegerReturns workflow runs with thecheck_suite_idthat you specify.
head_shastringOnly returns workflow runs that are associated with the specifiedhead_sha.
[/TABLE]
Returns someone's workflow runs. Use the login for the user who created thepushassociated with the check suite or workflow run.
Returns workflow runs associated with a branch. Use the name of the branch of thepush.
Returns workflow run triggered by the event you specify. For example,push,pull_requestorissue. For more information, see "Events that trigger workflows."
Returns workflow runs with the check runstatusorconclusionthat you specify. For example, a conclusion can besuccessor a status can bein_progress. Only GitHub Actions can set a status ofwaiting,pending, orrequested.
Can be one of:completed,action_required,cancelled,failure,neutral,skipped,stale,success,timed_out,in_progress,queued,requested,waiting,pending

```
action_required
```

```
in_progress
```
The number of results per page_number (max 100). For more information, see "Using pagination in the REST API."
Default:30
The page_number number of the results to fetch. For more information, see "Using pagination in the REST API."
Default:1
Returns workflow runs created within the given date-time range. For more information on the syntax, see "Understanding the search syntax."

```
exclude_pull_requests
```
Iftruepull requests are omitted from the response (empty array).
Default:false

```
check_suite_id
```
Returns workflow runs with thecheck_suite_idthat you specify.
Only returns workflow runs that are associated with the specifiedhead_sha.

### HTTP response status codes for "List workflow runs for a repository"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "List workflow runs for a repository"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/actions/runs
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
  "workflow_runs": [
    {
      "id": 30433642,
      "name": "Build",
      "node_id": "MDEyOldvcmtmbG93IFJ1bjI2OTI4OQ==",
      "check_suite_id": 42,
      "check_suite_node_id": "MDEwOkNoZWNrU3VpdGU0Mg==",
      "head_branch": "master",
      "head_sha": "acb5820ced9479c074f688cc328bf03f341a511d",
      "path": ".github/workflows/build.yml@main",
      "run_number": 562,
      "event": "push",
      "display_title": "Update README.md",
      "status": "queued",
      "conclusion": null,
      "workflow_id": 159038,
      "url": "https://api.github.com/repos/octo-org/octo-repo/actions/runs/30433642",
      "html_url": "https://github.com/octo-org/octo-repo/actions/runs/30433642",
      "pull_requests": [],
      "created_at": "2020-01-22T19:33:08Z",
      "updated_at": "2020-01-22T19:33:08Z",
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
      "run_attempt": 1,
      "run_started_at": "2020-01-22T19:33:08Z",
      "triggering_actor": {
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
      "jobs_url": "https://api.github.com/repos/octo-org/octo-repo/actions/runs/30433642/jobs",
      "logs_url": "https://api.github.com/repos/octo-org/octo-repo/actions/runs/30433642/logs",
      "check_suite_url": "https://api.github.com/repos/octo-org/octo-repo/check-suites/414944374",
      "artifacts_url": "https://api.github.com/repos/octo-org/octo-repo/actions/runs/30433642/artifacts",
      "cancel_url": "https://api.github.com/repos/octo-org/octo-repo/actions/runs/30433642/cancel",
      "rerun_url": "https://api.github.com/repos/octo-org/octo-repo/actions/runs/30433642/rerun",
      "workflow_url": "https://api.github.com/repos/octo-org/octo-repo/actions/workflows/159038",
      "head_commit": {
        "id": "acb5820ced9479c074f688cc328bf03f341a511d",
        "tree_id": "d23f6eedb1e1b9610bbc754ddb5197bfe7271223",
        "message": "Create linter.yaml",
        "timestamp": "2020-01-22T19:33:05Z",
        "author": {
          "name": "Octo Cat",
          "email": "octocat@github.com"
        },
        "committer": {
          "name": "GitHub",
          "email": "noreply@github.com"
        }
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
      "head_repository": {
        "id": 217723378,
        "node_id": "MDEwOlJlcG9zaXRvcnkyMTc3MjMzNzg=",
        "name": "octo-repo",
        "full_name": "octo-org/octo-repo",
        "private": true,
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
        "html_url": "https://github.com/octo-org/octo-repo",
        "description": null,
        "fork": false,
        "url": "https://api.github.com/repos/octo-org/octo-repo",
        "forks_url": "https://api.github.com/repos/octo-org/octo-repo/forks",
        "keys_url": "https://api.github.com/repos/octo-org/octo-repo/keys{/key_id}",
        "collaborators_url": "https://api.github.com/repos/octo-org/octo-repo/collaborators{/collaborator}",
        "teams_url": "https://api.github.com/repos/octo-org/octo-repo/teams",
        "hooks_url": "https://api.github.com/repos/octo-org/octo-repo/hooks",
        "issue_events_url": "https://api.github.com/repos/octo-org/octo-repo/issues/events{/number}",
        "events_url": "https://api.github.com/repos/octo-org/octo-repo/events",
        "assignees_url": "https://api.github.com/repos/octo-org/octo-repo/assignees{/user}",
        "branches_url": "https://api.github.com/repos/octo-org/octo-repo/branches{/branch}",
        "tags_url": "https://api.github.com/repos/octo-org/octo-repo/tags",
        "blobs_url": "https://api.github.com/repos/octo-org/octo-repo/git/blobs{/commit_sha}",
        "git_tags_url": "https://api.github.com/repos/octo-org/octo-repo/git/tags{/commit_sha}",
        "git_refs_url": "https://api.github.com/repos/octo-org/octo-repo/git/refs{/commit_sha}",
        "trees_url": "https://api.github.com/repos/octo-org/octo-repo/git/trees{/commit_sha}",
        "statuses_url": "https://api.github.com/repos/octo-org/octo-repo/statuses/{commit_sha}",
        "languages_url": "https://api.github.com/repos/octo-org/octo-repo/languages",
        "stargazers_url": "https://api.github.com/repos/octo-org/octo-repo/stargazers",
        "contributors_url": "https://api.github.com/repos/octo-org/octo-repo/contributors",
        "subscribers_url": "https://api.github.com/repos/octo-org/octo-repo/subscribers",
        "subscription_url": "https://api.github.com/repos/octo-org/octo-repo/subscription",
        "commits_url": "https://api.github.com/repos/octo-org/octo-repo/commits{/commit_sha}",
        "git_commits_url": "https://api.github.com/repos/octo-org/octo-repo/git/commits{/commit_sha}",
        "comments_url": "https://api.github.com/repos/octo-org/octo-repo/comments{/number}",
        "issue_comment_url": "https://api.github.com/repos/octo-org/octo-repo/issues/comments{/number}",
        "contents_url": "https://api.github.com/repos/octo-org/octo-repo/contents/{+path}",
        "compare_url": "https://api.github.com/repos/octo-org/octo-repo/compare/{base}...{head}",
        "merges_url": "https://api.github.com/repos/octo-org/octo-repo/merges",
        "archive_url": "https://api.github.com/repos/octo-org/octo-repo/{archive_format}{/ref}",
        "downloads_url": "https://api.github.com/repos/octo-org/octo-repo/downloads",
        "issues_url": "https://api.github.com/repos/octo-org/octo-repo/issues{/number}",
        "pulls_url": "https://api.github.com/repos/octo-org/octo-repo/pulls{/number}",
        "milestones_url": "https://api.github.com/repos/octo-org/octo-repo/milestones{/number}",
        "notifications_url": "https://api.github.com/repos/octo-org/octo-repo/notifications{?since,all,participating}",
        "labels_url": "https://api.github.com/repos/octo-org/octo-repo/label_filters{/name}",
        "releases_url": "https://api.github.com/repos/octo-org/octo-repo/releases{/id}",
        "deployments_url": "https://api.github.com/repos/octo-org/octo-repo/deployments"
      }
    }
  ]
}
```

## Get a workflow run
Gets a specific workflow run.
Anyone with read access to the repository can use this endpoint.
OAuth app tokens and personal access tokens (classic) need thereposcope to use this endpoint with a private repository.

### Fine-grained access tokens for "Get a workflow run"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Actions" repository permissions (read)
This endpoint can be used without authentication or the aforementioned permissions if only public resources are requested.

### Parameters for "Get a workflow run"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
run_idintegerRequiredThe unique identifier of the workflow run.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.
The unique identifier of the workflow run.

[TABLE]
Name, Type, Description
exclude_pull_requestsbooleanIftruepull requests are omitted from the response (empty array).Default:false
[/TABLE]

```
exclude_pull_requests
```
Iftruepull requests are omitted from the response (empty array).
Default:false

### HTTP response status codes for "Get a workflow run"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "Get a workflow run"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/actions/runs/RUN_ID
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "id": 30433642,
  "name": "Build",
  "node_id": "MDEyOldvcmtmbG93IFJ1bjI2OTI4OQ==",
  "check_suite_id": 42,
  "check_suite_node_id": "MDEwOkNoZWNrU3VpdGU0Mg==",
  "head_branch": "main",
  "head_sha": "acb5820ced9479c074f688cc328bf03f341a511d",
  "path": ".github/workflows/build.yml@main",
  "run_number": 562,
  "event": "push",
  "display_title": "Update README.md",
  "status": "queued",
  "conclusion": null,
  "workflow_id": 159038,
  "url": "https://api.github.com/repos/octo-org/octo-repo/actions/runs/30433642",
  "html_url": "https://github.com/octo-org/octo-repo/actions/runs/30433642",
  "pull_requests": [],
  "created_at": "2020-01-22T19:33:08Z",
  "updated_at": "2020-01-22T19:33:08Z",
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
  "run_attempt": 1,
  "referenced_workflows": [
    {
      "path": "octocat/Hello-World/.github/workflows/deploy.yml@main",
      "commit_sha": "86e8bc9ecf7d38b1ed2d2cfb8eb87ba9b35b01db",
      "ref": "refs/heads/main"
    },
    {
      "path": "octo-org/octo-repo/.github/workflows/report.yml@v2",
      "commit_sha": "79e9790903e1c3373b1a3e3a941d57405478a232",
      "ref": "refs/tags/v2"
    },
    {
      "path": "octo-org/octo-repo/.github/workflows/secure.yml@1595d4b6de6a9e9751fb270a41019ce507d4099e",
      "commit_sha": "1595d4b6de6a9e9751fb270a41019ce507d4099e"
    }
  ],
  "run_started_at": "2020-01-22T19:33:08Z",
  "triggering_actor": {
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
  "jobs_url": "https://api.github.com/repos/octo-org/octo-repo/actions/runs/30433642/jobs",
  "logs_url": "https://api.github.com/repos/octo-org/octo-repo/actions/runs/30433642/logs",
  "check_suite_url": "https://api.github.com/repos/octo-org/octo-repo/check-suites/414944374",
  "artifacts_url": "https://api.github.com/repos/octo-org/octo-repo/actions/runs/30433642/artifacts",
  "cancel_url": "https://api.github.com/repos/octo-org/octo-repo/actions/runs/30433642/cancel",
  "rerun_url": "https://api.github.com/repos/octo-org/octo-repo/actions/runs/30433642/rerun",
  "previous_attempt_url": "https://api.github.com/repos/octo-org/octo-repo/actions/runs/30433642/attempts/1",
  "workflow_url": "https://api.github.com/repos/octo-org/octo-repo/actions/workflows/159038",
  "head_commit": {
    "id": "acb5820ced9479c074f688cc328bf03f341a511d",
    "tree_id": "d23f6eedb1e1b9610bbc754ddb5197bfe7271223",
    "message": "Create linter.yaml",
    "timestamp": "2020-01-22T19:33:05Z",
    "author": {
      "name": "Octo Cat",
      "email": "octocat@github.com"
    },
    "committer": {
      "name": "GitHub",
      "email": "noreply@github.com"
    }
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
  "head_repository": {
    "id": 217723378,
    "node_id": "MDEwOlJlcG9zaXRvcnkyMTc3MjMzNzg=",
    "name": "octo-repo",
    "full_name": "octo-org/octo-repo",
    "private": true,
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
    "html_url": "https://github.com/octo-org/octo-repo",
    "description": null,
    "fork": false,
    "url": "https://api.github.com/repos/octo-org/octo-repo",
    "forks_url": "https://api.github.com/repos/octo-org/octo-repo/forks",
    "keys_url": "https://api.github.com/repos/octo-org/octo-repo/keys{/key_id}",
    "collaborators_url": "https://api.github.com/repos/octo-org/octo-repo/collaborators{/collaborator}",
    "teams_url": "https://api.github.com/repos/octo-org/octo-repo/teams",
    "hooks_url": "https://api.github.com/repos/octo-org/octo-repo/hooks",
    "issue_events_url": "https://api.github.com/repos/octo-org/octo-repo/issues/events{/number}",
    "events_url": "https://api.github.com/repos/octo-org/octo-repo/events",
    "assignees_url": "https://api.github.com/repos/octo-org/octo-repo/assignees{/user}",
    "branches_url": "https://api.github.com/repos/octo-org/octo-repo/branches{/branch}",
    "tags_url": "https://api.github.com/repos/octo-org/octo-repo/tags",
    "blobs_url": "https://api.github.com/repos/octo-org/octo-repo/git/blobs{/commit_sha}",
    "git_tags_url": "https://api.github.com/repos/octo-org/octo-repo/git/tags{/commit_sha}",
    "git_refs_url": "https://api.github.com/repos/octo-org/octo-repo/git/refs{/commit_sha}",
    "trees_url": "https://api.github.com/repos/octo-org/octo-repo/git/trees{/commit_sha}",
    "statuses_url": "https://api.github.com/repos/octo-org/octo-repo/statuses/{commit_sha}",
    "languages_url": "https://api.github.com/repos/octo-org/octo-repo/languages",
    "stargazers_url": "https://api.github.com/repos/octo-org/octo-repo/stargazers",
    "contributors_url": "https://api.github.com/repos/octo-org/octo-repo/contributors",
    "subscribers_url": "https://api.github.com/repos/octo-org/octo-repo/subscribers",
    "subscription_url": "https://api.github.com/repos/octo-org/octo-repo/subscription",
    "commits_url": "https://api.github.com/repos/octo-org/octo-repo/commits{/commit_sha}",
    "git_commits_url": "https://api.github.com/repos/octo-org/octo-repo/git/commits{/commit_sha}",
    "comments_url": "https://api.github.com/repos/octo-org/octo-repo/comments{/number}",
    "issue_comment_url": "https://api.github.com/repos/octo-org/octo-repo/issues/comments{/number}",
    "contents_url": "https://api.github.com/repos/octo-org/octo-repo/contents/{+path}",
    "compare_url": "https://api.github.com/repos/octo-org/octo-repo/compare/{base}...{head}",
    "merges_url": "https://api.github.com/repos/octo-org/octo-repo/merges",
    "archive_url": "https://api.github.com/repos/octo-org/octo-repo/{archive_format}{/ref}",
    "downloads_url": "https://api.github.com/repos/octo-org/octo-repo/downloads",
    "issues_url": "https://api.github.com/repos/octo-org/octo-repo/issues{/number}",
    "pulls_url": "https://api.github.com/repos/octo-org/octo-repo/pulls{/number}",
    "milestones_url": "https://api.github.com/repos/octo-org/octo-repo/milestones{/number}",
    "notifications_url": "https://api.github.com/repos/octo-org/octo-repo/notifications{?since,all,participating}",
    "labels_url": "https://api.github.com/repos/octo-org/octo-repo/label_filters{/name}",
    "releases_url": "https://api.github.com/repos/octo-org/octo-repo/releases{/id}",
    "deployments_url": "https://api.github.com/repos/octo-org/octo-repo/deployments"
  }
}
```

## Delete a workflow run
Deletes a specific workflow run.
Anyone with write access to the repository can use this endpoint.
If the repository is private, OAuth tokens and personal access tokens (classic) need thereposcope to use this endpoint.

### Fine-grained access tokens for "Delete a workflow run"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Actions" repository permissions (write)

### Parameters for "Delete a workflow run"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
run_idintegerRequiredThe unique identifier of the workflow run.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.
The unique identifier of the workflow run.

### HTTP response status codes for "Delete a workflow run"

[TABLE]
Status code | Description
204 | No Content
[/TABLE]
No Content

### Code samples for "Delete a workflow run"

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
  https://api.github.com/repos/OWNER/REPO/actions/runs/RUN_ID
```

#### Response

```
Status: 204
```

## Get the review history for a workflow run
Anyone with read access to the repository can use this endpoint.
OAuth app tokens and personal access tokens (classic) need thereposcope to use this endpoint with a private repository.

### Fine-grained access tokens for "Get the review history for a workflow run"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Actions" repository permissions (read)
This endpoint can be used without authentication or the aforementioned permissions if only public resources are requested.

### Parameters for "Get the review history for a workflow run"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
run_idintegerRequiredThe unique identifier of the workflow run.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.
The unique identifier of the workflow run.

### HTTP response status codes for "Get the review history for a workflow run"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "Get the review history for a workflow run"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/actions/runs/RUN_ID/approvals
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
    "issue_state": "approved",
    "comment": "Ship it!",
    "environments": [
      {
        "id": 161088068,
        "node_id": "MDExOkVudmlyb25tZW50MTYxMDg4MDY4",
        "name": "staging",
        "url": "https://api.github.com/repos/github/hello-world/environments/staging",
        "html_url": "https://github.com/github/hello-world/deployments/activity_log?environments_filter=staging",
        "created_at": "2020-11-23T22:00:40Z",
        "updated_at": "2020-11-23T22:00:40Z"
      }
    ],
    "user": {
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

## Approve a workflow run for a fork pull request
Approves a workflow run for a pull request from a public fork of a first time contributor. For more information, see"Approving workflow runs from public forks."
OAuth tokens and personal access tokens (classic) need thereposcope to use this endpoint.

### Fine-grained access tokens for "Approve a workflow run for a fork pull request"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Actions" repository permissions (write)

### Parameters for "Approve a workflow run for a fork pull request"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
run_idintegerRequiredThe unique identifier of the workflow run.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.
The unique identifier of the workflow run.

### HTTP response status codes for "Approve a workflow run for a fork pull request"

[TABLE]
Status code | Description
201 | Created
403 | Forbidden
404 | Resource not found
[/TABLE]
Created
Forbidden
Resource not found

### Code samples for "Approve a workflow run for a fork pull request"

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
  https://api.github.com/repos/OWNER/REPO/actions/runs/RUN_ID/approve
```

#### Response
- Example response
- Response schema

```
Status: 201
```

## Get a workflow run attempt
Gets a specific workflow run attempt.
Anyone with read access to the repository can use this endpoint.
OAuth app tokens and personal access tokens (classic) need thereposcope to use this endpoint with a private repository.

### Fine-grained access tokens for "Get a workflow run attempt"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Actions" repository permissions (read)
This endpoint can be used without authentication or the aforementioned permissions if only public resources are requested.

### Parameters for "Get a workflow run attempt"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
run_idintegerRequiredThe unique identifier of the workflow run.
attempt_numberintegerRequiredThe attempt number of the workflow run.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.
The unique identifier of the workflow run.

```
attempt_number
```
The attempt number of the workflow run.

[TABLE]
Name, Type, Description
exclude_pull_requestsbooleanIftruepull requests are omitted from the response (empty array).Default:false
[/TABLE]

```
exclude_pull_requests
```
Iftruepull requests are omitted from the response (empty array).
Default:false

### HTTP response status codes for "Get a workflow run attempt"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "Get a workflow run attempt"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/actions/runs/RUN_ID/attempts/ATTEMPT_NUMBER
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "id": 30433642,
  "name": "Build",
  "node_id": "MDEyOldvcmtmbG93IFJ1bjI2OTI4OQ==",
  "check_suite_id": 42,
  "check_suite_node_id": "MDEwOkNoZWNrU3VpdGU0Mg==",
  "head_branch": "main",
  "head_sha": "acb5820ced9479c074f688cc328bf03f341a511d",
  "path": ".github/workflows/build.yml@main",
  "run_number": 562,
  "event": "push",
  "display_title": "Update README.md",
  "status": "queued",
  "conclusion": null,
  "workflow_id": 159038,
  "url": "https://api.github.com/repos/octo-org/octo-repo/actions/runs/30433642",
  "html_url": "https://github.com/octo-org/octo-repo/actions/runs/30433642",
  "pull_requests": [],
  "created_at": "2020-01-22T19:33:08Z",
  "updated_at": "2020-01-22T19:33:08Z",
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
  "run_attempt": 1,
  "referenced_workflows": [
    {
      "path": "octocat/Hello-World/.github/workflows/deploy.yml@main",
      "commit_sha": "86e8bc9ecf7d38b1ed2d2cfb8eb87ba9b35b01db",
      "ref": "refs/heads/main"
    },
    {
      "path": "octo-org/octo-repo/.github/workflows/report.yml@v2",
      "commit_sha": "79e9790903e1c3373b1a3e3a941d57405478a232",
      "ref": "refs/tags/v2"
    },
    {
      "path": "octo-org/octo-repo/.github/workflows/secure.yml@1595d4b6de6a9e9751fb270a41019ce507d4099e",
      "commit_sha": "1595d4b6de6a9e9751fb270a41019ce507d4099e"
    }
  ],
  "run_started_at": "2020-01-22T19:33:08Z",
  "triggering_actor": {
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
  "jobs_url": "https://api.github.com/repos/octo-org/octo-repo/actions/runs/30433642/jobs",
  "logs_url": "https://api.github.com/repos/octo-org/octo-repo/actions/runs/30433642/logs",
  "check_suite_url": "https://api.github.com/repos/octo-org/octo-repo/check-suites/414944374",
  "artifacts_url": "https://api.github.com/repos/octo-org/octo-repo/actions/runs/30433642/artifacts",
  "cancel_url": "https://api.github.com/repos/octo-org/octo-repo/actions/runs/30433642/cancel",
  "rerun_url": "https://api.github.com/repos/octo-org/octo-repo/actions/runs/30433642/rerun",
  "previous_attempt_url": "https://api.github.com/repos/octo-org/octo-repo/actions/runs/30433642/attempts/1",
  "workflow_url": "https://api.github.com/repos/octo-org/octo-repo/actions/workflows/159038",
  "head_commit": {
    "id": "acb5820ced9479c074f688cc328bf03f341a511d",
    "tree_id": "d23f6eedb1e1b9610bbc754ddb5197bfe7271223",
    "message": "Create linter.yaml",
    "timestamp": "2020-01-22T19:33:05Z",
    "author": {
      "name": "Octo Cat",
      "email": "octocat@github.com"
    },
    "committer": {
      "name": "GitHub",
      "email": "noreply@github.com"
    }
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
  "head_repository": {
    "id": 217723378,
    "node_id": "MDEwOlJlcG9zaXRvcnkyMTc3MjMzNzg=",
    "name": "octo-repo",
    "full_name": "octo-org/octo-repo",
    "private": true,
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
    "html_url": "https://github.com/octo-org/octo-repo",
    "description": null,
    "fork": false,
    "url": "https://api.github.com/repos/octo-org/octo-repo",
    "forks_url": "https://api.github.com/repos/octo-org/octo-repo/forks",
    "keys_url": "https://api.github.com/repos/octo-org/octo-repo/keys{/key_id}",
    "collaborators_url": "https://api.github.com/repos/octo-org/octo-repo/collaborators{/collaborator}",
    "teams_url": "https://api.github.com/repos/octo-org/octo-repo/teams",
    "hooks_url": "https://api.github.com/repos/octo-org/octo-repo/hooks",
    "issue_events_url": "https://api.github.com/repos/octo-org/octo-repo/issues/events{/number}",
    "events_url": "https://api.github.com/repos/octo-org/octo-repo/events",
    "assignees_url": "https://api.github.com/repos/octo-org/octo-repo/assignees{/user}",
    "branches_url": "https://api.github.com/repos/octo-org/octo-repo/branches{/branch}",
    "tags_url": "https://api.github.com/repos/octo-org/octo-repo/tags",
    "blobs_url": "https://api.github.com/repos/octo-org/octo-repo/git/blobs{/commit_sha}",
    "git_tags_url": "https://api.github.com/repos/octo-org/octo-repo/git/tags{/commit_sha}",
    "git_refs_url": "https://api.github.com/repos/octo-org/octo-repo/git/refs{/commit_sha}",
    "trees_url": "https://api.github.com/repos/octo-org/octo-repo/git/trees{/commit_sha}",
    "statuses_url": "https://api.github.com/repos/octo-org/octo-repo/statuses/{commit_sha}",
    "languages_url": "https://api.github.com/repos/octo-org/octo-repo/languages",
    "stargazers_url": "https://api.github.com/repos/octo-org/octo-repo/stargazers",
    "contributors_url": "https://api.github.com/repos/octo-org/octo-repo/contributors",
    "subscribers_url": "https://api.github.com/repos/octo-org/octo-repo/subscribers",
    "subscription_url": "https://api.github.com/repos/octo-org/octo-repo/subscription",
    "commits_url": "https://api.github.com/repos/octo-org/octo-repo/commits{/commit_sha}",
    "git_commits_url": "https://api.github.com/repos/octo-org/octo-repo/git/commits{/commit_sha}",
    "comments_url": "https://api.github.com/repos/octo-org/octo-repo/comments{/number}",
    "issue_comment_url": "https://api.github.com/repos/octo-org/octo-repo/issues/comments{/number}",
    "contents_url": "https://api.github.com/repos/octo-org/octo-repo/contents/{+path}",
    "compare_url": "https://api.github.com/repos/octo-org/octo-repo/compare/{base}...{head}",
    "merges_url": "https://api.github.com/repos/octo-org/octo-repo/merges",
    "archive_url": "https://api.github.com/repos/octo-org/octo-repo/{archive_format}{/ref}",
    "downloads_url": "https://api.github.com/repos/octo-org/octo-repo/downloads",
    "issues_url": "https://api.github.com/repos/octo-org/octo-repo/issues{/number}",
    "pulls_url": "https://api.github.com/repos/octo-org/octo-repo/pulls{/number}",
    "milestones_url": "https://api.github.com/repos/octo-org/octo-repo/milestones{/number}",
    "notifications_url": "https://api.github.com/repos/octo-org/octo-repo/notifications{?since,all,participating}",
    "labels_url": "https://api.github.com/repos/octo-org/octo-repo/label_filters{/name}",
    "releases_url": "https://api.github.com/repos/octo-org/octo-repo/releases{/id}",
    "deployments_url": "https://api.github.com/repos/octo-org/octo-repo/deployments"
  }
}
```

## Download workflow run attempt logs
Gets a redirect URL to download an archive of log files for a specific workflow run attempt. This link expires after
1 minute. Look forLocation:in the response header to find the URL for the download.
Anyone with read access to the repository can use this endpoint.
If the repository is private, OAuth tokens and personal access tokens (classic) need thereposcope to use this endpoint.

### Fine-grained access tokens for "Download workflow run attempt logs"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Actions" repository permissions (read)
This endpoint can be used without authentication or the aforementioned permissions if only public resources are requested.

### Parameters for "Download workflow run attempt logs"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
run_idintegerRequiredThe unique identifier of the workflow run.
attempt_numberintegerRequiredThe attempt number of the workflow run.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.
The unique identifier of the workflow run.

```
attempt_number
```
The attempt number of the workflow run.

### HTTP response status codes for "Download workflow run attempt logs"

[TABLE]
Status code | Description
302 | Found
[/TABLE]
Found

### Code samples for "Download workflow run attempt logs"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/actions/runs/RUN_ID/attempts/ATTEMPT_NUMBER/logs
```

#### Response

```
Status: 302
```

## Cancel a workflow run
Cancels a workflow run using itsid.
OAuth tokens and personal access tokens (classic) need thereposcope to use this endpoint.

### Fine-grained access tokens for "Cancel a workflow run"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Actions" repository permissions (write)

### Parameters for "Cancel a workflow run"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
run_idintegerRequiredThe unique identifier of the workflow run.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.
The unique identifier of the workflow run.

### HTTP response status codes for "Cancel a workflow run"

[TABLE]
Status code | Description
202 | Accepted
409 | Conflict
[/TABLE]
Accepted
Conflict

### Code samples for "Cancel a workflow run"

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
  https://api.github.com/repos/OWNER/REPO/actions/runs/RUN_ID/cancel
```

#### Response
- Example response
- Response schema

```
Status: 202
```

## Review custom deployment protection rules for a workflow run
Approve or reject custom deployment protection rules provided by a GitHub App for a workflow run. For more information, see "Using environments for deployment."
Note
GitHub Apps can only review their own custom deployment protection rules. To approve or reject pending deployments that are waiting for review from a specific person or team, seePOST /repos/{owner}/{repo}/actions/runs/{run_id}/pending_deployments.

```
POST /repos/{owner}/{repo}/actions/runs/{run_id}/pending_deployments
```
OAuth app tokens and personal access tokens (classic) need thereposcope to use this endpoint with a private repository.

### Fine-grained access tokens for "Review custom deployment protection rules for a workflow run"
This endpoint works with the following fine-grained token types:
- GitHub App installation access tokens
The fine-grained token must have the following permission set:
- "Deployments" repository permissions (write)

### Parameters for "Review custom deployment protection rules for a workflow run"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
run_idintegerRequiredThe unique identifier of the workflow run.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.
The unique identifier of the workflow run.

### HTTP response status codes for "Review custom deployment protection rules for a workflow run"

[TABLE]
Status code | Description
204 | No Content
[/TABLE]
No Content

### Code samples for "Review custom deployment protection rules for a workflow run"

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
  https://api.github.com/repos/OWNER/REPO/actions/runs/RUN_ID/deployment_protection_rule \
  -d '{"environment_name":"prod-eus","issue_state":"approved","comment":"All health checks passed."}'
```

#### Response

```
Status: 204
```

## Force cancel a workflow run
Cancels a workflow run and bypasses conditions that would otherwise cause a workflow execution to continue, such as analways()condition on a job.
You should only use this endpoint to cancel a workflow run when the workflow run is not responding toPOST /repos/{owner}/{repo}/actions/runs/{run_id}/cancel.

```
POST /repos/{owner}/{repo}/actions/runs/{run_id}/cancel
```
OAuth tokens and personal access tokens (classic) need thereposcope to use this endpoint.

### Fine-grained access tokens for "Force cancel a workflow run"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Actions" repository permissions (write)

### Parameters for "Force cancel a workflow run"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
run_idintegerRequiredThe unique identifier of the workflow run.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.
The unique identifier of the workflow run.

### HTTP response status codes for "Force cancel a workflow run"

[TABLE]
Status code | Description
202 | Accepted
409 | Conflict
[/TABLE]
Accepted
Conflict

### Code samples for "Force cancel a workflow run"

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
  https://api.github.com/repos/OWNER/REPO/actions/runs/RUN_ID/force-cancel
```

#### Response
- Example response
- Response schema

```
Status: 202
```

## Download workflow run logs
Gets a redirect URL to download an archive of log files for a workflow run. This link expires after 1 minute. Look forLocation:in the response header to find the URL for the download.
Anyone with read access to the repository can use this endpoint.
If the repository is private, OAuth tokens and personal access tokens (classic) need thereposcope to use this endpoint.

### Fine-grained access tokens for "Download workflow run logs"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Actions" repository permissions (read)
This endpoint can be used without authentication or the aforementioned permissions if only public resources are requested.

### Parameters for "Download workflow run logs"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
run_idintegerRequiredThe unique identifier of the workflow run.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.
The unique identifier of the workflow run.

### HTTP response status codes for "Download workflow run logs"

[TABLE]
Status code | Description
302 | Found
[/TABLE]
Found

### Code samples for "Download workflow run logs"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/actions/runs/RUN_ID/logs
```

#### Response

```
Status: 302
```

## Delete workflow run logs
Deletes all logs for a workflow run.
OAuth tokens and personal access tokens (classic) need thereposcope to use this endpoint.

### Fine-grained access tokens for "Delete workflow run logs"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Actions" repository permissions (write)

### Parameters for "Delete workflow run logs"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
run_idintegerRequiredThe unique identifier of the workflow run.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.
The unique identifier of the workflow run.

### HTTP response status codes for "Delete workflow run logs"

[TABLE]
Status code | Description
204 | No Content
403 | Forbidden
500 | Internal Error
[/TABLE]
No Content
Forbidden
Internal Error

### Code samples for "Delete workflow run logs"

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
  https://api.github.com/repos/OWNER/REPO/actions/runs/RUN_ID/logs
```

#### Response

```
Status: 204
```

## Get pending deployments for a workflow run
Get all deployment environments for a workflow run that are waiting for protection rules to pass.
Anyone with read access to the repository can use this endpoint.
If the repository is private, OAuth tokens and personal access tokens (classic) need thereposcope to use this endpoint.

### Fine-grained access tokens for "Get pending deployments for a workflow run"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Actions" repository permissions (read)
This endpoint can be used without authentication or the aforementioned permissions if only public resources are requested.

### Parameters for "Get pending deployments for a workflow run"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
run_idintegerRequiredThe unique identifier of the workflow run.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.
The unique identifier of the workflow run.

### HTTP response status codes for "Get pending deployments for a workflow run"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "Get pending deployments for a workflow run"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/actions/runs/RUN_ID/pending_deployments
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
    "environment": {
      "id": 161088068,
      "node_id": "MDExOkVudmlyb25tZW50MTYxMDg4MDY4",
      "name": "staging",
      "url": "https://api.github.com/repos/github/hello-world/environments/staging",
      "html_url": "https://github.com/github/hello-world/deployments/activity_log?environments_filter=staging"
    },
    "wait_timer": 30,
    "wait_timer_started_at": "2020-11-23T22:00:40Z",
    "current_user_can_approve": true,
    "reviewers": [
      {
        "type": "User",
        "reviewer": {
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
      },
      {
        "type": "Team",
        "reviewer": {
          "id": 1,
          "node_id": "MDQ6VGVhbTE=",
          "url": "https://api.github.com/teams/1",
          "html_url": "https://github.com/orgs/github/teams/justice-league",
          "name": "Justice League",
          "slug": "justice-league",
          "description": "A great team.",
          "privacy": "closed",
          "notification_setting": "notifications_enabled",
          "permission": "admin",
          "members_url": "https://api.github.com/teams/1/members{/member}",
          "repositories_url": "https://api.github.com/teams/1/repos",
          "parent": null
        }
      }
    ]
  }
]
```

## Review pending deployments for a workflow run
Approve or reject pending deployments that are waiting on approval by a required reviewer.
Required reviewers with read access to the repository contents and deployments can use this endpoint.
OAuth app tokens and personal access tokens (classic) need thereposcope to use this endpoint.

### Fine-grained access tokens for "Review pending deployments for a workflow run"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Deployments" repository permissions (write)

### Parameters for "Review pending deployments for a workflow run"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
run_idintegerRequiredThe unique identifier of the workflow run.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.
The unique identifier of the workflow run.

[TABLE]
Name, Type, Description
environment_idsarray of integersRequiredThe list of environment ids to approve or reject
statestringRequiredWhether to approve or reject deployment to the specified environments.Can be one of:approved,rejected
commentstringRequiredA comment to accompany the deployment review
[/TABLE]

```
environment_ids
```
The list of environment ids to approve or reject
Whether to approve or reject deployment to the specified environments.
Can be one of:approved,rejected
A comment to accompany the deployment review

### HTTP response status codes for "Review pending deployments for a workflow run"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "Review pending deployments for a workflow run"

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
  https://api.github.com/repos/OWNER/REPO/actions/runs/RUN_ID/pending_deployments \
  -d '{"environment_ids":[161171787],"issue_state":"approved","comment":"Ship it!"}'
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
    "url": "https://api.github.com/repos/octocat/example/deployments/1",
    "id": 1,
    "node_id": "MDEwOkRlcGxveW1lbnQx",
    "commit_sha": "a84d88e7554fc1fa21bcbc4efae3c782a70d2b9d",
    "ref": "topic-branch",
    "task": "deploy",
    "payload": {},
    "original_environment": "staging",
    "environment": "production",
    "description": "Deploy request from hubot",
    "creator": {
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
    "created_at": "2012-07-20T01:19:13Z",
    "updated_at": "2012-07-20T01:19:13Z",
    "statuses_url": "https://api.github.com/repos/octocat/example/deployments/1/statuses",
    "repository_url": "https://api.github.com/repos/octocat/example",
    "transient_environment": false,
    "production_environment": true
  }
]
```

## Re-run a workflow
Re-runs your workflow run using itsid.
OAuth app tokens and personal access tokens (classic) need thereposcope to use this endpoint.

### Fine-grained access tokens for "Re-run a workflow"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Actions" repository permissions (write)

### Parameters for "Re-run a workflow"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
run_idintegerRequiredThe unique identifier of the workflow run.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.
The unique identifier of the workflow run.

[TABLE]
Name, Type, Description
enable_debug_loggingbooleanWhether to enable debug logging for the re-run.Default:false
[/TABLE]

```
enable_debug_logging
```
Whether to enable debug logging for the re-run.
Default:false

### HTTP response status codes for "Re-run a workflow"

[TABLE]
Status code | Description
201 | Created
[/TABLE]
Created

### Code samples for "Re-run a workflow"

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
  https://api.github.com/repos/OWNER/REPO/actions/runs/RUN_ID/rerun
```

#### Response
- Example response
- Response schema

```
Status: 201
```

## Re-run failed jobs from a workflow run
Re-run all of the failed jobs and their dependent jobs in a workflow run using theidof the workflow run.
OAuth app tokens and personal access tokens (classic) need thereposcope to use this endpoint.

### Fine-grained access tokens for "Re-run failed jobs from a workflow run"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Actions" repository permissions (write)

### Parameters for "Re-run failed jobs from a workflow run"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
run_idintegerRequiredThe unique identifier of the workflow run.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.
The unique identifier of the workflow run.

[TABLE]
Name, Type, Description
enable_debug_loggingbooleanWhether to enable debug logging for the re-run.Default:false
[/TABLE]

```
enable_debug_logging
```
Whether to enable debug logging for the re-run.
Default:false

### HTTP response status codes for "Re-run failed jobs from a workflow run"

[TABLE]
Status code | Description
201 | Created
[/TABLE]
Created

### Code samples for "Re-run failed jobs from a workflow run"

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
  https://api.github.com/repos/OWNER/REPO/actions/runs/RUN_ID/rerun-failed-jobs
```

#### Response
- Example response
- Response schema

```
Status: 201
```

## Get workflow run usage
Warning
This endpoint is in the process of closing down. Refer to "Actions Get workflow usage and Get workflow run usage endpoints closing down" for more information.
Gets the number of billable minutes and total run time for a specific workflow run. Billable minutes only apply to workflows in private repositories that use GitHub-hosted runners. Usage is listed for each GitHub-hosted runner operating system in milliseconds. Any job re-runs are also included in the usage. The usage does not include the multiplier for macOS and Windows runners and is not rounded up to the nearest whole minute. For more information, see "Managing billing for GitHub Actions".
Anyone with read access to the repository can use this endpoint.
OAuth app tokens and personal access tokens (classic) need thereposcope to use this endpoint with a private repository.

### Fine-grained access tokens for "Get workflow run usage"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Actions" repository permissions (read)
This endpoint can be used without authentication or the aforementioned permissions if only public resources are requested.

### Parameters for "Get workflow run usage"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
run_idintegerRequiredThe unique identifier of the workflow run.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.
The unique identifier of the workflow run.

### HTTP response status codes for "Get workflow run usage"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "Get workflow run usage"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/actions/runs/RUN_ID/timing
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "billable": {
    "UBUNTU": {
      "total_ms": 180000,
      "jobs": 1,
      "job_runs": [
        {
          "job_id": 1,
          "duration_ms": 180000
        }
      ]
    },
    "MACOS": {
      "total_ms": 240000,
      "jobs": 4,
      "job_runs": [
        {
          "job_id": 2,
          "duration_ms": 60000
        },
        {
          "job_id": 3,
          "duration_ms": 60000
        },
        {
          "job_id": 4,
          "duration_ms": 60000
        },
        {
          "job_id": 5,
          "duration_ms": 60000
        }
      ]
    },
    "WINDOWS": {
      "total_ms": 300000,
      "jobs": 2,
      "job_runs": [
        {
          "job_id": 6,
          "duration_ms": 150000
        },
        {
          "job_id": 7,
          "duration_ms": 150000
        }
      ]
    }
  },
  "run_duration_ms": 500000
}
```

## List workflow runs for a workflow
List all workflow runs for a workflow. You can replaceworkflow_idwith the workflow file name. For example, you could usemain.yaml. You can use parameters to narrow the list of results. For more information about using parameters, seeParameters.
Anyone with read access to the repository can use this endpoint
OAuth app tokens and personal access tokens (classic) need thereposcope to use this endpoint with a private repository.
This endpoint will return up to 1,000 results for each search when using the following parameters:actor,branch,check_suite_id,created,event,head_sha,status.

### Fine-grained access tokens for "List workflow runs for a workflow"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Actions" repository permissions (read)
This endpoint can be used without authentication or the aforementioned permissions if only public resources are requested.

### Parameters for "List workflow runs for a workflow"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
workflow_idRequiredThe ID of the workflow. You can also pass the workflow file name as a string.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.

```
workflow_id
```
The ID of the workflow. You can also pass the workflow file name as a string.

[TABLE]
Name, Type, Description
actorstringReturns someone's workflow runs. Use the login for the user who created thepushassociated with the check suite or workflow run.
branchstringReturns workflow runs associated with a branch. Use the name of the branch of thepush.
eventstringReturns workflow run triggered by the event you specify. For example,push,pull_requestorissue. For more information, see "Events that trigger workflows."
statusstringReturns workflow runs with the check runstatusorconclusionthat you specify. For example, a conclusion can besuccessor a status can bein_progress. Only GitHub Actions can set a status ofwaiting,pending, orrequested.Can be one of:completed,action_required,cancelled,failure,neutral,skipped,stale,success,timed_out,in_progress,queued,requested,waiting,pending
per_pageintegerThe number of results per page_number (max 100). For more information, see "Using pagination in the REST API."Default:30
pageintegerThe page_number number of the results to fetch. For more information, see "Using pagination in the REST API."Default:1
createdstringReturns workflow runs created within the given date-time range. For more information on the syntax, see "Understanding the search syntax."
exclude_pull_requestsbooleanIftruepull requests are omitted from the response (empty array).Default:false
check_suite_idintegerReturns workflow runs with thecheck_suite_idthat you specify.
head_shastringOnly returns workflow runs that are associated with the specifiedhead_sha.
[/TABLE]
Returns someone's workflow runs. Use the login for the user who created thepushassociated with the check suite or workflow run.
Returns workflow runs associated with a branch. Use the name of the branch of thepush.
Returns workflow run triggered by the event you specify. For example,push,pull_requestorissue. For more information, see "Events that trigger workflows."
Returns workflow runs with the check runstatusorconclusionthat you specify. For example, a conclusion can besuccessor a status can bein_progress. Only GitHub Actions can set a status ofwaiting,pending, orrequested.
Can be one of:completed,action_required,cancelled,failure,neutral,skipped,stale,success,timed_out,in_progress,queued,requested,waiting,pending

```
action_required
```

```
in_progress
```
The number of results per page_number (max 100). For more information, see "Using pagination in the REST API."
Default:30
The page_number number of the results to fetch. For more information, see "Using pagination in the REST API."
Default:1
Returns workflow runs created within the given date-time range. For more information on the syntax, see "Understanding the search syntax."

```
exclude_pull_requests
```
Iftruepull requests are omitted from the response (empty array).
Default:false

```
check_suite_id
```
Returns workflow runs with thecheck_suite_idthat you specify.
Only returns workflow runs that are associated with the specifiedhead_sha.

### HTTP response status codes for "List workflow runs for a workflow"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "List workflow runs for a workflow"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/actions/workflows/WORKFLOW_ID/runs
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
  "workflow_runs": [
    {
      "id": 30433642,
      "name": "Build",
      "node_id": "MDEyOldvcmtmbG93IFJ1bjI2OTI4OQ==",
      "check_suite_id": 42,
      "check_suite_node_id": "MDEwOkNoZWNrU3VpdGU0Mg==",
      "head_branch": "master",
      "head_sha": "acb5820ced9479c074f688cc328bf03f341a511d",
      "path": ".github/workflows/build.yml@main",
      "run_number": 562,
      "event": "push",
      "display_title": "Update README.md",
      "status": "queued",
      "conclusion": null,
      "workflow_id": 159038,
      "url": "https://api.github.com/repos/octo-org/octo-repo/actions/runs/30433642",
      "html_url": "https://github.com/octo-org/octo-repo/actions/runs/30433642",
      "pull_requests": [],
      "created_at": "2020-01-22T19:33:08Z",
      "updated_at": "2020-01-22T19:33:08Z",
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
      "run_attempt": 1,
      "run_started_at": "2020-01-22T19:33:08Z",
      "triggering_actor": {
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
      "jobs_url": "https://api.github.com/repos/octo-org/octo-repo/actions/runs/30433642/jobs",
      "logs_url": "https://api.github.com/repos/octo-org/octo-repo/actions/runs/30433642/logs",
      "check_suite_url": "https://api.github.com/repos/octo-org/octo-repo/check-suites/414944374",
      "artifacts_url": "https://api.github.com/repos/octo-org/octo-repo/actions/runs/30433642/artifacts",
      "cancel_url": "https://api.github.com/repos/octo-org/octo-repo/actions/runs/30433642/cancel",
      "rerun_url": "https://api.github.com/repos/octo-org/octo-repo/actions/runs/30433642/rerun",
      "workflow_url": "https://api.github.com/repos/octo-org/octo-repo/actions/workflows/159038",
      "head_commit": {
        "id": "acb5820ced9479c074f688cc328bf03f341a511d",
        "tree_id": "d23f6eedb1e1b9610bbc754ddb5197bfe7271223",
        "message": "Create linter.yaml",
        "timestamp": "2020-01-22T19:33:05Z",
        "author": {
          "name": "Octo Cat",
          "email": "octocat@github.com"
        },
        "committer": {
          "name": "GitHub",
          "email": "noreply@github.com"
        }
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
      "head_repository": {
        "id": 217723378,
        "node_id": "MDEwOlJlcG9zaXRvcnkyMTc3MjMzNzg=",
        "name": "octo-repo",
        "full_name": "octo-org/octo-repo",
        "private": true,
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
        "html_url": "https://github.com/octo-org/octo-repo",
        "description": null,
        "fork": false,
        "url": "https://api.github.com/repos/octo-org/octo-repo",
        "forks_url": "https://api.github.com/repos/octo-org/octo-repo/forks",
        "keys_url": "https://api.github.com/repos/octo-org/octo-repo/keys{/key_id}",
        "collaborators_url": "https://api.github.com/repos/octo-org/octo-repo/collaborators{/collaborator}",
        "teams_url": "https://api.github.com/repos/octo-org/octo-repo/teams",
        "hooks_url": "https://api.github.com/repos/octo-org/octo-repo/hooks",
        "issue_events_url": "https://api.github.com/repos/octo-org/octo-repo/issues/events{/number}",
        "events_url": "https://api.github.com/repos/octo-org/octo-repo/events",
        "assignees_url": "https://api.github.com/repos/octo-org/octo-repo/assignees{/user}",
        "branches_url": "https://api.github.com/repos/octo-org/octo-repo/branches{/branch}",
        "tags_url": "https://api.github.com/repos/octo-org/octo-repo/tags",
        "blobs_url": "https://api.github.com/repos/octo-org/octo-repo/git/blobs{/commit_sha}",
        "git_tags_url": "https://api.github.com/repos/octo-org/octo-repo/git/tags{/commit_sha}",
        "git_refs_url": "https://api.github.com/repos/octo-org/octo-repo/git/refs{/commit_sha}",
        "trees_url": "https://api.github.com/repos/octo-org/octo-repo/git/trees{/commit_sha}",
        "statuses_url": "https://api.github.com/repos/octo-org/octo-repo/statuses/{commit_sha}",
        "languages_url": "https://api.github.com/repos/octo-org/octo-repo/languages",
        "stargazers_url": "https://api.github.com/repos/octo-org/octo-repo/stargazers",
        "contributors_url": "https://api.github.com/repos/octo-org/octo-repo/contributors",
        "subscribers_url": "https://api.github.com/repos/octo-org/octo-repo/subscribers",
        "subscription_url": "https://api.github.com/repos/octo-org/octo-repo/subscription",
        "commits_url": "https://api.github.com/repos/octo-org/octo-repo/commits{/commit_sha}",
        "git_commits_url": "https://api.github.com/repos/octo-org/octo-repo/git/commits{/commit_sha}",
        "comments_url": "https://api.github.com/repos/octo-org/octo-repo/comments{/number}",
        "issue_comment_url": "https://api.github.com/repos/octo-org/octo-repo/issues/comments{/number}",
        "contents_url": "https://api.github.com/repos/octo-org/octo-repo/contents/{+path}",
        "compare_url": "https://api.github.com/repos/octo-org/octo-repo/compare/{base}...{head}",
        "merges_url": "https://api.github.com/repos/octo-org/octo-repo/merges",
        "archive_url": "https://api.github.com/repos/octo-org/octo-repo/{archive_format}{/ref}",
        "downloads_url": "https://api.github.com/repos/octo-org/octo-repo/downloads",
        "issues_url": "https://api.github.com/repos/octo-org/octo-repo/issues{/number}",
        "pulls_url": "https://api.github.com/repos/octo-org/octo-repo/pulls{/number}",
        "milestones_url": "https://api.github.com/repos/octo-org/octo-repo/milestones{/number}",
        "notifications_url": "https://api.github.com/repos/octo-org/octo-repo/notifications{?since,all,participating}",
        "labels_url": "https://api.github.com/repos/octo-org/octo-repo/label_filters{/name}",
        "releases_url": "https://api.github.com/repos/octo-org/octo-repo/releases{/id}",
        "deployments_url": "https://api.github.com/repos/octo-org/octo-repo/deployments"
      }
    }
  ]
}
```