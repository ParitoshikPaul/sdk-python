#from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import render,redirect
from django.template import loader
from thingspace.auth import auth

def index(request):
    auth_object = auth()

    auth_object.set_config_data(settings.CLIENT_KEY, settings.CLIENT_SECRET,
                                settings.REDIRECT_URI, settings.AUTH_URL,
                                settings.API_URL, settings.VERSION)
    if request.GET.get('code'):
        return auth_object.token(request.GET.get('code'))
    else:
        render(request, 'test.html')

def authenticate(request):
    auth_object = auth()
    auth_object.set_config_data(settings.CLIENT_KEY, settings.CLIENT_SECRET,
                                settings.REDIRECT_URI, settings.AUTH_URL,
                                settings.API_URL, settings.VERSION)
    return redirect(auth_object.authorize())
    #return HttpResponse(auth_object.authorize())
# Create your views here.
