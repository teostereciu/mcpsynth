# database

*Source: https://developers.notion.com/reference/database*

---

##### Notion API

##### Objects

##### Endpoints

##### Webhook events

## ​Object fields

## Data source

## Data source properties

## Page
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
- Database
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
- Databases (deprecated)
- Comments
- Views
- File Uploads
- Search
- Users
- File uploads
- Object fields

[TABLE]
Field | Type | Description | Example value
object | string | Always"database". | "database"
id | string(UUID) | Unique identifier for the database. | "2f26ee68-df30-4251-aad4-8ddc420cba3d"
data_sources | array of data source objects | List of child data sources, each of which is a JSON object with anidandname.UseRetrieve a data sourceto get more details on the data source, including itsproperties. | [{"id": "c174b72c-d782-432f-8dc0-b647e1c96df6", "name": "Tasks data source"}]
created_time | string(ISO 8601 date and time) | Date and time when this database was created. Formatted as anISO 8601 date timestring. | "2020-03-17T19:10:04.968Z"
created_by | Partial User | User who created the database. | {"object": "user","id": "45ee8d13-687b-47ce-a5ca-6e2e45548c4b"}
last_edited_time | string(ISO 8601 date and time) | Date and time when this database was updated. Formatted as anISO 8601 date timestring. | "2020-03-17T21:49:37.913Z"
last_edited_by | Partial User | User who last edited the database. | {"object": "user","id": "45ee8d13-687b-47ce-a5ca-6e2e45548c4b"}
title | array ofrich text objects | Name of the database as it appears in Notion. Seerich text object) for a breakdown of the properties. | "title": [ { "type": "text", "text": { "content": "Can I create a URL property", "link": null }, "annotations": { "bold": false, "italic": false, "strikethrough": false, "underline": false, "code": false, "color": "default" }, "plain_text": "Can I create a URL property", "href": null } ]
description | array ofrich text objects | Description of the database as it appears in Notion. Seerich text object) for a breakdown of the properties. | 
icon | File ObjectorEmoji object | Page icon. | 
cover | File object | Page cover image. | 
parent | object | Information about the database’s parent. SeeParent object. | { "type": "page_id", "page_id": "af5f89b5-a8ff-4c56-a5e8-69797d11b9f8" }
url | string | The URL of the Notion database. | "https://www.notion.so/668d797c76fa49349b05ad288df2d136"
archived | boolean | Deprecated.Usein_trashinstead. This is an alias forin_trashand always returns the same value. | false
in_trash | boolean | Whether the database has been trashed. | false
is_inline | boolean | Has the valuetrueif the database appears in the page as an inline block. Otherwise has the valuefalseif the database appears as a child page. | false
public_url | string | The public page URL if the page has been published to the web. Otherwise,null. | "https://jm-testing.notion.site/p1-6df2c07bfc6b4c46815ad205d132e22d"1
[/TABLE]