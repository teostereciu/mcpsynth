# Tag

*Source: https://docs.clockify.me/#tag/Tag*

---

## Find tags on a workspace

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

workspaceIdrequired| string Example:  64a687e29ae1f428e7ebe303Represents a workspace identifier across the system.
---|---

##### query Parameters

name| string Example:  name=feature_XIf provided, you'll get a filtered list of tags that matches the provided string in their name.
---|---
strict-name-search| boolean Default:  false Flag to toggle on/off strict search mode. When set to true, search by name will only return tags whose name exactly matches the string value given for the 'name' parameter. When set to false, results will also include tags whose name contain the string value, but could be longer than the string value itself. For example, if there is a tag with the name 'applications', and the search value is 'app', setting strict-name-search to true will not return that tag in the results, whereas setting it to false will.
excluded-ids| string Example:  excluded-ids=90p687e29ae1f428e7ebe657&excluded-ids=3r8687e29ae1f428e7eg567yRepresents a list of excluded ids
sort-column| string Enum: "ID" "NAME" Example:  sort-column=NAMERepresents a column to be used as sorting criteria.
sort-order| string Enum: "ASCENDING" "DESCENDING" Example:  sort-order=ASCENDINGRepresents a sorting mode.
page| integer <int32> Default:  1 Example:  page=1Page number.
page-size| integer <int32> >= 1  Default:  50 Example:  page-size=50Page size.
archived| boolean Default:  false Example:  archived=falseFilters the result whether tags are archived or not.

### Responses

**200**

OK

## Add a new tag

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

workspaceIdrequired| string Example:  64a687e29ae1f428e7ebe303Represents a workspace identifier across the system.
---|---

##### Request Body schema: application/json

required

name| string [ 0 .. 100 ] characters  Represents a tag name.
---|---

### Responses

**201**

Created

## Delete a tag

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

idrequired| string Example:  21s687e29ae1f428e7ebe404Represents a tag identifier across the system.
---|---
workspaceIdrequired| string Example:  64a687e29ae1f428e7ebe303Represents a workspace identifier across the system.

### Responses

**200**

OK

## Get a tag by ID

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

idrequired| string Example:  21s687e29ae1f428e7ebe404Represents a tag identifier across the system.
---|---
workspaceIdrequired| string Example:  64a687e29ae1f428e7ebe303Represents a workspace identifier across the system.

### Responses

**200**

OK

## Update a tag

##### Authorizations:

_ApiKeyAuth_ _AddonKeyAuth_

##### path Parameters

idrequired| string Example:  21s687e29ae1f428e7ebe404Represents a tag identifier across the system.
---|---
workspaceIdrequired| string Example:  64a687e29ae1f428e7ebe303Represents a workspace identifier across the system.

##### Request Body schema: application/json

required

archived| boolean Default:  false Indicates whether a tag will be archived or not.
---|---
name| string [ 0 .. 100 ] characters  Represents a tag name.

### Responses

**200**

OK