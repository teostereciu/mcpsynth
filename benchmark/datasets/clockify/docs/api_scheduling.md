# Scheduling

*Source: https://docs.clockify.me/#tag/Scheduling*

---

## Get all assignments

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

workspaceIdrequired| string Example:  64a687e29ae1f428e7ebe303Represents a workspace identifier across the system.
---|---

##### query Parameters

name| string Default:  "" Example:  name=BugfixingIf provided, assignments will be filtered by name
---|---
startrequired| string Example:  start=2020-01-01T00:00:00ZRepresents a start date in the yyyy-MM-ddThh:mm:ssZ format.
endrequired| string Example:  end=2021-01-01T00:00:00ZRepresents a start date in the yyyy-MM-ddThh:mm:ssZ format.
sort-column| string Enum: "PROJECT" "USER" "ID" Example:  sort-column=USERRepresents the column as the sorting criteria.
sort-order| string Enum: "ASCENDING" "DESCENDING" Example:  sort-order=ASCENDINGRepresents the sorting mode.
page| integer <int32> Default:  1 Example:  page=1Page number.
page-size| integer <int32> >= 1  Default:  50 Example:  page-size=50Page size.

### Responses

**200**

OK

## Get all scheduled assignments per project

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

workspaceIdrequired| string Example:  64a687e29ae1f428e7ebe303Represents a workspace identifier across the system.
---|---

##### Request Body schema: application/json

required

endrequired| string <date-time> Represents an end date in the yyyy-MM-ddThh:mm:ssZ format.
---|---
page| integer <int32> Default:  1 Page number.
pageSize| integer <int32> <= 200  Default:  50 Page size.
search| string Represents a term for searching projects and clients by name.
startrequired| string <date-time> Represents a start date in the yyyy-MM-ddThh:mm:ssZ format.
statusFilter| string Enum: "PUBLISHED" "UNPUBLISHED" "ALL" Filters assignments by status.

### Responses

**200**

OK

## Get all scheduled assignments on project

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

workspaceIdrequired| string Example:  64a687e29ae1f428e7ebe303Represents a workspace identifier across the system.
---|---
projectIdrequired| string Example:  56b687e29ae1f428e7ebe504Represents a project identifier across the system.

##### query Parameters

startrequired| string Example:  start=2020-01-01T00:00:00ZRepresents a start date in the yyyy-MM-ddThh:mm:ssZ format.
---|---
endrequired| string Example:  end=2021-01-01T00:00:00ZRepresents an end date in the yyyy-MM-ddThh:mm:ssZ format.

### Responses

**200**

OK

## Publish assignments

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

workspaceIdrequired| string Example:  64a687e29ae1f428e7ebe303Represents a workspace identifier across the system.
---|---

##### Request Body schema: application/json

required

endrequired| string Represents end date in yyyy-MM-ddThh:mm:ssZ format.
---|---
notifyUsers| boolean Default:  false Indicates whether to notify users when assignment is published.
search| string Represents a search string.
startrequired| string Represents start date in yyyy-MM-ddThh:mm:ssZ format.
userFilter| object (ContainsUsersFilterRequestV1)  Represents a user filter request object.
userGroupFilter| object (ContainsUserGroupFilterRequestV1)  Represents a user group filter request object.
viewType| string Enum: "PROJECTS" "TEAM" "ALL" Represents view type.

### Responses

**200**

OK

## Create a recurring assignment

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

workspaceIdrequired| string Example:  64a687e29ae1f428e7ebe303Represents a workspace identifier across the system.
---|---

##### Request Body schema: application/json

required

billable| boolean Default:  false Indicates whether assignment is billable or not.
---|---
endrequired| string Represents an end date in the yyyy-MM-ddThh:mm:ssZ format.
hoursPerDayrequired| number <double> Represents assignment total hours per day.
includeNonWorkingDays| boolean Default:  false Indicates whether to include non-working days or not.
note| string [ 0 .. 100 ] characters  Represents an assignment note.
projectIdrequired| string non-empty  Represents a project identifier across the system.
recurringAssignment| object (RecurringAssignmentRequestV1)
startrequired| string Represents a start date in the yyyy-MM-ddThh:mm:ssZ format.
startTime| string Represents a start time in the hh:mm:ss format.
taskId| string Represents a task identifier across the system.
userIdrequired| string non-empty  Represents a user identifier across the system.

### Responses

**201**

Created

## Delete a recurring assignment

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

workspaceIdrequired| string Example:  64a687e29ae1f428e7ebe303Represents a workspace identifier across the system.
---|---
assignmentIdrequired| string Example:  5b641568b07987035750505eRepresents an assignment identifier across the system.

##### query Parameters

seriesUpdateOption| string Enum: "THIS_ONE" "THIS_AND_FOLLOWING" "ALL" Example:  seriesUpdateOption=ALLRepresents a series option.
---|---

### Responses

**200**

OK

## Update a recurring assignment

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

workspaceIdrequired| string Example:  64a687e29ae1f428e7ebe303Represents a workspace identifier across the system.
---|---
assignmentIdrequired| string Example:  5b641568b07987035750505eRepresents an assignment identifier across the system.

##### Request Body schema: application/json

required

billable| boolean Default:  false Indicates whether assignment is billable or not.
---|---
endrequired| string Represents an end date in the yyyy-MM-ddThh:mm:ssZ format.
hoursPerDay| number <double> Represents assignment total hours per day.
includeNonWorkingDays| boolean Default:  false Indicates whether to include non-working days or not.
note| string [ 0 .. 100 ] characters  Represents an assignment note.
seriesUpdateOption| string Enum: "THIS_ONE" "THIS_AND_FOLLOWING" "ALL" Valid series option
startrequired| string Represents start date in yyyy-MM-ddThh:mm:ssZ format.
startTime| string Represents a start time in the hh:mm:ss format.
taskId| string Represents task identifier across the system.

### Responses

**200**

OK

## Change the recurring period

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

workspaceIdrequired| string Example:  64a687e29ae1f428e7ebe303Represents a workspace identifier across the system.
---|---
assignmentIdrequired| string Example:  5b641568b07987035750505eRepresents an assignment identifier across the system.

##### Request Body schema: application/json

required

repeat| boolean Default:  false Indicates whether assignment is recurring or not.
---|---
weeksrequired| integer <int32> [ 1 .. 99 ]  Indicates number of weeks for assignment.

### Responses

**200**

OK

## Get total of users' capacity on workspace

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

workspaceIdrequired| string Example:  64a687e29ae1f428e7ebe303Represents a workspace identifier across the system.
---|---

##### Request Body schema: application/json

required

endrequired| string <date-time> Represents an end date in the yyyy-MM-ddThh:mm:ssZ format.
---|---
page| integer <int32> Default:  1 Page number.
pageSize| integer <int32> <= 200  Default:  50 Page size.
search| string Represents the keyword for searching users by name or email.
startrequired| string <date-time> Represents a start date in the yyyy-MM-ddThh:mm:ssZ format.
statusFilter| string Enum: "PUBLISHED" "UNPUBLISHED" "ALL" Filters assignments by status.
userFilter| object (ContainsUsersFilterRequestV1)  Represents a user filter request object.
userGroupFilter| object (ContainsUserGroupFilterRequestV1)  Represents a user group filter request object.

### Responses

**200**

OK

## Get total capacity of a user

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

workspaceIdrequired| string Example:  64a687e29ae1f428e7ebe303Represents a workspace identifier across the system.
---|---
userIdrequired| string Example:  5a0ab5acb07987125438b60fRepresents a user identifier across the system.

##### query Parameters

page| integer <int32> Default:  1 Example:  page=1Page number.
---|---
page-size| integer <int32> >= 1  Default:  50 Example:  page-size=50Page size.
startrequired| string Example:  start=2020-01-01T00:00:00ZRepresents a start date in the yyyy-MM-ddThh:mm:ssZ format.
endrequired| string Example:  end=2021-01-01T00:00:00ZRepresents an end date in the yyyy-MM-ddThh:mm:ssZ format.

### Responses

**200**

OK

## Copy a scheduled assignment

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

workspaceIdrequired| string Example:  64a687e29ae1f428e7ebe303Represents a workspace identifier across the system.
---|---
assignmentIdrequired| string Example:  5b641568b07987035750505eRepresents an assignment identifier across the system.

##### Request Body schema: application/json

required

seriesUpdateOption| string Enum: "THIS_ONE" "THIS_AND_FOLLOWING" "ALL" Represents a series update option.
---|---
userIdrequired| string Represents a user identifier across the system.

### Responses

**200**

OK