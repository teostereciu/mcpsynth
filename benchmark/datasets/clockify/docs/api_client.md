# Client

*Source: https://docs.clockify.me/#tag/Client*

---

## Find clients on a workspace

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

workspaceIdrequired| string Example:  64a687e29ae1f428e7ebe303Represents a workspace identifier across the system.
---|---

##### query Parameters

name| string Example:  name=Client XFilters client results that matches with the string provided in their client name.
---|---
sort-column| string Default:  "NAME" Example:  sort-column=NAMEColumn name that will be used as criteria for sorting results.
sort-order| string Example:  sort-order=ASCENDINGSorting mode
page| integer <int32> Default:  1 Example:  page=1Page number.
page-size| integer <int32> >= 1  Default:  50 Example:  page-size=50Page size.
archived| string Filter whether to include archived clients or not.

### Responses

**200**

OK

## Add a new client

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

workspaceIdrequired| string Example:  64a687e29ae1f428e7ebe303Represents a workspace identifier across the system.
---|---

##### Request Body schema: application/json

required

address| string [ 0 .. 3000 ] characters  Represents a client's address.
---|---
email| string <email> Represents a client email.
name| string [ 0 .. 100 ] characters  Represents a client name.
note| string [ 0 .. 3000 ] characters  Represents additional notes for the client.

### Responses

**201**

Created

## Delete a client

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

idrequired| string Example:  44a687e29ae1f428e7ebe305Represents a client identifier across the system.
---|---
workspaceIdrequired| string Example:  64a687e29ae1f428e7ebe303Represents a workspace identifier across the system.

### Responses

**200**

OK

## Get a client by ID

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

idrequired| string Example:  44a687e29ae1f428e7ebe305Represents a client identifier across the system.
---|---
workspaceIdrequired| string Example:  64a687e29ae1f428e7ebe303Represents a workspace identifier across the system.

### Responses

**200**

OK

## Update a client

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

idrequired| string Example:  44a687e29ae1f428e7ebe305Represents a client identifier across the system.
---|---
workspaceIdrequired| string Example:  64a687e29ae1f428e7ebe303Represents a workspace identifier across the system.

##### query Parameters

archive-projects| boolean
---|---
mark-tasks-as-done| boolean

##### Request Body schema: application/json

required

address| string [ 0 .. 3000 ] characters  Represents a client's address.
---|---
archived| boolean Default:  false Indicates if client will be archived or not.
ccEmails| Array of strings <email> [ 0 .. 3 ] items [ items <email > ]
currencyId| string Represents a currency identifier across the system.
email| string <email> Represents a client email.
name| string [ 0 .. 100 ] characters  Represents a client name.
note| string [ 0 .. 3000 ] characters  Represents additional notes for the client.

### Responses

**200**

OK