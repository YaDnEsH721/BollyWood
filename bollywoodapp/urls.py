from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('create_game', views.create_game, name="create_game"),
    path('create_room', views.create_room, name="create_room"),
    path('join_game', views.join_game, name="join_game"),
]