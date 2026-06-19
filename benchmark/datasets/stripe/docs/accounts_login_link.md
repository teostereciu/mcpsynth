# accounts/login_link

*Source: https://docs.stripe.com/api/accounts/login_link*

---

# Login Links
Login Links are single-use URLs that takes an Express account to the login page for their Stripe dashboard.A Login Link differs from anAccount Linkin that it takes the user directly to theirExpress dashboard for the specified account

# The Login Link object

### Attributes
- urlstringThe URL for the login link.

#### urlstring

### More attributesExpand all
- objectstring
- createdtimestamp

#### objectstring

#### createdtimestamp

```
{"object":"login_link","created":1686084879,"url":"https://connect.stripe.com/express/acct_1032D82eZvKYlo2C/F44eiGHh5sEV"}
```

```
{"object":"login_link","created":1686084879,"url":"https://connect.stripe.com/express/acct_1032D82eZvKYlo2C/F44eiGHh5sEV"}
```

# Create a login link
Creates a login link for a connected account to access the Express Dashboard.
You can only create login links for accounts that use theExpress Dashboardand are connected to your platform.

### Parameters
Noparameters.

### Returns
Returns a login link object if the call succeeded.

```
curl-X POST https://api.stripe.com/v1/accounts/acct_1032D82eZvKYlo2C/login_links \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
curl-X POST https://api.stripe.com/v1/accounts/acct_1032D82eZvKYlo2C/login_links \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
{"object":"login_link","created":1686084879,"url":"https://connect.stripe.com/express/acct_1032D82eZvKYlo2C/F44eiGHh5sEV"}
```

```
{"object":"login_link","created":1686084879,"url":"https://connect.stripe.com/express/acct_1032D82eZvKYlo2C/F44eiGHh5sEV"}
```