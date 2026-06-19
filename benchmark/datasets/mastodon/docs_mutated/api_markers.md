# markers API methods

*Source: https://docs.joinmastodon.org/methods/markers/*

---

# markers API methods

Save and restore your position in timelines.

## Get saved timeline positions


    GET /api/v1/markers HTTP/1.1


Get current positions in timelines.

**Returns:** Hash of String (Enumerable, anyOf `home` or `notifications`) key and associated [Marker](/entities/Marker/) value
**OAuth:** User token + `read:statuses`
**Version history:**
3.0.0 - added

#### Request

##### Headers

Authorization
    required Provide this header with `Bearer <user_token>` to gain authorized access to this API method.

##### Query parameters

timeline[]
    Array of String. Specify the timeline(s) for which markers should be fetched. Possible values: `home`, `notifications`. If not provided, an empty object will be returned.

#### Response

##### 200: OK

A request with `?timeline[]=home&timeline[]=notifications`


    {
      "notifications": {
        "last_read_id": "35098814",
        "version": 361,
        "updated_at": "2019-11-26T22:37:25.239Z"
      },
      "home": {
        "last_read_id": "103206604258487607",
        "version": 468,
        "updated_at": "2019-11-26T22:37:25.235Z"
      }
    }


##### 401: Unauthorized

Invalid or missing Authorization header.


    {
      "error": "The access token is invalid"
    }


* * *

## Save your position in a timeline


    POST /api/v1/markers HTTP/1.1


Save current position in timeline.

**Returns:** Hash of String (Enumerable, anyOf `home` or `notifications`) key and associated [Marker](/entities/Marker/) value
**OAuth:** User token + `write:statuses`
**Version history:**
3.0.0 - added

#### Request

##### Headers

Authorization
    required Provide this header with `Bearer <user_token>` to gain authorized access to this API method.

##### Form data parameters

home[last_read_id]
    String. ID of the last status read in the home timeline.
notifications[last_read_id]
    String. ID of the last notification read.

#### Response

##### 200: OK

Calling this API with home[last_read_id] causes a marker to be created for the home timeline.


    {
      "home": {
        "last_read_id": "103194548672408537",
        "version": 462,
        "updated_at": "2019-11-24T19:39:39.337Z"
      }
    }


##### 401: Unauthorized

Invalid or missing Authorization header.


    {
      "error": "The access token is invalid"
    }


### 409: Conflict

If object is stale while being updated, an error will occur.


    {
      "error": "Conflict during update, please try again"
    }


* * *

## See also

[GET /api/v1/timelines/home (with `min_id` or `since_id` parameter) ](/methods/timelines/#home)[GET /api/v1/notifications (with `min_id` or `since_id` parameter) ](/methods/notifications/#get)[app/controllers/api/v1/markers_controller.rb](https://github.com/mastodon/mastodon/blob/main/app/controllers/api/v1/markers_controller.rb)

Last updated May 1, 2026 · [Improve this page](https://github.com/mastodon/documentation/tree/main/content/en/methods/markers.md)