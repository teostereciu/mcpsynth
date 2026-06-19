def add_alert_words(words):
    """Add alert words to the current user."""
    request = {'alert_words': words}
    return call_endpoint('/users/me/alert_words', method='POST', request=request)
