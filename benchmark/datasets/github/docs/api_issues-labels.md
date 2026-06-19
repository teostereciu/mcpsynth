# REST API endpoints for labels

*Source: https://docs.github.com/en/rest/issues/labels*

---

# REST API endpoints for labels
Use the REST API to manage labels for repositories, issues and pull requests.

## About labels
You can use the REST API to manage labels for a repository and add or remove labels to issues and pull requests. Every pull request is an issue, but not every issue is a pull request. For this reason, "shared" actions for both features, like managing assignees, labels, and milestones, are provided within the Issues endpoints.

## List labels for an issue
Lists all labels for an issue.

### Fine-grained access tokens for "List labels for an issue"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have at least one of the following permission sets:
- "Issues" repository permissions (read)
- "Pull requests" repository permissions (read)
This endpoint can be used without authentication or the aforementioned permissions if only public resources are requested.

### Parameters for "List labels for an issue"

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
per_pageintegerThe number of results per page (max 100). For more information, see "Using pagination in the REST API."Default:30
pageintegerThe page number of the results to fetch. For more information, see "Using pagination in the REST API."Default:1
[/TABLE]
The number of results per page (max 100). For more information, see "Using pagination in the REST API."
Default:30
The page number of the results to fetch. For more information, see "Using pagination in the REST API."
Default:1

### HTTP response status codes for "List labels for an issue"

[TABLE]
Status code | Description
200 | OK
301 | Moved permanently
404 | Resource not found
410 | Gone
[/TABLE]
OK
Moved permanently
Resource not found
Gone

### Code samples for "List labels for an issue"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/issues/ISSUE_NUMBER/labels
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
    "id": 208045946,
    "node_id": "MDU6TGFiZWwyMDgwNDU5NDY=",
    "url": "https://api.github.com/repos/octocat/Hello-World/labels/bug",
    "name": "bug",
    "description": "Something isn't working",
    "color": "f29513",
    "default": true
  },
  {
    "id": 208045947,
    "node_id": "MDU6TGFiZWwyMDgwNDU5NDc=",
    "url": "https://api.github.com/repos/octocat/Hello-World/labels/enhancement",
    "name": "enhancement",
    "description": "New feature or request",
    "color": "a2eeef",
    "default": false
  }
]
```

## Add labels to an issue
Adds labels to an issue.

### Fine-grained access tokens for "Add labels to an issue"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have at least one of the following permission sets:
- "Issues" repository permissions (write)
- "Pull requests" repository permissions (write)

### Parameters for "Add labels to an issue"

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
labelsarray of stringsThe names of the labels to add to the issue's existing labels. You can also pass anarrayof labels directly, but GitHub recommends passing an object with thelabelskey. To replace all of the labels for an issue, use "Set labels for an issue."
[/TABLE]
The names of the labels to add to the issue's existing labels. You can also pass anarrayof labels directly, but GitHub recommends passing an object with thelabelskey. To replace all of the labels for an issue, use "Set labels for an issue."

### HTTP response status codes for "Add labels to an issue"

[TABLE]
Status code | Description
200 | OK
301 | Moved permanently
404 | Resource not found
410 | Gone
422 | Validation failed, or the endpoint has been spammed.
[/TABLE]
OK
Moved permanently
Resource not found
Gone
Validation failed, or the endpoint has been spammed.

### Code samples for "Add labels to an issue"

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
  https://api.github.com/repos/OWNER/REPO/issues/ISSUE_NUMBER/labels \
  -d '{"labels":["bug","enhancement"]}'
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
    "id": 208045946,
    "node_id": "MDU6TGFiZWwyMDgwNDU5NDY=",
    "url": "https://api.github.com/repos/octocat/Hello-World/labels/bug",
    "name": "bug",
    "description": "Something isn't working",
    "color": "f29513",
    "default": true
  },
  {
    "id": 208045947,
    "node_id": "MDU6TGFiZWwyMDgwNDU5NDc=",
    "url": "https://api.github.com/repos/octocat/Hello-World/labels/enhancement",
    "name": "enhancement",
    "description": "New feature or request",
    "color": "a2eeef",
    "default": false
  }
]
```

## Set labels for an issue
Removes any previous labels and sets the new labels for an issue.

### Fine-grained access tokens for "Set labels for an issue"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have at least one of the following permission sets:
- "Issues" repository permissions (write)
- "Pull requests" repository permissions (write)

### Parameters for "Set labels for an issue"

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
labelsarray of stringsThe names of the labels to set for the issue. The labels you set replace any existing labels. You can pass an empty array to remove all labels. Alternatively, you can pass a single label as astringor anarrayof labels directly, but GitHub recommends passing an object with thelabelskey. You can also add labels to the existing labels for an issue. For more information, see "Add labels to an issue."
[/TABLE]
The names of the labels to set for the issue. The labels you set replace any existing labels. You can pass an empty array to remove all labels. Alternatively, you can pass a single label as astringor anarrayof labels directly, but GitHub recommends passing an object with thelabelskey. You can also add labels to the existing labels for an issue. For more information, see "Add labels to an issue."

### HTTP response status codes for "Set labels for an issue"

[TABLE]
Status code | Description
200 | OK
301 | Moved permanently
404 | Resource not found
410 | Gone
422 | Validation failed, or the endpoint has been spammed.
[/TABLE]
OK
Moved permanently
Resource not found
Gone
Validation failed, or the endpoint has been spammed.

### Code samples for "Set labels for an issue"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -X PUT \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/issues/ISSUE_NUMBER/labels \
  -d '{"labels":["bug","enhancement"]}'
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
    "id": 208045946,
    "node_id": "MDU6TGFiZWwyMDgwNDU5NDY=",
    "url": "https://api.github.com/repos/octocat/Hello-World/labels/bug",
    "name": "bug",
    "description": "Something isn't working",
    "color": "f29513",
    "default": true
  },
  {
    "id": 208045947,
    "node_id": "MDU6TGFiZWwyMDgwNDU5NDc=",
    "url": "https://api.github.com/repos/octocat/Hello-World/labels/enhancement",
    "name": "enhancement",
    "description": "New feature or request",
    "color": "a2eeef",
    "default": false
  }
]
```

## Remove all labels from an issue
Removes all labels from an issue.

### Fine-grained access tokens for "Remove all labels from an issue"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have at least one of the following permission sets:
- "Issues" repository permissions (write)
- "Pull requests" repository permissions (write)

### Parameters for "Remove all labels from an issue"

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

### HTTP response status codes for "Remove all labels from an issue"

[TABLE]
Status code | Description
204 | No Content
301 | Moved permanently
404 | Resource not found
410 | Gone
[/TABLE]
No Content
Moved permanently
Resource not found
Gone

### Code samples for "Remove all labels from an issue"

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
  https://api.github.com/repos/OWNER/REPO/issues/ISSUE_NUMBER/labels
```

#### Response

```
Status: 204
```

## Remove a label from an issue
Removes the specified label from the issue, and returns the remaining labels on the issue. This endpoint returns a404 Not Foundstatus if the label does not exist.

### Fine-grained access tokens for "Remove a label from an issue"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have at least one of the following permission sets:
- "Issues" repository permissions (write)
- "Pull requests" repository permissions (write)

### Parameters for "Remove a label from an issue"

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
namestringRequired
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.

```
issue_number
```
The number that identifies the issue.

### HTTP response status codes for "Remove a label from an issue"

[TABLE]
Status code | Description
200 | OK
301 | Moved permanently
404 | Resource not found
410 | Gone
[/TABLE]
OK
Moved permanently
Resource not found
Gone

### Code samples for "Remove a label from an issue"

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
  https://api.github.com/repos/OWNER/REPO/issues/ISSUE_NUMBER/labels/NAME
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
    "id": 208045946,
    "node_id": "MDU6TGFiZWwyMDgwNDU5NDY=",
    "url": "https://api.github.com/repos/octocat/Hello-World/labels/bug",
    "name": "bug",
    "description": "Something isn't working",
    "color": "f29513",
    "default": true
  }
]
```

## List labels for a repository
Lists all labels for a repository.

### Fine-grained access tokens for "List labels for a repository"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have at least one of the following permission sets:
- "Issues" repository permissions (read)
- "Pull requests" repository permissions (read)
This endpoint can be used without authentication or the aforementioned permissions if only public resources are requested.

### Parameters for "List labels for a repository"

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
per_pageintegerThe number of results per page (max 100). For more information, see "Using pagination in the REST API."Default:30
pageintegerThe page number of the results to fetch. For more information, see "Using pagination in the REST API."Default:1
[/TABLE]
The number of results per page (max 100). For more information, see "Using pagination in the REST API."
Default:30
The page number of the results to fetch. For more information, see "Using pagination in the REST API."
Default:1

### HTTP response status codes for "List labels for a repository"

[TABLE]
Status code | Description
200 | OK
404 | Resource not found
[/TABLE]
OK
Resource not found

### Code samples for "List labels for a repository"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/labels
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
    "id": 208045946,
    "node_id": "MDU6TGFiZWwyMDgwNDU5NDY=",
    "url": "https://api.github.com/repos/octocat/Hello-World/labels/bug",
    "name": "bug",
    "description": "Something isn't working",
    "color": "f29513",
    "default": true
  },
  {
    "id": 208045947,
    "node_id": "MDU6TGFiZWwyMDgwNDU5NDc=",
    "url": "https://api.github.com/repos/octocat/Hello-World/labels/enhancement",
    "name": "enhancement",
    "description": "New feature or request",
    "color": "a2eeef",
    "default": false
  }
]
```

## Create a label
Creates a label for the specified repository with the given name and color. The name and color parameters are required. The color must be a validhexadecimal color code.

### Fine-grained access tokens for "Create a label"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have at least one of the following permission sets:
- "Issues" repository permissions (write)
- "Pull requests" repository permissions (write)

### Parameters for "Create a label"

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
namestringRequiredThe name of the label. Emoji can be added to label names, using either native emoji or colon-style markup. For example, typing:strawberry:will render the emoji. For a full list of available emoji and codes, see "Emoji cheat sheet."
colorstringThehexadecimal color codefor the label, without the leading#.
descriptionstringA short description of the label. Must be 100 characters or fewer.
[/TABLE]
The name of the label. Emoji can be added to label names, using either native emoji or colon-style markup. For example, typing:strawberry:will render the emoji. For a full list of available emoji and codes, see "Emoji cheat sheet."
Thehexadecimal color codefor the label, without the leading#.

```
description
```
A short description of the label. Must be 100 characters or fewer.

### HTTP response status codes for "Create a label"

[TABLE]
Status code | Description
201 | Created
404 | Resource not found
422 | Validation failed, or the endpoint has been spammed.
[/TABLE]
Created
Resource not found
Validation failed, or the endpoint has been spammed.

### Code samples for "Create a label"

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
  https://api.github.com/repos/OWNER/REPO/labels \
  -d '{"name":"bug","description":"Something isn'\''t working","color":"f29513"}'
```

#### Response
- Example response
- Response schema

```
Status: 201
```

```
{
  "id": 208045946,
  "node_id": "MDU6TGFiZWwyMDgwNDU5NDY=",
  "url": "https://api.github.com/repos/octocat/Hello-World/labels/bug",
  "name": "bug",
  "description": "Something isn't working",
  "color": "f29513",
  "default": true
}
```

## Get a label
Gets a label using the given name.

### Fine-grained access tokens for "Get a label"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have at least one of the following permission sets:
- "Issues" repository permissions (read)
- "Pull requests" repository permissions (read)
This endpoint can be used without authentication or the aforementioned permissions if only public resources are requested.

### Parameters for "Get a label"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
namestringRequired
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.

### HTTP response status codes for "Get a label"

[TABLE]
Status code | Description
200 | OK
404 | Resource not found
[/TABLE]
OK
Resource not found

### Code samples for "Get a label"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/labels/NAME
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "id": 208045946,
  "node_id": "MDU6TGFiZWwyMDgwNDU5NDY=",
  "url": "https://api.github.com/repos/octocat/Hello-World/labels/bug",
  "name": "bug",
  "description": "Something isn't working",
  "color": "f29513",
  "default": true
}
```

## Update a label
Updates a label using the given label name.

### Fine-grained access tokens for "Update a label"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have at least one of the following permission sets:
- "Issues" repository permissions (write)
- "Pull requests" repository permissions (write)

### Parameters for "Update a label"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
namestringRequired
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.

[TABLE]
Name, Type, Description
new_namestringThe new name of the label. Emoji can be added to label names, using either native emoji or colon-style markup. For example, typing:strawberry:will render the emoji. For a full list of available emoji and codes, see "Emoji cheat sheet."
colorstringThehexadecimal color codefor the label, without the leading#.
descriptionstringA short description of the label. Must be 100 characters or fewer.
[/TABLE]
The new name of the label. Emoji can be added to label names, using either native emoji or colon-style markup. For example, typing:strawberry:will render the emoji. For a full list of available emoji and codes, see "Emoji cheat sheet."
Thehexadecimal color codefor the label, without the leading#.

```
description
```
A short description of the label. Must be 100 characters or fewer.

### HTTP response status codes for "Update a label"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "Update a label"

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
  https://api.github.com/repos/OWNER/REPO/labels/NAME \
  -d '{"new_name":"bug :bug:","description":"Small bug fix required","color":"b01f26"}'
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "id": 208045946,
  "node_id": "MDU6TGFiZWwyMDgwNDU5NDY=",
  "url": "https://api.github.com/repos/octocat/Hello-World/labels/bug%20:bug:",
  "name": "bug :bug:",
  "description": "Small bug fix required",
  "color": "b01f26",
  "default": true
}
```

## Delete a label
Deletes a label using the given label name.

### Fine-grained access tokens for "Delete a label"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have at least one of the following permission sets:
- "Issues" repository permissions (write)
- "Pull requests" repository permissions (write)

### Parameters for "Delete a label"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
namestringRequired
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.

### HTTP response status codes for "Delete a label"

[TABLE]
Status code | Description
204 | No Content
[/TABLE]
No Content

### Code samples for "Delete a label"

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
  https://api.github.com/repos/OWNER/REPO/labels/NAME
```

#### Response

```
Status: 204
```

## List labels for issues in a milestone
Lists labels for issues in a milestone.

### Fine-grained access tokens for "List labels for issues in a milestone"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have at least one of the following permission sets:
- "Issues" repository permissions (read)
- "Pull requests" repository permissions (read)
This endpoint can be used without authentication or the aforementioned permissions if only public resources are requested.

### Parameters for "List labels for issues in a milestone"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
milestone_numberintegerRequiredThe number that identifies the milestone.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.

```
milestone_number
```
The number that identifies the milestone.

[TABLE]
Name, Type, Description
per_pageintegerThe number of results per page (max 100). For more information, see "Using pagination in the REST API."Default:30
pageintegerThe page number of the results to fetch. For more information, see "Using pagination in the REST API."Default:1
[/TABLE]
The number of results per page (max 100). For more information, see "Using pagination in the REST API."
Default:30
The page number of the results to fetch. For more information, see "Using pagination in the REST API."
Default:1

### HTTP response status codes for "List labels for issues in a milestone"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "List labels for issues in a milestone"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/milestones/MILESTONE_NUMBER/labels
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
    "id": 208045946,
    "node_id": "MDU6TGFiZWwyMDgwNDU5NDY=",
    "url": "https://api.github.com/repos/octocat/Hello-World/labels/bug",
    "name": "bug",
    "description": "Something isn't working",
    "color": "f29513",
    "default": true
  },
  {
    "id": 208045947,
    "node_id": "MDU6TGFiZWwyMDgwNDU5NDc=",
    "url": "https://api.github.com/repos/octocat/Hello-World/labels/enhancement",
    "name": "enhancement",
    "description": "New feature or request",
    "color": "a2eeef",
    "default": false
  }
]
```