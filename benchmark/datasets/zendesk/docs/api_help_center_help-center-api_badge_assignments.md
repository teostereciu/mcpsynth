# Badge Assignments

*Source: https://developer.zendesk.com/api-reference/help_center/help-center-api/badge_assignments/*

---

## On this page

  * [JSON format](/api-reference/help_center/help-center-api/badge_assignments/#json-format)
  * [List Badge Assignments](/api-reference/help_center/help-center-api/badge_assignments/#list-badge-assignments)
  * [Create Badge Assignment](/api-reference/help_center/help-center-api/badge_assignments/#create-badge-assignment)
  * [Delete Badge Assignment](/api-reference/help_center/help-center-api/badge_assignments/#delete-badge-assignment)


# Badge Assignments

## On this page

  * [JSON format](/api-reference/help_center/help-center-api/badge_assignments/#json-format)
  * [List Badge Assignments](/api-reference/help_center/help-center-api/badge_assignments/#list-badge-assignments)
  * [Create Badge Assignment](/api-reference/help_center/help-center-api/badge_assignments/#create-badge-assignment)
  * [Delete Badge Assignment](/api-reference/help_center/help-center-api/badge_assignments/#delete-badge-assignment)


Assigning a badge adds a [badge](/api-reference/help_center/help-center-api/badges/) to a particular user's profile in the help center.

Badges are available on the Gather Professional plan.

### JSON format

Badges assignments are JSON objects with the following properties:

Name| Type| Read-only| Mandatory| Comment
---|---|---|---|---
id| string| yes| no| Automatically assigned when the badge assignment is created
badge_id| string| no| yes| The id of the badge
user_id| string| no| yes| The id of the user
created_at| timestamp| yes| no| When the badge assignment was created

#### Example


    {  "id": "01E86XPXH5BK09KRWTDVEKVVY8",  "badge_id": "01E86XPPRDCNHYTSVWSRMD76R0",  "user_id": "57919551",  "created_at": "2020-05-13T11:46:26.000Z"}

### List Badge Assignments

  * ` GET /api/v2/gather/badge_assignments`


You can filter the results with any combination of the following query parameters:

  * `user_id`
  * `badge_id`
  * `badge_category_id`
  * `brand_id`


Examples:

  * `GET /api/v2/gather/badge_assignments?user_id={user_id}`
  * `GET /api/v2/gather/badge_assignments?user_id={user_id}&brand_id={brand_id}`
  * `GET /api/v2/gather/badge_assignments?badge_id={badge_id}`
  * `GET /api/v2/gather/badge_assignments?badge_category_id={badge_category_id}`


#### Allowed for

  * Help Center managers


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
user_id| integer| Query| false| Returns assignments for the specified user
badge_id| integer| Query| false| Returns assignments for the specified badge
badge_category_id| integer| Query| false| Returns assignments for badges under the specified category
brand_id| integer| Query| false| Returns assignments for the specified brand

#### Using curl


    curl 'https://{subdomain}.zendesk.com/api/v2/gather/badge_assignments?badge_id=01E89DZ2NA6ZPMBMRPFRXC2BRY' \  -v -u {email_address}:{password}

#### Example Response


    Status: 200 OK
    {    "badge_assignments": [        {            "id": "01E86XPXH5BK09KRWTDVEKVVY8",            "badge_id": "01E89DZ2NA6ZPMBMRPFRXC2BRY",            "user_id": "57919551",            "created_at": "2020-05-13T11:46:26.000Z"        }    ]}

### Create Badge Assignment

  * `POST /api/v2/gather/badge_assignments`


#### Allowed for

  * Help Center managers


#### Using curl


    curl https://{subdomain}.zendesk.com/api/v2/gather/badges \  -v -u {email_address}:{password} -d '{"badge_assignment": {"badge_id": "{{badge_id}}", "user_id": "{{user_id}}"}}' \  -X POST -H "Content-Type: application/json"

### Delete Badge Assignment

  * `DELETE /api/v2/gather/badge_assignments/{id}`


#### Allowed for

  * Help Center managers


#### Using curl


    curl https://{subdomain}.zendesk.com/api/v2/gather/badge_assignments/{id} \  -v -u {email_address}:{password} -X DELETE

#### Example Response


    Status: 204 No Content

Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)