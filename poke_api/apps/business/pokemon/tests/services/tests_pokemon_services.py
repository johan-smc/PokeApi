from django.core.exceptions import ValidationError
from django.test import TestCase

from business.pokemon.models import Pokemon, PokemonStat
from business.pokemon.services import create_pokemon, update_pokemon, \
    create_or_update_pokemon
from business.pokemon_species.models import PokemonSpecies
from business.stats.models import Stat


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
            'species': self.pokemon_species,
            'stats': [
                {
                    'base_stat': 45,
                    'effort': 0,
                    'stat': {
                        'name': 'speed'
                    }
                }]
        }
        self.service = create_pokemon

    def test_create_pokemon(self):
        self.assertEqual(0, Pokemon.objects.count())
        new_pokemon = self.service(**self.data)
        self.assertEqual(1, Pokemon.objects.count())
        self.assertEqual(new_pokemon, Pokemon.objects.first())


class UpdatePokemonTests(TestCase):
    """Group of tests that ensures check if a pokemon is being updated
    correctly """

    def setUp(self):
        self.pokemon_species = PokemonSpecies.objects.create(name="test")
        self.data = {
            'id': 1,
            'name': 'test',
            'height': 12,
            'weight': 13,
            'species': self.pokemon_species,
        }
        self.pokemon = Pokemon.objects.create(**self.data)
        self.data['stats'] = [
                {
                    'base_stat': 45,
                    'effort': 0,
                    'stat': {
                        'name': 'speed'
                    }
                }]
        self.service = update_pokemon

    def test_update_pokemon(self):
        self.assertEqual(1, Pokemon.objects.count())
        self.data['id'] = self.pokemon.id
        self.data['name'] = 'test2'
        now_pokemon = self.service(**self.data)
        self.assertEqual(1, Pokemon.objects.count())
        self.assertEqual(now_pokemon, Pokemon.objects.first())

    def test_update_pokemon_not_exists(self):
        self.assertEqual(1, Pokemon.objects.count())
        self.data['id'] = -1
        with self.assertRaises(ValidationError):
            self.service(**self.data)


class CreateOrUpdatePokemonTests(TestCase):
    """Group of tests that ensures check if a pokemon is being updated
    or created correctly """

    def setUp(self):
        self.pokemon_species = PokemonSpecies.objects.create(name="test")
        self.data = {
            'id': 1,
            'name': 'test',
            'height': 12,
            'weight': 13,
            'species': self.pokemon_species,
        }
        self.pokemon = Pokemon.objects.create(**self.data)
        self.data['stats'] = [
            {
                'base_stat': 45,
                'effort': 0,
                'stat': {
                    'name': 'speed'
                }
            }]
        self.service = create_or_update_pokemon

    def test_update_pokemon(self):
        self.assertEqual(1, Pokemon.objects.count())
        self.data['id'] = self.pokemon.id
        self.data['name'] = 'name2'
        now_pokemon = self.service(**self.data)
        self.assertEqual(1, Pokemon.objects.count())
        self.assertEqual(now_pokemon, Pokemon.objects.first())

    def test_create_pokemon_not_exists(self):
        self.assertEqual(1, Pokemon.objects.count())
        self.data['id'] = 2
        self.data['species'] = PokemonSpecies.objects.create(name="test2")
        self.service(**self.data)
        self.assertEqual(2, Pokemon.objects.count())
