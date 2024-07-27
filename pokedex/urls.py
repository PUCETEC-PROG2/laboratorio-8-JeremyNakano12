from django.urls import path

from . import views

app_name = "pokedex"
urlpatterns = [
    path("", views.index, name="index"),
    path("pokemon/<int:pokemon_id>/", views.pokemon, name="pokemon"),
    path("pokemon/edit/<int:pokemon_id>/", views.edit_pokemon, name="edit_pokemon"),
    path("pokemon/delete/<int:pokemon_id>/", views.delete_pokemon, name="delete_pokemon"),
    path("trainer/<int:trainer_id>/", views.trainer, name="trainer"),
    path("pokemon/", views.list_pokemon, name="list_pokemon"),
    path("trainer/", views.list_trainer, name="list_trainer"),
    path("pokemon/add_pokemon/", views.add_pokemon, name="add_pokemon"),
    path("login/", views.CustomLoginView.as_view(), name="login"),

]