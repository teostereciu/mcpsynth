# Request List page

*Source: https://developer.zendesk.com/api-reference/help_center/help-center-templates/request_list_page/*

---

## On this page

  * [Request List page](/api-reference/help_center/help-center-templates/request_list_page/#request-list-page)
  * [Available properties](/api-reference/help_center/help-center-templates/request_list_page/#available-properties)
  * [Available helpers](/api-reference/help_center/help-center-templates/request_list_page/#available-helpers)
  * [Available forms](/api-reference/help_center/help-center-templates/request_list_page/#available-forms)
  * [Sorters](/api-reference/help_center/help-center-templates/request_list_page/#sorters)
  * [Example](/api-reference/help_center/help-center-templates/request_list_page/#example)


# Request List page

## On this page

  * [Request List page](/api-reference/help_center/help-center-templates/request_list_page/#request-list-page)
  * [Available properties](/api-reference/help_center/help-center-templates/request_list_page/#available-properties)
  * [Available helpers](/api-reference/help_center/help-center-templates/request_list_page/#available-helpers)
  * [Available forms](/api-reference/help_center/help-center-templates/request_list_page/#available-forms)
  * [Sorters](/api-reference/help_center/help-center-templates/request_list_page/#sorters)
  * [Example](/api-reference/help_center/help-center-templates/request_list_page/#example)


## Request List page

The Request List page template is rendered when a user navigates to `https://{yoursubdomain}.zendesk.com/hc/{locale}/requests`.

### Available properties

You can use the following properties in the Request List page template.

Name| Type| Description
---|---|---
filters| array| An array of [filter](/api-reference/help_center/help-center-templates/objects#filter-object) objects for the page
current_filter| object| The current [filter](/api-reference/help_center/help-center-templates/objects#filter-object) object
sorters| array| An array of [filter](/api-reference/help_center/help-center-templates/objects#filter-object) objects for the page. See Sorters below
current_sorter| object| The current [filter](/api-reference/help_center/help-center-templates/objects#filter-object) object
query| string| The current search query
requests| array| An array of [request](/api-reference/help_center/help-center-templates/objects#request-object) objects
promoted_articles| array| An array of promoted [article](/api-reference/help_center/help-center-templates/objects#article-object) objects
ticket_forms| array| An array of [ticket form](/api-reference/help_center/help-center-templates/objects#ticket-form-object) objects
help_center| object| A [help_center](/api-reference/help_center/help-center-templates/objects#help_center-object) object that holds information and settings about the current help center
settings| object| A [settings](/api-reference/help_center/help-center-templates/objects#settings-object) object with custom settings for the current theme
signed_in| boolean| Whether the user is logged in or not
featured_posts| array| An array of featured [post](/api-reference/help_center/help-center-templates/objects#post-object) objects
brand| object| A [brand](/api-reference/help_center/help-center-templates/objects#brand-object) object representing the current brand
user| object| A [user](/api-reference/help_center/help-center-templates/objects#user-object) object representing the current user
path_steps| array| An array of [path_step](/api-reference/help_center/help-center-templates/objects#path_step-object) objects

### Available helpers

You can use the following helpers in this page template. You can also use any [built-in helpers](/api-reference/help_center/help-center-templates/helpers#built-in-helpers), [global helpers](/api-reference/help_center/help-center-templates/helpers#global-helpers), or [global advanced helpers](/api-reference/help_center/help-center-templates/advanced_helpers#global-advanced-helpers).

Name| Description
---|---
request_list| List of requests. See [request_list helper](/api-reference/help_center/help-center-templates/advanced_helpers#request_list-helper)
breadcrumbs| Breadcrumbs for the Request List page. See [breadcrumbs helper](/api-reference/help_center/help-center-templates/helpers#breadcrumbs-helper)
pagination| Pagination links. See [pagination helper](/api-reference/help_center/help-center-templates/helpers#pagination-helper)
form| A form for data input. See bellow the available forms for this page

### Available forms

You can add the following form to the Request List page template:

Name| Description
---|---
[requests_filter](/api-reference/help_center/help-center-templates/helpers/#form-helper)| A form to filter which requests are shown

Use the `form` helper to insert it. See [Form Helper](/api-reference/help_center/help-center-templates/helpers#form-helper).

#### Available identifiers

The following [identifiers](/api-reference/help_center/help-center-templates/helpers#identifiers) are available in this page:

Identifier| Form| Field(s)| Description
---|---|---|---
query| requests_filter| input| Identifies a search field
organization| requests_filter| label, select| Identifies a drop-down to select an organization
status| requests_filter| label, select| Identifies a drop-down to select a status

### Sorters

Iterating through the `sorters` array of [filter](/api-reference/help_center/help-center-templates/objects#filter-object) objects adds the following links to the page:

Link text| Action
---|---
Created| Sorts by most recent creation time
Last activity| Sorts by most recent activity in descending order

### Example


    <header class="my-activities-header">  {{breadcrumbs}}</header>
    <div class="requests-list">  <ul>    {{#each requests}}      <tr>        <td>{{id}}</td>        <td>          <a href="{{url}}">            {{#if subject}}              {{subject}}            {{else}}              {{excerpt description characters=50}}            {{/if}}          </a>        </td>        <td>          {{#is ../current_filter.identifier "my"}}            {{date created_at timeago=true}}          {{else}}            {{requester.name}}          {{/is}}        </td>        <td>{{date updated_at timeago=true}}</td>        <td>          <span class="request-status request-{{status}}" title="{{status_description}}">            {{status_name}}          </span>        </td>      </tr>    {{/each}}  </ul></div>

Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)