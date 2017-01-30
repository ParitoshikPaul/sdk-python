from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^favoritesform', views.favoritesform, name='favoritesform'),
    url(r'^favorites', views.favorites, name='favorites'),
    url(r'^updatefavoritesform', views.updatefavoritesform, name='updatefavoritesform'),
    url(r'^updatefavorites', views.updatefavorites, name='updatefavorites'),
    url(r'^deletefavoritesform', views.deletefavoritesform, name='deletefavoritesform'),
    url(r'^deletefavorites', views.deletefavorites, name='deletefavorites'),
]