# Service catalog page templates

*Source: https://developer.zendesk.com/api-reference/help_center/help-center-templates/service_catalog/*

---

## On this page

  * [Service catalog page templates](/api-reference/help_center/help-center-templates/service_catalog/#service-catalog-page-templates)
  * [Service catalog items](/api-reference/help_center/help-center-templates/service_catalog/#service-catalog-items)
  * [Available properties](/api-reference/help_center/help-center-templates/service_catalog/#available-properties)
  * [Available helpers](/api-reference/help_center/help-center-templates/service_catalog/#available-helpers)
  * [Example](/api-reference/help_center/help-center-templates/service_catalog/#example)


# Service catalog page templates

## On this page

  * [Service catalog page templates](/api-reference/help_center/help-center-templates/service_catalog/#service-catalog-page-templates)
  * [Service catalog items](/api-reference/help_center/help-center-templates/service_catalog/#service-catalog-items)
  * [Available properties](/api-reference/help_center/help-center-templates/service_catalog/#available-properties)
  * [Available helpers](/api-reference/help_center/help-center-templates/service_catalog/#available-helpers)
  * [Example](/api-reference/help_center/help-center-templates/service_catalog/#example)


## Service catalog page templates

Service catalog page templates are optional. They become available after enabling service catalog in your account.

The service catalog has two page templates:

  * the service list page
  * the service page


Both expose exactly the same methods.

The service list page is rendered when a user navigates to `https://{yoursubdomain}.zendesk.com/hc/{locale}/services/`.

The service page is rendered when a user navigates to `https://{yoursubdomain}.zendesk.com/hc/{locale}/services/{service_id}`.

Service catalog pages are only rendered in help centers that have service catalog enabled. You may have multiple help centers and multiple brands, but only one with service catalog enabled.

### Service catalog items

To display a list of available services, you can call the service catalog [list API](https://developer.zendesk.com/api-reference/help_center/employee-services/service_catalog_items/#list-service-catalog-items) or the service catalog [search API](https://developer.zendesk.com/api-reference/help_center/employee-services/service_catalog_items/#search-service-catalog-items) using JavaScript in your theme code.

Each service catalog item has a form_id, which relates the item to a ticket form.
Viewing a [ticket form](https://developer.zendesk.com/api-reference/ticketing/tickets/ticket_forms/#show-ticket-form) displays a list of associated [ticket field ids](https://developer.zendesk.com/api-reference/ticketing/tickets/ticket_fields/#list-ticket-fields). Ticket fields can be used when creating or updating a service catalog item, to be displayed in the item's request form.

Submitting a service catalog item request will create a [ticket request](https://developer.zendesk.com/api-reference/ticketing/tickets/ticket-requests/.#create-request).

### Available properties

The following properties can be used in both the service list page template and the service page template.

Name| Type| Description
---|---|---
brand| object| A [brand](/api-reference/help_center/help-center-templates/objects#brand-object) object representing the current brand
help_center| object| A [help_center](/api-reference/help_center/help-center-templates/objects#help_center-object) object that holds information and settings about the current help center
settings| object| A [settings](/api-reference/help_center/help-center-templates/objects#settings-object) object with custom settings for the current theme
signed_in| boolean| Whether the user is logged in or not
user| object| A [user](/api-reference/help_center/help-center-templates/objects#user-object) object representing the current user

### Available helpers

You can use the following helpers for the service list and service page templates. You can also use any [built-in helpers](/api-reference/help_center/help-center-templates/helpers#built-in-helpers), [global helpers](/api-reference/help_center/help-center-templates/helpers#global-helpers), or [global advanced helpers](/api-reference/help_center/help-center-templates/advanced_helpers#global-advanced-helpers).

Name| Description
---|---
breadcrumbs| Breadcrumbs for the current page. See [breadcrumbs helper](/api-reference/help_center/help-center-templates/helpers#breadcrumbs-helper)

### Example


    <div class="container">  <div class="sub-nav">{{breadcrumbs}}</div>
      <div id="main-content">    <div id="service-catalog-item"></div>  </div></div>

Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)