# Time Off

*Source: https://docs.clockify.me/#tag/Time%20Off*

---

## Create a time off request

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

workspaceIdrequired| string Example:  60f91b3ffdaf031696ec61a8Represents a workspace identifier across the system.
---|---
policyIdrequired| string Example:  63034cd0cb0fb876a57e93adRepresents a policy identifier across the system.

##### Request Body schema: application/json

required

note| string Provide the note you would like to use for creating the time off request.
---|---
timeOffPeriodrequired| object (TimeOffRequestPeriodV1Request)  Provide the period you would like to use for creating the time off request. If `timeZone` isn't set, should be aligned with time zone for user in settings. Can be shifted from user time zone with explicit setting of `timeZone`.

### Responses

**200**

OK

## Delete a time off request

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

workspaceIdrequired| string Example:  60f91b3ffdaf031696ec61a8Represents a workspace identifier across the system.
---|---
policyIdrequired| string Example:  63034cd0cb0fb876a57e93adRepresents a policy identifier across the system.
requestIdrequired| string Example:  6308850156b7d75ea8fd3fbdRepresents a time off request identifier across the system.

### Responses

**200**

OK

## Change a time off request status

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

workspaceIdrequired| string Example:  60f91b3ffdaf031696ec61a8Represents a workspace identifier across the system.
---|---
policyIdrequired| string Example:  63034cd0cb0fb876a57e93adRepresents a policy identifier across the system.
requestIdrequired| string Example:  6308850156b7d75ea8fd3fbdRepresents a time off request identifier across the system.

##### Request Body schema: application/json

required

note| string Provide the note you would like to use for changing the time off request.
---|---
status| string Enum: "APPROVED" "REJECTED" Provide the status you would like to use for changing the time off request.

### Responses

**200**

OK

## Create a time off request for a user

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

workspaceIdrequired| string Example:  60f91b3ffdaf031696ec61a8Represents a workspace identifier across the system.
---|---
policyIdrequired| string Example:  63034cd0cb0fb876a57e93adRepresents a policy identifier across the system.
userIdrequired| string Example:  60f924bafdaf031696ec6218Represents a user identifier across the system.

##### Request Body schema: application/json

required

note| string Provide the note you would like to use for creating the time off request.
---|---
timeOffPeriodrequired| object (TimeOffRequestPeriodV1Request)  Provide the period you would like to use for creating the time off request. If `timeZone` isn't set, should be aligned with time zone for user in settings. Can be shifted from user time zone with explicit setting of `timeZone`.

### Responses

**200**

OK

## Get all time off requests on a workspace

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

workspaceIdrequired| string Example:  60f91b3ffdaf031696ec61a8Represents a workspace identifier across the system.
---|---

##### Request Body schema: application/json

required

end| string <date-time> Return time off requests created before the specified time in requester's time zone. Provide end in format YYYY-MM-DDTHH:MM:SS.ssssssZ
---|---
page| integer <int32> <= 1000  Default:  1 Page number.
pageSize| integer <int32> [ 1 .. 200 ]  Default:  50 Page size.
start| string <date-time> Return time off requests created after the specified time in requester's time zone. Provide start in format YYYY-MM-DDTHH:MM:SS.ssssssZ
statuses| Array of strings unique Items Enum: "PENDING" "APPROVED" "REJECTED" "ALL" Filters time off requests by status.
userGroups| Array of strings unique  Provide the user group ids of time off requests.
users| Array of strings unique  Provide the user ids of time off requests. If empty, will return time off requests of all users (with a maximum of 5000 users).

### Responses

**200**

OK