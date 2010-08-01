from django.conf import settings

from meetup import meetup_api_client

class MeetupClient(object):
    def __init__(self, access_key, access_secret):
        self.client = meetup_api_client.MeetupOAuth(settings.MEETUP_CONSUMER_KEY, 
                                                    settings.MEETUP_CONSUMER_SECRET,
                                                    access_key=access_key, 
                                                    access_secret=access_secret)
        self.access_key = access_key
        self.access_secret = access_secret

    def get_profile(self):
        response = self.client.get_members(relation='self')
        member = response.results[0]
        return member

def get_auth_url(callback):
    client = meetup_api_client.MeetupOAuth(settings.MEETUP_CONSUMER_KEY, 
                                           settings.MEETUP_CONSUMER_SECRET)
    session = client.new_session()
    session.fetch_request_token(callback)
    authorize_url = session.get_authorize_url()
    return authorize_url, session.request_token.secret

def confirm_auth(request_key, request_secret, verifier):
    client = meetup_api_client.MeetupOAuth(settings.MEETUP_CONSUMER_KEY, 
                                           settings.MEETUP_CONSUMER_SECRET)
    session = client.new_session(request_key=request_key, request_secret=request_secret)
    session.fetch_access_token(oauth_verifier=verifier)
    return MeetupClient(session.access_token.key, session.access_token.secret)
