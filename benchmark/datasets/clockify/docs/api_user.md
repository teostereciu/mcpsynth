# User

*Source: https://docs.clockify.me/#tag/User*

---

## Add a photo

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### Request Body schema: multipart/form-data

filerequired| string <binary> Image to be uploaded
---|---

### Responses

**200**

OK

post/v1/file/image

https://api.clockify.me/api/v1/file/image

###  Response samples

  * 200


Content type

application/json

Copy

`{

  * "name": "image-01234567.jpg",

  * "url": "<https://clockify.com/image-01234567.jpg>"


}`

## Get currently logged-in user's info

##### Authorizations:

_MarketplaceKeyAuth_ _ApiKeyAuth_ _AddonKeyAuth_

##### query Parameters

include-memberships| boolean Default:  false Example:  include-memberships=trueIf set to true, memberships will be included.
---|---

### Responses

**200**

OK

## Get a member's profile

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

workspaceIdrequired| string Example:  64a687e29ae1f428e7ebe303Represents a workspace identifier across the system.
---|---
userIdrequired| string Example:  5a0ab5acb07987125438b60fRepresents a user identifier across the system.

### Responses

**200**

OK

## Update a member's profile

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

workspaceIdrequired| string Example:  64a687e29ae1f428e7ebe303Represents a workspace identifier across the system.
---|---
userIdrequired| string Example:  5a0ab5acb07987125438b60fRepresents a user identifier across the system.

##### Request Body schema: application/json

required

imageUrl| string Represents an image url. A field that can only be updated for limited users.
---|---
name| string [ 1 .. 100 ] characters  Deprecated  This body field is deprecated and can only be updated for limited users. Represents name of the user and can be changed on the CAKE.com Account profile page.
removeProfileImage| boolean Default:  false Indicates whether to remove profile image or not. A field that can only be updated for limited users.
userCustomFields| Array of objects (UpsertUserCustomFieldRequest)  Represents a list of upsert user custom field objects.
weekStart| string Enum: "MONDAY" "TUESDAY" "WEDNESDAY" "THURSDAY" "FRIDAY" "SATURDAY" "SUNDAY" Represents a day of the week.
workCapacity| string Represents work capacity as a time duration in the ISO-8601 format. For example, for a 7hr work day, input should be PT7H.
workingDays| string Enum: "MONDAY" "TUESDAY" "WEDNESDAY" "THURSDAY" "FRIDAY" "SATURDAY" "SUNDAY" Represents a list of days of the week.

### Responses

**200**

OK

## Find all users on a workspace

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

workspaceIdrequired| string Example:  64a687e29ae1f428e7ebe303Represents a workspace identifier across the system.
---|---

##### query Parameters

email| string Example:  email=mail@example.comIf provided, you'll get a filtered list of users that contain the provided string in their email address.
---|---
project-id| string Example:  project-id=21a687e29ae1f428e7ebe606If provided, you'll get a list of users that have access to the project.
status| string Enum: "PENDING" "ACTIVE" "DECLINED" "INACTIVE" "ALL" Example:  status=ACTIVEIf provided, you'll get a filtered list of users with the corresponding status.
account-statuses| string Example:  account-statuses=LIMITEDIf provided, you'll get a filtered list of users with the corresponding account status filter. If not, this will only filter ACTIVE, PENDING_EMAIL_VERIFICATION, and NOT_REGISTERED Users.
name| string Example:  name=JohnIf provided, you'll get a filtered list of users that contain the provided string in their name
sort-column| string Enum: "ID" "EMAIL" "NAME" "NAME_LOWERCASE" "ACCESS" "HOURLYRATE" "COSTRATE" Example:  sort-column=IDSorting column criteria. Default value: EMAIL
sort-order| string Enum: "ASCENDING" "DESCENDING" Example:  sort-order=ASCENDINGSorting mode. Default value: ASCENDING
page| integer <int32> Default:  1 Example:  page=1Page number.
page-size| integer <int32> >= 1  Default:  50 Example:  page-size=50Page size.
memberships| string Enum: "ALL" "NONE" "WORKSPACE" "PROJECT" "USERGROUP" Example:  memberships=WORKSPACEIf provided, you'll get all users along with workspaces, groups, or projects they have access to. Default value is NONE.
include-rolesrequired| string Default:  "false" If you pass along includeRoles=true, you'll get each user's detailed manager role (including projects and members which they manage)

### Responses

**200**

OK

## Filter workspace users

##### Authorizations:

_MarketplaceKeyAuth_ _ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

workspaceIdrequired| string Example:  64a687e29ae1f428e7ebe303Represents a workspace identifier across the system.
---|---

##### Request Body schema: application/json

required

accountStatuses| Array of strings unique  If provided, you'll get a filtered list of users with the corresponding account status filter. If not, this will only filter ACTIVE, PENDING_EMAIL_VERIFICATION, and NOT_REGISTERED Users.
---|---
email| string If provided, you'll get a filtered list of users that contain the provided string in their email address.
includeRoles| boolean Default:  false If you pass along includeRoles=true, you'll get each user's detailed manager role (including projects and members for whom they're managers)
memberships| string Default:  "NONE" Enum: "ALL" "NONE" "WORKSPACE" "PROJECT" "USERGROUP" If provided, you'll get all users along with workspaces, groups, or projects they have access to.
name| string If provided, you'll get a filtered list of users that contain the provided string in their name.
page| integer <int32> Default:  1 Page number.
pageSize| integer <int32> >= 1  Default:  50 Page size.
projectId| string If provided, you'll get a list of users that have access to the project.
roles| Array of strings unique Items Enum: "WORKSPACE_ADMIN" "OWNER" "TEAM_MANAGER" "PROJECT_MANAGER" If provided, you'll get a filtered list of users that have any of the specified roles. Owners are counted as admins when filtering.
sortColumn| string Enum: "ID" "EMAIL" "NAME" "NAME_LOWERCASE" "ACCESS" "HOURLYRATE" "COSTRATE" Sorting criteria
sortOrder| string Enum: "ASCENDING" "DESCENDING" Sorting mode
status| string Enum: "PENDING" "ACTIVE" "DECLINED" "INACTIVE" "ALL" If provided, you'll get a filtered list of users with the corresponding status.
userGroups| Array of strings unique  If provided, you'll get a list of users that belong to the specified user group IDs.

### Responses

**200**

OK

## Update a user's custom field

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

workspaceIdrequired| string Example:  64a687e29ae1f428e7ebe303Represents a workspace identifier across the system.
---|---
userIdrequired| string Example:  5a0ab5acb07987125438b60fRepresents a user identifier across the system.
customFieldIdrequired| string Example:  5e4117fe8c625f38930d57b7Represents custom field identifier across the system.

##### Request Body schema: application/json

required

value| object Represents custom field value.
---|---

### Responses

**201**

Created

## Find user's team manager

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

workspaceIdrequired| string Example:  64a687e29ae1f428e7ebe303Represents a workspace identifier across the system.
---|---
userIdrequired| string Example:  5a0ab5acb07987125438b60fRepresents a user identifier across the system.

##### query Parameters

sort-column| string Enum: "ID" "EMAIL" "NAME" "NAME_LOWERCASE" "ACCESS" "HOURLYRATE" "COSTRATE" Example:  sort-column=IDSorting column criteria
---|---
sort-order| string Enum: "ASCENDING" "DESCENDING" Example:  sort-order=ASCENDINGSorting mode
page| integer <int32> Default:  1 Example:  page=1Page number.
page-size| integer <int32> >= 1  Default:  50 Example:  page-size=50Page size.

### Responses

**200**

OK

## Remove user's manager role

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

workspaceIdrequired| string Example:  64a687e29ae1f428e7ebe303Represents a workspace identifier across the system.
---|---
userIdrequired| string Example:  5a0ab5acb07987125438b60fRepresents a user identifier across the system.

##### Request Body schema: application/json

required

entityIdrequired| string non-empty  Represents an entity identifier across the system.
---|---
rolerequired| string Enum: "WORKSPACE_ADMIN" "TEAM_MANAGER" "PROJECT_MANAGER" Represents a valid role.
sourceType| string Value: "USER_GROUP" Optional field used to indicate that the target of the operation is a user group, in which case the value USER_GROUP should be used, alongside a valid user group ID for the entityId field. If omitted, a user ID should be used for the entityId field.

### Responses

**204**

No Content

## Give manager role to a user

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

workspaceIdrequired| string Example:  64a687e29ae1f428e7ebe303Represents a workspace identifier across the system.
---|---
userIdrequired| string Example:  5a0ab5acb07987125438b60fRepresents a user identifier across the system.

##### Request Body schema: application/json

required

entityIdrequired| string non-empty  Represents an entity identifier across the system.
---|---
rolerequired| string Enum: "WORKSPACE_ADMIN" "TEAM_MANAGER" "PROJECT_MANAGER" Represents a valid role.
sourceType| string Value: "USER_GROUP" Optional field used to indicate that the target of the operation is a user group, in which case the value USER_GROUP should be used, alongside a valid user group ID for the entityId field. If omitted, a user ID should be used for the entityId field.

### Responses

**201**

Created