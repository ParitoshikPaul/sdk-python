from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^authenticate/', views.authenticate, name='authenticate'),
    url(r'^accountusage/', views.accountusage, name='accountusage'),
    url(r'^fops/', views.upload_intent, name='uploadintent'),
    url(r'^fullview/', views.fullview, name='fullview'),
    url(r'^workon/(?P<filename>.*?)$', views.workon, name='workon'),
]
