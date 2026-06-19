# Notification

*Source: https://codeberg.org/swagger.v1.json*

---

### GET `/notifications`

**List users's notification threads**

**Parameters:**
  - `all` [query] *boolean*: If true, show notifications marked as read. Default value is false
  - `status-types` [query] *array*: Show notifications with the provided status types. Options are: unread, read and/or pinned. Defaults to unread & pinned.
  - `subject-type` [query] *array*: filter notifications by subject type
  - `since` [query] *string*: Only show notifications updated after the given time. This is a timestamp in RFC 3339 format
  - `before` [query] *string*: Only show notifications updated before the given time. This is a timestamp in RFC 3339 format
  - `page` [query] *integer*: page number of results to return (1-based)
  - `limit` [query] *integer*: page size of results

**Responses:**
  - `200`: 

### PUT `/notifications`

**Mark notification threads as read, pinned or unread**

**Parameters:**
  - `last_read_at` [query] *string*: Describes the last point that notifications were checked. Anything updated since this time will not be updated.
  - `all` [query] *boolean*: If true, mark all notifications on this repo. Default value is false
  - `status-types` [query] *array*: Mark notifications with the provided status types. Options are: unread, read and/or pinned. Defaults to unread.
  - `to-status` [query] *string*: Status to mark notifications as, Defaults to read.

**Responses:**
  - `205`: 

### GET `/notifications/new`

**Check if unread notifications exist**

**Responses:**
  - `200`: 

### GET `/notifications/threads/{id}`

**Get notification thread by ID**

**Parameters:**
  - `id` [path] (required) *integer*: id of notification thread

**Responses:**
  - `200`: 
  - `403`: 
  - `404`: 

### PATCH `/notifications/threads/{id}`

**Mark notification thread as read by ID**

**Parameters:**
  - `id` [path] (required) *integer*: id of notification thread
  - `to-status` [query] *string*: Status to mark notifications as

**Responses:**
  - `205`: 
  - `403`: 
  - `404`: 

### GET `/repos/{owner}/{repo}/notifications`

**List users's notification threads on a specific repo**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `all` [query] *boolean*: If true, show notifications marked as read. Default value is false
  - `status-types` [query] *array*: Show notifications with the provided status types. Options are: unread, read and/or pinned. Defaults to unread & pinned
  - `subject-type` [query] *array*: filter notifications by subject type
  - `since` [query] *string*: Only show notifications updated after the given time. This is a timestamp in RFC 3339 format
  - `before` [query] *string*: Only show notifications updated before the given time. This is a timestamp in RFC 3339 format
  - `page` [query] *integer*: page number of results to return (1-based)
  - `limit` [query] *integer*: page size of results

**Responses:**
  - `200`: 

### PUT `/repos/{owner}/{repo}/notifications`

**Mark notification threads as read, pinned or unread on a specific repo**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the repo
  - `repo` [path] (required) *string*: name of the repo
  - `all` [query] *boolean*: If true, mark all notifications on this repo. Default value is false
  - `status-types` [query] *array*: Mark notifications with the provided status types. Options are: unread, read and/or pinned. Defaults to unread.
  - `to-status` [query] *string*: Status to mark notifications as. Defaults to read.
  - `last_read_at` [query] *string*: Describes the last point that notifications were checked. Anything updated since this time will not be updated.

**Responses:**
  - `205`: 
