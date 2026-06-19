# Issue

*Source: https://codeberg.org/swagger.v1.json*

---

### GET `/repos/issues/search`

**Search for issues across the repositories that the user has access to**

**Parameters:**
  - `state` [query] *string*: State of the issue
  - `labels` [query] *string*: Comma-separated list of label names. Fetch only issues that have any of these labels. Non existent labels are discarded.
  - `milestones` [query] *string*: Comma-separated list of milestone names. Fetch only issues that have any of these milestones. Non existent milestones are discarded.
  - `q` [query] *string*: Search string
  - `priority_repo_id` [query] *integer*: Repository ID to prioritize in the results
  - `type` [query] *string*: Filter by issue type
  - `since` [query] *string*: Only show issues updated after the given time (RFC 3339 format)
  - `before` [query] *string*: Only show issues updated before the given time (RFC 3339 format)
  - `assigned` [query] *boolean*: Filter issues or pulls assigned to the authenticated user
  - `created` [query] *boolean*: Filter issues or pulls created by the authenticated user
  - `mentioned` [query] *boolean*: Filter issues or pulls mentioning the authenticated user
  - `review_requested` [query] *boolean*: Filter pull requests where the authenticated user's review was requested
  - `reviewed` [query] *boolean*: Filter pull requests reviewed by the authenticated user
  - `owner` [query] *string*: Filter by repository owner
  - `team` [query] *string*: Filter by team (requires organization owner parameter)
  - `page` [query] *integer*: Page number of results to return (1-based)
  - `limit` [query] *integer*: Number of items per page
  - `sort` [query] *string*: Type of sort

**Responses:**
  - `200`: 
  - `400`: 
  - `422`: 

### GET `/repos/{owner}/{repo}/issues`

**List a repository's issues**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `state` [query] *string*: whether issue is open or closed
  - `labels` [query] *string*: comma separated list of labels. Fetch only issues that have any of this labels. Non existent labels are discarded
  - `q` [query] *string*: search string
  - `type` [query] *string*: filter by type (issues / pulls) if set
  - `milestones` [query] *string*: comma separated list of milestone names or ids. It uses names and fall back to ids. Fetch only issues that have any of this milestones. Non existent milestones are discarded
  - `since` [query] *string*: Only show items updated after the given time. This is a timestamp in RFC 3339 format
  - `before` [query] *string*: Only show items updated before the given time. This is a timestamp in RFC 3339 format
  - `created_by` [query] *string*: Only show items which were created by the given user
  - `assigned_by` [query] *string*: Only show items for which the given user is assigned
  - `mentioned_by` [query] *string*: Only show items in which the given user was mentioned
  - `page` [query] *integer*: page number of results to return (1-based)
  - `limit` [query] *integer*: page size of results
  - `sort` [query] *string*: Type of sort

**Responses:**
  - `200`: 
  - `404`: 
  - `422`: 

### POST `/repos/{owner}/{repo}/issues`

**Create an issue. If using deadline only the date will be taken into account, and time of day ignored.**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `body` [body] *any*: 

**Request body** (`body`): 

**Responses:**
  - `201`: 
  - `403`: 
  - `404`: 
  - `412`: 
  - `422`: 
  - `423`: 

### GET `/repos/{owner}/{repo}/issues/comments`

**List all comments in a repository**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `since` [query] *string*: if provided, only comments updated since the provided time are returned.
  - `before` [query] *string*: if provided, only comments updated before the provided time are returned.
  - `page` [query] *integer*: page number of results to return (1-based)
  - `limit` [query] *integer*: page size of results

**Responses:**
  - `200`: 
  - `404`: 
  - `422`: 
  - `500`: 

### DELETE `/repos/{owner}/{repo}/issues/comments/{id}`

**Delete a comment**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `id` [path] (required) *integer*: id of comment to delete

**Responses:**
  - `204`: 
  - `403`: 
  - `500`: 

### GET `/repos/{owner}/{repo}/issues/comments/{id}`

**Get a comment**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `id` [path] (required) *integer*: id of the comment

**Responses:**
  - `200`: 
  - `204`: 
  - `403`: 
  - `404`: 
  - `500`: 

### PATCH `/repos/{owner}/{repo}/issues/comments/{id}`

**Edit a comment**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `id` [path] (required) *integer*: id of the comment to edit
  - `body` [body] *any*: 

**Request body** (`body`): 

**Responses:**
  - `200`: 
  - `204`: 
  - `403`: 
  - `404`: 
  - `423`: 
  - `500`: 

### GET `/repos/{owner}/{repo}/issues/comments/{id}/assets`

**List comment's attachments**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `id` [path] (required) *integer*: id of the comment

**Responses:**
  - `200`: 
  - `404`: 

### POST `/repos/{owner}/{repo}/issues/comments/{id}/assets`

**Create a comment attachment**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `id` [path] (required) *integer*: id of the comment
  - `name` [query] *string*: name of the attachment
  - `updated_at` [query] *string*: time of the attachment's creation. This is a timestamp in RFC 3339 format
  - `attachment` [formData] (required) *file*: attachment to upload

**Responses:**
  - `201`: 
  - `400`: 
  - `404`: 
  - `413`: 
  - `422`: 
  - `423`: 

### DELETE `/repos/{owner}/{repo}/issues/comments/{id}/assets/{attachment_id}`

**Delete a comment attachment**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `id` [path] (required) *integer*: id of the comment
  - `attachment_id` [path] (required) *integer*: id of the attachment to delete

**Responses:**
  - `204`: 
  - `404`: 
  - `423`: 

### GET `/repos/{owner}/{repo}/issues/comments/{id}/assets/{attachment_id}`

**Get a comment attachment**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `id` [path] (required) *integer*: id of the comment
  - `attachment_id` [path] (required) *integer*: id of the attachment to get

**Responses:**
  - `200`: 
  - `404`: 

### PATCH `/repos/{owner}/{repo}/issues/comments/{id}/assets/{attachment_id}`

**Edit a comment attachment**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `id` [path] (required) *integer*: id of the comment
  - `attachment_id` [path] (required) *integer*: id of the attachment to edit
  - `body` [body] *any*: 

**Request body** (`body`): 

**Responses:**
  - `201`: 
  - `404`: 
  - `413`: 
  - `423`: 

### DELETE `/repos/{owner}/{repo}/issues/comments/{id}/reactions`

**Remove a reaction from a comment of an issue**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `id` [path] (required) *integer*: id of the comment to edit
  - `content` [body] *any*: 

**Request body** (`content`): 

**Responses:**
  - `200`: 
  - `403`: 
  - `404`: 

### GET `/repos/{owner}/{repo}/issues/comments/{id}/reactions`

**Get a list of reactions from a comment of an issue**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `id` [path] (required) *integer*: id of the comment to edit

**Responses:**
  - `200`: 
  - `403`: 
  - `404`: 

### POST `/repos/{owner}/{repo}/issues/comments/{id}/reactions`

**Add a reaction to a comment of an issue**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `id` [path] (required) *integer*: id of the comment to edit
  - `content` [body] *any*: 

**Request body** (`content`): 

**Responses:**
  - `200`: 
  - `201`: 
  - `403`: 
  - `404`: 

### DELETE `/repos/{owner}/{repo}/issues/{index}`

**Delete an issue**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `index` [path] (required) *integer*: index of issue to delete

**Responses:**
  - `204`: 
  - `403`: 
  - `404`: 

### GET `/repos/{owner}/{repo}/issues/{index}`

**Get an issue**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `index` [path] (required) *integer*: index of the issue to get

**Responses:**
  - `200`: 
  - `404`: 

### PATCH `/repos/{owner}/{repo}/issues/{index}`

**Edit an issue. If using deadline only the date will be taken into account, and time of day ignored.**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `index` [path] (required) *integer*: index of the issue to edit
  - `body` [body] *any*: 

**Request body** (`body`): 

**Responses:**
  - `201`: 
  - `403`: 
  - `404`: 
  - `412`: 

### GET `/repos/{owner}/{repo}/issues/{index}/assets`

**List issue's attachments**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `index` [path] (required) *integer*: index of the issue

**Responses:**
  - `200`: 
  - `404`: 

### POST `/repos/{owner}/{repo}/issues/{index}/assets`

**Create an issue attachment**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `index` [path] (required) *integer*: index of the issue
  - `name` [query] *string*: name of the attachment
  - `updated_at` [query] *string*: time of the attachment's creation. This is a timestamp in RFC 3339 format
  - `attachment` [formData] (required) *file*: attachment to upload

**Responses:**
  - `201`: 
  - `400`: 
  - `404`: 
  - `413`: 
  - `422`: 
  - `423`: 

### DELETE `/repos/{owner}/{repo}/issues/{index}/assets/{attachment_id}`

**Delete an issue attachment**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `index` [path] (required) *integer*: index of the issue
  - `attachment_id` [path] (required) *integer*: id of the attachment to delete

**Responses:**
  - `204`: 
  - `404`: 
  - `423`: 

### GET `/repos/{owner}/{repo}/issues/{index}/assets/{attachment_id}`

**Get an issue attachment**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `index` [path] (required) *integer*: index of the issue
  - `attachment_id` [path] (required) *integer*: id of the attachment to get

**Responses:**
  - `200`: 
  - `404`: 

### PATCH `/repos/{owner}/{repo}/issues/{index}/assets/{attachment_id}`

**Edit an issue attachment**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `index` [path] (required) *integer*: index of the issue
  - `attachment_id` [path] (required) *integer*: id of the attachment to edit
  - `body` [body] *any*: 

**Request body** (`body`): 

**Responses:**
  - `201`: 
  - `404`: 
  - `413`: 
  - `423`: 

### DELETE `/repos/{owner}/{repo}/issues/{index}/blocks`

**Unblock the issue given in the body by the issue in path**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `index` [path] (required) *integer*: index of the issue
  - `body` [body] *any*: 

**Request body** (`body`): 

**Responses:**
  - `200`: 
  - `404`: 

### GET `/repos/{owner}/{repo}/issues/{index}/blocks`

**List issues that are blocked by this issue**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `index` [path] (required) *integer*: index of the issue
  - `page` [query] *integer*: page number of results to return (1-based)
  - `limit` [query] *integer*: page size of results

**Responses:**
  - `200`: 
  - `404`: 

### POST `/repos/{owner}/{repo}/issues/{index}/blocks`

**Block the issue given in the body by the issue in path**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `index` [path] (required) *integer*: index of the issue
  - `body` [body] *any*: 

**Request body** (`body`): 

**Responses:**
  - `201`: 
  - `404`: the issue does not exist

### GET `/repos/{owner}/{repo}/issues/{index}/comments`

**List all comments on an issue**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `index` [path] (required) *integer*: index of the issue
  - `since` [query] *string*: if provided, only comments updated since the specified time are returned.
  - `before` [query] *string*: if provided, only comments updated before the provided time are returned.

**Responses:**
  - `200`: 
  - `404`: 
  - `422`: 
  - `500`: 

### POST `/repos/{owner}/{repo}/issues/{index}/comments`

**Add a comment to an issue**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `index` [path] (required) *integer*: index of the issue
  - `body` [body] *any*: 

**Request body** (`body`): 

**Responses:**
  - `201`: 
  - `403`: 
  - `404`: 
  - `423`: 
  - `500`: 

### DELETE `/repos/{owner}/{repo}/issues/{index}/comments/{id}`

**Delete a comment**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `index` [path] (required) *integer*: this parameter is ignored
  - `id` [path] (required) *integer*: id of comment to delete

**Responses:**
  - `204`: 
  - `403`: 
  - `500`: 

### PATCH `/repos/{owner}/{repo}/issues/{index}/comments/{id}`

**Edit a comment**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `index` [path] (required) *integer*: this parameter is ignored
  - `id` [path] (required) *integer*: id of the comment to edit
  - `body` [body] *any*: 

**Request body** (`body`): 

**Responses:**
  - `200`: 
  - `204`: 
  - `403`: 
  - `404`: 
  - `500`: 

### POST `/repos/{owner}/{repo}/issues/{index}/deadline`

**Set an issue deadline. If set to null, the deadline is deleted. If using deadline only the date will be taken into account, and time of day ignored.**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `index` [path] (required) *integer*: index of the issue to create or update a deadline on
  - `body` [body] *any*: 

**Request body** (`body`): 

**Responses:**
  - `201`: 
  - `403`: 
  - `404`: 

### DELETE `/repos/{owner}/{repo}/issues/{index}/dependencies`

**Remove an issue dependency**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `index` [path] (required) *integer*: index of the issue
  - `body` [body] *any*: 

**Request body** (`body`): 

**Responses:**
  - `200`: 
  - `404`: 
  - `423`: 

### GET `/repos/{owner}/{repo}/issues/{index}/dependencies`

**List an issue's dependencies, i.e all issues that block this issue.**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `index` [path] (required) *integer*: index of the issue
  - `page` [query] *integer*: page number of results to return (1-based)
  - `limit` [query] *integer*: page size of results

**Responses:**
  - `200`: 
  - `404`: 

### POST `/repos/{owner}/{repo}/issues/{index}/dependencies`

**Make the issue in the url depend on the issue in the form.**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `index` [path] (required) *integer*: index of the issue
  - `body` [body] *any*: 

**Request body** (`body`): 

**Responses:**
  - `201`: 
  - `404`: the issue does not exist
  - `423`: 

### DELETE `/repos/{owner}/{repo}/issues/{index}/labels`

**Remove all labels from an issue**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `index` [path] (required) *integer*: index of the issue
  - `body` [body] *any*: 

**Request body** (`body`): 

**Responses:**
  - `204`: 
  - `403`: 
  - `404`: 

### GET `/repos/{owner}/{repo}/issues/{index}/labels`

**Get an issue's labels**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `index` [path] (required) *integer*: index of the issue

**Responses:**
  - `200`: 
  - `404`: 

### POST `/repos/{owner}/{repo}/issues/{index}/labels`

**Add a label to an issue**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `index` [path] (required) *integer*: index of the issue
  - `body` [body] *any*: 

**Request body** (`body`): 

**Responses:**
  - `200`: 
  - `403`: 
  - `404`: 

### PUT `/repos/{owner}/{repo}/issues/{index}/labels`

**Replace an issue's labels**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `index` [path] (required) *integer*: index of the issue
  - `body` [body] *any*: 

**Request body** (`body`): 

**Responses:**
  - `200`: 
  - `403`: 
  - `404`: 

### DELETE `/repos/{owner}/{repo}/issues/{index}/labels/{identifier}`

**Remove a label from an issue**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `index` [path] (required) *integer*: index of the issue
  - `identifier` [path] (required) *string*: name or id of the label to remove
  - `body` [body] *any*: 

**Request body** (`body`): 

**Responses:**
  - `204`: 
  - `403`: 
  - `404`: 
  - `422`: 

### DELETE `/repos/{owner}/{repo}/issues/{index}/pin`

**Unpin an Issue**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `index` [path] (required) *integer*: index of issue to unpin

**Responses:**
  - `204`: 
  - `403`: 
  - `404`: 

### POST `/repos/{owner}/{repo}/issues/{index}/pin`

**Pin an Issue**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `index` [path] (required) *integer*: index of issue to pin

**Responses:**
  - `204`: 
  - `403`: 
  - `404`: 

### PATCH `/repos/{owner}/{repo}/issues/{index}/pin/{position}`

**Moves the Pin to the given Position**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `index` [path] (required) *integer*: index of issue
  - `position` [path] (required) *integer*: the new position

**Responses:**
  - `204`: 
  - `403`: 
  - `404`: 

### DELETE `/repos/{owner}/{repo}/issues/{index}/reactions`

**Remove a reaction from an issue**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `index` [path] (required) *integer*: index of the issue
  - `content` [body] *any*: 

**Request body** (`content`): 

**Responses:**
  - `200`: 
  - `403`: 
  - `404`: 

### GET `/repos/{owner}/{repo}/issues/{index}/reactions`

**Get a list reactions of an issue**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `index` [path] (required) *integer*: index of the issue
  - `page` [query] *integer*: page number of results to return (1-based)
  - `limit` [query] *integer*: page size of results

**Responses:**
  - `200`: 
  - `403`: 
  - `404`: 

### POST `/repos/{owner}/{repo}/issues/{index}/reactions`

**Add a reaction to an issue**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `index` [path] (required) *integer*: index of the issue
  - `content` [body] *any*: 

**Request body** (`content`): 

**Responses:**
  - `200`: 
  - `201`: 
  - `403`: 
  - `404`: 

### DELETE `/repos/{owner}/{repo}/issues/{index}/stopwatch/delete`

**Delete an issue's existing stopwatch.**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `index` [path] (required) *integer*: index of the issue to stop the stopwatch on

**Responses:**
  - `204`: 
  - `403`: Not repo writer, user does not have rights to toggle stopwatch
  - `404`: 
  - `409`: Cannot cancel a non existent stopwatch

### POST `/repos/{owner}/{repo}/issues/{index}/stopwatch/start`

**Start stopwatch on an issue.**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `index` [path] (required) *integer*: index of the issue to create the stopwatch on

**Responses:**
  - `201`: 
  - `403`: Not repo writer, user does not have rights to toggle stopwatch
  - `404`: 
  - `409`: Cannot start a stopwatch again if it already exists

### POST `/repos/{owner}/{repo}/issues/{index}/stopwatch/stop`

**Stop an issue's existing stopwatch.**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `index` [path] (required) *integer*: index of the issue to stop the stopwatch on

**Responses:**
  - `201`: 
  - `403`: Not repo writer, user does not have rights to toggle stopwatch
  - `404`: 
  - `409`: Cannot stop a non existent stopwatch

### GET `/repos/{owner}/{repo}/issues/{index}/subscriptions`

**Get users who subscribed on an issue.**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `index` [path] (required) *integer*: index of the issue
  - `page` [query] *integer*: page number of results to return (1-based)
  - `limit` [query] *integer*: page size of results

**Responses:**
  - `200`: 
  - `404`: 

### GET `/repos/{owner}/{repo}/issues/{index}/subscriptions/check`

**Check if user is subscribed to an issue**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `index` [path] (required) *integer*: index of the issue

**Responses:**
  - `200`: 
  - `404`: 

### DELETE `/repos/{owner}/{repo}/issues/{index}/subscriptions/{user}`

**Unsubscribe user from issue**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `index` [path] (required) *integer*: index of the issue
  - `user` [path] (required) *string*: user witch unsubscribe

**Responses:**
  - `200`: Already unsubscribed
  - `201`: Successfully Unsubscribed
  - `304`: User can only subscribe itself if he is no admin
  - `404`: 

### PUT `/repos/{owner}/{repo}/issues/{index}/subscriptions/{user}`

**Subscribe user to issue**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `index` [path] (required) *integer*: index of the issue
  - `user` [path] (required) *string*: user to subscribe

**Responses:**
  - `200`: Already subscribed
  - `201`: Successfully Subscribed
  - `304`: User can only subscribe itself if he is no admin
  - `404`: 

### GET `/repos/{owner}/{repo}/issues/{index}/timeline`

**List all comments and events on an issue**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `index` [path] (required) *integer*: index of the issue
  - `since` [query] *string*: if provided, only comments updated since the specified time are returned.
  - `page` [query] *integer*: page number of results to return (1-based)
  - `limit` [query] *integer*: page size of results
  - `before` [query] *string*: if provided, only comments updated before the provided time are returned.

**Responses:**
  - `200`: 
  - `404`: 
  - `422`: 
  - `500`: 

### DELETE `/repos/{owner}/{repo}/issues/{index}/times`

**Reset a tracked time of an issue**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `index` [path] (required) *integer*: index of the issue to add tracked time to

**Responses:**
  - `204`: 
  - `400`: 
  - `403`: 
  - `404`: 

### GET `/repos/{owner}/{repo}/issues/{index}/times`

**List an issue's tracked times**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `index` [path] (required) *integer*: index of the issue
  - `user` [query] *string*: optional filter by user (available for issue managers)
  - `since` [query] *string*: Only show times updated after the given time. This is a timestamp in RFC 3339 format
  - `before` [query] *string*: Only show times updated before the given time. This is a timestamp in RFC 3339 format
  - `page` [query] *integer*: page number of results to return (1-based)
  - `limit` [query] *integer*: page size of results

**Responses:**
  - `200`: 
  - `403`: 
  - `404`: 
  - `422`: 

### POST `/repos/{owner}/{repo}/issues/{index}/times`

**Add tracked time to a issue**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `index` [path] (required) *integer*: index of the issue
  - `body` [body] *any*: 

**Request body** (`body`): 

**Responses:**
  - `200`: 
  - `400`: 
  - `403`: 
  - `404`: 

### DELETE `/repos/{owner}/{repo}/issues/{index}/times/{id}`

**Delete specific tracked time**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `index` [path] (required) *integer*: index of the issue
  - `id` [path] (required) *integer*: id of time to delete

**Responses:**
  - `204`: 
  - `400`: 
  - `403`: 
  - `404`: 

### GET `/repos/{owner}/{repo}/labels`

**Get all of a repository's labels**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `sort` [query] *string*: Specifies the sorting method: mostissues, leastissues, or reversealphabetically.
  - `page` [query] *integer*: page number of results to return (1-based)
  - `limit` [query] *integer*: page size of results

**Responses:**
  - `200`: 
  - `404`: 

### POST `/repos/{owner}/{repo}/labels`

**Create a label**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `body` [body] *any*: 

**Request body** (`body`): 

**Responses:**
  - `201`: 
  - `404`: 
  - `422`: 

### DELETE `/repos/{owner}/{repo}/labels/{id}`

**Delete a label**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `id` [path] (required) *integer*: id of the label to delete

**Responses:**
  - `204`: 
  - `404`: 

### GET `/repos/{owner}/{repo}/labels/{id}`

**Get a single label**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `id` [path] (required) *integer*: id of the label to get

**Responses:**
  - `200`: 
  - `404`: 

### PATCH `/repos/{owner}/{repo}/labels/{id}`

**Update a label**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `id` [path] (required) *integer*: id of the label to edit
  - `body` [body] *any*: 

**Request body** (`body`): 

**Responses:**
  - `200`: 
  - `404`: 
  - `422`: 

### GET `/repos/{owner}/{repo}/milestones`

**Get all of a repository's opened milestones**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `state` [query] *string*: Milestone state, Recognized values are open, closed and all. Defaults to "open"
  - `name` [query] *string*: filter by milestone name
  - `page` [query] *integer*: page number of results to return (1-based)
  - `limit` [query] *integer*: page size of results

**Responses:**
  - `200`: 
  - `404`: 

### POST `/repos/{owner}/{repo}/milestones`

**Create a milestone**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `body` [body] *any*: 

**Request body** (`body`): 

**Responses:**
  - `201`: 
  - `404`: 

### DELETE `/repos/{owner}/{repo}/milestones/{id}`

**Delete a milestone**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `id` [path] (required) *integer*: the milestone to delete, identified by ID and if not available by name

**Responses:**
  - `204`: 
  - `404`: 

### GET `/repos/{owner}/{repo}/milestones/{id}`

**Get a milestone**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `id` [path] (required) *integer*: the milestone to get, identified by ID and if not available by name

**Responses:**
  - `200`: 
  - `404`: 

### PATCH `/repos/{owner}/{repo}/milestones/{id}`

**Update a milestone**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `id` [path] (required) *integer*: the milestone to edit, identified by ID and if not available by name
  - `body` [body] *any*: 

**Request body** (`body`): 

**Responses:**
  - `200`: 
  - `404`: 
