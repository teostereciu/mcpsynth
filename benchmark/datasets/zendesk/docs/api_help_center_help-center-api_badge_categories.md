# Badge Categories

*Source: https://developer.zendesk.com/api-reference/help_center/help-center-api/badge_categories/*

---

## On this page

  * [JSON format](/api-reference/help_center/help-center-api/badge_categories/#json-format)
  * [List Badge Categories](/api-reference/help_center/help-center-api/badge_categories/#list-badge-categories)
  * [Show Badge Category](/api-reference/help_center/help-center-api/badge_categories/#show-badge-category)
  * [Create Badge Category](/api-reference/help_center/help-center-api/badge_categories/#create-badge-category)
  * [Delete Badge Category](/api-reference/help_center/help-center-api/badge_categories/#delete-badge-category)


# Badge Categories

## On this page

  * [JSON format](/api-reference/help_center/help-center-api/badge_categories/#json-format)
  * [List Badge Categories](/api-reference/help_center/help-center-api/badge_categories/#list-badge-categories)
  * [Show Badge Category](/api-reference/help_center/help-center-api/badge_categories/#show-badge-category)
  * [Create Badge Category](/api-reference/help_center/help-center-api/badge_categories/#create-badge-category)
  * [Delete Badge Category](/api-reference/help_center/help-center-api/badge_categories/#delete-badge-category)


A badge category provides a way to group together related [badges](/api-reference/help_center/help-center-api/badges/).

Badges are available on the Gather Professional plan.

### JSON format

Badge categories are JSON objects with the following properties:

Name| Type| Read-only| Mandatory| Comment
---|---|---|---|---
id| string| yes| no| Automatically assigned when the badge category is created
brand_id| string| no| yes| The brand that the badge category pertains to. Can only be set when the badge category is created
name| string| no| yes| The name of the badge category. Shown to users who award or remove badges
slug| string| no| yes| A unique (within the brand) textual code of the badge category. Used in the [Templating language](/api-reference/help_center/help-center-templates/introduction/) as a keyword for filtering
created_at| timestamp| yes| no| When the badge category was created
updated_at| timestamp| yes| no| When the badge category was last updated

#### Example


    {  "id": "01E89E1AD4BG6JA2XSZZN5BZVC",  "brand_id": "7056041",  "name": "Achievements",  "slug": "achievements",  "created_at": "2020-05-13T11:46:16.000Z",  "updated_at": "2020-05-13T11:46:16.000Z"}

### List Badge Categories

  * `GET /api/v2/gather/badge_categories`


Lists all badge categories.

This request can be further filtered using the `brand_id` query string parameter to only show badge categories within a particular brand.

#### Allowed for

  * Help Center managers


#### Parameters

Name| Type| In| Required| Description
---|---|---|---|---
brand_id| integer| Query| false| Returns badge categories for the specified brand

#### Using curl


    curl https://{subdomain}.zendesk.com/api/v2/gather/badge_categories \  -v -u {email_address}:{password}

#### Example Response


    Status: 200 OK
    {    "badge_categories": [        {            "id": "01E86XPM9459S78F83VH8CD69H",            "brand_id": "7056041",            "name": "Titles",            "slug": "titles",            "created_at": "2020-05-13T11:46:16.000Z",            "updated_at": "2020-05-13T11:46:16.000Z"        },        {            "id": "01E89E1AD4BG6JA2XSZZN5BZVC",            "brand_id": "7056041",            "name": "Achievements",            "slug": "achievements",            "created_at": "2020-05-14T11:10:13.000Z",            "updated_at": "2020-05-14T11:10:13.000Z"        }    ]}

### Show Badge Category

  * `GET /api/v2/gather/badge_categories/{id}`


Shows information about a single badge category.

#### Allowed for

  * Help Center managers


#### Using curl


    curl https://{subdomain}.zendesk.com/api/v2/gather/badge_categories/{id} \  -v -u {email_address}:{password}

#### Example Response


    Status: 200 OK
    {    "badge_category": {        "id": "01E89E1AD4BG6JA2XSZZN5BZVC",        "brand_id": "7056041",        "name": "Achievements",        "slug": "achievements",        "created_at": "2020-05-13T11:46:16.000Z",        "updated_at": "2020-05-13T11:46:16.000Z"    }}

### Create Badge Category

  * `POST /api/v2/gather/badge_categories`


#### Allowed for

  * Help Center managers


#### Using curl


    curl https://{subdomain}.zendesk.com/api/v2/gather/badge_category \  -v -u {email_address}:{password} -d '{"badge_category": {"brand_id": "{{brand_id}}", "name": "Certifications", "slug": "certs" }}' \  -X POST -H "Content-Type: application/json"

### Delete Badge Category

  * `DELETE /api/v2/gather/badge_categories/{id}`


Badge categories can only be deleted if they do not contain any badges.

#### Allowed for

  * Help Center managers


#### Using curl


    curl https://{subdomain}.zendesk.com/api/v2/gather/badge_categories/{id} \  -v -u {email_address}:{password} -X DELETE

#### Example Response


    Status: 204 No Content

Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)