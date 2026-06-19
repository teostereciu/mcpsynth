# Webhooks

*Source: https://docs.clockify.me/#tag/Webhooks*

---

## Get all webhooks for addon on a workspace

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

workspaceIdrequired| string Example:  64a687e29ae1f428e7ebe303Represents a workspace identifier across the system.
---|---
addonIdrequired| string Example:  64c777ddd3fcab07cfbb210cRepresents an addon identifier across the system.

### Responses

**200**

OK

## Get all webhooks on a workspace

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

workspaceIdrequired| string Example:  64a687e29ae1f428e7ebe303Represents a workspace identifier across the system.
---|---

##### query Parameters

type| string Enum: "USER_CREATED" "SYSTEM" "ADDON" Example:  type=USER_CREATEDRepresents a webhook type.
---|---

### Responses

**200**

OK

## Create a webhook

Creating a webhook generates a new token which can be used to verify that the webhook being sent was sent by Clockify, as it will always be present in the header.

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

workspaceIdrequired| string Example:  64a687e29ae1f428e7ebe303Represents a workspace identifier across the system.
---|---

##### Request Body schema: application/json

required

name| string [ 2 .. 30 ] characters  Represents a webhook name.
---|---
triggerSourcerequired| Array of strings Represents a list of trigger sources.
triggerSourceTyperequired| string Enum: "PROJECT_ID" "USER_ID" "TAG_ID" "TASK_ID" "WORKSPACE_ID" "ASSIGNMENT_ID" "EXPENSE_ID" Represents a webhook event trigger source type.
urlrequired| string non-empty  Represents a webhook target url.
webhookEventrequired| string Enum: "NEW_PROJECT" "NEW_TASK" "NEW_CLIENT" "NEW_TIMER_STARTED" "TIMER_STOPPED" "TIME_ENTRY_UPDATED" "TIME_ENTRY_DELETED" "TIME_ENTRY_SPLIT" "NEW_TIME_ENTRY" "TIME_ENTRY_RESTORED" "NEW_TAG" "USER_DELETED_FROM_WORKSPACE" "USER_JOINED_WORKSPACE" "USER_DEACTIVATED_ON_WORKSPACE" "USER_ACTIVATED_ON_WORKSPACE" "USER_EMAIL_CHANGED" "USER_UPDATED" "NEW_INVOICE" "INVOICE_UPDATED" "NEW_APPROVAL_REQUEST" "APPROVAL_REQUEST_STATUS_UPDATED" "TIME_OFF_REQUESTED" "TIME_OFF_REQUEST_UPDATED" "TIME_OFF_REQUEST_APPROVED" "TIME_OFF_REQUEST_REJECTED" "TIME_OFF_REQUEST_STARTED" "TIME_OFF_REQUEST_WITHDRAWN" "BALANCE_UPDATED" "TAG_UPDATED" "TAG_DELETED" "TASK_UPDATED" "CLIENT_UPDATED" "TASK_DELETED" "CLIENT_DELETED" "EXPENSE_RESTORED" "ASSIGNMENT_CREATED" "ASSIGNMENT_DELETED" "ASSIGNMENT_PUBLISHED" "ASSIGNMENT_UPDATED" "EXPENSE_CREATED" "EXPENSE_DELETED" "EXPENSE_UPDATED" "PROJECT_UPDATED" "PROJECT_DELETED" "USER_GROUP_CREATED" "USER_GROUP_UPDATED" "USER_GROUP_DELETED" "USERS_INVITED_TO_WORKSPACE" "LIMITED_USERS_ADDED_TO_WORKSPACE" "COST_RATE_UPDATED" "BILLABLE_RATE_UPDATED" Represents a webhook event type.

### Responses

**201**

Created

## Delete a webhook

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

workspaceIdrequired| string Example:  64a687e29ae1f428e7ebe303Represents a workspace identifier across the system.
---|---
webhookIdrequired| string Example:  5b715448b0798751107918abRepresents a webhook identifier across the system.

### Responses

**200**

OK

## Get a specific webhook by id

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

workspaceIdrequired| string Example:  64a687e29ae1f428e7ebe303Represents a workspace identifier across the system.
---|---
webhookIdrequired| string Example:  5b715448b0798751107918abRepresents a webhook identifier across the system.

### Responses

**200**

OK

## Update a webhook

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

workspaceIdrequired| string Example:  64a687e29ae1f428e7ebe303Represents a workspace identifier across the system.
---|---
webhookIdrequired| string Example:  5b715448b0798751107918abRepresents a webhook identifier across the system.

##### Request Body schema: application/json

required

name| string [ 2 .. 30 ] characters  Represents a webhook name.
---|---
triggerSourcerequired| Array of strings Represents a list of trigger sources.
triggerSourceTyperequired| string Enum: "PROJECT_ID" "USER_ID" "TAG_ID" "TASK_ID" "WORKSPACE_ID" "ASSIGNMENT_ID" "EXPENSE_ID" Represents a webhook event trigger source type.
urlrequired| string non-empty  Represents a workspace identifier across the system.
webhookEventrequired| string Enum: "NEW_PROJECT" "NEW_TASK" "NEW_CLIENT" "NEW_TIMER_STARTED" "TIMER_STOPPED" "TIME_ENTRY_UPDATED" "TIME_ENTRY_DELETED" "TIME_ENTRY_SPLIT" "NEW_TIME_ENTRY" "TIME_ENTRY_RESTORED" "NEW_TAG" "USER_DELETED_FROM_WORKSPACE" "USER_JOINED_WORKSPACE" "USER_DEACTIVATED_ON_WORKSPACE" "USER_ACTIVATED_ON_WORKSPACE" "USER_EMAIL_CHANGED" "USER_UPDATED" "NEW_INVOICE" "INVOICE_UPDATED" "NEW_APPROVAL_REQUEST" "APPROVAL_REQUEST_STATUS_UPDATED" "TIME_OFF_REQUESTED" "TIME_OFF_REQUEST_UPDATED" "TIME_OFF_REQUEST_APPROVED" "TIME_OFF_REQUEST_REJECTED" "TIME_OFF_REQUEST_STARTED" "TIME_OFF_REQUEST_WITHDRAWN" "BALANCE_UPDATED" "TAG_UPDATED" "TAG_DELETED" "TASK_UPDATED" "CLIENT_UPDATED" "TASK_DELETED" "CLIENT_DELETED" "EXPENSE_RESTORED" "ASSIGNMENT_CREATED" "ASSIGNMENT_DELETED" "ASSIGNMENT_PUBLISHED" "ASSIGNMENT_UPDATED" "EXPENSE_CREATED" "EXPENSE_DELETED" "EXPENSE_UPDATED" "PROJECT_UPDATED" "PROJECT_DELETED" "USER_GROUP_CREATED" "USER_GROUP_UPDATED" "USER_GROUP_DELETED" "USERS_INVITED_TO_WORKSPACE" "LIMITED_USERS_ADDED_TO_WORKSPACE" "COST_RATE_UPDATED" "BILLABLE_RATE_UPDATED" Represents a webhook event type.

### Responses

**200**

OK

## Get logs for a webhook

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

workspaceIdrequired| string Example:  64a687e29ae1f428e7ebe303Represents a workspace identifier across the system.
---|---
webhookIdrequired| string Represents a webhook identifier across the system.

##### query Parameters

page| integer <int32> Default:  0 Example:  page=1Page number.
---|---
size| integer <int32> >= 1  Default:  50 Example:  size=50Page size.

##### Request Body schema: application/json

required

from| string <date-time> Represents date and time in yyyy-MM-ddThh:mm:ssZ format. If provided, results will include logs which occurred after this value.
---|---
sortByNewest| boolean Default:  false If set to true, logs will be sorted with most recent first.
status| string Enum: "ALL" "SUCCEEDED" "FAILED" Filters logs by status.
to| string <date-time> Represents date and time in yyyy-MM-ddThh:mm:ssZ format. If provided, results will include logs which occurred before this value.

### Responses

**200**

OK

## Generate a new token

Generates a new webhook token and invalidates previous one

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

workspaceIdrequired| string Example:  64a687e29ae1f428e7ebe303Represents a workspace identifier across the system.
---|---
webhookIdrequired| string Example:  5b715448b0798751107918abRepresents a webhook identifier across the system.

### Responses

**200**

OK