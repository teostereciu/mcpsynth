# Task

*Source: https://docs.clockify.me/#tag/Task*

---

## Find tasks on a project

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

projectIdrequired| string Example:  25b687e29ae1f428e7ebe123Represents a project identifier across the system.
---|---
workspaceIdrequired| string Example:  64a687e29ae1f428e7ebe303Represents a workspace identifier across the system.

##### query Parameters

name| string Example:  name=BugfixingIf provided, you'll get a filtered list of tasks that matches the provided string in their name.
---|---
strict-name-search| boolean Default:  false Flag to toggle on/off strict search mode. When set to true, search by name only will return tasks whose name exactly matches the string value given for the 'name' parameter. When set to false, results will also include tasks whose name contain the string value, but could be longer than the string value itself. For example, if there is a task with the name 'applications', and the search value is 'app', setting strict-name-search to true will not return that task in the results, whereas setting it to false will.
is-active| boolean Default:  false Filters search results whether task is active or not.
page| integer <int32> Default:  1 Example:  page=1Page number.
page-size| integer <int32> >= 1  Default:  50 Example:  page-size=50Page size.
sort-column| string Enum: "ID" "NAME" Example:  sort-column=IDRepresents the column as criteria for sorting tasks.
sort-order| string Enum: "ASCENDING" "DESCENDING" Example:  sort-order=ASCENDINGSorting mode.

### Responses

**200**

OK

## Add a new task on a project

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

projectIdrequired| string Example:  25b687e29ae1f428e7ebe123Represents a project identifier across the system.
---|---
workspaceIdrequired| string Example:  64a687e29ae1f428e7ebe303Represents a workspace identifier across the system.

##### query Parameters

contains-assignee| boolean Default:  true Flag to set whether task will have assignee or none.
---|---

##### Request Body schema: application/json

required

assigneeId| string Deprecated
---|---
assigneeIds| Array of strings unique  Represents list of assignee ids for the task.
budgetEstimate| integer <int64> >= 0  Represents a task budget estimate as long.
estimate| string Represents a task duration estimate in ISO-8601 format.
id| string Represents task identifier across the system.
namerequired| string [ 1 .. 1000 ] characters  Represents task name.
status| string Enum: "ACTIVE" "DONE" "ALL" Represents task status.
userGroupIds| Array of strings unique  Represents list of user group ids for the task.

### Responses

**201**

Created

## Update a task's cost rate

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

projectIdrequired| string Example:  25b687e29ae1f428e7ebe123Represents a project identifier across the system.
---|---
workspaceIdrequired| string Example:  64a687e29ae1f428e7ebe303Represents a workspace identifier across the system.
idrequired| string Example:  57a687e29ae1f428e7ebe107Represents a task identifier across the system.

##### Request Body schema: application/json

required

amountrequired| integer <int32> >= 0  Represents an amount as integer.
---|---
since| string Represents a date and time in yyyy-MM-ddThh:mm:ssZ format.

### Responses

**200**

OK

## Update a task's billable rate

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

projectIdrequired| string Example:  25b687e29ae1f428e7ebe123Represents a project identifier across the system.
---|---
workspaceIdrequired| string Example:  64a687e29ae1f428e7ebe303Represents a workspace identifier across the system.
idrequired| string Example:  57a687e29ae1f428e7ebe107Represents a task identifier across the system.

##### Request Body schema: application/json

required

amountrequired| integer <int32> >= 0  Represents an hourly rate amount as integer.
---|---
since| string Represents a date and time in yyyy-MM-ddThh:mm:ssZ format.

### Responses

**200**

OK

## Delete a task from a project

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

taskIdrequired| string Example:  57a687e29ae1f428e7ebe107Represents a task identifier across the system.
---|---
workspaceIdrequired| string Example:  64a687e29ae1f428e7ebe303Represents a workspace identifier across the system.
projectIdrequired| string Example:  25b687e29ae1f428e7ebe123Represents a project identifier across the system.

### Responses

**200**

OK

## Get a task by id

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

taskIdrequired| string Example:  57a687e29ae1f428e7ebe107Represents a task identifier across the system.
---|---
projectIdrequired| string Example:  25b687e29ae1f428e7ebe123Represents a project identifier across the system.
workspaceIdrequired| string Example:  64a687e29ae1f428e7ebe303Represents a workspace identifier across the system.

### Responses

**200**

OK

## Update a task on a project

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

taskIdrequired| string Example:  57a687e29ae1f428e7ebe107Represents a task identifier across the system.
---|---
workspaceIdrequired| string Example:  64a687e29ae1f428e7ebe303Represents a workspace identifier across the system.
projectIdrequired| string Example:  25b687e29ae1f428e7ebe123Represents a project identifier across the system.

##### query Parameters

contains-assignee| boolean Default:  true Flag to set whether task will have assignee or none.
---|---
membership-status| string Enum: "PENDING" "ACTIVE" "DECLINED" "INACTIVE" "ALL" Example:  membership-status=ACTIVERepresents a membership status.

##### Request Body schema: application/json

required

assigneeId| string Deprecated
---|---
assigneeIds| Array of strings unique  Represents list of assignee ids for the task.
billable| boolean Default:  false Indicates whether a task is billable or not.
budgetEstimate| integer <int64> >= 0  Represents a task budget estimate as integer.
estimate| string Represents a task duration estimate.
namerequired| string [ 1 .. 1000 ] characters  Represents task name.
status| string Enum: "ACTIVE" "DONE" "ALL" Represents task status.
userGroupIds| Array of strings unique  Represents list of user group ids for the task.

### Responses

**200**

OK