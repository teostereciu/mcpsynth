# Time entry

*Source: https://docs.clockify.me/#tag/Time%20entry*

---

## Add a new time entry

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

workspaceIdrequired| string Example:  64a687e29ae1f428e7ebe303Represents a workspace identifier across the system.
---|---

##### Request Body schema: application/json

required

billable| boolean Default:  false Indicates whether a time entry is billable or not.
---|---
customAttributes| Array of objects (CreateCustomAttributeRequest)  [ 0 .. 10 ] items  Represents a list of create custom field request objects.
customFields| Array of objects (UpdateCustomFieldRequest)  [ 0 .. 50 ] items  Represents a list of value objects for user’s custom fields.
description| string <= 3000 characters  Represents time entry description.
end| string <date-time> Represents an end date in yyyy-MM-ddThh:mm:ssZ format.
projectId| string Represents a project identifier across the system.
start| string <date-time> Represents a start date in yyyy-MM-ddThh:mm:ssZ format.
tagIds| Array of strings Represents a list of tag ids.
taskId| string Represents a task identifier across the system.
type| string Enum: "REGULAR" "BREAK" Valid time entry type.

### Responses

**201**

Created

## Mark time entries as invoiced

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

workspaceIdrequired| string Example:  64a687e29ae1f428e7ebe303Represents a workspace identifier across the system.
---|---

##### Request Body schema: application/json

required

invoicedrequired| boolean Default:  false Indicates whether time entry is invoiced or not.
---|---
timeEntryIdsrequired| Array of objects (TimeEntryId)  non-empty  unique  Represents a list of invoiced time entry ids

### Responses

**200**

OK

## Get all in progress time entries on a workspace

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

workspaceIdrequired| string
---|---

##### query Parameters

page| integer <int32> >= 1  Default:  1
---|---
page-size| integer <int32> [ 1 .. 1000 ]  Default:  10

### Responses

**200**

OK

## Delete a time entry from a workspace

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

workspaceIdrequired| string Example:  64a687e29ae1f428e7ebe303Represents a workspace identifier across the system.
---|---
idrequired| string Example:  64c777ddd3fcab07cfbb210cRepresents a time entry identifier across the system.

### Responses

**204**

No Content

## Get a specific time entry on a workspace

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

workspaceIdrequired| string Example:  64a687e29ae1f428e7ebe303Represents a workspace identifier across the system.
---|---
idrequired| string Example:  64c777ddd3fcab07cfbb210cRepresents a time entry identifier across the system.

##### query Parameters

hydrated| boolean Default:  false Flag to set whether to include additional information of a time entry or not.
---|---

### Responses

**200**

OK

## Update time entry on a workspace

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

workspaceIdrequired| string Example:  64a687e29ae1f428e7ebe303Represents a workspace identifier across the system.
---|---
idrequired| string Example:  64c777ddd3fcab07cfbb210cRepresents a time entry identifier across the system.

##### Request Body schema: application/json

required

billable| boolean Default:  false Indicates whether a time entry is billable or not.
---|---
customFields| Array of objects (UpdateCustomFieldRequest)  [ 0 .. 50 ] items  Represents a list of value objects for user’s custom fields.
description| string [ 0 .. 3000 ] characters  Represents time entry description.
end| string <date-time> Represents an end date in yyyy-MM-ddThh:mm:ssZ format.
projectId| string Represents a project identifier across the system.
startrequired| string <date-time> Represents a start date in yyyy-MM-ddThh:mm:ssZ format.
tagIds| Array of strings Represents a list of tag ids.
taskId| string Represents a task identifier across the system.
type| string Enum: "REGULAR" "BREAK"

### Responses

**200**

OK

## Delete all time entries for a user on a workspace

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

workspaceIdrequired| string Example:  64a687e29ae1f428e7ebe303Represents a workspace identifier across the system.
---|---
userIdrequired| string Example:  5a0ab5acb07987125438b60fRepresents a user identifier across the system.

##### query Parameters

time-entry-idsrequired| Array of strings Example:  time-entry-ids=5a0ab5acb07987125438b60fRepresents a list of time entry ids to delete.
---|---

### Responses

**200**

OK

## Get time entries for a user on a workspace

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

workspaceIdrequired| string Example:  64a687e29ae1f428e7ebe303Represents a workspace identifier across the system.
---|---
userIdrequired| string Example:  5a0ab5acb07987125438b60fRepresents a user identifier across the system.

##### query Parameters

description| string Example:  description=Description keywordsRepresents a term for searching time entries by description.
---|---
start| string Example:  start=2020-01-01T00:00:00ZRepresents a start date in the yyyy-MM-ddThh:mm:ssZ format.
end| string Example:  end=2021-01-01T00:00:00ZRepresents an end date in the yyyy-MM-ddThh:mm:ssZ format.
project| string Example:  project=5b641568b07987035750505eIf provided, you'll get a filtered list of time entries that matches the provided string in their project id.
task| string Example:  task=64c777ddd3fcab07cfbb210cIf provided, you'll get a filtered list of time entries that matches the provided string in their task id.
tags| Array of strings unique  Example:  tags=5e4117fe8c625f38930d57b7&tags=7e4117fe8c625f38930d57b8If provided, you'll get a filtered list of time entries that matches the provided string(s) in their tag id(s).
project-required| boolean Default:  false Flag to set whether to only get time entries which have a project.
task-required| boolean Default:  false Flag to set whether to only get time entries which have tasks.
hydrated| boolean Default:  false Flag to set whether to include additional information on time entries or not.
page| integer <int32> Default:  1 Example:  page=1Page number.
page-size| integer <int32> >= 1  Default:  50 Example:  page-size=50Page size.
in-progress| string Flag to set whether to filter only in progress time entries.
get-week-before| string Example:  get-week-before=2020-01-01T00:00:00ZValid yyyy-MM-ddThh:mm:ssZ format date. If provided, filters results within the week before the datetime provided and only those entries with assigned project or task.

### Responses

**200**

OK

## Stop a currently running timer on a workspace for a user

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

workspaceIdrequired| string Example:  64a687e29ae1f428e7ebe303Represents a workspace identifier across the system.
---|---
userIdrequired| string Example:  5a0ab5acb07987125438b60fRepresents a user identifier across the system.

##### Request Body schema: application/json

required

endrequired| string <date-time> Represents an end date in the yyyy-MM-ddThh:mm:ssZ format.
---|---

### Responses

**200**

OK

## Add a new time entry for another user on workspace

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

workspaceIdrequired| string Example:  64a687e29ae1f428e7ebe303Represents a workspace identifier across the system.
---|---
userIdrequired| string Example:  5a0ab5acb07987125438b60fRepresents a user identifier across the system.

##### query Parameters

from-entry| string Example:  from-entry=64c777ddd3fcab07cfbb210cRepresents a time entry identifier across the system.
---|---

##### Request Body schema: application/json

required

billable| boolean Default:  false Indicates whether a time entry is billable or not.
---|---
customAttributes| Array of objects (CreateCustomAttributeRequest)  [ 0 .. 10 ] items  Represents a list of create custom field request objects.
customFields| Array of objects (UpdateCustomFieldRequest)  [ 0 .. 50 ] items  Represents a list of value objects for user’s custom fields.
description| string <= 3000 characters  Represents time entry description.
end| string <date-time> Represents an end date in yyyy-MM-ddThh:mm:ssZ format.
projectId| string Represents a project identifier across the system.
start| string <date-time> Represents a start date in yyyy-MM-ddThh:mm:ssZ format.
tagIds| Array of strings Represents a list of tag ids.
taskId| string Represents a task identifier across the system.
type| string Enum: "REGULAR" "BREAK" Valid time entry type.

### Responses

**201**

Created

## Bulk edit time entries

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

workspaceIdrequired| string Example:  64a687e29ae1f428e7ebe303Represents a workspace identifier across the system.
---|---
userIdrequired| string Example:  5a0ab5acb07987125438b60fRepresents a user identifier across the system.

##### query Parameters

hydrated| boolean Default:  false If set to true, results will contain additional information about the time entry.
---|---

##### Request Body schema: application/json

required

Array (non-empty)

billable| boolean Default:  false Indicates whether a time entry is billable or not.
---|---
customFields| Array of objects (UpdateCustomFieldRequest)  [ 0 .. 50 ] items
description| string [ 0 .. 3000 ] characters  Represents a time entry description.
end| string <date-time> Represents an end date in the yyyy-MM-ddThh:mm:ssZ format.
idrequired| string non-empty  Represents a time entry identifier across the system.
projectId| string Represents a project identifier across the system.
start| string <date-time> Represents a start date in the yyyy-MM-ddThh:mm:ssZ format.
tagIds| Array of strings Represents a list of tag ids.
taskId| string Represents a task identifier across the system.
type| string Enum: "REGULAR" "BREAK"

### Responses

**200**

OK

## Duplicate a time entry

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

workspaceIdrequired| string Example:  64a687e29ae1f428e7ebe303Represents a workspace identifier across the system.
---|---
userIdrequired| string Example:  5a0ab5acb07987125438b60fRepresents a user identifier across the system.
idrequired| string Example:  8j39fn9307hh5125439g2astRepresents a time entry identifier across the system.

### Responses

**201**

Created