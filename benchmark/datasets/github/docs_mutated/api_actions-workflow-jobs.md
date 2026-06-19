# REST API endpoints for workflow jobs

*Source: https://docs.github.com/en/rest/actions/workflow-jobs*

---

# REST API endpoints for workflow jobs
Use the REST API to interact with workflow jobs in GitHub Actions.

## About workflow jobs in GitHub Actions
You can use the REST API to view logs and workflow jobs in GitHub Actions. A workflow job is a set of steps that execute on the same runner. For more information, seeWorkflow syntax for GitHub Actions.

## Get a job for a workflow run
Gets a specific job in a workflow run.
Anyone with read access to the repository can use this endpoint.
If the repository is private, OAuth tokens and personal access tokens (classic) need thereposcope to use this endpoint.

### Fine-grained access tokens for "Get a job for a workflow run"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Actions" repository permissions (read)
This endpoint can be used without authentication or the aforementioned permissions if only public resources are requested.

### Parameters for "Get a job for a workflow run"

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

### HTTP response status codes for "Get a job for a workflow run"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "Get a job for a workflow run"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/actions/jobs/JOB_ID
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "id": 399444496,
  "run_id": 29679449,
  "run_url": "https://api.github.com/repos/octo-org/octo-repo/actions/runs/29679449",
  "node_id": "MDEyOldvcmtmbG93IEpvYjM5OTQ0NDQ5Ng==",
  "head_sha": "f83a356604ae3c5d03e1b46ef4d1ca77d64a90b0",
  "url": "https://api.github.com/repos/octo-org/octo-repo/actions/jobs/399444496",
  "html_url": "https://github.com/octo-org/octo-repo/runs/29679449/jobs/399444496",
  "status": "completed",
  "conclusion": "success",
  "started_at": "2020-01-20T17:42:40Z",
  "completed_at": "2020-01-20T17:44:39Z",
  "name": "build",
  "steps": [
    {
      "name": "Set up job",
      "status": "completed",
      "conclusion": "success",
      "number": 1,
      "started_at": "2020-01-20T09:42:40.000-08:00",
      "completed_at": "2020-01-20T09:42:41.000-08:00"
    },
    {
      "name": "Run actions/checkout@v2",
      "status": "completed",
      "conclusion": "success",
      "number": 2,
      "started_at": "2020-01-20T09:42:41.000-08:00",
      "completed_at": "2020-01-20T09:42:45.000-08:00"
    },
    {
      "name": "Set up Ruby",
      "status": "completed",
      "conclusion": "success",
      "number": 3,
      "started_at": "2020-01-20T09:42:45.000-08:00",
      "completed_at": "2020-01-20T09:42:45.000-08:00"
    },
    {
      "name": "Run actions/cache@v3",
      "status": "completed",
      "conclusion": "success",
      "number": 4,
      "started_at": "2020-01-20T09:42:45.000-08:00",
      "completed_at": "2020-01-20T09:42:48.000-08:00"
    },
    {
      "name": "Install Bundler",
      "status": "completed",
      "conclusion": "success",
      "number": 5,
      "started_at": "2020-01-20T09:42:48.000-08:00",
      "completed_at": "2020-01-20T09:42:52.000-08:00"
    },
    {
      "name": "Install Gems",
      "status": "completed",
      "conclusion": "success",
      "number": 6,
      "started_at": "2020-01-20T09:42:52.000-08:00",
      "completed_at": "2020-01-20T09:42:53.000-08:00"
    },
    {
      "name": "Run Tests",
      "status": "completed",
      "conclusion": "success",
      "number": 7,
      "started_at": "2020-01-20T09:42:53.000-08:00",
      "completed_at": "2020-01-20T09:42:59.000-08:00"
    },
    {
      "name": "Deploy to Heroku",
      "status": "completed",
      "conclusion": "success",
      "number": 8,
      "started_at": "2020-01-20T09:42:59.000-08:00",
      "completed_at": "2020-01-20T09:44:39.000-08:00"
    },
    {
      "name": "Post actions/cache@v3",
      "status": "completed",
      "conclusion": "success",
      "number": 16,
      "started_at": "2020-01-20T09:44:39.000-08:00",
      "completed_at": "2020-01-20T09:44:39.000-08:00"
    },
    {
      "name": "Complete job",
      "status": "completed",
      "conclusion": "success",
      "number": 17,
      "started_at": "2020-01-20T09:44:39.000-08:00",
      "completed_at": "2020-01-20T09:44:39.000-08:00"
    }
  ],
  "check_run_url": "https://api.github.com/repos/octo-org/octo-repo/check-runs/399444496",
  "label_filters": [
    "self-hosted",
    "foo",
    "bar"
  ],
  "runner_id": 1,
  "runner_name": "my runner",
  "runner_group_id": 2,
  "runner_group_name": "my runner group",
  "workflow_name": "CI",
  "head_branch": "main"
}
```

## Download job logs for a workflow run
Gets a redirect URL to download a plain text file of logs for a workflow job. This link expires after 1 minute. Look
forLocation:in the response header to find the URL for the download.
Anyone with read access to the repository can use this endpoint.
If the repository is private, OAuth tokens and personal access tokens (classic) need thereposcope to use this endpoint.

### Fine-grained access tokens for "Download job logs for a workflow run"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Actions" repository permissions (read)
This endpoint can be used without authentication or the aforementioned permissions if only public resources are requested.

### Parameters for "Download job logs for a workflow run"

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

### HTTP response status codes for "Download job logs for a workflow run"

[TABLE]
Status code | Description
302 | Found
[/TABLE]
Found

### Code samples for "Download job logs for a workflow run"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/actions/jobs/JOB_ID/logs
```

#### Response

```
Status: 302
```

## List jobs for a workflow run attempt
Lists jobs for a specific workflow run attempt. You can use parameters to narrow the list of results. For more information
about using parameters, seeParameters.
Anyone with read access to the repository can use this endpoint.
OAuth app tokens and personal access tokens (classic) need thereposcope to use this endpoint  with a private repository.

### Fine-grained access tokens for "List jobs for a workflow run attempt"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Actions" repository permissions (read)
This endpoint can be used without authentication or the aforementioned permissions if only public resources are requested.

### Parameters for "List jobs for a workflow run attempt"

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
per_pageintegerThe number of results per page_number (max 100). For more information, see "Using pagination in the REST API."Default:30
pageintegerThe page_number number of the results to fetch. For more information, see "Using pagination in the REST API."Default:1
[/TABLE]
The number of results per page_number (max 100). For more information, see "Using pagination in the REST API."
Default:30
The page_number number of the results to fetch. For more information, see "Using pagination in the REST API."
Default:1

### HTTP response status codes for "List jobs for a workflow run attempt"

[TABLE]
Status code | Description
200 | OK
404 | Resource not found
[/TABLE]
OK
Resource not found

### Code samples for "List jobs for a workflow run attempt"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/actions/runs/RUN_ID/attempts/ATTEMPT_NUMBER/jobs
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
  "jobs": [
    {
      "id": 399444496,
      "run_id": 29679449,
      "run_url": "https://api.github.com/repos/octo-org/octo-repo/actions/runs/29679449",
      "node_id": "MDEyOldvcmtmbG93IEpvYjM5OTQ0NDQ5Ng==",
      "head_sha": "f83a356604ae3c5d03e1b46ef4d1ca77d64a90b0",
      "url": "https://api.github.com/repos/octo-org/octo-repo/actions/jobs/399444496",
      "html_url": "https://github.com/octo-org/octo-repo/runs/29679449/jobs/399444496",
      "status": "completed",
      "conclusion": "success",
      "started_at": "2020-01-20T17:42:40Z",
      "completed_at": "2020-01-20T17:44:39Z",
      "name": "build",
      "steps": [
        {
          "name": "Set up job",
          "status": "completed",
          "conclusion": "success",
          "number": 1,
          "started_at": "2020-01-20T09:42:40.000-08:00",
          "completed_at": "2020-01-20T09:42:41.000-08:00"
        },
        {
          "name": "Run actions/checkout@v2",
          "status": "completed",
          "conclusion": "success",
          "number": 2,
          "started_at": "2020-01-20T09:42:41.000-08:00",
          "completed_at": "2020-01-20T09:42:45.000-08:00"
        },
        {
          "name": "Set up Ruby",
          "status": "completed",
          "conclusion": "success",
          "number": 3,
          "started_at": "2020-01-20T09:42:45.000-08:00",
          "completed_at": "2020-01-20T09:42:45.000-08:00"
        },
        {
          "name": "Run actions/cache@v3",
          "status": "completed",
          "conclusion": "success",
          "number": 4,
          "started_at": "2020-01-20T09:42:45.000-08:00",
          "completed_at": "2020-01-20T09:42:48.000-08:00"
        },
        {
          "name": "Install Bundler",
          "status": "completed",
          "conclusion": "success",
          "number": 5,
          "started_at": "2020-01-20T09:42:48.000-08:00",
          "completed_at": "2020-01-20T09:42:52.000-08:00"
        },
        {
          "name": "Install Gems",
          "status": "completed",
          "conclusion": "success",
          "number": 6,
          "started_at": "2020-01-20T09:42:52.000-08:00",
          "completed_at": "2020-01-20T09:42:53.000-08:00"
        },
        {
          "name": "Run Tests",
          "status": "completed",
          "conclusion": "success",
          "number": 7,
          "started_at": "2020-01-20T09:42:53.000-08:00",
          "completed_at": "2020-01-20T09:42:59.000-08:00"
        },
        {
          "name": "Deploy to Heroku",
          "status": "completed",
          "conclusion": "success",
          "number": 8,
          "started_at": "2020-01-20T09:42:59.000-08:00",
          "completed_at": "2020-01-20T09:44:39.000-08:00"
        },
        {
          "name": "Post actions/cache@v3",
          "status": "completed",
          "conclusion": "success",
          "number": 16,
          "started_at": "2020-01-20T09:44:39.000-08:00",
          "completed_at": "2020-01-20T09:44:39.000-08:00"
        },
        {
          "name": "Complete job",
          "status": "completed",
          "conclusion": "success",
          "number": 17,
          "started_at": "2020-01-20T09:44:39.000-08:00",
          "completed_at": "2020-01-20T09:44:39.000-08:00"
        }
      ],
      "check_run_url": "https://api.github.com/repos/octo-org/octo-repo/check-runs/399444496",
      "label_filters": [
        "self-hosted",
        "foo",
        "bar"
      ],
      "runner_id": 1,
      "runner_name": "my runner",
      "runner_group_id": 2,
      "runner_group_name": "my runner group",
      "workflow_name": "CI",
      "head_branch": "main"
    }
  ]
}
```

## List jobs for a workflow run
Lists jobs for a workflow run. You can use parameters to narrow the list of results. For more information
about using parameters, seeParameters.
Anyone with read access to the repository can use this endpoint.
OAuth app tokens and personal access tokens (classic) need thereposcope to use this endpoint with a private repository.

### Fine-grained access tokens for "List jobs for a workflow run"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Actions" repository permissions (read)
This endpoint can be used without authentication or the aforementioned permissions if only public resources are requested.

### Parameters for "List jobs for a workflow run"

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
filterstringFilters jobs by theircompleted_attimestamp.latestreturns jobs from the most recent execution of the workflow run.allreturns all jobs for a workflow run, including from old executions of the workflow run.Default:latestCan be one of:latest,all
per_pageintegerThe number of results per page_number (max 100). For more information, see "Using pagination in the REST API."Default:30
pageintegerThe page_number number of the results to fetch. For more information, see "Using pagination in the REST API."Default:1
[/TABLE]
Filters jobs by theircompleted_attimestamp.latestreturns jobs from the most recent execution of the workflow run.allreturns all jobs for a workflow run, including from old executions of the workflow run.
Default:latest
Can be one of:latest,all
The number of results per page_number (max 100). For more information, see "Using pagination in the REST API."
Default:30
The page_number number of the results to fetch. For more information, see "Using pagination in the REST API."
Default:1

### HTTP response status codes for "List jobs for a workflow run"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "List jobs for a workflow run"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/actions/runs/RUN_ID/jobs
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
  "jobs": [
    {
      "id": 399444496,
      "run_id": 29679449,
      "run_url": "https://api.github.com/repos/octo-org/octo-repo/actions/runs/29679449",
      "node_id": "MDEyOldvcmtmbG93IEpvYjM5OTQ0NDQ5Ng==",
      "head_sha": "f83a356604ae3c5d03e1b46ef4d1ca77d64a90b0",
      "url": "https://api.github.com/repos/octo-org/octo-repo/actions/jobs/399444496",
      "html_url": "https://github.com/octo-org/octo-repo/runs/29679449/jobs/399444496",
      "status": "completed",
      "conclusion": "success",
      "started_at": "2020-01-20T17:42:40Z",
      "completed_at": "2020-01-20T17:44:39Z",
      "name": "build",
      "steps": [
        {
          "name": "Set up job",
          "status": "completed",
          "conclusion": "success",
          "number": 1,
          "started_at": "2020-01-20T09:42:40.000-08:00",
          "completed_at": "2020-01-20T09:42:41.000-08:00"
        },
        {
          "name": "Run actions/checkout@v2",
          "status": "completed",
          "conclusion": "success",
          "number": 2,
          "started_at": "2020-01-20T09:42:41.000-08:00",
          "completed_at": "2020-01-20T09:42:45.000-08:00"
        },
        {
          "name": "Set up Ruby",
          "status": "completed",
          "conclusion": "success",
          "number": 3,
          "started_at": "2020-01-20T09:42:45.000-08:00",
          "completed_at": "2020-01-20T09:42:45.000-08:00"
        },
        {
          "name": "Run actions/cache@v3",
          "status": "completed",
          "conclusion": "success",
          "number": 4,
          "started_at": "2020-01-20T09:42:45.000-08:00",
          "completed_at": "2020-01-20T09:42:48.000-08:00"
        },
        {
          "name": "Install Bundler",
          "status": "completed",
          "conclusion": "success",
          "number": 5,
          "started_at": "2020-01-20T09:42:48.000-08:00",
          "completed_at": "2020-01-20T09:42:52.000-08:00"
        },
        {
          "name": "Install Gems",
          "status": "completed",
          "conclusion": "success",
          "number": 6,
          "started_at": "2020-01-20T09:42:52.000-08:00",
          "completed_at": "2020-01-20T09:42:53.000-08:00"
        },
        {
          "name": "Run Tests",
          "status": "completed",
          "conclusion": "success",
          "number": 7,
          "started_at": "2020-01-20T09:42:53.000-08:00",
          "completed_at": "2020-01-20T09:42:59.000-08:00"
        },
        {
          "name": "Deploy to Heroku",
          "status": "completed",
          "conclusion": "success",
          "number": 8,
          "started_at": "2020-01-20T09:42:59.000-08:00",
          "completed_at": "2020-01-20T09:44:39.000-08:00"
        },
        {
          "name": "Post actions/cache@v3",
          "status": "completed",
          "conclusion": "success",
          "number": 16,
          "started_at": "2020-01-20T09:44:39.000-08:00",
          "completed_at": "2020-01-20T09:44:39.000-08:00"
        },
        {
          "name": "Complete job",
          "status": "completed",
          "conclusion": "success",
          "number": 17,
          "started_at": "2020-01-20T09:44:39.000-08:00",
          "completed_at": "2020-01-20T09:44:39.000-08:00"
        }
      ],
      "check_run_url": "https://api.github.com/repos/octo-org/octo-repo/check-runs/399444496",
      "label_filters": [
        "self-hosted",
        "foo",
        "bar"
      ],
      "runner_id": 1,
      "runner_name": "my runner",
      "runner_group_id": 2,
      "runner_group_name": "my runner group",
      "workflow_name": "CI",
      "head_branch": "main"
    }
  ]
}
```