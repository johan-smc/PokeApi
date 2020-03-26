from django.test import TestCase

from business.pokemon_species.models import PokemonSpecies
from business.pokemon_species.services import create_pokemon_species


class CreatePokemonSpeciesTests(TestCase):
    """Group of tests that ensures check if a pokemon species is being created
    correctly """

    def setUp(self):
        self.data = {
            'name': 'test'
        }
        self.service = create_pokemon_species

    def test_create_pokemon_species(self):
        self.assertEqual(0, PokemonSpecies.objects.count())
        new_pokemon_species = self.service(**self.data)
        self.assertEqual(1, PokemonSpecies.objects.count())
        self.assertEqual(new_pokemon_species, PokemonSpecies.objects.first())
