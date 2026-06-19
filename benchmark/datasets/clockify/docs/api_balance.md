# Balance

*Source: https://docs.clockify.me/#tag/Balance*

---

## Get balances for a policy

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

workspaceIdrequired| string Example:  60f91b3ffdaf031696ec61a8Represents a workspace identifier across the system.
---|---
policyIdrequired| string Example:  63034cd0cb0fb876a57e93adRepresents a policy identifier across the system.

##### query Parameters

page| integer <int32> <= 1000  Default:  1 Example:  page=1
---|---
page-size| integer <int32> [ 1 .. 200 ]  Default:  50 Example:  page-size=50
sort| string Enum: "USER" "POLICY" "USED" "BALANCE" "TOTAL" Example:  sort=USERIf provided, you'll get result sorted by sort column.
sort-order| string Enum: "ASCENDING" "DESCENDING" Example:  sort-order=ASCENDINGSort results in ascending or descending order.

### Responses

**200**

OK

## Update a balance

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

workspaceIdrequired| string Example:  60f91b3ffdaf031696ec61a8Represents a workspace identifier across the system.
---|---
policyIdrequired| string Example:  63034cd0cb0fb876a57e93adRepresents a policy identifier across the system.

##### Request Body schema: application/json

required

note| string Represents a new balance note value.
---|---
userIdsrequired| Array of strings non-empty  unique  Represents the list of users' identifiers whose balance is to be updated.
valuerequired| number <double> [ -10000 .. 10000 ]  Represents a new balance value.

### Responses

**204**

No Content

## Get balance for a user

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

workspaceIdrequired| string Example:  60f91b3ffdaf031696ec61a8Represents a workspace identifier across the system.
---|---
userIdrequired| string Example:  60f924bafdaf031696ec6218Represents a user identifier across the system.

##### query Parameters

page| string <= 1000  Page number.
---|---
page-size| string [ 1 .. 200 ]  Page size.
sort| string Enum: "USER" "POLICY" "USED" "BALANCE" "TOTAL" Example:  sort=POLICYSort result based on given criteria
sort-order| string Enum: "ASCENDING" "DESCENDING" Example:  sort-order=ASCENDINGSort result by providing sort order.

### Responses

**200**

OK