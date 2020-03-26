from unittest import mock

from django.core.exceptions import ValidationError
from django.test import TestCase

from business.evolution.models import ChainLink, EvolutionChain
from business.pokemon.models import Pokemon
from business.pokemon.services import create_pokemon, update_pokemon, \
    create_or_update_pokemon, create_pokemon_by_species, \
    create_pokemon_by_chain_link, fetch_pokemons_from_evolution_chain_by_id
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


class CreatePokemonBySpeciesTests(TestCase):
    """Group of tests that ensures check if a pokemon is being created
    correctly """

    def setUp(self):
        self.pokemon_species = PokemonSpecies.objects.create(name="test")
        self.data = {
            "height": 7,
            "id": 1,
            "name": "bulbasaur",
            "species": {
                "name": "bulbasaur",
            },
            "stats": [
                {
                    "base_stat": 45,
                    "effort": 0,
                    "stat": {
                        "name": "speed",
                    }
                }
            ],
            "weight": 69
        }
        self.service = create_pokemon_by_species

    @mock.patch('business.pokemon.services.get_request')
    def test_create_pokemon_by_species(self, mock_get):
        mock_get.return_value = self.data
        self.assertEqual(0, Pokemon.objects.count())
        new_pokemon = self.service(
            species=self.pokemon_species
        )
        self.assertEqual(1, Pokemon.objects.count())
        self.assertEqual(new_pokemon, Pokemon.objects.first())


class CreatePokemonByChainLink(TestCase):
    """Group of tests that ensures check if a pokemon is being created
    correctly """

    def setUp(self):
        self.pokemon_species = PokemonSpecies.objects.create(name="test")
        self.chain = ChainLink.objects.create(species=self.pokemon_species)
        self.data = {
            "height": 7,
            "id": 1,
            "name": "bulbasaur",
            "species": {
                "name": "bulbasaur",
            },
            "stats": [
                {
                    "base_stat": 45,
                    "effort": 0,
                    "stat": {
                        "name": "speed",
                    }
                }
            ],
            "weight": 69
        }
        self.service = create_pokemon_by_chain_link

    @mock.patch('business.pokemon.services.get_request')
    def test_create_pokemon_by_chain_link(self, mock_get):
        mock_get.return_value = self.data
        self.assertEqual(0, Pokemon.objects.count())
        self.service(
            chain_link=self.chain
        )
        self.assertEqual(1, Pokemon.objects.count())


class CreateFetchPokemonsFromEvolutionChainById(TestCase):
    """Group of tests that ensures check if a pokemon is being created
    correctly """

    def setUp(self):
        self.pokemon_species = PokemonSpecies.objects.create(name="test")
        self.chain = ChainLink.objects.create(species=self.pokemon_species)
        self.data = {
            'id': 1,
            'chain': self.chain
        }
        self.evolution_chain = EvolutionChain.objects.create(**self.data)
        self.data = {
            "height": 7,
            "id": 1,
            "name": "bulbasaur",
            "species": {
                "name": "bulbasaur",
            },
            "stats": [
                {
                    "base_stat": 45,
                    "effort": 0,
                    "stat": {
                        "name": "speed",
                    }
                }
            ],
            "weight": 69
        }
        self.service = fetch_pokemons_from_evolution_chain_by_id

    @mock.patch('business.pokemon.services.get_request')
    @mock.patch('business.pokemon.services.fetch_evolution_chain_from_id')
    def test_fetch_pokemons_from_evolution_chain_by_id(self, mock_evolution,
                                                       mock_get):
        mock_evolution.return_value = self.evolution_chain
        mock_get.return_value = self.data
        self.assertEqual(0, Pokemon.objects.count())
        self.service(
            id=1
        )
        self.assertEqual(1, Pokemon.objects.count())
