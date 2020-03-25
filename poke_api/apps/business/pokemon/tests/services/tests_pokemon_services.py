from django.test import TestCase

from business.pokemon.models import Pokemon
from business.pokemon.services import create_pokemon
from business.pokemon_species.models import PokemonSpecies


class CreatePokemonTests(TestCase):
    """Group of tests that ensures check if a pokemon is being created
    correctly """

    def setUp(self):
        self.pokemon_species = PokemonSpecies.objects.create(name="test")
        self.data = {
            'id': 1,
            'name': 'test',
            'height': 12,
            'weight': 13,
            'species': self.pokemon_species
        }
        self.service = create_pokemon

    def test_create_pokemon(self):
        self.assertEqual(0, Pokemon.objects.count())
        new_pokemon = self.service(**self.data)
        self.assertEqual(1, Pokemon.objects.count())
        self.assertEqual(new_pokemon, Pokemon.objects.first())
