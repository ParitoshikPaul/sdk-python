from django.shortcuts import render, redirect
from thingspace.exceptions import UnauthorizedError
from thingspace.exceptions import CloudError
from .forms import FavoritesForm
from .forms import UpdateFavoritesForm
from .forms import DeleteFavoritesForm


def favoritesform(request):

    form = FavoritesForm()
    get_account = request.cloud.account()
    return render(request, 'favorites/favoritesform.html', {'form': form, 'get_account': get_account})

def favorites(request):
    if not request.cloud.authenticated:
        return redirect('index')

    try:
        virtualfolder = request.POST.get('virtualfolder')
        type = request.POST.get('type')
        filetype = request.POST.get('filetype')
        favorites = request.cloud.favorites(virtualfolder, type, filetype)
        return render(request, 'favorites/favorites.html', {'favorites': favorites})
    except UnauthorizedError:
        return redirect('logout')
    except CloudError as error:
        return render(request, 'favorites/favorites.html', {error: error})

def updatefavoritesform(request):

    form = UpdateFavoritesForm()
    get_account = request.cloud.account()
    return render(request, 'favorites/updatefavoritesform.html', {'form': form, 'get_account': get_account})

def updatefavorites(request):
    if not request.cloud.authenticated:
        return redirect('index')

    try:
        uri = request.POST.get('uri')
        createversion = request.POST.get('createversion')
        updated = request.cloud.updatefavorites(uri, createversion)
        return render(request, 'favorites/updatefavorites.html', {'updated': updated})
    except UnauthorizedError:
        return redirect('logout')
    except CloudError as error:
        return render(request, 'favorites/updatefavorites.html', {error: error})

def deletefavoritesform(request):

    form = DeleteFavoritesForm()
    get_account = request.cloud.account()
    return render(request, 'favorites/deletefavoritesform.html', {'form': form, 'get_account': get_account})

def deletefavorites(request):
    if not request.cloud.authenticated:
        return redirect('index')

    try:
        uri = request.POST.get('uri')
        createversion = request.POST.get('createversion')
        deleted = request.cloud.deletefavorites(uri, createversion)
        return render(request, 'favorites/deletefavorites.html', {'deleted': deleted})
    except UnauthorizedError:
        return redirect('logout')
    except CloudError as error:
        return render(request, 'favorites/deletefavorites.html', {error: error})
