# Community Topic page

*Source: https://developer.zendesk.com/api-reference/help_center/help-center-templates/community_topic_page/*

---

## On this page

  * [Community Topic page](/api-reference/help_center/help-center-templates/community_topic_page/#community-topic-page)
  * [Available properties](/api-reference/help_center/help-center-templates/community_topic_page/#available-properties)
  * [Available helpers](/api-reference/help_center/help-center-templates/community_topic_page/#available-helpers)
  * [Sorters](/api-reference/help_center/help-center-templates/community_topic_page/#sorters)
  * [Example](/api-reference/help_center/help-center-templates/community_topic_page/#example)


# Community Topic page

## On this page

  * [Community Topic page](/api-reference/help_center/help-center-templates/community_topic_page/#community-topic-page)
  * [Available properties](/api-reference/help_center/help-center-templates/community_topic_page/#available-properties)
  * [Available helpers](/api-reference/help_center/help-center-templates/community_topic_page/#available-helpers)
  * [Sorters](/api-reference/help_center/help-center-templates/community_topic_page/#sorters)
  * [Example](/api-reference/help_center/help-center-templates/community_topic_page/#example)


## Community Topic page

The Community Topic page template is rendered when a user navigates to `https://{yoursubdomain}.zendesk.com/hc/{locale}/community/topics/{topic_id}`.

### Available properties

Name| Type| Description
---|---|---
topic| object| A [topic](/api-reference/help_center/help-center-templates/objects#topic-object) object
posts| array| An array of [post](/api-reference/help_center/help-center-templates/objects#post-object) objects
filters| array| An array of [filter](/api-reference/help_center/help-center-templates/objects#filter-object) objects. Useful for filtering the posts in the topic
current_filter| object| The current [filter](/api-reference/help_center/help-center-templates/objects#filter-object) object
sorters| array| An array of [filter](/api-reference/help_center/help-center-templates/objects#filter-object) objects. Useful for sorting the posts in the topic. See Sorters below
current_sorter| object| The current [filter](/api-reference/help_center/help-center-templates/objects#filter-object) object
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
breadcrumbs| Breadcrumbs for the Topic page. See [breadcrumbs helper](/api-reference/help_center/help-center-templates/helpers#breadcrumbs-helper)
pagination| Pagination links. See [pagination helper](/api-reference/help_center/help-center-templates/helpers#pagination-helper)
subscribe| A link to follow or unfollow new posts and comments in the topic. See [subscribe](/api-reference/help_center/help-center-templates/helpers#subscribe-helper)

### Sorters

Iterating through the `sorters` array of [filter](/api-reference/help_center/help-center-templates/objects#filter-object) objects adds the following links to the page:

Link text| Action
---|---
Newest post| Sorts by post creation time in descending order
Recent activity| Sorts by the most recent activity in descending order. Post activity are actions such as post created, comment created etc.
Votes| Sorts by highest vote sum in descending order
Comments| Sorts by largest number of comments in descending order

### Example


    <nav class="sub-nav">  {{breadcrumbs}}  {{search scoped=true}}</nav>
    <header class="page-header">  <h1>    {{#if topic.internal}}      <span class="visibility-internal" data-title="{{t 'internal'}}">        <span class="visibility-internal-icon"></span>      </span>    {{/if}}    {{topic.name}}  </h1>  <span class="post-to-community">    {{link 'new_post' role='button' topic_id=topic.id}}  </span></header>
    <p>{{topic.description}}</p>
    <div class="topic-header">  <span class="topic-filters">    <span class="dropdown">      <span class="dropdown-toggle">        {{current_filter.label}}      </span>      <span class="dropdown-menu" role="menu">        {{#each filters}}          <a href="{{url}}" aria-selected="{{selected}}" role="menuitem">            {{name}}          </a>        {{/each}}      </span>    </span>    <span class="dropdown">      <span class="dropdown-toggle">        {{current_sorter.label}}      </span>      <span class="dropdown-menu" role="menu">        {{#each sorters}}          <a href="{{url}}" aria-selected="{{selected}}" role="menuitem">            {{name}}          </a>        {{/each}}      </span>    </span>
      </span>  <span class="topic-follow">    {{subscribe}}  </span></div>
    {{#each posts}}  <div class="post-overview {{#if featured}}post-featured{{/if}} {{#if pinned}}post-pinned{{/if}} clearfix">    <span class="post-overview-info">      <a href="{{url}}" title="{{title}}">{{title}}</a>      <span class="meta-group">        <span>{{author.name}}</span>        <span>{{date created_at timeago=true}}</span>      </span>    </span>    <span class="post-overview-count">      <strong>{{comment_count}}</strong>      {{t 'comment' count=comment_count}}    </span>    <span class="post-overview-count">      <strong>{{vote_sum}}</strong>      {{t 'vote' count=vote_sum}}    </span>    <span class="post-overview-status">      {{#if status}}        <span class="post-{{status.id}}">{{status.name}}</span>      {{/if}}    </span>  </div>{{/each}}
    {{pagination}}

Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)