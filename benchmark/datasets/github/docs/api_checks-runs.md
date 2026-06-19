# REST API endpoints for check runs

*Source: https://docs.github.com/en/rest/checks/runs*

---

# REST API endpoints for check runs
Use the REST API to manage check runs.
Note
Write permission for the REST API to interact with checks is only available to GitHub Apps. OAuth apps and authenticated users can view check runs and check suites, but they are not able to create them. If you aren't building a GitHub App, you might be interested in using the REST API to interact withcommit statuses.

## Create a check run
Creates a new check run for a specific commit in a repository.
To create a check run, you must use a GitHub App. OAuth apps and authenticated users are not able to create a check suite.
In a check suite, GitHub limits the number of check runs with the same name to 1000. Once these check runs exceed 1000, GitHub will start to automatically delete older check runs.
Note
The Checks API only looks for pushes in the repository where the check suite or check run were created. Pushes to a branch in a forked repository are not detected and return an emptypull_requestsarray.

### Fine-grained access tokens for "Create a check run"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Checks" repository permissions (write)

### Parameters for "Create a check run"

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
statusRequiredValue:completed
[/TABLE]
Value:completed

### HTTP response status codes for "Create a check run"

[TABLE]
Status code | Description
201 | Created
[/TABLE]
Created

### Code samples for "Create a check run"

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
  https://api.github.com/repos/OWNER/REPO/check-runs \
  -d '{"name":"mighty_readme","head_sha":"ce587453ced02b1526dfb4cb910479d431683101","status":"in_progress","external_id":"42","started_at":"2018-05-04T01:14:52Z","output":{"title":"Mighty Readme report","summary":"","text":""}}'
```

#### Response for in_progress conclusion
- Example response
- Response schema

```
Status: 201
```

```
{
  "id": 4,
  "head_sha": "ce587453ced02b1526dfb4cb910479d431683101",
  "node_id": "MDg6Q2hlY2tSdW40",
  "external_id": "42",
  "url": "https://api.github.com/repos/github/hello-world/check-runs/4",
  "html_url": "https://github.com/github/hello-world/runs/4",
  "details_url": "https://example.com",
  "status": "in_progress",
  "conclusion": null,
  "started_at": "2018-05-04T01:14:52Z",
  "completed_at": null,
  "output": {
    "title": "Mighty Readme report",
    "summary": "There are 0 failures, 2 warnings, and 1 notice.",
    "text": "You may have some misspelled words on lines 2 and 4. You also may want to add a section in your README about how to install your app.",
    "annotations_count": 2,
    "annotations_url": "https://api.github.com/repos/github/hello-world/check-runs/4/annotations"
  },
  "name": "mighty_readme",
  "check_suite": {
    "id": 5
  },
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
  "pull_requests": [
    {
      "url": "https://api.github.com/repos/github/hello-world/pulls/1",
      "id": 1934,
      "number": 3956,
      "head": {
        "ref": "say-hello",
        "sha": "3dca65fa3e8d4b3da3f3d056c59aee1c50f41390",
        "repo": {
          "id": 526,
          "url": "https://api.github.com/repos/github/hello-world",
          "name": "hello-world"
        }
      },
      "base": {
        "ref": "master",
        "sha": "e7fdf7640066d71ad16a86fbcbb9c6a10a18af4f",
        "repo": {
          "id": 526,
          "url": "https://api.github.com/repos/github/hello-world",
          "name": "hello-world"
        }
      }
    }
  ]
}
```

## Get a check run
Gets a single check run using itsid.
Note
The Checks API only looks for pushes in the repository where the check suite or check run were created. Pushes to a branch in a forked repository are not detected and return an emptypull_requestsarray.
OAuth app tokens and personal access tokens (classic) need thereposcope to use this endpoint on a private repository.

### Fine-grained access tokens for "Get a check run"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Checks" repository permissions (read)
This endpoint can be used without authentication or the aforementioned permissions if only public resources are requested.

### Parameters for "Get a check run"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
check_run_idintegerRequiredThe unique identifier of the check run.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.

```
check_run_id
```
The unique identifier of the check run.

### HTTP response status codes for "Get a check run"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "Get a check run"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/check-runs/CHECK_RUN_ID
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "id": 4,
  "head_sha": "ce587453ced02b1526dfb4cb910479d431683101",
  "node_id": "MDg6Q2hlY2tSdW40",
  "external_id": "",
  "url": "https://api.github.com/repos/github/hello-world/check-runs/4",
  "html_url": "https://github.com/github/hello-world/runs/4",
  "details_url": "https://example.com",
  "status": "completed",
  "conclusion": "neutral",
  "started_at": "2018-05-04T01:14:52Z",
  "completed_at": "2018-05-04T01:14:52Z",
  "output": {
    "title": "Mighty Readme report",
    "summary": "There are 0 failures, 2 warnings, and 1 notice.",
    "text": "You may have some misspelled words on lines 2 and 4. You also may want to add a section in your README about how to install your app.",
    "annotations_count": 2,
    "annotations_url": "https://api.github.com/repos/github/hello-world/check-runs/4/annotations"
  },
  "name": "mighty_readme",
  "check_suite": {
    "id": 5
  },
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
  "pull_requests": [
    {
      "url": "https://api.github.com/repos/github/hello-world/pulls/1",
      "id": 1934,
      "number": 3956,
      "head": {
        "ref": "say-hello",
        "sha": "3dca65fa3e8d4b3da3f3d056c59aee1c50f41390",
        "repo": {
          "id": 526,
          "url": "https://api.github.com/repos/github/hello-world",
          "name": "hello-world"
        }
      },
      "base": {
        "ref": "master",
        "sha": "e7fdf7640066d71ad16a86fbcbb9c6a10a18af4f",
        "repo": {
          "id": 526,
          "url": "https://api.github.com/repos/github/hello-world",
          "name": "hello-world"
        }
      }
    }
  ]
}
```

## Update a check run
Updates a check run for a specific commit in a repository.
Note
The endpoints to manage checks only look for pushes in the repository where the check suite or check run were created. Pushes to a branch in a forked repository are not detected and return an emptypull_requestsarray.
OAuth apps and personal access tokens (classic) cannot use this endpoint.

### Fine-grained access tokens for "Update a check run"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Checks" repository permissions (write)

### Parameters for "Update a check run"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
check_run_idintegerRequiredThe unique identifier of the check run.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.

```
check_run_id
```
The unique identifier of the check run.

[TABLE]
Name, Type, Description
namestringThe name of the check. For example, "code-coverage".
details_urlstringThe URL of the integrator's site that has the full details of the check.
external_idstringA reference for the run on the integrator's system.
started_atstringThis is a timestamp inISO 8601format:YYYY-MM-DDTHH:MM:SSZ.
statusstringThe current status of the check run. Only GitHub Actions can set a status ofwaiting,pending, orrequested.Can be one of:queued,in_progress,completed,waiting,requested,pending
conclusionstringRequired if you providecompleted_ator astatusofcompleted. The final conclusion of the check.Note:Providingconclusionwill automatically set thestatusparameter tocompleted. You cannot change a check run conclusion tostale, only GitHub can set this.Can be one of:action_required,cancelled,failure,neutral,success,skipped,stale,timed_out
completed_atstringThe time the check completed. This is a timestamp inISO 8601format:YYYY-MM-DDTHH:MM:SSZ.
outputobjectCheck runs can accept a variety of data in theoutputobject, including atitleandsummaryand can optionally provide descriptive details about the run.
Properties ofoutputName, Type, DescriptiontitlestringRequired.summarystringRequiredCan contain Markdown.textstringCan contain Markdown.annotationsarray of objectsAdds information from your analysis to specific lines of code. Annotations are visible in GitHub's pull request UI. Annotations are visible in GitHub's pull request UI. The Checks API limits the number of annotations to a maximum of 50 per API request. To create more than 50 annotations, you have to make multiple requests to theUpdate a check runendpoint. Each time you update the check run, annotations are appended to the list of annotations that already exist for the check run. GitHub Actions are limited to 10 warning annotations and 10 error annotations per step. For details about annotations in the UI, see "About status checks".Properties ofannotationsName, Type, DescriptionpathstringRequiredThe path of the file to add an annotation to. For example,assets/css/main.css.start_lineintegerRequiredThe start line of the annotation. Line numbers start at 1.end_lineintegerRequiredThe end line of the annotation.start_columnintegerThe start column of the annotation. Annotations only supportstart_columnandend_columnon the same line. Omit this parameter ifstart_lineandend_linehave different values. Column numbers start at 1.end_columnintegerThe end column of the annotation. Annotations only supportstart_columnandend_columnon the same line. Omit this parameter ifstart_lineandend_linehave different values.annotation_levelstringRequiredThe level of the annotation.Can be one of:notice,warning,failuremessagestringRequiredA short description of the feedback for these lines of code. The maximum size is 64 KB.titlestringThe title that represents the annotation. The maximum size is 255 characters.raw_detailsstringDetails about this annotation. The maximum size is 64 KB.imagesarray of objectsAdds images to the output displayed in the GitHub pull request UI.Properties ofimagesName, Type, DescriptionaltstringRequiredThe alternative text for the image.image_urlstringRequiredThe full URL of the image.captionstringA short image description. | Name, Type, Description | titlestringRequired. | summarystringRequiredCan contain Markdown. | textstringCan contain Markdown. | annotationsarray of objectsAdds information from your analysis to specific lines of code. Annotations are visible in GitHub's pull request UI. Annotations are visible in GitHub's pull request UI. The Checks API limits the number of annotations to a maximum of 50 per API request. To create more than 50 annotations, you have to make multiple requests to theUpdate a check runendpoint. Each time you update the check run, annotations are appended to the list of annotations that already exist for the check run. GitHub Actions are limited to 10 warning annotations and 10 error annotations per step. For details about annotations in the UI, see "About status checks". | Properties ofannotationsName, Type, DescriptionpathstringRequiredThe path of the file to add an annotation to. For example,assets/css/main.css.start_lineintegerRequiredThe start line of the annotation. Line numbers start at 1.end_lineintegerRequiredThe end line of the annotation.start_columnintegerThe start column of the annotation. Annotations only supportstart_columnandend_columnon the same line. Omit this parameter ifstart_lineandend_linehave different values. Column numbers start at 1.end_columnintegerThe end column of the annotation. Annotations only supportstart_columnandend_columnon the same line. Omit this parameter ifstart_lineandend_linehave different values.annotation_levelstringRequiredThe level of the annotation.Can be one of:notice,warning,failuremessagestringRequiredA short description of the feedback for these lines of code. The maximum size is 64 KB.titlestringThe title that represents the annotation. The maximum size is 255 characters.raw_detailsstringDetails about this annotation. The maximum size is 64 KB. | Name, Type, Description | pathstringRequiredThe path of the file to add an annotation to. For example,assets/css/main.css. | start_lineintegerRequiredThe start line of the annotation. Line numbers start at 1. | end_lineintegerRequiredThe end line of the annotation. | start_columnintegerThe start column of the annotation. Annotations only supportstart_columnandend_columnon the same line. Omit this parameter ifstart_lineandend_linehave different values. Column numbers start at 1. | end_columnintegerThe end column of the annotation. Annotations only supportstart_columnandend_columnon the same line. Omit this parameter ifstart_lineandend_linehave different values. | annotation_levelstringRequiredThe level of the annotation.Can be one of:notice,warning,failure | messagestringRequiredA short description of the feedback for these lines of code. The maximum size is 64 KB. | titlestringThe title that represents the annotation. The maximum size is 255 characters. | raw_detailsstringDetails about this annotation. The maximum size is 64 KB. | imagesarray of objectsAdds images to the output displayed in the GitHub pull request UI. | Properties ofimagesName, Type, DescriptionaltstringRequiredThe alternative text for the image.image_urlstringRequiredThe full URL of the image.captionstringA short image description. | Name, Type, Description | altstringRequiredThe alternative text for the image. | image_urlstringRequiredThe full URL of the image. | captionstringA short image description.
Name, Type, Description
titlestringRequired.
summarystringRequiredCan contain Markdown.
textstringCan contain Markdown.
annotationsarray of objectsAdds information from your analysis to specific lines of code. Annotations are visible in GitHub's pull request UI. Annotations are visible in GitHub's pull request UI. The Checks API limits the number of annotations to a maximum of 50 per API request. To create more than 50 annotations, you have to make multiple requests to theUpdate a check runendpoint. Each time you update the check run, annotations are appended to the list of annotations that already exist for the check run. GitHub Actions are limited to 10 warning annotations and 10 error annotations per step. For details about annotations in the UI, see "About status checks".
Properties ofannotationsName, Type, DescriptionpathstringRequiredThe path of the file to add an annotation to. For example,assets/css/main.css.start_lineintegerRequiredThe start line of the annotation. Line numbers start at 1.end_lineintegerRequiredThe end line of the annotation.start_columnintegerThe start column of the annotation. Annotations only supportstart_columnandend_columnon the same line. Omit this parameter ifstart_lineandend_linehave different values. Column numbers start at 1.end_columnintegerThe end column of the annotation. Annotations only supportstart_columnandend_columnon the same line. Omit this parameter ifstart_lineandend_linehave different values.annotation_levelstringRequiredThe level of the annotation.Can be one of:notice,warning,failuremessagestringRequiredA short description of the feedback for these lines of code. The maximum size is 64 KB.titlestringThe title that represents the annotation. The maximum size is 255 characters.raw_detailsstringDetails about this annotation. The maximum size is 64 KB. | Name, Type, Description | pathstringRequiredThe path of the file to add an annotation to. For example,assets/css/main.css. | start_lineintegerRequiredThe start line of the annotation. Line numbers start at 1. | end_lineintegerRequiredThe end line of the annotation. | start_columnintegerThe start column of the annotation. Annotations only supportstart_columnandend_columnon the same line. Omit this parameter ifstart_lineandend_linehave different values. Column numbers start at 1. | end_columnintegerThe end column of the annotation. Annotations only supportstart_columnandend_columnon the same line. Omit this parameter ifstart_lineandend_linehave different values. | annotation_levelstringRequiredThe level of the annotation.Can be one of:notice,warning,failure | messagestringRequiredA short description of the feedback for these lines of code. The maximum size is 64 KB. | titlestringThe title that represents the annotation. The maximum size is 255 characters. | raw_detailsstringDetails about this annotation. The maximum size is 64 KB.
Name, Type, Description
pathstringRequiredThe path of the file to add an annotation to. For example,assets/css/main.css.
start_lineintegerRequiredThe start line of the annotation. Line numbers start at 1.
end_lineintegerRequiredThe end line of the annotation.
start_columnintegerThe start column of the annotation. Annotations only supportstart_columnandend_columnon the same line. Omit this parameter ifstart_lineandend_linehave different values. Column numbers start at 1.
end_columnintegerThe end column of the annotation. Annotations only supportstart_columnandend_columnon the same line. Omit this parameter ifstart_lineandend_linehave different values.
annotation_levelstringRequiredThe level of the annotation.Can be one of:notice,warning,failure
messagestringRequiredA short description of the feedback for these lines of code. The maximum size is 64 KB.
titlestringThe title that represents the annotation. The maximum size is 255 characters.
raw_detailsstringDetails about this annotation. The maximum size is 64 KB.
imagesarray of objectsAdds images to the output displayed in the GitHub pull request UI.
Properties ofimagesName, Type, DescriptionaltstringRequiredThe alternative text for the image.image_urlstringRequiredThe full URL of the image.captionstringA short image description. | Name, Type, Description | altstringRequiredThe alternative text for the image. | image_urlstringRequiredThe full URL of the image. | captionstringA short image description.
Name, Type, Description
altstringRequiredThe alternative text for the image.
image_urlstringRequiredThe full URL of the image.
captionstringA short image description.
actionsarray of objectsPossible further actions the integrator can perform, which a user may trigger. Each action includes alabel,identifieranddescription. A maximum of three actions are accepted. To learn more about check runs and requested actions, see "Check runs and requested actions."
Properties ofactionsName, Type, DescriptionlabelstringRequiredThe text to be displayed on a button in the web UI. The maximum size is 20 characters.descriptionstringRequiredA short explanation of what this action would do. The maximum size is 40 characters.identifierstringRequiredA reference for the action on the integrator's system. The maximum size is 20 characters. | Name, Type, Description | labelstringRequiredThe text to be displayed on a button in the web UI. The maximum size is 20 characters. | descriptionstringRequiredA short explanation of what this action would do. The maximum size is 40 characters. | identifierstringRequiredA reference for the action on the integrator's system. The maximum size is 20 characters.
Name, Type, Description
labelstringRequiredThe text to be displayed on a button in the web UI. The maximum size is 20 characters.
descriptionstringRequiredA short explanation of what this action would do. The maximum size is 40 characters.
identifierstringRequiredA reference for the action on the integrator's system. The maximum size is 20 characters.
[/TABLE]
The name of the check. For example, "code-coverage".

```
details_url
```
The URL of the integrator's site that has the full details of the check.

```
external_id
```
A reference for the run on the integrator's system.
This is a timestamp inISO 8601format:YYYY-MM-DDTHH:MM:SSZ.
The current status of the check run. Only GitHub Actions can set a status ofwaiting,pending, orrequested.
Can be one of:queued,in_progress,completed,waiting,requested,pending

```
in_progress
```
Required if you providecompleted_ator astatusofcompleted. The final conclusion of the check.Note:Providingconclusionwill automatically set thestatusparameter tocompleted. You cannot change a check run conclusion tostale, only GitHub can set this.

```
completed_at
```
Can be one of:action_required,cancelled,failure,neutral,success,skipped,stale,timed_out

```
action_required
```

```
completed_at
```
The time the check completed. This is a timestamp inISO 8601format:YYYY-MM-DDTHH:MM:SSZ.
Check runs can accept a variety of data in theoutputobject, including atitleandsummaryand can optionally provide descriptive details about the run.

[TABLE]
Name, Type, Description
titlestringRequired.
summarystringRequiredCan contain Markdown.
textstringCan contain Markdown.
annotationsarray of objectsAdds information from your analysis to specific lines of code. Annotations are visible in GitHub's pull request UI. Annotations are visible in GitHub's pull request UI. The Checks API limits the number of annotations to a maximum of 50 per API request. To create more than 50 annotations, you have to make multiple requests to theUpdate a check runendpoint. Each time you update the check run, annotations are appended to the list of annotations that already exist for the check run. GitHub Actions are limited to 10 warning annotations and 10 error annotations per step. For details about annotations in the UI, see "About status checks".
Properties ofannotationsName, Type, DescriptionpathstringRequiredThe path of the file to add an annotation to. For example,assets/css/main.css.start_lineintegerRequiredThe start line of the annotation. Line numbers start at 1.end_lineintegerRequiredThe end line of the annotation.start_columnintegerThe start column of the annotation. Annotations only supportstart_columnandend_columnon the same line. Omit this parameter ifstart_lineandend_linehave different values. Column numbers start at 1.end_columnintegerThe end column of the annotation. Annotations only supportstart_columnandend_columnon the same line. Omit this parameter ifstart_lineandend_linehave different values.annotation_levelstringRequiredThe level of the annotation.Can be one of:notice,warning,failuremessagestringRequiredA short description of the feedback for these lines of code. The maximum size is 64 KB.titlestringThe title that represents the annotation. The maximum size is 255 characters.raw_detailsstringDetails about this annotation. The maximum size is 64 KB. | Name, Type, Description | pathstringRequiredThe path of the file to add an annotation to. For example,assets/css/main.css. | start_lineintegerRequiredThe start line of the annotation. Line numbers start at 1. | end_lineintegerRequiredThe end line of the annotation. | start_columnintegerThe start column of the annotation. Annotations only supportstart_columnandend_columnon the same line. Omit this parameter ifstart_lineandend_linehave different values. Column numbers start at 1. | end_columnintegerThe end column of the annotation. Annotations only supportstart_columnandend_columnon the same line. Omit this parameter ifstart_lineandend_linehave different values. | annotation_levelstringRequiredThe level of the annotation.Can be one of:notice,warning,failure | messagestringRequiredA short description of the feedback for these lines of code. The maximum size is 64 KB. | titlestringThe title that represents the annotation. The maximum size is 255 characters. | raw_detailsstringDetails about this annotation. The maximum size is 64 KB.
Name, Type, Description
pathstringRequiredThe path of the file to add an annotation to. For example,assets/css/main.css.
start_lineintegerRequiredThe start line of the annotation. Line numbers start at 1.
end_lineintegerRequiredThe end line of the annotation.
start_columnintegerThe start column of the annotation. Annotations only supportstart_columnandend_columnon the same line. Omit this parameter ifstart_lineandend_linehave different values. Column numbers start at 1.
end_columnintegerThe end column of the annotation. Annotations only supportstart_columnandend_columnon the same line. Omit this parameter ifstart_lineandend_linehave different values.
annotation_levelstringRequiredThe level of the annotation.Can be one of:notice,warning,failure
messagestringRequiredA short description of the feedback for these lines of code. The maximum size is 64 KB.
titlestringThe title that represents the annotation. The maximum size is 255 characters.
raw_detailsstringDetails about this annotation. The maximum size is 64 KB.
imagesarray of objectsAdds images to the output displayed in the GitHub pull request UI.
Properties ofimagesName, Type, DescriptionaltstringRequiredThe alternative text for the image.image_urlstringRequiredThe full URL of the image.captionstringA short image description. | Name, Type, Description | altstringRequiredThe alternative text for the image. | image_urlstringRequiredThe full URL of the image. | captionstringA short image description.
Name, Type, Description
altstringRequiredThe alternative text for the image.
image_urlstringRequiredThe full URL of the image.
captionstringA short image description.
[/TABLE]
Required.
Can contain Markdown.
Can contain Markdown.

```
annotations
```
Adds information from your analysis to specific lines of code. Annotations are visible in GitHub's pull request UI. Annotations are visible in GitHub's pull request UI. The Checks API limits the number of annotations to a maximum of 50 per API request. To create more than 50 annotations, you have to make multiple requests to theUpdate a check runendpoint. Each time you update the check run, annotations are appended to the list of annotations that already exist for the check run. GitHub Actions are limited to 10 warning annotations and 10 error annotations per step. For details about annotations in the UI, see "About status checks".

```
annotations
```

[TABLE]
Name, Type, Description
pathstringRequiredThe path of the file to add an annotation to. For example,assets/css/main.css.
start_lineintegerRequiredThe start line of the annotation. Line numbers start at 1.
end_lineintegerRequiredThe end line of the annotation.
start_columnintegerThe start column of the annotation. Annotations only supportstart_columnandend_columnon the same line. Omit this parameter ifstart_lineandend_linehave different values. Column numbers start at 1.
end_columnintegerThe end column of the annotation. Annotations only supportstart_columnandend_columnon the same line. Omit this parameter ifstart_lineandend_linehave different values.
annotation_levelstringRequiredThe level of the annotation.Can be one of:notice,warning,failure
messagestringRequiredA short description of the feedback for these lines of code. The maximum size is 64 KB.
titlestringThe title that represents the annotation. The maximum size is 255 characters.
raw_detailsstringDetails about this annotation. The maximum size is 64 KB.
[/TABLE]
The path of the file to add an annotation to. For example,assets/css/main.css.
The start line of the annotation. Line numbers start at 1.
The end line of the annotation.

```
start_column
```
The start column of the annotation. Annotations only supportstart_columnandend_columnon the same line. Omit this parameter ifstart_lineandend_linehave different values. Column numbers start at 1.
The end column of the annotation. Annotations only supportstart_columnandend_columnon the same line. Omit this parameter ifstart_lineandend_linehave different values.

```
annotation_level
```
The level of the annotation.
Can be one of:notice,warning,failure
A short description of the feedback for these lines of code. The maximum size is 64 KB.
The title that represents the annotation. The maximum size is 255 characters.

```
raw_details
```
Details about this annotation. The maximum size is 64 KB.
Adds images to the output displayed in the GitHub pull request UI.

[TABLE]
Name, Type, Description
altstringRequiredThe alternative text for the image.
image_urlstringRequiredThe full URL of the image.
captionstringA short image description.
[/TABLE]
The alternative text for the image.
The full URL of the image.
A short image description.
Possible further actions the integrator can perform, which a user may trigger. Each action includes alabel,identifieranddescription. A maximum of three actions are accepted. To learn more about check runs and requested actions, see "Check runs and requested actions."

[TABLE]
Name, Type, Description
labelstringRequiredThe text to be displayed on a button in the web UI. The maximum size is 20 characters.
descriptionstringRequiredA short explanation of what this action would do. The maximum size is 40 characters.
identifierstringRequiredA reference for the action on the integrator's system. The maximum size is 20 characters.
[/TABLE]
The text to be displayed on a button in the web UI. The maximum size is 20 characters.

```
description
```
A short explanation of what this action would do. The maximum size is 40 characters.
A reference for the action on the integrator's system. The maximum size is 20 characters.

### HTTP response status codes for "Update a check run"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "Update a check run"

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
  https://api.github.com/repos/OWNER/REPO/check-runs/CHECK_RUN_ID \
  -d '{"name":"mighty_readme","started_at":"2018-05-04T01:14:52Z","status":"completed","conclusion":"success","completed_at":"2018-05-04T01:14:52Z","output":{"title":"Mighty Readme report","summary":"There are 0 failures, 2 warnings, and 1 notices.","text":"You may have some misspelled words on lines 2 and 4. You also may want to add a section in your README about how to install your app.","annotations":[{"path":"README.md","annotation_level":"warning","title":"Spell Checker","message":"Check your spelling for '\''banaas'\''.","raw_details":"Do you mean '\''bananas'\'' or '\''banana'\''?","start_line":2,"end_line":2},{"path":"README.md","annotation_level":"warning","title":"Spell Checker","message":"Check your spelling for '\''aples'\''","raw_details":"Do you mean '\''apples'\'' or '\''Naples'\''","start_line":4,"end_line":4}],"images":[{"alt":"Super bananas","image_url":"http://example.com/images/42"}]}}'
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "id": 4,
  "head_sha": "ce587453ced02b1526dfb4cb910479d431683101",
  "node_id": "MDg6Q2hlY2tSdW40",
  "external_id": "",
  "url": "https://api.github.com/repos/github/hello-world/check-runs/4",
  "html_url": "https://github.com/github/hello-world/runs/4",
  "details_url": "https://example.com",
  "status": "completed",
  "conclusion": "neutral",
  "started_at": "2018-05-04T01:14:52Z",
  "completed_at": "2018-05-04T01:14:52Z",
  "output": {
    "title": "Mighty Readme report",
    "summary": "There are 0 failures, 2 warnings, and 1 notice.",
    "text": "You may have some misspelled words on lines 2 and 4. You also may want to add a section in your README about how to install your app.",
    "annotations_count": 2,
    "annotations_url": "https://api.github.com/repos/github/hello-world/check-runs/4/annotations"
  },
  "name": "mighty_readme",
  "check_suite": {
    "id": 5
  },
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
  "pull_requests": [
    {
      "url": "https://api.github.com/repos/github/hello-world/pulls/1",
      "id": 1934,
      "number": 3956,
      "head": {
        "ref": "say-hello",
        "sha": "3dca65fa3e8d4b3da3f3d056c59aee1c50f41390",
        "repo": {
          "id": 526,
          "url": "https://api.github.com/repos/github/hello-world",
          "name": "hello-world"
        }
      },
      "base": {
        "ref": "master",
        "sha": "e7fdf7640066d71ad16a86fbcbb9c6a10a18af4f",
        "repo": {
          "id": 526,
          "url": "https://api.github.com/repos/github/hello-world",
          "name": "hello-world"
        }
      }
    }
  ]
}
```

## List check run annotations
Lists annotations for a check run using the annotationid.
OAuth app tokens and personal access tokens (classic) need thereposcope to use this endpoint on a private repository.

### Fine-grained access tokens for "List check run annotations"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Checks" repository permissions (read)
This endpoint can be used without authentication or the aforementioned permissions if only public resources are requested.

### Parameters for "List check run annotations"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
check_run_idintegerRequiredThe unique identifier of the check run.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.

```
check_run_id
```
The unique identifier of the check run.

[TABLE]
Name, Type, Description
per_pageintegerThe number of results per page (max 100). For more information, see "Using pagination in the REST API."Default:30
pageintegerThe page number of the results to fetch. For more information, see "Using pagination in the REST API."Default:1
[/TABLE]
The number of results per page (max 100). For more information, see "Using pagination in the REST API."
Default:30
The page number of the results to fetch. For more information, see "Using pagination in the REST API."
Default:1

### HTTP response status codes for "List check run annotations"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "List check run annotations"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/check-runs/CHECK_RUN_ID/annotations
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
    "path": "README.md",
    "start_line": 2,
    "end_line": 2,
    "start_column": 5,
    "end_column": 10,
    "annotation_level": "warning",
    "title": "Spell Checker",
    "message": "Check your spelling for 'banaas'.",
    "raw_details": "Do you mean 'bananas' or 'banana'?",
    "blob_href": "https://api.github.com/repos/github/rest-api-description/git/blobs/abc"
  }
]
```

## Rerequest a check run
Triggers GitHub to rerequest an existing check run, without pushing new code to a repository. This endpoint will trigger thecheck_runwebhookevent with the actionrerequested. When a check run isrerequested, thestatusof the check suite it belongs to is reset toqueuedand theconclusionis cleared. The check run itself is not updated. GitHub apps recieving thecheck_runwebhookwith thererequestedaction should then decide if the check run should be reset or updated and call theupdatecheck_runendpointto update the check_run if desired.
For more information about how to re-run GitHub Actions jobs, see "Re-run a job from a workflow run".

### Fine-grained access tokens for "Rerequest a check run"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Checks" repository permissions (write)

### Parameters for "Rerequest a check run"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
check_run_idintegerRequiredThe unique identifier of the check run.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.

```
check_run_id
```
The unique identifier of the check run.

### HTTP response status codes for "Rerequest a check run"

[TABLE]
Status code | Description
201 | Created
403 | Forbidden if the check run is not rerequestable or doesn't belong to the authenticated GitHub App
404 | Resource not found
422 | Validation error if the check run is not rerequestable
[/TABLE]
Created
Forbidden if the check run is not rerequestable or doesn't belong to the authenticated GitHub App
Resource not found
Validation error if the check run is not rerequestable

### Code samples for "Rerequest a check run"

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
  https://api.github.com/repos/OWNER/REPO/check-runs/CHECK_RUN_ID/rerequest
```

#### Response
- Example response
- Response schema

```
Status: 201
```

## List check runs in a check suite
Lists check runs for a check suite using itsid.
Note
The endpoints to manage checks only look for pushes in the repository where the check suite or check run were created. Pushes to a branch in a forked repository are not detected and return an emptypull_requestsarray.
OAuth app tokens and personal access tokens (classic) need thereposcope to use this endpoint on a private repository.

### Fine-grained access tokens for "List check runs in a check suite"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Checks" repository permissions (read)
This endpoint can be used without authentication or the aforementioned permissions if only public resources are requested.

### Parameters for "List check runs in a check suite"

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

[TABLE]
Name, Type, Description
check_namestringReturns check runs with the specifiedname.
statusstringReturns check runs with the specifiedstatus.Can be one of:queued,in_progress,completed
filterstringFilters check runs by theircompleted_attimestamp.latestreturns the most recent check runs.Default:latestCan be one of:latest,all
per_pageintegerThe number of results per page (max 100). For more information, see "Using pagination in the REST API."Default:30
pageintegerThe page number of the results to fetch. For more information, see "Using pagination in the REST API."Default:1
[/TABLE]
Returns check runs with the specifiedname.
Returns check runs with the specifiedstatus.
Can be one of:queued,in_progress,completed

```
in_progress
```
Filters check runs by theircompleted_attimestamp.latestreturns the most recent check runs.
Default:latest
Can be one of:latest,all
The number of results per page (max 100). For more information, see "Using pagination in the REST API."
Default:30
The page number of the results to fetch. For more information, see "Using pagination in the REST API."
Default:1

### HTTP response status codes for "List check runs in a check suite"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "List check runs in a check suite"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/check-suites/CHECK_SUITE_ID/check-runs
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
  "check_runs": [
    {
      "id": 4,
      "head_sha": "ce587453ced02b1526dfb4cb910479d431683101",
      "node_id": "MDg6Q2hlY2tSdW40",
      "external_id": "",
      "url": "https://api.github.com/repos/github/hello-world/check-runs/4",
      "html_url": "https://github.com/github/hello-world/runs/4",
      "details_url": "https://example.com",
      "status": "completed",
      "conclusion": "neutral",
      "started_at": "2018-05-04T01:14:52Z",
      "completed_at": "2018-05-04T01:14:52Z",
      "output": {
        "title": "Mighty Readme report",
        "summary": "There are 0 failures, 2 warnings, and 1 notice.",
        "text": "You may have some misspelled words on lines 2 and 4. You also may want to add a section in your README about how to install your app.",
        "annotations_count": 2,
        "annotations_url": "https://api.github.com/repos/github/hello-world/check-runs/4/annotations"
      },
      "name": "mighty_readme",
      "check_suite": {
        "id": 5
      },
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
      "pull_requests": [
        {
          "url": "https://api.github.com/repos/github/hello-world/pulls/1",
          "id": 1934,
          "number": 3956,
          "head": {
            "ref": "say-hello",
            "sha": "3dca65fa3e8d4b3da3f3d056c59aee1c50f41390",
            "repo": {
              "id": 526,
              "url": "https://api.github.com/repos/github/hello-world",
              "name": "hello-world"
            }
          },
          "base": {
            "ref": "master",
            "sha": "e7fdf7640066d71ad16a86fbcbb9c6a10a18af4f",
            "repo": {
              "id": 526,
              "url": "https://api.github.com/repos/github/hello-world",
              "name": "hello-world"
            }
          }
        }
      ]
    }
  ]
}
```

## List check runs for a Git reference
Lists check runs for a commit ref. Therefcan be a SHA, branch name, or a tag name.
Note
The endpoints to manage checks only look for pushes in the repository where the check suite or check run were created. Pushes to a branch in a forked repository are not detected and return an emptypull_requestsarray.
If there are more than 1000 check suites on a single git reference, this endpoint will limit check runs to the 1000 most recent check suites. To iterate over all possible check runs, use theList check suites for a Git referenceendpoint and provide thecheck_suite_idparameter to theList check runs in a check suiteendpoint.
OAuth app tokens and personal access tokens (classic) need thereposcope to use this endpoint on a private repository.

### Fine-grained access tokens for "List check runs for a Git reference"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Checks" repository permissions (read)
This endpoint can be used without authentication or the aforementioned permissions if only public resources are requested.

### Parameters for "List check runs for a Git reference"

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
check_namestringReturns check runs with the specifiedname.
statusstringReturns check runs with the specifiedstatus.Can be one of:queued,in_progress,completed
filterstringFilters check runs by theircompleted_attimestamp.latestreturns the most recent check runs.Default:latestCan be one of:latest,all
per_pageintegerThe number of results per page (max 100). For more information, see "Using pagination in the REST API."Default:30
pageintegerThe page number of the results to fetch. For more information, see "Using pagination in the REST API."Default:1
app_idinteger
[/TABLE]
Returns check runs with the specifiedname.
Returns check runs with the specifiedstatus.
Can be one of:queued,in_progress,completed

```
in_progress
```
Filters check runs by theircompleted_attimestamp.latestreturns the most recent check runs.
Default:latest
Can be one of:latest,all
The number of results per page (max 100). For more information, see "Using pagination in the REST API."
Default:30
The page number of the results to fetch. For more information, see "Using pagination in the REST API."
Default:1

### HTTP response status codes for "List check runs for a Git reference"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "List check runs for a Git reference"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/commits/REF/check-runs
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
  "check_runs": [
    {
      "id": 4,
      "head_sha": "ce587453ced02b1526dfb4cb910479d431683101",
      "node_id": "MDg6Q2hlY2tSdW40",
      "external_id": "",
      "url": "https://api.github.com/repos/github/hello-world/check-runs/4",
      "html_url": "https://github.com/github/hello-world/runs/4",
      "details_url": "https://example.com",
      "status": "completed",
      "conclusion": "neutral",
      "started_at": "2018-05-04T01:14:52Z",
      "completed_at": "2018-05-04T01:14:52Z",
      "output": {
        "title": "Mighty Readme report",
        "summary": "There are 0 failures, 2 warnings, and 1 notice.",
        "text": "You may have some misspelled words on lines 2 and 4. You also may want to add a section in your README about how to install your app.",
        "annotations_count": 2,
        "annotations_url": "https://api.github.com/repos/github/hello-world/check-runs/4/annotations"
      },
      "name": "mighty_readme",
      "check_suite": {
        "id": 5
      },
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
      "pull_requests": [
        {
          "url": "https://api.github.com/repos/github/hello-world/pulls/1",
          "id": 1934,
          "number": 3956,
          "head": {
            "ref": "say-hello",
            "sha": "3dca65fa3e8d4b3da3f3d056c59aee1c50f41390",
            "repo": {
              "id": 526,
              "url": "https://api.github.com/repos/github/hello-world",
              "name": "hello-world"
            }
          },
          "base": {
            "ref": "master",
            "sha": "e7fdf7640066d71ad16a86fbcbb9c6a10a18af4f",
            "repo": {
              "id": 526,
              "url": "https://api.github.com/repos/github/hello-world",
              "name": "hello-world"
            }
          }
        }
      ]
    }
  ]
}
```