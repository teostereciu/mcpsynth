# changes-by-version

*Source: https://developers.notion.com/reference/changes-by-version*

---

##### Notion API

##### Objects

##### Endpoints

##### Webhook events
- Status
- Community
- Blog
- Introduction
- Integration capabilities
- Webhooks
- Request limits
- Status codes
- VersioningOverviewChanges by version
- Overview
- Changes by version
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

[TABLE]
Version | Breaking changes
2026-03-11 | Theafterparameter on Append Block Children is replaced by apositionobject. Thearchivedfield is removed in favor ofin_trashacross all request parameters and response bodies. Thetranscriptionblock type is renamed tomeeting_notes.SeeUpgrading to 2026-03-11for details.
2025-09-03 | /v1/databasesAPIs are re-organized into/v1/data_sources(for managing individual data sources under a database container) and/v1/databases(for managing the database container.)Existing database IDs stay the same, but a new concept of data source IDs is introduced, and required in order to manage data source properties, to support multi-source databases (new in the Notion app as of September 2025.)SeechangelogandUpgrading to 2025-09-03guide for more details.
2022-06-28 | Page properties must be retrieved using the page properties endpoint.Parents are now always direct parents; a parent field has been added to block.Database relations have a type ofsingle_propertyanddual_property.Seechangelogfor more details.
2022-02-22 | Seechangelog.
2021-08-16 | TheAppend block childrenendpoint returns a list of newBlock objectchildren instead of the parent block.Array rollup property types changed fromfile,textandpersontofiles,rich_textandpeople.Property IDs are now encoded to be URL safe.Empty number, email, select, date, and rollup properties are now returned in page responses asnull.More information
2021-05-13 | Rich text property values use the typerich_textinstead oftext.Migration details
[/TABLE]