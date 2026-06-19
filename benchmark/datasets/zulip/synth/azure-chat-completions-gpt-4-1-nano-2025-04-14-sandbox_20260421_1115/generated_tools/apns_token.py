def add_apns_device_token(token, appid='org.zulip.Zulip'):
    """Add an APNs device token for push notifications."""
    request = {'token': token, 'appid': appid}
    return call_endpoint('/users/me/apns_device_token', method='POST', request=request)
