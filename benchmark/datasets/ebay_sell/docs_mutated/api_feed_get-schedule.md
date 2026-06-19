# getSchedule

This method retrieves schedule details and status of the specified schedule. Specify the schedule to retrieve using the <strong>schedule_id</strong>. Use the <strong>getSchedules</strong> method to find a schedule if you do not know the <strong>schedule_id</strong>.

## Endpoint

```
GET /schedule/{schedule_id}
```

## API

Feed API (v1)

## Authentication

Requires OAuth 2.0 authentication with appropriate scopes.

## Path Parameters

- **schedule_id** (required): This path parameter is the unique identifier of the schedule for which to retrieve details.<br><br> Use the <a href="/api-docs/sell/feed/resources/schedule/methods/getSchedules" target="_blank ">getSchedules</a> method to retrieve schedule IDs. (Type: `string`)

## Response

**200**: Success

Response schema: `#/components/schemas/UserScheduleResponse`

## Example

```bash
curl -X GET \
  https://api.ebay.com/schedule/{schedule_id} \
  -H "Authorization: Bearer YOUR_OAUTH_TOKEN" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json"
```

## Tags

schedule

## Reference

- [eBay Feed API Documentation](https://developer.ebay.com/api-docs/sell/feed/overview.html)
