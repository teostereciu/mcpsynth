# query-a-data-source

*Source: https://developers.notion.com/reference/query-a-data-source*

---

##### Notion API

##### Objects

##### Endpoints

##### Webhook events

### ​Overview

### ​Filtering

### ​Sorting

### ​Recommendations for performance

### ​Other important details and tips

### ​Errors

#### Authorizations

#### Headers

#### Path Parameters

#### Query Parameters

#### Body

#### Response
Bearer authentication header of the formBearer <token>, where<token>is your auth token.
TheAPI versionto use for this request. The latest version is2026-03-11.
Showchild attributes
Optionally filter the results to only include pages or data sources. Regular, non-wiki databases only support page children. The default behavior is no result type filtering, in other words, returning both pages and data sources for wikis.

```
import{Client}from"@notionhq/client"constnotion=newClient({auth:process.env.NOTION_API_KEY})constresponse=awaitnotion.dataSources.query({data_source_id:"d9824bdc-8445-4327-be8b-5b47500af6ce",filter:{property:"Status",select:{equals:"Done"}},sorts:[{property:"Created",direction:"descending"}]})
```

```
{"type":"<string>","page_or_data_source": {},"object":"<string>","next_cursor":"<string>","has_more":true,"results": [{"object":"<string>","id":"3c90c3cc-0d44-4b50-8888-8dd25736052a","created_time":"2023-11-07T05:31:56Z","last_edited_time":"2023-11-07T05:31:56Z","in_trash":true,"is_archived":true,"is_locked":true,"url":"<string>","public_url":"<string>","parent": {"type":"<string>","database_id":"3c90c3cc-0d44-4b50-8888-8dd25736052a"},"properties": {},"icon": {"type":"<string>","emoji":"<string>"},"cover": {"type":"<string>","file": {"url":"<string>","expiry_time":"2023-11-07T05:31:56Z"}},"created_by": {"id":"3c90c3cc-0d44-4b50-8888-8dd25736052a","object":"<string>"},"last_edited_by": {"id":"3c90c3cc-0d44-4b50-8888-8dd25736052a","object":"<string>"}}]}
```

```
{"and": [{"property":"Done","checkbox": {"equals":true}},{"or": [{"property":"Tags","contains":"A"},{"property":"Tags","contains":"B"}]}]}
```

```
{"property":"Done","checkbox": {"equals":true}}
```

```
https://api.notion.com/v1/data_sources/[DATA_SOURCE_ID]/query?filter_properties[]=title
```

```
notion.dataSources.query({data_source_id:id,filter_properties:["title","status"]})
```

```
{"object":"error","status":503,"code":"service_unavailable","message":"Public API data source query is temporarily unavailable due to backend datastore timeouts. Retry with exponential backoff; if retries continue to fail, reduce page_size or narrow filters/sorts.","additional_data": {"endpoint_name":"public_queryDataSource","notion_error_name":"PgPoolWaitConnectionTimeout","retry_guidance": ["Use exponential backoff with jitter","Reduce page_size","Narrow query filters/sorts"]}}
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
- Data sourcesPOSTCreate a data sourceGETRetrieve a data sourceGETList data source templatesUpdate a data sourceQuery a data sourcePOSTQuery a data sourceFilter data source entriesSort data source entries
- Databases (deprecated)
- Comments
- Views
- File Uploads
- Search
- Users
- POSTCreate a data source
- GETRetrieve a data source
- GETList data source templates
- Update a data source
- Query a data sourcePOSTQuery a data sourceFilter data source entriesSort data source entries
- POSTQuery a data source
- Filter data source entries
- Sort data source entries
- Data sources
- File uploads
- Using more specific filter conditions to reduce the result set, e.g. a more specific title query or a shorter time window.
- Dividing large data sources (ones with more than several dozen thousand pages) into multiple; e.g. splitting a “tasks” database into “Tasks” and “Bugs”.
- Pruning data source schemas to remove any complex formulas, rollups, two-way relations, or other properties that are no longer in use.
- Setting upintegration webhooksto reduce the need for polling this API by instead automatically notifying your system of incremental workspace events.
- If a formula depends on a page property that is a relation, and that relation has more than 25 references, only 25 will be evaluated as part of the formula.
- Rollups and formulas that depend on multiple layers of relations may not return correct results.
- Notion recommends individuallyretrieving each page property itemto get the most accurate result.
- Option 1
- Option 2
- Title
- Rich Text
- Number
- Checkbox
- Select
- Multi Select
- Date
- People
- Files
- Url
- Email
- Phone Number
- Relation
- Created By
- Created Time
- Last Edited By
- Last Edited Time
- Formula
- Unique Id
- Rollup
- Verification
- Option 3
- Option 4
1. Add a rollup property to the data source which uses a formula to get the related page’s title. This works well if you have access toupdatethe data source’s schema.
2. Otherwise,retrieve the individual related pagesusing each page ID.