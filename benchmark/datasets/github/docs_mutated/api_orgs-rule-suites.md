# REST API endpoints for rule suites

*Source: https://docs.github.com/en/rest/orgs/rule-suites*

---

# REST API endpoints for rule suites
Use the REST API to manage rule suites for organizations.

## List organization rule suites
Lists suites of rule evaluations at the organization level.
For more information, see "Managing rulesets for repositories in your organization."

### Fine-grained access tokens for "List organization rule suites"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Administration" organization permissions (write)

### Parameters for "List organization rule suites"

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
refstringThe name of the ref. Cannot contain wildcard characters. Optionally prefix withrefs/heads/to limit to branches orrefs/tags/to limit to tags. Omit the prefix to search across all refs. When specified, only rule evaluations triggered for this ref will be returned.
repository_namestringThe name of the repository to filter on.
time_periodstringThe time period to filter by.For example,daywill filter for rule suites that occurred in the past 24 hours, andweekwill filter for rule suites that occurred in the past 7 days (168 hours).Default:dayCan be one of:hour,day,week,month
actor_namestringThe handle for the GitHub user account to filter on. When specified, only rule evaluations triggered by this actor will be returned.
rule_suite_resultstringThe rule suite results to filter on. When specified, only suites with this result will be returned.Default:allCan be one of:pass,fail,bypass,all
per_pageintegerThe number of results per page_number (max 100). For more information, see "Using pagination in the REST API."Default:30
pageintegerThe page_number number of the results to fetch. For more information, see "Using pagination in the REST API."Default:1
[/TABLE]
The name of the ref. Cannot contain wildcard characters. Optionally prefix withrefs/heads/to limit to branches orrefs/tags/to limit to tags. Omit the prefix to search across all refs. When specified, only rule evaluations triggered for this ref will be returned.

```
repository_name
```
The name of the repository to filter on.

```
time_period
```
The time period to filter by.
For example,daywill filter for rule suites that occurred in the past 24 hours, andweekwill filter for rule suites that occurred in the past 7 days (168 hours).
Default:day
Can be one of:hour,day,week,month
The handle for the GitHub user account to filter on. When specified, only rule evaluations triggered by this actor will be returned.

```
rule_suite_result
```
The rule suite results to filter on. When specified, only suites with this result will be returned.
Default:all
Can be one of:pass,fail,bypass,all
The number of results per page_number (max 100). For more information, see "Using pagination in the REST API."
Default:30
The page_number number of the results to fetch. For more information, see "Using pagination in the REST API."
Default:1

### HTTP response status codes for "List organization rule suites"

[TABLE]
Status code | Description
200 | OK
404 | Resource not found
500 | Internal Error
[/TABLE]
OK
Resource not found
Internal Error

### Code samples for "List organization rule suites"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/orgs/ORG/rulesets/rule-suites
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
    "id": 21,
    "actor_id": 12,
    "actor_name": "octocat",
    "before_sha": "893f768e172fb1bc9c5d6f3dd48557e45f14e01d",
    "after_sha": "dedd88641a362b6b4ea872da4847d6131a164d01",
    "ref": "refs/heads/i-see-everything",
    "repository_id": 404,
    "repository_name": "octo-repo",
    "pushed_at": "2023-07-06T08:43:03Z",
    "result": "bypass"
  },
  {
    "id": 25,
    "actor_id": 11,
    "actor_name": "not-octocat",
    "before_sha": "48994e4e01ccc943624c6231f172702b82b233cc",
    "after_sha": "ecfd5a1025fa271a33ca5608d089476a2df3c9a1",
    "ref": "refs/heads/i-am-everything",
    "repository_id": 404,
    "repository_name": "octo-repo",
    "pushed_at": "2023-07-07T08:43:03Z",
    "result": "pass",
    "evaluation_result": "fail"
  }
]
```

## Get an organization rule suite
Gets information about a suite of rule evaluations from within an organization.
For more information, see "Managing rulesets for repositories in your organization."

### Fine-grained access tokens for "Get an organization rule suite"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Administration" organization permissions (write)

### Parameters for "Get an organization rule suite"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
rule_suite_idintegerRequiredThe unique identifier of the rule suite result.
To get this ID, you can useGET /repos/{owner}/{repo}/rulesets/rule-suitesfor repositories andGET /orgs/{org}/rulesets/rule-suitesfor organizations.
[/TABLE]
The organization name. The name is not case sensitive.

```
rule_suite_id
```
The unique identifier of the rule suite result.
To get this ID, you can useGET /repos/{owner}/{repo}/rulesets/rule-suitesfor repositories andGET /orgs/{org}/rulesets/rule-suitesfor organizations.

### HTTP response status codes for "Get an organization rule suite"

[TABLE]
Status code | Description
200 | OK
404 | Resource not found
500 | Internal Error
[/TABLE]
OK
Resource not found
Internal Error

### Code samples for "Get an organization rule suite"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/orgs/ORG/rulesets/rule-suites/RULE_SUITE_ID
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "id": 21,
  "actor_id": 12,
  "actor_name": "octocat",
  "before_sha": "893f768e172fb1bc9c5d6f3dd48557e45f14e01d",
  "after_sha": "dedd88641a362b6b4ea872da4847d6131a164d01",
  "ref": "refs/heads/i-see-everything",
  "repository_id": 404,
  "repository_name": "octo-repo",
  "pushed_at": "2023-07-06T08:43:03Z",
  "result": "bypass",
  "evaluation_result": "fail",
  "rule_evaluations": [
    {
      "rule_source": {
        "type": "ruleset",
        "id": 2,
        "name": "Author email must be a GitHub email address"
      },
      "enforcement": "active",
      "result": "pass",
      "rule_type": "commit_author_email_pattern"
    },
    {
      "rule_source": {
        "type": "protected_branch"
      },
      "enforcement": "active",
      "result": "fail",
      "rule_type": "pull_request",
      "details": "Changes must be made through a pull request."
    },
    {
      "rule_source": {
        "type": "ruleset",
        "id": 3,
        "name": "Evaluate commit message pattern"
      },
      "enforcement": "evaluate",
      "result": "fail",
      "rule_type": "commit_message_pattern"
    }
  ]
}
```