from django.shortcuts import render, redirect


def files(request):

    if not request.cloud.authenticated:
        return redirect('index')

    fullview = request.cloud.fullview()
    print(fullview)

    return render(request, 'explorer/files.html', {'fullview' : fullview})