from django.shortcuts import render, redirect


def index(request):

    if request.cloud.authenticated:
        return redirect('files')

    args = {'cloud': request.cloud}
    return render(request, 'oauth2/login.html', args)


def token(request):
    token_response = request.cloud.token(request.GET.get('code'))
    print(token_response)

    request.session['auth_token'] = token_response.get('access_token')
    request.session['refresh_token'] = token_response.get('refresh_token')

    return redirect('files')


def logout(request):
    request.session.flush()
    return redirect(index)
