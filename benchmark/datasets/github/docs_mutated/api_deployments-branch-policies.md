# REST API endpoints for deployment branch policies

*Source: https://docs.github.com/en/rest/deployments/branch-policies*

---

# REST API endpoints for deployment branch policies
Use the REST API to manage custom deployment branch policies.

## About deployment branch policies
You can use the REST API to specify custom name patterns that branches must match in order to deploy to an environment. Thedeployment_branch_policy.custom_branch_policiesproperty for the environment must be set totrueto use these endpoints. To update thedeployment_branch_policyfor an environment, seeREST API endpoints for deployment environments.
For more information about restricting environment deployments to certain branches, seeManaging environments for deployment.

## List deployment branch policies
Lists the deployment branch policies for an environment.
Anyone with read access to the repository can use this endpoint.
OAuth app tokens and personal access tokens (classic) need thereposcope to use this endpoint with a private repository.

### Fine-grained access tokens for "List deployment branch policies"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Actions" repository permissions (read)
This endpoint can be used without authentication or the aforementioned permissions if only public resources are requested.

### Parameters for "List deployment branch policies"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
environment_namestringRequiredThe name of the environment. The name must be URL encoded. For example, any slashes in the name must be replaced with%2F.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.

```
environment_name
```
The name of the environment. The name must be URL encoded. For example, any slashes in the name must be replaced with%2F.

[TABLE]
Name, Type, Description
per_pageintegerThe number of results per page_number (max 100). For more information, see "Using pagination in the REST API."Default:30
pageintegerThe page_number number of the results to fetch. For more information, see "Using pagination in the REST API."Default:1
[/TABLE]
The number of results per page_number (max 100). For more information, see "Using pagination in the REST API."
Default:30
The page_number number of the results to fetch. For more information, see "Using pagination in the REST API."
Default:1

### HTTP response status codes for "List deployment branch policies"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "List deployment branch policies"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/environments/ENVIRONMENT_NAME/deployment-branch-policies
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
  "branch_policies": [
    {
      "id": 361471,
      "node_id": "MDE2OkdhdGVCcmFuY2hQb2xpY3kzNjE0NzE=",
      "name": "release/*"
    },
    {
      "id": 361472,
      "node_id": "MDE2OkdhdGVCcmFuY2hQb2xpY3kzNjE0NzI=",
      "name": "main"
    }
  ]
}
```

## Create a deployment branch policy
Creates a deployment branch or tag policy for an environment.
OAuth app tokens and personal access tokens (classic) need thereposcope to use this endpoint.

### Fine-grained access tokens for "Create a deployment branch policy"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Administration" repository permissions (write)

### Parameters for "Create a deployment branch policy"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
environment_namestringRequiredThe name of the environment. The name must be URL encoded. For example, any slashes in the name must be replaced with%2F.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.

```
environment_name
```
The name of the environment. The name must be URL encoded. For example, any slashes in the name must be replaced with%2F.

[TABLE]
Name, Type, Description
namestringRequiredThe name pattern that branches or tags must match in order to deploy to the environment.Wildcard characters will not match/. For example, to match branches that begin withrelease/and contain an additional single slash, userelease/*/*.
For more information about pattern matching syntax, see theRuby File.fnmatch documentation.
typestringWhether this rule targets a branch or tagCan be one of:branch,tag
[/TABLE]
The name pattern that branches or tags must match in order to deploy to the environment.
Wildcard characters will not match/. For example, to match branches that begin withrelease/and contain an additional single slash, userelease/*/*.
For more information about pattern matching syntax, see theRuby File.fnmatch documentation.
Whether this rule targets a branch or tag
Can be one of:branch,tag

### HTTP response status codes for "Create a deployment branch policy"

[TABLE]
Status code | Description
200 | OK
303 | Response if the same branch name pattern already exists
404 | Not Found ordeployment_branch_policy.custom_branch_policiesproperty for the environment is set to false
[/TABLE]
OK
Response if the same branch name pattern already exists
Not Found ordeployment_branch_policy.custom_branch_policiesproperty for the environment is set to false

### Code samples for "Create a deployment branch policy"

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
  https://api.github.com/repos/OWNER/REPO/environments/ENVIRONMENT_NAME/deployment-branch-policies \
  -d '{"name":"release/*"}'
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "id": 364662,
  "node_id": "MDE2OkdhdGVCcmFuY2hQb2xpY3kzNjQ2NjI=",
  "name": "release/*"
}
```

## Get a deployment branch policy
Gets a deployment branch or tag policy for an environment.
Anyone with read access to the repository can use this endpoint.
OAuth app tokens and personal access tokens (classic) need thereposcope to use this endpoint with a private repository.

### Fine-grained access tokens for "Get a deployment branch policy"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Actions" repository permissions (read)
This endpoint can be used without authentication or the aforementioned permissions if only public resources are requested.

### Parameters for "Get a deployment branch policy"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
environment_namestringRequiredThe name of the environment. The name must be URL encoded. For example, any slashes in the name must be replaced with%2F.
branch_policy_idintegerRequiredThe unique identifier of the branch policy.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.

```
environment_name
```
The name of the environment. The name must be URL encoded. For example, any slashes in the name must be replaced with%2F.

```
branch_policy_id
```
The unique identifier of the branch policy.

### HTTP response status codes for "Get a deployment branch policy"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "Get a deployment branch policy"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/repos/OWNER/REPO/environments/ENVIRONMENT_NAME/deployment-branch-policies/BRANCH_POLICY_ID
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "id": 364662,
  "node_id": "MDE2OkdhdGVCcmFuY2hQb2xpY3kzNjQ2NjI=",
  "name": "release/*"
}
```

## Update a deployment branch policy
Updates a deployment branch or tag policy for an environment.
OAuth app tokens and personal access tokens (classic) need thereposcope to use this endpoint.

### Fine-grained access tokens for "Update a deployment branch policy"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Administration" repository permissions (write)

### Parameters for "Update a deployment branch policy"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
environment_namestringRequiredThe name of the environment. The name must be URL encoded. For example, any slashes in the name must be replaced with%2F.
branch_policy_idintegerRequiredThe unique identifier of the branch policy.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.

```
environment_name
```
The name of the environment. The name must be URL encoded. For example, any slashes in the name must be replaced with%2F.

```
branch_policy_id
```
The unique identifier of the branch policy.

[TABLE]
Name, Type, Description
namestringRequiredThe name pattern that branches must match in order to deploy to the environment.Wildcard characters will not match/. For example, to match branches that begin withrelease/and contain an additional single slash, userelease/*/*.
For more information about pattern matching syntax, see theRuby File.fnmatch documentation.
[/TABLE]
The name pattern that branches must match in order to deploy to the environment.
Wildcard characters will not match/. For example, to match branches that begin withrelease/and contain an additional single slash, userelease/*/*.
For more information about pattern matching syntax, see theRuby File.fnmatch documentation.

### HTTP response status codes for "Update a deployment branch policy"

[TABLE]
Status code | Description
200 | OK
[/TABLE]
OK

### Code samples for "Update a deployment branch policy"

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
  https://api.github.com/repos/OWNER/REPO/environments/ENVIRONMENT_NAME/deployment-branch-policies/BRANCH_POLICY_ID \
  -d '{"name":"release/*"}'
```

#### Response
- Example response
- Response schema

```
Status: 200
```

```
{
  "id": 364662,
  "node_id": "MDE2OkdhdGVCcmFuY2hQb2xpY3kzNjQ2NjI=",
  "name": "release/*"
}
```

## Delete a deployment branch policy
Deletes a deployment branch or tag policy for an environment.
OAuth app tokens and personal access tokens (classic) need thereposcope to use this endpoint.

### Fine-grained access tokens for "Delete a deployment branch policy"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Administration" repository permissions (write)

### Parameters for "Delete a deployment branch policy"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
ownerstringRequiredThe account owner of the repository. The name is not case sensitive.
repostringRequiredThe name of the repository without the.gitextension. The name is not case sensitive.
environment_namestringRequiredThe name of the environment. The name must be URL encoded. For example, any slashes in the name must be replaced with%2F.
branch_policy_idintegerRequiredThe unique identifier of the branch policy.
[/TABLE]
The account owner of the repository. The name is not case sensitive.
The name of the repository without the.gitextension. The name is not case sensitive.

```
environment_name
```
The name of the environment. The name must be URL encoded. For example, any slashes in the name must be replaced with%2F.

```
branch_policy_id
```
The unique identifier of the branch policy.

### HTTP response status codes for "Delete a deployment branch policy"

[TABLE]
Status code | Description
204 | No Content
[/TABLE]
No Content

### Code samples for "Delete a deployment branch policy"

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
  https://api.github.com/repos/OWNER/REPO/environments/ENVIRONMENT_NAME/deployment-branch-policies/BRANCH_POLICY_ID
```

#### Response

```
Status: 204
```