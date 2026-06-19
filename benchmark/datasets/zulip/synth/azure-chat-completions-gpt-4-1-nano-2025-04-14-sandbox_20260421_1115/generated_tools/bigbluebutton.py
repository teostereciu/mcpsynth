def create_bigbluebutton_call(meeting_name, voice_only=False):
    """Create a BigBlueButton video call URL."""
    request = {'meeting_name': meeting_name, 'voice_only': voice_only}
    return call_endpoint('/calls/bigbluebutton/create', method='GET', request=request)
