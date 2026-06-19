# property-item-object

*Source: https://developers.notion.com/reference/property-item-object*

---

##### Notion API

##### Objects

##### Endpoints

##### Webhook events

## ​Overview

## ​Common fields

## ​Paginated values

## ​Title

## ​Rich text

## ​Number

## ​Select

## ​Multi-select

### ​Option values

## ​Date

## ​Formula

### ​String formula

### ​Number formula

### ​Boolean formula

### ​Date formula

## ​Relation

## ​Rollup

### ​Number rollup

### ​Date rollup

### ​Array rollup

### ​Incomplete rollup

## ​People

## ​Files

## ​Checkbox

## ​URL

## ​Email

## ​Phone number

## ​Created time

## ​Created by

## ​Last edited time

## ​Last edited by

```
{"Name": {"object":"list","results": [{"object":"property_item","id":"title","type":"title","title": {"type":"text","text": {"content":"The title","link":null},"annotations": {"bold":false,"italic":false,"strikethrough":false,"underline":false,"code":false,"color":"default"},"plain_text":"The title","href":null}}],"next_cursor":null,"has_more":false,"type":"property_item","property_item": {"id":"title","next_url":null,"type":"title","title": {}}}}
```

```
{"Details": {"object":"list","results": [{"object":"property_item","id":"NVv%5E","type":"rich_text","rich_text": {"type":"text","text": {"content":"Some more text with ","link":null},"annotations": {"bold":false,"italic":false,"strikethrough":false,"underline":false,"code":false,"color":"default"},"plain_text":"Some more text with ","href":null}},{"object":"property_item","id":"NVv%5E","type":"rich_text","rich_text": {"type":"text","text": {"content":"fun formatting","link":null},"annotations": {"bold":false,"italic":true,"strikethrough":false,"underline":false,"code":false,"color":"default"},"plain_text":"fun formatting","href":null}}],"next_cursor":null,"has_more":false,"type":"property_item","property_item": {"id":"NVv^","next_url":null,"type":"rich_text","rich_text": {}}}}
```

```
{"Quantity": {"object":"property_item","id":"XpXf","type":"number","number":1234}}
```

```
{"Option": {"object":"property_item","id":"%7CtzR","type":"select","select": {"id":"64190ec9-e963-47cb-bc37-6a71d6b71206","name":"Option 1","color":"orange"}}}
```

```
{"Tags": {"object":"property_item","id":"z%7D%5C%3C","type":"multi_select","multi_select": [{"id":"91e6959e-7690-4f55-b8dd-d3da9debac45","name":"A","color":"orange"},{"id":"2f998e2d-7b1c-485b-ba6b-5e6a815ec8f5","name":"B","color":"purple"}]}}
```

```
{"Shipment Time": {"object":"property_item","id":"i%3Ahj","type":"date","date": {"start":"2021-05-11T11:00:00.000-04:00","end":null,"time_zone":null}}}
```

```
{"Formula": {"object":"property_item","id":"KpQq","type":"formula","formula": {"type":"number","number":1234}}}
```

```
{"Project": {"object":"list","results": [{"object":"property_item","id":"vYdV","type":"relation","relation": {"id":"535c3fb2-95e6-4b37-a696-036e5eac5cf6"}}],"next_cursor":null,"has_more":true,"type":"property_item","property_item": {"id":"vYdV","next_url":null,"type":"relation","relation": {}}}}
```

```
{"Rollup": {"object":"list","results": [{"object":"property_item","id":"vYdV","type":"relation","relation": {"id":"535c3fb2-95e6-4b37-a696-036e5eac5cf6"}}...],"next_cursor":"1QaTunT5","has_more":true,"type":"property_item","property_item": {"id":"y}~p","next_url":"http://api.notion.com/v1/pages/0e5235bf86aa4efb93aa772cce7eab71/properties/y%7D~p?start_cursor=1QaTunT5&page_size=25","type":"rollup","rollup": {"function":"sum","type":"incomplete","incomplete": {}}}}}
```

```
{"Owners": {"object":"property_item","id":"KpQq","type":"people","people": [{"object":"user","id":"285e5768-3fdc-4742-ab9e-125f9050f3b8","name":"Example Avo","avatar_url":null,"type":"person","person": {"email":"[email protected]"}}]}}
```

```
{"Files": {"object":"property_item","id":"KpQq","type":"files","files": [{"type":"external","name":"Space Wallpaper","external":"https://website.domain/images/space.png"}]}}
```

```
{"Done?": {"object":"property_item","id":"KpQq","type":"checkbox","checkbox":true}}
```

```
{"Website": {"object":"property_item","id":"KpQq","type":"url","url":"https://notion.so/notiondevs"}}
```

```
{"Shipper's Contact": {"object":"property_item","id":"KpQq","type":"email","email":"hello@test.com"}}
```

```
{"Shipper's No.": {"object":"property_item","id":"KpQq","type":"phone_number","phone_number":"415-000-1111"}}
```

```
{"Created Time": {"object":"property_item","id":"KpQq","type":"create_time","created_time":"2020-03-17T19:10:04.968Z"}}
```

```
{"Created By": {"created_by": {"object":"user","id":"23345d4f-cf71-4a70-89a5-226c95a6eaae","name":"Test User","type":"person","person": {"email":"avo@example.org"}}}}
```

```
{"Last Edited Time": {"last_edited_time":"2020-03-17T19:10:04.968Z"}}
```

```
{"Last Edited By": {"last_edited_by": {"object":"user","id":"23345d4f-cf71-4a70-89a5-226c95a6eaae","name":"Test User","type":"person","person": {"email":"avo@example.org"}}}}
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
- Common fields
- Paginated values
- Title
- Rich text
- Number
- Select
- Multi-select
- Option values
- Date
- Formula
- String formula
- Number formula
- Boolean formula
- Date formula
- Relation
- Rollup
- Number rollup
- Date rollup
- Array rollup
- Incomplete rollup
- People
- Files
- Checkbox
- URL
- Email
- Phone number
- Created time
- Created by
- Last edited time
- Last edited by
- show_unique(Show unique values)
- unique(Count unique values)
- median(Median)

[TABLE]
Property | Type | Description | Example value
object | "property_item" | Always"property_item". | "property_item"
id | string | Underlying identifier for the property. This identifier is guaranteed to remain constant when the property name changes. It may be a UUID, but is often a short random string.Theidmay be used in place ofnamewhen creating or updating pages. | "f%5C%5C%3Ap"
type | string(enum) | Type of the property. Possible values are"rich_text","number","select","multi_select","date","formula","relation","rollup","title","people","files","checkbox","url","email","phone_number","created_time","created_by","last_edited_time", and"last_edited_by". | "rich_text"
[/TABLE]

[TABLE]
Property | Type | Description | Example value
object | "list" | Always"list". | "list"
type | "property_item" | Always"property_item". | "property_item"
results | list | List ofproperty_itemobjects. | [{"object": "property_item", "id": "vYdV", "type": "relation", "relation": { "id": "535c3fb2-95e6-4b37-a696-036e5eac5cf6"}}... ]
property_item | object | Aproperty_itemobject that describes the property. | {"id": "title", "next_url": null, "type": "title", "title": {}}
next_url | stringornull | The URL the user can request to get the next page of results. | "http://api.notion.com/v1/pages/0e5235bf86aa4efb93aa772cce7eab71/properties/vYdV?start_cursor=LYxaUO&page_size=25"
[/TABLE]

[TABLE]
Property | Type | Description | Example value
id | string(UUIDv4) | ID of the option.When updating a select property, you can use eithernameorid. | "b3d773ca-b2c9-47d8-ae98-3c2ce3b2bffb"
name | string | Name of the option as it appears in Notion.If the selectdatabase propertydoes not yet have an option by that name, it will be added to the database schema if the integration also has write access to the parent database.Note: Commas (”,”) are not valid for select values. | "Fruit"
color | string(enum) | Color of the option. Possible values are:"default","gray","brown","red","orange","yellow","green","blue","purple","pink".Defaults to"default". Not currently editable. | "red"
[/TABLE]

[TABLE]
Property | Type | Description | Example value
id | string(UUIDv4) | ID of the option. When updating a multi-select property, you can use eithernameorid. | "b3d773ca-b2c9-47d8-ae98-3c2ce3b2bffb"
name | string | Name of the option as it appears in Notion.If the multi-selectdatabase propertydoes not yet have an option by that name, it will be added to the database schema if the integration also has write access to the parent database.Note: Commas (”,”) are not valid for select values. | "Fruit"
color | string(enum) | Color of the option. Possible values are:"default","gray","brown","red","orange","yellow","green","blue","purple","pink".  Defaults to"default".Not currently editable. | "red"
[/TABLE]

[TABLE]
Property | Type | Description | Example value
start | string (ISO 8601 date and time) | An ISO 8601 format date, with optional time. | "2020-12-08T12:00:00Z"
end | string (optional,ISO 8601 date and time) | An ISO 8601 formatted date, with optional time. Represents the end of a date range.Ifnull, this property’s date value is not a range. | "2020-12-08T12:00:00Z"
time_zone | string (optional, enum) | Time zone information forstartandend. Possible values are extracted from theIANA databaseand they are based on the time zones fromMoment.js.When time zone is provided,startandendshould not have anyUTC offset. In addition, when time zone is provided,startandendcannot be dates without time information.Ifnull, time zone information will be contained inUTC offsets instartandend. | "America/Los_Angeles"
[/TABLE]

[TABLE]
Property | Type | Description
type | string(enum) | The type of the formula result. Possible values are"string","number","boolean", and"date".
[/TABLE]

[TABLE]
Property | Type | Description
type | string(enum) | The type of rollup. Possible values are"number","date","array","unsupported"and"incomplete".
function | string(enum) | Describes the aggregation used. Possible values include:count,count_values,empty,not_empty,unique,show_unique,percent_empty,percent_not_empty,sum,average,median,min,max,range,earliest_date,latest_date,date_range,checked,unchecked,percent_checked,percent_unchecked,count_per_group,percent_per_group,show_original
[/TABLE]