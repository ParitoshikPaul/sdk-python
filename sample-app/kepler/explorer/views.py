from django.shortcuts import render, redirect
from thingspace.exceptions import UnauthorizedError
from thingspace.exceptions import CloudError
from .forms import PlaylistForm
from .forms import CreateplaylistForm

def files(request):
    if not request.cloud.authenticated:
        return redirect('index')

    try:
        account = request.cloud.account()
        files, empty_folders, etag, deleted = request.cloud.fullview()
        return render(request, 'explorer/files.html', {'files': files, 'account': account})
    except UnauthorizedError:
        return redirect('logout')
    except CloudError as error:
        return render(request, 'explorer/files.html', {error: error})


def search(request):
    if not request.cloud.authenticated:
        return redirect('index')

    query = request.GET.get('query', None)

    if not query:
        return render(request, 'explorer/search.html', {})

    try:
        files, folders = request.cloud.search(query='name:' + query)
        return render(request, 'explorer/search.html', {'files': files, 'folders': folders})
    except UnauthorizedError:
        return redirect('logout')
    except CloudError as error:
        return render(request, 'explorer/search.html', {error: error})


def metadata(request, path='/'):
    if not request.cloud.authenticated:
        return redirect('index')


    #build the bread crumbs
    if path == '/':
        breadcrumbs = [{'name': '/', 'url': ''}]
    else:
        path_tokens = path.split('/')
        breadcrumbs = []
        for index, path_token in enumerate(path_tokens):
            if index == 0:
                breadcrumbs.append({'name': '/', 'url': ''})
            else:
                breadcrumbs.append({'name': path_token, 'url': breadcrumbs[index - 1]['url'] + '/' + path_token})

    try:
        files, folders = request.cloud.metadata(path=path)
        return render(request, 'explorer/explorer.html', {'files': files, 'folders': folders, 'breadcrumbs': breadcrumbs})
    except UnauthorizedError:
        return redirect('logout')
    except CloudError as error:
        return render(request, 'explorer/explorer.html', {error: error})


def trash(request, operation=None):
    if not request.cloud.authenticated:
        return redirect('index')

    try:
        if operation == 'empty':
            request.cloud.empty_trash()
        elif operation == 'restore':
            request.cloud.restore(request.POST['path'])
        files, folders = request.cloud.trash()
        return render(request, 'explorer/trash.html', {'files': files, 'folders': folders})

    except UnauthorizedError:
        return redirect('logout')
    except CloudError as error:
        return render(request, 'explorer/trash.html', {error: error})

def playlist(request):
    if not request.cloud.authenticated:
        return redirect('index')

    try:
        playlists = request.cloud.playlists()
        return render(request, 'explorer/playlists.html', {'playlists': playlists})
    except UnauthorizedError:
        return redirect('logout')
    except CloudError as error:
        return render(request, 'explorer/playlists.html', {error: error})

def playlist_items(request, uid):
    if not request.cloud.authenticated:
        return redirect('index')

    try:
        playlist = request.cloud.playlist(uid)
        items = request.cloud.playlist_items(uid)
        print(items)
    except UnauthorizedError:
        return redirect('logout')

    return render(request, 'explorer/playlist_items.html', {"playlist": playlist, "playlist_items": items})

def playlistform(request):

    form = PlaylistForm()
    get_account = request.cloud.account()
    return render(request, 'explorer/playlistform.html', {'form': form, 'get_account': get_account})


def createplaylistform(request):

    form = CreateplaylistForm()
    get_account = request.cloud.account()
    name = request.POST.get('name')
    paths = request.POST.get('paths')
    type = request.POST.get('type')
    createdplaylist = request.cloud.create_playlist(name, paths, type)
    return render(request, 'explorer/createplaylistform.html', {'form': form, 'get_account': get_account, 'createdplaylist': createdplaylist})



