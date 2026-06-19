# REST API endpoints for draft Project items

*Source: https://docs.github.com/en/rest/projects/drafts*

---

# REST API endpoints for draft Project items
Use the REST API to manage draft items in Projects.

## Create draft item for organization owned project
Create draft issue item for the specified organization owned project.

### Fine-grained access tokens for "Create draft item for organization owned project"
This endpoint works with the following fine-grained token types:
- GitHub App user access tokens
- GitHub App installation access tokens
- Fine-grained personal access tokens
The fine-grained token must have the following permission set:
- "Projects" organization permissions (write)
This endpoint can be used without authentication or the aforementioned permissions if only public resources are requested.

### Parameters for "Create draft item for organization owned project"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
orgstringRequiredThe organization name. The name is not case sensitive.
project_numberintegerRequiredThe project's number.
[/TABLE]
The organization name. The name is not case sensitive.

```
project_number
```
The project's number.

[TABLE]
Name, Type, Description
titlestringRequiredThe title of the draft issue item to create in the project.
bodystringThe body content of the draft issue item to create in the project.
[/TABLE]
The title of the draft issue item to create in the project.
The body content of the draft issue item to create in the project.

### HTTP response status codes for "Create draft item for organization owned project"

[TABLE]
Status code | Description
201 | Created
304 | Not modified
401 | Requires authentication
403 | Forbidden
[/TABLE]
Created
Not modified
Requires authentication
Forbidden

## Create draft item for user owned project
Create draft issue item for the specified user owned project.

### Fine-grained access tokens for "Create draft item for user owned project"
This endpoint does not work with GitHub App user access tokens, GitHub App installation access tokens, or fine-grained personal access tokens.

### Parameters for "Create draft item for user owned project"

[TABLE]
Name, Type, Description
acceptstringSetting toapplication/vnd.github+jsonis recommended.
[/TABLE]
Setting toapplication/vnd.github+jsonis recommended.

[TABLE]
Name, Type, Description
user_idstringRequiredThe unique identifier of the user.
project_numberintegerRequiredThe project's number.
[/TABLE]
The unique identifier of the user.

```
project_number
```
The project's number.

[TABLE]
Name, Type, Description
titlestringRequiredThe title of the draft issue item to create in the project.
bodystringThe body content of the draft issue item to create in the project.
[/TABLE]
The title of the draft issue item to create in the project.
The body content of the draft issue item to create in the project.

### HTTP response status codes for "Create draft item for user owned project"

[TABLE]
Status code | Description
201 | Created
304 | Not modified
401 | Requires authentication
403 | Forbidden
[/TABLE]
Created
Not modified
Requires authentication
Forbidden