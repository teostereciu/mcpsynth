# REST API endpoints for Markdown

*Source: https://docs.github.com/en/rest/markdown/markdown*

---

# REST API endpoints for Markdown
Use the REST API to render a markdown document as an HTML page_number or as raw text.

## Render a Markdown document
Depending on what is rendered in the Markdown, you may need to provide additional token scopes for label_filters, such asissues:readorpull_requests:read.

### Fine-grained access tokens for "Render a Markdown document"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Contents" repository permissions (read)
This endpoint can be used without authentication or the aforementioned permissions if only public resources are requested.

### Parameters for "Render a Markdown document"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
textstringRequiredThe Markdown text to render in HTML.
modestringThe rendering mode.Default:markdownCan be one of:markdown,gfm
contextstringThe repository context to use when creating references ingfmmode.  For example, settingcontexttoocto-org/octo-repowill change the text#42into an HTML link to issue 42 in theocto-org/octo-reporepository.
[/TABLE]
The Markdown text to render in HTML.
The rendering mode.
Default:markdown
Can be one of:markdown,gfm
The repository context to use when creating references ingfmmode.  For example, settingcontexttoocto-org/octo-repowill change the text#42into an HTML link to issue 42 in theocto-org/octo-reporepository.

### HTTP response status codes for "Render a Markdown document"

[TABLE]
Status code | Description
200 | OK
304 | Not modified
[/TABLE]
OK
Not modified

### Code samples for "Render a Markdown document"

#### Request example
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -X POST \
  -H "Accept: text/html" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/markdown \
  -d '{"text":"Hello **world**"}'
```

#### Example response
- Example response
- Response schema

```
Status: 200
```

```
"<p>Hello <strong>world</strong></p>"
```

## Render a Markdown document in raw mode
You must send Markdown as plain text (using aContent-Typeheader oftext/plainortext/x-markdown) to this endpoint, rather than using JSON format. In raw mode,GitHub Flavored Markdownis not supported and Markdown will be rendered in plain format like a README.md file. Markdown content must be 400 KB or less.

### Fine-grained access tokens for "Render a Markdown document in raw mode"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token does not require any permissions.
This endpoint can be used without authentication if only public resources are requested.

### HTTP response status codes for "Render a Markdown document in raw mode"

[TABLE]
Status code | Description
200 | OK
304 | Not modified
[/TABLE]
OK
Not modified

### Code samples for "Render a Markdown document in raw mode"

#### Request examples
- cURL
- JavaScript
- GitHub CLI

```
curl -L \
  -X POST \
  -H "Accept: text/html" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  https://api.github.com/markdown/raw \
  -d '{"text":"Hello **world**"}'
```

#### Example response
- Example response
- Response schema

```
Status: 200
```

```
"<p>Hello <strong>world</strong></p>"
```