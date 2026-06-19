# Approval

*Source: https://docs.clockify.me/#tag/Approval*

---

## Get approval requests

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

workspaceIdrequired| string Example:  64a687e29ae1f428e7ebe303Represents a workspace identifier across the system.
---|---

##### query Parameters

status| string Enum: "PENDING" "APPROVED" "WITHDRAWN_APPROVAL" Example:  status=PENDINGFilters results based on the provided approval state.
---|---
sort-column| string Enum: "ID" "USER_ID" "START" "UPDATED_AT" Example:  sort-column=STARTRepresents the column name to be used as sorting criteria.
sort-order| string Enum: "ASCENDING" "DESCENDING" Example:  sort-order=ASCENDINGRepresents the sorting order.
page| integer <int32> Default:  1 Example:  page=1Page number.
page-size| integer <int32> >= 1  Default:  50 Example:  page-size=50Page size.

### Responses

**200**

OK

## Submit approval request

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

workspaceIdrequired| string Example:  64a687e29ae1f428e7ebe303Represents a workspace identifier across the system.
---|---

##### Request Body schema: application/json

required

period| string Enum: "WEEKLY" "SEMI_MONTHLY" "MONTHLY" Specifies the approval period. It has to match the workspace approval period setting.
---|---
periodStartrequired| string non-empty  Specifies an approval period start date in yyyy-MM-ddThh:mm:ssZ format.

### Responses

**201**

Created

## Submit non pending/approved entries/expenses for approval to an existing approval request

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

workspaceIdrequired| string Example:  64a687e29ae1f428e7ebe303Represents a workspace identifier across the system.
---|---

##### Request Body schema: application/json

required

period| string Enum: "WEEKLY" "SEMI_MONTHLY" "MONTHLY" Specifies the approval period. It has to match the workspace approval period setting.
---|---
periodStartrequired| string non-empty  Specifies an approval period start date in yyyy-MM-ddThh:mm:ssZ format.

### Responses

**200**

OK

## Submit an approval request for a user

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

workspaceIdrequired| string Example:  64a687e29ae1f428e7ebe303Represents a workspace identifier across the system.
---|---
userIdrequired| string Example:  5a0ab5acb07987125438b60fRepresents a user identifier across the system.

##### Request Body schema: application/json

required

period| string Enum: "WEEKLY" "SEMI_MONTHLY" "MONTHLY" Specifies the approval period. It has to match the workspace approval period setting.
---|---
periodStartrequired| string non-empty  Specifies an approval period start date in yyyy-MM-ddThh:mm:ssZ format.

### Responses

**201**

Created

## Re-submit rejected/withdrawn entries/expenses for an approval of a user

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

workspaceIdrequired| string Example:  64a687e29ae1f428e7ebe303Represents a workspace identifier across the system.
---|---
userIdrequired| string Example:  5a0ab5acb07987125438b60fRepresents a user identifier across the system.

##### Request Body schema: application/json

required

period| string Enum: "WEEKLY" "SEMI_MONTHLY" "MONTHLY" Specifies the approval period. It has to match the workspace approval period setting.
---|---
periodStartrequired| string non-empty  Specifies an approval period start date in yyyy-MM-ddThh:mm:ssZ format.

### Responses

**200**

OK

## Update an approval request

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

workspaceIdrequired| string Example:  64a687e29ae1f428e7ebe303Represents a workspace identifier across the system.
---|---
approvalRequestIdrequired| string Example:  940ab5acb07987125438b65yRepresents an approval request identifier across the system.

##### Request Body schema: application/json

required

note| string Additional notes for the approval request.
---|---
staterequired| string Enum: "PENDING" "APPROVED" "WITHDRAWN_SUBMISSION" "WITHDRAWN_APPROVAL" "REJECTED" Specifies the approval state to set.

### Responses

**200**

OK