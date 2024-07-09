from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("pokemon/<int:pokemon_id>/", views.pokemon, name="pokemon"),
    path("trainer/<int:trainer_id>/", views.trainer, name="trainer"),
    path("pokemon/", views.list_pokemon, name="list_pokemon"),
    path("trainer/", views.list_trainer, name="list_trainer"),
]