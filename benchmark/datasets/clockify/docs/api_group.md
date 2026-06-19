# Group

*Source: https://docs.clockify.me/#tag/Group*

---

## Find all groups on a workspace

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

workspaceIdrequired| string Example:  64a687e29ae1f428e7ebe303Represents a workspace identifier across the system.
---|---

##### query Parameters

project-id| string Example:  project-id=5a0ab5acb07987125438b60fIf provided, you'll get a filtered list of groups that matches the string provided in their project id.
---|---
name| string Example:  name=development_teamIf provided, you'll get a filtered list of groups that matches the string provided in their name.
sort-column| string Enum: "ID" "NAME" Example:  sort-column=NAMEColumn to be used as the sorting criteria.
sort-order| string Enum: "ASCENDING" "DESCENDING" Example:  sort-order=ASCENDINGSorting mode.
page| integer <int32> Default:  1 Example:  page=1Page number.
page-size| integer <int32> >= 1  Default:  50 Example:  page-size=50Page size.
includeTeamManagers| boolean Default:  false Example:  includeTeamManagers=trueIf provided, you'll get a list of team managers assigned to this user group.

### Responses

**200**

OK

## Add a new group

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

workspaceIdrequired| string Example:  64a687e29ae1f428e7ebe303Represents a workspace identifier across the system.
---|---

##### Request Body schema: application/json

required

name| string [ 0 .. 100 ] characters  Represents a user group name.
---|---

### Responses

**201**

Created

## Delete a group

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

workspaceIdrequired| string Example:  64a687e29ae1f428e7ebe303Represents a workspace identifier across the system.
---|---
idrequired| string Example:  76a687e29ae1f428e7ebe101Represents a user group identifier across the system.

### Responses

**200**

OK

## Update a group

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

idrequired| string Example:  76a687e29ae1f428e7ebe101Represents a user group identifier across the system.
---|---
workspaceIdrequired| string Example:  64a687e29ae1f428e7ebe303Represents a workspace identifier across the system.

##### Request Body schema: application/json

required

name| string [ 0 .. 100 ] characters  Represents a user group name.
---|---

### Responses

**200**

OK

## Add users to a group

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

workspaceIdrequired| string Example:  64a687e29ae1f428e7ebe303Represents a workspace identifier across the system.
---|---
userGroupIdrequired| string Example:  76a687e29ae1f428e7ebe101Represents a user group identifier across the system.

##### Request Body schema: application/json

required

userIdrequired| string Represents a user identifier across the system.
---|---

### Responses

**200**

OK

## Remove a user from a group

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

workspaceIdrequired| string Example:  64a687e29ae1f428e7ebe303Represents a workspace identifier across the system.
---|---
userGroupIdrequired| string Example:  76a687e29ae1f428e7ebe101Represents a user group identifier across the system.
userIdrequired| string Example:  5a0ab5acb07987125438b60fRepresents a user identifier across the system.

### Responses

**200**

OK