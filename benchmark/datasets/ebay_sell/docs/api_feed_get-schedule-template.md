# getScheduleTemplate

This method retrieves the details of the specified template. Specify the template to retrieve using the <strong>schedule_template_id</strong> path parameter. Use the <strong>getScheduleTemplates</strong> method to find a schedule template if you do not know the <strong>schedule_template_id</strong>.

## Endpoint

```
GET /schedule_template/{schedule_template_id}
```

## API

Feed API (v1)

## Authentication

Requires OAuth 2.0 authentication with appropriate scopes.

## Path Parameters

- **schedule_template_id** (required): This path parameter is the unique identifier of the schedule template being retrieved.<br><br>Use the <a href="/api-docs/sell/feed/resources/schedule/methods/getScheduleTemplates" target="_blank ">getScheduleTemplates</a> method to retrieve schedule template IDs.<br><br><span class="tablenote"><b>Note:</b> Template schedules are currently only available for <code>LMS_ORDER_REPORT</code>.</span> (Type: `string`)

## Response

**200**: Success

Response schema: `#/components/schemas/ScheduleTemplateResponse`

## Example

```bash
curl -X GET \
  https://api.ebay.com/schedule_template/{schedule_template_id} \
  -H "Authorization: Bearer YOUR_OAUTH_TOKEN" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json"
```

## Tags

schedule

## Reference

- [eBay Feed API Documentation](https://developer.ebay.com/api-docs/sell/feed/overview.html)
