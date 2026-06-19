# webhooks-events-delivery

*Source: https://developers.notion.com/reference/webhooks-events-delivery*

---

##### Notion API

##### Objects

##### Endpoints

##### Webhook events

## ​Event types

### ​Event properties

### ​Supported webhook event types

## ​Event delivery

### ​Event aggregation

### ​Event ordering

### ​Delivery retries

## ​Sample event payloads

### ​page.created

### ​page.properties_updated

### ​page.content_updated

### ​page.moved

### ​page.deleted

### ​page.undeleted

### ​page.locked

### ​page.unlocked

### ​database.created

### ​database.content_updated

### ​database.moved

### ​database.deleted

### ​database.undeleted

### ​database.schema_updated

### ​data_source.content_updated

### ​data_source.created

### ​data_source.deleted

### ​data_source.moved

### ​data_source.schema_updated

### ​data_source.undeleted

### ​comment.created

### ​comment.updated

### ​comment.deleted

```
{"id":"367cba44-b6f3-4c92-81e7-6a2e9659efd4","timestamp":"2024-12-05T23:55:34.285Z","workspace_id":"13950b26-c203-4f3b-b97d-93ec06319565","workspace_name":"Quantify Labs","subscription_id":"29d75c0d-5546-4414-8459-7b7a92f1fc4b","integration_id":"0ef2e755-4912-8096-91c1-00376a88a5ca","type":"page.created","authors": [{"id":"c7c11cca-1d73-471d-9b6e-bdef51470190","type":"person"}],"accessible_by": [{"id":"556a1abf-4f08-40c6-878a-75890d2a88ba","type":"person"},{"id":"1edc05f6-2702-81b5-8408-00279347f034","type":"bot"}],"attempt_number":1,"entity": {"id":"153104cd-477e-809d-8dc4-ff2d96ae3090","type":"page"},"data": {"parent": {"id":"0ef104cd-477e-80e1-8571-cfd10e92339a","type":"page"}}}
```

```
{"id":"1782edd6-a853-4d4a-b02c-9c8c16f28e53","timestamp":"2024-12-05T23:57:05.379Z","workspace_id":"13950b26-c203-4f3b-b97d-93ec06319565","workspace_name":"Quantify Labs","subscription_id":"29d75c0d-5546-4414-8459-7b7a92f1fc4b","integration_id":"0ef2e755-4912-8096-91c1-00376a88a5ca","type":"page.properties_updated","authors": [{"id":"c7c11cca-1d73-471d-9b6e-bdef51470190","type":"person"}],"accessible_by": [{"id":"556a1abf-4f08-40c6-878a-75890d2a88ba","type":"person"},{"id":"1edc05f6-2702-81b5-8408-00279347f034","type":"bot"}],"attempt_number":1,"entity": {"id":"153104cd-477e-809d-8dc4-ff2d96ae3090","type":"page"},"data": {"parent": {"id":"13950b26-c203-4f3b-b97d-93ec06319565","type":"space"},"updated_properties": ["XGe%40","bDf%5B","DbAu"]}}
```

```
{"id":"56c3e00c-4f0c-4566-9676-4b058a50a03d","timestamp":"2024-12-05T19:49:36.997Z","workspace_id":"13950b26-c203-4f3b-b97d-93ec06319565","workspace_name":"Quantify Labs","subscription_id":"29d75c0d-5546-4414-8459-7b7a92f1fc4b","integration_id":"0ef2e755-4912-8096-91c1-00376a88a5ca","type":"page.content_updated","authors": [{"id":"c7c11cca-1d73-471d-9b6e-bdef51470190","type":"person"}],"accessible_by": [{"id":"556a1abf-4f08-40c6-878a-75890d2a88ba","type":"person"},{"id":"1edc05f6-2702-81b5-8408-00279347f034","type":"bot"}],"attempt_number":1,"entity": {"id":"0ef104cd-477e-80e1-8571-cfd10e92339a","type":"page"},"data": {"updated_blocks": [{"id":"153104cd-477e-80ec-a87d-f7ff0236d35c","type":"block"}],"parent": {"id":"0ef104cd-477e-80e1-8571-cfd10e92339a","type":"page"}}}
```

```
{"id":"7de99a6f-2edd-4116-bf59-2d09407bddec","timestamp":"2024-12-11T05:43:14.383Z","workspace_id":"13950b26-c203-4f3b-b97d-93ec06319565","workspace_name":"Quantify Labs","subscription_id":"29d75c0d-5546-4414-8459-7b7a92f1fc4b","integration_id":"0ef2e755-4912-8096-91c1-00376a88a5ca","type":"page.moved","authors": [{"id":"c7c11cca-1d73-471d-9b6e-bdef51470190","type":"person"}],"accessible_by": [{"id":"556a1abf-4f08-40c6-878a-75890d2a88ba","type":"person"},{"id":"1edc05f6-2702-81b5-8408-00279347f034","type":"bot"}],"attempt_number":1,"entity": {"id":"154104cd-477e-8030-9989-d4daf352d900","type":"page"},"data": {"parent": {"id":"0ef104cd-477e-80e1-8571-cfd10e92339a","type":"page"}}}
```

```
{"id":"ea6b8136-1db6-4f2e-b157-84a532437f62","timestamp":"2024-12-05T23:59:31.215Z","workspace_id":"13950b26-c203-4f3b-b97d-93ec06319565","workspace_name":"Quantify Labs","subscription_id":"29d75c0d-5546-4414-8459-7b7a92f1fc4b","integration_id":"0ef2e755-4912-8096-91c1-00376a88a5ca","type":"page.deleted","authors": [{"id":"c7c11cca-1d73-471d-9b6e-bdef51470190","type":"person"}],"accessible_by": [{"id":"556a1abf-4f08-40c6-878a-75890d2a88ba","type":"person"},{"id":"1edc05f6-2702-81b5-8408-00279347f034","type":"bot"}],"attempt_number":1,"entity": {"id":"153104cd-477e-8001-935c-c4b11828dfbd","type":"page"},"data": {"parent": {"id":"0ef104cd-477e-80e1-8571-cfd10e92339a","type":"page"}}}
```

```
{"id":"ec37232c-a17b-4f02-bb7c-8d8e1f5f2250","timestamp":"2024-12-06T00:00:03.356Z","workspace_id":"13950b26-c203-4f3b-b97d-93ec06319565","workspace_name":"Quantify Labs","subscription_id":"29d75c0d-5546-4414-8459-7b7a92f1fc4b","integration_id":"0ef2e755-4912-8096-91c1-00376a88a5ca","type":"page.undeleted","authors": [{"id":"c7c11cca-1d73-471d-9b6e-bdef51470190","type":"person"}],"accessible_by": [{"id":"556a1abf-4f08-40c6-878a-75890d2a88ba","type":"person"},{"id":"1edc05f6-2702-81b5-8408-00279347f034","type":"bot"}],"attempt_number":1,"entity": {"id":"153104cd-477e-8001-935c-c4b11828dfbd","type":"page"},"data": {"parent": {"id":"0ef104cd-477e-80e1-8571-cfd10e92339a","type":"page"}}}
```

```
{"id":"e2a3092c-5af0-442f-9d11-b813145edb72","timestamp":"2024-12-06T00:00:56.480Z","workspace_id":"13950b26-c203-4f3b-b97d-93ec06319565","workspace_name":"Quantify Labs","subscription_id":"29d75c0d-5546-4414-8459-7b7a92f1fc4b","integration_id":"0ef2e755-4912-8096-91c1-00376a88a5ca","type":"page.locked","authors": [{"id":"c7c11cca-1d73-471d-9b6e-bdef51470190","type":"person"}],"accessible_by": [{"id":"556a1abf-4f08-40c6-878a-75890d2a88ba","type":"person"},{"id":"1edc05f6-2702-81b5-8408-00279347f034","type":"bot"}],"attempt_number":1,"entity": {"id":"153104cd-477e-8001-935c-c4b11828dfbd","type":"page"},"data": {"parent": {"id":"0ef104cd-477e-80e1-8571-cfd10e92339a","type":"page"}}}
```

```
{"id":"d0bd8927-0826-4db0-9e26-83d57253f1ff","timestamp":"2024-12-05T23:50:35.868Z","workspace_id":"13950b26-c203-4f3b-b97d-93ec06319565","workspace_name":"Quantify Labs","subscription_id":"29d75c0d-5546-4414-8459-7b7a92f1fc4b","integration_id":"0ef2e755-4912-8096-91c1-00376a88a5ca","type":"database.created","authors": [{"id":"c7c11cca-1d73-471d-9b6e-bdef51470190","type":"person"}],"accessible_by": [{"id":"556a1abf-4f08-40c6-878a-75890d2a88ba","type":"person"},{"id":"1edc05f6-2702-81b5-8408-00279347f034","type":"bot"}],"attempt_number":1,"entity": {"id":"153104cd-477e-80eb-ae76-e1c2a32c7b35","type":"database"},"data": {"parent": {"id":"153104cd-477e-803a-88dc-caececf26478","type":"page"}}}
```

```
{"id":"25e44fe0-6785-45bb-adc2-a321526c12c5","timestamp":"2024-12-13T17:48:13.700Z","workspace_id":"13950b26-c203-4f3b-b97d-93ec06319565","workspace_name":"Quantify Labs","subscription_id":"29d75c0d-5546-4414-8459-7b7a92f1fc4b","integration_id":"0ef2e755-4912-8096-91c1-00376a88a5ca","type":"database.content_updated","authors": [{"id":"c7c11cca-1d73-471d-9b6e-bdef51470190","type":"person"}],"accessible_by": [{"id":"556a1abf-4f08-40c6-878a-75890d2a88ba","type":"person"},{"id":"1edc05f6-2702-81b5-8408-00279347f034","type":"bot"}],"attempt_number":1,"entity": {"id":"15b104cd-477e-80c2-84a0-c32cefba5cff","type":"database"},"data": {"updated_blocks": [{"id":"15b104cd-477e-80a4-bff3-cd05428a4d55","type":"block"},{"id":"15b104cd-477e-80be-98e7-cdf0897fa5c9","type":"block"}],"parent": {"id":"0ef104cd-477e-80e1-8571-cfd10e92339a","type":"page"}}}
```

```
{"id":"f9c70013-d79d-4c4e-8d5b-939429949a2e","timestamp":"2024-12-06T06:54:08.468Z","workspace_id":"13950b26-c203-4f3b-b97d-93ec06319565","workspace_name":"Quantify Labs","subscription_id":"29d75c0d-5546-4414-8459-7b7a92f1fc4b","integration_id":"0ef2e755-4912-8096-91c1-00376a88a5ca","type":"database.moved","authors": [{"id":"c7c11cca-1d73-471d-9b6e-bdef51470190","type":"person"}],"accessible_by": [{"id":"556a1abf-4f08-40c6-878a-75890d2a88ba","type":"person"},{"id":"1edc05f6-2702-81b5-8408-00279347f034","type":"bot"}],"attempt_number":1,"entity": {"id":"153104cd-477e-80eb-ae76-e1c2a32c7b35","type":"database"},"data": {"parent": {"id":"0ef104cd-477e-80e1-8571-cfd10e92339a","type":"page"}}}
```

```
{"id":"c00e2ea7-032a-4e20-ae05-d69028a09ae9","timestamp":"2024-12-05T23:51:27.295Z","workspace_id":"13950b26-c203-4f3b-b97d-93ec06319565","workspace_name":"Quantify Labs","subscription_id":"29d75c0d-5546-4414-8459-7b7a92f1fc4b","integration_id":"0ef2e755-4912-8096-91c1-00376a88a5ca","type":"database.deleted","authors": [{"id":"c7c11cca-1d73-471d-9b6e-bdef51470190","type":"person"}],"accessible_by": [{"id":"556a1abf-4f08-40c6-878a-75890d2a88ba","type":"person"},{"id":"1edc05f6-2702-81b5-8408-00279347f034","type":"bot"}],"attempt_number":1,"entity": {"id":"153104cd-477e-80eb-ae76-e1c2a32c7b35","type":"database"},"data": {"parent": {"id":"0ef104cd-477e-80e1-8571-cfd10e92339a","type":"page"}}}
```

```
{"id":"edd8ff6e-0f07-4621-934b-76ca55129cc2","timestamp":"2024-12-05T23:52:16.149Z","workspace_id":"13950b26-c203-4f3b-b97d-93ec06319565","workspace_name":"Quantify Labs","subscription_id":"29d75c0d-5546-4414-8459-7b7a92f1fc4b","integration_id":"0ef2e755-4912-8096-91c1-00376a88a5ca","type":"database.undeleted","authors": [{"id":"c7c11cca-1d73-471d-9b6e-bdef51470190","type":"person"}],"accessible_by": [{"id":"556a1abf-4f08-40c6-878a-75890d2a88ba","type":"person"},{"id":"1edc05f6-2702-81b5-8408-00279347f034","type":"bot"}],"attempt_number":1,"entity": {"id":"153104cd-477e-80eb-ae76-e1c2a32c7b35","type":"database"},"data": {"parent": {"id":"0ef104cd-477e-80e1-8571-cfd10e92339a","type":"page"}}}
```

```
{"id":"5496f509-6988-4bab-b6a9-bdce0b720ca0","timestamp":"2024-12-05T23:55:22.243Z","workspace_id":"13950b26-c203-4f3b-b97d-93ec06319565","workspace_name":"Quantify Labs","subscription_id":"29d75c0d-5546-4414-8459-7b7a92f1fc4b","integration_id":"0ef2e755-4912-8096-91c1-00376a88a5ca","type":"database.schema_updated","authors": [{"id":"c7c11cca-1d73-471d-9b6e-bdef51470190","type":"person"}],"accessible_by": [{"id":"556a1abf-4f08-40c6-878a-75890d2a88ba","type":"person"},{"id":"1edc05f6-2702-81b5-8408-00279347f034","type":"bot"}],"attempt_number":1,"entity": {"id":"153104cd-477e-80eb-ae76-e1c2a32c7b35","type":"database"},"data": {"parent": {"id":"0ef104cd-477e-80e1-8571-cfd10e92339a","type":"page"},"updated_properties": [{"id":"kqLW","name":"Created at","action":"created"},{"id":"wX%7Bd","name":"Blurb","action":"updated"},{"id":"LIM%5D","name":"Description","action":"deleted"}],}}
```

```
{"id":"6f6469cb-8022-409d-a560-62e631a84d74","timestamp":"2025-09-03T17:24:49.997Z","workspace_id":"13950b26-c203-4f3b-b97d-93ec06319565","workspace_name":"Quantify Labs","subscription_id":"29d75c0d-5546-4414-8459-7b7a92f1fc4b","integration_id":"0ef2e755-4912-8096-91c1-00376a88a5ca","authors": [{"id":"c7c11cca-1d73-471d-9b6e-bdef51470190","type":"person"}],"attempt_number":1,"api_version":"2025-09-03","entity": {"id":"263104cd-477e-804b-8c32-000b2fcd241a","type":"data_source"},"type":"data_source.created","data": {"parent": {"id":"153104cd-477e-803a-88dc-caececf26478","type":"page"}}}
```

```
{"id":"4e443c81-a332-40af-9300-c7eb6e514737","timestamp":"2025-09-03T17:54:38.833Z","workspace_id":"13950b26-c203-4f3b-b97d-93ec06319565","workspace_name":"Quantify Labs","subscription_id":"29d75c0d-5546-4414-8459-7b7a92f1fc4b","integration_id":"0ef2e755-4912-8096-91c1-00376a88a5ca","authors": [{"id":"c7c11cca-1d73-471d-9b6e-bdef51470190","type":"person"}],"attempt_number":1,"api_version":"2025-09-03","entity": {"id":"263104cd-477e-804b-8c32-000b2fcd241a","type":"data_source"},"type":"data_source.deleted","data": {"parent": {"id":"263104cd-477e-80ef-8afe-c488d39a5cdb","type":"page"}}}
```

```
{"id":"b6cc0a2c-f8f6-440b-920d-e3d6d7cf2e44","timestamp":"2025-09-03T17:49:13.978Z","workspace_id":"13950b26-c203-4f3b-b97d-93ec06319565","workspace_name":"Quantify Labs","subscription_id":"29d75c0d-5546-4414-8459-7b7a92f1fc4b","integration_id":"0ef2e755-4912-8096-91c1-00376a88a5ca","authors": [{"id":"c7c11cca-1d73-471d-9b6e-bdef51470190","type":"person"}],"attempt_number":1,"api_version":"2025-09-03","entity": {"id":"263104cd-477e-8025-aae1-000b58fc5834","type":"data_source"},"type":"data_source.moved","data": {"parent": {"id":"263104cd-477e-80ef-8afe-c488d39a5cdb","type":"database"}}}
```

```
{"id":"afc2475f-aaeb-4a69-8158-b654ba4bc47b","timestamp":"2025-09-03T17:55:42.075Z","workspace_id":"13950b26-c203-4f3b-b97d-93ec06319565","workspace_name":"Quantify Labs","subscription_id":"29d75c0d-5546-4414-8459-7b7a92f1fc4b","integration_id":"0ef2e755-4912-8096-91c1-00376a88a5ca","authors": [{"id":"c7c11cca-1d73-471d-9b6e-bdef51470190","type":"person"}],"attempt_number":1,"api_version":"2025-09-03","entity": {"id":"263104cd-477e-8025-aae1-000b58fc5834","type":"data_source"},"type":"data_source.undeleted","data": {"parent": {"id":"153104cd-477e-803a-88dc-caececf26478","type":"page"}}}
```

```
{"id":"c6780f24-10b7-4f42-a6fd-230b6cf7ad69","timestamp":"2024-12-05T20:46:45.854Z","workspace_id":"13950b26-c203-4f3b-b97d-93ec06319565","workspace_name":"Quantify Labs","subscription_id":"29d75c0d-5546-4414-8459-7b7a92f1fc4b","integration_id":"0ef2e755-4912-8096-91c1-00376a88a5ca","type":"comment.created","authors": [{"id":"c7c11cca-1d73-471d-9b6e-bdef51470190","type":"person"}],"accessible_by": [{"id":"556a1abf-4f08-40c6-878a-75890d2a88ba","type":"person"},{"id":"1edc05f6-2702-81b5-8408-00279347f034","type":"bot"}],"attempt_number":1,"entity": {"id":"153104cd-477e-80ca-8f75-001d9e2b6839","type":"comment"},"data": {"page_id":"0ef104cd-477e-80e1-8571-cfd10e92339a","parent": {"id":"0ef104cd-477e-80e1-8571-cfd10e92339a","type":"page"}}}
```

```
{"id":"9cf67341-47d7-43f7-be6f-24b49dcc335b","timestamp":"2024-12-05T20:48:00.550Z","workspace_id":"13950b26-c203-4f3b-b97d-93ec06319565","workspace_name":"Quantify Labs","subscription_id":"29d75c0d-5546-4414-8459-7b7a92f1fc4b","integration_id":"0ef2e755-4912-8096-91c1-00376a88a5ca","type":"comment.created","authors": [{"id":"c7c11cca-1d73-471d-9b6e-bdef51470190","type":"person"}],"accessible_by": [{"id":"556a1abf-4f08-40c6-878a-75890d2a88ba","type":"person"},{"id":"1edc05f6-2702-81b5-8408-00279347f034","type":"bot"}],"attempt_number":1,"entity": {"id":"153104cd-477e-8071-b16a-001d9a35ad84","type":"comment"},"data": {"page_id":"0ef104cd-477e-80e1-8571-cfd10e92339a","parent": {"id":"153104cd-477e-803a-88dc-caececf26478","type":"block"}}}
```

```
{"id":"68ad06e4-5b68-498d-8812-9a1d3e069e46","timestamp":"2024-12-05T20:47:22.657Z","workspace_id":"13950b26-c203-4f3b-b97d-93ec06319565","workspace_name":"Quantify Labs","subscription_id":"29d75c0d-5546-4414-8459-7b7a92f1fc4b","integration_id":"0ef2e755-4912-8096-91c1-00376a88a5ca","type":"comment.updated","authors": [{"id":"c7c11cca-1d73-471d-9b6e-bdef51470190","type":"person"}],"accessible_by": [{"id":"556a1abf-4f08-40c6-878a-75890d2a88ba","type":"person"},{"id":"1edc05f6-2702-81b5-8408-00279347f034","type":"bot"}],"attempt_number":1,"entity": {"id":"153104cd-477e-80ca-8f75-001d9e2b6839","type":"comment"},"data": {"page_id":"0ef104cd-477e-80e1-8571-cfd10e92339a","parent": {"id":"0ef104cd-477e-80e1-8571-cfd10e92339a","type":"page"}}}
```

```
{"id":"aa4436d0-6694-49ad-aabb-55c6307f091b","timestamp":"2024-12-05T20:49:08.688Z","workspace_id":"13950b26-c203-4f3b-b97d-93ec06319565","workspace_name":"Quantify Labs","subscription_id":"29d75c0d-5546-4414-8459-7b7a92f1fc4b","integration_id":"0ef2e755-4912-8096-91c1-00376a88a5ca","type":"comment.deleted","authors": [{"id":"c7c11cca-1d73-471d-9b6e-bdef51470190","type":"person"}],"accessible_by": [{"id":"556a1abf-4f08-40c6-878a-75890d2a88ba","type":"person"},{"id":"1edc05f6-2702-81b5-8408-00279347f034","type":"bot"}],"attempt_number":1,"entity": {"id":"153104cd-477e-8071-b16a-001d9a35ad84","type":"comment"},"data": {"page_id":"0ef104cd-477e-80e1-8571-cfd10e92339a","parent": {"id":"153104cd-477e-803a-88dc-caececf26478","type":"block"}}}
```
- Status
- Community
- Blog
- Introduction
- Integration capabilities
- WebhooksOverviewEvent types & delivery
- Request limits
- Status codes
- Versioning
- Overview
- Event types & delivery
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
- Event types
- Event properties
- Supported webhook event types
- Event delivery
- Event aggregation
- Event ordering
- Delivery retries
- Sample event payloads
- page.created
- page.properties_updated
- page.content_updated
- page.moved
- page.deleted
- page.undeleted
- page.locked
- page.unlocked
- database.created
- database.content_updated
- database.moved
- database.deleted
- database.undeleted
- database.schema_updated
- data_source.content_updated
- data_source.created
- data_source.deleted
- data_source.moved
- data_source.schema_updated
- data_source.undeleted
- comment.created
- comment.updated
- comment.deleted

[TABLE]
Field | Type | Description
id | UUID | The unique ID of the webhook event
timestamp | String | ISO 8601 formatted time at which the event occurred. This field can be used to order events on your side
workspace_id | UUID | The workspace ID where the event originated from
subscription_id | UUID | The ID of the webhook subscription
integration_id | UUID | Associated integration ID the subscription is set up with
type | String | Type of the event, e.g.page.created
authors | Array | Array of objects with the ID (id) and type (type) of the author who performed the action.typecan be"person","bot", or"agent". Typically an array of length 1; can be more for aggregated events. Seebotorpersonfor details retrievable by ID in theUsers API.
accessible_by | Array | Array of objects with the ID (id) and type (type) of each accessible bot and user who owns the bot connection to theintegration_idand has access to the webhook’sentity. Only for public integrations.typecan be"person"or"bot".
attempt_number | number | Attempt number (1-8) of the current event delivery
entity | Object | ID (id) and type (type) of the object that triggered the event.typecan be"page","block", or"database".
data | Object | Additional, event-specific data.
[/TABLE]

[TABLE]
Type | Description | Is aggregated?
page.content_updated | Triggered when the content of a page changes — for example adding or removing a block on the page. | Yes
page.created | Triggered when a new page is created. | Yes
page.deleted | Triggered when a page is moved to the trash. | Yes
page.locked | Triggered when a page is locked from editing. | No
page.moved | Triggered when a page is moved to another location. | Yes
page.properties_updated | Triggered when a page’s property is updated. | Yes
page.undeleted | Triggered when a page is restored from the trash. | Yes
page.unlocked | Triggered when a page is unlocked | No
database.content_updated | Triggered when a database’s content is updated— for example, adding or removing a child page.Deprecatedin 2025-09-03 API version. | Yes
database.created | Triggered when a new database is created. | Yes
database.deleted | Triggered when a database is moved to the trash. | Yes
database.moved | Triggered when a database is moved to another location. | Yes
database.schema_updated | Triggered when a database’s schema is updated — for example, adding or removing a database property.Deprecatedin 2025-09-03 API version. | Yes
database.undeleted | Triggered when a database is restored from the trash. | Yes
data_source.content_updated | Triggered when a data source’s content is updated— for example, adding or removing a child page.Newin 2025-09-03 API version. | Yes
data_source.created | Triggered when a new data source is created within an existing database.Newin 2025-09-03 API version. | Yes
data_source.deleted | Triggered when a data source is moved to the trash.Newin 2025-09-03 API version. | Yes
data_source.moved | Triggered when a data source is moved to another database.Newin 2025-09-03 API version. | Yes
data_source.schema_updated | Triggered when a data source’s schema is updated — for example, adding or removing a database property.Newin 2025-09-03 API version. | Yes
data_source.undeleted | Triggered when a data source is restored from the trash.Newin 2025-09-03 API version. | Yes
comment.created | Triggered when a new comment or suggested edit is added to a page or block | No
comment.deleted | Triggered when a comment is deleted. | No
comment.updated | Triggered when a comment is edited. | No
[/TABLE]