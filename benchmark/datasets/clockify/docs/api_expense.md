# Expense

*Source: https://docs.clockify.me/#tag/Expense*

---

## Get all expenses on a workspace

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

workspaceIdrequired| string Example:  64a687e29ae1f428e7ebe303Represents a workspace identifier across the system.
---|---

##### query Parameters

page| integer <int32> Default:  1 Example:  page=1Page number.
---|---
page-size| integer <int32> >= 1  Default:  50 Example:  page-size=50Page size.
user-id| string Example:  user-id=5a0ab5acb07987125438b60fIf provided, you'll get a filtered list of expenses which match the provided string in the user ID linked to the expense.

### Responses

**200**

OK

## Create an expense

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

workspaceIdrequired| string Example:  64a687e29ae1f428e7ebe303Represents a workspace identifier across the system.
---|---

##### Request Body schema: multipart/form-data

amountrequired| number <double> <= 92233720368547760  Represents an expense amount as the double data type.
---|---
billable| boolean Default:  false Indicates whether expense is billable or not.
categoryIdrequired| string Represents a category identifier across the system.
daterequired| string <date-time> Provides a valid yyyy-MM-ddThh:mm:ssZ format date.
filerequired| string <binary>
notes| string [ 0 .. 3000 ] characters  Represents notes for an expense.
projectIdrequired| string Represents a project identifier across the system.
taskId| string Represents a task identifier across the system.
userIdrequired| string non-empty  Represents a user identifier across the system.

### Responses

**201**

Created

## Get all expense categories

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

workspaceIdrequired| string Example:  64a687e29ae1f428e7ebe303Represents a workspace identifier across the system.
---|---

##### query Parameters

sort-column| string Value: "NAME" Example:  sort-column=NAMERepresents the column name to be used as sorting criteria.
---|---
sort-order| string Enum: "ASCENDING" "DESCENDING" Example:  sort-order=ASCENDINGRepresents the sorting order.
page| integer <int32> Default:  1 Example:  page=1Page number.
page-size| integer <int32> >= 1  Default:  50 Example:  page-size=50Page size.
archived| boolean Default:  false Example:  archived=trueFlag to filter results based on whether category is archived or not.
name| string Example:  name=procurementIf provided, you'll get a filtered list of expense categories that matches the provided string in their name.

### Responses

**200**

OK

## Add an expense category

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

workspaceIdrequired| string Example:  64a687e29ae1f428e7ebe303Represents a workspace identifier across the system.
---|---

##### Request Body schema: application/json

required

hasUnitPrice| boolean Default:  false Flag whether expense category has unit price or none.
---|---
namerequired| string [ 0 .. 250 ] characters  Represents a valid expense category name.
priceInCents| integer <int32> Represents price in cents as integer.
unit| string Represents a valid expense category unit.

### Responses

**201**

Created

## Delete an expense category

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

workspaceIdrequired| string Example:  64a687e29ae1f428e7ebe303Represents a workspace identifier across the system.
---|---
categoryIdrequired| string Example:  89a687e29ae1f428e7ebe567Represents a category identifier across the system.

### Responses

**204**

No Content

## Update an expense category

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

workspaceIdrequired| string Example:  64a687e29ae1f428e7ebe303Represents a workspace identifier across the system.
---|---
categoryIdrequired| string Example:  89a687e29ae1f428e7ebe567Represents a category identifier across the system.

##### Request Body schema: application/json

required

hasUnitPrice| boolean Default:  false Flag whether expense category has unit price or none.
---|---
namerequired| string [ 0 .. 250 ] characters  Represents a valid expense category name.
priceInCents| integer <int32> Represents price in cents as integer.
unit| string Represents a valid expense category unit.

### Responses

**200**

OK

## Archive an expense category

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

workspaceIdrequired| string Example:  64a687e29ae1f428e7ebe303Represents a workspace identifier across the system.
---|---
categoryIdrequired| string Example:  89a687e29ae1f428e7ebe567Represents a category identifier across the system.

##### Request Body schema: application/json

required

archived| boolean Default:  false Flag whether to archive the expense category or not.
---|---

### Responses

**200**

OK

## Delete an expense

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

workspaceIdrequired| string Example:  64a687e29ae1f428e7ebe303Represents a workspace identifier across the system.
---|---
expenseIdrequired| string Example:  64c777ddd3fcab07cfbb210cRepresents an expense identifier across the system.

### Responses

**200**

OK

## Get an expense by ID

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

workspaceIdrequired| string Example:  64a687e29ae1f428e7ebe303Represents a workspace identifier across the system.
---|---
expenseIdrequired| string Example:  64c777ddd3fcab07cfbb210cRepresents an expense identifier across the system.

### Responses

**200**

OK

## Update an expense

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

workspaceIdrequired| string Example:  64a687e29ae1f428e7ebe303Represents a workspace identifier across the system.
---|---
expenseIdrequired| string Example:  64c777ddd3fcab07cfbb210cRepresents an expense identifier across the system.

##### Request Body schema: multipart/form-data

amountrequired| number <double> [ 0 .. 92233720368547760 ]  Represents an expense amount as the double data type.
---|---
billable| boolean Default:  false Indicates whether expense is billable or not.
categoryIdrequired| string Represents a category identifier across the system.
changeFieldsrequired| Array of stringsItems Enum: "USER" "DATE" "PROJECT" "TASK" "CATEGORY" "NOTES" "AMOUNT" "BILLABLE" "FILE" Represents a list of expense change fields.
daterequired| string <date-time> Provides a valid yyyy-MM-ddThh:mm:ssZ format date.
filerequired| string <binary>
notes| string [ 0 .. 3000 ] characters  Represents notes for an expense.
projectId| string Represents a project identifier across the system.
taskId| string Represents a task identifier across the system.
userIdrequired| string non-empty  Represents a user identifier across the system.

### Responses

**200**

OK

## Download a receipt

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

fileIdrequired| string Example:  745687e29ae1f428e7ebe890Represents a file identifier across the system.
---|---
expenseIdrequired| string Example:  64c777ddd3fcab07cfbb210cRepresents an expense identifier across the system.
workspaceIdrequired| string Example:  64a687e29ae1f428e7ebe303Represents a workspace identifier across the system.

### Responses

**200**

OK