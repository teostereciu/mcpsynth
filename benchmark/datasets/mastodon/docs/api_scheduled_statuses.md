# scheduled_statuses API methods

*Source: https://docs.joinmastodon.org/methods/scheduled_statuses/*

---

# scheduled_statuses API methods

Manage statuses that were scheduled to be published at a future date.

## View scheduled statuses


    GET /api/v1/scheduled_statuses HTTP/1.1


**Returns:** Array of [ScheduledStatus](/entities/ScheduledStatus/)
**OAuth:** User token + `read:statuses`
**Version history:**
2.7.0 - added
3.3.0 - both `min_id` and `max_id` can be used at the same time now

#### Request

##### Headers

Authorization
    required Provide this header with `Bearer <user_token>` to gain authorized access to this API method.

##### Query parameters

max_id
    String. All results returned will be lesser than this ID. In effect, sets an upper bound on results.
since_id
    String. All results returned will be greater than this ID. In effect, sets a lower bound on results.
min_id
    String. Returns results immediately newer than this ID. In effect, sets a cursor at this ID and paginates forward.
limit
    Integer. Maximum number of results to return. Defaults to 20 statuses. Max 40 statuses.

#### Response

##### 200: OK


    [
      {
        "id": "3221",
        "scheduled_at": "2019-12-05T12:33:01.000Z",
        "params": {
          "poll": null,
          "text": "test content",
          "media_ids": null,
          "sensitive": null,
          "visibility": null,
          "idempotency": null,
          "scheduled_at": null,
          "spoiler_text": null,
          "application_id": 596551,
          "in_reply_to_id": null
        },
        "media_attachments": []
      }
    ]


##### 401: Unauthorized

Invalid or missing Authorization header.


    {
      "error": "The access token is invalid"
    }


* * *

## View a single scheduled status


    GET /api/v1/scheduled_statuses/:id HTTP/1.1


**Returns:** [ScheduledStatus](/entities/ScheduledStatus/)
**OAuth:** User token + `read:statuses`
**Version history:**
2.7.0 - added

#### Request

##### Path parameters

:id
    required String. The ID of the ScheduledStatus in the database.

##### Headers

Authorization
    required Provide this header with `Bearer <user_token>` to gain authorized access to this API method.

#### Response

##### 200: OK


    {
      "id": "3221",
      "scheduled_at": "2019-12-05T12:33:01.000Z",
      "params": {
        "poll": null,
        "text": "test content",
        "media_ids": null,
        "sensitive": null,
        "visibility": null,
        "idempotency": null,
        "scheduled_at": null,
        "spoiler_text": null,
        "application_id": 596551,
        "in_reply_to_id": null
      },
      "media_attachments": []
    }


##### 401: Unauthorized

Invalid or missing Authorization header.


    {
      "error": "The access token is invalid"
    }


##### 404: Not found

ScheduledStatus is not owned by you or does not exist


    {
      "error": "Record not found"
    }


* * *

## Update a scheduled status’s publishing date


    PUT /api/v1/scheduled_statuses/:id HTTP/1.1


**Returns:** [ScheduledStatus](/entities/ScheduledStatus/)
**OAuth:** User token + `write:statuses`
**Version history:**
2.7.0 - added

#### Request

##### Path parameters

:id
    required String. The ID of the ScheduledStatus in the database.

##### Headers

Authorization
    required Provide this header with `Bearer <user_token>` to gain authorized access to this API method.

##### Form data parameters

scheduled_at
    String. [Datetime](/api/datetime-format/#datetime) at which the status will be published. Must be at least 5 minutes into the future.

#### Response

##### 200: OK


    {
      "id": "3221",
      "scheduled_at": "2019-12-05T13:33:01.000Z",
      "params": {
        "poll": null,
        "text": "test content",
        "media_ids": null,
        "sensitive": null,
        "visibility": null,
        "idempotency": null,
        "scheduled_at": null,
        "spoiler_text": null,
        "application_id": 596551,
        "in_reply_to_id": null
      },
      "media_attachments": []
    }


##### 401: Unauthorized

Invalid or missing Authorization header.


    {
      "error": "The access token is invalid"
    }


##### 404: Not found

ScheduledStatus is not owned by you or does not exist


    {
      "error": "Record not found"
    }


##### 422: Unprocessable entity


    {
      "error": "Validation failed: Scheduled at The scheduled date must be in the future"
    }


* * *

## Cancel a scheduled status


    DELETE /api/v1/scheduled_statuses/:id HTTP/1.1


**Returns:** Empty
**OAuth:** User token + `write:statuses`
**Version history:**
2.7.0 - added

#### Request

##### Path parameters

:id
    required String. The ID of the ScheduledStatus in the database.

##### Headers

Authorization
    required Provide this header with `Bearer <user_token>` to gain authorized access to this API method.

#### Response

##### 200: OK


    {}


##### 401: Unauthorized

Invalid or missing Authorization header.


    {
      "error": "The access token is invalid"
    }


##### 404: Not found

ScheduledStatus is not owned by you or does not exist


    {
      "error": "Record not found"
    }


* * *

## See also

[POST /api/v1/statuses (`scheduled_at` parameter) ](/methods/statuses/#create)[app/controllers/api/v1/scheduled_statuses_controller.rb](https://github.com/mastodon/mastodon/blob/main/app/controllers/api/v1/scheduled_statuses_controller.rb)

Last updated May 1, 2026 · [Improve this page](https://github.com/mastodon/documentation/tree/main/content/en/methods/scheduled_statuses.md)