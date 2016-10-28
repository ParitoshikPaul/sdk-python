from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import render,redirect
from django.template import loader
from thingspace.auth import auth
from thingspace.fops import fops
from thingspace.account import account
from hashlib import sha256
#from thingspace.account import account

def index(request):
    auth_object = auth()

    auth_object.set_config_data(settings.CLIENT_KEY, settings.CLIENT_SECRET,
                                settings.REDIRECT_URI, settings.AUTH_URL,
                                settings.API_URL, settings.VERSION)
    if request.GET.get('code'):
        auth_data = auth_object.token(request.GET.get('code'))
        #return HttpResponse(str(auth_data))
        request.session['access_token'] = auth_data['data']['access_token']
        request.session['refresh_token'] = auth_data['data']['refresh_token']
        request.session['expires_in'] = auth_data['data']['expires_in']
        #return HttpResponse(str(auth_object.token(request.GET.get('code'))))

    if not request.session.get('access_token'):
        return authenticate(request)
    #return HttpResponse(str(request.session.get('access_token')))
    account_object = account(request.session.get('access_token'),
                             settings.API_URL + settings.VERSION +
                             '/account')
    account_info = account_object.getaccount()
    if account_info['http_status'] is not 200:
        #Token is expired
        del request.session['access_token']
        refresh_data = auth_object.refreshToken(request.session.get('refresh_token'))
        if refresh_data['http_status'] is not 200:
            self.authenticate(request)
        request.session['access_token'] = refresh_data['access_token']
        request.session['refresh_token'] = refresh_data['refresh_token']
        request.session['expires_in'] = refresh_data['expires_in']
        account_object = account(request.session.get('access_token'),
                                 settings.API_URL + settings.VERSION +
                                 '/account')
        account_info = account_object.getaccount()


    context = {
        'account': account_info,
    }
    #return HttpResponse(str(account_info))

    return render(request, 'dashboard.html', context)

def accountusage(request):
    if not request.session.get('access_token'):
        return authenticate(request)

    account_object = account(request.session.get('access_token'),
                             settings.API_URL + settings.VERSION +
                             '/account')
    account_info = account_object.getaccount()
    context = {
        'account': account_info,
    }
    #return HttpResponse(str(context))
    return render(request, 'account.html', context)


def upload_intent(request):
    if not request.session.get('access_token'):
        return authenticate(request)

    fops_object = fops(request.session.get('access_token'), settings.API_URL +
                       settings.VERSION)

    upload_intent = fops_object.get_fileupload_intent('/test', 'test.txt', 1024,
                                               sha256('null'))
    context = {
        'file_upload': str(upload_intent),
    }
    return render(request, 'fops.html', context)

def fullview(request):
    if not request.session.get('access_token'):
        return authenticate(request)

    fops_object = fops(request.session.get('access_token'), settings.API_URL +
                       settings.VERSION)

    fullview = fops_object.fullview()
    context = {
        'fullview':  fullview
    }
    #return HttpResponse(str(context['fullview']['data']))
    return render(request, 'fullview.html', context)

def authenticate(request):
    auth_object = auth()
    auth_object.set_config_data(settings.CLIENT_KEY, settings.CLIENT_SECRET,
                                settings.REDIRECT_URI, settings.AUTH_URL,
                                settings.API_URL, settings.VERSION)
    return redirect(auth_object.authorize())
    #return HttpResponse(auth_object.authorize())

def workon(request, filename):
    fops_object = fops(request.session.get('access_token'), settings.API_URL +
                       settings.VERSION)
    fileview  = fops_object.fileview()
    context = {
        'fileview': fileview
    }
    return render(request, 'fileview.html', context)
# Create your views here.
