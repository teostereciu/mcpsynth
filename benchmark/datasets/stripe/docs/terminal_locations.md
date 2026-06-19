# terminal/locations

*Source: https://docs.stripe.com/api/terminal/locations*

---

# Location
A Location represents a grouping of readers.
Related guide:Fleet management

# The Location object

### Attributes
- idstringUnique identifier for the object.
- addressobjectThe full address of the location.Show child attributes
- display_namestringThe display name of the location.
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format.

#### idstring

#### addressobject

#### display_namestring

#### metadataobject

### More attributesExpand all
- objectstring
- address_kananullableobjectPreview feature
- address_kanjinullableobjectPreview feature
- configuration_overridesnullablestring
- display_name_kananullablestringPreview feature
- display_name_kanjinullablestringPreview feature
- livemodeboolean
- phonenullablestringPreview feature

#### objectstring

#### address_kananullableobjectPreview feature

#### address_kanjinullableobjectPreview feature

#### configuration_overridesnullablestring

#### display_name_kananullablestringPreview feature

#### display_name_kanjinullablestringPreview feature

#### livemodeboolean

#### phonenullablestringPreview feature

```
{"id":"tml_FBakXQG8bQk4Mm","object":"terminal.location","address":{"city":"San Francisco","country":"US","line1":"1234 Main Street","line2":"","postal_code":"94111","state":"CA"},"display_name":"My First Store","livemode":false,"metadata":{}}
```

```
{"id":"tml_FBakXQG8bQk4Mm","object":"terminal.location","address":{"city":"San Francisco","country":"US","line1":"1234 Main Street","line2":"","postal_code":"94111","state":"CA"},"display_name":"My First Store","livemode":false,"metadata":{}}
```

# Create a Location
Creates a newLocationobject.For further details, including which address fields are required in each country, see theManage locationsguide.

### Parameters
- addressobjectThe full address of the location.Show child parameters
- display_namestringA name for the location. Maximum length is 1000 characters.
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value tometadata.

#### addressobject

#### display_namestring

#### metadataobject

### More parametersExpand all
- address_kanaobjectPreview feature
- address_kanjiobjectPreview feature
- configuration_overridesstring
- display_name_kanastringPreview feature
- display_name_kanjistringPreview feature
- phonestringPreview feature

#### address_kanaobjectPreview feature

#### address_kanjiobjectPreview feature

#### configuration_overridesstring

#### display_name_kanastringPreview feature

#### display_name_kanjistringPreview feature

#### phonestringPreview feature

### Returns
Returns aLocationobject if creation succeeds.

```
curlhttps://api.stripe.com/v1/terminal/locations \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d display_name="My First Store"\-d"address[line1]"="1234 Main Street"\-d"address[city]"="San Francisco"\-d"address[postal_code]"=94111 \-d"address[state]"=CA \-d"address[country]"=US
```

```
curlhttps://api.stripe.com/v1/terminal/locations \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d display_name="My First Store"\-d"address[line1]"="1234 Main Street"\-d"address[city]"="San Francisco"\-d"address[postal_code]"=94111 \-d"address[state]"=CA \-d"address[country]"=US
```

```
{"id":"tml_FBakXQG8bQk4Mm","object":"terminal.location","address":{"city":"San Francisco","country":"US","line1":"1234 Main Street","line2":"","postal_code":"94111","state":"CA"},"display_name":"My First Store","livemode":false,"metadata":{}}
```

```
{"id":"tml_FBakXQG8bQk4Mm","object":"terminal.location","address":{"city":"San Francisco","country":"US","line1":"1234 Main Street","line2":"","postal_code":"94111","state":"CA"},"display_name":"My First Store","livemode":false,"metadata":{}}
```

# Update a Location
Updates aLocationobject by setting the values of the parameters passed. Any parameters not provided will be left unchanged.

### Parameters
- addressobjectThe full address of the location. You can’t change the location’scountry. If you need to modify thecountryfield, create a newLocationobject and re-register any existing readers to that location.Show child parameters
- display_namestringA name for the location.
- metadataobjectSet ofkey-value pairsthat you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value tometadata.

#### addressobject

#### display_namestring

#### metadataobject

### More parametersExpand all
- address_kanaobjectPreview feature
- address_kanjiobjectPreview feature
- configuration_overridesstring
- display_name_kanastringPreview feature
- display_name_kanjistringPreview feature
- phonestringPreview feature

#### address_kanaobjectPreview feature

#### address_kanjiobjectPreview feature

#### configuration_overridesstring

#### display_name_kanastringPreview feature

#### display_name_kanjistringPreview feature

#### phonestringPreview feature

### Returns
Returns an updatedLocationobject if a valid identifier was provided.

```
curlhttps://api.stripe.com/v1/terminal/locations/tml_FBakXQG8bQk4Mm \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d display_name="Update Store Name"
```

```
curlhttps://api.stripe.com/v1/terminal/locations/tml_FBakXQG8bQk4Mm \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"\-d display_name="Update Store Name"
```

```
{"id":"tml_FBakXQG8bQk4Mm","object":"terminal.location","address":{"city":"San Francisco","country":"US","line1":"1234 Main Street","line2":"","postal_code":"94111","state":"CA"},"display_name":"Update Store Name","livemode":false,"metadata":{}}
```

```
{"id":"tml_FBakXQG8bQk4Mm","object":"terminal.location","address":{"city":"San Francisco","country":"US","line1":"1234 Main Street","line2":"","postal_code":"94111","state":"CA"},"display_name":"Update Store Name","livemode":false,"metadata":{}}
```

# Retrieve a Location
Retrieves aLocationobject.

### Parameters
Noparameters.

### Returns
Returns aLocationobject if a valid identifier was provided.

```
curlhttps://api.stripe.com/v1/terminal/locations/tml_FBakXQG8bQk4Mm \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
curlhttps://api.stripe.com/v1/terminal/locations/tml_FBakXQG8bQk4Mm \-u"sk_test_Gx4mWEg...4DYMUIqfIrszsk_test_Gx4mWEgHtCMr4DYMUIqfIrsz:"
```

```
{"id":"tml_FBakXQG8bQk4Mm","object":"terminal.location","address":{"city":"San Francisco","country":"US","line1":"1234 Main Street","line2":"","postal_code":"94111","state":"CA"},"display_name":"My First Store","livemode":false,"metadata":{}}
```

```
{"id":"tml_FBakXQG8bQk4Mm","object":"terminal.location","address":{"city":"San Francisco","country":"US","line1":"1234 Main Street","line2":"","postal_code":"94111","state":"CA"},"display_name":"My First Store","livemode":false,"metadata":{}}
```