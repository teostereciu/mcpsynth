# sessionauthentication/1/overview

*Source: https://docs.adyen.com/api-explorer/sessionauthentication/1/overview*

---

# Session authentication API
The Session authentication API enables you to create and manage the JSON Web Tokens (JWT) required for integratingcomponents.

## Authentication
We recommend that you use an API key to connect to the Session authentication API. Generate an API key in your Customer Area if you have aplatform setupormarketplace setup. If you have an Adyen Issuing integration,generate an API keyin your Balance Platform Customer Area.
To connect to the Session authentication API, add anX-API-Keyheader with the API key as the value, for example:

```
curl
-H 'Content-Type: application/json' \
-H 'X-API-Key: YOUR_API_KEY' \
...
```

```
curl
-H 'Content-Type: application/json' \
-H 'X-API-Key: YOUR_API_KEY' \
...
```

## Roles and permissions
To create a token, you must meet specific requirements. These requirements vary depending on the type of component. For more information, see the documentation forOnboardingandPlatform Experiencecomponents.

## Going live
To access the live endpoint, generate an API key in your live Customer Area if you have aplatformormarketplace setup. If you have an Adyen Issuing integration,generate an API keyin your Balance Platform Customer Area. You can then use the API key to send requests tohttps://authe-live.adyen.com/authe/api/v1.