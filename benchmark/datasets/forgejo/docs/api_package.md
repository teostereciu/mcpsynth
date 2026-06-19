# Package

*Source: https://codeberg.org/swagger.v1.json*

---

### GET `/packages/{owner}`

**Gets all packages of an owner**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the packages
  - `page` [query] *integer*: page number of results to return (1-based)
  - `limit` [query] *integer*: page size of results
  - `type` [query] *string*: package type filter
  - `q` [query] *string*: name filter

**Responses:**
  - `200`: 
  - `404`: 

### POST `/packages/{owner}/{type}/{name}/-/link/{repo_name}`

**Link a package to a repository**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the package
  - `type` [path] (required) *string*: type of the package
  - `name` [path] (required) *string*: name of the package
  - `repo_name` [path] (required) *string*: name of the repository to link.

**Responses:**
  - `201`: 
  - `404`: 

### POST `/packages/{owner}/{type}/{name}/-/unlink`

**Unlink a package from a repository**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the package
  - `type` [path] (required) *string*: type of the package
  - `name` [path] (required) *string*: name of the package

**Responses:**
  - `201`: 
  - `404`: 

### DELETE `/packages/{owner}/{type}/{name}/{version}`

**Delete a package**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the package
  - `type` [path] (required) *string*: type of the package
  - `name` [path] (required) *string*: name of the package
  - `version` [path] (required) *string*: version of the package

**Responses:**
  - `204`: 
  - `404`: 

### GET `/packages/{owner}/{type}/{name}/{version}`

**Gets a package**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the package
  - `type` [path] (required) *string*: type of the package
  - `name` [path] (required) *string*: name of the package
  - `version` [path] (required) *string*: version of the package

**Responses:**
  - `200`: 
  - `404`: 

### GET `/packages/{owner}/{type}/{name}/{version}/files`

**Gets all files of a package**

**Parameters:**
  - `owner` [path] (required) *string*: owner of the package
  - `type` [path] (required) *string*: type of the package
  - `name` [path] (required) *string*: name of the package
  - `version` [path] (required) *string*: version of the package

**Responses:**
  - `200`: 
  - `404`: 
