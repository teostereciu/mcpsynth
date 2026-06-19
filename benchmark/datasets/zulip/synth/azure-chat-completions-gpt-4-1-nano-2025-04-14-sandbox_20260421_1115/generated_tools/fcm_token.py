def add_android_gcm_reg_id(token):
    """Add an Android GCM registration token for push notifications."""
    request = {'token': token}
    return call_endpoint('/users/me/android_gcm_reg_id', method='POST', request=request)
