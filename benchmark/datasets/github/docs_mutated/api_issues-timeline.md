# REST API endpoints for timeline events

*Source: https://docs.github.com/en/rest/issues/timeline*

---

# REST API endpoints for timeline events
Use the REST API to receive events triggered by timeline activity in issues and pull requests.

## About timeline events
You can use the REST API to view different types of events triggered by timeline activity in issues and pull requests. For more information about the specific events that you can receive, seeIssue event types. To view GitHub activity outside of issues and pull requests, seeGitHub event types.
You can use timeline events to display information about issues and pull requests or determine who should be notified of issue comments.
Every pull request is an issue, but not every issue is a pull request. For this reason, "shared" actions for both features, like managing assignees, label_filters, and milestones, are provided within the Issues endpoints.

## List timeline events for an issue
List all timeline events for an issue.

### Fine-grained access tokens for "List timeline events for an issue"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have at least one of the following permission sets:
- "Issues" repository permissions (read)
- "Pull requests" repository permissions (read)
This endpoint can be used without authentication or the aforementioned permissions if only public resources are requested.

### Parameters for "List timeline events for an issue"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
issue_numberintegerRequiredThe number that identifies the issue.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.

```
issue_number
```
The number that identifies the issue.

[TABLE]
Name, Type, Description
per_pageintegerThe number of results per page_number (max 100). For more information, see "Using pagination in the REST API."Default:30
pageintegerThe page_number number of the results to fetch. For more information, see "Using pagination in the REST API."Default:1
[/TABLE]
The number of results per page_number (max 100). For more information, see "Using pagination in the REST API."
Default:30
The page_number number of the results to fetch. For more information, see "Using pagination in the REST API."
Default:1

### HTTP response status codes for "List timeline events for an issue"

[TABLE]
Status code | Description
200 | OK
404 | Resource not found
410 | Gone
[/TABLE]
OK
Resource not found
Gone

### Code samples for "List timeline events for an issue"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/issues/ISSUE_NUMBER/timeline
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
    "id": 6430295168,
    "node_id": "LOE_lADODwFebM5HwC0kzwAAAAF_RoSA",
    "url": "https://api.github.com/repos/github/roadmap/issues/events/6430295168",
    "actor": {
      "login": "github",
      "id": 9919,
      "node_id": "MDEyOk9yZ2FuaXphdGlvbjk5MTk=",
      "avatar_url": "https://avatars.githubusercontent.com/u/9919?v=4",
      "gravatar_id": "",
      "url": "https://api.github.com/users/github",
      "html_url": "https://github.com/github",
      "followers_url": "https://api.github.com/users/github/followers",
      "following_url": "https://api.github.com/users/github/following{/other_user}",
      "gists_url": "https://api.github.com/users/github/gists{/gist_id}",
      "starred_url": "https://api.github.com/users/github/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/github/subscriptions",
      "organizations_url": "https://api.github.com/users/github/orgs",
      "repos_url": "https://api.github.com/users/github/repos",
      "events_url": "https://api.github.com/users/github/events{/privacy}",
      "received_events_url": "https://api.github.com/users/github/received_events",
      "type": "Organization",
      "site_admin": false
    },
    "event": "locked",
    "commit_id": null,
    "commit_url": null,
    "created_at": "2022-04-13T20:49:13Z",
    "lock_reason": null,
    "performed_via_github_app": null
  },
  {
    "id": 6430296748,
    "node_id": "LE_lADODwFebM5HwC0kzwAAAAF_Roqs",
    "url": "https://api.github.com/repos/github/roadmap/issues/events/6430296748",
    "actor": {
      "login": "github-product-roadmap",
      "id": 67656570,
      "node_id": "MDQ6VXNlcjY3NjU2NTcw",
      "avatar_url": "https://avatars.githubusercontent.com/u/67656570?v=4",
      "gravatar_id": "",
      "url": "https://api.github.com/users/github-product-roadmap",
      "html_url": "https://github.com/github-product-roadmap",
      "followers_url": "https://api.github.com/users/github-product-roadmap/followers",
      "following_url": "https://api.github.com/users/github-product-roadmap/following{/other_user}",
      "gists_url": "https://api.github.com/users/github-product-roadmap/gists{/gist_id}",
      "starred_url": "https://api.github.com/users/github-product-roadmap/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/github-product-roadmap/subscriptions",
      "organizations_url": "https://api.github.com/users/github-product-roadmap/orgs",
      "repos_url": "https://api.github.com/users/github-product-roadmap/repos",
      "events_url": "https://api.github.com/users/github-product-roadmap/events{/privacy}",
      "received_events_url": "https://api.github.com/users/github-product-roadmap/received_events",
      "type": "User",
      "site_admin": false
    },
    "event": "labeled",
    "commit_id": null,
    "commit_url": null,
    "created_at": "2022-04-13T20:49:34Z",
    "label": {
      "name": "beta",
      "color": "99dd88"
    },
    "performed_via_github_app": null
  },
  {
    "id": 6635165802,
    "node_id": "RTE_lADODwFebM5HwC0kzwAAAAGLfJhq",
    "url": "https://api.github.com/repos/github/roadmap/issues/events/6635165802",
    "actor": {
      "login": "github-product-roadmap",
      "id": 67656570,
      "node_id": "MDQ6VXNlcjY3NjU2NTcw",
      "avatar_url": "https://avatars.githubusercontent.com/u/67656570?v=4",
      "gravatar_id": "",
      "url": "https://api.github.com/users/github-product-roadmap",
      "html_url": "https://github.com/github-product-roadmap",
      "followers_url": "https://api.github.com/users/github-product-roadmap/followers",
      "following_url": "https://api.github.com/users/github-product-roadmap/following{/other_user}",
      "gists_url": "https://api.github.com/users/github-product-roadmap/gists{/gist_id}",
      "starred_url": "https://api.github.com/users/github-product-roadmap/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/github-product-roadmap/subscriptions",
      "organizations_url": "https://api.github.com/users/github-product-roadmap/orgs",
      "repos_url": "https://api.github.com/users/github-product-roadmap/repos",
      "events_url": "https://api.github.com/users/github-product-roadmap/events{/privacy}",
      "received_events_url": "https://api.github.com/users/github-product-roadmap/received_events",
      "type": "User",
      "site_admin": false
    },
    "event": "renamed",
    "commit_id": null,
    "commit_url": null,
    "created_at": "2022-05-18T19:29:01Z",
    "rename": {
      "from": "Secret scanning: dry-runs for enterprise-level custom patterns (cloud)",
      "to": "Secret scanning: dry-runs for enterprise-level custom patterns"
    },
    "performed_via_github_app": null
  },
  {
    "url": "https://api.github.com/repos/github/roadmap/issues/comments/1130876857",
    "html_url": "https://github.com/github/roadmap/issues/493#issuecomment-1130876857",
    "issue_url": "https://api.github.com/repos/github/roadmap/issues/493",
    "id": 1130876857,
    "node_id": "IC_kwDODwFebM5DZ8-5",
    "user": {
      "login": "octocat",
      "id": 94867353,
      "node_id": "U_kgDOBaePmQ",
      "avatar_url": "https://avatars.githubusercontent.com/u/94867353?v=4",
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
    "created_at": "2022-05-19T00:52:15Z",
    "updated_at": "2022-05-19T00:52:15Z",
    "author_association": "COLLABORATOR",
    "body": "🚢  Shipped to the cloud: https://github.blog/changelog/2022-05-12-secret-scanning-dry-runs-for-enterprise-level-custom-patterns/",
    "reactions": {
      "url": "https://api.github.com/repos/github/roadmap/issues/comments/1130876857/reactions",
      "total_count": 0,
      "+1": 0,
      "-1": 0,
      "laugh": 0,
      "hooray": 0,
      "confused": 0,
      "heart": 0,
      "rocket": 0,
      "eyes": 0
    },
    "performed_via_github_app": null,
    "event": "commented",
    "actor": {
      "login": "octocat",
      "id": 94867353,
      "node_id": "U_kgDOBaePmQ",
      "avatar_url": "https://avatars.githubusercontent.com/u/94867353?v=4",
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
    }
  }
]
```