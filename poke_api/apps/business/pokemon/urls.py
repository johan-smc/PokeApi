from django.urls import path

from business.pokemon.views import PokemonViewSet

urlpatterns = [
    path(
        '<str:name>',
        PokemonViewSet.as_view({
            'get': 'get_pokemon_by_name',
        }),
        name='pokemon'
    ),
]
