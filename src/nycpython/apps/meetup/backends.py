from django.contrib.auth.models import User

from nycpython.apps.meetup.models import MeetupProfile

MEETUP_USER_PREFIX = 'meetup_'

class MeetupOauthBackend(object):
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

    def authenticate(self, member, access_key, access_secret):
        id = member.id
        username = '%s%s' % (MEETUP_USER_PREFIX, member.id)

        user, created = User.objects.get_or_create(username=username)
        profile, created = MeetupProfile.objects.get_or_create(user=user)
        profile.meetup_id = member.id
        profile.name = member.name
        profile.photo_url = member.photo_url
        profile.bio = member.bio
        profile.city = member.city
        profile.state = member.state
        profile.access_key = access_key
        profile.secret_key = access_secret
        profile.save()
        return user
