from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^files', views.files, name='files'),
    url(r'^metadata(?P<path>.+)', views.metadata, name='metadata'),
    url(r'^metadata', views.metadata, name='metadata'),
    url(r'^search', views.search, name='search'),
    url(r'^trash/(?P<operation>.*)', views.trash, name='empty_trash'),
    url(r'^trash', views.trash, name='trash'),
]