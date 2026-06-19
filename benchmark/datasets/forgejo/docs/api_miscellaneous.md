# Miscellaneous

*Source: https://codeberg.org/swagger.v1.json*

---

### GET `/gitignore/templates`

**Returns a list of all gitignore templates**

**Responses:**
  - `200`: 

### GET `/gitignore/templates/{name}`

**Returns information about a gitignore template**

**Parameters:**
  - `name` [path] (required) *string*: name of the template

**Responses:**
  - `200`: 
  - `404`: 

### GET `/label/templates`

**Returns a list of all label templates**

**Responses:**
  - `200`: 

### GET `/label/templates/{name}`

**Returns all labels in a template**

**Parameters:**
  - `name` [path] (required) *string*: name of the template

**Responses:**
  - `200`: 
  - `404`: 

### GET `/licenses`

**Returns a list of all license templates**

**Responses:**
  - `200`: 

### GET `/licenses/{name}`

**Returns information about a license template**

**Parameters:**
  - `name` [path] (required) *string*: name of the license

**Responses:**
  - `200`: 
  - `404`: 

### POST `/markdown`

**Render a markdown document as HTML**

**Parameters:**
  - `body` [body] *any*: 

**Request body** (`body`): 

**Responses:**
  - `200`: 
  - `422`: 

### POST `/markdown/raw`

**Render raw markdown as HTML**

**Parameters:**
  - `body` [body] (required) *string*: Request body to render

**Request body** (`body`): Request body to render

**Responses:**
  - `200`: 
  - `422`: 

### POST `/markup`

**Render a markup document as HTML**

**Parameters:**
  - `body` [body] *any*: 

**Request body** (`body`): 

**Responses:**
  - `200`: 
  - `422`: 

### GET `/nodeinfo`

**Returns the nodeinfo of the Forgejo application**

**Responses:**
  - `200`: 

### GET `/signing-key.gpg`

**Get default signing-key.gpg**

**Responses:**
  - `200`: GPG armored public key

### GET `/signing-key.ssh`

**Get default signing-key.ssh**

**Responses:**
  - `200`: SSH public key in OpenSSH authorized key format
  - `404`: 

### GET `/version`

**Returns the version of the running application**

**Responses:**
  - `200`: 
