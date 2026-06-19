# intro

*Source: https://developers.notion.com/reference/intro*

---

##### Notion API

##### Objects

##### Endpoints

##### Webhook events

## ​Conventions

### ​JSON conventions

## ​Code samples & SDKs

## ​Pagination

### ​Supported endpoints

### ​Responses

### ​Parameters for paginated requests

### ​How to send a paginated request

#### ​Example: paginate through query results from a data source

```
curl-XPOST'https://api.notion.com/v1/data_sources/<data_source_id>/query'\-H'Authorization: Bearer <secret_bot>'\-H'Notion-Version: 2026-03-11'\-H'Content-Type: application/json'\--data'{"page_cursor": "33e19cb9-751f-4993-b74d-234d67d0d534"}'
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
- Conventions
- JSON conventions
- Code samples & SDKs
- Pagination
- Supported endpoints
- Responses
- Parameters for paginated requests
- How to send a paginated request
- Example: paginate through query results from a data source
- Top-level resources have an"object"property. This property can be used to determine the type of the resource (e.g."database","user", etc.)
- Top-level resources are addressable by a UUIDv4"id"property. You may omit dashes from the ID when making requests to the API, e.g. when copying the ID from a Notion URL.
- Property names are insnake_case(notcamelCaseorkebab-case).
- Temporal values (dates and datetimes) are encoded inISO 8601strings. Datetimes will include the time value (2020-08-12T02:12:33.231Z) while dates will include only the date (2020-08-12)
- The Notion API does not support empty strings. To unset a string value for properties like aurlpage property value, for example, use an explicitnullinstead of"".

[TABLE]
HTTP method | Endpoint
GET | List all users
GET | List block children
GET | List comments
GET | Retrieve a page property item
GET | List file uploads
GET | List data source templates
GET | List views
GET | Get view query results
POST | Query a data source
POST | Create a view query
POST | Search
[/TABLE]

[TABLE]
Field | Type | Description
has_more | boolean | Whether the response includes the end of the list.falseif there are no more results. Otherwise,true.
next_cursor | string | A string that can be used to retrieve the next page of results by passing the value as thestart_cursorparameterto the same endpoint.Only available whenhas_moreis true.
object | "list" | The constant string"list".
results | array of objects | The list, or partial list, of endpoint-specific results. Refer to asupported endpoint’s individual documentation for details.
type | "block""comment""data_source""file_upload""page""page_or_database""property_item""template""user""view" | A constant string that represents the type of the objects inresults.
{type} | paginated list object | An object containing type-specific pagination information. Forproperty_items, the value corresponds to thepaginated page property type. For all other types, the value is an empty object.
[/TABLE]

[TABLE]
Parameter | Type | Description
results_per_page | number | The number of items from the full list to include in the response.Default:100Maximum:100The response may contain fewer than the default number of results.
page_cursor | string | Anext_cursorvalue returned in a previousresponse. Treat this as an opaque value.Defaults toundefined, which returns results from the beginning of the list.
[/TABLE]