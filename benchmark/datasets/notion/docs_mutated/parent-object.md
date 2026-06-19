# parent-object

*Source: https://developers.notion.com/reference/parent-object*

---

##### Notion API

##### Objects

##### Endpoints

##### Webhook events

### ​Database parent

### ​Data source parent

### ​Page parent

### ​Workspace parent

### ​Block parent

```
{"type":"database_id","database_id":"d9824bdc-8445-4327-be8b-5b47500af6ce"}
```

```
{"type":"data_source_id","data_source_id":"1a44be12-0953-4631-b498-9e5817518db8","database_id":"d9824bdc-8445-4327-be8b-5b47500af6ce"}
```

```
{"type":"page_id","page_id":"59833787-2cf9-4fdf-8782-e53db20768a5"}
```

```
{"type":"workspace","workspace":true}
```

```
{"type":"block_id","block_id":"7d50a184-5bbe-4d90-8f29-6bec57ed817b"}
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
- Databases (deprecated)
- Comments
- Views
- File Uploads
- Search
- Users
- File uploads
- Database parent
- Data source parent
- Page parent
- Workspace parent
- Block parent
- Pages can be parented by other pages, data sources, blocks, or by the whole workspace.Prior toAPI version 2025-09-03, page parents were databases, not data sources.
- Blocks can be parented by pages, data sources, or blocks.
- Databases can be parented by pages, blocks, or by the whole workspace.For wikis, databases can also have a data source parent.
- Data sources are parented by databases.Linked or externally synced external data sources may have data source parents, but aren’t thoroughly supported in Notion’s API.
- Prior toAPI version 2025-09-03, page parents were databases, not data sources.
- For wikis, databases can also have a data source parent.
- Linked or externally synced external data sources may have data source parents, but aren’t thoroughly supported in Notion’s API.

[TABLE]
Property | Type | Description | Example values
type | string | Always"database_id". | "database_id"
database_id | string(UUIDv4) | The ID of thedatabasethat this page belongs to. | "b8595b75-abd1-4cad-8dfe-f935a8ef57cb"
[/TABLE]

[TABLE]
Property | Type | Description | Example values
type | string | Always"data_source_id". | "data_source_id"
data_source_id | string(UUIDv4) | The ID of thedata sourcethat this page belongs to. | "1a44be12-0953-4631-b498-9e5817518db8"
database_id | string(UUIDv4) | The ID of thedatabasethat the data source belongs to, provided in the API response for convenience. | "b8595b75-abd1-4cad-8dfe-f935a8ef57cb"
[/TABLE]

[TABLE]
Property | Type | Description | Example values
type | string | Always"page_id". | "page_id"
page_id | string(UUIDv4) | The ID of thepagethat this page belongs to. | "59833787-2cf9-4fdf-8782-e53db20768a5"
[/TABLE]

[TABLE]
Property | Type | Description | Example values
type | type | Always"workspace". | "workspace"
workspace | boolean | Alwaystrue. | true
[/TABLE]

[TABLE]
Property | Type | Description | Example values
type | type | Always"block_id". | "block_id"
block_id | string(UUIDv4) | The ID of thepagethat this page belongs to. | "ea29285f-7282-4b00-b80c-32bdbab50261"
[/TABLE]