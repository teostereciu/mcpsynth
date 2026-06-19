# deleteSchedule

This method deletes an existing schedule. Specify the schedule to delete using the <strong>schedule_id</strong> path parameter.

## Endpoint

```
DELETE /schedule/{schedule_id}
```

## API

Feed API (v1)

## Authentication

Requires OAuth 2.0 authentication with appropriate scopes.

## Path Parameters

- **schedule_id** (required): This path parameter is the unique identifier of the schedule being deleted.<br><br>Use the <a href="/api-docs/sell/feed/resources/schedule/methods/getSchedules" target="_blank ">getSchedules</a> method to retrieve schedule IDs. (Type: `string`)

## Response

**204**: No Content

## Example

```bash
curl -X DELETE \
  https://api.ebay.com/schedule/{schedule_id} \
  -H "Authorization: Bearer YOUR_OAUTH_TOKEN" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json"
```

## Tags

schedule

## Reference

- [eBay Feed API Documentation](https://developer.ebay.com/api-docs/sell/feed/overview.html)
