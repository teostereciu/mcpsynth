def create_nextcloud_talk_call(room_name):
    """Create a Nextcloud Talk video call URL."""
    request = {'room_name': room_name}
    return call_endpoint('/calls/nextcloud_talk/create', method='POST', request=request)
