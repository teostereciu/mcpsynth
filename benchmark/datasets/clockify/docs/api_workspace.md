# Workspace

*Source: https://docs.clockify.me/#tag/Workspace*

---

## Get all my workspaces

##### Authorizations:

_MarketplaceKeyAuth_ _ApiKeyAuth_

##### query Parameters

roles| string Enum: "WORKSPACE_ADMIN" "OWNER" "TEAM_MANAGER" "PROJECT_MANAGER" Example:  roles=WORKSPACE_ADMIN&roles=OWNERIf provided, you'll get a filtered list of workspaces where you have any of the specified roles. Owners are not counted as admins when filtering.
---|---

### Responses

**200**

OK

## Add a workspace

##### Authorizations:

_ApiKeyAuth_

##### Request Body schema: application/json

required

name| string [ 1 .. 50 ] characters  Represents a workspace name.
---|---
organizationId| string Represents the Cake organization identifier across the system.

### Responses

**201**

Created

## Get workspace info

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

workspaceIdrequired| string Example:  64a687e29ae1f428e7ebe303Represents a workspace identifier across the system.
---|---

### Responses

**200**

OK

## Update workspace cost rate

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

workspaceIdrequired| string Example:  64a687e29ae1f428e7ebe303Represents a workspace identifier across the system.
---|---

##### Request Body schema: application/json

required

amountrequired| integer <int32> >= 0  Represents an amount as integer.
---|---
since| string Represents a date and time in yyyy-MM-ddThh:mm:ssZ format.

### Responses

**200**

OK

## Update workspace billable rate

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

workspaceIdrequired| string Example:  64a687e29ae1f428e7ebe303Represents a workspace identifier across the system.
---|---

##### Request Body schema: application/json

required

amountrequired| integer <int32> >= 0  Represents an amount as integer.
---|---
currencyrequired| string [ 1 .. 100 ] characters  Default:  "USD" Represents a currency.
since| string Represents a date and time in yyyy-MM-ddThh:mm:ssZ format.

### Responses

**200**

OK

## Add user to a workspace

You can add users to a workspace via API only if that workspace has a paid subscription. If the workspace has a paid subscription, you can add as many users as you want but you are limited by the number of paid user seats on that workspace.

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

workspaceIdrequired| string Example:  64a687e29ae1f428e7ebe303Represents a workspace identifier across the system.
---|---

##### query Parameters

send-emailrequired| string Default:  "true" Indicates whether to send an email when user is added to the workspace.
---|---

##### Request Body schema: application/json

required

emailrequired| string non-empty  Represents an email address of the user.
---|---

### Responses

**200**

OK

## Update a user's status

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

workspaceIdrequired| string Example:  64a687e29ae1f428e7ebe303Represents a workspace identifier across the system.
---|---
userIdrequired| string Example:  89b687e29ae1f428e7ebe912Represents a user identifier across the system.

##### Request Body schema: application/json

required

statusrequired| string Enum: "ACTIVE" "INACTIVE" Represents membership status.
---|---

### Responses

**200**

OK

## Update a user's cost rate

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

workspaceIdrequired| string Example:  64a687e29ae1f428e7ebe303Represents a workspace identifier across the system.
---|---
userIdrequired| string Example:  89b687e29ae1f428e7ebe912Represents a user identifier across the system.

##### Request Body schema: application/json

required

amountrequired| integer <int32> >= 0  Represents an amount as integer.
---|---
since| string Represents a date and time in yyyy-MM-ddThh:mm:ssZ format.

### Responses

**200**

OK

## Update a user's hourly rate

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

workspaceIdrequired| string Example:  64a687e29ae1f428e7ebe303Represents a workspace identifier across the system.
---|---
userIdrequired| string Example:  89b687e29ae1f428e7ebe912Represents a user identifier across the system.

##### Request Body schema: application/json

required

amountrequired| integer <int32> >= 0  Represents an hourly rate amount as integer.
---|---
since| string Represents a date and time in yyyy-MM-ddThh:mm:ssZ format.

### Responses

**200**

OK