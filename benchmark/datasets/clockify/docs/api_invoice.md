# Invoice

*Source: https://docs.clockify.me/#tag/Invoice*

---

## Get all invoices on a workspace

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

workspaceIdrequired| string Example:  64a687e29ae1f428e7ebe303Represents a workspace identifier across the system.
---|---

##### query Parameters

page| integer <int32> Default:  1 Example:  page=1Page number.
---|---
page-size| integer <int32> >= 1  Default:  50 Example:  page-size=50Page size.
statuses| string Enum: "UNSENT" "SENT" "PAID" "PARTIALLY_PAID" "VOID" "OVERDUE" Example:  statuses=UNSENT&statuses=PAIDIf provided, you'll get a filtered result of invoices that matches the provided string in the user ID linked to the expense.
sort-column| string Enum: "ID" "CLIENT" "DUE_ON" "ISSUE_DATE" "AMOUNT" "BALANCE" Example:  sort-column=CLIENTValid column name as sorting criteria. Default: ID
sort-order| string Enum: "ASCENDING" "DESCENDING" Example:  sort-order=ASCENDINGSort order. Default: ASCENDING

### Responses

**200**

OK

## Add an invoice

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

workspaceIdrequired| string Example:  64a687e29ae1f428e7ebe303Represents a workspace identifier across the system.
---|---

##### Request Body schema: application/json

required

clientIdrequired| string non-empty  Represents a client identifier across the system.
---|---
currencyrequired| string non-empty  Represents the currency used by the invoice.
dueDaterequired| string <date-time> Represents an invoice due date in yyyy-MM-ddThh:mm:ssZ format.
issuedDaterequired| string <date-time> Represents an invoice issued date in yyyy-MM-ddThh:mm:ssZ format.
numberrequired| string non-empty  Represents an invoice number.
timeViewMode| string Enum: "TIME_SENSITIVE_VIEW" "AGGREGATED_TIME_VIEW"

### Responses

**201**

Created

## Filter out invoices

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

workspaceIdrequired| string Example:  64a687e29ae1f428e7ebe303Represents a workspace identifier across the system.
---|---

##### Request Body schema: application/json

required

clients| object (ContainsArchivedFilterRequest)  Represents a project filter for imported items.
---|---
companies| object (BaseFilterRequest)  Represents a company filter object. If provided, you'll get a filtered list of invoices that matches the specified company filter.
exactAmount| integer <int64> Represents an invoice amount. If provided, you'll get a filtered list of invoices that has the equal amount as specified.
exactBalance| integer <int64> Represents an invoice balance. If provided, you'll get a filtered list of invoices that has the equal balance as specified.
greaterThanAmount| integer <int64> Represents an invoice amount. If provided, you'll get a filtered list of invoices that has amount greater than specified.
greaterThanBalance| integer <int64> Represents an invoice balance. If provided, you'll get a filtered list of invoices that has balance greater than specified.
invoiceNumber| string If provided, you'll get a filtered list of invoices that contain the provided string in their invoice number.
issueDate| object (TimeRangeRequestDtoV1)  Represents a time range object. If provided, you'll get a filtered list of invoices that has issue date within the time range specified.
lessThanAmount| integer <int64> Represents an invoice amount. If provided, you'll get a filtered list of invoices that has amount less than specified.
lessThanBalance| integer <int64> Represents an invoice balance. If provided, you'll get a filtered list of invoices that has balance less than specified.
page| integer <int32> Default:  1 Page number.
pageSize| integer <int32> Default:  50 Page size.
sortColumn| string Enum: "ID" "CLIENT" "DUE_ON" "ISSUE_DATE" "AMOUNT" "BALANCE" Represents the column name to be used as sorting criteria.
sortOrder| string Enum: "ASCENDING" "DESCENDING" Represents the sorting order.
statuses| Array of stringsItems Enum: "UNSENT" "SENT" "PAID" "PARTIALLY_PAID" "VOID" "OVERDUE" Represents a list of invoice statuses. If provided, you'll get a filtered list of invoices that matches any of the invoice status provided.
strictSearch| boolean Default:  false Flag to toggle on/off strict search mode. When set to true, search by invoice number only will return invoices whose number exactly matches the string value given for the 'invoiceNumber' parameter. When set to false, results will also include invoices whose number contain the string value, but could be longer than the string value itself. For example, if there is an invoice with the number '123456', and the search value is '123', setting strict-name-search to true will not return that invoice in the results, whereas setting it to false will.

### Responses

**200**

OK

## Get an invoice in another language

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

workspaceIdrequired| string Example:  64a687e29ae1f428e7ebe303Represents a workspace identifier across the system.
---|---

### Responses

**200**

OK

## Change an invoice language

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

workspaceIdrequired| string Example:  64a687e29ae1f428e7ebe303Represents a workspace identifier across the system.
---|---

##### Request Body schema: application/json

required

defaults| object (InvoiceDefaultSettingsRequestV1)  Represents an invoice default settings object.
---|---
exportFields| object (InvoiceExportFieldsRequest)  Represents an invoice export fields object.
labelsrequired| object (LabelsCustomizationRequest)  Represents a label customization object.

### Responses

**200**

OK

## Delete an invoice

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

workspaceIdrequired| string Example:  64a687e29ae1f428e7ebe303Represents a workspace identifier across the system.
---|---
invoiceIdrequired| string Example:  78a687e29ae1f428e7ebe303Represents an invoice identifier across the system.

### Responses

**200**

OK

## Get an invoice by ID

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

workspaceIdrequired| string Example:  64a687e29ae1f428e7ebe303Represents a workspace identifier across the system.
---|---
invoiceIdrequired| string Example:  83q687e29ae1f428e7ebe195Represents an invoice identifier across the system.

### Responses

**200**

OK

## Update an invoice

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

workspaceIdrequired| string Example:  64a687e29ae1f428e7ebe303Represents a workspace identifier across the system.
---|---
invoiceIdrequired| string Example:  78a687e29ae1f428e7ebe303Represents an invoice identifier across the system.

##### Request Body schema: application/json

required

clientId| string Represents client identifier across the system.
---|---
companyId| string Represents company identifier across the system.
currencyrequired| string [ 1 .. 100 ] characters  Represents the currency used by the invoice.
discountPercentrequired| number <double> Represents an invoice discount percent as double.
dueDaterequired| string <date-time> Represents an invoice due date in yyyy-MM-ddThh:mm:ssZ format.
issuedDaterequired| string <date-time> Represents an invoice issued date in yyyy-MM-ddThh:mm:ssZ format.
note| string Represents an invoice note.
numberrequired| string non-empty  Represents an invoice number.
subject| string Represents an invoice subject.
tax2Percentrequired| number <double> Represents an invoice tax 2 percent as double.
taxPercentrequired| number <double> Represents an invoice tax percent as double.
taxType| object (TaxType)  Represents an invoice taxation type.
visibleZeroFields| string Enum: "TAX" "TAX_2" "DISCOUNT" Represents a list of zero value invoice fields that will be visible.

### Responses

**200**

OK

## Duplicate an invoice

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

invoiceIdrequired| string Example:  78a687e29ae1f428e7ebe303Represents an invoice identifier across the system.
---|---
workspaceIdrequired| string Example:  64a687e29ae1f428e7ebe303Represents a workspace identifier across the system.

### Responses

**201**

Created

## Export an invoice

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

invoiceIdrequired| string Example:  78a687e29ae1f428e7ebe303Represents an invoice identifier across the system.
---|---
workspaceIdrequired| string Example:  64a687e29ae1f428e7ebe303Represents a workspace identifier across the system.

##### query Parameters

userLocalerequired| string Example:  userLocale=enRepresents a locale.
---|---

### Responses

**200**

OK

## Add item to an invoice

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

workspaceIdrequired| string Example:  64a687e29ae1f428e7ebe303Represents a workspace identifier across the system.
---|---
invoiceIdrequired| string Example:  83q687e29ae1f428e7ebe195Represents an invoice identifier across the system.

##### Request Body schema: application/json

required

applyTaxesrequired| string Enum: "TAX1" "TAX2" "TAX1TAX2" "NONE" Represents taxes applied to the invoice item. Applies only when the specified taxes are active on the invoice.
---|---
descriptionrequired| string Represents an invoice item description.
itemTyperequired| string non-empty  Represents an item type.
quantityrequired| integer <int64> Represents an item quantity.
unitPricerequired| integer <int64> Represents an item unit price.

### Responses

**200**

OK

## Import time entries and expenses to an invoice

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

workspaceIdrequired| string Example:  64a687e29ae1f428e7ebe303Represents a workspace identifier across the system.
---|---
invoiceIdrequired| string Example:  83q687e29ae1f428e7ebe195Represents an invoice identifier across the system.

##### Request Body schema: application/json

required

expenseFieldsForDetailedGroup| Array of strings unique  Default:  "NOTE"Items Enum: "PROJECT" "TASK" "CATEGORY" "NOTE" "DATE" "USER" Represents a set of expense fields to include when using the DETAILED expense grouping type.
---|---
expensesGroupBy| string Default:  "PROJECT" Enum: "CATEGORY" "PROJECT" "USER" Represents a group field when using the GROUPED expense group type.
expensesGroupType| string Default:  "DETAILED" Enum: "GROUPED" "DETAILED" Represents an expense group type.
fromrequired| string Represents date and time in the yyyy-MM-ddThh:mm:ssZ format.
importExpensesrequired| boolean Default:  false Indicates if billable expenses should be imported alongside time entries.
projectFilterrequired| object (ContainsArchivedFilterRequest)  Represents a project filter for imported items.
roundTimeEntryDuration| boolean Default:  false Indicates if imported time entry durations should be rounded to the nearest 15 minute interval.
timeEntryFieldsForDetailedGroup| Array of strings unique Items Enum: "PROJECT" "TASK" "TAGS" "DESCRIPTION" "DATE" "USER" Represents a set of time entry fields to include when using DETAILED time entry grouping type.
timeEntryGroupTyperequired| string Enum: "SINGLE_ITEM" "GROUPED" "DETAILED" Represents a time entry group type.
timeEntryPrimaryGroupBy| string Enum: "USER" "PROJECT" "DATE" Represents a primary group field when using the GROUPED time entry grouping type.
timeEntrySecondaryGroupBy| string Enum: "PROJECT" "USER" "TASK" "DATE" "DESCRIPTION" "NONE" Represents a secondary group field when using the GROUPED time entry grouping type. Should not have the same grouping type as the primary group field.
torequired| string Represents date and time in the yyyy-MM-ddThh:mm:ssZ format.

### Responses

**200**

OK

## Delete item from an invoice

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

workspaceIdrequired| string Example:  64a687e29ae1f428e7ebe303Represents a workspace identifier across the system.
---|---
invoiceIdrequired| string Example:  83q687e29ae1f428e7ebe195Represents an invoice identifier across the system.
orderrequired| integer <int32> >= 1  Example:  3Represents an invoice item order.

### Responses

**200**

OK

## Get payments for an invoice

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

workspaceIdrequired| string Example:  64a687e29ae1f428e7ebe303Represents a workspace identifier across the system.
---|---
invoiceIdrequired| string Example:  78a687e29ae1f428e7ebe303Represents an invoice identifier across the system.

##### query Parameters

page| integer <int32> Default:  1 Example:  page=1Page number.
---|---
page-size| integer <int32> >= 1  Default:  50 Example:  page-size=50Page size.

### Responses

**200**

OK

## Add payment to an invoice

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

workspaceIdrequired| string Example:  64a687e29ae1f428e7ebe303Represents a workspace identifier across the system.
---|---
invoiceIdrequired| string Example:  78a687e29ae1f428e7ebe303Represents an invoice identifier across the system.

##### Request Body schema: application/json

required

amount| integer <int64> >= 1  Represents an invoice payment amount as long.
---|---
note| string [ 0 .. 1000 ] characters  Represents an invoice payment note.
paymentDate| string Represents an invoice payment date in yyyy-MM-ddThh:mm:ssZ format.

### Responses

**201**

Created

## Delete payment from an invoice

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

invoiceIdrequired| string Example:  78a687e29ae1f428e7ebe303Represents an invoice identifier across the system.
---|---
workspaceIdrequired| string Example:  64a687e29ae1f428e7ebe303Represents a workspace identifier across the system.
paymentIdrequired| string Example:  56p687e29ae1f428e7ebe456Represents a payment identifier across the system.

### Responses

**200**

OK

## Change an invoice status

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

workspaceIdrequired| string Example:  64a687e29ae1f428e7ebe303Represents a workspace identifier across the system.
---|---
invoiceIdrequired| string Example:  78a687e29ae1f428e7ebe303Represents an invoice identifier across the system.

##### Request Body schema: application/json

required

invoiceStatus| string Enum: "UNSENT" "SENT" "PAID" "PARTIALLY_PAID" "VOID" "OVERDUE" Represents the invoice status to be set.
---|---

### Responses

**200**

OK