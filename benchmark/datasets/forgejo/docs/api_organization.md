# Organization

*Source: https://codeberg.org/swagger.v1.json*

---

### POST `/org/{org}/repos`

**Create a repository in an organization**

**Parameters:**
  - `org` [path] (required) *string*: name of organization
  - `body` [body] *any*: 

**Request body** (`body`): 

**Responses:**
  - `201`: 
  - `403`: 
  - `404`: 
  - `422`: 

### GET `/orgs`

**List all organizations**

**Parameters:**
  - `page` [query] *integer*: page number of results to return (1-based)
  - `limit` [query] *integer*: page size of results

**Responses:**
  - `200`: 

### POST `/orgs`

**Create an organization**

**Parameters:**
  - `organization` [body] (required) *any*: 

**Request body** (`organization`): 

**Responses:**
  - `201`: 
  - `403`: 
  - `422`: 

### DELETE `/orgs/{org}`

**Delete an organization**

**Parameters:**
  - `org` [path] (required) *string*: organization that is to be deleted

**Responses:**
  - `204`: 
  - `404`: 

### GET `/orgs/{org}`

**Get an organization**

**Parameters:**
  - `org` [path] (required) *string*: name of the organization to get

**Responses:**
  - `200`: 
  - `404`: 

### PATCH `/orgs/{org}`

**Edit an organization**

**Parameters:**
  - `org` [path] (required) *string*: name of the organization to edit
  - `body` [body] (required) *any*: 

**Request body** (`body`): 

**Responses:**
  - `200`: 
  - `404`: 
  - `422`: 

### GET `/orgs/{org}/actions/runners`

**Get the organization's runners**

**Parameters:**
  - `org` [path] (required) *string*: name of the organization
  - `visible` [query] *boolean*: whether to include all visible runners (true) or only those that are directly owned by the organization (false)
  - `page` [query] *integer*: page number of results to return (1-based)
  - `limit` [query] *integer*: page size of results

**Responses:**
  - `200`: 
  - `400`: 
  - `404`: 

### POST `/orgs/{org}/actions/runners`

**Register a new organization-level runner**

**Parameters:**
  - `org` [path] (required) *string*: name of the organization
  - `body` [body] *any*: 

**Request body** (`body`): 

**Responses:**
  - `201`: 
  - `400`: 
  - `401`: 
  - `404`: 

### GET `/orgs/{org}/actions/runners/jobs`

**Search for organization's action jobs according filter conditions**

**Parameters:**
  - `org` [path] (required) *string*: name of the organization
  - `labels` [query] *string*: a comma separated list of run job labels to search for

**Responses:**
  - `200`: 
  - `403`: 

### GET `/orgs/{org}/actions/runners/registration-token`

**Get the organization's runner registration token**

This operation has been deprecated in Forgejo 15. Use the web UI or [`/orgs/{org}/actions/runners`](#/organization/registerOrgRunner) instead.

**Parameters:**
  - `org` [path] (required) *string*: name of the organization

**Responses:**
  - `200`: 

### DELETE `/orgs/{org}/actions/runners/{runner_id}`

**Delete a particular runner that belongs to the organization**

**Parameters:**
  - `org` [path] (required) *string*: name of the organization
  - `runner_id` [path] (required) *string*: ID of the runner

**Responses:**
  - `204`: runner has been deleted
  - `400`: 
  - `404`: 

### GET `/orgs/{org}/actions/runners/{runner_id}`

**Get a particular runner that belongs to the organization**

**Parameters:**
  - `org` [path] (required) *string*: name of the organization
  - `runner_id` [path] (required) *string*: ID of the runner

**Responses:**
  - `200`: 
  - `400`: 
  - `404`: 

### GET `/orgs/{org}/actions/secrets`

**List actions secrets of an organization**

**Parameters:**
  - `org` [path] (required) *string*: name of the organization
  - `page` [query] *integer*: page number of results to return (1-based)
  - `limit` [query] *integer*: page size of results

**Responses:**
  - `200`: 
  - `404`: 

### DELETE `/orgs/{org}/actions/secrets/{secretname}`

**Delete a secret in an organization**

**Parameters:**
  - `org` [path] (required) *string*: name of organization
  - `secretname` [path] (required) *string*: name of the secret

**Responses:**
  - `204`: delete one secret of the organization
  - `400`: 
  - `404`: 

### PUT `/orgs/{org}/actions/secrets/{secretname}`

**Create or Update a secret value in an organization**

**Parameters:**
  - `org` [path] (required) *string*: name of organization
  - `secretname` [path] (required) *string*: name of the secret
  - `body` [body] *any*: 

**Request body** (`body`): 

**Responses:**
  - `201`: response when creating a secret
  - `204`: response when updating a secret
  - `400`: 
  - `404`: 

### GET `/orgs/{org}/actions/variables`

**List variables of an organization**

**Parameters:**
  - `org` [path] (required) *string*: name of the organization
  - `page` [query] *integer*: page number of results to return (1-based)
  - `limit` [query] *integer*: page size of results

**Responses:**
  - `200`: 
  - `400`: 
  - `404`: 

### DELETE `/orgs/{org}/actions/variables/{variablename}`

**Delete organization's variable by name**

**Parameters:**
  - `org` [path] (required) *string*: name of the organization
  - `variablename` [path] (required) *string*: name of the variable

**Responses:**
  - `204`: response when deleting a variable
  - `400`: 
  - `404`: 

### GET `/orgs/{org}/actions/variables/{variablename}`

**Get organization's variable by name**

**Parameters:**
  - `org` [path] (required) *string*: name of the organization
  - `variablename` [path] (required) *string*: name of the variable

**Responses:**
  - `200`: 
  - `400`: 
  - `404`: 

### POST `/orgs/{org}/actions/variables/{variablename}`

**Create a new variable in organization**

**Parameters:**
  - `org` [path] (required) *string*: name of the organization
  - `variablename` [path] (required) *string*: name of the variable
  - `body` [body] *any*: 

**Request body** (`body`): 

**Responses:**
  - `201`: response when creating an org-level variable
  - `204`: response when creating an org-level variable
  - `400`: 
  - `404`: 

### PUT `/orgs/{org}/actions/variables/{variablename}`

**Update variable in organization**

**Parameters:**
  - `org` [path] (required) *string*: name of the organization
  - `variablename` [path] (required) *string*: name of the variable
  - `body` [body] *any*: 

**Request body** (`body`): 

**Responses:**
  - `201`: response when updating an org-level variable
  - `204`: response when updating an org-level variable
  - `400`: 
  - `404`: 

### GET `/orgs/{org}/activities/feeds`

**List an organization's activity feeds**

**Parameters:**
  - `org` [path] (required) *string*: name of the org
  - `date` [query] *string*: the date of the activities to be found
  - `page` [query] *integer*: page number of results to return (1-based)
  - `limit` [query] *integer*: page size of results

**Responses:**
  - `200`: 
  - `404`: 

### DELETE `/orgs/{org}/avatar`

**Delete an organization's avatar. It will be replaced by a default one**

**Parameters:**
  - `org` [path] (required) *string*: name of the organization

**Responses:**
  - `204`: 
  - `404`: 

### POST `/orgs/{org}/avatar`

**Update an organization's avatar**

**Parameters:**
  - `org` [path] (required) *string*: name of the organization
  - `body` [body] *any*: 

**Request body** (`body`): 

**Responses:**
  - `204`: 
  - `404`: 

### PUT `/orgs/{org}/block/{username}`

**Blocks a user from the organization**

**Parameters:**
  - `org` [path] (required) *string*: name of the org
  - `username` [path] (required) *string*: username of the user

**Responses:**
  - `204`: 
  - `404`: 
  - `422`: 

### GET `/orgs/{org}/hooks`

**List an organization's webhooks**

**Parameters:**
  - `org` [path] (required) *string*: name of the organization
  - `page` [query] *integer*: page number of results to return (1-based)
  - `limit` [query] *integer*: page size of results

**Responses:**
  - `200`: 
  - `404`: 

### POST `/orgs/{org}/hooks`

**Create a hook**

**Parameters:**
  - `org` [path] (required) *string*: name of the organization
  - `body` [body] (required) *any*: 

**Request body** (`body`): 

**Responses:**
  - `201`: 
  - `404`: 

### DELETE `/orgs/{org}/hooks/{id}`

**Delete a hook**

**Parameters:**
  - `org` [path] (required) *string*: name of the organization
  - `id` [path] (required) *integer*: id of the hook to delete

**Responses:**
  - `204`: 
  - `404`: 

### GET `/orgs/{org}/hooks/{id}`

**Get a hook**

**Parameters:**
  - `org` [path] (required) *string*: name of the organization
  - `id` [path] (required) *integer*: id of the hook to get

**Responses:**
  - `200`: 
  - `404`: 

### PATCH `/orgs/{org}/hooks/{id}`

**Update a hook**

**Parameters:**
  - `org` [path] (required) *string*: name of the organization
  - `id` [path] (required) *integer*: id of the hook to update
  - `body` [body] *any*: 

**Request body** (`body`): 

**Responses:**
  - `200`: 
  - `404`: 

### GET `/orgs/{org}/labels`

**List an organization's labels**

**Parameters:**
  - `org` [path] (required) *string*: name of the organization
  - `sort` [query] *string*: Specifies the sorting method: mostissues, leastissues, or reversealphabetically.
  - `page` [query] *integer*: page number of results to return (1-based)
  - `limit` [query] *integer*: page size of results

**Responses:**
  - `200`: 
  - `404`: 

### POST `/orgs/{org}/labels`

**Create a label for an organization**

**Parameters:**
  - `org` [path] (required) *string*: name of the organization
  - `body` [body] *any*: 

**Request body** (`body`): 

**Responses:**
  - `201`: 
  - `404`: 
  - `422`: 

### DELETE `/orgs/{org}/labels/{id}`

**Delete a label**

**Parameters:**
  - `org` [path] (required) *string*: name of the organization
  - `id` [path] (required) *integer*: id of the label to delete

**Responses:**
  - `204`: 
  - `404`: 

### GET `/orgs/{org}/labels/{id}`

**Get a single label**

**Parameters:**
  - `org` [path] (required) *string*: name of the organization
  - `id` [path] (required) *integer*: id of the label to get

**Responses:**
  - `200`: 
  - `404`: 

### PATCH `/orgs/{org}/labels/{id}`

**Update a label**

**Parameters:**
  - `org` [path] (required) *string*: name of the organization
  - `id` [path] (required) *integer*: id of the label to edit
  - `body` [body] *any*: 

**Request body** (`body`): 

**Responses:**
  - `200`: 
  - `404`: 
  - `422`: 

### GET `/orgs/{org}/list_blocked`

**List the organization's blocked users**

**Parameters:**
  - `org` [path] (required) *string*: name of the org
  - `page` [query] *integer*: page number of results to return (1-based)
  - `limit` [query] *integer*: page size of results

**Responses:**
  - `200`: 

### GET `/orgs/{org}/members`

**List an organization's members**

**Parameters:**
  - `org` [path] (required) *string*: name of the organization
  - `page` [query] *integer*: page number of results to return (1-based)
  - `limit` [query] *integer*: page size of results

**Responses:**
  - `200`: 
  - `404`: 

### DELETE `/orgs/{org}/members/{username}`

**Remove a member from an organization**

**Parameters:**
  - `org` [path] (required) *string*: name of the organization
  - `username` [path] (required) *string*: username of the user

**Responses:**
  - `204`: member removed
  - `404`: 

### GET `/orgs/{org}/members/{username}`

**Check if a user is a member of an organization**

**Parameters:**
  - `org` [path] (required) *string*: name of the organization
  - `username` [path] (required) *string*: username of the user

**Responses:**
  - `204`: user is a member
  - `303`: redirection to /orgs/{org}/public_members/{username}
  - `404`: user is not a member

### GET `/orgs/{org}/public_members`

**List an organization's public members**

**Parameters:**
  - `org` [path] (required) *string*: name of the organization
  - `page` [query] *integer*: page number of results to return (1-based)
  - `limit` [query] *integer*: page size of results

**Responses:**
  - `200`: 
  - `404`: 

### DELETE `/orgs/{org}/public_members/{username}`

**Conceal a user's membership**

**Parameters:**
  - `org` [path] (required) *string*: name of the organization
  - `username` [path] (required) *string*: username of the user

**Responses:**
  - `204`: 
  - `403`: 
  - `404`: 

### GET `/orgs/{org}/public_members/{username}`

**Check if a user is a public member of an organization**

**Parameters:**
  - `org` [path] (required) *string*: name of the organization
  - `username` [path] (required) *string*: username of the user

**Responses:**
  - `204`: user is a public member
  - `404`: user is not a public member

### PUT `/orgs/{org}/public_members/{username}`

**Publicize a user's membership**

**Parameters:**
  - `org` [path] (required) *string*: name of the organization
  - `username` [path] (required) *string*: username of the user

**Responses:**
  - `204`: membership publicized
  - `403`: 
  - `404`: 

### GET `/orgs/{org}/quota`

**Get quota information for an organization**

**Parameters:**
  - `org` [path] (required) *string*: name of the organization

**Responses:**
  - `200`: 
  - `403`: 
  - `404`: 

### GET `/orgs/{org}/quota/artifacts`

**List the artifacts affecting the organization's quota**

**Parameters:**
  - `org` [path] (required) *string*: name of the organization
  - `page` [query] *integer*: page number of results to return (1-based)
  - `limit` [query] *integer*: page size of results

**Responses:**
  - `200`: 
  - `403`: 
  - `404`: 

### GET `/orgs/{org}/quota/attachments`

**List the attachments affecting the organization's quota**

**Parameters:**
  - `org` [path] (required) *string*: name of the organization
  - `page` [query] *integer*: page number of results to return (1-based)
  - `limit` [query] *integer*: page size of results

**Responses:**
  - `200`: 
  - `403`: 
  - `404`: 

### GET `/orgs/{org}/quota/check`

**Check if the organization is over quota for a given subject**

**Parameters:**
  - `org` [path] (required) *string*: name of the organization
  - `subject` [query] (required) *string*: subject of the quota

**Responses:**
  - `200`: Returns true if the action is accepted.
  - `403`: 
  - `404`: 
  - `422`: 

### GET `/orgs/{org}/quota/packages`

**List the packages affecting the organization's quota**

**Parameters:**
  - `org` [path] (required) *string*: name of the organization
  - `page` [query] *integer*: page number of results to return (1-based)
  - `limit` [query] *integer*: page size of results

**Responses:**
  - `200`: 
  - `403`: 
  - `404`: 

### POST `/orgs/{org}/rename`

**Rename an organization**

**Parameters:**
  - `org` [path] (required) *string*: existing org name
  - `body` [body] (required) *any*: 

**Request body** (`body`): 

**Responses:**
  - `204`: 
  - `403`: 
  - `422`: 

### GET `/orgs/{org}/repos`

**List an organization's repos**

**Parameters:**
  - `org` [path] (required) *string*: name of the organization
  - `page` [query] *integer*: page number of results to return (1-based)
  - `limit` [query] *integer*: page size of results

**Responses:**
  - `200`: 
  - `404`: 

### POST `/orgs/{org}/repos`

**Create a repository in an organization**

**Parameters:**
  - `org` [path] (required) *string*: name of organization
  - `body` [body] *any*: 

**Request body** (`body`): 

**Responses:**
  - `201`: 
  - `400`: 
  - `403`: 
  - `404`: 

### GET `/orgs/{org}/teams`

**List an organization's teams**

**Parameters:**
  - `org` [path] (required) *string*: name of the organization
  - `page` [query] *integer*: page number of results to return (1-based)
  - `limit` [query] *integer*: page size of results

**Responses:**
  - `200`: 
  - `404`: 

### POST `/orgs/{org}/teams`

**Create a team**

**Parameters:**
  - `org` [path] (required) *string*: name of the organization
  - `body` [body] *any*: 

**Request body** (`body`): 

**Responses:**
  - `201`: 
  - `404`: 
  - `422`: 

### GET `/orgs/{org}/teams/search`

**Search for teams within an organization**

**Parameters:**
  - `org` [path] (required) *string*: name of the organization
  - `q` [query] *string*: keywords to search
  - `include_desc` [query] *boolean*: include search within team description (defaults to true)
  - `page` [query] *integer*: page number of results to return (1-based)
  - `limit` [query] *integer*: page size of results

**Responses:**
  - `200`: SearchResults of a successful search
  - `404`: 

### PUT `/orgs/{org}/unblock/{username}`

**Unblock a user from the organization**

**Parameters:**
  - `org` [path] (required) *string*: name of the org
  - `username` [path] (required) *string*: username of the user

**Responses:**
  - `204`: 
  - `404`: 
  - `422`: 

### DELETE `/teams/{id}`

**Delete a team**

**Parameters:**
  - `id` [path] (required) *integer*: id of the team to delete

**Responses:**
  - `204`: team deleted
  - `404`: 

### GET `/teams/{id}`

**Get a team**

**Parameters:**
  - `id` [path] (required) *integer*: id of the team to get

**Responses:**
  - `200`: 
  - `404`: 

### PATCH `/teams/{id}`

**Edit a team**

**Parameters:**
  - `id` [path] (required) *integer*: id of the team to edit
  - `body` [body] *any*: 

**Request body** (`body`): 

**Responses:**
  - `200`: 
  - `404`: 

### GET `/teams/{id}/activities/feeds`

**List a team's activity feeds**

**Parameters:**
  - `id` [path] (required) *integer*: id of the team
  - `date` [query] *string*: the date of the activities to be found
  - `page` [query] *integer*: page number of results to return (1-based)
  - `limit` [query] *integer*: page size of results

**Responses:**
  - `200`: 
  - `404`: 

### GET `/teams/{id}/members`

**List a team's members**

**Parameters:**
  - `id` [path] (required) *integer*: id of the team
  - `page` [query] *integer*: page number of results to return (1-based)
  - `limit` [query] *integer*: page size of results

**Responses:**
  - `200`: 
  - `404`: 

### DELETE `/teams/{id}/members/{username}`

**Remove a team member**

**Parameters:**
  - `id` [path] (required) *integer*: id of the team
  - `username` [path] (required) *string*: username of the user to remove

**Responses:**
  - `204`: 
  - `404`: 

### GET `/teams/{id}/members/{username}`

**List a particular member of team**

**Parameters:**
  - `id` [path] (required) *integer*: id of the team
  - `username` [path] (required) *string*: username of the member to list

**Responses:**
  - `200`: 
  - `404`: 

### PUT `/teams/{id}/members/{username}`

**Add a team member**

**Parameters:**
  - `id` [path] (required) *integer*: id of the team
  - `username` [path] (required) *string*: username of the user to add

**Responses:**
  - `204`: 
  - `404`: 

### GET `/teams/{id}/repos`

**List a team's repos**

**Parameters:**
  - `id` [path] (required) *integer*: id of the team
  - `page` [query] *integer*: page number of results to return (1-based)
  - `limit` [query] *integer*: page size of results

**Responses:**
  - `200`: 
  - `404`: 

### DELETE `/teams/{id}/repos/{org}/{repo}`

**Remove a repository from a team**

This does not delete the repository, it only removes the repository from the team.

**Parameters:**
  - `id` [path] (required) *integer*: id of the team
  - `org` [path] (required) *string*: organization that owns the repo to remove
  - `repo` [path] (required) *string*: name of the repo to remove

**Responses:**
  - `204`: 
  - `403`: 
  - `404`: 

### GET `/teams/{id}/repos/{org}/{repo}`

**List a particular repo of team**

**Parameters:**
  - `id` [path] (required) *integer*: id of the team
  - `org` [path] (required) *string*: organization that owns the repo to list
  - `repo` [path] (required) *string*: name of the repo to list

**Responses:**
  - `200`: 
  - `404`: 

### PUT `/teams/{id}/repos/{org}/{repo}`

**Add a repository to a team**

**Parameters:**
  - `id` [path] (required) *integer*: id of the team
  - `org` [path] (required) *string*: organization that owns the repo to add
  - `repo` [path] (required) *string*: name of the repo to add

**Responses:**
  - `204`: 
  - `403`: 
  - `404`: 

### GET `/user/orgs`

**List the current user's organizations**

**Parameters:**
  - `page` [query] *integer*: page number of results to return (1-based)
  - `limit` [query] *integer*: page size of results

**Responses:**
  - `200`: 
  - `401`: 
  - `403`: 
  - `404`: 

### GET `/users/{username}/orgs`

**List a user's organizations**

**Parameters:**
  - `username` [path] (required) *string*: username of user
  - `page` [query] *integer*: page number of results to return (1-based)
  - `limit` [query] *integer*: page size of results

**Responses:**
  - `200`: 
  - `404`: 

### GET `/users/{username}/orgs/{org}/permissions`

**Get user permissions in organization**

**Parameters:**
  - `username` [path] (required) *string*: username of user
  - `org` [path] (required) *string*: name of the organization

**Responses:**
  - `200`: 
  - `403`: 
  - `404`: 
