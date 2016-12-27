from django.shortcuts import render, redirect
from thingspace.exceptions import UnauthorizedError
from thingspace.exceptions import CloudError
from .forms import ContactsForm

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

def contacts_form(request):

    form = ContactsForm()
    get_account = request.cloud.account()
    return render(request, 'explorer/contactsform.html', {'form': form, 'get_account': get_account})

def contacts(request):

    if not request.cloud.authenticated:
        return redirect('index')

    try:
        page = request.POST.get('page')
        count = request.POST.get('count')
        sort = request.POST.get('sort')
        account = request.cloud.account()
        contacts = request.cloud.contacts(page, count, sort)
        return render(request, 'explorer/contacts.html', {'contacts': contacts})
    except UnauthorizedError:
        return redirect('logout')
    except CloudError as error:
        return render(request, 'explorer/contacts.html', {error: error})

    return



