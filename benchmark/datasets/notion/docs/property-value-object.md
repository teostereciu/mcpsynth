# property-value-object

*Source: https://developers.notion.com/reference/property-value-object*

---

##### Notion API

##### Objects

##### Endpoints

##### Webhook events

## ​Overview

## ​Attributes

## ​Type objects

### ​Checkbox

#### ​Examplepropertiesbody param for a POST or PATCH page request that creates or updates acheckboxpage property value

#### ​Examplecheckboxpage property value as returned in a GET page request

### ​Created by

#### ​Examplecreated_bypage property value as returned in a GET page request

### ​Created time

#### ​Examplecreated_timepage property value as returned in a GET page request

### ​Date

#### ​Exampledatepage property value as returned in a GET page request

### ​Email

#### ​Exampleemailpage property value as returned in a GET page request

### ​Files

#### ​Example creation or update offilesproperty

#### ​Examplefilespage property value as returned in a GET page request

### ​Formula

#### ​Exampleformulapage property value as returned in a GET page request

### ​Icon

#### ​Example emojiiconproperty value as returned in GET page request

#### ​Example uploadediconpage property value as returned in a GET page request

#### ​Example updating a page icon to an uploaded file

### ​Last edited by

#### ​Examplelast_edited_bypage property value as returned in a GET page request

### ​Last edited time

#### ​Examplelast_edited_timepage property value as returned in a GET page request

### ​Multi-select

#### ​Examplemulti_selectpage property value as returned in a GET page request

### ​Number

#### ​Examplenumberpage property value as returned in a GET page request

### ​People

#### ​Examplepeoplepage property value as returned in a GET page request

### ​Phone number

#### ​Examplephone_numberpage property value as returned in a GET page request

### ​Relation

#### ​Examplerelationpage property value as returned in a GET page request

### ​Rollup

#### ​Examplerolluppage property value as returned in a GET page request

### ​Rich text

#### ​Examplerich_textpage property value as returned in a GET page request

### ​Select

#### ​Example select page property value as returned in a GET page request

### ​Status

#### ​Examplestatuspage property value as returned in a GET page request

### ​Title

#### ​Exampletitlepage property value as returned in a GET page request

### ​URL

#### ​Exampleurlpage property value as returned in a GET page request

### ​Unique ID

#### ​Exampleunique_idpage property value as returned in a GET page request

### ​Verification

#### ​Exampleverificationpage property values as returned in a GET page request

### ​Unsupported properties

## ​Paginated page properties

```
{"properties": {"Task completed": {"checkbox":true}}}
```

```
{"Task completed": {"id":"ZI%40W","type":"checkbox","checkbox":true}}
```

```
{"created_by": {"object":"user","id":"c2f20311-9e54-4d11-8c79-7398424ae41e"}}
```

```
{"Created time": {"id":"eB_%7D","type":"created_time","created_time":"2022-10-24T22:54:00.000Z"}}
```

```
{"properties": {"Due date": {"date": {"start":"2023-02-23"}}}}
```

```
{"Due date": {"id":"M%3BBw","type":"date","date": {"start":"2023-02-07","end":null,"time_zone":null}}}
```

```
{"properties": {"Email": {"email":"ada@makenotion.com"}}}
```

```
{"Email": {"id":"y%5C%5E_","type":"email","email":"ada@makenotion.com"}}
```

```
{"properties": {"Blueprint": {"files": [{"name":"Project Alpha blueprint","external": {"url":"https://www.figma.com/file/g7eazMtXnqON4i280CcMhk/project-alpha-blueprint?node-id=0%3A1&t=nXseWIETQIgv31YH-1"}}]}}}
```

```
{"Blueprint": {"id":"tJPS","type":"files","files": [{"name":"Project blueprint","type":"external","external": {"url":"https://www.figma.com/file/g7eazMtXnqON4i280CcMhk/project-alpha-blueprint?node-id=0%3A1&t=nXseWIETQIgv31YH-1"}}]}}
```

```
{"Days until launch": {"id":"CSoE","type":"formula","formula": {"type":"number","number":56}}}
```

```
{"icon": {"type":"emoji","emoji":"😀"}}
```

```
{"icon": {"type":"file","file": {"url":"https://local-files-secure.s3.us-west-2.amazonaws.com/13950b26-c203-4f3b-b97d-93ec06319565/a7084c4c-3e9a-4324-af99-34e0cb7f8fe7/notion.jpg?...","expiry_time":"2024-12-03T19:44:56.932Z"}}}
```

```
{"icon": {"type":"file_upload","file_upload": {"id":"43833259-72ae-404e-8441-b6577f3159b4"}}}
```

```
{"Last edited by column name": {"id":"uGNN","type":"last_edited_by","last_edited_by": {"object":"user","id":"9188c6a5-7381-452f-b3dc-d4865aa89bdf","name":"Test Integration","avatar_url":"https://s3-us-west-2.amazonaws.com/public.notion-static.com/3db373fe-18f6-4a3c-a536-0f061cb9627f/leplane.jpeg","type":"bot","bot": {}}}}
```

```
{"Last edited time": {"id":"%3Defk","type":"last_edited_time","last_edited_time":"2023-02-24T21:06:00.000Z"}}
```

```
{"properties": {"Programming language": {"multi_select": [{"name":"TypeScript"},{"name":"Python"}]}}}
```

```
{"Programming language": {"id":"QyRn","name":"Programming language","type":"multi_select","multi_select": [{"id":"tC;=","name":"TypeScript","color":"purple"},{"id":"e4413a91-9f84-4c4a-a13d-5b4b3ef870bb","name":"JavaScript","color":"red"},{"id":"fc44b090-2166-40c8-8c58-88f2d8085ec0","name":"Python","color":"gray"}]}}
```

```
{"properties": {"Number of subscribers": {"number":42}}}
```

```
{"Number of subscribers": {"id":"WPj%5E","type":"number","number":42}}
```

```
{"properties": {"Stakeholders": {"people": [{"object":"user","id":"c2f20311-9e54-4d11-8c79-7398424ae41e"}]}}}
```

```
{"Stakeholders": {"id":"%7BLUX","type":"people","people": [{"object":"user","id":"c2f20311-9e54-4d11-8c79-7398424ae41e","name":"Kimberlee Johnson","avatar_url":null,"type":"person","person": {"email":"[email protected]"}}]}}
```

```
{"properties": {"Contact phone number": {"phone_number":"415-202-4776"}}}
```

```
{"Contact phone number": {"id":"%5DKhQ","type":"phone_number","phone_number":"415-202-4776"}}
```

```
{"properties": {"Related tasks": {"relation": [{"id":"dd456007-6c66-4bba-957e-ea501dcda3a6"},{"id":"0c1f7cb2-8090-4f18-924e-d92965055e32"}]}}}
```

```
{"Related tasks": {"id":"hgMz","type":"relation","relation": [{"id":"dd456007-6c66-4bba-957e-ea501dcda3a6"},{"id":"0c1f7cb2-8090-4f18-924e-d92965055e32"}],"has_more":false}}
```

```
{"Number of units": {"id":"hgMz","type":"rollup","rollup": {"type":"number","number":2,"function":"count"}}}
```

```
{"properties": {"Description": {"rich_text": [{"type":"text","text": {"content":"There is some ","link":null},"annotations": {"bold":false,"italic":false,"strikethrough":false,"underline":false,"code":false,"color":"default"},"plain_text":"There is some ","href":null},{"type":"text","text": {"content":"text","link":null},"annotations": {"bold":true,"italic":false,"strikethrough":false,"underline":false,"code":false,"color":"default"},"plain_text":"text","href":null},{"type":"text","text": {"content":" in this property!","link":null},"annotations": {"bold":false,"italic":false,"strikethrough":false,"underline":false,"code":false,"color":"default"},"plain_text":" in this property!","href":null}]}}}
```

```
{"Description": {"id":"HbZT","type":"rich_text","rich_text": [{"type":"text","text": {"content":"There is some ","link":null},"annotations": {"bold":false,"italic":false,"strikethrough":false,"underline":false,"code":false,"color":"default"},"plain_text":"There is some ","href":null},{"type":"text","text": {"content":"text","link":null},"annotations": {"bold":true,"italic":false,"strikethrough":false,"underline":false,"code":false,"color":"default"},"plain_text":"text","href":null},{"type":"text","text": {"content":" in this property!","link":null},"annotations": {"bold":false,"italic":false,"strikethrough":false,"underline":false,"code":false,"color":"default"},"plain_text":" in this property!","href":null}]}}
```

```
{"properties": {"Department": {"select": {"name":"Marketing"}}}}
```

```
{"Department": {"id":"Yc%3FJ","type":"select","select": {"id":"ou@_","name":"jQuery","color":"purple"}}}
```

```
{"properties": {"Status": {"status": {"name":"Not started"}}}}
```

```
{"Status": {"id":"Z%3ClH","type":"status","status": {"id":"539f2705-6529-42d8-a215-61a7183a92c0","name":"In progress","color":"blue"}}}
```

```
{"properties": {"Title": {"id":"title","type":"title","title": [{"type":"text","text": {"content":"A better title for the page","link":null},"annotations": {"bold":false,"italic":false,"strikethrough":false,"underline":false,"code":false,"color":"default"},"plain_text":"This is also not done","href":null}]}}}
```

```
{"Title": {"id":"title","type":"title","title": [{"type":"text","text": {"content":"A better title for the page","link":null},"annotations": {"bold":false,"italic":false,"strikethrough":false,"underline":false,"code":false,"color":"default"},"plain_text":"This is also not done","href":null}]}}
```

```
{"properties": {"Website": {"url":"https://developers.notion.com/"}}}
```

```
{"Website": {"id":"bB%3D%5B","type":"url","url":"https://developers.notion.com/"}}
```

```
{"test-ID": {"id":"tqqd","type":"unique_id","unique_id": {"number":3,"prefix":"RL",},},}
```

```
{Verification: {id:"fpVq",type:"verification",verification: {state:"unverified",verified_by:null,date:null},},}
```

```
{"properties": {"Place": {"id":"%60%40Gq","type":"place","place":null}}}
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
- PageOverviewPage propertiesOverviewPage property items
- Database
- Data source
- View
- Comment
- File
- User
- Parent
- Emoji
- Unfurl attribute (Link Previews)
- Overview
- Page propertiesOverviewPage property items
- Page property items
- Authentication
- Blocks
- Pages
- Databases
- Data sources
- Databases (deprecated)
- Comments
- Views
- File Uploads
- Search
- Users
- File uploads
- Attributes
- Type objects
- Checkbox
- Example properties body param for a POST or PATCH page request that creates or updates a checkbox page property value
- Example checkbox page property value as returned in a GET page request
- Created by
- Example created_by page property value as returned in a GET page request
- Created time
- Example created_time page property value as returned in a GET page request
- Date
- Example date page property value as returned in a GET page request
- Email
- Example email page property value as returned in a GET page request
- Files
- Example creation or update of files property
- Example files page property value as returned in a GET page request
- Formula
- Example formula page property value as returned in a GET page request
- Icon
- Example emoji icon property value as returned in GET page request
- Example uploaded icon page property value as returned in a GET page request
- Example updating a page icon to an uploaded file
- Last edited by
- Example last_edited_by page property value as returned in a GET page request
- Last edited time
- Example last_edited_time page property value as returned in a GET page request
- Multi-select
- Example multi_select page property value as returned in a GET page request
- Number
- Example number page property value as returned in a GET page request
- People
- Example people page property value as returned in a GET page request
- Phone number
- Example phone_number page property value as returned in a GET page request
- Relation
- Example relation page property value as returned in a GET page request
- Rollup
- Example rollup page property value as returned in a GET page request
- Rich text
- Example rich_text page property value as returned in a GET page request
- Select
- Example select page property value as returned in a GET page request
- Example status page property value as returned in a GET page request
- Title
- Example title page property value as returned in a GET page request
- URL
- Example url page property value as returned in a GET page request
- Unique ID
- Example unique_id page property value as returned in a GET page request
- Verification
- Example verification page property values as returned in a GET page request
- Unsupported properties
- Paginated page properties

[TABLE]
Field | Type | Description | Example value
id | string | An underlying identifier for the property. Historically, this may be a UUID, but newer IDs are a short ID that’s always URL-encoded in the API and inintegration webhooks.idmay be used in place of name when creating or updating pages.idremains constant when the property name changes. | "f%5C%5C%3Ap"
type | string(enum) | The type of the property in the page object. Possible type values are:-checkbox-created_by-created_time-date-email-files-formula-last_edited_by-last_edited_time-multi_select-number-people-phone_number-relation-rollup-rich_text-select-status-title-url-unique_id-verificationRefer to specific type sections below for details on type-specific values. | "rich_text"
checkboxcreated_bycreated_timedateemailfilesformulalast_edited_bylast_edited_timemulti_selectnumberpeoplephone_numberrelationrolluprich_textselectstatustitleurlunique_idverification | object | A type object that contains data specific to the page property type, including the page property value.Refer to thetype objects sectionfor descriptions and examples of each type. | "checkbox": true
[/TABLE]

[TABLE]
Field | Type | Description | Example value
checkbox | boolean | Whether the checkbox is checked (true) or unchecked (false). | true
[/TABLE]

[TABLE]
Field | Type | Description | Example value
created_by | object | Auser objectcontaining information about the user who created the page.created_bycan’t be updated. | Refer to the example response objects below.
[/TABLE]

[TABLE]
Field | Type | Description | Example value
created_time | string(ISO 8601date and time) | The date and time that the page was created.Thecreated_timevalue can’t be updated. | "2022-10-12T16:34:00.000Z"
[/TABLE]

[TABLE]
Field | Type | Description | Example value
end | string(ISO 8601date and time) | (Optional) A string representing the end of a date range.If the value isnull, then the date value is not a range. | "2020-12-08T12:00:00Z"
start | string(ISO 8601date and time) | A date, with an optional time.If thedatevalue is a range, thenstartrepresents the start of the range. | "2020-12-08T12:00:00Z”
[/TABLE]

[TABLE]
Field | Type | Description | Example value
email | string | A string describing an email address. | "ada@makenotion.com"
[/TABLE]

[TABLE]
Field | Type | Description | Example value
files | array offile objects | An array of objects containing information about the files. | Refer to the example response objects below.
[/TABLE]

[TABLE]
Field | Type | Description | Example value
boolean||date||number||string | boolean||date||number||string | The value of the result of the formula. The value can’t be updated directly via the API. | 42
type | string(enum) | A string indicating the data type of the result of the formula. Possibletypevalues are: -boolean-date-number-string | "number"
[/TABLE]

[TABLE]
Field | Type | Description | Example value
icon | an object | Icon object | Refer to the example response objects below.
[/TABLE]

[TABLE]
Field | Type | Description | Example value
last_edited_by | object | Auser objectcontaining information about the user who last updated the page.last_edited_bycan’t be updated. | Refer to the example response objects below.
[/TABLE]

[TABLE]
Field | Type | Description | Example value
last_edited_time | string(ISO 8601date and time) | The date and time that the page was last edited. Thelast_edited_timevalue can’t be updated. | "2022-10-12T16:34:00.000Z"
[/TABLE]

[TABLE]
Field | Type | Description | Example value
color | string(enum) | Color of the option. Note: thecolorvalue can’t be updated via the API.Possible"color"values are:-blue-brown-default(the default value)-gray-green-orange-pink-purple-red-yellow | "red"
id | string | The ID of the option.You can useidornameto update a multi-select property. | "b3d773ca-b2c9-47d8-ae98-3c2ce3b2bffb"
name | string | The name of the option as it appears in Notion.If the multi-selectdata source propertydoes not yet have an option by that name, then the name will be added to the data source schema if the integration also has write access to the parent data source.Note: Commas (",") are not valid for select values. | "JavaScript"
[/TABLE]

[TABLE]
Field | Type | Description | Example value
number | number | A number representing some value. | 1234
[/TABLE]

[TABLE]
Field | Type | Description | Example value
people | array ofuser objects | An array of user objects. | Refer to the example response objects below.
[/TABLE]

[TABLE]
Field | Type | Description | Example value
phone_number | string | A string representing a phone number. No phone number format is enforced. | "415-867-5309"
[/TABLE]

[TABLE]
Field | Type | Description | Example value
has_more | boolean | If arelationhas more than 25 references, then thehas_morevalue for the relation in the response object istrue. If a relation doesn’t exceed the limit, thenhas_moreisfalse. | Refer to the example response objects below.
relation | an array of page references | An array of related page references. A page reference is an object with anidkey and a string value corresponding to a page ID in another data source. | Refer to the example response objects below.
[/TABLE]

[TABLE]
Field | Type | Description | Example value
array||date||incomplete||number||unsupported | Corresponds to the field.For example, if the field isnumber, then the type of the value isnumber. | The value of the calculated rollup. The value can’t be directly updated via the API. | 1234
function | string(enum) | The function that is evaluated for every page in the relation of the rollup. Possible"function"values are:-average-checked-count-count_per_group-count_values-date_range-earliest_date-empty-latest_date-max-median-min-not_empty-percent_checked-percent_empty-percent_not_empty-percent_per_group-percent_unchecked-range-show_original-show_unique-sum-unchecked-unique | "sum"
type | array||date||incomplete||number||unsupported | The value type of the calculated rollup. | number
[/TABLE]

[TABLE]
Field | Type | Description | Example value
rich_text | an array ofrich text objects | An array ofrich text objects | Refer to the example response objects below.
[/TABLE]

[TABLE]
Property | Type | Description | Example value
color | string(enum) | The color of the option. Possible"color"values are:-blue-brown-default-gray-green-orange-pink-purple-red-yellowDefaults todefault. Thecolorvalue can’t be updated via the API. | red
id | string | The ID of the option.You can useidornametoupdatea select property. | "b3d73ca-b2c9-47d8-ae98-3c2ce3b2bffb"
name | string | The name of the option as it appears in Notion.If the selectdata source propertydoesn’t have an option by that name yet, then the name is added to the data source schema if the integration also has write access to the parent data source.Note: Commas (",") are not valid for select values. | "jQuery"
[/TABLE]

[TABLE]
Property | Type | Description | Example value
color | string(enum) | The color of the option. Possible"color"values are:-blue-brown-default-gray-green-orange-pink-purple-red-yellowDefaults todefault. Thecolorvalue can’t be updated via the API. | "red"
id | string | string | "b3d773ca-b2c9-47d8-ae98-3c2ce3b2bffb"
name | string | The name of the option as it appears in Notion. | "In progress"
[/TABLE]

[TABLE]
Field | Type | Description | Example value
title | an array ofrich text objects | An array ofrich text objects. | Refer to the example response objects below.
[/TABLE]

[TABLE]
Field | Type | Description | Example value
url | string | A string that describes a web address. | "https://developers.notion.com/"
[/TABLE]

[TABLE]
Field | Type | Description | Example value
number | number | The ID count (auto-incrementing). | 3
prefix | stringornull | An optional prefix to be applied to the unique ID. | ”RL”
[/TABLE]

[TABLE]
Field | Type | Description | Example value
state | string | The verification state of the page."verified"or"unverified". | "unverified"
verified_by | Userobject ornull | If the page if verified, aUserobject will be included to indicate the user who verified the page. | Refer to the example response objects below.
date | Object ornull | If the page is verified, the date object will include the date the verification started (start). If an expiration date is set for the verification, an end date (end) will be included. (ISO 8601date and time.) | Refer to the example response objects below.
[/TABLE]

[TABLE]
Field | Type | Description | Example value
object | "list" | Always"list". | "list"
type | "property_item" | Always"property_item". | "property_item"
results | list | List ofproperty_itemobjects. | [{"object": "property_item", "id": "vYdV", "type": "relation", "relation": { "id": "535c3fb2-95e6-4b37-a696-036e5eac5cf6"}}... ]
property_item | object | Aproperty_itemobject that describes the property. | {"id": "title", "next_url": null, "type": "title", "title": {}}
next_url | stringornull | The URL the user can request to get the next page of results. | "http://api.notion.com/v1/pages/0e5235bf86aa4efb93aa772cce7eab71/properties/vYdV?start_cursor=LYxaUO&page_size=25"
[/TABLE]