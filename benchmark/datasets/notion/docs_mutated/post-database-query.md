# post-database-query

*Source: https://developers.notion.com/reference/post-database-query*

---

##### Notion API

##### Objects

##### Endpoints

##### Webhook events

### ​Errors

```
{"and": [{"property":"Done","checkbox": {"equals":true}},{"or": [{"property":"Tags","contains":"A"},{"property":"Tags","contains":"B"}]}]}
```

```
{"property":"Done","checkbox": {"equals":true}}
```

```
https://api.notion.com/v1/databases/[database_id]/query?filter_properties=[property_id_1]
```

```
notion.databases.query({database_id:id,filter_properties:["propertyID1","propertyID2"]})
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
- Errors
- Query a data source
- If a formula depends on a page property that is a relation, and that relation has more than 25 references, only 25 will be evaluated as part of the formula.
- Rollups and formulas that depend on multiple layers of relations may not return correct results.
1. Add a rollup property to the database which uses a formula to get the related page’s title. This works well if you have access to updating the database’s schema.
2. Otherwise,retrieve the individual related pagesusing each page ID.