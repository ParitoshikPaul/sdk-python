from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^token', views.token, name='token'),
    url(r'^refresh', views.refresh, name='refresh'),
    url(r'^logout', views.logout, name='logout'),
    url(r'^invalidate_access_token', views.invalidate_access_token, name='invalidate_access_token'),
]