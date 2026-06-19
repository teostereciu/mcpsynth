# updateSchedule

This method updates an existing schedule. Specify the schedule to update using the <strong>schedule_id</strong> path parameter. If the schedule template has changed after the schedule was created or updated, the input will be validated using the changed template.<p> <span class="tablenote"><strong>Note:</strong> Make sure to include all fields required by the schedule template (<strong>scheduleTemplateId</strong>). Call the <strong>getScheduleTemplate</strong> method (or the <strong>getScheduleTemplates</strong> method), to find out which fields are required or optional. If you do not know the <strong>scheduleTemplateId</strong>, call the <strong>getSchedule</strong> method to find out.</span></p>

## Endpoint

```
PUT /schedule/{schedule_id}
```

## API

Feed API (v1)

## Authentication

Requires OAuth 2.0 authentication with appropriate scopes.

## Path Parameters

- **schedule_id** (required): This path parameter is the unique identifier of the schedule being updated. <br><br> Use the <a href="/api-docs/sell/feed/resources/schedule/methods/getSchedules" target="_blank ">getSchedules</a> method to retrieve schedule IDs. (Type: `string`)

## Headers

- **Content-Type** (required): This header indicates the format of the request body provided by the client. Its value should be set to <b>application/json</b>. <br><br> For more information, refer to <a href="/api-docs/static/rest-request-components.html#HTTP" target="_blank ">HTTP request headers</a>. (Type: `string`)

### Request Body

See schema: `#/components/schemas/UpdateUserScheduleRequest`


## Response

**204**: No Content

## Example

```bash
curl -X PUT \
  https://api.ebay.com/schedule/{schedule_id} \
  -H "Authorization: Bearer YOUR_OAUTH_TOKEN" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json"
```

## Tags

schedule

## Reference

- [eBay Feed API Documentation](https://developer.ebay.com/api-docs/sell/feed/overview.html)
