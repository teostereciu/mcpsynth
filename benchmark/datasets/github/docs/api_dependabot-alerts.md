# REST API endpoints for Dependabot alerts

*Source: https://docs.github.com/en/rest/dependabot/alerts*

---

# REST API endpoints for Dependabot alerts
Use the REST API to interact with Dependabot alerts for a repository.
Note
The ability to use the REST API to manage Dependabot alerts is currently in public preview and subject to change.

## About Dependabot alerts
You can view Dependabot alerts for a repository and update individual alerts with the REST API. For more information, seeAbout Dependabot alerts.

## List Dependabot alerts for an enterprise
Lists Dependabot alerts for repositories that are owned by the specified enterprise.
The authenticated user must be a member of the enterprise to use this endpoint.
Alerts are only returned for organizations in the enterprise for which you are an organization owner or a security manager. For more information about security managers, see "Managing security managers in your organization."
OAuth app tokens and personal access tokens (classic) need therepoorsecurity_eventsscope to use this endpoint.

### Fine-grained access tokens for "List Dependabot alerts for an enterprise"
This endpoint does not work with GitHub App user access tokens, GitHub App installation access tokens, or fine-grained personal access tokens.

### Parameters for "List Dependabot alerts for an enterprise"

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
statestringA comma-separated list of states. If specified, only alerts with these states will be returned.Can be:auto_dismissed,dismissed,fixed,open
severitystringA comma-separated list of severities. If specified, only alerts with these severities will be returned.Can be:low,medium,high,critical
ecosystemstringA comma-separated list of ecosystems. If specified, only alerts for these ecosystems will be returned.Can be:composer,go,maven,npm,nuget,pip,pub,rubygems,rust
packagestringA comma-separated list of package names. If specified, only alerts for these packages will be returned.
epss_percentagestringCVE Exploit Prediction Scoring System (EPSS) percentage. Can be specified as:An exact number (n)Comparators such as>n,<n,>=n,<=nA range liken..n, wherenis a number from 0.0 to 1.0Filters the list of alerts based on EPSS percentages. If specified, only alerts with the provided EPSS percentages will be returned.
hasFilters the list of alerts based on whether the alert has the given value. If specified, only alerts meeting this criterion will be returned.
Multiplehasfilters can be passed to filter for alerts that have all of the values. Currently, onlypatchis supported.
assigneestringFilter alerts by assignees.
Provide a comma-separated list of user handles (e.g.,octocatoroctocat,hubot) to return alerts assigned to any of the specified users.
Use*to list alerts with at least one assignee ornoneto list alerts with no assignees.
scopestringThe scope of the vulnerable dependency. If specified, only alerts with this scope will be returned.Can be one of:development,runtime
sortstringThe property by which to sort the results.createdmeans when the alert was created.updatedmeans when the alert's state last changed.epss_percentagesorts alerts by the Exploit Prediction Scoring System (EPSS) percentage.Default:createdCan be one of:created,updated,epss_percentage
directionstringThe direction to sort the results by.Default:descCan be one of:asc,desc
beforestringA cursor, as given in theLink header. If specified, the query only searches for results before this cursor. For more information, see "Using pagination in the REST API."
afterstringA cursor, as given in theLink header. If specified, the query only searches for results after this cursor. For more information, see "Using pagination in the REST API."
per_pageintegerThe number of results per page (max 100). For more information, see "Using pagination in the REST API."Default:30
[/TABLE]
A comma-separated list of states. If specified, only alerts with these states will be returned.
Can be:auto_dismissed,dismissed,fixed,open
A comma-separated list of severities. If specified, only alerts with these severities will be returned.
Can be:low,medium,high,critical
A comma-separated list of ecosystems. If specified, only alerts for these ecosystems will be returned.
Can be:composer,go,maven,npm,nuget,pip,pub,rubygems,rust
A comma-separated list of package names. If specified, only alerts for these packages will be returned.

```
epss_percentage
```
CVE Exploit Prediction Scoring System (EPSS) percentage. Can be specified as:
- An exact number (n)
- Comparators such as>n,<n,>=n,<=n
- A range liken..n, wherenis a number from 0.0 to 1.0
Filters the list of alerts based on EPSS percentages. If specified, only alerts with the provided EPSS percentages will be returned.
Filters the list of alerts based on whether the alert has the given value. If specified, only alerts meeting this criterion will be returned.
Multiplehasfilters can be passed to filter for alerts that have all of the values. Currently, onlypatchis supported.
Filter alerts by assignees.
Provide a comma-separated list of user handles (e.g.,octocatoroctocat,hubot) to return alerts assigned to any of the specified users.
Use*to list alerts with at least one assignee ornoneto list alerts with no assignees.
The scope of the vulnerable dependency. If specified, only alerts with this scope will be returned.
Can be one of:development,runtime

```
development
```
The property by which to sort the results.createdmeans when the alert was created.updatedmeans when the alert's state last changed.epss_percentagesorts alerts by the Exploit Prediction Scoring System (EPSS) percentage.
Default:created
Can be one of:created,updated,epss_percentage

```
epss_percentage
```
The direction to sort the results by.
Default:desc
Can be one of:asc,desc
A cursor, as given in theLink header. If specified, the query only searches for results before this cursor. For more information, see "Using pagination in the REST API."
A cursor, as given in theLink header. If specified, the query only searches for results after this cursor. For more information, see "Using pagination in the REST API."
The number of results per page (max 100). For more information, see "Using pagination in the REST API."
Default:30

### HTTP response status codes for "List Dependabot alerts for an enterprise"

[TABLE]
Status code | Description
200 | OK
304 | Not modified
403 | Forbidden
404 | Resource not found
422 | Validation failed, or the endpoint has been spammed.
[/TABLE]
OK
Not modified
Forbidden
Resource not found
Validation failed, or the endpoint has been spammed.

### Code samples for "List Dependabot alerts for an enterprise"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/enterprises/ENTERPRISE/dependabot/alerts
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
    "state": "dismissed",
    "dependency": {
      "package": {
        "ecosystem": "pip",
        "name": "django"
      },
      "manifest_path": "path/to/requirements.txt",
      "scope": "runtime"
    },
    "security_advisory": {
      "ghsa_id": "GHSA-rf4j-j272-fj86",
      "cve_id": "CVE-2018-6188",
      "summary": "Django allows remote attackers to obtain potentially sensitive information by leveraging data exposure from the confirm_login_allowed() method, as demonstrated by discovering whether a user account is inactive",
      "description": "django.contrib.auth.forms.AuthenticationForm in Django 2.0 before 2.0.2, and 1.11.8 and 1.11.9, allows remote attackers to obtain potentially sensitive information by leveraging data exposure from the confirm_login_allowed() method, as demonstrated by discovering whether a user account is inactive.",
      "vulnerabilities": [
        {
          "package": {
            "ecosystem": "pip",
            "name": "django"
          },
          "severity": "high",
          "vulnerable_version_range": ">= 2.0.0, < 2.0.2",
          "first_patched_version": {
            "identifier": "2.0.2"
          }
        },
        {
          "package": {
            "ecosystem": "pip",
            "name": "django"
          },
          "severity": "high",
          "vulnerable_version_range": ">= 1.11.8, < 1.11.10",
          "first_patched_version": {
            "identifier": "1.11.10"
          }
        }
      ],
      "severity": "high",
      "cvss": {
        "vector_string": "CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N",
        "score": 7.5
      },
      "cvss_severities": {
        "cvss_v3": {
          "vector_string": "CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N",
          "score": 7.5
        },
        "cvss_v4": {
          "vector_string": "CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:H/VI:N/VA:N/SC:N/SI:N/SA:N",
          "score": 8.7
        }
      },
      "epss": [
        {
          "percentage": 0.00045,
          "percentile": "0.16001e0"
        }
      ],
      "cwes": [
        {
          "cwe_id": "CWE-200",
          "name": "Exposure of Sensitive Information to an Unauthorized Actor"
        }
      ],
      "identifiers": [
        {
          "type": "GHSA",
          "value": "GHSA-rf4j-j272-fj86"
        },
        {
          "type": "CVE",
          "value": "CVE-2018-6188"
        }
      ],
      "references": [
        {
          "url": "https://nvd.nist.gov/vuln/detail/CVE-2018-6188"
        },
        {
          "url": "https://github.com/advisories/GHSA-rf4j-j272-fj86"
        },
        {
          "url": "https://usn.ubuntu.com/3559-1/"
        },
        {
          "url": "https://www.djangoproject.com/weblog/2018/feb/01/security-releases/"
        },
        {
          "url": "http://www.securitytracker.com/id/1040422"
        }
      ],
      "published_at": "2018-10-03T21:13:54Z",
      "updated_at": "2022-04-26T18:35:37Z",
      "withdrawn_at": null
    },
    "security_vulnerability": {
      "package": {
        "ecosystem": "pip",
        "name": "django"
      },
      "severity": "high",
      "vulnerable_version_range": ">= 2.0.0, < 2.0.2",
      "first_patched_version": {
        "identifier": "2.0.2"
      }
    },
    "url": "https://api.github.com/repos/octo-org/octo-repo/dependabot/alerts/2",
    "html_url": "https://github.com/octo-org/octo-repo/security/dependabot/2",
    "created_at": "2022-06-15T07:43:03Z",
    "updated_at": "2022-08-23T14:29:47Z",
    "dismissed_at": "2022-08-23T14:29:47Z",
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
    "dismissed_reason": "tolerable_risk",
    "dismissed_comment": "This alert is accurate but we use a sanitizer.",
    "fixed_at": null,
    "assignees": [
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
    ],
    "repository": {
      "id": 217723378,
      "node_id": "MDEwOlJlcG9zaXRvcnkyMTc3MjMzNzg=",
      "name": "octo-repo",
      "full_name": "octo-org/octo-repo",
      "owner": {
        "login": "octo-org",
        "id": 6811672,
        "node_id": "MDEyOk9yZ2FuaXphdGlvbjY4MTE2NzI=",
        "avatar_url": "https://avatars3.githubusercontent.com/u/6811672?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/octo-org",
        "html_url": "https://github.com/octo-org",
        "followers_url": "https://api.github.com/users/octo-org/followers",
        "following_url": "https://api.github.com/users/octo-org/following{/other_user}",
        "gists_url": "https://api.github.com/users/octo-org/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/octo-org/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/octo-org/subscriptions",
        "organizations_url": "https://api.github.com/users/octo-org/orgs",
        "repos_url": "https://api.github.com/users/octo-org/repos",
        "events_url": "https://api.github.com/users/octo-org/events{/privacy}",
        "received_events_url": "https://api.github.com/users/octo-org/received_events",
        "type": "Organization",
        "site_admin": false
      },
      "private": true,
      "html_url": "https://github.com/octo-org/octo-repo",
      "description": null,
      "fork": false,
      "url": "https://api.github.com/repos/octo-org/octo-repo",
      "archive_url": "https://api.github.com/repos/octo-org/octo-repo/{archive_format}{/ref}",
      "assignees_url": "https://api.github.com/repos/octo-org/octo-repo/assignees{/user}",
      "blobs_url": "https://api.github.com/repos/octo-org/octo-repo/git/blobs{/sha}",
      "branches_url": "https://api.github.com/repos/octo-org/octo-repo/branches{/branch}",
      "collaborators_url": "https://api.github.com/repos/octo-org/octo-repo/collaborators{/collaborator}",
      "comments_url": "https://api.github.com/repos/octo-org/octo-repo/comments{/number}",
      "commits_url": "https://api.github.com/repos/octo-org/octo-repo/commits{/sha}",
      "compare_url": "https://api.github.com/repos/octo-org/octo-repo/compare/{base}...{head}",
      "contents_url": "https://api.github.com/repos/octo-org/octo-repo/contents/{+path}",
      "contributors_url": "https://api.github.com/repos/octo-org/octo-repo/contributors",
      "deployments_url": "https://api.github.com/repos/octo-org/octo-repo/deployments",
      "downloads_url": "https://api.github.com/repos/octo-org/octo-repo/downloads",
      "events_url": "https://api.github.com/repos/octo-org/octo-repo/events",
      "forks_url": "https://api.github.com/repos/octo-org/octo-repo/forks",
      "git_commits_url": "https://api.github.com/repos/octo-org/octo-repo/git/commits{/sha}",
      "git_refs_url": "https://api.github.com/repos/octo-org/octo-repo/git/refs{/sha}",
      "git_tags_url": "https://api.github.com/repos/octo-org/octo-repo/git/tags{/sha}",
      "hooks_url": "https://api.github.com/repos/octo-org/octo-repo/hooks",
      "issue_comment_url": "https://api.github.com/repos/octo-org/octo-repo/issues/comments{/number}",
      "issue_events_url": "https://api.github.com/repos/octo-org/octo-repo/issues/events{/number}",
      "issues_url": "https://api.github.com/repos/octo-org/octo-repo/issues{/number}",
      "keys_url": "https://api.github.com/repos/octo-org/octo-repo/keys{/key_id}",
      "labels_url": "https://api.github.com/repos/octo-org/octo-repo/labels{/name}",
      "languages_url": "https://api.github.com/repos/octo-org/octo-repo/languages",
      "merges_url": "https://api.github.com/repos/octo-org/octo-repo/merges",
      "milestones_url": "https://api.github.com/repos/octo-org/octo-repo/milestones{/number}",
      "notifications_url": "https://api.github.com/repos/octo-org/octo-repo/notifications{?since,all,participating}",
      "pulls_url": "https://api.github.com/repos/octo-org/octo-repo/pulls{/number}",
      "releases_url": "https://api.github.com/repos/octo-org/octo-repo/releases{/id}",
      "stargazers_url": "https://api.github.com/repos/octo-org/octo-repo/stargazers",
      "statuses_url": "https://api.github.com/repos/octo-org/octo-repo/statuses/{sha}",
      "subscribers_url": "https://api.github.com/repos/octo-org/octo-repo/subscribers",
      "subscription_url": "https://api.github.com/repos/octo-org/octo-repo/subscription",
      "tags_url": "https://api.github.com/repos/octo-org/octo-repo/tags",
      "teams_url": "https://api.github.com/repos/octo-org/octo-repo/teams",
      "trees_url": "https://api.github.com/repos/octo-org/octo-repo/git/trees{/sha}"
    }
  },
  {
    "number": 1,
    "state": "open",
    "dependency": {
      "package": {
        "ecosystem": "pip",
        "name": "ansible"
      },
      "manifest_path": "path/to/requirements.txt",
      "scope": "runtime"
    },
    "security_advisory": {
      "ghsa_id": "GHSA-8f4m-hccc-8qph",
      "cve_id": "CVE-2021-20191",
      "summary": "Insertion of Sensitive Information into Log File in ansible",
      "description": "A flaw was found in ansible. Credentials, such as secrets, are being disclosed in console log by default and not protected by no_log feature when using those modules. An attacker can take advantage of this information to steal those credentials. The highest threat from this vulnerability is to data confidentiality.",
      "vulnerabilities": [
        {
          "package": {
            "ecosystem": "pip",
            "name": "ansible"
          },
          "severity": "medium",
          "vulnerable_version_range": ">= 2.9.0, < 2.9.18",
          "first_patched_version": {
            "identifier": "2.9.18"
          }
        },
        {
          "package": {
            "ecosystem": "pip",
            "name": "ansible"
          },
          "severity": "medium",
          "vulnerable_version_range": "< 2.8.19",
          "first_patched_version": {
            "identifier": "2.8.19"
          }
        },
        {
          "package": {
            "ecosystem": "pip",
            "name": "ansible"
          },
          "severity": "medium",
          "vulnerable_version_range": ">= 2.10.0, < 2.10.7",
          "first_patched_version": {
            "identifier": "2.10.7"
          }
        }
      ],
      "severity": "medium",
      "cvss": {
        "vector_string": "CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N",
        "score": 5.5
      },
      "cvss_severities": {
        "cvss_v3": {
          "vector_string": "CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N",
          "score": 5.5
        },
        "cvss_v4": {
          "vector_string": "CVSS:4.0/AV:L/AC:L/AT:N/PR:N/UI:P/VC:H/VI:H/VA:H/SC:N/SI:N/SA:N",
          "score": 8.5
        }
      },
      "cwes": [
        {
          "cwe_id": "CWE-532",
          "name": "Insertion of Sensitive Information into Log File"
        }
      ],
      "identifiers": [
        {
          "type": "GHSA",
          "value": "GHSA-8f4m-hccc-8qph"
        },
        {
          "type": "CVE",
          "value": "CVE-2021-20191"
        }
      ],
      "references": [
        {
          "url": "https://nvd.nist.gov/vuln/detail/CVE-2021-20191"
        },
        {
          "url": "https://access.redhat.com/security/cve/cve-2021-20191"
        },
        {
          "url": "https://bugzilla.redhat.com/show_bug.cgi?id=1916813"
        }
      ],
      "published_at": "2021-06-01T17:38:00Z",
      "updated_at": "2021-08-12T23:06:00Z",
      "withdrawn_at": null
    },
    "security_vulnerability": {
      "package": {
        "ecosystem": "pip",
        "name": "ansible"
      },
      "severity": "medium",
      "vulnerable_version_range": "< 2.8.19",
      "first_patched_version": {
        "identifier": "2.8.19"
      }
    },
    "url": "https://api.github.com/repos/octo-org/hello-world/dependabot/alerts/1",
    "html_url": "https://github.com/octo-org/hello-world/security/dependabot/1",
    "created_at": "2022-06-14T15:21:52Z",
    "updated_at": "2022-06-14T15:21:52Z",
    "dismissed_at": null,
    "dismissed_by": null,
    "dismissed_reason": null,
    "dismissed_comment": null,
    "fixed_at": null,
    "assignees": [],
    "repository": {
      "id": 664700648,
      "node_id": "MDEwOlJlcG9zaXRvcnk2NjQ3MDA2NDg=",
      "name": "hello-world",
      "full_name": "octo-org/hello-world",
      "owner": {
        "login": "octo-org",
        "id": 6811672,
        "node_id": "MDEyOk9yZ2FuaXphdGlvbjY4MTE2NzI=",
        "avatar_url": "https://avatars3.githubusercontent.com/u/6811672?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/octo-org",
        "html_url": "https://github.com/octo-org",
        "followers_url": "https://api.github.com/users/octo-org/followers",
        "following_url": "https://api.github.com/users/octo-org/following{/other_user}",
        "gists_url": "https://api.github.com/users/octo-org/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/octo-org/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/octo-org/subscriptions",
        "organizations_url": "https://api.github.com/users/octo-org/orgs",
        "repos_url": "https://api.github.com/users/octo-org/repos",
        "events_url": "https://api.github.com/users/octo-org/events{/privacy}",
        "received_events_url": "https://api.github.com/users/octo-org/received_events",
        "type": "Organization",
        "site_admin": false
      },
      "private": true,
      "html_url": "https://github.com/octo-org/hello-world",
      "description": null,
      "fork": false,
      "url": "https://api.github.com/repos/octo-org/hello-world",
      "archive_url": "https://api.github.com/repos/octo-org/hello-world/{archive_format}{/ref}",
      "assignees_url": "https://api.github.com/repos/octo-org/hello-world/assignees{/user}",
      "blobs_url": "https://api.github.com/repos/octo-org/hello-world/git/blobs{/sha}",
      "branches_url": "https://api.github.com/repos/octo-org/hello-world/branches{/branch}",
      "collaborators_url": "https://api.github.com/repos/octo-org/hello-world/collaborators{/collaborator}",
      "comments_url": "https://api.github.com/repos/octo-org/hello-world/comments{/number}",
      "commits_url": "https://api.github.com/repos/octo-org/hello-world/commits{/sha}",
      "compare_url": "https://api.github.com/repos/octo-org/hello-world/compare/{base}...{head}",
      "contents_url": "https://api.github.com/repos/octo-org/hello-world/contents/{+path}",
      "contributors_url": "https://api.github.com/repos/octo-org/hello-world/contributors",
      "deployments_url": "https://api.github.com/repos/octo-org/hello-world/deployments",
      "downloads_url": "https://api.github.com/repos/octo-org/hello-world/downloads",
      "events_url": "https://api.github.com/repos/octo-org/hello-world/events",
      "forks_url": "https://api.github.com/repos/octo-org/hello-world/forks",
      "git_commits_url": "https://api.github.com/repos/octo-org/hello-world/git/commits{/sha}",
      "git_refs_url": "https://api.github.com/repos/octo-org/hello-world/git/refs{/sha}",
      "git_tags_url": "https://api.github.com/repos/octo-org/hello-world/git/tags{/sha}",
      "hooks_url": "https://api.github.com/repos/octo-org/hello-world/hooks",
      "issue_comment_url": "https://api.github.com/repos/octo-org/hello-world/issues/comments{/number}",
      "issue_events_url": "https://api.github.com/repos/octo-org/hello-world/issues/events{/number}",
      "issues_url": "https://api.github.com/repos/octo-org/hello-world/issues{/number}",
      "keys_url": "https://api.github.com/repos/octo-org/hello-world/keys{/key_id}",
      "labels_url": "https://api.github.com/repos/octo-org/hello-world/labels{/name}",
      "languages_url": "https://api.github.com/repos/octo-org/hello-world/languages",
      "merges_url": "https://api.github.com/repos/octo-org/hello-world/merges",
      "milestones_url": "https://api.github.com/repos/octo-org/hello-world/milestones{/number}",
      "notifications_url": "https://api.github.com/repos/octo-org/hello-world/notifications{?since,all,participating}",
      "pulls_url": "https://api.github.com/repos/octo-org/hello-world/pulls{/number}",
      "releases_url": "https://api.github.com/repos/octo-org/hello-world/releases{/id}",
      "stargazers_url": "https://api.github.com/repos/octo-org/hello-world/stargazers",
      "statuses_url": "https://api.github.com/repos/octo-org/hello-world/statuses/{sha}",
      "subscribers_url": "https://api.github.com/repos/octo-org/hello-world/subscribers",
      "subscription_url": "https://api.github.com/repos/octo-org/hello-world/subscription",
      "tags_url": "https://api.github.com/repos/octo-org/hello-world/tags",
      "teams_url": "https://api.github.com/repos/octo-org/hello-world/teams",
      "trees_url": "https://api.github.com/repos/octo-org/hello-world/git/trees{/sha}"
    }
  }
]
```

## List Dependabot alerts for an organization
Lists Dependabot alerts for an organization.
The authenticated user must be an owner or security manager for the organization to use this endpoint.
OAuth app tokens and personal access tokens (classic) need thesecurity_eventsscope to use this endpoint. If this endpoint is only used with public repositories, the token can use thepublic_reposcope instead.

### Fine-grained access tokens for "List Dependabot alerts for an organization"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Dependabot alerts" repository permissions (read)

### Parameters for "List Dependabot alerts for an organization"

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
statestringA comma-separated list of states. If specified, only alerts with these states will be returned.Can be:auto_dismissed,dismissed,fixed,open
severitystringA comma-separated list of severities. If specified, only alerts with these severities will be returned.Can be:low,medium,high,critical
ecosystemstringA comma-separated list of ecosystems. If specified, only alerts for these ecosystems will be returned.Can be:composer,go,maven,npm,nuget,pip,pub,rubygems,rust
packagestringA comma-separated list of package names. If specified, only alerts for these packages will be returned.
epss_percentagestringCVE Exploit Prediction Scoring System (EPSS) percentage. Can be specified as:An exact number (n)Comparators such as>n,<n,>=n,<=nA range liken..n, wherenis a number from 0.0 to 1.0Filters the list of alerts based on EPSS percentages. If specified, only alerts with the provided EPSS percentages will be returned.
artifact_registry_urlstringA comma-separated list of artifact registry URLs. If specified, only alerts for repositories with storage records matching these URLs will be returned.
artifact_registrystringA comma-separated list of Artifact Registry name strings. If specified, only alerts for repositories with storage records matching these registries will be returned.Can be:jfrog-artifactory
hasFilters the list of alerts based on whether the alert has the given value. If specified, only alerts meeting this criterion will be returned.
Multiplehasfilters can be passed to filter for alerts that have all of the values.
assigneestringFilter alerts by assignees.
Provide a comma-separated list of user handles (e.g.,octocatoroctocat,hubot) to return alerts assigned to any of the specified users.
Use*to list alerts with at least one assignee ornoneto list alerts with no assignees.
runtime_riskstringA comma-separated list of runtime risk strings. If specified, only alerts for repositories with deployment records matching these risks will be returned.Can be:critical-resource,internet-exposed,sensitive-data,lateral-movement
scopestringThe scope of the vulnerable dependency. If specified, only alerts with this scope will be returned.Can be one of:development,runtime
sortstringThe property by which to sort the results.createdmeans when the alert was created.updatedmeans when the alert's state last changed.epss_percentagesorts alerts by the Exploit Prediction Scoring System (EPSS) percentage.Default:createdCan be one of:created,updated,epss_percentage
directionstringThe direction to sort the results by.Default:descCan be one of:asc,desc
beforestringA cursor, as given in theLink header. If specified, the query only searches for results before this cursor. For more information, see "Using pagination in the REST API."
afterstringA cursor, as given in theLink header. If specified, the query only searches for results after this cursor. For more information, see "Using pagination in the REST API."
per_pageintegerThe number of results per page (max 100). For more information, see "Using pagination in the REST API."Default:30
[/TABLE]
A comma-separated list of states. If specified, only alerts with these states will be returned.
Can be:auto_dismissed,dismissed,fixed,open
A comma-separated list of severities. If specified, only alerts with these severities will be returned.
Can be:low,medium,high,critical
A comma-separated list of ecosystems. If specified, only alerts for these ecosystems will be returned.
Can be:composer,go,maven,npm,nuget,pip,pub,rubygems,rust
A comma-separated list of package names. If specified, only alerts for these packages will be returned.

```
epss_percentage
```
CVE Exploit Prediction Scoring System (EPSS) percentage. Can be specified as:
- An exact number (n)
- Comparators such as>n,<n,>=n,<=n
- A range liken..n, wherenis a number from 0.0 to 1.0
Filters the list of alerts based on EPSS percentages. If specified, only alerts with the provided EPSS percentages will be returned.

```
artifact_registry_url
```
A comma-separated list of artifact registry URLs. If specified, only alerts for repositories with storage records matching these URLs will be returned.

```
artifact_registry
```
A comma-separated list of Artifact Registry name strings. If specified, only alerts for repositories with storage records matching these registries will be returned.
Can be:jfrog-artifactory
Filters the list of alerts based on whether the alert has the given value. If specified, only alerts meeting this criterion will be returned.
Multiplehasfilters can be passed to filter for alerts that have all of the values.
Filter alerts by assignees.
Provide a comma-separated list of user handles (e.g.,octocatoroctocat,hubot) to return alerts assigned to any of the specified users.
Use*to list alerts with at least one assignee ornoneto list alerts with no assignees.

```
runtime_risk
```
A comma-separated list of runtime risk strings. If specified, only alerts for repositories with deployment records matching these risks will be returned.
Can be:critical-resource,internet-exposed,sensitive-data,lateral-movement
The scope of the vulnerable dependency. If specified, only alerts with this scope will be returned.
Can be one of:development,runtime

```
development
```
The property by which to sort the results.createdmeans when the alert was created.updatedmeans when the alert's state last changed.epss_percentagesorts alerts by the Exploit Prediction Scoring System (EPSS) percentage.
Default:created
Can be one of:created,updated,epss_percentage

```
epss_percentage
```
The direction to sort the results by.
Default:desc
Can be one of:asc,desc
A cursor, as given in theLink header. If specified, the query only searches for results before this cursor. For more information, see "Using pagination in the REST API."
A cursor, as given in theLink header. If specified, the query only searches for results after this cursor. For more information, see "Using pagination in the REST API."
The number of results per page (max 100). For more information, see "Using pagination in the REST API."
Default:30

### HTTP response status codes for "List Dependabot alerts for an organization"

[TABLE]
Status code | Description
200 | OK
304 | Not modified
400 | Bad Request
403 | Forbidden
404 | Resource not found
422 | Validation failed, or the endpoint has been spammed.
[/TABLE]
OK
Not modified
Bad Request
Forbidden
Resource not found
Validation failed, or the endpoint has been spammed.

### Code samples for "List Dependabot alerts for an organization"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/orgs/ORG/dependabot/alerts
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
    "state": "dismissed",
    "dependency": {
      "package": {
        "ecosystem": "pip",
        "name": "django"
      },
      "manifest_path": "path/to/requirements.txt",
      "scope": "runtime"
    },
    "security_advisory": {
      "ghsa_id": "GHSA-rf4j-j272-fj86",
      "cve_id": "CVE-2018-6188",
      "summary": "Django allows remote attackers to obtain potentially sensitive information by leveraging data exposure from the confirm_login_allowed() method, as demonstrated by discovering whether a user account is inactive",
      "description": "django.contrib.auth.forms.AuthenticationForm in Django 2.0 before 2.0.2, and 1.11.8 and 1.11.9, allows remote attackers to obtain potentially sensitive information by leveraging data exposure from the confirm_login_allowed() method, as demonstrated by discovering whether a user account is inactive.",
      "vulnerabilities": [
        {
          "package": {
            "ecosystem": "pip",
            "name": "django"
          },
          "severity": "high",
          "vulnerable_version_range": ">= 2.0.0, < 2.0.2",
          "first_patched_version": {
            "identifier": "2.0.2"
          }
        },
        {
          "package": {
            "ecosystem": "pip",
            "name": "django"
          },
          "severity": "high",
          "vulnerable_version_range": ">= 1.11.8, < 1.11.10",
          "first_patched_version": {
            "identifier": "1.11.10"
          }
        }
      ],
      "severity": "high",
      "cvss": {
        "vector_string": "CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N",
        "score": 7.5
      },
      "cvss_severities": {
        "cvss_v3": {
          "vector_string": "CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N",
          "score": 7.5
        },
        "cvss_v4": {
          "vector_string": "CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:H/VI:N/VA:N/SC:N/SI:N/SA:N",
          "score": 8.7
        }
      },
      "epss": [
        {
          "percentage": 0.00045,
          "percentile": "0.16001e0"
        }
      ],
      "cwes": [
        {
          "cwe_id": "CWE-200",
          "name": "Exposure of Sensitive Information to an Unauthorized Actor"
        }
      ],
      "identifiers": [
        {
          "type": "GHSA",
          "value": "GHSA-rf4j-j272-fj86"
        },
        {
          "type": "CVE",
          "value": "CVE-2018-6188"
        }
      ],
      "references": [
        {
          "url": "https://nvd.nist.gov/vuln/detail/CVE-2018-6188"
        },
        {
          "url": "https://github.com/advisories/GHSA-rf4j-j272-fj86"
        },
        {
          "url": "https://usn.ubuntu.com/3559-1/"
        },
        {
          "url": "https://www.djangoproject.com/weblog/2018/feb/01/security-releases/"
        },
        {
          "url": "http://www.securitytracker.com/id/1040422"
        }
      ],
      "published_at": "2018-10-03T21:13:54Z",
      "updated_at": "2022-04-26T18:35:37Z",
      "withdrawn_at": null
    },
    "security_vulnerability": {
      "package": {
        "ecosystem": "pip",
        "name": "django"
      },
      "severity": "high",
      "vulnerable_version_range": ">= 2.0.0, < 2.0.2",
      "first_patched_version": {
        "identifier": "2.0.2"
      }
    },
    "url": "https://api.github.com/repos/octo-org/octo-repo/dependabot/alerts/2",
    "html_url": "https://github.com/octo-org/octo-repo/security/dependabot/2",
    "created_at": "2022-06-15T07:43:03Z",
    "updated_at": "2022-08-23T14:29:47Z",
    "dismissed_at": "2022-08-23T14:29:47Z",
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
    "dismissed_reason": "tolerable_risk",
    "dismissed_comment": "This alert is accurate but we use a sanitizer.",
    "fixed_at": null,
    "assignees": [
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
    ],
    "repository": {
      "id": 217723378,
      "node_id": "MDEwOlJlcG9zaXRvcnkyMTc3MjMzNzg=",
      "name": "octo-repo",
      "full_name": "octo-org/octo-repo",
      "owner": {
        "login": "octo-org",
        "id": 6811672,
        "node_id": "MDEyOk9yZ2FuaXphdGlvbjY4MTE2NzI=",
        "avatar_url": "https://avatars3.githubusercontent.com/u/6811672?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/octo-org",
        "html_url": "https://github.com/octo-org",
        "followers_url": "https://api.github.com/users/octo-org/followers",
        "following_url": "https://api.github.com/users/octo-org/following{/other_user}",
        "gists_url": "https://api.github.com/users/octo-org/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/octo-org/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/octo-org/subscriptions",
        "organizations_url": "https://api.github.com/users/octo-org/orgs",
        "repos_url": "https://api.github.com/users/octo-org/repos",
        "events_url": "https://api.github.com/users/octo-org/events{/privacy}",
        "received_events_url": "https://api.github.com/users/octo-org/received_events",
        "type": "Organization",
        "site_admin": false
      },
      "private": true,
      "html_url": "https://github.com/octo-org/octo-repo",
      "description": null,
      "fork": false,
      "url": "https://api.github.com/repos/octo-org/octo-repo",
      "archive_url": "https://api.github.com/repos/octo-org/octo-repo/{archive_format}{/ref}",
      "assignees_url": "https://api.github.com/repos/octo-org/octo-repo/assignees{/user}",
      "blobs_url": "https://api.github.com/repos/octo-org/octo-repo/git/blobs{/sha}",
      "branches_url": "https://api.github.com/repos/octo-org/octo-repo/branches{/branch}",
      "collaborators_url": "https://api.github.com/repos/octo-org/octo-repo/collaborators{/collaborator}",
      "comments_url": "https://api.github.com/repos/octo-org/octo-repo/comments{/number}",
      "commits_url": "https://api.github.com/repos/octo-org/octo-repo/commits{/sha}",
      "compare_url": "https://api.github.com/repos/octo-org/octo-repo/compare/{base}...{head}",
      "contents_url": "https://api.github.com/repos/octo-org/octo-repo/contents/{+path}",
      "contributors_url": "https://api.github.com/repos/octo-org/octo-repo/contributors",
      "deployments_url": "https://api.github.com/repos/octo-org/octo-repo/deployments",
      "downloads_url": "https://api.github.com/repos/octo-org/octo-repo/downloads",
      "events_url": "https://api.github.com/repos/octo-org/octo-repo/events",
      "forks_url": "https://api.github.com/repos/octo-org/octo-repo/forks",
      "git_commits_url": "https://api.github.com/repos/octo-org/octo-repo/git/commits{/sha}",
      "git_refs_url": "https://api.github.com/repos/octo-org/octo-repo/git/refs{/sha}",
      "git_tags_url": "https://api.github.com/repos/octo-org/octo-repo/git/tags{/sha}",
      "hooks_url": "https://api.github.com/repos/octo-org/octo-repo/hooks",
      "issue_comment_url": "https://api.github.com/repos/octo-org/octo-repo/issues/comments{/number}",
      "issue_events_url": "https://api.github.com/repos/octo-org/octo-repo/issues/events{/number}",
      "issues_url": "https://api.github.com/repos/octo-org/octo-repo/issues{/number}",
      "keys_url": "https://api.github.com/repos/octo-org/octo-repo/keys{/key_id}",
      "labels_url": "https://api.github.com/repos/octo-org/octo-repo/labels{/name}",
      "languages_url": "https://api.github.com/repos/octo-org/octo-repo/languages",
      "merges_url": "https://api.github.com/repos/octo-org/octo-repo/merges",
      "milestones_url": "https://api.github.com/repos/octo-org/octo-repo/milestones{/number}",
      "notifications_url": "https://api.github.com/repos/octo-org/octo-repo/notifications{?since,all,participating}",
      "pulls_url": "https://api.github.com/repos/octo-org/octo-repo/pulls{/number}",
      "releases_url": "https://api.github.com/repos/octo-org/octo-repo/releases{/id}",
      "stargazers_url": "https://api.github.com/repos/octo-org/octo-repo/stargazers",
      "statuses_url": "https://api.github.com/repos/octo-org/octo-repo/statuses/{sha}",
      "subscribers_url": "https://api.github.com/repos/octo-org/octo-repo/subscribers",
      "subscription_url": "https://api.github.com/repos/octo-org/octo-repo/subscription",
      "tags_url": "https://api.github.com/repos/octo-org/octo-repo/tags",
      "teams_url": "https://api.github.com/repos/octo-org/octo-repo/teams",
      "trees_url": "https://api.github.com/repos/octo-org/octo-repo/git/trees{/sha}"
    }
  },
  {
    "number": 1,
    "state": "open",
    "dependency": {
      "package": {
        "ecosystem": "pip",
        "name": "ansible"
      },
      "manifest_path": "path/to/requirements.txt",
      "scope": "runtime"
    },
    "security_advisory": {
      "ghsa_id": "GHSA-8f4m-hccc-8qph",
      "cve_id": "CVE-2021-20191",
      "summary": "Insertion of Sensitive Information into Log File in ansible",
      "description": "A flaw was found in ansible. Credentials, such as secrets, are being disclosed in console log by default and not protected by no_log feature when using those modules. An attacker can take advantage of this information to steal those credentials. The highest threat from this vulnerability is to data confidentiality.",
      "vulnerabilities": [
        {
          "package": {
            "ecosystem": "pip",
            "name": "ansible"
          },
          "severity": "medium",
          "vulnerable_version_range": ">= 2.9.0, < 2.9.18",
          "first_patched_version": {
            "identifier": "2.9.18"
          }
        },
        {
          "package": {
            "ecosystem": "pip",
            "name": "ansible"
          },
          "severity": "medium",
          "vulnerable_version_range": "< 2.8.19",
          "first_patched_version": {
            "identifier": "2.8.19"
          }
        },
        {
          "package": {
            "ecosystem": "pip",
            "name": "ansible"
          },
          "severity": "medium",
          "vulnerable_version_range": ">= 2.10.0, < 2.10.7",
          "first_patched_version": {
            "identifier": "2.10.7"
          }
        }
      ],
      "severity": "medium",
      "cvss": {
        "vector_string": "CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N",
        "score": 5.5
      },
      "cvss_severities": {
        "cvss_v3": {
          "vector_string": "CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N",
          "score": 5.5
        },
        "cvss_v4": {
          "vector_string": "CVSS:4.0/AV:L/AC:L/AT:N/PR:N/UI:P/VC:H/VI:H/VA:H/SC:N/SI:N/SA:N",
          "score": 8.5
        }
      },
      "cwes": [
        {
          "cwe_id": "CWE-532",
          "name": "Insertion of Sensitive Information into Log File"
        }
      ],
      "identifiers": [
        {
          "type": "GHSA",
          "value": "GHSA-8f4m-hccc-8qph"
        },
        {
          "type": "CVE",
          "value": "CVE-2021-20191"
        }
      ],
      "references": [
        {
          "url": "https://nvd.nist.gov/vuln/detail/CVE-2021-20191"
        },
        {
          "url": "https://access.redhat.com/security/cve/cve-2021-20191"
        },
        {
          "url": "https://bugzilla.redhat.com/show_bug.cgi?id=1916813"
        }
      ],
      "published_at": "2021-06-01T17:38:00Z",
      "updated_at": "2021-08-12T23:06:00Z",
      "withdrawn_at": null
    },
    "security_vulnerability": {
      "package": {
        "ecosystem": "pip",
        "name": "ansible"
      },
      "severity": "medium",
      "vulnerable_version_range": "< 2.8.19",
      "first_patched_version": {
        "identifier": "2.8.19"
      }
    },
    "url": "https://api.github.com/repos/octo-org/hello-world/dependabot/alerts/1",
    "html_url": "https://github.com/octo-org/hello-world/security/dependabot/1",
    "created_at": "2022-06-14T15:21:52Z",
    "updated_at": "2022-06-14T15:21:52Z",
    "dismissed_at": null,
    "dismissed_by": null,
    "dismissed_reason": null,
    "dismissed_comment": null,
    "fixed_at": null,
    "assignees": [],
    "repository": {
      "id": 664700648,
      "node_id": "MDEwOlJlcG9zaXRvcnk2NjQ3MDA2NDg=",
      "name": "hello-world",
      "full_name": "octo-org/hello-world",
      "owner": {
        "login": "octo-org",
        "id": 6811672,
        "node_id": "MDEyOk9yZ2FuaXphdGlvbjY4MTE2NzI=",
        "avatar_url": "https://avatars3.githubusercontent.com/u/6811672?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/octo-org",
        "html_url": "https://github.com/octo-org",
        "followers_url": "https://api.github.com/users/octo-org/followers",
        "following_url": "https://api.github.com/users/octo-org/following{/other_user}",
        "gists_url": "https://api.github.com/users/octo-org/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/octo-org/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/octo-org/subscriptions",
        "organizations_url": "https://api.github.com/users/octo-org/orgs",
        "repos_url": "https://api.github.com/users/octo-org/repos",
        "events_url": "https://api.github.com/users/octo-org/events{/privacy}",
        "received_events_url": "https://api.github.com/users/octo-org/received_events",
        "type": "Organization",
        "site_admin": false
      },
      "private": true,
      "html_url": "https://github.com/octo-org/hello-world",
      "description": null,
      "fork": false,
      "url": "https://api.github.com/repos/octo-org/hello-world",
      "archive_url": "https://api.github.com/repos/octo-org/hello-world/{archive_format}{/ref}",
      "assignees_url": "https://api.github.com/repos/octo-org/hello-world/assignees{/user}",
      "blobs_url": "https://api.github.com/repos/octo-org/hello-world/git/blobs{/sha}",
      "branches_url": "https://api.github.com/repos/octo-org/hello-world/branches{/branch}",
      "collaborators_url": "https://api.github.com/repos/octo-org/hello-world/collaborators{/collaborator}",
      "comments_url": "https://api.github.com/repos/octo-org/hello-world/comments{/number}",
      "commits_url": "https://api.github.com/repos/octo-org/hello-world/commits{/sha}",
      "compare_url": "https://api.github.com/repos/octo-org/hello-world/compare/{base}...{head}",
      "contents_url": "https://api.github.com/repos/octo-org/hello-world/contents/{+path}",
      "contributors_url": "https://api.github.com/repos/octo-org/hello-world/contributors",
      "deployments_url": "https://api.github.com/repos/octo-org/hello-world/deployments",
      "downloads_url": "https://api.github.com/repos/octo-org/hello-world/downloads",
      "events_url": "https://api.github.com/repos/octo-org/hello-world/events",
      "forks_url": "https://api.github.com/repos/octo-org/hello-world/forks",
      "git_commits_url": "https://api.github.com/repos/octo-org/hello-world/git/commits{/sha}",
      "git_refs_url": "https://api.github.com/repos/octo-org/hello-world/git/refs{/sha}",
      "git_tags_url": "https://api.github.com/repos/octo-org/hello-world/git/tags{/sha}",
      "hooks_url": "https://api.github.com/repos/octo-org/hello-world/hooks",
      "issue_comment_url": "https://api.github.com/repos/octo-org/hello-world/issues/comments{/number}",
      "issue_events_url": "https://api.github.com/repos/octo-org/hello-world/issues/events{/number}",
      "issues_url": "https://api.github.com/repos/octo-org/hello-world/issues{/number}",
      "keys_url": "https://api.github.com/repos/octo-org/hello-world/keys{/key_id}",
      "labels_url": "https://api.github.com/repos/octo-org/hello-world/labels{/name}",
      "languages_url": "https://api.github.com/repos/octo-org/hello-world/languages",
      "merges_url": "https://api.github.com/repos/octo-org/hello-world/merges",
      "milestones_url": "https://api.github.com/repos/octo-org/hello-world/milestones{/number}",
      "notifications_url": "https://api.github.com/repos/octo-org/hello-world/notifications{?since,all,participating}",
      "pulls_url": "https://api.github.com/repos/octo-org/hello-world/pulls{/number}",
      "releases_url": "https://api.github.com/repos/octo-org/hello-world/releases{/id}",
      "stargazers_url": "https://api.github.com/repos/octo-org/hello-world/stargazers",
      "statuses_url": "https://api.github.com/repos/octo-org/hello-world/statuses/{sha}",
      "subscribers_url": "https://api.github.com/repos/octo-org/hello-world/subscribers",
      "subscription_url": "https://api.github.com/repos/octo-org/hello-world/subscription",
      "tags_url": "https://api.github.com/repos/octo-org/hello-world/tags",
      "teams_url": "https://api.github.com/repos/octo-org/hello-world/teams",
      "trees_url": "https://api.github.com/repos/octo-org/hello-world/git/trees{/sha}"
    }
  }
]
```

## List Dependabot alerts for a repository
OAuth app tokens and personal access tokens (classic) need thesecurity_eventsscope to use this endpoint. If this endpoint is only used with public repositories, the token can use thepublic_reposcope instead.

### Fine-grained access tokens for "List Dependabot alerts for a repository"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Dependabot alerts" repository permissions (read)

### Parameters for "List Dependabot alerts for a repository"

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
statestringA comma-separated list of states. If specified, only alerts with these states will be returned.Can be:auto_dismissed,dismissed,fixed,open
severitystringA comma-separated list of severities. If specified, only alerts with these severities will be returned.Can be:low,medium,high,critical
ecosystemstringA comma-separated list of ecosystems. If specified, only alerts for these ecosystems will be returned.Can be:composer,go,maven,npm,nuget,pip,pub,rubygems,rust
packagestringA comma-separated list of package names. If specified, only alerts for these packages will be returned.
manifeststringA comma-separated list of full manifest paths. If specified, only alerts for these manifests will be returned.
epss_percentagestringCVE Exploit Prediction Scoring System (EPSS) percentage. Can be specified as:An exact number (n)Comparators such as>n,<n,>=n,<=nA range liken..n, wherenis a number from 0.0 to 1.0Filters the list of alerts based on EPSS percentages. If specified, only alerts with the provided EPSS percentages will be returned.
hasFilters the list of alerts based on whether the alert has the given value. If specified, only alerts meeting this criterion will be returned.
Multiplehasfilters can be passed to filter for alerts that have all of the values. Currently, onlypatchis supported.
assigneestringFilter alerts by assignees.
Provide a comma-separated list of user handles (e.g.,octocatoroctocat,hubot) to return alerts assigned to any of the specified users.
Use*to list alerts with at least one assignee ornoneto list alerts with no assignees.
scopestringThe scope of the vulnerable dependency. If specified, only alerts with this scope will be returned.Can be one of:development,runtime
sortstringThe property by which to sort the results.createdmeans when the alert was created.updatedmeans when the alert's state last changed.epss_percentagesorts alerts by the Exploit Prediction Scoring System (EPSS) percentage.Default:createdCan be one of:created,updated,epss_percentage
directionstringThe direction to sort the results by.Default:descCan be one of:asc,desc
beforestringA cursor, as given in theLink header. If specified, the query only searches for results before this cursor. For more information, see "Using pagination in the REST API."
afterstringA cursor, as given in theLink header. If specified, the query only searches for results after this cursor. For more information, see "Using pagination in the REST API."
per_pageintegerThe number of results per page (max 100). For more information, see "Using pagination in the REST API."Default:30
[/TABLE]
A comma-separated list of states. If specified, only alerts with these states will be returned.
Can be:auto_dismissed,dismissed,fixed,open
A comma-separated list of severities. If specified, only alerts with these severities will be returned.
Can be:low,medium,high,critical
A comma-separated list of ecosystems. If specified, only alerts for these ecosystems will be returned.
Can be:composer,go,maven,npm,nuget,pip,pub,rubygems,rust
A comma-separated list of package names. If specified, only alerts for these packages will be returned.
A comma-separated list of full manifest paths. If specified, only alerts for these manifests will be returned.

```
epss_percentage
```
CVE Exploit Prediction Scoring System (EPSS) percentage. Can be specified as:
- An exact number (n)
- Comparators such as>n,<n,>=n,<=n
- A range liken..n, wherenis a number from 0.0 to 1.0
Filters the list of alerts based on EPSS percentages. If specified, only alerts with the provided EPSS percentages will be returned.
Filters the list of alerts based on whether the alert has the given value. If specified, only alerts meeting this criterion will be returned.
Multiplehasfilters can be passed to filter for alerts that have all of the values. Currently, onlypatchis supported.
Filter alerts by assignees.
Provide a comma-separated list of user handles (e.g.,octocatoroctocat,hubot) to return alerts assigned to any of the specified users.
Use*to list alerts with at least one assignee ornoneto list alerts with no assignees.
The scope of the vulnerable dependency. If specified, only alerts with this scope will be returned.
Can be one of:development,runtime

```
development
```
The property by which to sort the results.createdmeans when the alert was created.updatedmeans when the alert's state last changed.epss_percentagesorts alerts by the Exploit Prediction Scoring System (EPSS) percentage.
Default:created
Can be one of:created,updated,epss_percentage

```
epss_percentage
```
The direction to sort the results by.
Default:desc
Can be one of:asc,desc
A cursor, as given in theLink header. If specified, the query only searches for results before this cursor. For more information, see "Using pagination in the REST API."
A cursor, as given in theLink header. If specified, the query only searches for results after this cursor. For more information, see "Using pagination in the REST API."
The number of results per page (max 100). For more information, see "Using pagination in the REST API."
Default:30

### HTTP response status codes for "List Dependabot alerts for a repository"

[TABLE]
Status code | Description
200 | OK
304 | Not modified
400 | Bad Request
403 | Forbidden
404 | Resource not found
422 | Validation failed, or the endpoint has been spammed.
[/TABLE]
OK
Not modified
Bad Request
Forbidden
Resource not found
Validation failed, or the endpoint has been spammed.

### Code samples for "List Dependabot alerts for a repository"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/dependabot/alerts
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
    "state": "dismissed",
    "dependency": {
      "package": {
        "ecosystem": "pip",
        "name": "django"
      },
      "manifest_path": "path/to/requirements.txt",
      "scope": "runtime"
    },
    "security_advisory": {
      "ghsa_id": "GHSA-rf4j-j272-fj86",
      "cve_id": "CVE-2018-6188",
      "summary": "Django allows remote attackers to obtain potentially sensitive information by leveraging data exposure from the confirm_login_allowed() method, as demonstrated by discovering whether a user account is inactive",
      "description": "django.contrib.auth.forms.AuthenticationForm in Django 2.0 before 2.0.2, and 1.11.8 and 1.11.9, allows remote attackers to obtain potentially sensitive information by leveraging data exposure from the confirm_login_allowed() method, as demonstrated by discovering whether a user account is inactive.",
      "vulnerabilities": [
        {
          "package": {
            "ecosystem": "pip",
            "name": "django"
          },
          "severity": "high",
          "vulnerable_version_range": ">= 2.0.0, < 2.0.2",
          "first_patched_version": {
            "identifier": "2.0.2"
          }
        },
        {
          "package": {
            "ecosystem": "pip",
            "name": "django"
          },
          "severity": "high",
          "vulnerable_version_range": ">= 1.11.8, < 1.11.10",
          "first_patched_version": {
            "identifier": "1.11.10"
          }
        }
      ],
      "severity": "high",
      "cvss": {
        "vector_string": "CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N",
        "score": 7.5
      },
      "cvss_severities": {
        "cvss_v3": {
          "vector_string": "CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N",
          "score": 7.5
        },
        "cvss_v4": {
          "vector_string": "CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:H/VI:N/VA:N/SC:N/SI:N/SA:N",
          "score": 8.7
        }
      },
      "epss": [
        {
          "percentage": 0.00045,
          "percentile": "0.16001e0"
        }
      ],
      "cwes": [
        {
          "cwe_id": "CWE-200",
          "name": "Exposure of Sensitive Information to an Unauthorized Actor"
        }
      ],
      "identifiers": [
        {
          "type": "GHSA",
          "value": "GHSA-rf4j-j272-fj86"
        },
        {
          "type": "CVE",
          "value": "CVE-2018-6188"
        }
      ],
      "references": [
        {
          "url": "https://nvd.nist.gov/vuln/detail/CVE-2018-6188"
        },
        {
          "url": "https://github.com/advisories/GHSA-rf4j-j272-fj86"
        },
        {
          "url": "https://usn.ubuntu.com/3559-1/"
        },
        {
          "url": "https://www.djangoproject.com/weblog/2018/feb/01/security-releases/"
        },
        {
          "url": "http://www.securitytracker.com/id/1040422"
        }
      ],
      "published_at": "2018-10-03T21:13:54Z",
      "updated_at": "2022-04-26T18:35:37Z",
      "withdrawn_at": null
    },
    "security_vulnerability": {
      "package": {
        "ecosystem": "pip",
        "name": "django"
      },
      "severity": "high",
      "vulnerable_version_range": ">= 2.0.0, < 2.0.2",
      "first_patched_version": {
        "identifier": "2.0.2"
      }
    },
    "url": "https://api.github.com/repos/octocat/hello-world/dependabot/alerts/2",
    "html_url": "https://github.com/octocat/hello-world/security/dependabot/2",
    "created_at": "2022-06-15T07:43:03Z",
    "updated_at": "2022-08-23T14:29:47Z",
    "dismissed_at": "2022-08-23T14:29:47Z",
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
    "dismissed_reason": "tolerable_risk",
    "dismissed_comment": "This alert is accurate but we use a sanitizer.",
    "fixed_at": null,
    "assignees": [
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
  },
  {
    "number": 1,
    "state": "open",
    "dependency": {
      "package": {
        "ecosystem": "pip",
        "name": "ansible"
      },
      "manifest_path": "path/to/requirements.txt",
      "scope": "runtime"
    },
    "security_advisory": {
      "ghsa_id": "GHSA-8f4m-hccc-8qph",
      "cve_id": "CVE-2021-20191",
      "summary": "Insertion of Sensitive Information into Log File in ansible",
      "description": "A flaw was found in ansible. Credentials, such as secrets, are being disclosed in console log by default and not protected by no_log feature when using those modules. An attacker can take advantage of this information to steal those credentials. The highest threat from this vulnerability is to data confidentiality.",
      "vulnerabilities": [
        {
          "package": {
            "ecosystem": "pip",
            "name": "ansible"
          },
          "severity": "medium",
          "vulnerable_version_range": ">= 2.9.0, < 2.9.18",
          "first_patched_version": {
            "identifier": "2.9.18"
          }
        },
        {
          "package": {
            "ecosystem": "pip",
            "name": "ansible"
          },
          "severity": "medium",
          "vulnerable_version_range": "< 2.8.19",
          "first_patched_version": {
            "identifier": "2.8.19"
          }
        },
        {
          "package": {
            "ecosystem": "pip",
            "name": "ansible"
          },
          "severity": "medium",
          "vulnerable_version_range": ">= 2.10.0, < 2.10.7",
          "first_patched_version": {
            "identifier": "2.10.7"
          }
        }
      ],
      "severity": "medium",
      "cvss": {
        "vector_string": "CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N",
        "score": 5.5
      },
      "cvss_severities": {
        "cvss_v3": {
          "vector_string": "CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N",
          "score": 5.5
        },
        "cvss_v4": {
          "vector_string": "CVSS:4.0/AV:L/AC:L/AT:N/PR:N/UI:P/VC:H/VI:H/VA:H/SC:N/SI:N/SA:N",
          "score": 8.5
        }
      },
      "cwes": [
        {
          "cwe_id": "CWE-532",
          "name": "Insertion of Sensitive Information into Log File"
        }
      ],
      "identifiers": [
        {
          "type": "GHSA",
          "value": "GHSA-8f4m-hccc-8qph"
        },
        {
          "type": "CVE",
          "value": "CVE-2021-20191"
        }
      ],
      "references": [
        {
          "url": "https://nvd.nist.gov/vuln/detail/CVE-2021-20191"
        },
        {
          "url": "https://access.redhat.com/security/cve/cve-2021-20191"
        },
        {
          "url": "https://bugzilla.redhat.com/show_bug.cgi?id=1916813"
        }
      ],
      "published_at": "2021-06-01T17:38:00Z",
      "updated_at": "2021-08-12T23:06:00Z",
      "withdrawn_at": null
    },
    "security_vulnerability": {
      "package": {
        "ecosystem": "pip",
        "name": "ansible"
      },
      "severity": "medium",
      "vulnerable_version_range": "< 2.8.19",
      "first_patched_version": {
        "identifier": "2.8.19"
      }
    },
    "url": "https://api.github.com/repos/octocat/hello-world/dependabot/alerts/1",
    "html_url": "https://github.com/octocat/hello-world/security/dependabot/1",
    "created_at": "2022-06-14T15:21:52Z",
    "updated_at": "2022-06-14T15:21:52Z",
    "dismissed_at": null,
    "dismissed_by": null,
    "dismissed_reason": null,
    "dismissed_comment": null,
    "fixed_at": null,
    "assignees": []
  }
]
```

## Get a Dependabot alert
OAuth app tokens and personal access tokens (classic) need thesecurity_eventsscope to use this endpoint. If this endpoint is only used with public repositories, the token can use thepublic_reposcope instead.

### Fine-grained access tokens for "Get a Dependabot alert"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Dependabot alerts" repository permissions (read)

### Parameters for "Get a Dependabot alert"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
alert_numberintegerRequiredThe number that identifies a Dependabot alert in its repository.
You can find this at the end of the URL for a Dependabot alert within GitHub,
or innumberfields in the response from theGET /repos/{owner}/{repo}/dependabot/alertsoperation.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.

```
alert_number
```
The number that identifies a Dependabot alert in its repository.
You can find this at the end of the URL for a Dependabot alert within GitHub,
or innumberfields in the response from theGET /repos/{owner}/{repo}/dependabot/alertsoperation.

### HTTP response status codes for "Get a Dependabot alert"

[TABLE]
Status code | Description
200 | OK
304 | Not modified
403 | Forbidden
404 | Resource not found
[/TABLE]
OK
Not modified
Forbidden
Resource not found

### Code samples for "Get a Dependabot alert"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/dependabot/alerts/ALERT_NUMBER
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "number": 1,
  "state": "open",
  "dependency": {
    "package": {
      "ecosystem": "pip",
      "name": "ansible"
    },
    "manifest_path": "path/to/requirements.txt",
    "scope": "runtime"
  },
  "security_advisory": {
    "ghsa_id": "GHSA-8f4m-hccc-8qph",
    "cve_id": "CVE-2021-20191",
    "summary": "Insertion of Sensitive Information into Log File in ansible",
    "description": "A flaw was found in ansible. Credentials, such as secrets, are being disclosed in console log by default and not protected by no_log feature when using those modules. An attacker can take advantage of this information to steal those credentials. The highest threat from this vulnerability is to data confidentiality.",
    "vulnerabilities": [
      {
        "package": {
          "ecosystem": "pip",
          "name": "ansible"
        },
        "severity": "medium",
        "vulnerable_version_range": ">= 2.9.0, < 2.9.18",
        "first_patched_version": {
          "identifier": "2.9.18"
        }
      },
      {
        "package": {
          "ecosystem": "pip",
          "name": "ansible"
        },
        "severity": "medium",
        "vulnerable_version_range": "< 2.8.19",
        "first_patched_version": {
          "identifier": "2.8.19"
        }
      },
      {
        "package": {
          "ecosystem": "pip",
          "name": "ansible"
        },
        "severity": "medium",
        "vulnerable_version_range": ">= 2.10.0, < 2.10.7",
        "first_patched_version": {
          "identifier": "2.10.7"
        }
      }
    ],
    "severity": "medium",
    "cvss": {
      "vector_string": "CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N",
      "score": 5.5
    },
    "cvss_severities": {
      "cvss_v3": {
        "vector_string": "CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N",
        "score": 5.5
      },
      "cvss_v4": {
        "vector_string": "CVSS:4.0/AV:L/AC:L/AT:N/PR:N/UI:P/VC:H/VI:H/VA:H/SC:N/SI:N/SA:N",
        "score": 8.5
      }
    },
    "epss": [
      {
        "percentage": 0.00045,
        "percentile": "0.16001e0"
      }
    ],
    "cwes": [
      {
        "cwe_id": "CWE-532",
        "name": "Insertion of Sensitive Information into Log File"
      }
    ],
    "identifiers": [
      {
        "type": "GHSA",
        "value": "GHSA-8f4m-hccc-8qph"
      },
      {
        "type": "CVE",
        "value": "CVE-2021-20191"
      }
    ],
    "references": [
      {
        "url": "https://nvd.nist.gov/vuln/detail/CVE-2021-20191"
      },
      {
        "url": "https://access.redhat.com/security/cve/cve-2021-20191"
      },
      {
        "url": "https://bugzilla.redhat.com/show_bug.cgi?id=1916813"
      }
    ],
    "published_at": "2021-06-01T17:38:00Z",
    "updated_at": "2021-08-12T23:06:00Z",
    "withdrawn_at": null
  },
  "security_vulnerability": {
    "package": {
      "ecosystem": "pip",
      "name": "ansible"
    },
    "severity": "medium",
    "vulnerable_version_range": "< 2.8.19",
    "first_patched_version": {
      "identifier": "2.8.19"
    }
  },
  "url": "https://api.github.com/repos/octocat/hello-world/dependabot/alerts/1",
  "html_url": "https://github.com/octocat/hello-world/security/dependabot/1",
  "created_at": "2022-06-14T15:21:52Z",
  "updated_at": "2022-06-14T15:21:52Z",
  "dismissed_at": null,
  "dismissed_by": null,
  "dismissed_reason": null,
  "dismissed_comment": null,
  "fixed_at": null,
  "assignees": [
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
}
```

## Update a Dependabot alert
The authenticated user must have access to security alerts for the repository to use this endpoint. For more information, see "Granting access to security alerts."
OAuth app tokens and personal access tokens (classic) need thesecurity_eventsscope to use this endpoint. If this endpoint is only used with public repositories, the token can use thepublic_reposcope instead.

### Fine-grained access tokens for "Update a Dependabot alert"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Dependabot alerts" repository permissions (write)

### Parameters for "Update a Dependabot alert"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
alert_numberintegerRequiredThe number that identifies a Dependabot alert in its repository.
You can find this at the end of the URL for a Dependabot alert within GitHub,
or innumberfields in the response from theGET /repos/{owner}/{repo}/dependabot/alertsoperation.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.

```
alert_number
```
The number that identifies a Dependabot alert in its repository.
You can find this at the end of the URL for a Dependabot alert within GitHub,
or innumberfields in the response from theGET /repos/{owner}/{repo}/dependabot/alertsoperation.

[TABLE]
Name, Type, Description
statestringThe state of the Dependabot alert.
Adismissed_reasonmust be provided when setting the state todismissed.Can be one of:dismissed,open
dismissed_reasonstringRequired whenstateisdismissed.A reason for dismissing the alert.Can be one of:fix_started,inaccurate,no_bandwidth,not_used,tolerable_risk
dismissed_commentstringAn optional comment associated with dismissing the alert.
assigneesarray of stringsUsernames to assign to this Dependabot Alert.
Pass one or more user logins toreplacethe set of assignees on this alert.
Send an empty array ([]) to clear all assignees from the alert.
[/TABLE]
The state of the Dependabot alert.
Adismissed_reasonmust be provided when setting the state todismissed.
Can be one of:dismissed,open

```
dismissed_reason
```
Required whenstateisdismissed.A reason for dismissing the alert.
Can be one of:fix_started,inaccurate,no_bandwidth,not_used,tolerable_risk

```
fix_started
```

```
no_bandwidth
```

```
tolerable_risk
```

```
dismissed_comment
```
An optional comment associated with dismissing the alert.
Usernames to assign to this Dependabot Alert.
Pass one or more user logins toreplacethe set of assignees on this alert.
Send an empty array ([]) to clear all assignees from the alert.

### HTTP response status codes for "Update a Dependabot alert"

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

### Code samples for "Update a Dependabot alert"

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
  https://api.github.com/repos/OWNER/REPO/dependabot/alerts/ALERT_NUMBER \
  -d '{"state":"dismissed","dismissed_reason":"tolerable_risk","dismissed_comment":"This alert is accurate but we use a sanitizer."}'
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "number": 2,
  "state": "dismissed",
  "dependency": {
    "package": {
      "ecosystem": "pip",
      "name": "django"
    },
    "manifest_path": "path/to/requirements.txt",
    "scope": "runtime"
  },
  "security_advisory": {
    "ghsa_id": "GHSA-rf4j-j272-fj86",
    "cve_id": "CVE-2018-6188",
    "summary": "Django allows remote attackers to obtain potentially sensitive information by leveraging data exposure from the confirm_login_allowed() method, as demonstrated by discovering whether a user account is inactive",
    "description": "django.contrib.auth.forms.AuthenticationForm in Django 2.0 before 2.0.2, and 1.11.8 and 1.11.9, allows remote attackers to obtain potentially sensitive information by leveraging data exposure from the confirm_login_allowed() method, as demonstrated by discovering whether a user account is inactive.",
    "vulnerabilities": [
      {
        "package": {
          "ecosystem": "pip",
          "name": "django"
        },
        "severity": "high",
        "vulnerable_version_range": ">= 2.0.0, < 2.0.2",
        "first_patched_version": {
          "identifier": "2.0.2"
        }
      },
      {
        "package": {
          "ecosystem": "pip",
          "name": "django"
        },
        "severity": "high",
        "vulnerable_version_range": ">= 1.11.8, < 1.11.10",
        "first_patched_version": {
          "identifier": "1.11.10"
        }
      }
    ],
    "severity": "high",
    "cvss": {
      "vector_string": "CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N",
      "score": 7.5
    },
    "cvss_severities": {
      "cvss_v3": {
        "vector_string": "CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N",
        "score": 7.5
      },
      "cvss_v4": {
        "vector_string": "CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:H/VI:N/VA:N/SC:N/SI:N/SA:N",
        "score": 8.7
      }
    },
    "cwes": [
      {
        "cwe_id": "CWE-200",
        "name": "Exposure of Sensitive Information to an Unauthorized Actor"
      }
    ],
    "identifiers": [
      {
        "type": "GHSA",
        "value": "GHSA-rf4j-j272-fj86"
      },
      {
        "type": "CVE",
        "value": "CVE-2018-6188"
      }
    ],
    "references": [
      {
        "url": "https://nvd.nist.gov/vuln/detail/CVE-2018-6188"
      },
      {
        "url": "https://github.com/advisories/GHSA-rf4j-j272-fj86"
      },
      {
        "url": "https://usn.ubuntu.com/3559-1/"
      },
      {
        "url": "https://www.djangoproject.com/weblog/2018/feb/01/security-releases/"
      },
      {
        "url": "http://www.securitytracker.com/id/1040422"
      }
    ],
    "published_at": "2018-10-03T21:13:54Z",
    "updated_at": "2022-04-26T18:35:37Z",
    "withdrawn_at": null
  },
  "security_vulnerability": {
    "package": {
      "ecosystem": "pip",
      "name": "django"
    },
    "severity": "high",
    "vulnerable_version_range": ">= 2.0.0, < 2.0.2",
    "first_patched_version": {
      "identifier": "2.0.2"
    }
  },
  "url": "https://api.github.com/repos/octocat/hello-world/dependabot/alerts/2",
  "html_url": "https://github.com/octocat/hello-world/security/dependabot/2",
  "created_at": "2022-06-15T07:43:03Z",
  "updated_at": "2022-08-23T14:29:47Z",
  "dismissed_at": "2022-08-23T14:29:47Z",
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
  "dismissed_reason": "tolerable_risk",
  "dismissed_comment": "This alert is accurate but we use a sanitizer.",
  "fixed_at": null,
  "assignees": []
}
```