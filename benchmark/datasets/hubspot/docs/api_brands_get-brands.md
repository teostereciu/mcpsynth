# Retrieve brands by associated user

*Source: https://developers.hubspot.com/docs/api-reference/legacy/account/brands/get-brands*

---

Brands

# Retrieve brands by associated user

Retrieve the brands that a specific user can access.

GET

/

business-units

/

v3

/

business-units

/

user

/

{userId}

Try it

Retrieve brands by associated user

cURL


    curl --request GET \
      --url https://api.hubapi.com/business-units/v3/business-units/user/{userId} \
      --header 'Authorization: Bearer <token>'

200

default


    {
      "results": [
        {
          "id": "<string>",
          "name": "<string>",
          "logoMetadata": {
            "logoAltText": "<string>",
            "logoUrl": "<string>",
            "resizedUrl": "<string>"
          }
        }
      ]
    }

Supported products

Required Scopes

#### Authorizations

oauth2private_appsoauth2private_apps

​

Authorization

string

header

required

The access token received from the authorization server in the OAuth 2.0 flow.

#### Path Parameters

​

userId

string

required

#### Query Parameters

​

name

string[]

​

properties

string[]

#### Response

200

application/json

successful operation

​

results

object[]

required

The collection of Business Units

Show child attributes

Last modified on March 30, 2026

Was this page helpful?

YesNo

⌘I

[facebook](https://www.facebook.com/hubspot)[instagram](https://www.instagram.com/hubspot)[youtube](https://youtube.com/user/HubSpot)[x](https://x.com/HubSpot)[linkedin](https://www.linkedin.com/company/hubspot)[medium](https://medium.com/@HubSpot)