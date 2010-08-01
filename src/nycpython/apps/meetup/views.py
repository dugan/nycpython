from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate

from nycpython.apps.meetup.client import get_auth_url, confirm_auth

from nycpython.lib.decorators import render_to

@render_to('meetup/login.html')
def begin_login(request):
    authorize_url, request_secret = get_auth_url('http://' + request.META['HTTP_HOST'] + '/meetup/confirm/')
    request.session['request_secret'] = request_secret
    return {'authorize_url' : authorize_url }

def confirm(request):
    request_key = request.GET['oauth_token']
    request_secret = request.session['request_secret']
    verifier =  request.GET['oauth_verifier']
    client = confirm_auth(request_key, request_secret, verifier)
    member = client.get_profile()
    user = authenticate(member=member, access_key=client.access_key, access_secret=client.access_secret)
    if not user.is_anonymous():
        login(request, user)
    return HttpResponseRedirect('/')

def logout(request):
    from django.contrib.auth import logout
    logout(request)
    return HttpResponseRedirect('/')


@render_to('meetup/test.html')
def test(request):
    import epdb
    epdb.st()
    client = request.user.meetup.get_client()
    member = client.get_profile()
    return {'member' : member }
