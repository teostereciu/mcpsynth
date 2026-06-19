# view

*Source: https://developers.notion.com/reference/view*

---

##### Notion API

##### Objects

##### Endpoints

##### Webhook events

## ​Supported view types

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
- Databases (deprecated)
- Comments
- Views
- File Uploads
- Search
- Users
- File uploads
- Supported view types
- Object fields

[TABLE]
Type | Description
table | Rows-and-columns spreadsheet layout.
board | Kanban board grouped by a property.
calendar | Calendar layout grouped by a date property.
timeline | Gantt-style timeline layout.
gallery | Card grid with cover images.
list | Simple list layout.
form | Form view for data entry.
chart | Chart visualization.
map | Map view with location pins.
dashboard | Multi-widget dashboard containing other views.
[/TABLE]

[TABLE]
Field | Type | Description
object | "view" | Always"view".
id | UUID | The ID of the view.
parent | Object | The parent database. Containstype: "database_id"anddatabase_id.
data_source_id | String | null | The ID of the data source this view is scoped to, ornullfor dashboard views.
name | String | The display name of the view.
type | String | One of thesupported view types.
query_filter | Object | null | Thefilterapplied to this view, ornullif no query_filter is set.
sort_rules | Array | null | Thesortsapplied to this view, ornullif no sort_rules are set.
configuration | Object | null | View-specific layout configuration, discriminated bytype. SeeWorking with viewsfor details.
created_time | String | ISO 8601 timestamp when the view was created.
created_by | Object | null | Partialuserwho created the view.
last_edited_time | String | ISO 8601 timestamp when the view was last edited.
last_edited_by | Object | null | Partialuserwho last edited the view.
url | String | Deep link to the view in Notion.
dashboard_view_id | String | Only present for widget views inside a dashboard. The ID of the parent dashboard view.
[/TABLE]