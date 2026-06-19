# post-database-query-filter

*Source: https://developers.notion.com/reference/post-database-query-filter*

---

##### Notion API

##### Objects

##### Endpoints

##### Webhook events

## ​The filter object

## ​Type-specific filter conditions

### ​Checkbox

### ​Date

### ​Files

### ​Formula

### ​Multi-select

### ​Number

### ​People

### ​Relation

### ​Rich text

### ​Rollup

#### ​Filter conditions forarrayrollup values

#### ​Filter conditions fordaterollup values

#### ​Filter conditions fornumberrollup values

### ​Select

### ​Status

### ​Timestamp

### ​Verification

### ​ID

## ​Compound filter conditions

### ​Example compound filter conditions

```
curl -X POST 'https://api.notion.com/v1/databases/897e5a76ae524b489fdfe71f5945d1af/query' \-H 'Authorization: Bearer '"$NOTION_API_KEY"'' \-H 'Notion-Version: 2022-06-28' \-H "Content-Type: application/json" \--data '{"filter": {"property": "Task completed","checkbox": {"equals": true}}}'
```

```
const{Client}=require('@notionhq/client');constnotion=newClient({auth:process.env.NOTION_API_KEY});// replace with your own database IDconstdatabaseId='d9824bdc-8445-4327-be8b-5b47500af6ce';constfilteredRows=async()=>{constresponse=awaitnotion.databases.query({database_id:databaseId,filter:{property:"Task completed",checkbox:{equals:true}},});returnresponse;}
```

```
{"and": [{"property":"Done","checkbox": {"equals":true}},{"or": [{"property":"Tags","contains":"A"},{"property":"Tags","contains":"B"}]}]}
```

```
{"filter": {"property":"Task completed","checkbox": {"equals":true}}}
```

```
{"filter": {"property":"Due date","date": {"on_or_after":"2023-02-08"}}}
```

```
{"filter": {"property":"Blueprint","files": {"is_not_empty":true}}}
```

```
{"filter": {"property":"One month deadline","formula": {"date":{"after":"2021-05-10"}}}}
```

```
{"filter": {"property":"Programming language","multi_select": {"contains":"TypeScript"}}}
```

```
{"filter": {"property":"Estimated working days","number": {"less_than_or_equal_to":5}}}
```

```
{"filter": {"property":"Last edited by","people": {"contains":"c2f20311-9e54-4d11-8c79-7398424ae41e"}}}
```

```
{"filter": {"property":"✔️ Task List","relation": {"contains":"0c1f7cb280904f18924ed92965055e32"}}}
```

```
{"filter": {"property":"Description","rich_text": {"contains":"cross-team"}}}
```

```
{"filter": {"property":"Related tasks","rollup": {"any": {"rich_text": {"contains":"Migrate database"}}}}}
```

```
{"filter": {"property":"Parent project due date","rollup": {"date": {"on_or_before":"2023-02-08"}}}}
```

```
{"filter": {"property":"Total estimated working days","rollup": {"number": {"does_not_equal":42}}}}
```

```
{"filter": {"property":"Frontend framework","select": {"equals":"React"}}}
```

```
{"filter": {"property":"Project status","status": {"equals":"Not started"}}}
```

```
{"filter": {"timestamp":"created_time","created_time": {"on_or_before":"2022-10-13"}}}
```

```
{"filter": {"property":"verification","verification": {"status":"verified"}}}
```

```
{"filter": {"and": [{"property":"ID","unique_id": {"greater_than":1}},{"property":"ID","unique_id": {"less_than":3}}]}}
```

```
{"filter": {"and": [{"property":"Complete","checkbox": {"equals":true}},{"property":"Working days","number": {"greater_than":10}}]}}
```

```
{"filter": {"or": [{"property":"Description","rich_text": {"contains":"2023"}},{"and": [{"property":"Department","select": {"equals":"Engineering"}},{"property":"Priority goal","checkbox": {"equals":true}}]}]}}
```
- Status
- Community
- Blog
- Introduction
- Integration capabilities
- Webhooks
- Request limits
- Status codes
- Versioning
- Block
- Page
- Database
- Data source
- View
- Comment
- File
- User
- Parent
- Emoji
- Unfurl attribute (Link Previews)
- Authentication
- Blocks
- Pages
- Databases
- Data sources
- Databases (deprecated)POSTCreate a databaseGETRetrieve a databaseGETGet databasesQuery a databasePOSTOverviewFilter database entriesSort database entriesUpdate a database
- Comments
- Views
- File Uploads
- Search
- Users
- POSTCreate a database
- GETRetrieve a database
- GETGet databases
- Query a databasePOSTOverviewFilter database entriesSort database entries
- Update a database
- POSTOverview
- Filter database entries
- Sort database entries
- File uploads
- The filter object
- Type-specific filter conditions
- Checkbox
- Date
- Files
- Formula
- Multi-select
- Number
- People
- Relation
- Rich text
- Rollup
- Filter conditions for array rollup values
- Filter conditions for date rollup values
- Filter conditions for number rollup values
- Select
- Timestamp
- Verification
- Compound filter conditions
- Example compound filter conditions
- Filter data source entries

[TABLE]
Field | Type | Description | Example value
property | string | The name of the property as it appears in the database, or the property ID. | "Task completed"
checkboxdatefilesformulamulti_selectnumberpeoplephone_numberrelationrich_textselectstatustimestampverificationID | object | The type-specific filter condition for the query. Only types listed in the Field column of this table are supported.Refer totype-specific filter conditionsfor details on corresponding object values. | "checkbox": { "equals": true }
[/TABLE]

[TABLE]
Field | Type | Description | Example value
equals | boolean | Whether acheckboxproperty value matches the provided value exactly.Returns or excludes all database entries with an exact value match. | false
does_not_equal | boolean | Whether acheckboxproperty value differs from the provided value.Returns or excludes all database entries with a difference in values. | true
[/TABLE]

[TABLE]
Field | Type | Description | Example value
after | string(ISO 8601 date) | The value to compare the date property value against.Returns database entries where the date property value is after the provided date. | "2021-05-10""2021-05-10T12:00:00""2021-10-15T12:00:00-07:00"
before | string(ISO 8601 date) | The value to compare the date property value against.Returns database entries where the date property value is before the provided date. | "2021-05-10""2021-05-10T12:00:00""2021-10-15T12:00:00-07:00"
equals | string(ISO 8601 date) | The value to compare the date property value against.Returns database entries where the date property value is the provided date. | "2021-05-10""2021-05-10T12:00:00""2021-10-15T12:00:00-07:00"
is_empty | true | The value to compare the date property value against. Returns database entries where the date property value contains no data. | true
is_not_empty | true | The value to compare the date property value against. Returns database entries where the date property value is not empty. | true
next_month | object(empty) | A filter that limits the results to database entries where the date property value is within the next month. | {}
next_week | object(empty) | A filter that limits the results to database entries where the date property value is within the next week. | {}
next_year | object(empty) | A filter that limits the results to database entries where the date property value is within the next year. | {}
on_or_after | string(ISO 8601 date) | The value to compare the date property value against.Returns database entries where the date property value is on or after the provided date. | "2021-05-10""2021-05-10T12:00:00""2021-10-15T12:00:00-07:00"
on_or_before | string(ISO 8601 date) | The value to compare the date property value against.Returns database entries where the date property value is on or before the provided date. | "2021-05-10""2021-05-10T12:00:00""2021-10-15T12:00:00-07:00"
past_month | object(empty) | A filter that limits the results to database entries where thedateproperty value is within the past month. | {}
past_week | object(empty) | A filter that limits the results to database entries where thedateproperty value is within the past week. | {}
past_year | object(empty) | A filter that limits the results to database entries where thedateproperty value is within the past year. | {}
this_week | object(empty) | A filter that limits the results to database entries where thedateproperty value is this week. | {}
[/TABLE]

[TABLE]
Field | Type | Description | Example value
is_empty | true | Whether the files property value does not contain any data.Returns all database entries with an emptyfilesproperty value. | true
is_not_empty | true | Whether thefilesproperty value contains data.Returns all entries with a populatedfilesproperty value. | true
[/TABLE]

[TABLE]
Field | Type | Description | Example value
checkbox | object | Acheckboxfilter condition to compare the formula result against.Returns database entries where the formula result matches the provided condition. | Refer to thecheckboxfilter condition.
date | object | Adatefilter condition to compare the formula result against.Returns database entries where the formula result matches the provided condition. | Refer to thedatefilter condition.
number | object | Anumberfilter condition to compare the formula result against.Returns database entries where the formula result matches the provided condition. | Refer to thenumberfilter condition.
string | object | Arich textfilter condition to compare the formula result against.Returns database entries where the formula result matches the provided condition. | Refer to therich textfilter condition.
[/TABLE]

[TABLE]
Field | Type | Description | Example value
contains | string | The value to compare the multi-select property value against.Returns database entries where the multi-select value matches the provided string. | "Marketing"
does_not_contain | string | The value to compare the multi-select property value against.Returns database entries where the multi-select value does not match the provided string. | "Engineering"
is_empty | true | Whether the multi-select property value is empty.Returns database entries where the multi-select value does not contain any data. | true
is_not_empty | true | Whether the multi-select property value is not empty.Returns database entries where the multi-select value does contains data. | true
[/TABLE]

[TABLE]
Field | Type | Description | Example value
does_not_equal | number | Thenumberto compare the number property value against.Returns database entries where the number property value differs from the providednumber. | 42
equals | number | Thenumberto compare the number property value against.Returns database entries where the number property value is the same as the provided number. | 42
greater_than | number | Thenumberto compare the number property value against.Returns database entries where the number property value exceeds the providednumber. | 42
greater_than_or_equal_to | number | Thenumberto compare the number property value against.Returns database entries where the number property value is equal to or exceeds the providednumber. | 42
is_empty | true | Whether thenumberproperty value is empty.Returns database entries where the number property value does not contain any data. | true
is_not_empty | true | Whether the number property value is not empty.Returns database entries where the number property value contains data. | true
less_than | number | Thenumberto compare the number property value against.Returns database entries where the number property value is less than the providednumber. | 42
less_than_or_equal_to | number | Thenumberto compare the number property value against.Returns database entries where the number property value is equal to or is less than the providednumber. | 42
[/TABLE]

[TABLE]
Field | Type | Description | Example value
contains | string(UUIDv4) | The value to compare the people property value against.Returns database entries where the people property value contains the providedstring. | "6c574cee-ca68-41c8-86e0-1b9e992689fb"
does_not_contain | string(UUIDv4) | The value to compare the people property value against. Returns database entries where the people property value does not contain the providedstring. | "6c574cee-ca68-41c8-86e0-1b9e992689fb"
is_empty | true | Whether the people property value does not contain any data.Returns database entries where the people property value does not contain any data. | true
is_not_empty | true | Whether the people property value contains data.Returns database entries where the people property value is not empty. | true
[/TABLE]

[TABLE]
Field | Type | Description | Example value
contains | string(UUIDv4) | The value to compare the relation property value against.Returns database entries where the relation property value contains the providedstring. | "6c574cee-ca68-41c8-86e0-1b9e992689fb"
does_not_contain | string(UUIDv4) | The value to compare the relation property value against.Returns entries where the relation property value does not contain the providedstring. | "6c574cee-ca68-41c8-86e0-1b9e992689fb"
is_empty | true | Whether the relation property value does not contain data.Returns database entries where the relation property value does not contain any data. | true
is_not_empty | true | Whether the relation property value contains data.Returns database entries where the property value is not empty. | true
[/TABLE]

[TABLE]
Field | Type | Description | Example value
contains | string | Thestringto compare the text property value against.Returns database entries with a text property value that includes the providedstring. | "Moved to Q2"
does_not_contain | string | Thestringto compare the text property value against.Returns database entries with a text property value that does not include the providedstring. | "Moved to Q2"
does_not_equal | string | Thestringto compare the text property value against.Returns database entries with a text property value that does not match the providedstring. | "Moved to Q2"
ends_with | string | Thestringto compare the text property value against.Returns database entries with a text property value that ends with the providedstring. | "Q2"
equals | string | Thestringto compare the text property value against.Returns database entries with a text property value that matches the providedstring. | "Moved to Q2"
is_empty | true | Whether the text property value does not contain any data.Returns database entries with a text property value that is empty. | true
is_not_empty | true | Whether the text property value contains any data.Returns database entries with a text property value that contains data. | true
starts_with | string | Thestringto compare the text property value against.Returns database entries with a text property value that starts with the providedstring. | ”Moved”
[/TABLE]

[TABLE]
Field | Type | Description | Example value
any | object | The value to compare each rollup property value against. Can be afilter conditionfor any other type.Returns database entries where the rollup property value matches the provided criteria. | "rich_text": { "contains": "Take Fig on a walk" }
every | object | The value to compare each rollup property value against. Can be afilter conditionfor any other type.Returns database entries where every rollup property value matches the provided criteria. | "rich_text": { "contains": "Take Fig on a walk" }
none | object | The value to compare each rollup property value against. Can be afilter conditionfor any other type.Returns database entries where no rollup property value matches the provided criteria. | "rich_text": { "contains": "Take Fig on a walk" }
[/TABLE]

[TABLE]
Field | Type | Description | Example value
date | object | Adatefilter condition to compare the rollup value against.Returns database entries where the rollup value matches the provided condition. | Refer to thedatefilter condition.
[/TABLE]

[TABLE]
Field | Type | Description | Example value
number | object | Anumberfilter condition to compare the rollup value against.Returns database entries where the rollup value matches the provided condition. | Refer to thenumberfilter condition.
[/TABLE]

[TABLE]
Field | Type | Description | Example value
equals | string | Thestringto compare the select property value against.Returns database entries where the select property value matches the provided string. | "This week"
does_not_equal | string | Thestringto compare the select property value against.Returns database entries where the select property value does not match the providedstring. | "Backlog"
is_empty | true | Whether the select property value does not contain data.Returns database entries where the select property value is empty. | true
is_not_empty | true | Whether the select property value contains data.Returns database entries where the select property value is not empty. | true
[/TABLE]

[TABLE]
Field | Type | Description | Example value
equals | string | The string to compare the status property value against.Returns database entries where the status property value matches the provided string. | ”This week”
does_not_equal | string | The string to compare the status property value against.Returns database entries where the status property value does not match the provided string. | ”Backlog”
is_empty | true | Whether the status property value does not contain data.Returns database entries where the status property value is empty. | true
is_not_empty | true | Whether the status property value contains data.Returns database entries where the status property value is not empty. | true
[/TABLE]

[TABLE]
Field | Type | Description | Example value
timestamp | created_time last_edited_time | A constant string representing the type of timestamp to use as a filter. | ”created_time”
created_time last_edited_time | object | A date filter condition used to filter the specified timestamp. | Refer to thedatefilter condition.
[/TABLE]

[TABLE]
Field | Type | Description | Example value
status | string | The verification status being queried. Valid options are:verified,expired,noneReturns database entries where the current verification status matches the queried status. | ”verified”
[/TABLE]

[TABLE]
Field | Type | Description | Example value
does_not_equal | number | The value to compare the unique_id property value against.Returns database entries where the unique_id property value differs from the provided value. | 42
equals | number | The value to compare the unique_id property value against.Returns database entries where the unique_id property value is the same as the provided value. | 42
greater_than | number | The value to compare the unique_id property value against.Returns database entries where the unique_id property value exceeds the provided value. | 42
greater_than_or_equal_to | number | The value to compare the unique_id property value against.Returns database entries where the unique_id property value is equal to or exceeds the provided value. | 42
less_than | number | The value to compare the unique_id property value against.Returns database entries where the unique_id property value is less than the provided value. | 42
less_than_or_equal_to | number | The value to compare the unique_id property value against.Returns database entries where the unique_id property value is equal to or is less than the provided value. | 42
[/TABLE]

[TABLE]
Field | Type | Description | Example value
and | array | An array offilterobjects or compound filter conditions.Returns database entries that matchallof the provided filter conditions. | Refer to the examples below.
or | array | An array offilterobjects or compound filter conditions.Returns database entries that matchanyof the provided filter conditions | Refer to the examples below.
[/TABLE]