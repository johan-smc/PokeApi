from django.test import TestCase

from business.pokemon.models import PokemonStat, Pokemon
from business.pokemon.services import create_pokemon_stat
from business.pokemon_species.models import PokemonSpecies


class CreatePokemonStatTests(TestCase):
    """Group of tests that ensures check if a pokemon stat is being created
    correctly """

    def setUp(self):
        self.pokemon_species = PokemonSpecies.objects.create(name="test")
        self.pokemon = Pokemon.objects.create(
            id=1,
            name='test',
            height=12,
            weight=1,
            species=self.pokemon_species
        )
        self.data = {
            'base_stat': 1,
            'effort': 2,
            'pokemon': self.pokemon,
            'stat': {
                'name': 'test'
            }
        }
        self.service = create_pokemon_stat

    def test_create_pokemon_stat(self):
        self.assertEqual(0, PokemonStat.objects.count())
        new_pokemon_stat = self.service(**self.data)
        self.assertEqual(1, PokemonStat.objects.count())
        self.assertEqual(new_pokemon_stat, PokemonStat.objects.first())
