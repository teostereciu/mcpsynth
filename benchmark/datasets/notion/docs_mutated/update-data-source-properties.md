# update-data-source-properties

*Source: https://developers.notion.com/reference/update-data-source-properties*

---

##### Notion API

##### Objects

##### Endpoints

##### Webhook events

## ​Remove a property

## ​Rename a property

## ​Update property type

### ​Select configuration updates

#### ​Existing select options

### ​Multi-select configuration updates

#### ​Existing multi-select options

### ​Status configuration updates

#### ​Existing status options

## ​Limitations

### ​Formula maximum depth

### ​Unsupported Rollup Aggregations

### ​“Could not find page/data source” Error

### ​Property value doesn’t match UI after pagination

```
"properties": {"J@cT":null,}
```

```
"properties": {"propertyToDelete":null}
```

```
"properties": {"J@cT": {"name":"New Property Name"}}
```

```
"properties": {"Old Property Name": {"name":"New Property Name}}
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
- Data sourcesPOSTCreate a data sourceGETRetrieve a data sourceGETList data source templatesUpdate a data sourcePATCHUpdate a data sourceUpdate data source propertiesQuery a data source
- Databases (deprecated)
- Comments
- Views
- File Uploads
- Search
- Users
- POSTCreate a data source
- GETRetrieve a data source
- GETList data source templates
- Update a data sourcePATCHUpdate a data sourceUpdate data source properties
- Query a data source
- PATCHUpdate a data source
- Update data source properties
- Data sources
- File uploads
- Remove a property
- Rename a property
- Update property type
- Select configuration updates
- Existing select options
- Multi-select configuration updates
- Existing multi-select options
- Status configuration updates
- Existing status options
- Limitations
- Formula maximum depth
- Unsupported Rollup Aggregations
- “Could not find page/data source” Error
- Property value doesn’t match UI after pagination
- show_unique(Show unique values)
- unique(Count unique values)
- median(Median)

[TABLE]
Property | Type | Description
name | string | The name of the property as it appears in Notion.
[/TABLE]

[TABLE]
Property | Type | Description | Example value
options | optional array ofexisting select optionsandselect option objects | Settings for select properties. If an existing option is omitted, it will be removed from the data source property. New options will be added to the data source property. | 
[/TABLE]

[TABLE]
Property | Type | Description | Example value
name | optionalstring | Name of the option. | "Fruit"
id | optionalstring | ID of the option. | "ff8e9269-9579-47f7-8f6e-83a84716863c"
[/TABLE]

[TABLE]
Property | Type | Description | Example value
options | optional array ofexisting select optionsandmulti-select option objects | Settings for multi select properties. If an existing option is omitted, it will be removed from the data source property. New options will be added to the data source property. | 
[/TABLE]

[TABLE]
Property | Type | Description | Example value
name | string | Name of the option as it appears in Notion. | "Fruit"
id | optionalstring | ID of the option. | "ff8e9269-9579-47f7-8f6e-83a84716863c"
[/TABLE]

[TABLE]
Property | Type | Description | Example value
options | optional array ofexisting status optionsandstatus option objects | Settings for status properties. If an existing option is omitted, it will be removed from the data source property. New options will be added to the “To-do” group. | 
[/TABLE]

[TABLE]
Property | Type | Description | Example value
name | optionalstring | Name of the option. | "In progress"
id | optionalstring | ID of the option. | "ff8e9269-9579-47f7-8f6e-83a84716863c"
[/TABLE]