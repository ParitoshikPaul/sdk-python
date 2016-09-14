from django.shortcuts import render

def index(request):
    return render(request, 'oauth2/login.html', {})