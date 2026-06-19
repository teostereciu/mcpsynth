# User

*Source: https://codeberg.org/swagger.v1.json*

---

### GET `/user`

**Get the authenticated user**

**Responses:**
  - `200`: 
  - `401`: 
  - `403`: 

### GET `/user/actions/runners`

**Get the user's runners**

**Parameters:**
  - `visible` [query] *boolean*: whether to include all visible runners (true) or only those that are directly owned by the user (false)
  - `page` [query] *integer*: page number of results to return (1-based)
  - `limit` [query] *integer*: page size of results

**Responses:**
  - `200`: 
  - `400`: 
  - `401`: 
  - `404`: 

### POST `/user/actions/runners`

**Register a new user-level runner**

**Parameters:**
  - `body` [body] *any*: 

**Request body** (`body`): 

**Responses:**
  - `201`: 
  - `400`: 
  - `401`: 
  - `404`: 

### GET `/user/actions/runners/jobs`

**Search for user's action jobs according filter conditions**

**Parameters:**
  - `labels` [query] *string*: a comma separated list of run job labels to search for

**Responses:**
  - `200`: 
  - `401`: 
  - `403`: 

### GET `/user/actions/runners/registration-token`

**Get the user's runner registration token**

This operation has been deprecated in Forgejo 15. Use the web UI or [`/user/actions/runners`](#/user/registerUserRunner) instead.

**Responses:**
  - `200`: 
  - `401`: 
  - `403`: 

### DELETE `/user/actions/runners/{runner_id}`

**Delete a particular user-level runner**

**Parameters:**
  - `runner_id` [path] (required) *string*: ID of the runner

**Responses:**
  - `204`: runner has been deleted
  - `400`: 
  - `401`: 
  - `404`: 

### GET `/user/actions/runners/{runner_id}`

**Get a particular runner that belongs to the user**

**Parameters:**
  - `runner_id` [path] (required) *string*: ID of the runner

**Responses:**
  - `200`: 
  - `400`: 
  - `401`: 
  - `404`: 

### DELETE `/user/actions/secrets/{secretname}`

**Delete a secret in a user scope**

**Parameters:**
  - `secretname` [path] (required) *string*: name of the secret

**Responses:**
  - `204`: delete one secret of the user
  - `400`: 
  - `401`: 
  - `403`: 
  - `404`: 

### PUT `/user/actions/secrets/{secretname}`

**Create or Update a secret value in a user scope**

**Parameters:**
  - `secretname` [path] (required) *string*: name of the secret
  - `body` [body] *any*: 

**Request body** (`body`): 

**Responses:**
  - `201`: response when creating a secret
  - `204`: response when updating a secret
  - `400`: 
  - `401`: 
  - `403`: 
  - `404`: 

### GET `/user/actions/variables`

**Get the user-level list of variables which is created by current doer**

**Parameters:**
  - `page` [query] *integer*: page number of results to return (1-based)
  - `limit` [query] *integer*: page size of results

**Responses:**
  - `200`: 
  - `400`: 
  - `401`: 
  - `403`: 
  - `404`: 

### DELETE `/user/actions/variables/{variablename}`

**Delete a user-level variable which is created by current doer**

**Parameters:**
  - `variablename` [path] (required) *string*: name of the variable

**Responses:**
  - `201`: response when deleting a variable
  - `204`: response when deleting a variable
  - `400`: 
  - `401`: 
  - `403`: 
  - `404`: 

### GET `/user/actions/variables/{variablename}`

**Get a user-level variable which is created by current doer**

**Parameters:**
  - `variablename` [path] (required) *string*: name of the variable

**Responses:**
  - `200`: 
  - `400`: 
  - `401`: 
  - `403`: 
  - `404`: 

### POST `/user/actions/variables/{variablename}`

**Create a user-level variable**

**Parameters:**
  - `variablename` [path] (required) *string*: name of the variable
  - `body` [body] *any*: 

**Request body** (`body`): 

**Responses:**
  - `201`: response when creating a variable
  - `204`: response when creating a variable
  - `400`: 
  - `401`: 
  - `403`: 
  - `404`: 

### PUT `/user/actions/variables/{variablename}`

**Update a user-level variable which is created by current doer**

**Parameters:**
  - `variablename` [path] (required) *string*: name of the variable
  - `body` [body] *any*: 

**Request body** (`body`): 

**Responses:**
  - `201`: response when updating a variable
  - `204`: response when updating a variable
  - `400`: 
  - `401`: 
  - `403`: 
  - `404`: 

### GET `/user/applications/oauth2`

**List the authenticated user's oauth2 applications**

**Parameters:**
  - `page` [query] *integer*: page number of results to return (1-based)
  - `limit` [query] *integer*: page size of results

**Responses:**
  - `200`: 
  - `401`: 
  - `403`: 

### POST `/user/applications/oauth2`

**Creates a new OAuth2 application**

**Parameters:**
  - `body` [body] (required) *any*: 

**Request body** (`body`): 

**Responses:**
  - `201`: 
  - `400`: 
  - `401`: 
  - `403`: 

### DELETE `/user/applications/oauth2/{id}`

**Delete an OAuth2 application**

**Parameters:**
  - `id` [path] (required) *integer*: token to be deleted

**Responses:**
  - `204`: 
  - `401`: 
  - `403`: 
  - `404`: 

### GET `/user/applications/oauth2/{id}`

**Get an OAuth2 application**

**Parameters:**
  - `id` [path] (required) *integer*: Application ID to be found

**Responses:**
  - `200`: 
  - `401`: 
  - `403`: 
  - `404`: 

### PATCH `/user/applications/oauth2/{id}`

**Update an OAuth2 application, this includes regenerating the client secret**

**Parameters:**
  - `id` [path] (required) *integer*: application to be updated
  - `body` [body] (required) *any*: 

**Request body** (`body`): 

**Responses:**
  - `200`: 
  - `401`: 
  - `403`: 
  - `404`: 

### DELETE `/user/avatar`

**Delete avatar of the current user. It will be replaced by a default one**

**Responses:**
  - `204`: 
  - `401`: 
  - `403`: 

### POST `/user/avatar`

**Update avatar of the current user**

**Parameters:**
  - `body` [body] *any*: 

**Request body** (`body`): 

**Responses:**
  - `204`: 
  - `401`: 
  - `403`: 

### PUT `/user/block/{username}`

**Blocks a user from the doer**

**Parameters:**
  - `username` [path] (required) *string*: username of the user

**Responses:**
  - `204`: 
  - `401`: 
  - `403`: 
  - `404`: 
  - `422`: 

### DELETE `/user/emails`

**Delete email addresses from the current user's account**

**Parameters:**
  - `body` [body] *any*: 

**Request body** (`body`): 

**Responses:**
  - `204`: 
  - `401`: 
  - `403`: 
  - `404`: 

### GET `/user/emails`

**List all email addresses of the current user**

**Responses:**
  - `200`: 
  - `401`: 
  - `403`: 

### POST `/user/emails`

**Add an email addresses to the current user's account**

**Parameters:**
  - `body` [body] *any*: 

**Request body** (`body`): 

**Responses:**
  - `201`: 
  - `401`: 
  - `403`: 
  - `422`: 

### GET `/user/followers`

**List the authenticated user's followers**

**Parameters:**
  - `page` [query] *integer*: page number of results to return (1-based)
  - `limit` [query] *integer*: page size of results

**Responses:**
  - `200`: 
  - `401`: 
  - `403`: 

### GET `/user/following`

**List the users that the authenticated user is following**

**Parameters:**
  - `page` [query] *integer*: page number of results to return (1-based)
  - `limit` [query] *integer*: page size of results

**Responses:**
  - `200`: 
  - `401`: 
  - `403`: 

### DELETE `/user/following/{username}`

**Unfollow a user**

**Parameters:**
  - `username` [path] (required) *string*: username of user to unfollow

**Responses:**
  - `204`: 
  - `401`: 
  - `403`: 
  - `404`: 

### GET `/user/following/{username}`

**Check whether a user is followed by the authenticated user**

**Parameters:**
  - `username` [path] (required) *string*: username of followed user

**Responses:**
  - `204`: 
  - `401`: 
  - `403`: 
  - `404`: 

### PUT `/user/following/{username}`

**Follow a user**

**Parameters:**
  - `username` [path] (required) *string*: username of user to follow

**Responses:**
  - `204`: 
  - `401`: 
  - `403`: 
  - `404`: 

### GET `/user/gpg_key_token`

**Get a Token to verify**

**Responses:**
  - `200`: 
  - `401`: 
  - `403`: 
  - `404`: 

### POST `/user/gpg_key_verify`

**Verify a GPG key**

**Parameters:**
  - `body` [body] *any*: 

**Request body** (`body`): 

**Responses:**
  - `201`: 
  - `401`: 
  - `403`: 
  - `404`: 
  - `422`: 

### GET `/user/gpg_keys`

**List the authenticated user's GPG keys**

**Parameters:**
  - `page` [query] *integer*: page number of results to return (1-based)
  - `limit` [query] *integer*: page size of results

**Responses:**
  - `200`: 
  - `401`: 
  - `403`: 

### POST `/user/gpg_keys`

**Add a GPG public key to current user's account**

**Parameters:**
  - `Form` [body] *any*: 

**Request body** (`Form`): 

**Responses:**
  - `201`: 
  - `401`: 
  - `403`: 
  - `404`: 
  - `422`: 

### DELETE `/user/gpg_keys/{id}`

**Remove a GPG public key from current user's account**

**Parameters:**
  - `id` [path] (required) *integer*: id of key to delete

**Responses:**
  - `204`: 
  - `401`: 
  - `403`: 
  - `404`: 

### GET `/user/gpg_keys/{id}`

**Get a GPG key**

**Parameters:**
  - `id` [path] (required) *integer*: id of key to get

**Responses:**
  - `200`: 
  - `401`: 
  - `403`: 
  - `404`: 

### GET `/user/hooks`

**List the authenticated user's webhooks**

**Parameters:**
  - `page` [query] *integer*: page number of results to return (1-based)
  - `limit` [query] *integer*: page size of results

**Responses:**
  - `200`: 
  - `401`: 
  - `403`: 

### POST `/user/hooks`

**Create a hook**

**Parameters:**
  - `body` [body] (required) *any*: 

**Request body** (`body`): 

**Responses:**
  - `201`: 
  - `401`: 
  - `403`: 

### DELETE `/user/hooks/{id}`

**Delete a hook**

**Parameters:**
  - `id` [path] (required) *integer*: id of the hook to delete

**Responses:**
  - `204`: 
  - `401`: 
  - `403`: 

### GET `/user/hooks/{id}`

**Get a hook**

**Parameters:**
  - `id` [path] (required) *integer*: id of the hook to get

**Responses:**
  - `200`: 
  - `401`: 
  - `403`: 

### PATCH `/user/hooks/{id}`

**Update a hook**

**Parameters:**
  - `id` [path] (required) *integer*: id of the hook to update
  - `body` [body] *any*: 

**Request body** (`body`): 

**Responses:**
  - `200`: 
  - `401`: 
  - `403`: 

### GET `/user/keys`

**List the authenticated user's public keys**

**Parameters:**
  - `fingerprint` [query] *string*: fingerprint of the key
  - `page` [query] *integer*: page number of results to return (1-based)
  - `limit` [query] *integer*: page size of results

**Responses:**
  - `200`: 
  - `401`: 
  - `403`: 

### POST `/user/keys`

**Create a public key**

**Parameters:**
  - `body` [body] *any*: 

**Request body** (`body`): 

**Responses:**
  - `201`: 
  - `401`: 
  - `403`: 
  - `422`: 

### DELETE `/user/keys/{id}`

**Delete a public key**

**Parameters:**
  - `id` [path] (required) *integer*: id of key to delete

**Responses:**
  - `204`: 
  - `401`: 
  - `403`: 
  - `404`: 

### GET `/user/keys/{id}`

**Get a public key**

**Parameters:**
  - `id` [path] (required) *integer*: id of key to get

**Responses:**
  - `200`: 
  - `401`: 
  - `403`: 
  - `404`: 

### GET `/user/list_blocked`

**List the authenticated user's blocked users**

**Parameters:**
  - `page` [query] *integer*: page number of results to return (1-based)
  - `limit` [query] *integer*: page size of results

**Responses:**
  - `200`: 
  - `401`: 
  - `403`: 

### GET `/user/quota`

**Get quota information for the authenticated user**

**Responses:**
  - `200`: 
  - `401`: 
  - `403`: 

### GET `/user/quota/artifacts`

**List the artifacts affecting the authenticated user's quota**

**Parameters:**
  - `page` [query] *integer*: page number of results to return (1-based)
  - `limit` [query] *integer*: page size of results

**Responses:**
  - `200`: 
  - `401`: 
  - `403`: 

### GET `/user/quota/attachments`

**List the attachments affecting the authenticated user's quota**

**Parameters:**
  - `page` [query] *integer*: page number of results to return (1-based)
  - `limit` [query] *integer*: page size of results

**Responses:**
  - `200`: 
  - `401`: 
  - `403`: 

### GET `/user/quota/check`

**Check if the authenticated user is over quota for a given subject**

**Parameters:**
  - `subject` [query] (required) *string*: subject of the quota

**Responses:**
  - `200`: Returns true if the action is accepted.
  - `401`: 
  - `403`: 
  - `422`: 

### GET `/user/quota/packages`

**List the packages affecting the authenticated user's quota**

**Parameters:**
  - `page` [query] *integer*: page number of results to return (1-based)
  - `limit` [query] *integer*: page size of results

**Responses:**
  - `200`: 
  - `401`: 
  - `403`: 

### GET `/user/repos`

**List the repos that the authenticated user owns**

**Parameters:**
  - `page` [query] *integer*: page number of results to return (1-based)
  - `limit` [query] *integer*: page size of results
  - `order_by` [query] *string*: order the repositories

**Responses:**
  - `200`: 
  - `401`: 
  - `403`: 
  - `422`: 

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

### GET `/user/settings`

**Get current user's account settings**

**Responses:**
  - `200`: 
  - `401`: 
  - `403`: 

### PATCH `/user/settings`

**Update settings in current user's account**

**Parameters:**
  - `body` [body] *any*: 

**Request body** (`body`): 

**Responses:**
  - `200`: 
  - `401`: 
  - `403`: 

### GET `/user/starred`

**The repos that the authenticated user has starred**

**Parameters:**
  - `page` [query] *integer*: page number of results to return (1-based)
  - `limit` [query] *integer*: page size of results

**Responses:**
  - `200`: 
  - `401`: 
  - `403`: 

### DELETE `/user/starred/{owner}/{repo}`

**Unstar the given repo**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo to unstar
  - `repo` [path] (required) *string*: name of the repo to unstar

**Responses:**
  - `204`: 
  - `401`: 
  - `403`: 
  - `404`: 

### GET `/user/starred/{owner}/{repo}`

**Whether the authenticated is starring the repo**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo

**Responses:**
  - `204`: 
  - `401`: 
  - `403`: 
  - `404`: 

### PUT `/user/starred/{owner}/{repo}`

**Star the given repo**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo to star
  - `repo` [path] (required) *string*: name of the repo to star

**Responses:**
  - `204`: 
  - `401`: 
  - `403`: 
  - `404`: 

### GET `/user/stopwatches`

**Get list of all existing stopwatches**

**Parameters:**
  - `page` [query] *integer*: page number of results to return (1-based)
  - `limit` [query] *integer*: page size of results

**Responses:**
  - `200`: 
  - `401`: 
  - `403`: 

### GET `/user/subscriptions`

**List repositories watched by the authenticated user**

**Parameters:**
  - `page` [query] *integer*: page number of results to return (1-based)
  - `limit` [query] *integer*: page size of results

**Responses:**
  - `200`: 
  - `401`: 
  - `403`: 

### GET `/user/teams`

**List all the teams a user belongs to**

**Parameters:**
  - `page` [query] *integer*: page number of results to return (1-based)
  - `limit` [query] *integer*: page size of results

**Responses:**
  - `200`: 
  - `401`: 
  - `403`: 

### GET `/user/times`

**List the current user's tracked times**

**Parameters:**
  - `page` [query] *integer*: page number of results to return (1-based)
  - `limit` [query] *integer*: page size of results
  - `since` [query] *string*: Only show times updated after the given time. This is a timestamp in RFC 3339 format
  - `before` [query] *string*: Only show times updated before the given time. This is a timestamp in RFC 3339 format

**Responses:**
  - `200`: 
  - `401`: 
  - `403`: 

### PUT `/user/unblock/{username}`

**Unblocks a user from the doer**

**Parameters:**
  - `username` [path] (required) *string*: username of the user

**Responses:**
  - `204`: 
  - `401`: 
  - `403`: 
  - `404`: 
  - `422`: 

### GET `/users/search`

**Search for users**

**Parameters:**
  - `q` [query] *string*: keyword
  - `uid` [query] *integer*: ID of the user to search for
  - `sort` [query] *string*: sort order of results
  - `page` [query] *integer*: page number of results to return (1-based)
  - `limit` [query] *integer*: page size of results

**Responses:**
  - `200`: SearchResults of a successful search

### GET `/users/{username}`

**Get a user**

**Parameters:**
  - `username` [path] (required) *string*: username of user to get

**Responses:**
  - `200`: 
  - `404`: 

### GET `/users/{username}/activities/feeds`

**List a user's activity feeds**

**Parameters:**
  - `username` [path] (required) *string*: username of user
  - `only-performed-by` [query] *boolean*: if true, only show actions performed by the requested user
  - `date` [query] *string*: the date of the activities to be found
  - `page` [query] *integer*: page number of results to return (1-based)
  - `limit` [query] *integer*: page size of results

**Responses:**
  - `200`: 
  - `404`: 

### GET `/users/{username}/followers`

**List the given user's followers**

**Parameters:**
  - `username` [path] (required) *string*: username of user
  - `page` [query] *integer*: page number of results to return (1-based)
  - `limit` [query] *integer*: page size of results

**Responses:**
  - `200`: 
  - `404`: 

### GET `/users/{username}/following`

**List the users that the given user is following**

**Parameters:**
  - `username` [path] (required) *string*: username of user
  - `page` [query] *integer*: page number of results to return (1-based)
  - `limit` [query] *integer*: page size of results

**Responses:**
  - `200`: 
  - `404`: 

### GET `/users/{username}/following/{target}`

**Check if one user is following another user**

**Parameters:**
  - `username` [path] (required) *string*: username of following user
  - `target` [path] (required) *string*: username of followed user

**Responses:**
  - `204`: 
  - `404`: 

### GET `/users/{username}/gpg_keys`

**List the given user's GPG keys**

**Parameters:**
  - `username` [path] (required) *string*: username of user
  - `page` [query] *integer*: page number of results to return (1-based)
  - `limit` [query] *integer*: page size of results

**Responses:**
  - `200`: 
  - `404`: 

### GET `/users/{username}/heatmap`

**Get a user's heatmap**

**Parameters:**
  - `username` [path] (required) *string*: username of user to get

**Responses:**
  - `200`: 
  - `404`: 

### GET `/users/{username}/keys`

**List the given user's public keys**

**Parameters:**
  - `username` [path] (required) *string*: username of user
  - `fingerprint` [query] *string*: fingerprint of the key
  - `page` [query] *integer*: page number of results to return (1-based)
  - `limit` [query] *integer*: page size of results

**Responses:**
  - `200`: 
  - `404`: 

### GET `/users/{username}/repos`

**List the repos owned by the given user**

**Parameters:**
  - `username` [path] (required) *string*: username of user
  - `page` [query] *integer*: page number of results to return (1-based)
  - `limit` [query] *integer*: page size of results

**Responses:**
  - `200`: 
  - `404`: 

### GET `/users/{username}/starred`

**The repos that the given user has starred**

**Parameters:**
  - `username` [path] (required) *string*: username of user
  - `page` [query] *integer*: page number of results to return (1-based)
  - `limit` [query] *integer*: page size of results

**Responses:**
  - `200`: 
  - `404`: 

### GET `/users/{username}/subscriptions`

**List the repositories watched by a user**

**Parameters:**
  - `username` [path] (required) *string*: username of the user
  - `page` [query] *integer*: page number of results to return (1-based)
  - `limit` [query] *integer*: page size of results

**Responses:**
  - `200`: 
  - `404`: 

### GET `/users/{username}/tokens`

**List the specified user's access tokens**

**Parameters:**
  - `username` [path] (required) *string*: username of user
  - `page` [query] *integer*: page number of results to return (1-based)
  - `limit` [query] *integer*: page size of results

**Responses:**
  - `200`: 
  - `403`: 
  - `404`: 

### POST `/users/{username}/tokens`

**Generate an access token for the specified user**

**Parameters:**
  - `username` [path] (required) *string*: username of user
  - `body` [body] *any*: 

**Request body** (`body`): 

**Responses:**
  - `201`: 
  - `400`: 
  - `403`: 
  - `404`: 

### DELETE `/users/{username}/tokens/{token}`

**Delete an access token from the specified user's account**

**Parameters:**
  - `username` [path] (required) *string*: username of user
  - `token` [path] (required) *string*: token to be deleted, identified by ID and if not available by name

**Responses:**
  - `204`: 
  - `403`: 
  - `404`: 
  - `422`: 
