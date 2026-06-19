# Article page

*Source: https://developer.zendesk.com/api-reference/help_center/help-center-templates/article_page/*

---

## On this page

  * [Article page](/api-reference/help_center/help-center-templates/article_page/#article-page)
  * [Available properties](/api-reference/help_center/help-center-templates/article_page/#available-properties)
  * [Available helpers](/api-reference/help_center/help-center-templates/article_page/#available-helpers)
  * [Available forms](/api-reference/help_center/help-center-templates/article_page/#available-forms)
  * [Sorters](/api-reference/help_center/help-center-templates/article_page/#sorters)
  * [Example](/api-reference/help_center/help-center-templates/article_page/#example)


# Article page

## On this page

  * [Article page](/api-reference/help_center/help-center-templates/article_page/#article-page)
  * [Available properties](/api-reference/help_center/help-center-templates/article_page/#available-properties)
  * [Available helpers](/api-reference/help_center/help-center-templates/article_page/#available-helpers)
  * [Available forms](/api-reference/help_center/help-center-templates/article_page/#available-forms)
  * [Sorters](/api-reference/help_center/help-center-templates/article_page/#sorters)
  * [Example](/api-reference/help_center/help-center-templates/article_page/#example)


## Article page

The Article page template is rendered when a user navigates to `https://{yoursubdomain}.zendesk.com/hc/{locale}/articles/{article_id}`.

### Available properties

You can use the following properties in the Article page template.

Name| Type| Description
---|---|---
article| object| An [article](/api-reference/help_center/help-center-templates/objects#article-object) object
attachments| array| An array of [attachment](/api-reference/help_center/help-center-templates/objects#attachment-object) objects
comments| array| An array of article [comment](/api-reference/help_center/help-center-templates/objects#article-comment-object) objects
comment_sorters| array| An array of [filter](/api-reference/help_center/help-center-templates/objects#filter-object) objects. Useful for sorting the comments. See Sorters below
promoted_articles| array| An array of promoted [article](/api-reference/help_center/help-center-templates/objects#article-object) objects
section| object| A [section](/api-reference/help_center/help-center-templates/objects#section-object) object. The object's `articles` property contains only the first 10 articles for performance reasons
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
breadcrumbs| Breadcrumbs for the article page. See [breadcrumbs helper](/api-reference/help_center/help-center-templates/helpers#breadcrumbs-helper)
pagination| Pagination links. See [pagination helper](/api-reference/help_center/help-center-templates/helpers#pagination-helper)
share| Sharing elements. See [share helper](/api-reference/help_center/help-center-templates/helpers#share-helper)
subscribe| A link to follow or unfollow new comments in the article
form| A form for data input. See bellow the available forms for this page
related_articles| A list of related articles. See [related articles helper](/api-reference/help_center/help-center-templates/advanced_helpers#related_articles-helper)
request_callout| A link to submit a new request, if available. See [request_callout helper](/api-reference/help_center/help-center-templates/advanced_helpers#request_callout-helper)
comment_callout| A link to submit a new comment, if available. See [comment_callout helper](/api-reference/help_center/help-center-templates/advanced_helpers#comment_callout-helper)

### Available forms

You can add the following form to the Article page template:

Name| Description
---|---
comment| A form to create a new article comment

Use the `form` helper to insert it. See [Form Helper](/api-reference/help_center/help-center-templates/helpers#form-helper).

#### Available identifiers

The following [identifiers](/api-reference/help_center/help-center-templates/helpers#identifiers) are available in this page:

Identifier| Form| Field(s)| Description
---|---|---|---
body| comment| textarea, wysiwyg| Identifies a text field for article comments

### Sorters

Iterating through the `comment_sorters` array of [filter](/api-reference/help_center/help-center-templates/objects#filter-object) objects adds the following links to the page:

Link text| Action
---|---
Date| Sorts by most recent comment creation time in descending order
Votes| Sorts by highest vote sum in descending order

Official comments are always given the highest priority and shown at the top.

### Example


    <nav class="sub-nav clearfix">  {{breadcrumbs}}  {{subscribe}}</nav>
    <article class="main-column">
      <header class="article-header clearfix">    <h1>{{article.title}}</h1>    <div class="article-metadata">      <div class="article-avatar">        <img src="{{article.author.avatar_url}}" alt="Avatar">      </div>      <div class="article-author">{{article.author.name}}</div>      <div class="article-updated">{{article.updated_at}}</div>    </div>  </header>
      <div class="article-body markdown">    {{article.body}}  </div>
      <footer class="article-footer clearfix">    {{article.vote 'up' class='article-vote-up' selected_class='article-voted' role='button'}}    {{article.vote 'down' class='article-vote-down' selected_class='article-voted' role='button'}}    {{share}}  </footer>
      <section class="article-comments">    <div class="article-comments-header">      <h2>Comments</h2>      <div class="comment-sorters">        {{#each comment_sorters}}          <a aria-selected="{{selected}}" href="{{url}}">{{name}}</a>        {{/each}}      </div>    </div>    <ul>    {{#each comments}}      <li class="comment">        <div class="comment-vote vote">          {{vote 'up' class='vote-up' selected_class='vote-voted'}}          {{vote 'sum' class='vote-sum'}}          {{vote 'down' class='vote-down' selected_class='vote-voted'}}        </div>        <div class="comment-container">          On {{date created_at}}, {{author.name}} wrote: {{body}}        </div>      </li>    {{/each}}    </ul>
        {{#form 'comment' class='comment-form'}}      <div class="comment-avatar">{{user_avatar class='user-avatar'}}</div>      <div class="comment-container">        {{wysiwyg 'body' rows='4'}}        <div class="comment-form-controls">{{input type='submit'}}</div>      </div>    {{/form}}  </section>
    </article>

Join our developer community

[Forum](https://support.zendesk.com/hc/en-us/community/topics)[Blog](https://medium.com/zendesk-developer-blog)[Slack](https://docs.google.com/forms/d/e/1FAIpQLScm_rDLWwzWnq6PpYWFOR_PwMaSBcaFft-1pYornQtBGAaiJA/viewform)

Zendesk181 Fremont Street, 17th Floor, San Francisco, California 94105

[Privacy Notice](https://www.zendesk.com/company/agreements-and-terms/privacy-notice/)[Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/)[System Status](https://status.zendesk.com)