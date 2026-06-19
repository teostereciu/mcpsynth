# app_rate_limited

*Source: https://docs.slack.dev/reference/events/app_rate_limited*

---

## Facts

**Required Scopes**

No scopes required!

**Compatible APIs**

[`Events`](/apis/events-api)

## Usage info​

This Events API-only event type has no "inner event". Instead, the complete payload you'll receive is similar to this JSON:


    {
        "token": "Jhj5dZrVaK7ZwHHjRyZWjbDl",
        "type": "app_rate_limited",
        "team_id": "T123456",
        "minute_rate_limited": 1518467820,
        "api_app_id": "A123456"
    }


This event type is only dispatched when your app is rate limited on the Events API. Rate limiting currently occurs when your app would receive more than 30,000 events in an hour from a single workspace.Property| Description| `token`| The same shared token that once was used to verify other events in the Events API. This is deprecated in favor of [signed secrets](/authentication/verifying-requests-from-slack).| `type`| This specific event type, `app_rate_limited`.| `minute_rate_limited`| A rounded epoch time value indicating the minute your application became rate limited for this workspace. `1518467820` is at 2018-02-12 20:37:00 UTC.| `team_id`| Subscriptions between your app and the workspace with this ID are being rate limited.| `api_app_id`| Your application's ID, especially useful if you have multiple applications working with the Events API.
---|---

This event does not require a specific OAuth scope or subscription. You'll automatically receive it when your app's event subscriptions are rate limited or disabled.

Event subscriptions may be limited and disabled when your app does not respond with a HTTP 200 OK to at 5% of event deliveries in the past 60 minutes.

[Learn more about Events API rate limiting](/apis/events-api/#rate_limiting).