# Repository

*Source: https://codeberg.org/swagger.v1.json*

---

### POST `/repos/migrate`

**Migrate a remote git repository**

**Parameters:**
  - `body` [body] *any*: 

**Request body** (`body`): 

**Responses:**
  - `201`: 
  - `403`: 
  - `409`: The repository with the same name already exists.
  - `413`: 
  - `422`: 

### GET `/repos/search`

**Search for repositories**

**Parameters:**
  - `q` [query] *string*: keyword
  - `topic` [query] *boolean*: Limit search to repositories with keyword as topic
  - `includeDesc` [query] *boolean*: include search of keyword within repository description
  - `uid` [query] *integer*: search only for repos that the user with the given id owns or contributes to
  - `priority_owner_id` [query] *integer*: repo owner to prioritize in the results
  - `team_id` [query] *integer*: search only for repos that belong to the given team id
  - `starredBy` [query] *integer*: search only for repos that the user with the given id has starred
  - `private` [query] *boolean*: include private repositories this user has access to (defaults to true)
  - `is_private` [query] *boolean*: show only public, private or all repositories (defaults to all)
  - `template` [query] *boolean*: include template repositories this user has access to (defaults to true)
  - `archived` [query] *boolean*: show only archived, non-archived or all repositories (defaults to all)
  - `mode` [query] *string*: type of repository to search for. Supported values are "fork", "source", "mirror" and "collaborative"
  - `exclusive` [query] *boolean*: if `uid` is given, search only for repos that the user owns
  - `sort` [query] *string*: sort repos by attribute. Supported values are "alpha", "created", "updated", "size", "git_size", "lfs_size", "stars", "forks" and "id". Default is "alpha"
  - `order` [query] *string*: sort order, either "asc" (ascending) or "desc" (descending). Default is "asc", ignored if "sort" is not specified.
  - `page` [query] *integer*: page number of results to return (1-based)
  - `limit` [query] *integer*: page size of results

**Responses:**
  - `200`: 
  - `422`: 

### DELETE `/repos/{owner}/{repo}`

**Delete a repository**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo to delete
  - `repo` [path] (required) *string*: name of the repo to delete

**Responses:**
  - `204`: 
  - `403`: 
  - `404`: 

### GET `/repos/{owner}/{repo}`

**Get a repository**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo

**Responses:**
  - `200`: 
  - `404`: 

### PATCH `/repos/{owner}/{repo}`

**Edit a repository's properties. Only fields that are set will be changed.**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo to edit
  - `repo` [path] (required) *string*: name of the repo to edit
  - `body` [body] *any*: Properties of a repo that you can edit

**Request body** (`body`): Properties of a repo that you can edit

**Responses:**
  - `200`: 
  - `403`: 
  - `404`: 
  - `422`: 

### GET `/repos/{owner}/{repo}/actions/runners`

**Get runners belonging to the repository**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `visible` [query] *boolean*: whether to include all visible runners (true) or only those that are directly owned by the repository (false)
  - `page` [query] *integer*: page number of results to return (1-based)
  - `limit` [query] *integer*: page size of results

**Responses:**
  - `200`: 
  - `400`: 
  - `404`: 

### POST `/repos/{owner}/{repo}/actions/runners`

**Register a new repository-level runner**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `body` [body] *any*: 

**Request body** (`body`): 

**Responses:**
  - `201`: 
  - `400`: 
  - `401`: 
  - `404`: 

### GET `/repos/{owner}/{repo}/actions/runners/jobs`

**Search for repository's action jobs according filter conditions**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `labels` [query] *string*: a comma separated list of run job labels to search for

**Responses:**
  - `200`: 
  - `403`: 

### GET `/repos/{owner}/{repo}/actions/runners/registration-token`

**Get a repository's runner registration token**

This operation has been deprecated in Forgejo 15. Use the web UI or [`/repos/{owner}/{repo}/actions/runners`](#/repository/registerRepoRunner) instead.

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo

**Responses:**
  - `200`: 

### DELETE `/repos/{owner}/{repo}/actions/runners/{runner_id}`

**Delete a particular runner that belongs to a repository**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `runner_id` [path] (required) *string*: ID of the runner

**Responses:**
  - `204`: runner has been deleted
  - `400`: 
  - `404`: 

### GET `/repos/{owner}/{repo}/actions/runners/{runner_id}`

**Get a particular runner that belongs to the repository**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `runner_id` [path] (required) *string*: ID of the runner

**Responses:**
  - `200`: 
  - `400`: 
  - `404`: 

### GET `/repos/{owner}/{repo}/actions/runs`

**List a repository's action runs**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `page` [query] *integer*: page number of results to return (1-based)
  - `limit` [query] *integer*: page size of results, default maximum page size is 50
  - `event` [query] *array*: Returns workflow run triggered by the specified events. For example, `push`, `pull_request` or `workflow_dispatch`.
  - `status` [query] *array*: Returns workflow runs with the check run status or conclusion that is specified. For example, a conclusion can be success or a status can be in_progress. Only Forgejo Actions can set a status of waiting, pending, or requested.
  - `run_number` [query] *integer*: Returns the workflow run associated with the run number.
  - `head_sha` [query] *string*: Only returns workflow runs that are associated with the specified head_sha.
  - `ref` [query] *string*: Only return workflow runs that involve the given Git reference, for example, `refs/heads/main`.
  - `workflow_id` [query] *string*: Only return workflow runs that involve the given workflow ID.

**Responses:**
  - `200`: 
  - `400`: 
  - `403`: 

### GET `/repos/{owner}/{repo}/actions/runs/{run_id}`

**Get an action run**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `run_id` [path] (required) *integer*: id of the action run

**Responses:**
  - `200`: 
  - `400`: 
  - `403`: 
  - `404`: 

### GET `/repos/{owner}/{repo}/actions/secrets`

**List an repo's actions secrets**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repository
  - `repo` [path] (required) *string*: name of the repository
  - `page` [query] *integer*: page number of results to return (1-based)
  - `limit` [query] *integer*: page size of results

**Responses:**
  - `200`: 
  - `404`: 

### DELETE `/repos/{owner}/{repo}/actions/secrets/{secretname}`

**Delete a secret in a repository**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repository
  - `repo` [path] (required) *string*: name of the repository
  - `secretname` [path] (required) *string*: name of the secret

**Responses:**
  - `204`: delete one secret of the organization
  - `400`: 
  - `404`: 

### PUT `/repos/{owner}/{repo}/actions/secrets/{secretname}`

**Create or Update a secret value in a repository**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repository
  - `repo` [path] (required) *string*: name of the repository
  - `secretname` [path] (required) *string*: name of the secret
  - `body` [body] *any*: 

**Request body** (`body`): 

**Responses:**
  - `201`: response when creating a secret
  - `204`: response when updating a secret
  - `400`: 
  - `404`: 

### GET `/repos/{owner}/{repo}/actions/tasks`

**List a repository's action tasks**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `page` [query] *integer*: page number of results to return (1-based)
  - `limit` [query] *integer*: page size of results, default maximum page size is 50
  - `status` [query] *array*: Returns workflow tasks with the check run status or conclusion that is specified.  For example, a conclusion can be success or a status can be in_progress.

**Responses:**
  - `200`: 
  - `400`: 
  - `403`: 
  - `404`: 
  - `409`: 
  - `422`: 

### GET `/repos/{owner}/{repo}/actions/variables`

**Get repo-level variables list**

**Parameters:**
  - `owner` [path] (required) *string*: name of the owner
  - `repo` [path] (required) *string*: name of the repository
  - `page` [query] *integer*: page number of results to return (1-based)
  - `limit` [query] *integer*: page size of results

**Responses:**
  - `200`: 
  - `400`: 
  - `404`: 

### DELETE `/repos/{owner}/{repo}/actions/variables/{variablename}`

**Delete a repo-level variable**

**Parameters:**
  - `owner` [path] (required) *string*: name of the owner
  - `repo` [path] (required) *string*: name of the repository
  - `variablename` [path] (required) *string*: name of the variable

**Responses:**
  - `204`: response when deleting a variable
  - `400`: 
  - `404`: 

### GET `/repos/{owner}/{repo}/actions/variables/{variablename}`

**Get a repo-level variable**

**Parameters:**
  - `owner` [path] (required) *string*: name of the owner
  - `repo` [path] (required) *string*: name of the repository
  - `variablename` [path] (required) *string*: name of the variable

**Responses:**
  - `200`: 
  - `400`: 
  - `404`: 

### POST `/repos/{owner}/{repo}/actions/variables/{variablename}`

**Create a repo-level variable**

**Parameters:**
  - `owner` [path] (required) *string*: name of the owner
  - `repo` [path] (required) *string*: name of the repository
  - `variablename` [path] (required) *string*: name of the variable
  - `body` [body] *any*: 

**Request body** (`body`): 

**Responses:**
  - `201`: response when creating a repo-level variable
  - `204`: response when creating a repo-level variable
  - `400`: 
  - `404`: 

### PUT `/repos/{owner}/{repo}/actions/variables/{variablename}`

**Update a repo-level variable**

**Parameters:**
  - `owner` [path] (required) *string*: name of the owner
  - `repo` [path] (required) *string*: name of the repository
  - `variablename` [path] (required) *string*: name of the variable
  - `body` [body] *any*: 

**Request body** (`body`): 

**Responses:**
  - `201`: response when updating a repo-level variable
  - `204`: response when updating a repo-level variable
  - `400`: 
  - `404`: 

### POST `/repos/{owner}/{repo}/actions/workflows/{workflowfilename}/dispatches`

**Dispatches a workflow**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `workflowfilename` [path] (required) *string*: name of the workflow
  - `body` [body] *any*: 

**Request body** (`body`): 

**Responses:**
  - `201`: 
  - `204`: 
  - `404`: 

### GET `/repos/{owner}/{repo}/activities/feeds`

**List a repository's activity feeds**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `date` [query] *string*: the date of the activities to be found
  - `page` [query] *integer*: page number of results to return (1-based)
  - `limit` [query] *integer*: page size of results

**Responses:**
  - `200`: 
  - `404`: 

### GET `/repos/{owner}/{repo}/archive/{archive}`

**Get an archive of a repository**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `archive` [path] (required) *string*: the git reference for download with attached archive format (e.g. master.zip)

**Responses:**
  - `200`: success
  - `404`: 

### GET `/repos/{owner}/{repo}/assignees`

**Return all users that have write access and can be assigned to issues**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo

**Responses:**
  - `200`: 
  - `404`: 

### DELETE `/repos/{owner}/{repo}/avatar`

**Delete a repository's avatar**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo

**Responses:**
  - `204`: 
  - `404`: 

### POST `/repos/{owner}/{repo}/avatar`

**Update a repository's avatar**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `body` [body] *any*: 

**Request body** (`body`): 

**Responses:**
  - `204`: 
  - `404`: 

### GET `/repos/{owner}/{repo}/branch_protections`

**List branch protections for a repository**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo

**Responses:**
  - `200`: 

### POST `/repos/{owner}/{repo}/branch_protections`

**Create a branch protections for a repository**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `body` [body] *any*: 

**Request body** (`body`): 

**Responses:**
  - `201`: 
  - `403`: 
  - `404`: 
  - `422`: 
  - `423`: 

### DELETE `/repos/{owner}/{repo}/branch_protections/{name}`

**Delete a specific branch protection for the repository**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `name` [path] (required) *string*: name of protected branch

**Responses:**
  - `204`: 
  - `404`: 

### GET `/repos/{owner}/{repo}/branch_protections/{name}`

**Get a specific branch protection for the repository**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `name` [path] (required) *string*: name of protected branch

**Responses:**
  - `200`: 
  - `404`: 

### PATCH `/repos/{owner}/{repo}/branch_protections/{name}`

**Edit a branch protections for a repository. Only fields that are set will be changed**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `name` [path] (required) *string*: name of protected branch
  - `body` [body] *any*: 

**Request body** (`body`): 

**Responses:**
  - `200`: 
  - `404`: 
  - `422`: 
  - `423`: 

### GET `/repos/{owner}/{repo}/branches`

**List a repository's branches**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `page` [query] *integer*: page number of results to return (1-based)
  - `limit` [query] *integer*: page size of results

**Responses:**
  - `200`: 

### POST `/repos/{owner}/{repo}/branches`

**Create a branch**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `body` [body] *any*: 

**Request body** (`body`): 

**Responses:**
  - `201`: 
  - `403`: The branch is archived or a mirror.
  - `404`: The old branch does not exist.
  - `409`: The branch with the same name already exists.
  - `413`: 
  - `423`: 

### DELETE `/repos/{owner}/{repo}/branches/{branch}`

**Delete a specific branch from a repository**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `branch` [path] (required) *string*: branch to delete

**Responses:**
  - `204`: 
  - `403`: 
  - `404`: 
  - `423`: 

### GET `/repos/{owner}/{repo}/branches/{branch}`

**Retrieve a specific branch from a repository, including its effective branch protection**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `branch` [path] (required) *string*: branch to get

**Responses:**
  - `200`: 
  - `404`: 

### PATCH `/repos/{owner}/{repo}/branches/{branch}`

**Update a branch**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `branch` [path] (required) *string*: name of the branch
  - `body` [body] *any*: 

**Request body** (`body`): 

**Responses:**
  - `204`: 
  - `403`: 
  - `404`: 
  - `422`: 

### GET `/repos/{owner}/{repo}/collaborators`

**List a repository's collaborators**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `page` [query] *integer*: page number of results to return (1-based)
  - `limit` [query] *integer*: page size of results

**Responses:**
  - `200`: 
  - `404`: 

### DELETE `/repos/{owner}/{repo}/collaborators/{collaborator}`

**Delete a collaborator from a repository**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `collaborator` [path] (required) *string*: username of the collaborator to delete

**Responses:**
  - `204`: 
  - `404`: 
  - `422`: 

### GET `/repos/{owner}/{repo}/collaborators/{collaborator}`

**Check if a user is a collaborator of a repository**

If the user is a collaborator, return 204. If the user is not a collaborator, return 404.

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `collaborator` [path] (required) *string*: username of the collaborator

**Responses:**
  - `204`: 
  - `404`: 
  - `422`: 

### PUT `/repos/{owner}/{repo}/collaborators/{collaborator}`

**Add a collaborator to a repository**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `collaborator` [path] (required) *string*: username of the collaborator to add
  - `body` [body] *any*: 

**Request body** (`body`): 

**Responses:**
  - `204`: 
  - `403`: 
  - `404`: 
  - `422`: 

### GET `/repos/{owner}/{repo}/collaborators/{collaborator}/permission`

**Get repository permissions for a user**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `collaborator` [path] (required) *string*: username of the collaborator

**Responses:**
  - `200`: 
  - `403`: 
  - `404`: 

### GET `/repos/{owner}/{repo}/commits`

**Get a list of all commits from a repository**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `sha` [query] *string*: SHA or branch to start listing commits from (usually 'master')
  - `path` [query] *string*: filepath of a file/dir
  - `stat` [query] *boolean*: include diff stats for every commit (disable for speedup, default 'true')
  - `verification` [query] *boolean*: include verification for every commit (disable for speedup, default 'true')
  - `files` [query] *boolean*: include a list of affected files for every commit (disable for speedup, default 'true')
  - `page` [query] *integer*: page number of results to return (1-based)
  - `limit` [query] *integer*: page size of results (ignored if used with 'path')
  - `not` [query] *string*: commits that match the given specifier will not be listed.

**Responses:**
  - `200`: 
  - `404`: 
  - `409`: 

### GET `/repos/{owner}/{repo}/commits/{ref}/status`

**Get a commit's combined status, by branch/tag/commit reference**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `ref` [path] (required) *string*: name of branch/tag/commit
  - `page` [query] *integer*: page number of results to return (1-based)
  - `limit` [query] *integer*: page size of results

**Responses:**
  - `200`: 
  - `400`: 
  - `404`: 

### GET `/repos/{owner}/{repo}/commits/{ref}/statuses`

**Get a commit's statuses, by branch/tag/commit reference**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `ref` [path] (required) *string*: name of branch/tag/commit
  - `sort` [query] *string*: type of sort
  - `state` [query] *string*: type of state
  - `page` [query] *integer*: page number of results to return (1-based)
  - `limit` [query] *integer*: page size of results

**Responses:**
  - `200`: 
  - `400`: 
  - `404`: 

### GET `/repos/{owner}/{repo}/commits/{sha}/pull`

**Get the pull request of the commit**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `sha` [path] (required) *string*: SHA of the commit to get

**Responses:**
  - `200`: 
  - `404`: 

### GET `/repos/{owner}/{repo}/compare/{basehead}`

**Get commit comparison information**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `basehead` [path] (required) *string*: compare two branches or commits

**Responses:**
  - `200`: 
  - `404`: 

### GET `/repos/{owner}/{repo}/contents`

**Gets the metadata of all the entries of the root dir**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `ref` [query] *string*: The name of the commit/branch/tag. Default the repository’s default branch (usually master)

**Responses:**
  - `200`: 
  - `404`: 

### POST `/repos/{owner}/{repo}/contents`

**Modify multiple files in a repository**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `body` [body] (required) *any*: 

**Request body** (`body`): 

**Responses:**
  - `201`: 
  - `403`: 
  - `404`: 
  - `409`: 
  - `413`: 
  - `422`: 
  - `423`: 

### DELETE `/repos/{owner}/{repo}/contents/{filepath}`

**Delete a file in a repository**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `filepath` [path] (required) *string*: path of the file to delete
  - `body` [body] (required) *any*: 

**Request body** (`body`): 

**Responses:**
  - `200`: 
  - `400`: 
  - `403`: 
  - `404`: 
  - `413`: 
  - `423`: 

### GET `/repos/{owner}/{repo}/contents/{filepath}`

**Gets the metadata and contents (if a file) of an entry in a repository, or a list of entries if a dir**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `filepath` [path] (required) *string*: path of the dir, file, symlink or submodule in the repo
  - `ref` [query] *string*: The name of the commit/branch/tag. Default the repository’s default branch (usually master)

**Responses:**
  - `200`: 
  - `404`: 

### POST `/repos/{owner}/{repo}/contents/{filepath}`

**Create a file in a repository**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `filepath` [path] (required) *string*: path of the file to create
  - `body` [body] (required) *any*: 

**Request body** (`body`): 

**Responses:**
  - `201`: 
  - `403`: 
  - `404`: 
  - `409`: 
  - `413`: 
  - `422`: 
  - `423`: 

### PUT `/repos/{owner}/{repo}/contents/{filepath}`

**Update a file in a repository**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `filepath` [path] (required) *string*: path of the file to update
  - `body` [body] (required) *any*: 

**Request body** (`body`): 

**Responses:**
  - `200`: 
  - `403`: 
  - `404`: 
  - `409`: 
  - `413`: 
  - `422`: 
  - `423`: 

### POST `/repos/{owner}/{repo}/convert`

**Convert a mirror repo to a normal repo.**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo to convert
  - `repo` [path] (required) *string*: name of the repo to convert

**Responses:**
  - `200`: 
  - `403`: 
  - `404`: 
  - `422`: 

### POST `/repos/{owner}/{repo}/diffpatch`

**Apply diff patch to repository**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `body` [body] (required) *any*: 

**Request body** (`body`): 

**Responses:**
  - `200`: 
  - `404`: 
  - `413`: 
  - `423`: 

### GET `/repos/{owner}/{repo}/editorconfig/{filepath}`

**Get the EditorConfig definitions of a file in a repository**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `filepath` [path] (required) *string*: filepath of file to get
  - `ref` [query] *string*: The name of the commit/branch/tag. Default the repository’s default branch (usually master)

**Responses:**
  - `200`: definitions
  - `404`: 

### DELETE `/repos/{owner}/{repo}/flags`

**Remove all flags from a repository**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo

**Responses:**
  - `204`: 
  - `403`: 
  - `404`: 

### GET `/repos/{owner}/{repo}/flags`

**List a repository's flags**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo

**Responses:**
  - `200`: 
  - `403`: 
  - `404`: 

### PUT `/repos/{owner}/{repo}/flags`

**Replace all flags of a repository**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `body` [body] *any*: 

**Request body** (`body`): 

**Responses:**
  - `204`: 
  - `403`: 
  - `404`: 

### DELETE `/repos/{owner}/{repo}/flags/{flag}`

**Remove a flag from a repository**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `flag` [path] (required) *string*: name of the flag

**Responses:**
  - `204`: 
  - `403`: 
  - `404`: 

### GET `/repos/{owner}/{repo}/flags/{flag}`

**Check if a repository has a given flag**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `flag` [path] (required) *string*: name of the flag

**Responses:**
  - `204`: 
  - `403`: 
  - `404`: 

### PUT `/repos/{owner}/{repo}/flags/{flag}`

**Add a flag to a repository**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `flag` [path] (required) *string*: name of the flag

**Responses:**
  - `204`: 
  - `403`: 
  - `404`: 

### GET `/repos/{owner}/{repo}/forks`

**List a repository's forks**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `page` [query] *integer*: page number of results to return (1-based)
  - `limit` [query] *integer*: page size of results

**Responses:**
  - `200`: 
  - `404`: 

### POST `/repos/{owner}/{repo}/forks`

**Fork a repository**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo to fork
  - `repo` [path] (required) *string*: name of the repo to fork
  - `body` [body] *any*: 

**Request body** (`body`): 

**Responses:**
  - `202`: 
  - `403`: 
  - `404`: 
  - `409`: The repository with the same name already exists.
  - `413`: 
  - `422`: 

### GET `/repos/{owner}/{repo}/git/blobs`

**Gets multiple blobs of a repository.**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `shas` [query] (required) *string*: a comma separated list of blob-sha (mind the overall URL-length limit of ~2,083 chars)

**Responses:**
  - `200`: 
  - `400`: 

### GET `/repos/{owner}/{repo}/git/blobs/{sha}`

**Gets the blob of a repository.**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `sha` [path] (required) *string*: sha of the blob to retrieve

**Responses:**
  - `200`: 
  - `400`: 
  - `404`: 

### GET `/repos/{owner}/{repo}/git/commits/{sha}`

**Get a single commit from a repository**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `sha` [path] (required) *string*: a git ref or commit sha
  - `stat` [query] *boolean*: include diff stats for every commit (disable for speedup, default 'true')
  - `verification` [query] *boolean*: include verification for every commit (disable for speedup, default 'true')
  - `files` [query] *boolean*: include a list of affected files for every commit (disable for speedup, default 'true')

**Responses:**
  - `200`: 
  - `404`: 
  - `422`: 

### GET `/repos/{owner}/{repo}/git/commits/{sha}.{diffType}`

**Get a commit's diff or patch**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `sha` [path] (required) *string*: SHA of the commit to get
  - `diffType` [path] (required) *string*: whether the output is diff or patch

**Responses:**
  - `200`: 
  - `404`: 

### DELETE `/repos/{owner}/{repo}/git/notes/{sha}`

**Removes a note corresponding to a single commit from a repository**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `sha` [path] (required) *string*: a git ref or commit sha

**Responses:**
  - `204`: 
  - `404`: 
  - `422`: 

### GET `/repos/{owner}/{repo}/git/notes/{sha}`

**Get a note corresponding to a single commit from a repository**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `sha` [path] (required) *string*: a git ref or commit sha
  - `verification` [query] *boolean*: include verification for every commit (disable for speedup, default 'true')
  - `files` [query] *boolean*: include a list of affected files for every commit (disable for speedup, default 'true')

**Responses:**
  - `200`: 
  - `404`: 
  - `422`: 

### POST `/repos/{owner}/{repo}/git/notes/{sha}`

**Set a note corresponding to a single commit from a repository**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `sha` [path] (required) *string*: a git ref or commit sha
  - `body` [body] *any*: 

**Request body** (`body`): 

**Responses:**
  - `200`: 
  - `404`: 
  - `422`: 

### GET `/repos/{owner}/{repo}/git/refs`

**Get specified ref or filtered repository's refs**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo

**Responses:**
  - `200`: 
  - `404`: 

### GET `/repos/{owner}/{repo}/git/refs/{ref}`

**Get specified ref or filtered repository's refs**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `ref` [path] (required) *string*: part or full name of the ref

**Responses:**
  - `200`: 
  - `404`: 

### GET `/repos/{owner}/{repo}/git/tags/{sha}`

**Gets the tag object of an annotated tag (not lightweight tags)**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `sha` [path] (required) *string*: sha of the tag. The Git tags API only supports annotated tag objects, not lightweight tags.

**Responses:**
  - `200`: 
  - `400`: 
  - `404`: 

### GET `/repos/{owner}/{repo}/git/trees/{sha}`

**Gets the tree of a repository.**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `sha` [path] (required) *string*: sha of the commit
  - `recursive` [query] *boolean*: show all directories and files
  - `page` [query] *integer*: page number; the 'truncated' field in the response will be true if there are still more items after this page, false if the last page
  - `per_page` [query] *integer*: number of items per page

**Responses:**
  - `200`: 
  - `400`: 
  - `404`: 

### GET `/repos/{owner}/{repo}/hooks`

**List the hooks in a repository**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `page` [query] *integer*: page number of results to return (1-based)
  - `limit` [query] *integer*: page size of results

**Responses:**
  - `200`: 
  - `404`: 

### POST `/repos/{owner}/{repo}/hooks`

**Create a hook**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `body` [body] *any*: 

**Request body** (`body`): 

**Responses:**
  - `201`: 
  - `404`: 

### GET `/repos/{owner}/{repo}/hooks/git`

**List the Git hooks in a repository**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo

**Responses:**
  - `200`: 
  - `404`: 

### DELETE `/repos/{owner}/{repo}/hooks/git/{id}`

**Delete a Git hook in a repository**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `id` [path] (required) *string*: id of the hook to get

**Responses:**
  - `204`: 
  - `404`: 

### GET `/repos/{owner}/{repo}/hooks/git/{id}`

**Get a Git hook**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `id` [path] (required) *string*: id of the hook to get

**Responses:**
  - `200`: 
  - `404`: 

### PATCH `/repos/{owner}/{repo}/hooks/git/{id}`

**Edit a Git hook in a repository**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `id` [path] (required) *string*: id of the hook to get
  - `body` [body] *any*: 

**Request body** (`body`): 

**Responses:**
  - `200`: 
  - `404`: 

### DELETE `/repos/{owner}/{repo}/hooks/{id}`

**Delete a hook in a repository**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `id` [path] (required) *integer*: id of the hook to delete

**Responses:**
  - `204`: 
  - `404`: 

### GET `/repos/{owner}/{repo}/hooks/{id}`

**Get a hook**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `id` [path] (required) *integer*: id of the hook to get

**Responses:**
  - `200`: 
  - `404`: 

### PATCH `/repos/{owner}/{repo}/hooks/{id}`

**Edit a hook in a repository**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `id` [path] (required) *integer*: index of the hook
  - `body` [body] *any*: 

**Request body** (`body`): 

**Responses:**
  - `200`: 
  - `404`: 

### POST `/repos/{owner}/{repo}/hooks/{id}/tests`

**Test a push webhook**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `id` [path] (required) *integer*: id of the hook to test
  - `ref` [query] *string*: The name of the commit/branch/tag, indicates which commit will be loaded to the webhook payload.

**Responses:**
  - `204`: 
  - `404`: 

### GET `/repos/{owner}/{repo}/issue_config`

**Returns the issue config for a repo**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo

**Responses:**
  - `200`: 
  - `404`: 

### GET `/repos/{owner}/{repo}/issue_config/validate`

**Returns the validation information for a issue config**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo

**Responses:**
  - `200`: 
  - `404`: 

### GET `/repos/{owner}/{repo}/issue_templates`

**Get available issue templates for a repository**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo

**Responses:**
  - `200`: 
  - `404`: 

### GET `/repos/{owner}/{repo}/issues/pinned`

**List a repo's pinned issues**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo

**Responses:**
  - `200`: 
  - `404`: 

### GET `/repos/{owner}/{repo}/keys`

**List a repository's keys**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `key_id` [query] *integer*: the key_id to search for
  - `fingerprint` [query] *string*: fingerprint of the key
  - `page` [query] *integer*: page number of results to return (1-based)
  - `limit` [query] *integer*: page size of results

**Responses:**
  - `200`: 
  - `404`: 

### POST `/repos/{owner}/{repo}/keys`

**Add a key to a repository**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `body` [body] *any*: 

**Request body** (`body`): 

**Responses:**
  - `201`: 
  - `404`: 
  - `422`: 

### DELETE `/repos/{owner}/{repo}/keys/{id}`

**Delete a key from a repository**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `id` [path] (required) *integer*: id of the key to delete

**Responses:**
  - `204`: 
  - `403`: 
  - `404`: 

### GET `/repos/{owner}/{repo}/keys/{id}`

**Get a repository's key by id**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `id` [path] (required) *integer*: id of the key to get

**Responses:**
  - `200`: 
  - `404`: 

### GET `/repos/{owner}/{repo}/languages`

**Get languages and number of bytes of code written**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo

**Responses:**
  - `200`: 
  - `404`: 

### GET `/repos/{owner}/{repo}/media/{filepath}`

**Get a file or it's LFS object from a repository**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `filepath` [path] (required) *string*: filepath of the file to get
  - `ref` [query] *string*: The name of the commit/branch/tag. Default the repository’s default branch (usually master)

**Responses:**
  - `200`: Returns raw file content.
  - `404`: 

### POST `/repos/{owner}/{repo}/mirror-sync`

**Sync a mirrored repository**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo to sync
  - `repo` [path] (required) *string*: name of the repo to sync

**Responses:**
  - `200`: 
  - `403`: 
  - `404`: 
  - `413`: 

### GET `/repos/{owner}/{repo}/new_pin_allowed`

**Returns if new Issue Pins are allowed**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo

**Responses:**
  - `200`: 
  - `404`: 

### GET `/repos/{owner}/{repo}/pulls`

**List a repo's pull requests. If a pull request is selected but fails to be retrieved for any reason, it will be a null value in the list of results.**

**Parameters:**
  - `owner` [path] (required) *string*: Owner of the repo
  - `repo` [path] (required) *string*: Name of the repo
  - `state` [query] *string*: State of pull request
  - `sort` [query] *string*: Type of sort
  - `milestone` [query] *integer*: ID of the milestone
  - `labels` [query] *array*: Label IDs
  - `poster` [query] *string*: Filter by pull request author
  - `page` [query] *integer*: Page number of results to return (1-based)
  - `limit` [query] *integer*: Page size of results

**Responses:**
  - `200`: 
  - `400`: 
  - `404`: 
  - `500`: 

### POST `/repos/{owner}/{repo}/pulls`

**Create a pull request**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `body` [body] *any*: 

**Request body** (`body`): 

**Responses:**
  - `201`: 
  - `404`: 
  - `409`: 
  - `413`: 
  - `422`: 
  - `423`: 

### GET `/repos/{owner}/{repo}/pulls/pinned`

**List a repo's pinned pull requests**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo

**Responses:**
  - `200`: 
  - `404`: 

### GET `/repos/{owner}/{repo}/pulls/{base}/{head}`

**Get a pull request by base and head**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `base` [path] (required) *string*: base of the pull request to get
  - `head` [path] (required) *string*: head of the pull request to get

**Responses:**
  - `200`: 
  - `404`: 

### GET `/repos/{owner}/{repo}/pulls/{index}`

**Get a pull request**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `index` [path] (required) *integer*: index of the pull request to get

**Responses:**
  - `200`: 
  - `404`: 

### PATCH `/repos/{owner}/{repo}/pulls/{index}`

**Update a pull request. If using deadline only the date will be taken into account, and time of day ignored.**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `index` [path] (required) *integer*: index of the pull request to edit
  - `body` [body] *any*: 

**Request body** (`body`): 

**Responses:**
  - `201`: 
  - `403`: 
  - `404`: 
  - `409`: 
  - `412`: 
  - `422`: 

### GET `/repos/{owner}/{repo}/pulls/{index}.{diffType}`

**Get a pull request diff or patch**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `index` [path] (required) *integer*: index of the pull request to get
  - `diffType` [path] (required) *string*: whether the output is diff or patch
  - `binary` [query] *boolean*: whether to include binary file changes. if true, the diff is applicable with `git apply`

**Responses:**
  - `200`: 
  - `404`: 

### GET `/repos/{owner}/{repo}/pulls/{index}/commits`

**Get commits for a pull request**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `index` [path] (required) *integer*: index of the pull request to get
  - `page` [query] *integer*: page number of results to return (1-based)
  - `limit` [query] *integer*: page size of results
  - `verification` [query] *boolean*: include verification for every commit (disable for speedup, default 'true')
  - `files` [query] *boolean*: include a list of affected files for every commit (disable for speedup, default 'true')

**Responses:**
  - `200`: 
  - `404`: 

### GET `/repos/{owner}/{repo}/pulls/{index}/files`

**Get changed files for a pull request**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `index` [path] (required) *integer*: index of the pull request to get
  - `skip-to` [query] *string*: skip to given file
  - `whitespace` [query] *string*: whitespace behavior
  - `page` [query] *integer*: page number of results to return (1-based)
  - `limit` [query] *integer*: page size of results

**Responses:**
  - `200`: 
  - `404`: 

### DELETE `/repos/{owner}/{repo}/pulls/{index}/merge`

**Cancel the scheduled auto merge for the given pull request**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `index` [path] (required) *integer*: index of the pull request to merge

**Responses:**
  - `204`: 
  - `403`: 
  - `404`: 
  - `423`: 

### GET `/repos/{owner}/{repo}/pulls/{index}/merge`

**Check if a pull request has been merged**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `index` [path] (required) *integer*: index of the pull request

**Responses:**
  - `204`: pull request has been merged
  - `404`: pull request has not been merged

### POST `/repos/{owner}/{repo}/pulls/{index}/merge`

**Merge a pull request**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `index` [path] (required) *integer*: index of the pull request to merge
  - `body` [body] *any*: 

**Request body** (`body`): 

**Responses:**
  - `200`: 
  - `404`: 
  - `405`: 
  - `409`: 
  - `413`: 
  - `423`: 

### DELETE `/repos/{owner}/{repo}/pulls/{index}/requested_reviewers`

**Cancel review requests for a pull request**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `index` [path] (required) *integer*: index of the pull request
  - `body` [body] (required) *any*: 

**Request body** (`body`): 

**Responses:**
  - `204`: 
  - `403`: 
  - `404`: 
  - `422`: 

### POST `/repos/{owner}/{repo}/pulls/{index}/requested_reviewers`

**Create review requests for a pull request**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `index` [path] (required) *integer*: index of the pull request
  - `body` [body] (required) *any*: 

**Request body** (`body`): 

**Responses:**
  - `201`: 
  - `403`: 
  - `404`: 
  - `422`: 

### GET `/repos/{owner}/{repo}/pulls/{index}/reviews`

**List all reviews for a pull request**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `index` [path] (required) *integer*: index of the pull request
  - `page` [query] *integer*: page number of results to return (1-based)
  - `limit` [query] *integer*: page size of results

**Responses:**
  - `200`: 
  - `404`: 

### POST `/repos/{owner}/{repo}/pulls/{index}/reviews`

**Create a review to an pull request**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `index` [path] (required) *integer*: index of the pull request
  - `body` [body] (required) *any*: 

**Request body** (`body`): 

**Responses:**
  - `200`: 
  - `404`: 
  - `422`: 

### DELETE `/repos/{owner}/{repo}/pulls/{index}/reviews/{id}`

**Delete a specific review from a pull request**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `index` [path] (required) *integer*: index of the pull request
  - `id` [path] (required) *integer*: id of the review

**Responses:**
  - `204`: 
  - `403`: 
  - `404`: 

### GET `/repos/{owner}/{repo}/pulls/{index}/reviews/{id}`

**Get a specific review for a pull request**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `index` [path] (required) *integer*: index of the pull request
  - `id` [path] (required) *integer*: id of the review

**Responses:**
  - `200`: 
  - `404`: 

### POST `/repos/{owner}/{repo}/pulls/{index}/reviews/{id}`

**Submit a pending review to an pull request**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `index` [path] (required) *integer*: index of the pull request
  - `id` [path] (required) *integer*: id of the review
  - `body` [body] (required) *any*: 

**Request body** (`body`): 

**Responses:**
  - `200`: 
  - `404`: 
  - `422`: 

### GET `/repos/{owner}/{repo}/pulls/{index}/reviews/{id}/comments`

**Get a specific review for a pull request**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `index` [path] (required) *integer*: index of the pull request
  - `id` [path] (required) *integer*: id of the review

**Responses:**
  - `200`: 
  - `404`: 

### POST `/repos/{owner}/{repo}/pulls/{index}/reviews/{id}/comments`

**Add a new comment to a pull request review**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `index` [path] (required) *integer*: index of the pull request
  - `id` [path] (required) *integer*: id of the review
  - `body` [body] (required) *any*: 

**Request body** (`body`): 

**Responses:**
  - `200`: 
  - `404`: 
  - `422`: 

### DELETE `/repos/{owner}/{repo}/pulls/{index}/reviews/{id}/comments/{comment}`

**Delete a pull review comment**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `index` [path] (required) *integer*: index of the pull request
  - `id` [path] (required) *integer*: id of the review
  - `comment` [path] (required) *integer*: id of the comment

**Responses:**
  - `204`: 
  - `403`: 
  - `404`: 

### GET `/repos/{owner}/{repo}/pulls/{index}/reviews/{id}/comments/{comment}`

**Get a pull review comment**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `index` [path] (required) *integer*: index of the pull request
  - `id` [path] (required) *integer*: id of the review
  - `comment` [path] (required) *integer*: id of the comment

**Responses:**
  - `200`: 
  - `403`: 
  - `404`: 

### POST `/repos/{owner}/{repo}/pulls/{index}/reviews/{id}/dismissals`

**Dismiss a review for a pull request**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `index` [path] (required) *integer*: index of the pull request
  - `id` [path] (required) *integer*: id of the review
  - `body` [body] (required) *any*: 

**Request body** (`body`): 

**Responses:**
  - `200`: 
  - `403`: 
  - `404`: 
  - `422`: 

### POST `/repos/{owner}/{repo}/pulls/{index}/reviews/{id}/undismissals`

**Cancel to dismiss a review for a pull request**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `index` [path] (required) *integer*: index of the pull request
  - `id` [path] (required) *integer*: id of the review

**Responses:**
  - `200`: 
  - `403`: 
  - `404`: 
  - `422`: 

### POST `/repos/{owner}/{repo}/pulls/{index}/update`

**Merge PR's baseBranch into headBranch**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `index` [path] (required) *integer*: index of the pull request to get
  - `style` [query] *string*: how to update pull request

**Responses:**
  - `200`: 
  - `403`: 
  - `404`: 
  - `409`: 
  - `413`: 
  - `422`: 

### GET `/repos/{owner}/{repo}/push_mirrors`

**Get all push mirrors of the repository**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `page` [query] *integer*: page number of results to return (1-based)
  - `limit` [query] *integer*: page size of results

**Responses:**
  - `200`: 
  - `400`: 
  - `403`: 
  - `404`: 

### POST `/repos/{owner}/{repo}/push_mirrors`

**Set up a new push mirror in a repository**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `body` [body] *any*: 

**Request body** (`body`): 

**Responses:**
  - `200`: 
  - `400`: 
  - `403`: 
  - `404`: 
  - `413`: 

### POST `/repos/{owner}/{repo}/push_mirrors-sync`

**Sync all push mirrored repository**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo to sync
  - `repo` [path] (required) *string*: name of the repo to sync

**Responses:**
  - `200`: 
  - `400`: 
  - `403`: 
  - `404`: 
  - `413`: 

### DELETE `/repos/{owner}/{repo}/push_mirrors/{name}`

**Remove a push mirror from a repository by remoteName**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `name` [path] (required) *string*: remote name of the pushMirror

**Responses:**
  - `204`: 
  - `400`: 
  - `404`: 

### GET `/repos/{owner}/{repo}/push_mirrors/{name}`

**Get push mirror of the repository by remoteName**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `name` [path] (required) *string*: remote name of push mirror

**Responses:**
  - `200`: 
  - `400`: 
  - `403`: 
  - `404`: 

### GET `/repos/{owner}/{repo}/raw/{filepath}`

**Get a file from a repository**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `filepath` [path] (required) *string*: filepath of the file to get
  - `ref` [query] *string*: The name of the commit/branch/tag. Default the repository’s default branch (usually master)

**Responses:**
  - `200`: Returns raw file content.
  - `404`: 

### GET `/repos/{owner}/{repo}/releases`

**List a repo's releases**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `draft` [query] *boolean*: filter (exclude / include) drafts, if you dont have repo write access none will show
  - `pre-release` [query] *boolean*: filter (exclude / include) pre-releases
  - `q` [query] *string*: Search string
  - `page` [query] *integer*: page number of results to return (1-based)
  - `limit` [query] *integer*: page size of results

**Responses:**
  - `200`: 
  - `404`: 

### POST `/repos/{owner}/{repo}/releases`

**Create a release**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `body` [body] *any*: 

**Request body** (`body`): 

**Responses:**
  - `201`: 
  - `404`: 
  - `409`: 
  - `422`: 

### GET `/repos/{owner}/{repo}/releases/latest`

**Gets the most recent non-prerelease, non-draft release of a repository, sorted by created_at**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo

**Responses:**
  - `200`: 
  - `404`: 

### DELETE `/repos/{owner}/{repo}/releases/tags/{tag}`

**Delete a release by tag name**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `tag` [path] (required) *string*: tag name of the release to delete

**Responses:**
  - `204`: 
  - `404`: 
  - `422`: 

### GET `/repos/{owner}/{repo}/releases/tags/{tag}`

**Get a release by tag name**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `tag` [path] (required) *string*: tag name of the release to get

**Responses:**
  - `200`: 
  - `404`: 

### DELETE `/repos/{owner}/{repo}/releases/{id}`

**Delete a release**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `id` [path] (required) *integer*: id of the release to delete

**Responses:**
  - `204`: 
  - `404`: 
  - `422`: 

### GET `/repos/{owner}/{repo}/releases/{id}`

**Get a release**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `id` [path] (required) *integer*: id of the release to get

**Responses:**
  - `200`: 
  - `404`: 

### PATCH `/repos/{owner}/{repo}/releases/{id}`

**Update a release**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `id` [path] (required) *integer*: id of the release to edit
  - `body` [body] *any*: 

**Request body** (`body`): 

**Responses:**
  - `200`: 
  - `404`: 

### GET `/repos/{owner}/{repo}/releases/{id}/assets`

**List release's attachments**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `id` [path] (required) *integer*: id of the release

**Responses:**
  - `200`: 
  - `404`: 

### POST `/repos/{owner}/{repo}/releases/{id}/assets`

**Create a release attachment**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `id` [path] (required) *integer*: id of the release
  - `name` [query] *string*: name of the attachment
  - `attachment` [formData] *file*: attachment to upload (this parameter is incompatible with `external_url`)
  - `external_url` [formData] *string*: url to external asset (this parameter is incompatible with `attachment`)

**Responses:**
  - `201`: 
  - `400`: 
  - `404`: 
  - `413`: 

### DELETE `/repos/{owner}/{repo}/releases/{id}/assets/{attachment_id}`

**Delete a release attachment**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `id` [path] (required) *integer*: id of the release
  - `attachment_id` [path] (required) *integer*: id of the attachment to delete

**Responses:**
  - `204`: 
  - `404`: 

### GET `/repos/{owner}/{repo}/releases/{id}/assets/{attachment_id}`

**Get a release attachment**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `id` [path] (required) *integer*: id of the release
  - `attachment_id` [path] (required) *integer*: id of the attachment to get

**Responses:**
  - `200`: 
  - `404`: 

### PATCH `/repos/{owner}/{repo}/releases/{id}/assets/{attachment_id}`

**Edit a release attachment**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `id` [path] (required) *integer*: id of the release
  - `attachment_id` [path] (required) *integer*: id of the attachment to edit
  - `body` [body] *any*: 

**Request body** (`body`): 

**Responses:**
  - `201`: 
  - `404`: 
  - `413`: 

### GET `/repos/{owner}/{repo}/reviewers`

**Return all users that can be requested to review in this repo**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo

**Responses:**
  - `200`: 
  - `404`: 

### GET `/repos/{owner}/{repo}/signing-key.gpg`

**Get signing-key.gpg for given repository**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo

**Responses:**
  - `200`: GPG armored public key

### GET `/repos/{owner}/{repo}/stargazers`

**List a repo's stargazers**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `page` [query] *integer*: page number of results to return (1-based)
  - `limit` [query] *integer*: page size of results

**Responses:**
  - `200`: 
  - `404`: 

### GET `/repos/{owner}/{repo}/statuses/{sha}`

**Get a commit's statuses**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `sha` [path] (required) *string*: sha of the commit
  - `sort` [query] *string*: type of sort
  - `state` [query] *string*: type of state
  - `page` [query] *integer*: page number of results to return (1-based)
  - `limit` [query] *integer*: page size of results

**Responses:**
  - `200`: 
  - `400`: 
  - `404`: 

### POST `/repos/{owner}/{repo}/statuses/{sha}`

**Create a commit status**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `sha` [path] (required) *string*: sha of the commit
  - `body` [body] *any*: 

**Request body** (`body`): 

**Responses:**
  - `201`: 
  - `400`: 
  - `404`: 

### GET `/repos/{owner}/{repo}/subscribers`

**List a repo's watchers**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `page` [query] *integer*: page number of results to return (1-based)
  - `limit` [query] *integer*: page size of results

**Responses:**
  - `200`: 
  - `404`: 

### DELETE `/repos/{owner}/{repo}/subscription`

**Unwatch a repo**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo

**Responses:**
  - `204`: 
  - `404`: 

### GET `/repos/{owner}/{repo}/subscription`

**Check if the current user is watching a repo**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo

**Responses:**
  - `200`: 
  - `404`: User is not watching this repo or repo do not exist

### PUT `/repos/{owner}/{repo}/subscription`

**Watch a repo**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo

**Responses:**
  - `200`: 
  - `404`: 

### GET `/repos/{owner}/{repo}/sync_fork`

**Gets information about syncing the fork default branch with the base branch**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo

**Responses:**
  - `200`: 
  - `400`: 
  - `404`: 

### POST `/repos/{owner}/{repo}/sync_fork`

**Syncs the default branch of a fork with the base branch**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo

**Responses:**
  - `204`: 
  - `400`: 
  - `404`: 

### GET `/repos/{owner}/{repo}/sync_fork/{branch}`

**Gets information about syncing a fork branch with the base branch**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `branch` [path] (required) *string*: The branch

**Responses:**
  - `200`: 
  - `400`: 
  - `404`: 

### POST `/repos/{owner}/{repo}/sync_fork/{branch}`

**Syncs a fork branch with the base branch**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `branch` [path] (required) *string*: The branch

**Responses:**
  - `204`: 
  - `400`: 
  - `404`: 

### GET `/repos/{owner}/{repo}/tag_protections`

**List tag protections for a repository**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo

**Responses:**
  - `200`: 

### POST `/repos/{owner}/{repo}/tag_protections`

**Create a tag protections for a repository**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `body` [body] *any*: 

**Request body** (`body`): 

**Responses:**
  - `201`: 
  - `403`: 
  - `404`: 
  - `422`: 
  - `423`: 

### DELETE `/repos/{owner}/{repo}/tag_protections/{id}`

**Delete a specific tag protection for the repository**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `id` [path] (required) *integer*: id of protected tag

**Responses:**
  - `204`: 
  - `404`: 

### GET `/repos/{owner}/{repo}/tag_protections/{id}`

**Get a specific tag protection for the repository**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `id` [path] (required) *integer*: id of the tag protect to get

**Responses:**
  - `200`: 
  - `404`: 

### PATCH `/repos/{owner}/{repo}/tag_protections/{id}`

**Edit a tag protections for a repository. Only fields that are set will be changed**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `id` [path] (required) *integer*: id of protected tag
  - `body` [body] *any*: 

**Request body** (`body`): 

**Responses:**
  - `200`: 
  - `404`: 
  - `422`: 
  - `423`: 

### GET `/repos/{owner}/{repo}/tags`

**List a repository's tags**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `page` [query] *integer*: page number of results to return (1-based)
  - `limit` [query] *integer*: page size of results, default maximum page size is 50

**Responses:**
  - `200`: 
  - `404`: 

### POST `/repos/{owner}/{repo}/tags`

**Create a new git tag in a repository**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `body` [body] *any*: 

**Request body** (`body`): 

**Responses:**
  - `201`: 
  - `404`: 
  - `405`: 
  - `409`: 
  - `413`: 
  - `422`: 
  - `423`: 

### DELETE `/repos/{owner}/{repo}/tags/{tag}`

**Delete a repository's tag by name**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `tag` [path] (required) *string*: name of tag to delete

**Responses:**
  - `204`: 
  - `404`: 
  - `405`: 
  - `409`: 
  - `422`: 
  - `423`: 

### GET `/repos/{owner}/{repo}/tags/{tag}`

**Get the tag of a repository by tag name**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `tag` [path] (required) *string*: name of tag

**Responses:**
  - `200`: 
  - `404`: 

### GET `/repos/{owner}/{repo}/teams`

**List a repository's teams**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo

**Responses:**
  - `200`: 
  - `404`: 
  - `405`: 

### DELETE `/repos/{owner}/{repo}/teams/{team}`

**Delete a team from a repository**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `team` [path] (required) *string*: team name

**Responses:**
  - `204`: 
  - `404`: 
  - `405`: 
  - `422`: 

### GET `/repos/{owner}/{repo}/teams/{team}`

**Check if a team is assigned to a repository**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `team` [path] (required) *string*: team name

**Responses:**
  - `200`: 
  - `404`: 
  - `405`: 

### PUT `/repos/{owner}/{repo}/teams/{team}`

**Add a team to a repository**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `team` [path] (required) *string*: team name

**Responses:**
  - `204`: 
  - `404`: 
  - `405`: 
  - `422`: 

### GET `/repos/{owner}/{repo}/times`

**List a repo's tracked times**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `user` [query] *string*: optional filter by user (available for issue managers)
  - `since` [query] *string*: Only show times updated after the given time. This is a timestamp in RFC 3339 format
  - `before` [query] *string*: Only show times updated before the given time. This is a timestamp in RFC 3339 format
  - `page` [query] *integer*: page number of results to return (1-based)
  - `limit` [query] *integer*: page size of results

**Responses:**
  - `200`: 
  - `400`: 
  - `403`: 
  - `404`: 
  - `422`: 

### GET `/repos/{owner}/{repo}/times/{user}`

**List a user's tracked times in a repo**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `user` [path] (required) *string*: username of user

**Responses:**
  - `200`: 
  - `400`: 
  - `403`: 
  - `404`: 

### GET `/repos/{owner}/{repo}/topics`

**Get list of topics that a repository has**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `page` [query] *integer*: page number of results to return (1-based)
  - `limit` [query] *integer*: page size of results

**Responses:**
  - `200`: 
  - `404`: 

### PUT `/repos/{owner}/{repo}/topics`

**Replace list of topics for a repository**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `body` [body] *any*: 

**Request body** (`body`): 

**Responses:**
  - `204`: 
  - `404`: 
  - `422`: 

### DELETE `/repos/{owner}/{repo}/topics/{topic}`

**Delete a topic from a repository**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `topic` [path] (required) *string*: name of the topic to delete

**Responses:**
  - `204`: 
  - `404`: 
  - `422`: 

### PUT `/repos/{owner}/{repo}/topics/{topic}`

**Add a topic to a repository**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `topic` [path] (required) *string*: name of the topic to add

**Responses:**
  - `204`: 
  - `404`: 
  - `422`: 

### POST `/repos/{owner}/{repo}/transfer`

**Transfer a repo ownership**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo to transfer
  - `repo` [path] (required) *string*: name of the repo to transfer
  - `body` [body] (required) *any*: Transfer Options

**Request body** (`body`): Transfer Options

**Responses:**
  - `202`: 
  - `403`: 
  - `404`: 
  - `413`: 
  - `422`: 

### POST `/repos/{owner}/{repo}/transfer/accept`

**Accept a repo transfer**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo to transfer
  - `repo` [path] (required) *string*: name of the repo to transfer

**Responses:**
  - `202`: 
  - `403`: 
  - `404`: 
  - `413`: 

### POST `/repos/{owner}/{repo}/transfer/reject`

**Reject a repo transfer**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo to transfer
  - `repo` [path] (required) *string*: name of the repo to transfer

**Responses:**
  - `200`: 
  - `403`: 
  - `404`: 

### POST `/repos/{owner}/{repo}/wiki/new`

**Create a wiki page**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `body` [body] *any*: 

**Request body** (`body`): 

**Responses:**
  - `201`: 
  - `400`: 
  - `403`: 
  - `404`: 
  - `413`: 
  - `423`: 

### DELETE `/repos/{owner}/{repo}/wiki/page/{pageName}`

**Delete a wiki page**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `pageName` [path] (required) *string*: name of the page

**Responses:**
  - `204`: 
  - `403`: 
  - `404`: 
  - `423`: 

### GET `/repos/{owner}/{repo}/wiki/page/{pageName}`

**Get a wiki page**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `pageName` [path] (required) *string*: name of the page

**Responses:**
  - `200`: 
  - `404`: 

### PATCH `/repos/{owner}/{repo}/wiki/page/{pageName}`

**Edit a wiki page**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `pageName` [path] (required) *string*: name of the page
  - `body` [body] *any*: 

**Request body** (`body`): 

**Responses:**
  - `200`: 
  - `400`: 
  - `403`: 
  - `404`: 
  - `413`: 
  - `423`: 

### GET `/repos/{owner}/{repo}/wiki/pages`

**Get all wiki pages**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `page` [query] *integer*: page number of results to return (1-based)
  - `limit` [query] *integer*: page size of results

**Responses:**
  - `200`: 
  - `404`: 

### GET `/repos/{owner}/{repo}/wiki/revisions/{pageName}`

**Get revisions of a wiki page**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `pageName` [path] (required) *string*: name of the page
  - `page` [query] *integer*: page number of results to return (1-based)

**Responses:**
  - `200`: 
  - `404`: 

### POST `/repos/{template_owner}/{template_repo}/generate`

**Create a repository using a template**

**Parameters:**
  - `template_owner` [path] (required) *string*: name of the template repository owner
  - `template_repo` [path] (required) *string*: name of the template repository
  - `body` [body] *any*: 

**Request body** (`body`): 

**Responses:**
  - `201`: 
  - `403`: 
  - `404`: 
  - `409`: The repository with the same name already exists.
  - `413`: 
  - `422`: 

### GET `/repositories/{id}`

**Get a repository by id**

**Parameters:**
  - `id` [path] (required) *integer*: id of the repo to get

**Responses:**
  - `200`: 
  - `404`: 

### GET `/topics/search`

**Search for topics by keyword**

**Parameters:**
  - `q` [query] (required) *string*: keyword to search for
  - `page` [query] *integer*: page number of results to return (1-based)
  - `limit` [query] *integer*: page size of results

**Responses:**
  - `200`: SearchResults of a successful search
  - `403`: 
  - `404`: 

### POST `/user/repos`

**Create a repository**

**Parameters:**
  - `body` [body] *any*: 

**Request body** (`body`): 

**Responses:**
  - `201`: 
  - `400`: 
  - `401`: 
  - `403`: 
  - `409`: The repository with the same name already exists.
  - `413`: 
  - `422`: 
