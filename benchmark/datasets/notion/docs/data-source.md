# data-source

*Source: https://developers.notion.com/reference/data-source*

---

##### Notion API

##### Objects

##### Endpoints

##### Webhook events

## ​Object fields
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
- Object fields
- Create a data source: add an additional data source for an existingDatabase
- Update a data source: update attributes, such as theproperties, of a data source
- Retrieve a data source
- Query a data source

[TABLE]
Field | Type | Description | Example value
object* | string | Always"data_source". | "data_source"
id* | string(UUID) | Unique identifier for the data source. | "2f26ee68-df30-4251-aad4-8ddc420cba3d"
properties* | object | Schema of properties for the data source as they appear in Notion.keystring The name of the property as it appears in Notion.valueobject AProperty object. | 
parent | object | Information about the data source’s parent database. SeeParent object. | {"type": "database_id", "database_id": "842a0286-cef0-46a8-abba-eac4c8ca644e"}
database_parent | object | Information about the database’s parent (in other words, the the data source’s grandparent). SeeParent object. | { "type": "page_id", "page_id": "af5f89b5-a8ff-4c56-a5e8-69797d11b9f8" }
created_time | string(ISO 8601 date and time) | Date and time when this data source was created. Formatted as anISO 8601 date timestring. | "2020-03-17T19:10:04.968Z"
created_by | Partial User | User who created the data source. | {"object": "user", "id": "45ee8d13-687b-47ce-a5ca-6e2e45548c4b"}
last_edited_time | string(ISO 8601 date and time) | Date and time when this data source was updated. Formatted as anISO 8601 date timestring. | "2020-03-17T21:49:37.913Z"
last_edited_by | Partial User | User who last edited the data source. | {"object": "user","id": "45ee8d13-687b-47ce-a5ca-6e2e45548c4b"}
title | array ofrich text objects | Name of the data source as it appears in Notion. Seerich text object) for a breakdown of the properties. | [ { "type": "text", "text": { "content": "Can I create a URL property", "link": null }, "annotations": { "bold": false, "italic": false, "strikethrough": false, "underline": false, "code": false, "color": "default" }, "plain_text": "Can I create a URL property", "href": null } ]
description | array ofrich text objects | Description of the data source as it appears in Notion. Seerich text object) for a breakdown of the properties. | 
icon | File ObjectorEmoji object | Data source icon. | 
archived | boolean | Deprecated.Usein_trashinstead. This is an alias forin_trashand always returns the same value. | false
in_trash | boolean | Whether the data source has been trashed. | false
[/TABLE]