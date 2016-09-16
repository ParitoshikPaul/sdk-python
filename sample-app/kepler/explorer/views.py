from django.shortcuts import render

def index(request):
    return render(request, 'explorer/explorer.html', {})

def files(request):
    return render(request, 'explorer/files.html', {})