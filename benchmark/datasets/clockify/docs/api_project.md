# Project

*Source: https://docs.clockify.me/#tag/Project*

---

## Get all projects on a workspace

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

workspaceIdrequired| string Example:  64a687e29ae1f428e7ebe303Represents a workspace identifier across the system.
---|---

##### query Parameters

name| string Example:  name=Software DevelopmentIf provided, you'll get a filtered list of projects that contains the provided string in the project name.
---|---
strict-name-search| boolean Default:  false Flag to toggle on/off strict search mode. When set to true, search by name will only return projects whose name exactly matches the string value given for the 'name' parameter. When set to false, results will also include projects whose name contain the string value, but could be longer than the string value itself. For example, if there is a project with the name 'applications', and the search value is 'app', setting strict-name-search to true will not return that project in the results, whereas setting it to false will.
archived| boolean Default:  false If provided and set to true, you'll only get archived projects. If omitted, you'll get both archived and non-archived projects.
billable| boolean Default:  false If provided and set to true, you'll only get billable projects. If omitted, you'll get both billable and non-billable projects.
clients| Array of strings unique  Example:  clients=5a0ab5acb07987125438b60f&clients=64c777ddd3fcab07cfbb210cIf provided, you'll get a filtered list of projects that contain clients which match any of the provided ids.
contains-client| boolean Default:  true If set to true, you'll get a filtered list of projects that contain clients which match the provided id(s) in 'clients' field. If set to false, you'll get a filtered list of projects which do NOT contain clients that match the provided id(s) in 'clients' field.
client-status| string Enum: "ACTIVE" "ARCHIVED" "ALL" Example:  client-status=ACTIVEFilters projects based on client status provided.
users| Array of strings unique  Example:  users=5a0ab5acb07987125438b60f&users=64c777ddd3fcab07cfbb210cIf provided, you'll get a filtered list of projects that contain users which match any of the provided ids.
contains-user| boolean Default:  true If set to true, you'll get a filtered list of projects that contain users which match the provided id(s) in 'users' field. If set to false, you'll get a filtered list of projects which do NOT contain users which match the provided id(s) in 'users' field.
user-status| string Enum: "PENDING" "ACTIVE" "DECLINED" "INACTIVE" "ALL" Example:  user-status=ALLFilters projects based on user status provided.
is-template| boolean Default:  false Filters projects based on whether they are used as a template or not.
sort-column| string Enum: "ID" "NAME" "CLIENT_NAME" "DURATION" "BUDGET" "PROGRESS" Example:  sort-column=NAMESorts the results by the given column/field.
sort-order| string Enum: "ASCENDING" "DESCENDING" Example:  sort-order=ASCENDINGSorting mode.
hydrated| boolean Default:  false If set to true, results will contain additional information about the project.
page| integer <int32> Default:  1 Example:  page=1Page number.
page-size| integer <int32> >= 1  Default:  50 Example:  page-size=50Page size.
access| string Enum: "PUBLIC" "PRIVATE" Example:  access=PUBLICValid set of string(s). If provided, you'll get a filtered list of projects that matches the provided access.
expense-limit| integer <int32> Default:  20 Example:  expense-limit=10Represents the maximum number of expenses to fetch.
expense-date| string Example:  expense-date=2024-12-31If provided, you will get expenses dated before the provided value in yyyy-MM-dd format.
userGroups| Array of strings unique  Example:  userGroups=5a0ab5acb07987125438b60f&userGroups=64c777ddd3fcab07cfbb210cIf provided, you'll get a filtered list of projects that contain groups which match any of the provided ids.
contains-group| boolean Default:  true If set to true, you'll get a filtered list of projects that contain groups which match the provided id(s) in 'userGroups' field. If set to false, you'll get a filtered list of projects which do NOT contain groups which match the provided id(s) in 'userGroups' field.

### Responses

**200**

OK

## Add a new project

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

workspaceIdrequired| string Example:  64a687e29ae1f428e7ebe303Represents a workspace identifier across the system.
---|---

##### Request Body schema: application/json

required

billable| boolean Default:  false Indicates whether project is billable or not.
---|---
clientId| string Represents client identifier across the system.
color| string^#(?:[0-9a-fA-F]{6}){1}$ Color format ^#(?:[0-9a-fA-F]{6}){1}$. Explanation: A valid color code should start with '#' and consist of six hexadecimal characters, representing a color in hexadecimal format. Color value is in standard RGB hexadecimal format.
costRate| object (CostRateRequestV1)
estimate| object (EstimateRequest)  Represents an estimate request object.
hourlyRate| object (HourlyRateRequestV1)
isPublic| boolean Default:  false Indicates whether project is public or not.
memberships| Array of objects (MembershipRequest)  Represents a list of membership request objects.
namerequired| string [ 2 .. 250 ] characters  Represents a project name.
note| string <= 16384 characters  Represents project note.
tasks| Array of objects (TaskRequest)  Represents a list of task request objects.

### Responses

**201**

Created

## Create project from a template

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

workspaceIdrequired| string Example:  64a687e29ae1f428e7ebe303Represents a workspace identifier across the system.
---|---

##### Request Body schema: application/json

required

clientId| string Represents a client identifier across the system.
---|---
color| string^#(?:[0-9a-fA-F]{6}){1}$ Color format ^#(?:[0-9a-fA-F]{6}){1}$. Explanation: A valid color code should start with '#' and consist of six hexadecimal characters, representing a color in hexadecimal format. Color value is in standard RGB hexadecimal format.
isPublic| boolean Default:  false Indicates whether the project is public or not.
namerequired| string [ 2 .. 250 ] characters  Represents a project name.
templateProjectIdrequired| string non-empty  Represents a project identifier across the system.

### Responses

**200**

OK

## Delete a project from a workspace

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

workspaceIdrequired| string Example:  64a687e29ae1f428e7ebe303Represents a workspace identifier across the system.
---|---
projectIdrequired| string Example:  5b641568b07987035750505eRepresents a project identifier across the system.

### Responses

**200**

OK

## Find a project by ID

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

workspaceIdrequired| string Example:  64a687e29ae1f428e7ebe303Represents a workspace identifier across the system.
---|---
projectIdrequired| string Example:  5b641568b07987035750505eRepresents a project identifier across the system.

##### query Parameters

hydrated| boolean Default:  false If set to true, results will contain additional information about the project
---|---
custom-field-entity-type| string Default:  "TIMEENTRY" Example:  custom-field-entity-type=TIMEENTRYIf provided, you'll get a filtered list of custom fields that matches the provided string with the custom field entity type.
expense-limit| integer <int32> Default:  20 Example:  expense-limit=10Represents the maximum number of expenses to fetch.
expense-date| string Example:  expense-date=2024-12-31If provided, you will get expenses dated before the provided value in yyyy-MM-dd format.

### Responses

**200**

OK

## Update a project on a workspace

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

workspaceIdrequired| string Example:  64a687e29ae1f428e7ebe303Represents a workspace identifier across the system.
---|---
projectIdrequired| string Example:  5b641568b07987035750505eRepresents a project identifier across the system.

##### Request Body schema: application/json

required

archived| boolean Default:  false Indicates whether project is archived or not.
---|---
billable| boolean Default:  false Indicates whether project is billable or not.
clientId| string Represents client identifier across the system.
color| string^#(?:[0-9a-fA-F]{6}){1}$ Color format ^#(?:[0-9a-fA-F]{6}){1}$. Explanation: A valid color code should start with '#' and consist of six hexadecimal characters, representing a color in hexadecimal format. Color value is in standard RGB hexadecimal format.
costRate| object (CostRateRequestV1)
hourlyRate| object (HourlyRateRequestV1)
isPublic| boolean Default:  false Indicates whether project is public or not.
name| string [ 2 .. 250 ] characters  Represents a project name.
note| string <= 16384 characters  Represents project note.

### Responses

**200**

OK

## Update project estimate

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

workspaceIdrequired| string Example:  64a687e29ae1f428e7ebe303Represents a workspace identifier across the system.
---|---
projectIdrequired| string Example:  5b641568b07987035750505eRepresents a project identifier across the system.

##### Request Body schema: application/json

required

budgetEstimate| object (EstimateWithOptionsRequest)  Represents estimate with options request object.
---|---
estimateReset| object (EstimateResetRequest)  Represents estimate reset request object.
timeEstimate| object (TimeEstimateRequest)  Represents project time estimate request object.

### Responses

**200**

OK

## Update project memberships

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

workspaceIdrequired| string Example:  64a687e29ae1f428e7ebe303Represents a workspace identifier across the system.
---|---
projectIdrequired| string Example:  5b641568b07987035750505eRepresents a project identifier across the system.

##### Request Body schema: application/json

required

membershipsrequired| Array of objects (UserIdWithRatesRequest)  Represents a list of users with id and rates request objects.
---|---
userGroups| object (UserGroupIdsSchema)  Provide list with user group ids and corresponding status.

### Responses

**200**

OK

## Assign/remove users to/from the project

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

workspaceIdrequired| string Example:  64a687e29ae1f428e7ebe303Represents a workspace identifier across the system.
---|---
projectIdrequired| string Example:  5b641568b07987035750505eRepresents a project identifier across the system.

##### Request Body schema: application/json

required

remove| boolean Default:  false Setting this flag to 'true' will remove the given users from the project.
---|---
userGroups| object (UserGroupIdsSchema)  Provide list with user group ids and corresponding status.
userIds| Array of strings Represents array of user ids which should be added/removed.

### Responses

**200**

OK

## Update a project template

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

workspaceIdrequired| string Example:  64a687e29ae1f428e7ebe303Represents a workspace identifier across the system.
---|---
projectIdrequired| string Example:  5b641568b07987035750505eRepresents a project identifier across the system.

##### Request Body schema: application/json

required

isTemplate| boolean Default:  false Indicates whether project is a template or not.
---|---

### Responses

**200**

OK

## Update project user's cost rate

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

workspaceIdrequired| string Example:  64a687e29ae1f428e7ebe303Represents a workspace identifier across the system.
---|---
projectIdrequired| string Example:  5b641568b07987035750505eRepresents a project identifier across the system.
userIdrequired| string Example:  4a0ab5acb07987125438b60fRepresents a user identifier across the system.

##### Request Body schema: application/json

required

amountrequired| integer <int32> >= 0  Represents an amount as integer.
---|---
since| string Represents a date and time in yyyy-MM-ddThh:mm:ssZ format.

### Responses

**200**

OK

## Update a project user's billable rate

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

workspaceIdrequired| string Example:  64a687e29ae1f428e7ebe303Represents a workspace identifier across the system.
---|---
projectIdrequired| string Example:  5b641568b07987035750505eRepresents a project identifier across the system.
userIdrequired| string Example:  4a0ab5acb07987125438b60fRepresents a user identifier across the system.

##### Request Body schema: application/json

required

amountrequired| integer <int32> >= 0  Represents an amount as integer.
---|---
since| string Represents a date and time in yyyy-MM-ddThh:mm:ssZ format.

### Responses

**200**

OK