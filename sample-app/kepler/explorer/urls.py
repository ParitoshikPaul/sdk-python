from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^files', views.files, name='files'),
]