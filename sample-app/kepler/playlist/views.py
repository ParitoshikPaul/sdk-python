from django.shortcuts import render, redirect
from thingspace.exceptions import UnauthorizedError
from thingspace.exceptions import CloudError
from .forms import PlaylistForm
from .forms import CreateplaylistForm

def playlist(request):
    if not request.cloud.authenticated:
        return redirect('index')

    try:
        type = request.POST.get('type')
        page = request.POST.get('page')
        count = request.POST.get('count')
        sort = request.POST.get('sort')
        account = request.cloud.account()
        playlists = request.cloud.playlists(type, page, count, sort)
        return render(request, 'playlist/playlists.html', {'playlists': playlists})
    except UnauthorizedError:
        return redirect('logout')
    except CloudError as error:
        return render(request, 'playlist/playlists.html', {error: error})

def playlist_items(request, uid):
    if not request.cloud.authenticated:
        return redirect('index')

    try:
        playlist = request.cloud.playlist(uid)
        items = request.cloud.playlist_items(uid)
        print(items)
    except UnauthorizedError:
        return redirect('logout')

    return render(request, 'playlist/playlist_items.html', {"playlist": playlist, "playlist_items": items})

def playlistform(request):

    form = PlaylistForm()
    get_account = request.cloud.account()
    return render(request, 'playlist/playlistform.html', {'form': form, 'get_account': get_account})


def createplaylistform(request):

    form = CreateplaylistForm()
    get_account = request.cloud.account()
    name = request.POST.get('name')
    paths = request.POST.get('paths')
    type = request.POST.get('type')
    createdplaylist = request.cloud.create_playlist(name, paths, type)
    return render(request, 'playlist/createplaylistform.html', {'form': form, 'get_account': get_account, 'createdplaylist': createdplaylist})

# Create your views here.
