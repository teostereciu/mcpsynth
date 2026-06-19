# filters API methods

*Source: https://docs.joinmastodon.org/methods/filters/*

---

# filters API methods

Create and manage filters.

## Server-side (v2) methods

Since Mastodon 4.0, filters can contain multiple keywords and are matched server-side. Clients apply the filter action based on [the status’s `filtered` attribute](/entities/Status/#filtered).

* * *

### View all filters


    GET /api/v2/filters HTTP/1.1


Obtain a list of all filter groups for the current user.

**Returns:** Array of [Filter](/entities/Filter/)
**OAuth:** User token + `read:filters`
**Version history:**
4.0.0 - added

#### Request

##### Headers

Authorization
    required Provide this header with `Bearer <user_token>` to gain authorized access to this API method.

#### Response

##### 200: OK


    [
      {
        "id": "20060",
        "title": "Remove Twitter crossposts from public timeline",
        "context": [
          "public"
        ],
        "expires_at": null,
        "filter_action": "hide",
        "keywords": [
            {
              "id": "1311",
              "keyword": "from birdsite",
              "whole_word": true
            },
            {
              "id": "1324",
              "keyword": "@twitter.com",
              "whole_word": false
            },
            {
              "id": "1325",
              "keyword": "https://t.co/",
              "whole_word": false
            }
        ],
        "statuses": []
      },
      // ...
    ]


##### 401: Unauthorized

Invalid or missing Authorization header.


    {
      "error": "The access token is invalid"
    }


* * *

### View a specific filter


    GET /api/v2/filters/:id HTTP/1.1


Obtain a single filter group owned by the current user.

**Returns:** [Filter](/entities/Filter/)
**OAuth:** User token + `read:filters`
**Version history:**
4.0.0 - added

#### Request

##### Path parameters

:id
    required String. The ID of the Filter in the database.

##### Headers

Authorization
    required Provide this header with `Bearer <user_token>` to gain authorized access to this API method.

#### Response

##### 200: OK


    {
      "id": "20060",
      "title": "Remove Twitter crossposts from public timeline",
      "context": [
        "public"
      ],
      "expires_at": null,
      "filter_action": "hide",
      "keywords": [
        {
          "id": "1311",
          "keyword": "from birdsite",
          "whole_word": true
        },
        {
          "id": "1324",
          "keyword": "@twitter.com",
          "whole_word": false
        },
        {
          "id": "1325",
          "keyword": "https://t.co/",
          "whole_word": false
        }
      ],
      "statuses": []
    }


##### 401: Unauthorized

Invalid or missing Authorization header.


    {
      "error": "The access token is invalid"
    }


##### 404: Not found

Filter is not owned by you or does not exist


    {
      "error": "Record not found"
    }


* * *

### Create a filter


    POST /api/v2/filters HTTP/1.1


Create a filter group with the given parameters.

**Returns:** [Filter](/entities/Filter/)
**OAuth:** User token + `write:filters`
**Version history:**
4.0.0 - added
4.4.0 (`mastodon` [API version](/entities/Instance/#api-versions) 5) - added `blur` value to `filter_action` attribute

#### Request

##### Headers

Authorization
    required Provide this header with `Bearer <user_token>` to gain authorized access to this API method.

##### Form data parameters

title
    required String. The name of the filter group.
context[]
    required Array of String. Where the filter should be applied. Specify at least one of `home`, `notifications`, `public`, `thread`, `account`.
filter_action
    String. The policy to be applied when the filter is matched. Specify `warn`, `hide` or `blur`.
expires_in
    Integer. How many seconds from now should the filter expire? Defaults to never expire.
keywords_attributes[][keyword]
    String. A keyword to be added to the newly-created filter group.
keywords_attributes[][whole_word]
    Boolean. Whether the keyword should consider word boundaries.

#### Response

##### 200: OK

Sample of a Filter created by the call:


    POST https://mastodon.example/api/v2/filters
    ?title=test
    &context[]=public
    &keywords_attributes[][keyword]=foo
    &keywords_attributes[][whole_word]=false
    &keywords_attributes[][keyword]=bar
    &keywords_attributes[][whole_word]=true


    {
      "id": "25933",
      "title": "test",
      "context": [
        "public"
      ],
      "expires_at": null,
      "filter_action": "warn",
      "keywords": [
        {
          "id": "34978",
          "keyword": "foo",
          "whole_word": false
        },
        {
          "id": "34979",
          "keyword": "bar",
          "whole_word": true
        }
      ],
      "statuses": []
    }


##### 401: Unauthorized

Invalid or missing Authorization header.


    {
      "error": "The access token is invalid"
    }


##### 404: Not found

Filter keyword ID was specified


    {
      "error": "Record not found"
    }


##### 422: Unprocessable entity


    {
      "error": "Validation failed: Title can't be blank, Context can't be blank, Context None or invalid context supplied"
    }


* * *

### Update a filter


    PUT /api/v2/filters/:id HTTP/1.1


Update a filter group with the given parameters.

**Returns:** [Filter](/entities/Filter/)
**OAuth:** User token + `write:filters`
**Version history:**
4.0.0 - added
4.4.0 (`mastodon` [API version](/entities/Instance/#api-versions) 5) - added `blur` value to `filter_action` attribute

#### Request

##### Path parameters

:id
    required String. The ID of the Filter in the database.

##### Headers

Authorization
    required Provide this header with `Bearer <user_token>` to gain authorized access to this API method.

##### Form data parameters

title
    String. The name of the filter group.
context[]
    Array of String. Where the filter should be applied. Specify at least one of `home`, `notifications`, `public`, `thread`, `account`.
filter_action
    String. The policy to be applied when the filter is matched. Specify `warn`, `hide` or `blur`.
expires_in
    Integer. How many seconds from now should the filter expire?
keywords_attributes[][keyword]
    String. A keyword to be added to the newly-created filter group.
keywords_attributes[][whole_word]
    Boolean. Whether the keyword should consider word boundaries.
keywords_attributes[][id]
    String. Provide the ID of an existing keyword to modify it, instead of creating a new keyword.
keywords_attributes[][_destroy]
    Boolean. If true, will remove the keyword with the given ID.

#### Response

##### 200: OK

Sample call:


    PUT /api/v2/filters/25933
    ?keywords_attributes[][id]=34978
    &keywords_attributes[][_destroy]=true
    &keywords_attributes[][id]=34979
    &keywords_attributes[][keyword]=baz


This will remove keyword 34978 (“foo”) and will replace keyword 34979 (“bar”) with a new keyword (“baz”)


    {
      "id": "25933",
      "title": "test",
      "context": [
        "public"
      ],
      "expires_at": null,
      "filter_action": "warn",
      "keywords": [
        {
          "id": "34979",
          "keyword": "baz",
          "whole_word": true
        }
      ],
      "statuses": []
    }


##### 401: Unauthorized

Invalid or missing Authorization header.


    {
      "error": "The access token is invalid"
    }


##### 404: Not found

Filter is not owned by you or does not exist. Alternatively, `keywords_attributes[][id]` was provided, there is no keyword with given id within this Filter.


    {
      "error": "Record not found"
    }


* * *

### Delete a filter


    DELETE /api/v2/filters/:id HTTP/1.1


Delete a filter group with the given id.

**Returns:** Empty
**OAuth:** User token + `write:filters`
**Version history:**
4.0.0 - added

##### Path parameters

:id
    required String. The ID of the Filter in the database.

##### Headers

Authorization
    required Provide this header with `Bearer <user_token>` to gain authorized access to this API method.

#### Response

##### 200: OK

Filter successfully deleted


    {}


##### 401: Unauthorized

Invalid or missing Authorization header.


    {
      "error": "The access token is invalid"
    }


##### 404: Not found

Filter is not owned by you or does not exist


    {
      "error": "Record not found"
    }


* * *

### View keywords added to a filter


    GET /api/v2/filters/:filter_id/keywords HTTP/1.1


List all keywords attached to the current filter group.

**Returns:** Array of [FilterKeyword](/entities/FilterKeyword/)
**OAuth:** User token + `read:filters`
**Version history:**
4.0.0 - added

#### Request

##### Path parameters

:filter_id
    required String. The ID of the Filter in the database.

##### Headers

Authorization
    required Provide this header with `Bearer <user_token>` to gain authorized access to this API method.

#### Response

##### 200: OK


    [
      {
        "id": "34979",
        "keyword": "baz",
        "whole_word": true
      },
      // ...
    ]


##### 401: Unauthorized

Invalid or missing Authorization header.


    {
      "error": "The access token is invalid"
    }


##### 404: Not found

Filter is not owned by you, or does not exist


    {
      "error": "Record not found"
    }


* * *

### Add a keyword to a filter


    POST /api/v2/filters/:filter_id/keywords HTTP/1.1


Add the given keyword to the specified filter group

**Returns:** [FilterKeyword](/entities/FilterKeyword/)
**OAuth:** User token + `write:filters`
**Version history:**
4.0.0 - added

#### Request

##### Path parameters

:filter_id
    required String. The ID of the Filter in the database.

##### Headers

Authorization
    required Provide this header with `Bearer <user_token>` to gain authorized access to this API method.

##### Form data parameters

keyword
    required String. The keyword to be added to the filter group.
whole_word
    Boolean. Whether the keyword should consider word boundaries.

#### Response

##### 200: OK


    {
      "id": "35583",
      "keyword": "some",
      "whole_word": false
    }


##### 401: Unauthorized

Invalid or missing Authorization header.


    {
      "error": "The access token is invalid"
    }


##### 404: Not found

Filter is not owned by you, or does not exist


    {
      "error": "Record not found"
    }


##### 422: Unprocessable entity

No keyword was provided


    {
      "error": "Validation failed: Keyword can't be blank"
    }


* * *

### View a single keyword


    GET /api/v2/filters/keywords/:id HTTP/1.1


Get one filter keyword by the given id.

**Returns:** [FilterKeyword](/entities/FilterKeyword/)
**OAuth:** User token + `read:filters`
**Version history:**
4.0.0 - added

#### Request

##### Path parameters

:id
    required String. The ID of the FilterKeyword in the database.

##### Headers

Authorization
    required Provide this header with `Bearer <user_token>` to gain authorized access to this API method.

#### Response

##### 200: OK


    {
      "id": "34979",
      "keyword": "baz",
      "whole_word": true
    }


##### 401: Unauthorized

Invalid or missing Authorization header.


    {
      "error": "The access token is invalid"
    }


##### 404: Not found

Filter is not owned by you, or the filter or filter keyword does not exist


    {
      "error": "Record not found"
    }


* * *

### Edit a keyword within a filter


    PUT /api/v2/filters/keywords/:id HTTP/1.1


Update the given filter keyword.

**Returns:** [FilterKeyword](/entities/FilterKeyword/)
**OAuth:** User token + `write:filters`
**Version history:**
4.0.0 - added

#### Request

##### Path parameters

:id
    required String. The ID of the FilterKeyword in the database.

##### Headers

Authorization
    required Provide this header with `Bearer <user_token>` to gain authorized access to this API method.

##### Form data parameters

keyword
    required String. The keyword to be added to the filter group.
whole_word
    Boolean. Whether the keyword should consider word boundaries.

#### Response

##### 200: OK

The keyword “some” was updated to the keyword “other”


    {
      "id": "35583",
      "keyword": "other",
      "whole_word": false
    }


##### 401: Unauthorized

Invalid or missing Authorization header.


    {
      "error": "The access token is invalid"
    }


##### 404: Not found

FilterKeyword is not owned by you, or does not exist


    {
      "error": "Record not found"
    }


##### 422: Unprocessable entity

No keyword was provided


    {
      "error": "Validation failed: Keyword can't be blank"
    }


* * *

### Remove keywords from a filter


    DELETE /api/v2/filters/keywords/:id HTTP/1.1


Deletes the given filter keyword.

**Returns:** Empty
**OAuth:** User token + `write:filters`
**Version history:**
4.0.0 - added

#### Request

##### Path parameters

:id
    required String. The ID of the FilterKeyword in the database.

##### Headers

Authorization
    required Provide this header with `Bearer <user_token>` to gain authorized access to this API method.

#### Response

##### 200: OK

FilterKeyword was deleted successfully


    {}


##### 401: Unauthorized

Invalid or missing Authorization header.


    {
      "error": "The access token is invalid"
    }


##### 404: Not found

FilterKeyword is not owned by you or does not exist


    {
      "error": "Record not found"
    }


* * *

### View all status filters


    GET /api/v2/filters/:filter_id/statuses HTTP/1.1


Obtain a list of all status filters within this filter group.

**Returns:** Array of [FilterStatus](/entities/FilterStatus/)
**OAuth:** User token + `read:filters`
**Version history:**
4.0.0 - added

#### Request

##### Path parameters

:filter_id
    required String. The ID of the Filter in the database.

##### Headers

Authorization
    required Provide this header with `Bearer <user_token>` to gain authorized access to this API method.

#### Response

##### 200: OK


    [
      {
        "id": "897",
        "status_id": "109416512469928632"
      },
      // ...
    ]


##### 401: Unauthorized

Invalid or missing Authorization header.


    {
      "error": "The access token is invalid"
    }


##### 404: Not found

Filter is not owned by you or does not exist


    {
      "error": "Record not found"
    }


* * *

### Add a status to a filter group


    POST /api/v2/filters/:filter_id/statuses HTTP/1.1


Add a status filter to the current filter group.

**Returns:** [FilterStatus](/entities/FilterStatus/)
**OAuth:** User token + `write:filters`
**Version history:**
4.0.0 - added

#### Request

##### Path parameters

:filter_id
    required String. The ID of the Filter in the database.

##### Headers

Authorization
    required Provide this header with `Bearer <user_token>` to gain authorized access to this API method.

##### Form data parameters

status_id
    required String. The status ID to be added to the filter group.

#### Response

##### 200: OK

FilterStatus created successfully within the current Filter


    {
      "id": "897",
      "status_id": "109416512469928632"
    }


##### 401: Unauthorized

Invalid or missing Authorization header.


    {
      "error": "The access token is invalid"
    }


##### 404: Not found

Filter is not owned by you or does not exist


    {
      "error": "Record not found"
    }


* * *

### View a single status filter


    GET /api/v2/filters/statuses/:id HTTP/1.1


Obtain a single status filter.

**Returns:** [FilterStatus](/entities/FilterStatus/)
**OAuth:** User token + `read:filters`
**Version history:**
4.0.0 - added

#### Request

##### Path parameters

:id
    required String. The ID of the FilterStatus in the database.

##### Headers

Authorization
    required Provide this header with `Bearer <user_token>` to gain authorized access to this API method.

#### Response

##### 200: OK


    {
      "id": "897",
      "status_id": "109416512469928632"
    }


##### 401: Unauthorized

Invalid or missing Authorization header.


    {
      "error": "The access token is invalid"
    }


##### 404: Not found

FilterStatus is not owned by you or does not exist


    {
      "error": "Record not found"
    }


* * *

### Remove a status from a filter group


    DELETE /api/v2/filters/statuses/:id HTTP/1.1


Remove a status filter from the current filter group.

**Returns:** [FilterStatus](/entities/FilterStatus/)
**OAuth:** User token + `write:filters`
**Version history:**
4.0.0 - added

#### Request

##### Path parameters

:id
    required String. The ID of the FilterStatus in the database.

##### Headers

Authorization
    required Provide this header with `Bearer <user_token>` to gain authorized access to this API method.

#### Response

##### 200: OK

FilterStatus deleted successfully


    {}


##### 401: Unauthorized

Invalid or missing Authorization header.


    {
      "error": "The access token is invalid"
    }


##### 404: Not found

FilterStatus is not owned by you or does not exist


    {
      "error": "Record not found"
    }


* * *

## Client-side (v1) methods

Prior to Mastodon 4.0, matching filters was done client-size and filters could only contain one phrase to filter against.

* * *

### View your filters deprecated


    GET /api/v1/filters HTTP/1.1


**Returns:** List of [V1::Filter](/entities/V1_Filter/)
**OAuth:** User token + `read:filters`
**Version history:**
2.4.3 - added
4.0.0 - deprecated. For compatibility purposes, now returns a List of V1::Filter, with each V1::Filter representing one FilterKeyword (with the `keyword` being presented in the `phrase` attribute)

#### Request

##### Headers

Authorization
    required Provide this header with `Bearer <user_token>` to gain authorized access to this API method.

#### Response

##### 200: OK

Excerpts of various filters in different contexts.


    [
      {
        "id": "6191",
        "phrase": ":eurovision2019:",
        "context": [
          "home"
        ],
        "whole_word": true,
        "expires_at": "2019-05-21T13:47:31.333Z",
        "irreversible": false
      },
      // ...
      {
        "id": "5580",
        "phrase": "@twitter.com",
        "context": [
          "home",
          "notifications",
          "public",
          "thread"
        ],
        "whole_word": false,
        "expires_at": null,
        "irreversible": true
      },
      // ...
    ]


##### 401: Unauthorized

Invalid or missing Authorization header.


    {
      "error": "The access token is invalid"
    }


* * *

### View a single filter deprecated


    GET /api/v1/filters/:id HTTP/1.1


**Returns:** [V1::Filter](/entities/V1_Filter/)
**OAuth:** User token + `read:filters`
**Version history:**
2.4.3 - added
4.0.0 - deprecated. For compatibility purposes, now returns a V1::Filter representing one FilterKeyword (with the `keyword` being presented in the `phrase` attribute)

#### Request

##### Path parameters

:id
    required String. The ID of the FilterKeyword in the database.

##### Headers

Authorization
    required Provide this header with `Bearer <user_token>` to gain authorized access to this API method.

#### Response

##### 200: OK


    {
      "id": "8449",
      "phrase": "test",
      "context": [
        "home",
        "notifications",
        "public",
        "thread"
      ],
      "whole_word": false,
      "expires_at": "2019-11-26T09:08:06.254Z",
      "irreversible": true
    }


##### 401: Unauthorized

Invalid or missing Authorization header.


    {
      "error": "The access token is invalid"
    }


##### 404: Not found

Filter ID does not exist, or is not owned by you


    {
      "error": "Record not found"
    }


* * *

### Create a filter deprecated


    POST /api/v1/filters HTTP/1.1


**Returns:** [V1::Filter](/entities/V1_Filter/)
**OAuth:** User token + `write:filters`
**Version history:**
2.4.3 - added
3.1.0 - added `account` context to filter in profile views
4.0.0 - deprecated. For compatibility purposes, now returns a V1::Filter representing one FilterKeyword (with the `keyword` being presented in the `phrase` attribute). This method will create a Filter that contains only one FilterKeyword. The `title` of the Filter and the `keyword` of the FilterKeyword will be set equal to the `phrase` provided.

#### Request

##### Headers

Authorization
    required Provide this header with `Bearer <user_token>` to gain authorized access to this API method.

##### Form data parameters

phrase
    required String. The text to be filtered.
context[]
    required Array of String. Where the filter should be applied. Specify at least one of `home`, `notifications`, `public`, `thread`, `account`.
irreversible
    Boolean. Should the server irreversibly drop matching entities from home and notifications? Defaults to false.
whole_word
    Boolean. Should the filter consider word boundaries for this keyword? Defaults to false.
expires_in
    Integer. Number of seconds from now that the filter should expire. Otherwise, `null` for a filter that doesn’t expire.

#### Response

##### 200: OK

The newly-created filter will be returned.


    {
      "id": "8449",
      "phrase": "test",
      "context": [
        "home",
        "notifications",
        "public",
        "thread"
      ],
      "whole_word": false,
      "expires_at": "2019-11-26T09:08:06.254Z",
      "irreversible": true
    }


##### 401: Unauthorized

Invalid or missing Authorization header.


    {
      "error": "The access token is invalid"
    }


##### 422: Unprocessable entity

If phrase is not provided properly:


    {
      "error": "Validation failed: Phrase can't be blank"
    }


If context is not provided properly:


    {
      "error": "Validation failed: Context can't be blank, Context None or invalid context supplied"
    }


* * *

### Update a filter deprecated


    PUT /api/v1/filters/:id HTTP/1.1


Replaces a filter’s parameters in-place.

**Returns:** [V1::Filter](/entities/V1_Filter/)
**OAuth:** User token + `write:filters`
**Version history:**
2.4.3 - added
3.1.0 - added `account` context to filter in profile views
4.0.0 - deprecated. For compatibility purposes, now returns a V1::Filter representing one FilterKeyword (with the `keyword` being presented in the `phrase` attribute). This method will return an error if you attempt to change `expires_in`, `irreversible`, or `context` for a filter with multiple keywords. Changing `phrase` and `whole_word` is always safe.

#### Request

##### Path parameters

:id
    required String. The ID of the FilterKeyword in the database.

##### Headers

Authorization
    required Provide this header with `Bearer <user_token>` to gain authorized access to this API method.

##### Form data parameters

phrase
    required String. The text to be filtered.
context[]
    required Array of String. Specify at least one of `home`, `notifications`, `public`, `thread`, `account`.
irreversible
    Boolean. Should the server irreversibly drop matching entities from home and notifications? Defaults to false.
whole_word
    Boolean. Should the filter consider word boundaries? Defaults to false.
expires_in
    Integer. Number of seconds from now that the filter should expire. Otherwise, `null` for a filter that doesn’t expire.

#### Response

##### 200: OK

Filter updated


    {
      "id": "8449",
      "phrase": "test",
      "context": [
        "home",
        "notifications",
        "public",
        "thread"
      ],
      "whole_word": false,
      "expires_at": null,
      "irreversible": true
    }


##### 401: Unauthorized

Invalid or missing Authorization header.


    {
      "error": "The access token is invalid"
    }


##### 404: Not found

Filter does not exist or is not owned by you


    {
      "error": "Record not found"
    }


##### 422: Unprocessable entity

If phrase is not provided properly:


    {
      "error": "Validation failed: Phrase can't be blank"
    }


If context is not provided properly:


    {
      "error": "Validation failed: Context can't be blank, Context None or invalid context supplied"
    }


* * *

### Remove a filter deprecated


    DELETE /api/v1/filters/:id HTTP/1.1


**Returns:** Empty
**OAuth:** User token + `write:filters`
**Version history:**
2.4.3 - added
4.0.0 - deprecated. This method will delete only the FilterKeyword from its parent Filter. To delete the parent Filter, you must use the v2 filters API.

#### Request

##### Path parameters

:id
    required String. The ID of the Filter in the database.

##### Headers

Authorization
    required Provide this header with `Bearer <user_token>` to gain authorized access to this API method.

#### Response

##### 200: OK

The filter has been deleted successfully, so an empty object will be returned.


    {}


##### 401: Unauthorized

Invalid or missing Authorization header.


    {
      "error": "The access token is invalid"
    }


##### 404: Not found

Filter does not exist or is not owned by you


    {
      "error": "Record not found"
    }


* * *

## See also

[Implementation guidelines for filters ](/api/guidelines/#filters)[app/controllers/api/v2/filters_controller.rb ](https://github.com/mastodon/mastodon/blob/main/app/controllers/api/v2/filters_controller.rb)[app/controllers/api/v1/filters/keywords_controller.rb ](https://github.com/mastodon/mastodon/blob/main/app/controllers/api/v1/filters/keywords_controller.rb)[app/controllers/api/v1/filters/statuses_controller.rb ](https://github.com/mastodon/mastodon/blob/main/app/controllers/api/v1/filters/statuses_controller.rb)[app/controllers/api/v1/filters_controller.rb](https://github.com/mastodon/mastodon/blob/main/app/controllers/api/v1/filters_controller.rb)

Last updated May 1, 2026 · [Improve this page](https://github.com/mastodon/documentation/tree/main/content/en/methods/filters.md)