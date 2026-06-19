# property-object

*Source: https://developers.notion.com/reference/property-object*

---

##### Notion API

##### Objects

##### Endpoints

##### Webhook events

## ​Checkbox

## ​Created by

## ​Created time

## ​Date

## ​Email

## ​Files

## ​Formula

## ​Last edited by

## ​Last edited time

## ​Multi-select

## ​Number

## ​People

## ​Phone number

## ​Place

## ​Relation

## ​Rich text

## ​Rollup

## ​Select

## ​Status

## ​Title

## ​Unique ID

## ​URL

```
{"Task complete": {"id":"BBla","name":"Task complete","type":"checkbox","checkbox": {}}}
```

```
{"Task complete": {"checkbox":true}}
```

```
{"Created by": {"id":"%5BJCR","name":"Created by","type":"created_by","created_by": {}}}
```

```
{"Created by": {"id":"%5BJCR","type":"created_by","created_by": {"object":"user","id":"c2f20311-9e54-4d11-8c79-7398424ae41e"}}}
```

```
{"Created time": {"id":"XcAf","name":"Created time","type":"created_time","created_time": {}}}
```

```
{"Created time": {"id":"XcAf","type":"created_time","created_time":"2022-10-24T22:54:00.000Z"}}
```

```
{"Task due date": {"id":"AJP%7D","name":"Task due date","type":"date","date": {}}}
```

```
{"Task due date": {"date": {"start":"2023-02-23","end":null,"time_zone":null}}}
```

```
{"Contact email": {"id":"oZbC","name":"Contact email","type":"email","email": {}}}
```

```
{"Contact email": {"email":"ada@makenotion.com"}}
```

```
{"Product image": {"id":"pb%3E%5B","name":"Product image","type":"files","files": {}}}
```

```
{"Product image": {"files": [{"type":"external","name":"Space Wallpaper","external": {"url":"https://website.domain/images/space.png"}}]}}
```

```
{"Updated price": {"id":"YU%7C%40","name":"Updated price","type":"formula","formula": {"expression":"prop(\"Price\") / 2"}}}
```

```
{"Updated price": {"id":"YU%7C%40","type":"formula","formula": {"type":"number","number":56}}}
```

```
{"Last edited by": {"id":"eB_}","name":"Last edited by","type":"last_edited_by","last_edited_by": {}}}
```

```
{"Last edited by": {"id":"eB_}","type":"last_edited_by","last_edited_by": {"object":"user","id":"9188c6a5-7381-452f-b3dc-d4865aa89bdf"}}}
```

```
{"Last edited time": {"id":"jGdo","name":"Last edited time","type":"last_edited_time","last_edited_time": {}}}
```

```
{"Last edited time": {"id":"jGdo","type":"last_edited_time","last_edited_time":"2023-02-24T21:06:00.000Z"}}
```

```
{"Store availability": {"id":"flsb","name":"Store availability","type":"multi_select","multi_select": {"options": [{"id":"5de29601-9c24-4b04-8629-0bca891c5120","name":"Duc Loi Market","color":"blue"},{"id":"385890b8-fe15-421b-b214-b02959b0f8d9","name":"Rainbow Grocery","color":"gray"}]}}}
```

```
{"Store availability": {"multi_select": [{"name":"Duc Loi Market"},{"name":"Rainbow Grocery"}]}}
```

```
{"Price": {"id":"%7B%5D_P","name":"Price","type":"number","number": {"format":"dollar"}}}
```

```
{"Price": {"number":42}}
```

```
{"Project owner": {"id":"FlgQ","name":"Project owner","type":"people","people": {}}}
```

```
{"Project owner": {"people": [{"object":"user","id":"c2f20311-9e54-4d11-8c79-7398424ae41e"}]}}
```

```
{"Contact phone number": {"id":"ULHa","name":"Contact phone number","type":"phone_number","phone_number": {}}}
```

```
{"Contact phone number": {"phone_number":"415-867-5309"}}
```

```
{"Place": {"id":"Xqz4","name":"Place","type":"place","place": {}}}
```

```
{"Place": {"id":"%60%40Gq","type":"place","place":null}}
```

```
{"Projects": {"id":"~pex","name":"Projects","type":"relation","relation": {"data_source_id":"6c4240a9-a3ce-413e-9fd0-8a51a4d0a49b","dual_property": {"synced_property_name":"Tasks","synced_property_id":"JU]K"}}}}
```

```
{"Projects": {"relation": [{"id":"dd456007-6c66-4bba-957e-ea501dcda3a6"},{"id":"0c1f7cb2-8090-4f18-924e-d92965055e32"}]}}
```

```
{"Project description": {"id":"NZZ%3B","name":"Project description","type":"rich_text","rich_text": {}}}
```

```
{"Project description": {"rich_text": [{"type":"text","text": {"content":"A project description"}}]}}
```

```
{"Estimated total project time": {"id":"%5E%7Cy%3C","name":"Estimated total project time","type":"rollup","rollup": {"rollup_property_name":"Days to complete","relation_property_name":"Tasks","rollup_property_id":"\\nyY","relation_property_id":"Y]<y","function":"sum"}}}
```

```
{"Food group": {"id":"%40Q%5BM","name":"Food group","type":"select","select": {"options": [{"id":"e28f74fc-83a7-4469-8435-27eb18f9f9de","name":"Vegetable","color":"purple"},{"id":"6132d771-b283-4cd9-ba44-b1ed30477c7f","name":"Fruit","color":"red"},{"id":"fc9ea861-820b-4f2b-bc32-44ed9eca873c","name":"Protein","color":"yellow"}]}}}
```

```
{"Food group": {"select": {"name":"Fruit"}}}
```

```
{"Status": {"id":"biOx","name":"Status","type":"status","status": {"options": [{"id":"034ece9a-384d-4d1f-97f7-7f685b29ae9b","name":"Not started","color":"default"},{"id":"330aeafb-598c-4e1c-bc13-1148aa5963d3","name":"In progress","color":"blue"},{"id":"497e64fb-01e2-41ef-ae2d-8a87a3bb51da","name":"Done","color":"green"}],"groups": [{"id":"b9d42483-e576-4858-a26f-ed940a5f678f","name":"To-do","color":"gray","option_ids": ["034ece9a-384d-4d1f-97f7-7f685b29ae9b"] },{"id":"cf4952eb-1265-46ec-86ab-4bded4fa2e3b","name":"In progress","color":"blue","option_ids": ["330aeafb-598c-4e1c-bc13-1148aa5963d3"] },{"id":"4fa7348e-ae74-46d9-9585-e773caca6f40","name":"Complete","color":"green","option_ids": ["497e64fb-01e2-41ef-ae2d-8a87a3bb51da"] }]}}}
```

```
{"Status": {"status": {"name":"In progress"}}}
```

```
{"Project name": {"id":"title","name":"Project name","type":"title","title": {}}}
```

```
{"Project name": {"title": [{"type":"text","text": {"content":"My project"}}]}}
```

```
{"Task ID": {"id":"tqqd","name":"Task ID","type":"unique_id","unique_id": {"prefix":"TASK"}}}
```

```
{"Task ID": {"id":"tqqd","type":"unique_id","unique_id": {"number":3,"prefix":"TASK"}}}
```

```
{"Project URL": {"id":"BZKU","name":"Project URL","type":"url","url": {}}}
```

```
{"Project URL": {"url":"https://developers.notion.com/"}}
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
- Data sourceOverviewData source properties
- View
- Comment
- File
- User
- Parent
- Emoji
- Unfurl attribute (Link Previews)
- Overview
- Data source properties
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
- Checkbox
- Created by
- Created time
- Date
- Email
- Files
- Formula
- Last edited by
- Last edited time
- Multi-select
- Number
- People
- Phone number
- Place
- Relation
- Rich text
- Rollup
- Select
- Title
- Unique ID
- URL
- Property
- Value

[TABLE]
Field | Type | Description | Example value
id | string | An identifier for the property, usually a short string of random letters and symbols. Some automatically generated property types have special human-readable IDs (e.g. all Title properties have anidof"title"). | "fy:{"
name | string | The name of the property as it appears in Notion. | 
description | string | The description of a property as it appears in Notion. | 
type | string(enum) | The type that controls the behavior of the property. Possible values are:"checkbox","created_by","created_time","date","email","files","formula","last_edited_by","last_edited_time","multi_select","number","people","phone_number","place","relation","rich_text","rollup","select","status","title","unique_id","url" | "rich_text"
[/TABLE]

[TABLE]
Field | Type | Description | Example value
expression | string | The formula used to compute values. Refer to theNotion help centerfor syntax. | "prop(\"Price\") / 2"
[/TABLE]

[TABLE]
Field | Type | Description | Example value
color | string(enum) | The color of the option. Possible values:blue,brown,default,gray,green,orange,pink,purple,red,yellow | "blue"
id | string | An identifier for the option. Does not change if the name is changed. | "ff8e9269-9579-47f7-8f6e-83a84716863c"
name | string | The name of the option as it appears in Notion. Commas are not valid. Names must be unique (case-insensitive). | "Fruit"
[/TABLE]

[TABLE]
Field | Type | Description | Example value
format | string(enum) | How the number displays in Notion. Values include:number,number_with_commas,percent,dollar,euro,pound,yen,yuan,won,ruble,rupee,franc,real,lira,krona,ringgit, andmore. | "percent"
[/TABLE]

[TABLE]
Field | Type | Description | Example value
data_source_id | string(UUID) | The data source that the relation refers to. Linked page values must belong to this data source. | "668d797c-76fa-4934-9b05-ad288df2d136"
dual_property | object | An object withsynced_property_idandsynced_property_namefor the corresponding property in the related data source. Present for dual (bidirectional) relations. | See example below.
[/TABLE]

[TABLE]
Field | Type | Description | Example value
function | string(enum) | The function that computes the rollup value. Values include:average,checked,count,count_values,date_range,earliest_date,empty,latest_date,max,median,min,not_empty,percent_checked,percent_empty,percent_not_empty,percent_unchecked,range,show_original,show_unique,sum,unchecked,unique | "sum"
relation_property_id | string | Theidof the related data source property. | "fy:{"
relation_property_name | string | Thenameof the related data source property. | "Tasks"
rollup_property_id | string | Theidof the property being rolled up. | "fy:{"
rollup_property_name | string | Thenameof the property being rolled up. | "Days to complete"
[/TABLE]

[TABLE]
Field | Type | Description | Example value
color | string(enum) | The color of the option. Possible values:blue,brown,default,gray,green,orange,pink,purple,red,yellow | "red"
id | string | An identifier for the option. Does not change if the name is changed. | "ff8e9269-9579-47f7-8f6e-83a84716863c"
name | string | The name of the option as it appears in Notion. Commas are not valid. Names must be unique (case-insensitive). | "Fruit"
[/TABLE]

[TABLE]
Field | Type | Description | Example value
color | string(enum) | The color of the option. Possible values:blue,brown,default,gray,green,orange,pink,purple,red,yellow | "green"
id | string | An identifier for the option. | "ff8e9269-9579-47f7-8f6e-83a84716863c"
name | string | The name of the option as it appears in Notion. Commas are not valid. Names must be unique (case-insensitive). | "In progress"
[/TABLE]

[TABLE]
Field | Type | Description | Example value
color | string(enum) | The color of the group. Possible values:blue,brown,default,gray,green,orange,pink,purple,red,yellow | "purple"
id | string | An identifier for the group. | "ff8e9269-9579-47f7-8f6e-83a84716863c"
name | string | The name of the group as it appears in Notion. | "To do"
option_ids | array of strings | Sorted list ofids of options that belong to this group. | 
[/TABLE]

[TABLE]
Field | Type | Description | Example value
prefix | stringornull | A common prefix assigned to pages. When set, enables lookup URLs likenotion.so/TASK-1234. | "TASK"
[/TABLE]