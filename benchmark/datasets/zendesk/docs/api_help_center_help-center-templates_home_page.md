# Home page

*Source: https://developer.zendesk.com/api-reference/help_center/help-center-templates/home_page/*

---

## On this page

  * [Home page](/api-reference/help_center/help-center-templates/home_page/#home-page)
  * [Available properties](/api-reference/help_center/help-center-templates/home_page/#available-properties)
  * [Available helpers](/api-reference/help_center/help-center-templates/home_page/#available-helpers)
  * [Example](/api-reference/help_center/help-center-templates/home_page/#example)


# Home page

## On this page

  * [Home page](/api-reference/help_center/help-center-templates/home_page/#home-page)
  * [Available properties](/api-reference/help_center/help-center-templates/home_page/#available-properties)
  * [Available helpers](/api-reference/help_center/help-center-templates/home_page/#available-helpers)
  * [Example](/api-reference/help_center/help-center-templates/home_page/#example)


## Home page

The Home page template is rendered when a user navigates to `https://{yoursubdomain}.zendesk.com/hc/{locale}/`.

### Available properties

You can use the following properties in the Home page template.

Name| Type| Description
---|---|---
categories| array| An array [category](/api-reference/help_center/help-center-templates/objects#category-object) objects
has_multiple_categories| boolean| Whether there is more than one category visible for the current user
promoted_articles| array| An array of promoted [article](/api-reference/help_center/help-center-templates/objects#article-object) objects
ticket_forms| array| An array of [ticket form](/api-reference/help_center/help-center-templates/objects#ticket-form-object) objects
help_center| object| A [help_center](/api-reference/help_center/help-center-templates/objects#help_center-object) object that holds information and settings about the current help center
settings| object| A [settings](/api-reference/help_center/help-center-templates/objects#settings-object) object with custom settings for the current theme
signed_in| boolean| Whether the user is logged in or not
featured_posts| array| An array of featured [post](/api-reference/help_center/help-center-templates/objects#post-object) objects
brand| object| A [brand](/api-reference/help_center/help-center-templates/objects#brand-object) object representing the current brand
user| object| A [user](/api-reference/help_center/help-center-templates/objects#user-object) object representing the current user

### Available helpers

You can use the following helpers in this page template. You can also use any [built-in helpers](/api-reference/help_center/help-center-templates/helpers#built-in-helpers), [global helpers](/api-reference/help_center/help-center-templates/helpers#global-helpers), or [global advanced helpers](/api-reference/help_center/help-center-templates/advanced_helpers#global-advanced-helpers).

Name| Description
---|---
pagination| Pagination links. See [pagination helper](/api-reference/help_center/help-center-templates/helpers#pagination-helper)

### Example


    <section class="hero-unit">  {{search}}</section>
    <div class="knowledge-base"><ul>{{#each categories}}  <li class="category-name">    <a href="{{url}}">{{name}}</a>    <ul>    {{#each sections}}      <li class="section-name">        <a href="{{url}}">{{name}}</a>      </li>    {{/each}}    </ul>  </li>{{/each}}
    {{pagination}}</ul></div>

Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)