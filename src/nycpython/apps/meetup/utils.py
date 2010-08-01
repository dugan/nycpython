from meetup import meetup_api_client

def get_meetup_client_for_user(user):
    access_key = user.meetup.access_key
    access_secret = user.meetup.access_secret
    return MeetupClient(user.meetup.access_key, user.meetup.access_secret)
