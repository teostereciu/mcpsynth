# Management Permission Groups

*Source: https://developer.zendesk.com/api-reference/help_center/help-center-api/permission_groups/*

---

## On this page

  * [JSON format](/api-reference/help_center/help-center-api/permission_groups/#json-format)
  * [Example](/api-reference/help_center/help-center-api/permission_groups/#example)
  * [List Permission Groups](/api-reference/help_center/help-center-api/permission_groups/#list-permission-groups)
  * [Show Permission Group](/api-reference/help_center/help-center-api/permission_groups/#show-permission-group)
  * [Create Permission Group](/api-reference/help_center/help-center-api/permission_groups/#create-permission-group)
  * [Update Permission Group](/api-reference/help_center/help-center-api/permission_groups/#update-permission-group)
  * [Delete Permission Group](/api-reference/help_center/help-center-api/permission_groups/#delete-permission-group)


# Management Permission Groups

## On this page

  * [JSON format](/api-reference/help_center/help-center-api/permission_groups/#json-format)
  * [Example](/api-reference/help_center/help-center-api/permission_groups/#example)
  * [List Permission Groups](/api-reference/help_center/help-center-api/permission_groups/#list-permission-groups)
  * [Show Permission Group](/api-reference/help_center/help-center-api/permission_groups/#show-permission-group)
  * [Create Permission Group](/api-reference/help_center/help-center-api/permission_groups/#create-permission-group)
  * [Update Permission Group](/api-reference/help_center/help-center-api/permission_groups/#update-permission-group)
  * [Delete Permission Group](/api-reference/help_center/help-center-api/permission_groups/#delete-permission-group)


A management permission group defines which agents can create, update, archive, and publish articles. It consists of a set of privileges, each of which is mapped to a [user segment](/api-reference/help_center/help-center-api/user_segments/). Agents receive whichever privileges are associated with the user segments they belong to.

The types of privileges a permission group can define depends on your Guide plan:

  * Guide Enterprise supports the `edit` and `publish` privileges
  * Guide Professional supports the `publish` privilege
  * Guide Lite does not allow creating or updating permission groups. However the `publish` privilege is still honored on any permission groups that exist when switching to Lite


Permission groups are defined at the account level, not the brand level. If you use a brand as the subdomain of a request, the API redirects the request to the account's primary subdomain.

You can use this API to define or change a permission group. However, you must use the [Articles](/api-reference/help_center/help-center-api/articles/) API to apply management permission groups to articles. You can change the definition of user segments using the [User Segments](/api-reference/help_center/help-center-api/user_segments/) API.

### JSON format

Management permission groups have the following attributes:

Name| Type| Read-only| Mandatory| Comment
---|---|---|---|---
id| integer| yes| no| Automatically assigned when the permission group is created
name| string| no| no| Permission group name
edit| array| no| no| The ids of user segments that have edit privileges
publish| array| no| no| The ids of user segments that have publish privileges
created_at| timestamp| yes| no| When the permission group was created
updated_at| timestamp| yes| no| When the permission group was last updated
built_in| boolean| yes| no| Whether the permission group is built-in. Built-in permission groups cannot be modified

### Example


    {  "permission_group": {    "id":         42,    "name":       "Printer Experts",    "built_in":   false,    "publish":    [123456],    "edit":       [],    "created_at": "2018-08-23 12:42:18 +0000",    "updated_at": "2018-08-23 12:42:18 +0000"  }}

### List Permission Groups

`GET /api/v2/guide/permission_groups.json`

#### Allowed for

  * Help Center managers


#### Using curl


    curl https://{subdomain}.zendesk.com/api/v2/guide/permission_groups.json \  -v -u {email_address}:{password}

#### Example Response


    Status: 200 OK
    {  "permission_groups": [    {      "id":         42,      "name":       "Printer Experts",      "built_in":   false,      "publish":    [123456],      "edit":       [],      "created_at": "2018-08-23 12:42:18 +0000",      "updated_at": "2018-08-23 12:42:18 +0000"    },    {      "id": 	    75,      "name":       "Managers",      "built_in":   true,      "publish":    [],      "edit":       [],      "created_at": "2018-03-16 08:29:27 +0000",      "updated_at": "2018-03-16 08:29:27 +0000"    },    ...  ]}

### Show Permission Group

`GET /api/v2/guide/permission_groups/{id}.json`

#### Allowed for

  * Help Center managers


#### Using curl


    curl https://{subdomain}.zendesk.com/api/v2/guide/permission_groups/{id}.json \  -v -u {email_address}:{password}

#### Example Response


    Status: 200 OK
    {  "permission_group": {    "id":         42,    "name":       "Printer Experts",    "built_in":   false,    "publish":    [12],    "edit":       [34],    "created_at": "2018-08-23 12:42:18 +0000",    "updated_at": "2018-08-23 12:42:18 +0000"  }}

### Create Permission Group

`POST /api/v2/guide/permission_groups.json`

#### Allowed for

  * Help Center managers


#### Using curl


    curl https://{subdomain}.zendesk.com/api/v2/guide/permission_groups.json \  -d '{ \    "permission_group": { \      "name": "Printer Experts", \      "edit": [12, ...], \      "publish": [34, ...] \    } \  }' \  -v -u {email_address}:{password} -X POST -H "Content-Type: application/json"

#### Example Response


    Status: 201 Created
    {  "permission_group": {    "id":         42,    "name":       "Printer Experts",    "built_in":   false,    "publish":    [34, ...],    "edit":       [12, ...],    "created_at": "2018-08-23 12:42:18 +0000",    "updated_at": "2018-08-23 12:42:18 +0000"  }}

### Update Permission Group

`PUT /api/v2/guide/permission_groups/{id}.json`

#### Allowed for

  * Help Center managers


#### Using curl


    curl https://{subdomain}.zendesk.com/api/v2/guide/permission_groups/{id}.json \  -d '{ \    "user_segment": { \      "name": "Super Printer Experts", \      "edit": [], \      "publish": [42, ...], \    } \  }' \  -v -u {email_address}:{password} -X PUT -H "Content-Type: application/json"

#### Example Response


    Status: 200 OK
    {  "permission_group": {    "id":         42,    "name":       "Super Printer Experts",    "built_in":   false,    "publish":    [42, ...],    "edit":       [],    "created_at": "2018-08-23 12:42:18 +0000",    "updated_at": "2018-08-24 00:42:15 +0000"  }}

### Delete Permission Group

`DELETE /api/v2/guide/permission_groups/{id}.json`

#### Allowed for

  * Help Center managers


#### Using curl


    curl https://{subdomain}.zendesk.com/api/v2/guide/permission_groups/{id}.json \  -v -u {email_address}:{password} -X DELETE

#### Example Response


    Status: 204 No Content

Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)