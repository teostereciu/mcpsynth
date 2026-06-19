# Policy

*Source: https://docs.clockify.me/#tag/Policy*

---

## Get policies on a workspace

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

workspaceIdrequired| string Example:  60f91b3ffdaf031696ec61a8Represents a workspace identifier across the system.
---|---

##### query Parameters

page| string <= 1000  Page number.
---|---
page-size| integer <int32> [ 1 .. 200 ]  Default:  50 Example:  page-size=50Page size.
name| string Example:  name=HolidaysIf provided, you'll get a filtered list of policies that contain the provided string in their name.
status| string Enum: "ACTIVE" "ARCHIVED" "ALL" Example:  status=ACTIVEIf provided, you'll get a filtered list of policies with the corresponding status.
sort-column| string Default:  "DEFAULT_SORT"
sort-order| string Default:  "ASCENDING"

### Responses

**200**

OK

## Create a time off policy

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

workspaceIdrequired| string Example:  60f91b3ffdaf031696ec61a8Represents a workspace identifier across the system.
---|---

##### Request Body schema: application/json

required

allowHalfDay| boolean Default:  false Indicates whether policy allows half days.
---|---
allowNegativeBalance| boolean Default:  false Indicates whether policy allows negative balances.
approverequired| object (PolicyApprovalDto)  Represents approval settings.
archived| boolean Default:  false Indicates whether policy is archived.
automaticAccrual| object (AutomaticAccrualRequest)  Provide automatic accrual settings.
automaticTimeEntryCreation| object (AutomaticTimeEntryCreationRequest)  Provides automatic time entry creation settings.
color| string^#(?:[0-9a-fA-F]{6}){1}$ Provide color in format ^#(?:[0-9a-fA-F]{6}){1}$. Explanation: A valid color code should start with '#' and consist of six hexadecimal characters, representing a color in hexadecimal format. Color value is in standard RGB hexadecimal format.
everyoneIncludingNew| boolean Default:  false Indicates whether the policy is to be applied to future new users.
hasExpiration| boolean Default:  false Indicates whether the policy balance should have expiration
icon| string Enum: "UMBRELLA" "SNOWFLAKE" "FAMILY" "PLANE" "STETHOSCOPE" "HEALTH_METRICS" "CHILDCARE" "LUGGAGE" "MONETIZATION" "CALENDAR" Provide icon.
namerequired| string [ 2 .. 100 ] characters  Represents a name of new policy.
negativeBalance| object (NegativeBalanceRequest)  Provide the negative balance data you would like to use for updating the policy.
timeUnit| string Enum: "DAYS" "HOURS" Indicates time unit of the policy.
userGroups| object (UserGroupIdsSchema)  Provide list with user group ids and corresponding status.
users| object (UserIdsSchema)  Provide list with user ids and corresponding status.

### Responses

**201**

Created

## Delete a policy

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

workspaceIdrequired| string Example:  60f91b3ffdaf031696ec61a8Represents a workspace identifier across the system.
---|---
idrequired| string Example:  63034cd0cb0fb876a57e93adRepresents a policy identifier across the system.

### Responses

**200**

OK

## Get a time off policy

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

workspaceIdrequired| string Example:  60f91b3ffdaf031696ec61a8Represents a workspace identifier across the system.
---|---
idrequired| string Example:  63034cd0cb0fb876a57e93adRepresents a policy identifier across the system.

### Responses

**200**

OK

## Change a policy status

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

workspaceIdrequired| string Example:  60f91b3ffdaf031696ec61a8Represents a workspace identifier across the system.
---|---
idrequired| string Example:  63034cd0cb0fb876a57e93adRepresents a policy identifier across the system.

##### Request Body schema: application/json

required

statusrequired| string Enum: "ACTIVE" "ARCHIVED" "ALL" Provide the status you would like to use for changing the policy.
---|---

### Responses

**200**

OK

## Update a policy

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

workspaceIdrequired| string Example:  60f91b3ffdaf031696ec61a8Represents a workspace identifier across the system.
---|---
idrequired| string Example:  63034cd0cb0fb876a57e93adRepresents a policy identifier across the system.

##### Request Body schema: application/json

required

allowHalfDayrequired| boolean Default:  false Indicates whether policy allows half day.
---|---
allowNegativeBalancerequired| boolean Default:  false Indicates whether policy allows negative balance.
approverequired| object (PolicyApprovalDto)  Represents approval settings.
archivedrequired| boolean Default:  false Indicates whether policy is archived.
automaticAccrual| object (AutomaticAccrualRequest)  Provide automatic accrual settings.
automaticTimeEntryCreation| object (AutomaticTimeEntryCreationRequest)  Provides automatic time entry creation settings.
color| string^#(?:[0-9a-fA-F]{6}){1}$ Provide color in format ^#(?:[0-9a-fA-F]{6}){1}$. Explanation: A valid color code should start with '#' and consist of six hexadecimal characters, representing a color in hexadecimal format. Color value is in standard RGB hexadecimal format.
everyoneIncludingNewrequired| boolean Default:  false Indicates whether the policy is shown to new users.
hasExpirationrequired| boolean Default:  false Indicates whether the policy has expiration.
icon| string Enum: "UMBRELLA" "SNOWFLAKE" "FAMILY" "PLANE" "STETHOSCOPE" "HEALTH_METRICS" "CHILDCARE" "LUGGAGE" "MONETIZATION" "CALENDAR" Provide icon.
namerequired| string [ 2 .. 100 ] characters  Provide the name you would like to use for updating the policy.
negativeBalance| object (NegativeBalanceRequest)  Provide the negative balance data you would like to use for updating the policy.
userGroupsrequired| object (UserGroupIdsSchema)  Provide list with user group ids and corresponding status.
usersrequired| object (UserIdsSchema)  Provide list with user ids and corresponding status.

### Responses

**200**

OK