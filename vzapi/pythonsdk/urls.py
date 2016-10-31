from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^authenticate/', views.authenticate, name='authenticate'),
    url(r'^accountusage/', views.accountusage, name='accountusage'),
    url(r'^fops/', views.upload_intent, name='uploadintent'),
    url(r'^fullview/', views.fullview, name='fullview'),
    url(r'^workon/(?P<filename>.*?)$', views.workon, name='workon'),
    url(r'^newfileview/(?P<filename>.*?)$', views.newfileview,
        name='newfileview'),
    url(r'^getfile/(?P<filename>.*?)$', views.getfile, name='getfile'),
    url(r'^trash/(?P<virtualfolder>.*?)$', views.trash, name='gettrash')
]
